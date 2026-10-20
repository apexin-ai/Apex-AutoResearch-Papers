# Research conversation: In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/, I need to find the 8

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 1
- **Tool calls:** 31
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a2dc3436d334616ab.jsonl`
- **Structured JSON:** [`e9225e4d17394e7afcf2.json`](../../sessions/e9/e9225e4d17394e7afcf2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

81 recorded events

### User

_source line 1 · 2026-05-15T19:58:05.175Z_

In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/, I need to find the 8B model SCS inference results for both SciERC and CoNLL2003 (the baselines for comparing against the 4B scale ablation). 

Search the registry.yaml file for experiments with "8b" or "mvp" or "scs" in their exp_id that are DONE and have SciERC or CoNLL results. Report:
1. The experiment IDs
2. Their key metrics: greedy_f1, oracle_f1, SJ_rho, FK_rho, LP_rho (both full and conditional if available)
3. The model used and checkpoint

Also check the experiments.tex file at docs/paper/sections/experiments.tex for the official numbers used in the paper tables (Table 2 and Table 3 for 8B results).

Keep the response concise — just the numbers I need for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "b826808f-7f49-4259-8108-15c1e7fe57a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-15T19:58:06.542Z_

I'll search for the 8B model SCS inference results in the registry and the paper's experiments section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b826808f-7f49-4259-8108-15c1e7fe57a6",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wopru6xKzanGLZh7sH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e215b164-8925-4658-879f-69c97d0d6f8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011vPpcNZDdbfecBkLCeVfUt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20848,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20848,
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

_source line 3 · 2026-05-15T19:58:06.760Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rr38CjqSWxooAFVQQSaCj9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e215b164-8925-4658-879f-69c97d0d6f8f",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wopru6xKzanGLZh7sH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8f9821c6-bd19-4b9f-8097-454ef90b1139",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011vPpcNZDdbfecBkLCeVfUt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20848,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20848,
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

_source line 4 · 2026-05-15T19:58:06.772Z_

<details><summary>↩ Tool result · reported error · `toolu_01Rr38CjqSWxooAFVQQSaCj9`</summary>

```text
EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f9821c6-bd19-4b9f-8097-454ef90b1139",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "7ee57e12-a4a5-4aef-a015-fb42a5b76f1d",
  "toolUseResult": "Error: EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie'",
  "sourceToolAssistantUUID": "8f9821c6-bd19-4b9f-8097-454ef90b1139",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:58:06.993Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RKNpMErr2VuSjZfBcJ9cdF`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"registry.yaml\" -o -name \"experiments.tex\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ee57e12-a4a5-4aef-a015-fb42a5b76f1d",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wopru6xKzanGLZh7sH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "34d38cc7-5183-4a26-b0cc-3fb19899d2be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011vPpcNZDdbfecBkLCeVfUt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20848,
      "cache_read_input_tokens": 0,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 20848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20848,
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

_source line 6 · 2026-05-15T19:58:07.181Z_

<details><summary>↩ Tool result · `toolu_01RKNpMErr2VuSjZfBcJ9cdF`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34d38cc7-5183-4a26-b0cc-3fb19899d2be",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "b18169b9-5249-465a-9431-353fb8e62765",
  "sourceToolAssistantUUID": "34d38cc7-5183-4a26-b0cc-3fb19899d2be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-15T19:58:08.342Z_

Now let me read the registry.yaml and experiments.tex files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b18169b9-5249-465a-9431-353fb8e62765",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4woy5GFzv1WWKJGh5S4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd301d82-5054-4218-af45-62ad35f3feaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S4azskCi5tQPPxPm8Y4LyL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1241,
      "cache_read_input_tokens": 20848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1241,
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

_source line 8 · 2026-05-15T19:58:08.557Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WiVcMuSq3qsu9yECK24Fm8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd301d82-5054-4218-af45-62ad35f3feaa",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4woy5GFzv1WWKJGh5S4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ef78cc89-caef-4fc1-aca0-1f95029bacb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S4azskCi5tQPPxPm8Y4LyL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1241,
      "cache_read_input_tokens": 20848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1241,
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

_source line 9 · 2026-05-15T19:58:08.731Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LA4DUzWWva5MxJSrJGM94d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef78cc89-caef-4fc1-aca0-1f95029bacb4",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4woy5GFzv1WWKJGh5S4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ba980f74-e709-42a3-aa3f-441c23777aed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S4azskCi5tQPPxPm8Y4LyL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1241,
      "cache_read_input_tokens": 20848,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1241
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 174,
          "cache_read_input_tokens": 20848,
          "cache_creation_input_tokens": 1241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1241,
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

_source line 10 · 2026-05-15T19:58:08.738Z_

<details><summary>↩ Tool result · `toolu_01LA4DUzWWva5MxJSrJGM94d`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N$-scaling analysis (Appendix~\ref{app:n_scaling}) shows sublinear gains beyond $N{=}8$; 3-seed stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirms identical signal rankings across seeds.}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best per column in \textbf{bold}. SciERC: joint NER (6 types) and RE (7 types, preliminary); CoNLL: NER (4 types). $N{=}16$ in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
31	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
32	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
33	\midrule
34	VC & Structural & \textbf{.379} & \textbf{.663} & \textbf{.350} & .694 & .424 & .789 & .426 & .709 \\
35	SJ  & Structural & .360 & .650 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
36	FK & Surface & .267 & .602 & .275 & .609 & .400 & .774 & .428 & .703 \\
37	EM  & Surface    & .295 & .614 & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
38	\midrule
39	LP     & Model      & .205 & .578 & .266 & .601 & .316 & .753 & .307 & \textbf{.761} \\
40	\bottomrule
41	\end{tabular}
42	\end{table*}
43	
44	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.\footnote{$\varepsilon{=}0.05$ is a convenience threshold used only in the selection analysis (\S\ref{sec:selection_gap}); quality estimation metrics ($\rho$, AUROC) are continuous and $\varepsilon$-free. Selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}).}
45	
46	\paragraph{Difficulty-dependent signal complementarity.}
47	On SciERC NER, structural signals lead: VC $\rho{=}0.379$, SJ $\rho{=}0.360$, outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$); on RE (preliminary), LP rises above SJ and FK in multi-seed analysis (Table~\ref{tab:multiseed}), likely because RE's 40\% zero-F1 rate favors generation confidence.
48	The best NER AUROC reaches 0.816 (EM, CoNLL Qwen); pairwise bootstrap CIs confirm the SJ--LP gap on SciERC NER ($\Delta\rho{=}{+}0.155$, CI excludes zero; Appendix~\ref{app:bootstrap_signal}).
49	Signal choice depends on use case: EM leads AUROC but not $\rho$ on CoNLL, preferred for binary triage; this $\rho$--AUROC dissociation replicates across configurations.
50	
51	\paragraph{Signal rankings shift with task difficulty.}
52	On CoNLL (greedy F1${\approx}$0.91), EM leads; on SciERC, structural signals dominate---demonstrating difficulty-dependent complementarity consistent across model families.
53	On WNUT-17 (52\% zero F1), all conditional signals collapse (Table~\ref{tab:wnut}), suggesting a capability boundary beyond which consistency captures binary success/failure but not quality gradation.
54	Restricting to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, Appendix~\ref{app:additional}): EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while LP RE collapses to $\rho{=}0.011$.
55	
56	%% ============================================================
57	\subsection{The Correlation-Selection Gap}
58	\label{sec:selection_gap}
59	
60	\begin{table}[t]
61	\centering
62	\small
63	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). NER: 2-seed mean${\pm}\sigma$ ($\sigma$ from 2 seeds; indicative only), Fisher combined $p$ vs.\ greedy; RE: single seed (preliminary). Best non-oracle in \textbf{bold}. $^\dagger$Greedy: a fixed $T{=}1.0$ sample.}
64	\label{tab:selection}
65	\begin{tabular}{lccc}
66	\toprule
67	Method & NER F1 & $p$ & RE F1 \\
68	\midrule
69	Oracle & $0.778 \pm 0.003$ & --- & 0.585 \\
70	\midrule
71	\multicolumn{4}{l}{\textit{Per-sample signal}} \\
72	LP           & $\mathbf{0.647} \pm 0.005$ & .29 & 0.395 \\
73	\midrule
74	\multicolumn{4}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
75	SJ           & $0.646 \pm 0.002$ & .68 & 0.386 \\
76	FK           & $0.646 \pm 0.001$ & .79 & --- \\
77	EM           & $0.637 \pm 0.001$ & .45 & 0.372 \\
78	VC           & $0.623 \pm 0.004$ & .26 & 0.359 \\
79	\midrule
80	Greedy$^\dagger$ & $0.645 \pm 0.001$ & --- & \textbf{0.404} \\
81	Random           & $0.610 \pm 0.003$ & --- & 0.354 \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	Despite strong quality estimation, confidence signals yield limited gains for best-of-$N$ selection (Table~\ref{tab:selection}; see also Figure~\ref{fig:selection_gap}).
87	Four of five signals are instance-level by construction (they assign identical scores to all candidates); the non-trivial question is whether LP---the only per-sample signal---can exploit the oracle headroom.
88	We anchor on SciERC, where output diversity is substantial (39--43\% unique outputs; Appendix~\ref{app:diversity}).
89	
90	\paragraph{No significant improvement over greedy.}
91	We evaluate significance via 2-seed instance-level sign tests ($n{=}551$, Fisher combination).
92	On NER, the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645).
93	LP achieves the highest mean selection F1 (0.647), indistinguishable from greedy ($\Delta{=}{+}0.2$~pp, $p{=}0.29$); all other signals also fail to reach significance (all $p{>}0.05$; Table~\ref{tab:selection}).
94	On RE, the best signal (LP, 0.395) falls below greedy (0.404; single seed, preliminary), while 18.1~pp of oracle headroom remains.
95	The pattern is consistent across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}).
96	
97	\paragraph{Quality estimation $\neq$ output selection.}
98	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; when per-sample variance is low, even perfect quality estimation fails to discriminate.
99	Closing this gap likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
100	
101	%% ============================================================
102	\subsection{Robustness}
103	\label{sec:robustness_main}
104	
105	Consistency-based signals (SJ, FK, EM, VC) are robust across $T{\in}\{0.7, 1.0\}$ and show sublinear gains from $N{=}8$ to $N{=}16$ (Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}); LP is excluded from this robustness claim, exhibiting the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$ on NER).
106	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}); RE miscalibration (ECE up to 0.339, preliminary) imposes a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba980f74-e709-42a3-aa3f-441c23777aed",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "b17cb7dd-6709-41ae-b5a6-82282d0bfcdd",
  "sourceToolAssistantUUID": "ba980f74-e709-42a3-aa3f-441c23777aed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T19:58:08.860Z_

<details><summary>↩ Tool result · reported error · `toolu_01WiVcMuSq3qsu9yECK24Fm8`</summary>

```text
File content (68777 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef78cc89-caef-4fc1-aca0-1f95029bacb4",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "29ef2bff-dd4d-4718-8cb6-7cefad288a07",
  "toolUseResult": "Error: File content (68777 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "ef78cc89-caef-4fc1-aca0-1f95029bacb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-15T19:58:11.552Z_

The experiments.tex file shows quality estimation and selection results but not the raw inference numbers. Let me search the registry.yaml for 8B model experiments:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29ef2bff-dd4d-4718-8cb6-7cefad288a07",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wp6Xyd6s87EDtkqTjf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0ea59755-029a-434b-a937-0e25182ed226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SQrz3iXW33K1ske7zuvqKb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3188,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 22089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 251,
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

_source line 13 · 2026-05-15T19:58:12.483Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YasERgVRSEZpZCgnGmY5hD`</summary>

```json
{
  "command": "grep -n \"8b\\|mvp\\|scs\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ea59755-029a-434b-a937-0e25182ed226",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wp6Xyd6s87EDtkqTjf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "33c79c72-6ba2-4c70-b559-7e6d0b5a3b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SQrz3iXW33K1ske7zuvqKb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3188,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 22089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 251,
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

_source line 14 · 2026-05-15T19:58:12.541Z_

<details><summary>↩ Tool result · `toolu_01YasERgVRSEZpZCgnGmY5hD`</summary>

```text
18:      command: sft training qwen3-8b on scierc with lora
19:      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora/
48:  mvp_pilot_001:
56:      model_name: qwen3-8b-scierc-merged
63:      command: CUDA_VISIBLE_DEVICES=0 python3 code/mvp_pilot.py
64:      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged
65:      log_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001.log
127:      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2
141:  mvp_pilot_002:
158:      note: Rerun of mvp_pilot_001 which crashed silently
159:      command: CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-lora
161:        1.0 --max_tokens 512 --output_dir output/mvp_pilot_001 --num_test 551 --seed
167:  mvp_pilot_003:
173:      command: CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged
176:        1024 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003
181:      model_name: qwen3-8b-scierc-merged
183:    log_path: /root/autodl-tmp/struct_self_consist_ie/mvp_pilot_003.log
184:    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003
259:      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2
287:  mvp_pilot_004:
304:      command: CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2
306:        8 --temperature 1.0 --max_tokens 1024 --output_dir output/mvp_pilot_004 --num_test
310:      log_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/mvp_pilot_004.log
311:      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004
353:  mvp_pilot_005:
368:      command: CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2
370:        8 --temperature 0.7 --max_tokens 1024 --output_dir output/mvp_pilot_005 --num_test
374:      tmux_session: mvp_pilot_005
375:      log_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/train.log
376:    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33c79c72-6ba2-4c70-b559-7e6d0b5a3b47",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "564cf8a5-1fae-459c-bd54-e063bae12865",
  "sourceToolAssistantUUID": "33c79c72-6ba2-4c70-b559-7e6d0b5a3b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T19:58:12.636Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GYJnnRWpADoDqG8rVgnYCN`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "564cf8a5-1fae-459c-bd54-e063bae12865",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wp6Xyd6s87EDtkqTjf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "33acd8df-591a-42d2-bf04-2d191530d465",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SQrz3iXW33K1ske7zuvqKb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3188,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 22089,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 251
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3188,
          "output_tokens": 207,
          "cache_read_input_tokens": 22089,
          "cache_creation_input_tokens": 251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 251,
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

_source line 16 · 2026-05-15T19:58:12.718Z_

<details><summary>↩ Tool result · `toolu_01GYJnnRWpADoDqG8rVgnYCN`</summary>

```text
4799 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33acd8df-591a-42d2-bf04-2d191530d465",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "2b23607c-d198-4b07-9628-38b76a6abc98",
  "sourceToolAssistantUUID": "33acd8df-591a-42d2-bf04-2d191530d465",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T19:58:14.176Z_

The registry is large. Let me search more specifically for experiments with "DONE" status and look for SciERC/CoNLL inference:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b23607c-d198-4b07-9628-38b76a6abc98",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wpNk3zpsPtCfyfh7yr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a91d2335-2c61-4a0a-908f-538bb383d0ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01812h1JicGVgZ2NCKnpPN9y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4435,
      "cache_read_input_tokens": 22340,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4435,
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

_source line 18 · 2026-05-15T19:58:14.766Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TLwG2HepEa5EMJgME18pzf`</summary>

```json
{
  "command": "grep -B 5 -A 30 \"exp_id.*scs\\|exp_id.*8b\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml | grep -A 30 \"status: DONE\" | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a91d2335-2c61-4a0a-908f-538bb383d0ed",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wpNk3zpsPtCfyfh7yr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "97cb95f1-bb0c-4507-bff9-2603bf6ba976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01812h1JicGVgZ2NCKnpPN9y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4435,
      "cache_read_input_tokens": 22340,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4435
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 160,
          "cache_read_input_tokens": 22340,
          "cache_creation_input_tokens": 4435,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4435,
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

_source line 19 · 2026-05-15T19:58:14.834Z_

<details><summary>↩ Tool result · `toolu_01TLwG2HepEa5EMJgME18pzf`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97cb95f1-bb0c-4507-bff9-2603bf6ba976",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "1a63d30e-0dd8-4124-baf0-3ee47de095ff",
  "sourceToolAssistantUUID": "97cb95f1-bb0c-4507-bff9-2603bf6ba976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-15T19:58:15.813Z_

Let me search for experiments with specific naming patterns and DONE status:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a63d30e-0dd8-4124-baf0-3ee47de095ff",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wpXmGyzn51QY6QnQ9E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9e8cfbc0-28bc-4da6-8b47-f24d9c2b2c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XaGEZGeNUJYkRaNUb6Vmny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 26775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 284,
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

_source line 21 · 2026-05-15T19:58:16.240Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01K9vRBrrCLAh6s523FrdpgM`</summary>

```json
{
  "command": "grep -n \"exp_id:\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml | grep -E \"scs|8b\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e8cfbc0-28bc-4da6-8b47-f24d9c2b2c34",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wpXmGyzn51QY6QnQ9E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "39c024aa-e169-4282-b4b7-95544670361e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XaGEZGeNUJYkRaNUb6Vmny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 26775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 284,
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

_source line 22 · 2026-05-15T19:58:16.308Z_

<details><summary>↩ Tool result · `toolu_01K9vRBrrCLAh6s523FrdpgM`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39c024aa-e169-4282-b4b7-95544670361e",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "81831038-4543-48f7-bf90-ccaaa6f881b4",
  "sourceToolAssistantUUID": "39c024aa-e169-4282-b4b7-95544670361e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T19:58:16.456Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PqsuZwFNoJ5RTbMQd4v2te`</summary>

```json
{
  "command": "grep -n \"status: DONE\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81831038-4543-48f7-bf90-ccaaa6f881b4",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wpXmGyzn51QY6QnQ9E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8eacf00a-4e74-44f6-8334-432acf27b8ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XaGEZGeNUJYkRaNUb6Vmny",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 26775,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 284
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 202,
          "cache_read_input_tokens": 26775,
          "cache_creation_input_tokens": 284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 284,
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

_source line 24 · 2026-05-15T19:58:16.511Z_

<details><summary>↩ Tool result · `toolu_01PqsuZwFNoJ5RTbMQd4v2te`</summary>

```text
4:    status: DONE
49:    status: DONE
109:    status: DONE
142:    status: DONE
168:    status: DONE
242:    status: DONE
288:    status: DONE
354:    status: DONE
423:    status: DONE
462:    status: DONE
509:    status: DONE
538:    status: DONE
576:    status: DONE
638:    status: DONE
670:    status: DONE
724:    status: DONE
774:    status: DONE
794:    status: DONE
817:    status: DONE
889:    status: DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8eacf00a-4e74-44f6-8334-432acf27b8ce",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "6f8de2c9-1e98-4806-8c53-d482c214efda",
  "sourceToolAssistantUUID": "8eacf00a-4e74-44f6-8334-432acf27b8ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T19:58:17.778Z_

Let me read sections of the registry that have DONE status entries. First, let me identify the experiment names around those line numbers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f8de2c9-1e98-4806-8c53-d482c214efda",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wpeycSMr9rnUzigdZk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f917ce0c-2ac8-4afc-bea4-3af996aa0c04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJxMzkBz3JVTwZ6EQAJL6N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 27059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 427,
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

_source line 26 · 2026-05-15T19:58:18.247Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TfKtAZpi8gH4CmwZAnY9Vq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml",
  "offset": 1,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f917ce0c-2ac8-4afc-bea4-3af996aa0c04",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wpeycSMr9rnUzigdZk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "42a20d47-792c-422c-a859-d3f4d61c5224",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJxMzkBz3JVTwZ6EQAJL6N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 27059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 427,
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

_source line 27 · 2026-05-15T19:58:18.254Z_

<details><summary>↩ Tool result · `toolu_01TfKtAZpi8gH4CmwZAnY9Vq`</summary>

```text
1	baseline: null
2	experiments:
3	  ft_001:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-14T06:04:28.030Z'
7	    updated_at: '2026-05-14T08:27:58.182Z'
8	    spec:
9	      hypothesis: Fine-tuned Qwen3-8B on SciERC UIE can achieve NER F1 >= 73 and serve
10	        as base model for structural consistency MVP
11	      model_name: Qwen/Qwen3-8B
12	      data_path: /root/autodl-tmp/struct_self_consist_ie/data/scierc
13	      data_count: 1861
14	      server: autodl-5090
15	      seed: 42
16	      method: LoRA r=16 alpha=32
17	      framework: LLaMA Factory 0.9.4
18	      command: sft training qwen3-8b on scierc with lora
19	      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora/
20	      log_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_001_train.log
21	      train_loss: 0.1099
22	      eval_loss: 0.0771
23	      epoch: 3
24	      train_runtime: 0:17:49
25	      note: 'gate0: NER PASS 60.4% / RE FAIL 33.8%'
26	    conclusion: success
27	    completed_at: '2026-05-14T06:30:32.889Z'
28	    metrics:
29	      train_loss: 0.1099
30	      eval_loss: 0.0771
31	      gate0_ner_f1_strict: 0.1143
32	      gate0_re_f1_strict: 0.0125
33	      gate0_ner_f1_text: 0.606
34	      gate0_re_f1_text: 0.3392
35	      gate0_offset_accuracy: 0.1665
36	      gate0_parse_failures: 43
37	      gate0_pass: false
38	      gate0_realigned_ner_f1: 0.6045
39	      gate0_realigned_re_f1: 0.338
40	      gate0_realigned_entity_offset_accuracy: 1
41	      gate0_realigned_relation_offset_accuracy: 1
42	      gate0_realigned_ner_pass: true
43	      gate0_realigned_re_pass: false
44	      gate0_realigned_pass: false
45	      gate0_ner_f1_delta_realign: 0.4901
46	      gate0_re_f1_delta_realign: 0.3255
47	      verdict_note: 'partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)'
48	  mvp_pilot_001:
49	    status: DONE
50	    retry_count: 0
51	    created_at: '2026-05-14T07:39:16.313Z'
52	    updated_at: '2026-05-14T08:05:34.348Z'
53	    spec:
54	      hypothesis: Structural self-consistency (soft Jaccard) correlates with per-instance
55	        F1 better than surface Fleiss Kappa on fine-tuned Qwen3-8B SciERC
56	      model_name: qwen3-8b-scierc-merged
57	      data_path: /root/autodl-tmp/struct_self_consist_ie/data/test.jsonl
58	      data_count: 551
59	      server: autodl-5090
60	      seed: 42
61	      parent: ft_001
62	      method: N=8 sampling T=1.0 + XGrammar + span realignment
63	      command: CUDA_VISIBLE_DEVICES=0 python3 code/mvp_pilot.py
64	      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged
65	      log_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001.log
66	    conclusion: negative
67	    completed_at: '2026-05-14T07:52:47.006Z'
68	    metrics:
69	      ner_greedy_f1: 0.611
70	      ner_oracle_f1: 0.78
71	      ner_headroom: 0.169
72	      ner_fleiss_kappa_mean: 0.2449
73	      ner_soft_jaccard_mean: 0.5041
74	      ner_full_rho_sj: 0.3616
75	      ner_full_rho_fk: 0.3515
76	      ner_full_n: 529
77	      ner_cond_rho_sj: 0.3688
78	      ner_cond_rho_fk: 0.3569
79	      ner_cond_n: 510
80	      ner_sj_beats_fk_full: true
81	      ner_sj_beats_fk_cond: true
82	      ner_sample_f1_pct_zero: 20.4
83	      ner_gold_empty_filtered: 22
84	      ner_all_zero_filtered: 19
85	      re_greedy_f1: 0.355
86	      re_oracle_f1: 0.572
87	      re_headroom: 0.217
88	      re_fleiss_kappa_mean: 0.0681
89	      re_soft_jaccard_mean: 0.3635
90	      re_full_rho_sj: 0.2535
91	      re_full_rho_fk: 0.2885
92	      re_full_n: 397
93	      re_cond_rho_sj: 0.3515
94	      re_cond_rho_fk: 0.3107
95	      re_cond_n: 320
96	      re_sj_beats_fk_full: false
97	      re_sj_beats_fk_cond: true
98	      re_sample_f1_pct_zero: 58.3
99	      re_gold_empty_filtered: 154
100	      re_all_zero_filtered: 77
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42a20d47-792c-422c-a859-d3f4d61c5224",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "55d8fb6b-8daf-4a27-bd44-d9f05dbce4f0",
  "sourceToolAssistantUUID": "42a20d47-792c-422c-a859-d3f4d61c5224",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T19:58:18.659Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LGDGBFLFTUrkRbXJDes16Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml",
  "offset": 280,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55d8fb6b-8daf-4a27-bd44-d9f05dbce4f0",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wpeycSMr9rnUzigdZk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f84731ad-3f12-4b2f-9dc3-b2006fd281b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJxMzkBz3JVTwZ6EQAJL6N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 27059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 427,
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

_source line 29 · 2026-05-15T19:58:18.667Z_

<details><summary>↩ Tool result · `toolu_01LGDGBFLFTUrkRbXJDes16Q`</summary>

```text
280	      gate0_ckpt400_ner_f1: 0.6475
281	      gate0_ckpt400_re_f1: 0.3793
282	      gate0_ckpt400_parse_failures: 0
283	      gate0_ckpt400_verdict: FAIL
284	      gate0_ckpt400_re_sample_f1_pct_zero: 58.8
285	      gate0_ckpt400_warning: '>30% samples F1=0'
286	    completed_at: '2026-05-14T08:51:32.405Z'
287	  mvp_pilot_004:
288	    status: DONE
289	    retry_count: 0
290	    created_at: '2026-05-14T08:51:38.203Z'
291	    updated_at: '2026-05-14T09:10:40.918Z'
292	    spec:
293	      hypothesis: With improved RE quality (F1=41.8%), structural self-consistency
294	        (soft Jaccard) correlates with per-instance F1 better than surface Fleiss
295	        Kappa, reaching rho_sj >= 0.40 on RE
296	      model_name: Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)
297	      data_path: /root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data
298	      data_count: 551
299	      server: autodl-5090
300	      seed: 42
301	      parent: ft_002_v2
302	      method: N=8 sampling T=1.0 + XGrammar + span realignment + max_tokens=1024 +
303	        gold-empty filter + conditional rho
304	      command: CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2
305	        --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples
306	        8 --temperature 1.0 --max_tokens 1024 --output_dir output/mvp_pilot_004 --num_test
307	        551 --seed 42 --tensor_parallel 1
308	      gpu: cuda:0
309	      pid: 31041
310	      log_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/mvp_pilot_004.log
311	      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004
312	    metrics:
313	      ner_greedy_f1: 0.6671
314	      ner_oracle_f1: 0.7756
315	      ner_headroom: 0.1085
316	      ner_fleiss_kappa_mean: 0.4048
317	      ner_soft_jaccard_mean: 0.7008
318	      ner_full_rho_fk: 0.259
319	      ner_full_rho_sj: 0.3825
320	      ner_full_n: 529
321	      ner_cond_rho_fk: 0.2352
322	      ner_cond_rho_sj: 0.3762
323	      ner_cond_n: 508
324	      ner_sj_beats_fk_full: true
325	      ner_sj_beats_fk_cond: true
326	      ner_sample_f1_mean: 0.6084
327	      ner_sample_f1_std: 0.3174
328	      ner_sample_f1_pct_zero: 12.19
329	      ner_gold_empty_filtered: 22
330	      ner_all_zero_filtered: 21
331	      re_greedy_f1: 0.4208
332	      re_oracle_f1: 0.5882
333	      re_headroom: 0.1674
334	      re_fleiss_kappa_mean: 0.2996
335	      re_soft_jaccard_mean: 0.6114
336	      re_full_rho_fk: 0.2782
337	      re_full_rho_sj: 0.2441
338	      re_full_n: 397
339	      re_cond_rho_fk: 0.3067
340	      re_cond_rho_sj: 0.3161
341	      re_cond_n: 313
342	      re_sj_beats_fk_full: false
343	      re_sj_beats_fk_cond: true
344	      re_sample_f1_mean: 0.3612
345	      re_sample_f1_std: 0.383
346	      re_sample_f1_pct_zero: 44.3
347	      re_gold_empty_filtered: 154
348	      re_all_zero_filtered: 84
349	      parse_failures: 0
350	      verdict: FAIL
351	    conclusion: negative
352	    completed_at: '2026-05-14T09:10:40.918Z'
353	  mvp_pilot_005:
354	    status: DONE
355	    retry_count: 0
356	    created_at: '2026-05-14T09:14:09.456Z'
357	    updated_at: '2026-05-14T09:47:06.597Z'
358	    spec:
359	      hypothesis: T=0.7 降低 RE zero rate，恢复 SJ>FK，rho_sj 可能 ≥ 0.30 (MARGINAL threshold)
360	      model_name: Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)
361	      data_path: /root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data
362	      data_count: 551
363	      server: autodl-5090
364	      seed: 42
365	      parent: ft_002_v2
366	      method: N=8 sampling T=0.7 + XGrammar + span realignment + max_tokens=1024 +
367	        gold-empty filter + conditional rho
368	      command: CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2
369	        --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples
370	        8 --temperature 0.7 --max_tokens 1024 --output_dir output/mvp_pilot_005 --num_test
371	        551 --seed 42 --tensor_parallel 1
372	      gpu: cuda:0
373	      pid: 32456
374	      tmux_session: mvp_pilot_005
375	      log_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/train.log
376	    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005
377	    metrics:
378	      ner_greedy_f1: 0.6619
379	      ner_oracle_f1: 0.7585
380	      ner_headroom: 0.0966
381	      ner_fleiss_kappa_mean: 0.4722
382	      ner_soft_jaccard_mean: 0.7757
383	      ner_full_rho_sj: 0.3875
384	      ner_full_rho_fk: 0.3211
385	      ner_full_n: 529
386	      ner_cond_rho_sj: 0.3868
387	      ner_cond_rho_fk: 0.305
388	      ner_cond_n: 504
389	      ner_sj_beats_fk_full: true
390	      ner_sj_beats_fk_cond: true
391	      ner_rho_advantage: 0.0664
392	      ner_sample_f1_mean: 0.6243
393	      ner_sample_f1_std: 0.3131
394	      ner_sample_f1_pct_zero: 11.2
395	      ner_gold_empty_filtered: 22
396	      ner_all_zero_filtered: 25
397	      re_greedy_f1: 0.4219
398	      re_oracle_f1: 0.5532
399	      re_headroom: 0.1313
400	      re_fleiss_kappa_mean: 0.3829
401	      re_soft_jaccard_mean: 0.687
402	      re_full_rho_sj: 0.2343
403	      re_full_rho_fk: 0.1835
404	      re_full_n: 397
405	      re_cond_rho_sj: 0.3716
406	      re_cond_rho_fk: 0.2533
407	      re_cond_n: 301
408	      re_sj_beats_fk_full: true
409	      re_sj_beats_fk_cond: true
410	      re_rho_advantage: 0.0508
411	      re_sample_f1_mean: 0.3782
412	      re_sample_f1_std: 0.3845
413	      re_sample_f1_pct_zero: 42.4
414	      re_gold_empty_filtered: 154
415	      re_all_zero_filtered: 96
416	      parse_failures: 0
417	      verdict: FAIL
418	      verdict_note: RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional
419	        but not full threshold
420	    conclusion: negative
421	    completed_at: '2026-05-14T09:47:06.597Z'
422	  e1_component_wise_re_sj:
423	    status: DONE
424	    retry_count: 0
425	    created_at: '2026-05-14T09:15:17.262Z'
426	    updated_at: '2026-05-14T09:23:38.818Z'
427	    spec:
428	      hypothesis: RE SJ 乘性惩罚是 root cause：分解后 head_sj ρ ≈ NER ρ (~0.38)，tail_sj 和乘性组合拖低整体
429	        ρ
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f84731ad-3f12-4b2f-9dc3-b2006fd281b8",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "b7ba10b0-9a43-4286-bde9-8ced28718745",
  "sourceToolAssistantUUID": "f84731ad-3f12-4b2f-9dc3-b2006fd281b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T19:58:18.895Z_

<details open><summary>🔧 Tool call — Read · `toolu_014N6KHJ2aCssaRErr6oddfy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml",
  "offset": 530,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7ba10b0-9a43-4286-bde9-8ced28718745",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wpeycSMr9rnUzigdZk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2f284b6f-da18-44a5-ba17-4a3312a9c9dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJxMzkBz3JVTwZ6EQAJL6N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 27059,
      "output_tokens": 351,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 427
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 351,
          "cache_read_input_tokens": 27059,
          "cache_creation_input_tokens": 427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 427,
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

_source line 31 · 2026-05-15T19:58:18.900Z_

<details><summary>↩ Tool result · `toolu_014N6KHJ2aCssaRErr6oddfy`</summary>

```text
530	      ner_full_tau: 0.2181
531	      ner_full_auroc: 0.6398
532	      re_full_rho: 0.1562
533	      re_full_p: 0.0018
534	      re_full_tau: 0.1185
535	      re_full_auroc: 0.5863
536	      diagnosis: EM between SJ and FK on NER, weakest on RE. Too coarse-grained.
537	  exp_014_entity_majority_voting:
538	    status: DONE
539	    retry_count: 0
540	    created_at: '2026-05-14T10:53:21.203Z'
541	    updated_at: '2026-05-14T11:33:30.085Z'
542	    spec:
543	      hypothesis: Entity-level majority voting confidence beats SJ as correlation
544	        signal
545	      model_name: N/A (reuse pilot_004 samples)
546	      data_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004
547	      data_count: 551
548	      server: autodl-5090
549	      seed: 42
550	      parent: mvp_pilot_004
551	      method: Per-entity voting across N=8 samples, consensus construction, confidence
552	        = mean voting rate
553	      command: python code/analyze_entity_voting.py
554	      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004
555	      log_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp014_entity_voting_report.json
556	    conclusion: success
557	    completed_at: '2026-05-14T11:18:09.468Z'
558	    metrics:
559	      ner_full_rho: 0.3915
560	      ner_full_p: 8.1e-21
561	      ner_full_tau: 0.2906
562	      ner_full_auroc: 0.7039
563	      re_full_rho: 0.3403
564	      re_full_p: 3.21e-12
565	      re_full_tau: 0.256
566	      re_full_auroc: 0.6668
567	      ner_voting_f1: 0.6246
568	      ner_greedy_f1: 0.6483
569	      ner_oracle_f1: 0.7793
570	      re_voting_f1: 0.3577
571	      re_greedy_f1: 0.4022
572	      re_oracle_f1: 0.5886
573	      diagnosis: Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE
574	        (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.
575	  exp_001_ner_n16_scierc:
576	    status: DONE
577	    retry_count: 0
578	    created_at: '2026-05-14T11:42:10.898Z'
579	    updated_at: '2026-05-14T12:42:49.592Z'
580	    spec:
581	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
582	        base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0
583	        python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2
584	        --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples
585	        16 --temperature 1.0 --seed 42 --output_dir output/exp001_n16_seed42 --num_test
586	        9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed42_run.log"
587	      server: autodl-5090
588	      gpu:
589	      - cuda:0
590	      pid: '54357'
591	      log_path: ~/runs/struct_self_consist_ie/exp_001_ner_n16_scierc.log
592	      submitted_at: '2026-05-14T12:15:46.646Z'
593	      submitted_via: submit_training_job
594	      backend: tmux
595	      account: root
596	    server: autodl-5090
597	    gpu: cuda:0
598	    account: root
599	    reproduce:
600	      server: autodl-5090
601	      gpu: cuda:0
602	      started_at: '2026-05-14T11:43:48.643Z'
603	    conclusion: success
604	    completed_at: '2026-05-14T11:55:45.664Z'
605	    metrics:
606	      n_instances: 551
607	      ner_n: 529
608	      re_n: 397
609	      N: 16
610	      T: 1
611	      seed: 42
612	      full_test_set: true
613	      ner_voting_conf_rho: 0.399
614	      ner_sj_rho: 0.398
615	      ner_em_rho: 0.339
616	      ner_fk_rho: 0.288
617	      ner_logprob_rho: 0.237
618	      ner_voting_conf_auroc: 0.704
619	      ner_sj_auroc: 0.697
620	      ner_cond_em_rho: 0.414
621	      ner_cond_sj_rho: 0.349
622	      ner_cond_vc_rho: 0.34
623	      re_voting_conf_rho: 0.38
624	      re_logprob_rho: 0.293
625	      re_fk_rho: 0.281
626	      re_sj_rho: 0.277
627	      re_em_rho: 0.148
628	      re_voting_conf_auroc: 0.699
629	      re_cond_em_rho: 0.475
630	      re_cond_sj_rho: 0.318
631	      re_cond_vc_rho: 0.35
632	      re_cond_em_auroc: 0.742
633	      diagnosis: '551 instances T=1.0: voting_conf best on full set (NER 0.399, RE
634	        0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475).
635	        RE full FAIL (SJ 0.277 < 0.40). Previous N-scaling ''breakthrough'' was artifact
636	        of 200 instances + T=0.7.'
637	  exp_002_ner_conll2003:
638	    status: DONE
639	    retry_count: 0
640	    created_at: '2026-05-14T11:42:15.223Z'
641	    updated_at: '2026-05-14T12:27:35.413Z'
642	    spec:
643	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
644	        base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0
645	        python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged
646	        --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8
647	        --temperature 1.0 --max_tokens 1024 --output_dir output/exp002_conll2003 --num_test
648	        99999 --seed 42 --collect_logprobs 2>&1 | tee /tmp/pilot_conll2003.log"
649	      server: autodl-5090
650	      gpu:
651	      - cuda:0
652	      pid: '58208'
653	      log_path: ~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log
654	      submitted_at: '2026-05-14T12:27:35.337Z'
655	      submitted_via: submit_training_job
656	      backend: tmux
657	      account: root
658	    server: autodl-5090
659	    gpu: cuda:1
660	    account: root
661	    reproduce:
662	      server: autodl-5090
663	      gpu: cuda:1
664	      started_at: '2026-05-14T11:43:49.959Z'
665	    conclusion: success
666	    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-lora
667	    log_path: ~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log
668	    completed_at: '2026-05-14T12:18:04.097Z'
669	  exp_003_ner_wnut17:
670	    status: DONE
671	    retry_count: 0
672	    created_at: '2026-05-14T11:42:17.544Z'
673	    updated_at: '2026-05-14T13:40:20.979Z'
674	    spec:
675	      merged_model_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged
676	      pilot_command: CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path
677	        checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17
678	        --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_pilot
679	        --num_test 9999 --collect_logprobs
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f284b6f-da18-44a5-ba17-4a3312a9c9dc",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "785098e0-57ed-4dd0-ab3a-48f81e5a94a6",
  "sourceToolAssistantUUID": "2f284b6f-da18-44a5-ba17-4a3312a9c9dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-15T19:58:21.010Z_

Good progress. I can see CoNLL2003 (exp_002) and SciERC (exp_001). Let me search for CoNLL metrics:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "785098e0-57ed-4dd0-ab3a-48f81e5a94a6",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wpqQvMRT4uKyUz38yf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "11a300d4-c242-4cd5-b723-8fa64c87bc92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T61yBUirKujawodbQegkxf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7721,
      "cache_read_input_tokens": 27486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7721,
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

_source line 33 · 2026-05-15T19:58:21.854Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rs1okLKU1kqx8bxGwGqxjJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml",
  "offset": 636,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11a300d4-c242-4cd5-b723-8fa64c87bc92",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wpqQvMRT4uKyUz38yf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ec8d862c-a2de-4458-b9ad-78500252bb7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T61yBUirKujawodbQegkxf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7721,
      "cache_read_input_tokens": 27486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7721,
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

_source line 34 · 2026-05-15T19:58:21.860Z_

<details><summary>↩ Tool result · `toolu_01Rs1okLKU1kqx8bxGwGqxjJ`</summary>

```text
636	        of 200 instances + T=0.7.'
637	  exp_002_ner_conll2003:
638	    status: DONE
639	    retry_count: 0
640	    created_at: '2026-05-14T11:42:15.223Z'
641	    updated_at: '2026-05-14T12:27:35.413Z'
642	    spec:
643	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
644	        base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0
645	        python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged
646	        --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8
647	        --temperature 1.0 --max_tokens 1024 --output_dir output/exp002_conll2003 --num_test
648	        99999 --seed 42 --collect_logprobs 2>&1 | tee /tmp/pilot_conll2003.log"
649	      server: autodl-5090
650	      gpu:
651	      - cuda:0
652	      pid: '58208'
653	      log_path: ~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log
654	      submitted_at: '2026-05-14T12:27:35.337Z'
655	      submitted_via: submit_training_job
656	      backend: tmux
657	      account: root
658	    server: autodl-5090
659	    gpu: cuda:1
660	    account: root
661	    reproduce:
662	      server: autodl-5090
663	      gpu: cuda:1
664	      started_at: '2026-05-14T11:43:49.959Z'
665	    conclusion: success
666	    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-lora
667	    log_path: ~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log
668	    completed_at: '2026-05-14T12:18:04.097Z'
669	  exp_003_ner_wnut17:
670	    status: DONE
671	    retry_count: 0
672	    created_at: '2026-05-14T11:42:17.544Z'
673	    updated_at: '2026-05-14T13:40:20.979Z'
674	    spec:
675	      merged_model_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged
676	      pilot_command: CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path
677	        checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17
678	        --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_pilot
679	        --num_test 9999 --collect_logprobs
680	      pilot_pid: 71498
681	      pilot_server: autodl-5090
682	      pilot_started_at: '2026-05-14T21:36:00Z'
683	      test_samples: 1287
684	    server: autodl-5090
685	    gpu: cuda:2
686	    account: root
687	    reproduce:
688	      server: autodl-5090
689	      gpu: cuda:2
690	      started_at: '2026-05-14T11:43:50.537Z'
691	      finished_at: '2026-05-14T12:53:13.262Z'
692	      training_hours: 1.16
693	    extra:
694	      hook_events:
695	      - event: on_complete
696	        action: agent
697	        ts: '2026-05-14T12:53:14.768981+00:00'
698	    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged
699	    metrics:
700	      ner:
701	        greedy_f1: 0.525
702	        oracle_f1: 0.664
703	        headroom: 0.139
704	        rho_sj_full: 0.082
705	        rho_fk_full: 0.124
706	        rho_logprob_full: -0.414
707	        rho_sj_cond: 0.275
708	        rho_fk_cond: 0.164
709	        rho_logprob_cond: 0.352
710	        sj_beats_logprob_cond: false
711	      n_instances: 1287
712	      n_gold_empty: 598
713	      sample_f1_mean: 0.401
714	      sample_f1_pct_zero: 53.7
715	      N: 16
716	      T: 1
717	      seed: 42
718	      verdict: FAIL
719	      verdict_note: '>30% samples F1=0; structural rho weak; logprob baseline stronger'
720	    conclusion: negative
721	    log_path: output/exp003_wnut17_pilot/
722	    completed_at: '2026-05-14T13:40:20.979Z'
723	  exp_007_ner_multi_model:
724	    status: DONE
725	    retry_count: 0
726	    created_at: '2026-05-14T11:42:20.748Z'
727	    updated_at: '2026-05-14T13:35:43.251Z'
728	    spec:
729	      command: bash -c 'source env.sh && cd /root/autodl-tmp/struct_self_consist_ie
730	        && llamafactory-cli train train_config_llama.yaml'
731	      server: gpu-5090-4x-2
732	      gpu:
733	      - cuda:0
734	      pid: '60970'
735	      log_path: ~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log
736	      submitted_at: '2026-05-14T12:43:09.108Z'
737	      submitted_via: submit_training_job
738	      backend: tmux
739	      account: root
740	      data_path: /root/autodl-tmp/struct_self_consist_ie/data
741	      data_count: 1861
742	      model_name: LLaMA-3.1-8B-Instruct
743	      seed: 42
744	      log_file: ~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log
745	      wall_clock_seconds: 165.8
746	      gpu_hours: 0.05
747	    server: autodl-5090
748	    gpu: cuda:3
749	    account: root
750	    reproduce:
751	      server: autodl-5090
752	      gpu: cuda:3
753	      started_at: '2026-05-14T11:43:50.977Z'
754	    conclusion: success
755	    completed_at: '2026-05-14T12:45:54.952Z'
756	    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-lora
757	    metrics:
758	      epoch: 5
759	      train_loss: 0.0767
760	      eval_loss: 0.1049
761	      train_runtime_sec: 1494.5
762	      train_samples_per_second: 6.226
763	      checkpoints:
764	      - checkpoint-400
765	      - checkpoint-500
766	      - checkpoint-585
767	      base_model: Meta-Llama-3.1-8B-Instruct
768	      lora_r: 32
769	      lora_alpha: 64
770	      note: EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal.
771	        Checkpoint fully intact.
772	    log_path: ~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log
773	  exp_007_ner_llama:
774	    status: DONE
775	    retry_count: 0
776	    created_at: '2026-05-14T11:42:21.510Z'
777	    updated_at: '2026-05-15T12:41:27.410Z'
778	    spec:
779	      description: Fine-tune LLaMA-3.1-8B on SciERC + NER pilot (N=8, T=0.7). Model-agnostic
780	        validation.
781	      hypothesis: SJ advantage is model-agnostic, not Qwen3-specific
782	      plan_id: exp-007
783	      claim: 1
784	      model_name: llama-3.1-8b-instruct (new fine-tune)
785	      dataset: SciERC
786	      priority: P0
787	      failure_reason: Superseded by exp_007_ner_multi_model + exp_007_llama_inference
788	        (completed on autodl-5090)
789	    conclusion: killed
790	    failure_reason: superseded by exp_007_llama_inference (DONE)
791	    notes: Completed as exp_007_llama_n16 on autodl-5090. Registry status corrected.
792	    completed_at: '2026-05-15T12:41:27.410Z'
793	  exp_005:
794	    status: DONE
795	    retry_count: 0
796	    created_at: '2026-05-14T11:45:16.360Z'
797	    updated_at: '2026-05-14T11:45:38.570Z'
798	    spec:
799	      hypothesis: 'Temperature sensitivity: systematic comparison of T=0.7 vs T=1.0
800	        on all 5 confidence signals'
801	      method: CPU-only analysis from checkpoint metrics (pilot_004 T=1.0, pilot_005
802	        T=0.7, exp_012/013/014)
803	      data_count: 551
804	      model_name: Qwen3-8B-SciERC-LoRA-v2
805	      data_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/
806	      server: local
807	      seed: 42
808	      parent: mvp_pilot_004,mvp_pilot_005
809	      command: python3 analyze_exp005_temperature.py
810	      checkpoint_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/
811	      log_path: N/A
812	      checkpoint_source: pilot_004+pilot_005 checkpoint metrics
813	      eval_data: SciERC test set (n=551)
814	    conclusion: success
815	    completed_at: '2026-05-14T11:45:38.570Z'
816	  exp_015_metrics_expansion:
817	    status: DONE
818	    retry_count: 0
819	    created_at: '2026-05-14T11:47:36.569Z'
820	    updated_at: '2026-05-14T15:16:34.851Z'
821	    spec:
822	      hypothesis: Comprehensive evaluation of all 5 confidence signals with extended
823	        metrics
824	      model_name: N/A (reuse pilot_004 samples)
825	      data_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl
826	      data_count: 551
827	      server: autodl-5090
828	      seed: 42
829	      parent: exp_012_logprob_baseline
830	      method: 'CPU-only analysis: 6 metrics x 5 signals x 2 subtasks (NER+RE)'
831	      command: python code/analyze_exp015_metrics_expansion.py
832	      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004
833	      log_path: /root/autodl-tmp/struct_self_consist_ie/output/exp015_metrics_expansion
834	    conclusion: success
835	    completed_at: '2026-05-14T12:22:32.661Z'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec8d862c-a2de-4458-b9ad-78500252bb7c",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "4d1c8bb8-696c-4d7f-bd32-1fef07904442",
  "sourceToolAssistantUUID": "ec8d862c-a2de-4458-b9ad-78500252bb7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T19:58:22.166Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TqAThtggtWjv6rT4P4ACnX`</summary>

```json
{
  "command": "grep -n \"exp_002_ner_conll\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d1c8bb8-696c-4d7f-bd32-1fef07904442",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wpqQvMRT4uKyUz38yf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d0543ef2-c24e-4cd8-a24e-81145c734676",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T61yBUirKujawodbQegkxf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7721,
      "cache_read_input_tokens": 27486,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7721
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 237,
          "cache_read_input_tokens": 27486,
          "cache_creation_input_tokens": 7721,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7721,
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

_source line 36 · 2026-05-15T19:58:22.218Z_

<details><summary>↩ Tool result · `toolu_01TqAThtggtWjv6rT4P4ACnX`</summary>

```text
637:  exp_002_ner_conll2003:
653:      log_path: ~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log
667:    log_path: ~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log
1337:      failure_reason: Superseded by exp_002_ner_conll2003 (completed on autodl-5090)
1341:    failure_reason: superseded by exp_002_ner_conll2003 (DONE)
2578:      parent: exp_002_ner_conll2003
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0543ef2-c24e-4cd8-a24e-81145c734676",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "be2c1209-3e7c-4c4d-8c5d-781b06cb7161",
  "sourceToolAssistantUUID": "d0543ef2-c24e-4cd8-a24e-81145c734676",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T19:58:24.113Z_

I see exp_002 doesn't have metrics shown in that section. Let me search for where the metrics are:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be2c1209-3e7c-4c4d-8c5d-781b06cb7161",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wq5LpUMWeyBqYxZoGV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "47738c60-1067-4586-a895-c0d20f7839c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0145rjr1GmqdaDW88SfQ3KF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3942,
      "cache_read_input_tokens": 35207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3942,
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

_source line 38 · 2026-05-15T19:58:24.928Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013gHsL7pcy8x3WowF1P5kit`</summary>

```json
{
  "command": "awk '/exp_002_ner_conll2003:/,/^  [a-z]/' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47738c60-1067-4586-a895-c0d20f7839c0",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wq5LpUMWeyBqYxZoGV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "87e49dc0-7fe2-4ece-b8cf-fe19f77e3f91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0145rjr1GmqdaDW88SfQ3KF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3942,
      "cache_read_input_tokens": 35207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3942,
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

_source line 39 · 2026-05-15T19:58:24.997Z_

<details><summary>↩ Tool result · `toolu_013gHsL7pcy8x3WowF1P5kit`</summary>

```text
  exp_002_ner_conll2003:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87e49dc0-7fe2-4ece-b8cf-fe19f77e3f91",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "3b590de8-0917-48db-8b61-e5540b446300",
  "sourceToolAssistantUUID": "87e49dc0-7fe2-4ece-b8cf-fe19f77e3f91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T19:58:25.225Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011k4WKty6DDcs1HAxz748aK`</summary>

```json
{
  "command": "awk '/exp_001_ner_n16_scierc:/,/^  [a-z]/' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml | grep -A 60 \"metrics:\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b590de8-0917-48db-8b61-e5540b446300",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wq5LpUMWeyBqYxZoGV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "79b432ba-c16d-40e7-a3fa-386e7559aee2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0145rjr1GmqdaDW88SfQ3KF5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3942,
      "cache_read_input_tokens": 35207,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3942
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 242,
          "cache_read_input_tokens": 35207,
          "cache_creation_input_tokens": 3942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3942,
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

_source line 41 · 2026-05-15T19:58:25.283Z_

<details><summary>↩ Tool result · `toolu_011k4WKty6DDcs1HAxz748aK`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79b432ba-c16d-40e7-a3fa-386e7559aee2",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "ef540ced-3e58-477c-b6e7-29abea922a2c",
  "sourceToolAssistantUUID": "79b432ba-c16d-40e7-a3fa-386e7559aee2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-15T19:58:26.278Z_

Let me check what comes after exp_002:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef540ced-3e58-477c-b6e7-29abea922a2c",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wqJXLAUSuSULg5NAUu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5d4edd36-f6ae-404c-b510-0c93dea9896b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JuuFrrFzFuiatJY3PS7Lc9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 39149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 321,
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

_source line 43 · 2026-05-15T19:58:26.643Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HzR1nyYMkTQwFF2Wtt62hG`</summary>

```json
{
  "command": "sed -n '637,750p' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d4edd36-f6ae-404c-b510-0c93dea9896b",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wqJXLAUSuSULg5NAUu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "063f29c9-f052-4bd6-9f8a-8de229073e94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JuuFrrFzFuiatJY3PS7Lc9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 39149,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 321
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 104,
          "cache_read_input_tokens": 39149,
          "cache_creation_input_tokens": 321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 321,
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

_source line 44 · 2026-05-15T19:58:26.699Z_

<details><summary>↩ Tool result · `toolu_01HzR1nyYMkTQwFF2Wtt62hG`</summary>

```text
  exp_002_ner_conll2003:
    status: DONE
    retry_count: 0
    created_at: '2026-05-14T11:42:15.223Z'
    updated_at: '2026-05-14T12:27:35.413Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0
        python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged
        --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8
        --temperature 1.0 --max_tokens 1024 --output_dir output/exp002_conll2003 --num_test
        99999 --seed 42 --collect_logprobs 2>&1 | tee /tmp/pilot_conll2003.log"
      server: autodl-5090
      gpu:
      - cuda:0
      pid: '58208'
      log_path: ~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log
      submitted_at: '2026-05-14T12:27:35.337Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
    server: autodl-5090
    gpu: cuda:1
    account: root
    reproduce:
      server: autodl-5090
      gpu: cuda:1
      started_at: '2026-05-14T11:43:49.959Z'
    conclusion: success
    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-lora
    log_path: ~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log
    completed_at: '2026-05-14T12:18:04.097Z'
  exp_003_ner_wnut17:
    status: DONE
    retry_count: 0
    created_at: '2026-05-14T11:42:17.544Z'
    updated_at: '2026-05-14T13:40:20.979Z'
    spec:
      merged_model_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged
      pilot_command: CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path
        checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17
        --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_pilot
        --num_test 9999 --collect_logprobs
      pilot_pid: 71498
      pilot_server: autodl-5090
      pilot_started_at: '2026-05-14T21:36:00Z'
      test_samples: 1287
    server: autodl-5090
    gpu: cuda:2
    account: root
    reproduce:
      server: autodl-5090
      gpu: cuda:2
      started_at: '2026-05-14T11:43:50.537Z'
      finished_at: '2026-05-14T12:53:13.262Z'
      training_hours: 1.16
    extra:
      hook_events:
      - event: on_complete
        action: agent
        ts: '2026-05-14T12:53:14.768981+00:00'
    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged
    metrics:
      ner:
        greedy_f1: 0.525
        oracle_f1: 0.664
        headroom: 0.139
        rho_sj_full: 0.082
        rho_fk_full: 0.124
        rho_logprob_full: -0.414
        rho_sj_cond: 0.275
        rho_fk_cond: 0.164
        rho_logprob_cond: 0.352
        sj_beats_logprob_cond: false
      n_instances: 1287
      n_gold_empty: 598
      sample_f1_mean: 0.401
      sample_f1_pct_zero: 53.7
      N: 16
      T: 1
      seed: 42
      verdict: FAIL
      verdict_note: '>30% samples F1=0; structural rho weak; logprob baseline stronger'
    conclusion: negative
    log_path: output/exp003_wnut17_pilot/
    completed_at: '2026-05-14T13:40:20.979Z'
  exp_007_ner_multi_model:
    status: DONE
    retry_count: 0
    created_at: '2026-05-14T11:42:20.748Z'
    updated_at: '2026-05-14T13:35:43.251Z'
    spec:
      command: bash -c 'source env.sh && cd /root/autodl-tmp/struct_self_consist_ie
        && llamafactory-cli train train_config_llama.yaml'
      server: gpu-5090-4x-2
      gpu:
      - cuda:0
      pid: '60970'
      log_path: ~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log
      submitted_at: '2026-05-14T12:43:09.108Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      data_path: /root/autodl-tmp/struct_self_consist_ie/data
      data_count: 1861
      model_name: LLaMA-3.1-8B-Instruct
      seed: 42
      log_file: ~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log
      wall_clock_seconds: 165.8
      gpu_hours: 0.05
    server: autodl-5090
    gpu: cuda:3
    account: root
    reproduce:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "063f29c9-f052-4bd6-9f8a-8de229073e94",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "d954b4cc-79aa-46c8-8c17-a703688c5266",
  "sourceToolAssistantUUID": "063f29c9-f052-4bd6-9f8a-8de229073e94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-15T19:58:28.215Z_

I see exp_002 doesn't have metrics in the registry. Let me look for inference experiments related to CoNLL and LLaMA. Let me search more broadly:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d954b4cc-79aa-46c8-8c17-a703688c5266",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wqQcwVZpKE6xhAwNQw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f3f631c5-ece8-403c-ab9a-49e704786a24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013uMViUE5XYjWNqXFoUBFWH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 39470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1776,
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

_source line 46 · 2026-05-15T19:58:29.334Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01R9ySnZxvkjYYsDmU4qm7i9`</summary>

```json
{
  "command": "grep -n \"conll\\|CoNLL\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3f631c5-ece8-403c-ab9a-49e704786a24",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wqQcwVZpKE6xhAwNQw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9d037962-4a55-46e8-9960-f295b77737f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013uMViUE5XYjWNqXFoUBFWH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 39470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1776,
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

_source line 47 · 2026-05-15T19:58:29.415Z_

<details><summary>↩ Tool result · `toolu_01R9ySnZxvkjYYsDmU4qm7i9`</summary>

```text
637:  exp_002_ner_conll2003:
645:        python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged
646:        --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8
647:        --temperature 1.0 --max_tokens 1024 --output_dir output/exp002_conll2003 --num_test
648:        99999 --seed 42 --collect_logprobs 2>&1 | tee /tmp/pilot_conll2003.log"
653:      log_path: ~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log
666:    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-lora
667:    log_path: ~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log
1318:  exp_002_merge_conll2003:
1326:        llamafactory-cli export export_config_conll2003.yaml > /tmp/merge_conll2003.log
1327:        2>&1 && echo 'MERGE_DONE' >> /tmp/merge_conll2003.log"
1332:      log_path: ~/runs/struct_self_consist_ie/exp_002_merge_conll2003.log
1337:      failure_reason: Superseded by exp_002_ner_conll2003 (completed on autodl-5090)
1341:    failure_reason: superseded by exp_002_ner_conll2003 (DONE)
1342:    notes: Completed as exp_002_conll_n16 on autodl-5090. Registry status corrected.
1350:      command: python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged
1351:        --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --collect_logprobs
1354:      data_path: data/conll2003
1356:      model_name: qwen3-8b-conll2003-lora-merged
1358:      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d037962-4a55-46e8-9960-f295b77737f8",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "4ee58b39-5cc3-4a6a-b6ed-4ea6f114c3ac",
  "sourceToolAssistantUUID": "9d037962-4a55-46e8-9960-f295b77737f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T19:58:29.672Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WzUS4w9WkvyXkqVpsn5gWG`</summary>

```json
{
  "command": "grep -n \"llama.*inference\\|llama.*conll\" -i /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ee58b39-5cc3-4a6a-b6ed-4ea6f114c3ac",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wqQcwVZpKE6xhAwNQw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ecf1584f-97fc-4dfd-b897-3c0ec8d291e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013uMViUE5XYjWNqXFoUBFWH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 39470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1776,
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

_source line 49 · 2026-05-15T19:58:29.754Z_

<details><summary>↩ Tool result · `toolu_01WzUS4w9WkvyXkqVpsn5gWG`</summary>

```text
787:      failure_reason: Superseded by exp_007_ner_multi_model + exp_007_llama_inference
790:    failure_reason: superseded by exp_007_llama_inference (DONE)
1326:        llamafactory-cli export export_config_conll2003.yaml > /tmp/merge_conll2003.log
1673:  exp_007_llama_inference:
1682:        output/exp007_llama_inference/
1687:      log_path: ~/runs/struct_self_consist_ie/exp_007_llama_inference.log
1697:      description: LLaMA-3.1-8B SciERC joint inference (NER+RE) with 8 samples, T=1.0,
1701:    log_path: output/exp007_llama_inference/
1836:  exp_017_llama_conll:
1842:      command: llamafactory-cli train train_config_llama_conll2003.yaml
1855:      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-conll2003-lora/
2501:  exp_017_llama_conll_infer:
2507:      hypothesis: 'LLaMA-3.1-8B CoNLL-2003 inference: cross-model cross-dataset validation
2510:      parent: exp_017_llama_conll
2511:      command: python code/run_llama_conll_infer.py
2519:      description: LLaMA CoNLL-2003 NER inference N=8 (cross-model + cross-dataset
2561:    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl
2562:    log_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/
2565:    notes: 'LLaMA CoNLL-2003 NER N=8 (not N=16, cost constraint: 3453 test instances).
2649:      parent: exp_007_llama_inference
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecf1584f-97fc-4dfd-b897-3c0ec8d291e4",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "640ec088-d9bf-40da-a51c-48adc5af9ce8",
  "sourceToolAssistantUUID": "ecf1584f-97fc-4dfd-b897-3c0ec8d291e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-15T19:58:31.346Z_

Good! I found exp_017_llama_conll_infer. Let me also look for LLaMA SciERC inference. Let me read these sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "640ec088-d9bf-40da-a51c-48adc5af9ce8",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wqdZomVvXVRDScxfTX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0c7f6f9b-1d4f-4aab-be1b-acff1eab043a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sf2BgdrwiNoYm8xYMGzEn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1471,
      "cache_read_input_tokens": 41246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1471,
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

_source line 51 · 2026-05-15T19:58:32.153Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AzYBamTQAiUtqvF2oDuARV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml",
  "offset": 1673,
  "limit": 180
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c7f6f9b-1d4f-4aab-be1b-acff1eab043a",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wqdZomVvXVRDScxfTX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "80720667-aecb-46ed-8ef7-e574580363bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sf2BgdrwiNoYm8xYMGzEn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1471,
      "cache_read_input_tokens": 41246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1471,
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

_source line 52 · 2026-05-15T19:58:32.161Z_

<details><summary>↩ Tool result · `toolu_01AzYBamTQAiUtqvF2oDuARV`</summary>

```text
1673	  exp_007_llama_inference:
1674	    status: DONE
1675	    retry_count: 0
1676	    created_at: '2026-05-14T13:54:48.055Z'
1677	    updated_at: '2026-05-14T14:28:32.909Z'
1678	    spec:
1679	      command: python run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged
1680	        --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples
1681	        8 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir
1682	        output/exp007_llama_inference/
1683	      server: autodl-5090
1684	      gpu:
1685	      - cuda:0
1686	      pid: '75172'
1687	      log_path: ~/runs/struct_self_consist_ie/exp_007_llama_inference.log
1688	      submitted_at: '2026-05-14T13:54:47.962Z'
1689	      submitted_via: submit_training_job
1690	      backend: tmux
1691	      account: root
1692	      data_path: data/scierc/processed_data
1693	      data_count: 551
1694	      model_name: Meta-Llama-3.1-8B-Instruct (LoRA fine-tuned on SciERC)
1695	      seed: 42
1696	      checkpoint_source: checkpoints/llama3.1-8b-scierc-merged
1697	      description: LLaMA-3.1-8B SciERC joint inference (NER+RE) with 8 samples, T=1.0,
1698	        logprobs collected.
1699	      wall_clock_seconds: 1038.5
1700	      gpu_hours: 0.29
1701	    log_path: output/exp007_llama_inference/
1702	    checkpoint_path: N/A
1703	    metrics:
1704	      ner:
1705	        greedy_f1: 0.66
1706	        oracle_f1: 0.781
1707	        headroom: 0.121
1708	        rho_fk: 0.327
1709	        rho_sj: 0.363
1710	        rho_fk_cond: 0.226
1711	        rho_sj_cond: 0.311
1712	        rho_logprob: 0.183
1713	        rho_logprob_cond: 0.109
1714	        structural_beats_surface: true
1715	        sample_f1_pct_zero: 11.6
1716	      re:
1717	        greedy_f1: 0.434
1718	        oracle_f1: 0.568
1719	        headroom: 0.135
1720	        rho_fk: 0.305
1721	        rho_sj: 0.299
1722	        rho_fk_cond: 0.259
1723	        rho_sj_cond: 0.405
1724	        rho_logprob: 0.288
1725	        rho_logprob_cond: 0.092
1726	        structural_beats_surface: false
1727	        sample_f1_pct_zero: 41.2
1728	      n_instances: 551
1729	      N: 8
1730	      T: 1
1731	      seed: 42
1732	      model: LLaMA-3.1-8B-Instruct
1733	      verdict: FAIL
1734	      verdict_note: RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0
1735	    conclusion: success
1736	    completed_at: '2026-05-14T14:12:06.442Z'
1737	  exp_001_seed42_v2:
1738	    status: DONE
1739	    retry_count: 0
1740	    created_at: '2026-05-14T14:34:02.350Z'
1741	    updated_at: '2026-05-14T15:23:52.846Z'
1742	    spec:
1743	      description: NER N=16 on SciERC, seed=42, ft_002_v2, with logprobs
1744	      hypothesis: Structural consistency (Fleiss kappa, Soft Jaccard) correlates with
1745	        per-instance NER F1 on SciERC
1746	      server: autodl-5090
1747	      data_path: data/scierc/processed_data
1748	      data_count: 551
1749	      model_name: ft_002_v2
1750	      seed: 42
1751	      command: CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py
1752	        --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data
1753	        --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42
1754	        --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed42_v2
1755	      gpu:
1756	      - cuda:1
1757	      pid: '78728'
1758	      backend: tmux
1759	      account: root
1760	      log_path: output/exp_001_seed42_v2/run.log
1761	    conclusion: success
1762	    metrics:
1763	      sj_rho_full: 0.428
1764	      sj_rho_cond: 0.369
1765	      structural_minus_surface: 0.147
1766	      conclusion_note: NER seed42 robustness confirmed, structural>surface +0.147
1767	    checkpoint_path: N/A (inference)
1768	    completed_at: '2026-05-14T15:23:34.091Z'
1769	    log_path: output/exp_001_seed42_v2/
1770	  exp_001_seed123_v2:
1771	    status: DONE
1772	    retry_count: 0
1773	    created_at: '2026-05-14T14:34:04.210Z'
1774	    updated_at: '2026-05-14T15:23:56.155Z'
1775	    spec:
1776	      description: NER N=16 on SciERC, seed=123, ft_002_v2, with logprobs
1777	      hypothesis: Structural consistency (Fleiss kappa, Soft Jaccard) correlates with
1778	        per-instance NER F1 on SciERC (seed robustness check)
1779	      server: autodl-5090
1780	      data_path: data/scierc/processed_data
1781	      data_count: 551
1782	      model_name: ft_002_v2
1783	      seed: 123
1784	      command: CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py
1785	        --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data
1786	        --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123
1787	        --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed123_v2
1788	      gpu:
1789	      - cuda:2
1790	      pid: '78733'
1791	      backend: tmux
1792	      account: root
1793	      log_path: output/exp_001_seed123_v2/run.log
1794	    conclusion: success
1795	    metrics:
1796	      sj_rho_full: 0.424
1797	      sj_rho_cond: 0.376
1798	      structural_minus_surface: 0.149
1799	      conclusion_note: NER seed123 robustness confirmed, structural>surface +0.149
1800	    checkpoint_path: N/A (inference)
1801	    completed_at: '2026-05-14T15:23:35.076Z'
1802	    log_path: output/exp_001_seed123_v2/
1803	  exp_008_re_n16_v2:
1804	    status: DONE
1805	    retry_count: 0
1806	    created_at: '2026-05-14T14:34:06.296Z'
1807	    updated_at: '2026-05-14T15:23:59.395Z'
1808	    spec:
1809	      description: RE N=16 on SciERC full set confirmation, ft_002_v2, with logprobs
1810	      hypothesis: Structural consistency correlates with per-instance RE F1 on SciERC
1811	        full dataset
1812	      server: autodl-5090
1813	      data_path: data/scierc/processed_data
1814	      data_count: 551
1815	      model_name: ft_002_v2
1816	      seed: 42
1817	      command: CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py
1818	        --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data
1819	        --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --num_test
1820	        9999 --collect_logprobs --output_dir output/exp_008_re_n16_v2
1821	      gpu:
1822	      - cuda:3
1823	      pid: '78737'
1824	      backend: tmux
1825	      account: root
1826	      log_path: output/exp_008_re_n16_v2/run.log
1827	    conclusion: negative
1828	    metrics:
1829	      sj_rho_full: 0.281
1830	      sj_rho_cond: 0.308
1831	      f1_zero_pct: 44.3
1832	      conclusion_note: 'RE N=16 v2 negative: SJ weak, 44.3% F1=0'
1833	    checkpoint_path: N/A (inference)
1834	    completed_at: '2026-05-14T15:23:35.598Z'
1835	    log_path: output/exp_008_re_n16_v2/
1836	  exp_017_llama_conll:
1837	    status: DONE
1838	    retry_count: 0
1839	    created_at: '2026-05-14T14:39:32.014Z'
1840	    updated_at: '2026-05-14T17:30:26.798Z'
1841	    spec:
1842	      command: llamafactory-cli train train_config_llama_conll2003.yaml
1843	      server: autodl-5090
1844	      data_path: /root/autodl-tmp/struct_self_consist_ie/data/conll2003
1845	      data_count: 14041
1846	      model_name: Meta-Llama-3.1-8B-Instruct
1847	      seed: 42
1848	      failure_reason: null
1849	      metrics:
1850	        train_loss: 0.039
1851	        eval_loss: 0.023
1852	        epochs: 5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80720667-aecb-46ed-8ef7-e574580363bf",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "0daf3970-4d9c-493e-b213-dda46faa0d71",
  "sourceToolAssistantUUID": "80720667-aecb-46ed-8ef7-e574580363bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T19:58:32.484Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MR9ak8tNk1Jap15b2sUfSv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml",
  "offset": 2501,
  "limit": 180
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0daf3970-4d9c-493e-b213-dda46faa0d71",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wqdZomVvXVRDScxfTX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "06e00a32-e877-449d-8937-e585fe03d499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sf2BgdrwiNoYm8xYMGzEn6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1471,
      "cache_read_input_tokens": 41246,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1471
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 262,
          "cache_read_input_tokens": 41246,
          "cache_creation_input_tokens": 1471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1471,
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

_source line 54 · 2026-05-15T19:58:32.495Z_

<details><summary>↩ Tool result · `toolu_01MR9ak8tNk1Jap15b2sUfSv`</summary>

```text
2501	  exp_017_llama_conll_infer:
2502	    status: DONE
2503	    retry_count: 0
2504	    created_at: '2026-05-14T17:33:23.653Z'
2505	    updated_at: '2026-05-14T17:55:35.572Z'
2506	    spec:
2507	      hypothesis: 'LLaMA-3.1-8B CoNLL-2003 inference: cross-model cross-dataset validation
2508	        of structural consistency signals'
2509	      plan_id: exp-017
2510	      parent: exp_017_llama_conll
2511	      command: python code/run_llama_conll_infer.py
2512	      server: autodl-5090
2513	      data_path: conll2003 test
2514	      data_count: 3453
2515	      model_name: LLaMA-3.1-8B-Instruct
2516	      seed: 42
2517	      n_samples: 8
2518	      temperature: 1
2519	      description: LLaMA CoNLL-2003 NER inference N=8 (cross-model + cross-dataset
2520	        validation)
2521	    metrics:
2522	      greedy_f1: 0.9266
2523	      oracle_f1: 0.9443
2524	      oracle_headroom: 0.0177
2525	      n_instances: 3453
2526	      n_valid: 2756
2527	      n_conditional: 2642
2528	      N: 8
2529	      full:
2530	        SJ_rho: 0.4314
2531	        FK_rho: 0.4277
2532	        logprob_rho: 0.3072
2533	        EM_rho: 0.4306
2534	        voting_conf_rho: 0.4256
2535	        SJ_AUROC: 0.7039
2536	        FK_AUROC: 0.7026
2537	        logprob_AUROC: 0.761
2538	        EM_AUROC: 0.7046
2539	        voting_conf_AUROC: 0.7088
2540	        SJ_ECE: 0.1137
2541	        FK_ECE: 0.1053
2542	        logprob_ECE: 0.129
2543	        EM_ECE: 0.1094
2544	        voting_conf_ECE: 0.0949
2545	      conditional:
2546	        SJ_rho: 0.4356
2547	        FK_rho: 0.431
2548	        logprob_rho: 0.3282
2549	        EM_rho: 0.4403
2550	        voting_conf_rho: 0.3743
2551	        SJ_AUROC: 0.7225
2552	        FK_AUROC: 0.7208
2553	        logprob_AUROC: 0.8102
2554	        EM_AUROC: 0.7257
2555	        voting_conf_AUROC: 0.6989
2556	        SJ_ECE: 0.0829
2557	        FK_ECE: 0.0796
2558	        logprob_ECE: 0.0922
2559	        EM_ECE: 0.0754
2560	        voting_conf_ECE: 0.0784
2561	    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl
2562	    log_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/
2563	    conclusion: success
2564	    completed_at: '2026-05-14T17:55:33.476Z'
2565	    notes: 'LLaMA CoNLL-2003 NER N=8 (not N=16, cost constraint: 3453 test instances).
2566	      SJ ρ=0.431 > logprob ρ=0.307 (Δ=+0.124). ρ-AUROC dissociation: logprob AUROC=0.761
2567	      > SJ AUROC=0.704. All 4 structural signals ρ>0.42 vs logprob 0.31. Directly
2568	      comparable to exp_002 (Qwen CoNLL N=8) and exp_007 (LLaMA SciERC N=8).'
2569	  exp_002_conll_n16:
2570	    status: DONE
2571	    retry_count: 0
2572	    created_at: '2026-05-14T18:12:16.041Z'
2573	    updated_at: '2026-05-14T19:03:19.801Z'
2574	    spec:
2575	      hypothesis: 'Qwen CoNLL-2003 N=16: cross-dataset N-scaling comparison with SciERC
2576	        N=16'
2577	      plan_id: exp-002
2578	      parent: exp_002_ner_conll2003
2579	      command: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
2580	        && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code
2581	        python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged
2582	        --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16
2583	        --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir
2584	        output/exp_002_conll_n16
2585	      server: autodl-5090
2586	      data_path: data/conll2003
2587	      data_count: 3453
2588	      model_name: qwen3-8b-conll2003-merged
2589	      seed: 42
2590	    conclusion: success
2591	    metrics:
2592	      N: 16
2593	      dataset: conll2003
2594	      subtask: ner
2595	      n_instances: 3453
2596	      n_valid: 2756
2597	      n_conditional: 2614
2598	      greedy_f1: 0.907
2599	      full:
2600	        SJ_rho: 0.4496
2601	        FK_rho: 0.3928
2602	        logprob_rho: 0.3146
2603	        EM_rho: 0.4627
2604	        voting_conf_rho: 0.4286
2605	        SJ_AUROC: 0.8264
2606	        FK_AUROC: 0.7821
2607	        logprob_AUROC: 0.7531
2608	        EM_AUROC: 0.8409
2609	        voting_conf_AUROC: 0.8071
2610	        SJ_ECE: 0.0747
2611	        FK_ECE: 0.1786
2612	        logprob_ECE: 0.2031
2613	        EM_ECE: 0.0786
2614	        voting_conf_ECE: 0.529
2615	      conditional:
2616	        SJ_rho: 0.4208
2617	        FK_rho: 0.3494
2618	        logprob_rho: 0.3756
2619	        EM_rho: 0.4658
2620	        voting_conf_rho: 0.3654
2621	        SJ_AUROC: 0.8405
2622	        FK_AUROC: 0.7819
2623	        logprob_AUROC: 0.8259
2624	        EM_AUROC: 0.8781
2625	        voting_conf_AUROC: 0.7951
2626	        SJ_ECE: 0.0982
2627	        FK_ECE: 0.1899
2628	        logprob_ECE: 0.2504
2629	        EM_ECE: 0.0997
2630	        voting_conf_ECE: 0.6096
2631	      n8_vs_n16_delta_rho_full:
2632	        SJ: 0.0139
2633	        FK: -0.007
2634	        logprob: -0.0011
2635	        EM: 0.012
2636	        voting_conf: 0.0049
2637	    checkpoint_path: output/exp_002_conll_n16/samples.jsonl
2638	    log_path: output/exp_002_conll_n16.log
2639	    completed_at: '2026-05-14T18:58:40.473Z'
2640	  exp_007_llama_n16:
2641	    status: DONE
2642	    retry_count: 0
2643	    created_at: '2026-05-14T18:31:44.366Z'
2644	    updated_at: '2026-05-14T19:03:50.284Z'
2645	    spec:
2646	      hypothesis: 'LLaMA SciERC N=16: cross-model N-scaling validation. If SJ rho
2647	        increases from N=8 (0.363) to N=16, N-scaling is model-agnostic.'
2648	      plan_id: exp-007
2649	      parent: exp_007_llama_inference
2650	      command: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
2651	        && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code
2652	        python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged
2653	        --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples
2654	        16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir
2655	        output/exp_007_llama_n16
2656	      server: autodl-5090
2657	      data_path: data/scierc/processed_data
2658	      data_count: 551
2659	      model_name: llama3.1-8b-scierc-merged
2660	      seed: 42
2661	      checkpoint_source: checkpoints/llama3.1-8b-scierc-merged
2662	      eval_data: data/scierc/processed_data
2663	    conclusion: success
2664	    checkpoint_path: output/exp_007_llama_n16/samples.jsonl
2665	    log_path: output/exp_007_llama_n16.log
2666	    completed_at: '2026-05-14T19:03:39.163Z'
2667	    metrics:
2668	      N: 16
2669	      dataset: scierc
2670	      subtask: ner
2671	      n_instances: 551
2672	      n_valid: 529
2673	      n_conditional: 478
2674	      greedy_f1: 0.645
2675	      full:
2676	        SJ_rho: 0.3791
2677	        FK_rho: 0.3081
2678	        logprob_rho: 0.2041
2679	        EM_rho: 0.3159
2680	        voting_conf_rho: 0.4515
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06e00a32-e877-449d-8937-e585fe03d499",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "3023dd02-4f9a-47f0-8a1a-50e8b8039435",
  "sourceToolAssistantUUID": "06e00a32-e877-449d-8937-e585fe03d499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-15T19:58:33.974Z_

Perfect! Now let me search for the Qwen CoNLL N=8 results. Let me look for exp_002 metrics more carefully:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3023dd02-4f9a-47f0-8a1a-50e8b8039435",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wqqMURPfqnbuvrf1T5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9405e322-c24a-4e35-b1da-8c6d15597580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012qyRLHPFGY5tddAGcP1ibF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6726,
      "cache_read_input_tokens": 42717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6726,
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

_source line 56 · 2026-05-15T19:58:35.109Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WSAk4V4U7URe5WTUTHfbgc`</summary>

```json
{
  "command": "grep -A 200 \"exp_002_ner_conll2003:\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml | grep -A 100 \"metrics:\" | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9405e322-c24a-4e35-b1da-8c6d15597580",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wqqMURPfqnbuvrf1T5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bc70ae86-69ce-4022-942e-18b60ceb3f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012qyRLHPFGY5tddAGcP1ibF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6726,
      "cache_read_input_tokens": 42717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6726,
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

_source line 57 · 2026-05-15T19:58:35.169Z_

<details><summary>↩ Tool result · `toolu_01WSAk4V4U7URe5WTUTHfbgc`</summary>

```text
    metrics:
      ner:
        greedy_f1: 0.525
        oracle_f1: 0.664
        headroom: 0.139
        rho_sj_full: 0.082
        rho_fk_full: 0.124
        rho_logprob_full: -0.414
        rho_sj_cond: 0.275
        rho_fk_cond: 0.164
        rho_logprob_cond: 0.352
        sj_beats_logprob_cond: false
      n_instances: 1287
      n_gold_empty: 598
      sample_f1_mean: 0.401
      sample_f1_pct_zero: 53.7
      N: 16
      T: 1
      seed: 42
      verdict: FAIL
      verdict_note: '>30% samples F1=0; structural rho weak; logprob baseline stronger'
    conclusion: negative
    log_path: output/exp003_wnut17_pilot/
    completed_at: '2026-05-14T13:40:20.979Z'
  exp_007_ner_multi_model:
    status: DONE
    retry_count: 0
    created_at: '2026-05-14T11:42:20.748Z'
    updated_at: '2026-05-14T13:35:43.251Z'
    spec:
      command: bash -c 'source env.sh && cd /root/autodl-tmp/struct_self_consist_ie
        && llamafactory-cli train train_config_llama.yaml'
      server: gpu-5090-4x-2
      gpu:
      - cuda:0
      pid: '60970'
      log_path: ~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log
      submitted_at: '2026-05-14T12:43:09.108Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      data_path: /root/autodl-tmp/struct_self_consist_ie/data
      data_count: 1861
      model_name: LLaMA-3.1-8B-Instruct
      seed: 42
      log_file: ~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log
      wall_clock_seconds: 165.8
      gpu_hours: 0.05
    server: autodl-5090
    gpu: cuda:3
    account: root
    reproduce:
      server: autodl-5090
      gpu: cuda:3
      started_at: '2026-05-14T11:43:50.977Z'
    conclusion: success
    completed_at: '2026-05-14T12:45:54.952Z'
    checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-lora
    metrics:
      epoch: 5
      train_loss: 0.0767
      eval_loss: 0.1049
      train_runtime_sec: 1494.5
      train_samples_per_second: 6.226
      checkpoints:
      - checkpoint-400
      - checkpoint-500
      - checkpoint-585
      base_model: Meta-Llama-3.1-8B-Instruct
      lora_r: 32
      lora_alpha: 64
      note: EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal.
        Checkpoint fully intact.
    log_path: ~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log
  exp_007_ner_llama:
    status: DONE
    retry_count: 0
    created_at: '2026-05-14T11:42:21.510Z'
    updated_at: '2026-05-15T12:41:27.410Z'
    spec:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc70ae86-69ce-4022-942e-18b60ceb3f40",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "2b1bd8db-ebc0-4077-93e6-b98a513abf34",
  "sourceToolAssistantUUID": "bc70ae86-69ce-4022-942e-18b60ceb3f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-15T19:58:35.222Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EXJAHgbSJyXVSU9xN3DBg7`</summary>

```json
{
  "command": "sed -n '1318,1450p' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b1bd8db-ebc0-4077-93e6-b98a513abf34",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wqqMURPfqnbuvrf1T5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bbdfa38f-6d41-47f7-abcf-23afe7b8c6dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012qyRLHPFGY5tddAGcP1ibF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6726,
      "cache_read_input_tokens": 42717,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6726
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 228,
          "cache_read_input_tokens": 42717,
          "cache_creation_input_tokens": 6726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6726,
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

_source line 59 · 2026-05-15T19:58:35.278Z_

<details><summary>↩ Tool result · `toolu_01EXJAHgbSJyXVSU9xN3DBg7`</summary>

```text
  exp_002_merge_conll2003:
    status: DONE
    retry_count: 0
    created_at: '2026-05-14T12:25:56.211Z'
    updated_at: '2026-05-15T12:41:26.419Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0
        llamafactory-cli export export_config_conll2003.yaml > /tmp/merge_conll2003.log
        2>&1 && echo 'MERGE_DONE' >> /tmp/merge_conll2003.log"
      server: autodl-5090
      gpu:
      - cuda:0
      pid: '57524'
      log_path: ~/runs/struct_self_consist_ie/exp_002_merge_conll2003.log
      submitted_at: '2026-05-14T12:25:56.139Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      failure_reason: Superseded by exp_002_ner_conll2003 (completed on autodl-5090)
      wall_clock_seconds: 87330.3
      gpu_hours: 24.26
    conclusion: killed
    failure_reason: superseded by exp_002_ner_conll2003 (DONE)
    notes: Completed as exp_002_conll_n16 on autodl-5090. Registry status corrected.
    completed_at: '2026-05-15T12:41:26.419Z'
  exp_002:
    status: DONE
    retry_count: 0
    created_at: '2026-05-14T12:39:53.226Z'
    updated_at: '2026-05-14T12:40:17.202Z'
    spec:
      command: python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged
        --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --collect_logprobs
        --num_test 99999
      server: autodl-5090
      data_path: data/conll2003
      data_count: 3453
      model_name: qwen3-8b-conll2003-lora-merged
      seed: 42
      checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged
      log_path: /tmp/pilot_conll2003.log
    conclusion: success
    completed_at: '2026-05-14T12:40:08.402Z'
    metrics:
      sj_rho_full: 0.4357
      sj_tau_full: 0.3851
      sj_auroc_full: 0.8008
      sj_rho_cond: 0.4511
      fk_rho_full: 0.3998
      fk_tau_full: 0.3568
      fk_auroc_full: 0.7741
      fk_rho_cond: 0.4064
      logprob_rho_full: 0.3157
      logprob_tau_full: 0.2469
      logprob_auroc_full: 0.7532
      logprob_rho_cond: 0.3562
      em_rho_full: 0.4507
      em_tau_full: 0.4002
      em_auroc_full: 0.8156
      em_rho_cond: 0.4799
      ev_rho_full: 0.4237
      ev_tau_full: 0.3777
      ev_auroc_full: 0.7889
      ev_rho_cond: 0.4127
      greedy_f1: 0.9123
      oracle_f1: 0.9543
      voting_f1: 0.9141
      oracle_headroom: 0.042
      sj_vs_logprob_delta_rho: 0.12
      sj_vs_logprob_ci_low: 0.0881
      sj_vs_logprob_ci_high: 0.154
      sj_vs_logprob_significant: true
      n_instances: 3453
      n_valid: 2756
      n_samples: 8
      temperature: 1
  exp_001_n16_seed123_full:
    status: DONE
    retry_count: 0
    created_at: '2026-05-14T12:43:47.915Z'
    updated_at: '2026-05-15T12:41:29.068Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0
        python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2
        --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples
        16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir
        output/exp001_n16_seed123_full/"
      server: gpu-5090-4x-2
      gpu:
      - cuda:0
      pid: '61812'
      log_path: ~/runs/struct_self_consist_ie/exp_001_n16_seed123_full.log
      submitted_at: '2026-05-14T12:44:06.059Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      failure_reason: Superseded by exp_001_seed123_v2 (NER-only on autodl-5090)
      wall_clock_seconds: 86243.0
      gpu_hours: 23.96
    conclusion: killed
    failure_reason: superseded by v2
    completed_at: '2026-05-15T12:41:29.068Z'
  exp_001_n16_seed456_full:
    status: DONE
    retry_count: 0
    created_at: '2026-05-14T12:44:31.348Z'
    updated_at: '2026-05-15T12:41:30.065Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1
        python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2
        --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples
        16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir
        output/exp001_n16_seed456/"
      server: gpu-5090-4x-2
      gpu:
      - cuda:1
      pid: '62170'
      log_path: ~/runs/struct_self_consist_ie/exp_001_n16_seed456_full.log
      submitted_at: '2026-05-14T12:44:31.087Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      failure_reason: Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)
      wall_clock_seconds: 86219.0
      gpu_hours: 23.95
    conclusion: killed
    failure_reason: superseded by v2
    completed_at: '2026-05-15T12:41:30.065Z'
  exp_008_re_n16_full:
    status: DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbdfa38f-6d41-47f7-abcf-23afe7b8c6dd",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "6bcbe02e-349a-41bd-a78e-ccf8203224e9",
  "sourceToolAssistantUUID": "bbdfa38f-6d41-47f7-abcf-23afe7b8c6dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-15T19:58:37.729Z_

Excellent! Now let me also get the Qwen SciERC N=8 data. I need to look at mvp_pilot_004 more carefully which I already saw:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bcbe02e-349a-41bd-a78e-ccf8203224e9",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wr3DrQ5gNWzKUt1AGY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f5f3a28d-95b0-46bd-9ba5-97f8069ad0cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E4tZjNSxE3xvdeqzyD1M8M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 52843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 61 · 2026-05-15T19:58:37.836Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012SCXRyBmZG8dBGjwzTPyTb`</summary>

```json
{
  "command": "sed -n '575,640p' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5f3a28d-95b0-46bd-9ba5-97f8069ad0cf",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wr3DrQ5gNWzKUt1AGY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "693d33aa-2bfc-4bca-9b96-731e9cca41dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E4tZjNSxE3xvdeqzyD1M8M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 52843,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 135,
          "cache_read_input_tokens": 52843,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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

_source line 62 · 2026-05-15T19:58:37.891Z_

<details><summary>↩ Tool result · `toolu_012SCXRyBmZG8dBGjwzTPyTb`</summary>

```text
  exp_001_ner_n16_scierc:
    status: DONE
    retry_count: 0
    created_at: '2026-05-14T11:42:10.898Z'
    updated_at: '2026-05-14T12:42:49.592Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0
        python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2
        --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples
        16 --temperature 1.0 --seed 42 --output_dir output/exp001_n16_seed42 --num_test
        9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed42_run.log"
      server: autodl-5090
      gpu:
      - cuda:0
      pid: '54357'
      log_path: ~/runs/struct_self_consist_ie/exp_001_ner_n16_scierc.log
      submitted_at: '2026-05-14T12:15:46.646Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
    server: autodl-5090
    gpu: cuda:0
    account: root
    reproduce:
      server: autodl-5090
      gpu: cuda:0
      started_at: '2026-05-14T11:43:48.643Z'
    conclusion: success
    completed_at: '2026-05-14T11:55:45.664Z'
    metrics:
      n_instances: 551
      ner_n: 529
      re_n: 397
      N: 16
      T: 1
      seed: 42
      full_test_set: true
      ner_voting_conf_rho: 0.399
      ner_sj_rho: 0.398
      ner_em_rho: 0.339
      ner_fk_rho: 0.288
      ner_logprob_rho: 0.237
      ner_voting_conf_auroc: 0.704
      ner_sj_auroc: 0.697
      ner_cond_em_rho: 0.414
      ner_cond_sj_rho: 0.349
      ner_cond_vc_rho: 0.34
      re_voting_conf_rho: 0.38
      re_logprob_rho: 0.293
      re_fk_rho: 0.281
      re_sj_rho: 0.277
      re_em_rho: 0.148
      re_voting_conf_auroc: 0.699
      re_cond_em_rho: 0.475
      re_cond_sj_rho: 0.318
      re_cond_vc_rho: 0.35
      re_cond_em_auroc: 0.742
      diagnosis: '551 instances T=1.0: voting_conf best on full set (NER 0.399, RE
        0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475).
        RE full FAIL (SJ 0.277 < 0.40). Previous N-scaling ''breakthrough'' was artifact
        of 200 instances + T=0.7.'
  exp_002_ner_conll2003:
    status: DONE
    retry_count: 0
    created_at: '2026-05-14T11:42:15.223Z'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "693d33aa-2bfc-4bca-9b96-731e9cca41dd",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "eb678108-f8b5-43df-aa70-3b230671b0f8",
  "sourceToolAssistantUUID": "693d33aa-2bfc-4bca-9b96-731e9cca41dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-15T19:58:39.638Z_

Now let me look at the paper's experiments.tex more carefully for the official table numbers. Let me search for Table 2 and Table 3:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb678108-f8b5-43df-aa70-3b230671b0f8",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wrEPKRK3YvP8UPXY3J",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "96c09b18-d35f-47c1-be19-f812bbdab848",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BmeBCFfhDVtXjUKekfpt7v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 4541,
      "cache_read_input_tokens": 49443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4541,
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

_source line 64 · 2026-05-15T19:58:40.822Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HQu4dV9Ft7AnCb9JGDYBgw`</summary>

```json
{
  "command": "grep -n \"Table 2\\|Table 3\\|table.*8b\\|table.*Qwen\\|table.*LLaMA\\|greedy_f1.*oracle\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96c09b18-d35f-47c1-be19-f812bbdab848",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wrEPKRK3YvP8UPXY3J",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e6c3307c-db81-4d9f-bca0-83f311550119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BmeBCFfhDVtXjUKekfpt7v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 4541,
      "cache_read_input_tokens": 49443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4541,
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

_source line 65 · 2026-05-15T19:58:40.872Z_

<details><summary>↩ Tool result · `toolu_01HQu4dV9Ft7AnCb9JGDYBgw`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6c3307c-db81-4d9f-bca0-83f311550119",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "f37b371b-9937-49d5-a13c-117d9b2aa775",
  "sourceToolAssistantUUID": "e6c3307c-db81-4d9f-bca0-83f311550119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-15T19:58:41.240Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A8xrJrCkfDwTRKN8syiqBM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 1,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f37b371b-9937-49d5-a13c-117d9b2aa775",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wrEPKRK3YvP8UPXY3J",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5a67be69-4b89-4bac-bda3-b756e81c8356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BmeBCFfhDVtXjUKekfpt7v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 4541,
      "cache_read_input_tokens": 49443,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4541
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 278,
          "cache_read_input_tokens": 49443,
          "cache_creation_input_tokens": 4541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4541,
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

_source line 67 · 2026-05-15T19:58:41.246Z_

<details><summary>↩ Tool result · `toolu_01A8xrJrCkfDwTRKN8syiqBM`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N$-scaling analysis (Appendix~\ref{app:n_scaling}) shows sublinear gains beyond $N{=}8$; 3-seed stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirms identical signal rankings across seeds.}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best per column in \textbf{bold}. SciERC: joint NER (6 types) and RE (7 types, preliminary); CoNLL: NER (4 types). $N{=}16$ in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
31	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
32	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
33	\midrule
34	VC & Structural & \textbf{.379} & \textbf{.663} & \textbf{.350} & .694 & .424 & .789 & .426 & .709 \\
35	SJ  & Structural & .360 & .650 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
36	FK & Surface & .267 & .602 & .275 & .609 & .400 & .774 & .428 & .703 \\
37	EM  & Surface    & .295 & .614 & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
38	\midrule
39	LP     & Model      & .205 & .578 & .266 & .601 & .316 & .753 & .307 & \textbf{.761} \\
40	\bottomrule
41	\end{tabular}
42	\end{table*}
43	
44	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.\footnote{$\varepsilon{=}0.05$ is a convenience threshold used only in the selection analysis (\S\ref{sec:selection_gap}); quality estimation metrics ($\rho$, AUROC) are continuous and $\varepsilon$-free. Selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}).}
45	
46	\paragraph{Difficulty-dependent signal complementarity.}
47	On SciERC NER, structural signals lead: VC $\rho{=}0.379$, SJ $\rho{=}0.360$, outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$); on RE (preliminary), LP rises above SJ and FK in multi-seed analysis (Table~\ref{tab:multiseed}), likely because RE's 40\% zero-F1 rate favors generation confidence.
48	The best NER AUROC reaches 0.816 (EM, CoNLL Qwen); pairwise bootstrap CIs confirm the SJ--LP gap on SciERC NER ($\Delta\rho{=}{+}0.155$, CI excludes zero; Appendix~\ref{app:bootstrap_signal}).
49	Signal choice depends on use case: EM leads AUROC but not $\rho$ on CoNLL, preferred for binary triage; this $\rho$--AUROC dissociation replicates across configurations.
50	
51	\paragraph{Signal rankings shift with task difficulty.}
52	On CoNLL (greedy F1${\approx}$0.91), EM leads; on SciERC, structural signals dominate---demonstrating difficulty-dependent complementarity consistent across model families.
53	On WNUT-17 (52\% zero F1), all conditional signals collapse (Table~\ref{tab:wnut}), suggesting a capability boundary beyond which consistency captures binary success/failure but not quality gradation.
54	Restricting to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, Appendix~\ref{app:additional}): EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while LP RE collapses to $\rho{=}0.011$.
55	
56	%% ============================================================
57	\subsection{The Correlation-Selection Gap}
58	\label{sec:selection_gap}
59	
60	\begin{table}[t]
61	\centering
62	\small
63	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). NER: 2-seed mean${\pm}\sigma$ ($\sigma$ from 2 seeds; indicative only), Fisher combined $p$ vs.\ greedy; RE: single seed (preliminary). Best non-oracle in \textbf{bold}. $^\dagger$Greedy: a fixed $T{=}1.0$ sample.}
64	\label{tab:selection}
65	\begin{tabular}{lccc}
66	\toprule
67	Method & NER F1 & $p$ & RE F1 \\
68	\midrule
69	Oracle & $0.778 \pm 0.003$ & --- & 0.585 \\
70	\midrule
71	\multicolumn{4}{l}{\textit{Per-sample signal}} \\
72	LP           & $\mathbf{0.647} \pm 0.005$ & .29 & 0.395 \\
73	\midrule
74	\multicolumn{4}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
75	SJ           & $0.646 \pm 0.002$ & .68 & 0.386 \\
76	FK           & $0.646 \pm 0.001$ & .79 & --- \\
77	EM           & $0.637 \pm 0.001$ & .45 & 0.372 \\
78	VC           & $0.623 \pm 0.004$ & .26 & 0.359 \\
79	\midrule
80	Greedy$^\dagger$ & $0.645 \pm 0.001$ & --- & \textbf{0.404} \\
81	Random           & $0.610 \pm 0.003$ & --- & 0.354 \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	Despite strong quality estimation, confidence signals yield limited gains for best-of-$N$ selection (Table~\ref{tab:selection}; see also Figure~\ref{fig:selection_gap}).
87	Four of five signals are instance-level by construction (they assign identical scores to all candidates); the non-trivial question is whether LP---the only per-sample signal---can exploit the oracle headroom.
88	We anchor on SciERC, where output diversity is substantial (39--43\% unique outputs; Appendix~\ref{app:diversity}).
89	
90	\paragraph{No significant improvement over greedy.}
91	We evaluate significance via 2-seed instance-level sign tests ($n{=}551$, Fisher combination).
92	On NER, the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645).
93	LP achieves the highest mean selection F1 (0.647), indistinguishable from greedy ($\Delta{=}{+}0.2$~pp, $p{=}0.29$); all other signals also fail to reach significance (all $p{>}0.05$; Table~\ref{tab:selection}).
94	On RE, the best signal (LP, 0.395) falls below greedy (0.404; single seed, preliminary), while 18.1~pp of oracle headroom remains.
95	The pattern is consistent across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}).
96	
97	\paragraph{Quality estimation $\neq$ output selection.}
98	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; when per-sample variance is low, even perfect quality estimation fails to discriminate.
99	Closing this gap likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
100	
101	%% ============================================================
102	\subsection{Robustness}
103	\label{sec:robustness_main}
104	
105	Consistency-based signals (SJ, FK, EM, VC) are robust across $T{\in}\{0.7, 1.0\}$ and show sublinear gains from $N{=}8$ to $N{=}16$ (Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}); LP is excluded from this robustness claim, exhibiting the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$ on NER).
106	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}); RE miscalibration (ECE up to 0.339, preliminary) imposes a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a67be69-4b89-4bac-bda3-b756e81c8356",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "2c638c9b-2d07-488f-8496-0196fe21053b",
  "sourceToolAssistantUUID": "5a67be69-4b89-4bac-bda3-b756e81c8356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-15T19:58:43.190Z_

The experiments.tex shows Table 1 (quality estimation) but I need to find the actual F1 numbers. Let me search for the full file to see if there are more tables:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c638c9b-2d07-488f-8496-0196fe21053b",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wrUm1XcquAxo7BsJCx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "87819d79-4d9a-4225-b8fe-7dbc791f22b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUPyctcMp8toesgtQSEc54",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 53984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3501,
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

_source line 69 · 2026-05-15T19:58:44.276Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SWT2JosnBa96tn48qYP1H4`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87819d79-4d9a-4225-b8fe-7dbc791f22b7",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wrUm1XcquAxo7BsJCx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "403c3131-7ac2-4009-a1c4-018b462c1c4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUPyctcMp8toesgtQSEc54",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 53984,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3501
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 218,
          "cache_read_input_tokens": 53984,
          "cache_creation_input_tokens": 3501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3501,
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

_source line 70 · 2026-05-15T19:58:44.282Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013mZDfEQDo2ftNXfG9fDjNk`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\begin{table\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "403c3131-7ac2-4009-a1c4-018b462c1c4d",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wrUm1XcquAxo7BsJCx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "97b4d4a1-fa86-4fde-9560-0218e886f136",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUPyctcMp8toesgtQSEc54",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 53984,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3501
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 218,
          "cache_read_input_tokens": 53984,
          "cache_creation_input_tokens": 3501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3501,
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

_source line 71 · 2026-05-15T19:58:44.355Z_

<details><summary>↩ Tool result · `toolu_013mZDfEQDo2ftNXfG9fDjNk`</summary>

```text
23:\begin{table*}[t]
60:\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97b4d4a1-fa86-4fde-9560-0218e886f136",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "1e7c634f-e116-455a-b00c-167e551e0a2f",
  "sourceToolAssistantUUID": "97b4d4a1-fa86-4fde-9560-0218e886f136",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T19:58:44.363Z_

<details><summary>↩ Tool result · `toolu_01SWT2JosnBa96tn48qYP1H4`</summary>

```text
106 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "403c3131-7ac2-4009-a1c4-018b462c1c4d",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "ea65968f-170c-4691-b331-9652b918cc90",
  "sourceToolAssistantUUID": "403c3131-7ac2-4009-a1c4-018b462c1c4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-15T19:58:45.771Z_

The experiments.tex seems to be incomplete (only 106 lines). Let me check if there's an appendix or other files with the actual results tables:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea65968f-170c-4691-b331-9652b918cc90",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wri3iXfGwowQVKB36P",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e7021f82-1ba1-4a26-9fbd-4e3f711d179a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GTkLiQAF6oE9fp6Q22Nqhq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 49,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 57485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 399,
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

_source line 74 · 2026-05-15T19:58:46.326Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EkbtuB12p9FvYdNwzvsjLH`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7021f82-1ba1-4a26-9fbd-4e3f711d179a",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wri3iXfGwowQVKB36P",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7a499d97-623f-4989-9f6b-0c5f2e8013fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GTkLiQAF6oE9fp6Q22Nqhq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 49,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 57485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 399,
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

_source line 75 · 2026-05-15T19:58:46.372Z_

<details><summary>↩ Tool result · `toolu_01EkbtuB12p9FvYdNwzvsjLH`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a499d97-623f-4989-9f6b-0c5f2e8013fc",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "b8396c5f-53d5-4880-8b72-0441cf28ea43",
  "sourceToolAssistantUUID": "7a499d97-623f-4989-9f6b-0c5f2e8013fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-15T19:58:46.680Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011Mym1ufTswAd7cfkhhqRZw`</summary>

```json
{
  "command": "grep -r \"greedy_f1\\|oracle_f1\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper --include=\"*.tex\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8396c5f-53d5-4880-8b72-0441cf28ea43",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wri3iXfGwowQVKB36P",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4ba4315f-c627-45ab-a372-e14e686aeefe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GTkLiQAF6oE9fp6Q22Nqhq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 49,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 57485,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 399
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 49,
          "output_tokens": 225,
          "cache_read_input_tokens": 57485,
          "cache_creation_input_tokens": 399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 399,
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

_source line 77 · 2026-05-15T19:58:46.757Z_

<details><summary>↩ Tool result · `toolu_011Mym1ufTswAd7cfkhhqRZw`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ba4315f-c627-45ab-a372-e14e686aeefe",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "8be1205b-6b0b-49a9-ac46-a135e7d3b2e8",
  "sourceToolAssistantUUID": "4ba4315f-c627-45ab-a372-e14e686aeefe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-15T19:58:47.786Z_

Let me check the appendix.tex file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8be1205b-6b0b-49a9-ac46-a135e7d3b2e8",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wrtJrXo23i5sJ5PN2g",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "700af24f-3114-4b52-b658-9deee6b02b78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W9s67hEkRsn9tSs2mbNQDD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 57884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 735,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 79 · 2026-05-15T19:58:48.079Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M649uxf637QD4XXP3ogsV6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 2000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "700af24f-3114-4b52-b658-9deee6b02b78",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4wrtJrXo23i5sJ5PN2g",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8cd501e5-4e61-425b-9c50-61ccaa9ac9a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W9s67hEkRsn9tSs2mbNQDD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 57884,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 735
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 121,
          "cache_read_input_tokens": 57884,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 735,
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

_source line 80 · 2026-05-15T19:58:48.488Z_

<details><summary>↩ Tool result · `toolu_01M649uxf637QD4XXP3ogsV6`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
48	\quad LP & $T{=}0.7$ & 0.249 & --- \\
49	\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\
50	\midrule
51	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
52	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
53	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
54	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
55	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
56	\midrule
57	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
58	\quad SJ &  & $0.474{\pm}0.009$ & --- \\
59	\quad FK &  & $0.467{\pm}0.009$ & --- \\
60	\quad EM &  & $0.473{\pm}0.010$ & --- \\
61	\quad VC &  & $0.470{\pm}0.006$ & --- \\
62	\quad LP &  & $0.311{\pm}0.003$ & --- \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
70	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\Delta\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}
71	\label{fig:temperature_robustness}
72	\end{figure}
73	
74	\paragraph{Temperature sensitivity.}
75	SJ NER $\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.
76	FK NER $\rho$ drops by 0.022, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
77	LP exhibits the largest temperature effect on NER ($\rho{=}0.249$ at $T{=}0.7$ vs.\ $0.205$ at $T{=}1.0$, $\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.
78	Across all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).
79	
80	\paragraph{Sample size scaling.}
81	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
82	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
83	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\ref{tab:quality_estimation}).
84	FK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.
85	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
86	SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.
87	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
88	
89	\paragraph{Transfer across model families.}
90	LLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, $\Delta\rho{=}0.069$; permutation $p{=}0.06$, borderline).
91	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
92	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$),\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.474{\pm}0.009$ vs.\ LP $0.311{\pm}0.003$, $\Delta{=}{+}0.163$).
93	
94	\section{Calibration Analysis}\label{app:calibration}
95	
96	\begin{figure*}[t]
97	\centering
98	\includegraphics[width=\textwidth]{fig_reliability}
99	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
100	\label{fig:reliability}
101	\end{figure*}
102	
103	Reliability diagrams use 10 equal-width bins.
104	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
105	
106	\section{Additional Analyses}\label{app:additional}
107	
108	\begin{figure*}[t]
109	\centering
110	\includegraphics[width=\textwidth]{fig_signal_heatmap}
111	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
112	\label{fig:signal_heatmap}
113	\end{figure*}
114	
115	\paragraph{Per-relation diagnostic.}
116	RE signal degradation is relation-specific.
117	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
118	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
119	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
120	
121	\paragraph{Capability stratification.}
122	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
123	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
124	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
125	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
126	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
127	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
128	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
129	
130	\paragraph{Length vs.\ log-probability.}
131	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
132	
133	\begin{figure}[t]
134	\centering
135	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
136	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
137	\label{fig:length_logprob_scatter}
138	\end{figure}
139	
140	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
141	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
142	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
143	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
144	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
145	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
146	Evaluation circularity is negligible.
147	
148	\paragraph{SJ normalizer robustness.}
149	Equation~\ref{eq:sj} uses $\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \cup g_j|$.
150	On SciERC NER ($N{=}8$, seed${=}42$), the two normalizers yield nearly identical quality estimation: $\rho_{\max}{=}0.360$ vs.\ $\rho_{\cup}{=}0.365$ ($\Delta\rho{=}0.005$, $\Delta$AUROC${=}0.003$); on CoNLL, $\rho_{\max}{=}0.431$ vs.\ $\rho_{\cup}{=}0.432$ ($\Delta\rho{<}0.001$).
151	The normalizer choice has negligible impact on results.
152	
153	\paragraph{Conditional filtering details.}
154	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\Delta\rho{=}{-}0.005$, $p{=}0.53$; preliminary).
155	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
156	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
157	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
158	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
159	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
160	
161	\paragraph{WNUT-17 full signal analysis.}
162	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
163	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
164	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
165	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
166	
167	\begin{table}[t]
168	\centering
169	\small
170	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
171	\label{tab:wnut}
172	\begin{tabular}{lccccc}
173	\toprule
174	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
175	\midrule
176	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
177	FK      & .125 & .001 & .555 & .169 & .002 \\
178	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
179	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
180	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
185	\paragraph{Cross-configuration selection analysis.}
186	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
187	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
188	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
189	
190	\begin{table*}[t]
191	\centering
192	\small
193	\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
194	\label{tab:cross_selection}
195	\begin{tabular}{llccccccc}
196	\toprule
197	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
198	\midrule
199	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
200	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
201	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
202	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
203	\bottomrule
204	\end{tabular}
205	\end{table*}
206	
207	\paragraph{Diminishing returns of $N$-scaling.}
208	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
209	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
210	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
211	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
212	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
213	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
214	
215	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
216	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
217	VC achieves the largest gain over greedy ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
218	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
219	This reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.
220	
221	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
222	
223	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
224	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
225	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
226	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
227	
228	\begin{table}[t]
229	\centering
230	\small
231	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
232	\label{tab:bootstrap_signal_ci}
233	\begin{tabular}{lcc}
234	\toprule
235	Signal & $\rho$ & 95\% CI \\
236	\midrule
237	VC & +0.379 & [+0.299, +0.456] \\
238	SJ & +0.360 & [+0.277, +0.437] \\
239	EM & +0.295 & [+0.212, +0.371] \\
240	FK & +0.267 & [+0.176, +0.354] \\
241	LP & +0.205 & [+0.119, +0.291] \\
242	\bottomrule
243	\end{tabular}
244	
245	\vspace{0.5em}
246	
247	\begin{tabular}{lccc}
248	\toprule
249	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
250	\midrule
251	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
252	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
253	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
254	\bottomrule
255	\end{tabular}
256	
257	\smallskip
258	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
259	\end{table}
260	
261	At $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.
262	On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$) and VC--FK ($\Delta\rho{=}0.138$--$0.188$, all $p{\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\Delta\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).
263	On CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\Delta\rho{=}0.071$ ($p{<}0.001$), SJ $\Delta\rho{=}0.056$ ($p{<}0.001$), VC $\Delta\rho{=}0.022$ ($p{=}0.040$).
264	
265	\section{Diversity and Selection Analysis}\label{app:diversity}
266	
267	\begin{figure*}[t]
268	\centering
269	\includegraphics[width=\textwidth]{fig_selection_gap}
270	\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.40, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\ref{tab:selection}.}
271	\label{fig:selection_gap}
272	\end{figure*}
273	
274	\paragraph{Output diversity quantification.}
275	Table~\ref{tab:diversity} summarizes output diversity across configurations.
276	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
277	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
278	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
279	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
280	
281	\begin{table}[t]
282	\centering
283	\small
284	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
285	\label{tab:diversity}
286	\begin{tabular}{lcc}
287	\toprule
288	Config & Identical & Unique \\
289	\midrule
290	Qwen/SciERC & 11\% & 43\% \\
291	LLaMA/SciERC & 18\% & 39\% \\
292	Qwen/CoNLL & 57\% & --- \\
293	LLaMA/CoNLL & 88\% & --- \\
294	WNUT-17 & 55\% & --- \\
295	\bottomrule
296	\end{tabular}
297	\end{table}
298	
299	\paragraph{Oracle-improvable fraction.}
300	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \S\ref{sec:evaluation}); the diversity quantification in Table~\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
301	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
302	
303	\paragraph{Diversity-stratified selection gap.}
304	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
305	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.
306	This rules out insufficient diversity as an explanation for the correlation-selection gap.
307	
308	\paragraph{TOST equivalence testing.}
309	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
310	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
311	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
312	These proportions use the same test data that defines the headroom and should be interpreted as context for practical relevance rather than independent calibration.
313	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
314	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
315	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
316	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
317	
318	\begin{table}[t]
319	\centering
320	\small
321	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
322	\label{tab:tost}
323	\begin{tabular}{l cccc cccc}
324	\toprule
325	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
326	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
327	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
328	\midrule
329	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
330	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
331	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
332	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
333	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
334	\bottomrule
335	\end{tabular}
336	\end{table}
337	
338	\section{Multi-Seed Stability}\label{app:multiseed}
339	
340	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
341	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals.
342	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
343	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
344	
345	\begin{table}[t]
346	\centering
347	\small
348	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
349	\label{tab:multiseed}
350	\begin{tabular}{lccccc}
351	\toprule
352	& LP & FK & SJ & VC & EM \\
353	\midrule
354	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
355	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
356	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
357	\midrule
358	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
359	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
360	\midrule
361	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
362	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
363	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
364	\bottomrule
365	\end{tabular}
366	\end{table}
367	
368	\section{Training Configuration}\label{app:training}
369	
370	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
371	
372	\begin{table}[t]
373	\centering
374	\small
375	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
376	\label{tab:training}
377	\begin{tabular}{ll}
378	\toprule
379	Parameter & Value \\
380	\midrule
381	LoRA rank / $\alpha$ & 32 / 64 \\
382	LoRA target & All linear modules \\
383	LoRA dropout & 0 \\
384	Optimizer & AdamW \\
385	Learning rate & 2e-4, cosine schedule \\
386	Warmup ratio & 0.1 \\
387	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
388	Epochs & 5 \\
389	Max sequence length & 2048 \\
390	Precision & bf16 \\
391	Gradient checkpointing & Enabled \\
392	Max gradient norm & 1.0 \\
393	Training seed & 42 \\
394	Framework & LLaMA Factory \\
395	\midrule
396	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
397	SciERC split & 1861 / 275 / 551 \\
398	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
399	& eval\_steps${=}$200, save\_limit${=}$5 \\
400	\bottomrule
401	\end{tabular}
402	\end{table}
403	
404	\paragraph{Prompt template.}
405	For NER, we use a structured prompt:
406	\begin{quote}
407	\small
408	\texttt{System:} You are an expert in Named Entity Recognition.\\
409	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
410	Text: \texttt{\{input\_text\}}\\
411	Entity types: \texttt{\{schema\_types\}}
412	\end{quote}
413	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
414	
415	\paragraph{Constrained decoding.}
416	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
417	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
418	
419	\section{Thinking Token Impact Analysis}\label{app:thinking_token}
420	
421	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks prepended to each response (\S\ref{sec:setup}).
422	We quantify the potential impact on LP scores through three complementary arguments.
423	
424	\paragraph{LP shift magnitude.}
425	The 4--5 thinking tokens contribute an estimated LP shift of 0.001 nats to the per-token log-probability average, representing 2.68\% of the median within-instance LP range (0.041 nats).
426	This shift is too small to alter LP-based rankings.
427	
428	\paragraph{Constant prefix cancellation.}
429	All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.
430	Any LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \textit{rankings} unchanged.
431	
432	\paragraph{CoNLL control group.}
433	CoNLL and WNUT-17 checkpoints were trained without thinking tokens (\texttt{enable\_thinking=False}).
434	If thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.
435	Instead, CoNLL shows \textit{higher} tied fractions at both temperatures (86.8\% at $T{=}1.0$, 95.8\% at $T{=}0.7$) than SciERC (60.3\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.
436	
437	\section{Log-Probability Score Compression}\label{app:logprob_ties}
438	
439	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
440	The median within-instance LP range is only 0.041 nats---below the $\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.
441	At $\varepsilon{=}0.05$, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
442	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
443	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
444	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
445	
446	\begin{figure}[t]
447	\centering
448	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
449	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
450	\label{fig:lp_range_cdf}
451	\end{figure}
452	
453	\begin{table}[t]
454	\centering
455	\small
456	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
457	\label{tab:logprob_ties}
458	\begin{tabular}{lc}
459	\toprule
460	$\varepsilon$ threshold & Tied instances (\%) \\
461	\midrule
462	0.01 & 1.1\% \\
463	0.05 & 60.3\% \\
464	0.1  & ${\sim}$84\% \\
465	0.5  & ${\sim}$99\% \\
466	\bottomrule
467	\end{tabular}
468	\end{table}
469	
470	\paragraph{Non-tied subset.}
471	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
472	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.
473	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
474	
475	\paragraph{$\varepsilon$ sensitivity sweep.}
476	Table~\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\varepsilon{=}0.01$ to $0.20$.
477	The tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.
478	$\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\varepsilon{\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\leq}36$).
479	
480	\begin{table}[t]
481	\centering
482	\small
483	\caption{$\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\%'' = fraction with within-instance LP range ${<}\varepsilon$. $\Delta$: selection F1 gain over greedy on the non-tied subset. The tied fraction increases smoothly; $\varepsilon{=}0.05$ yields the strongest statistical separation.}
484	\label{tab:epsilon_sweep}
485	\begin{tabular}{ccccc}
486	\toprule
487	$\varepsilon$ & Tied\% & Non-tied $n$ & $\Delta$ (pp) & $p$ \\
488	\midrule
489	0.01 & 1.1\% & 523 & $+$0.58 & .21 \\
490	0.02 & 13.6\% & 457 & $+$0.83 & .15 \\
491	0.03 & 31.8\% & 361 & $+$1.31 & .079 \\
492	\textbf{0.05} & \textbf{60.3\%} & \textbf{210} & \textbf{$+$2.86} & \textbf{.004} \\
493	0.10 & 83.9\% & 85 & $+$3.69 & .034 \\
494	0.15 & 93.2\% & 36 & $+$4.15 & .11 \\
495	0.20 & 96.4\% & 19 & $+$4.59 & .13 \\
496	\bottomrule
497	\end{tabular}
498	\end{table}
499	
500	\paragraph{$\varepsilon$ robustness of selection F1.}\label{app:epsilon_robustness}
501	The preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\varepsilon$ to define MBR-style proximity in selection.
502	Table~\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\varepsilon \in [0, 0.2]$ for all signals and configurations.
503	At $\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.
504	Spearman $\rho$---the primary quality estimation metric throughout---is a continuous rank correlation that does not depend on any discretization threshold; the $\varepsilon$ parameter affects only the selection analysis.
505	
506	\begin{table}[t]
507	\centering
508	\small
509	\caption{Maximum selection F1 variation (pp) across $\varepsilon \in [0, 0.2]$. At $\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}
510	\label{tab:epsilon_robustness}
511	\begin{tabular}{lcccc}
512	\toprule
513	& \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL}} \\
514	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
515	Signal & Qwen & LLaMA & Qwen & LLaMA \\
516	\midrule
517	SJ & 0.92 & 1.45 & 0.99 & 0.18 \\
518	FK & 1.03 & 0.93 & 0.60 & 0.15 \\
519	VC & 2.33 & 0.53 & 0.72 & 0.18 \\
520	EM & 0.00 & 0.00 & 0.00 & 0.00 \\
521	LP & 3.65 & 2.58 & 3.00 & 0.31 \\
522	\bottomrule
523	\end{tabular}
524	\end{table}
525	
526	\section{RE Conditional Selection}\label{app:re_conditional_selection}
527	
528	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
529	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
530	All five signals underperform greedy on both subsets.
531	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
532	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
533	
534	\begin{table}[t]
535	\centering
536	\small
537	\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
538	\label{tab:re_cond_selection}
539	\begin{tabular}{lcc}
540	\toprule
541	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
542	\midrule
543	Oracle & 0.585 & 0.757 \\
544	\midrule
545	LP & 0.395 & 0.600 \\
546	SJ & 0.386 & 0.604 \\
547	EM & 0.372 & 0.583 \\
548	VC & 0.359 & 0.574 \\
549	\midrule
550	Greedy & 0.404 & 0.674 \\
551	\bottomrule
552	\end{tabular}
553	\end{table}
554	
555	\section{RE $N{=}16$ Selection Analysis}\label{app:re_n16_selection}
556	
557	Table~\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.
558	All four consistency signals underperform greedy, with EM showing the largest deficit ($\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).
559	LP is the only positive signal ($\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).
560	Even the most favorable seed captures only ${\sim}9\%$ of the 17.1~pp oracle headroom.
561	This cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the structural limitation of instance-level signals for candidate ranking.
562	
563	\begin{table}[t]
564	\centering
565	\small
566	\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC ($N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ greedy. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
567	\label{tab:re_n16_selection}
568	\begin{tabular}{lccc}
569	\toprule
570	Method & F1 & $\Delta$ (pp) & $p$(Fisher) \\
571	\midrule
572	Oracle & $.463{\pm}.006$ & $+$17.1 & --- \\
573	\midrule
574	LP & $\mathbf{.299}{\pm}.007$ & $+$0.7 & .058 \\
575	VC & $.284{\pm}.002$ & $-$0.8 & .973 \\
576	FK & $.283{\pm}.005$ & $-$0.9 & .985 \\
577	SJ & $.281{\pm}.005$ & $-$1.0 & .993 \\
578	EM & $.277{\pm}.007$ & $-$1.5 & .999 \\
579	\midrule
580	Greedy & $.291{\pm}.000$ & --- & --- \\
581	Random & $.262{\pm}.001$ & $-$2.9 & --- \\
582	\bottomrule
583	\end{tabular}
584	\end{table}
585	
586	\section{MBR Decoding and Task-Specific Interactions}\label{app:mbr_discussion}
587	
588	\paragraph{Connection to MBR decoding.}
589	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
590	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
591	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
592	
593	\paragraph{Task-specific decoding interactions.}
594	The free-form ablation reveals divergent behavior across tasks.
595	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
596	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
597	This interaction does not generalize to NER, where selection remains negligible under both regimes.
598	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
599	The non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
600	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
601	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
602	
603	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
604	
605	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).
606	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
607	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
608	RE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\ $-0.68$~pp constrained).
609	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
610	
611	\begin{table*}[t]
612	\centering
613	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}
614	\label{tab:freeform_ablation}
615	
616	\vspace{2pt}
617	{\small\textsc{Panel A: Logprob Distribution}}
618	\vspace{2pt}
619	
620	\begin{tabular}{lccc}
621	\toprule
622	Metric & Constrained & Free-form & $\Delta$ \\
623	\midrule
624	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
625	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
626	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
627	\bottomrule
628	\end{tabular}
629	
630	\vspace{8pt}
631	
632	{\small\textsc{Panel B: Selection F1}}
633	\vspace{2pt}
634	
635	\begin{tabular}{llccc}
636	\toprule
637	Task & Method & Constrained & Free-form & $\Delta$ \\
638	\midrule
639	\multirow{3}{*}{NER}
640	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
641	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
642	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
643	\midrule
644	\multirow{3}{*}{RE}
645	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
646	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
647	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
648	\bottomrule
649	\end{tabular}
650	
651	\vspace{8pt}
652	
653	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
654	\vspace{2pt}
655	
656	\begin{tabular}{l ccc ccc}
657	\toprule
658	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
659	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
660	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
661	\midrule
662	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
663	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
664	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
665	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
666	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
667	\bottomrule
668	\end{tabular}
669	
670	\vspace{8pt}
671	
672	{\small\textsc{Panel D: Parse Rate (Free-form)}}
673	\vspace{2pt}
674	
675	\begin{tabular}{lc}
676	\toprule
677	Metric & Value \\
678	\midrule
679	Total samples          & 4408 \\
680	Parse rate             & 99.95\% \\
681	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
682	\bottomrule
683	\end{tabular}
684	
685	\end{table*}
686	
687	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
688	
689	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
690	
691	\paragraph{Pairwise overlap.}
692	LP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
693	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
694	
695	\paragraph{Instance complexity drives failure.}
696	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
697	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
698	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
699	
700	\begin{table}[t]
701	\centering
702	\small
703	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}
704	\label{tab:stable_failures}
705	\begin{tabular}{lcccc}
706	\toprule
707	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
708	\midrule
709	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
710	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
711	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
712	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
713	\bottomrule
714	\end{tabular}
715	\end{table}
716	
717	\paragraph{Flip instances.}
718	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
719	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
720	
721	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
722	
723	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
724	
725	\begin{table}[t]
726	\centering
727	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
728	\label{tab:n-scaling}
729	\small
730	\begin{tabular}{l ccc ccc}
731	\toprule
732	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
733	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
734	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
735	\midrule
736	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
737	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
738	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
739	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
740	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
741	\midrule
742	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
743	\bottomrule
744	\end{tabular}
745	\end{table}
746	
747	\begin{table}[t]
748	\centering
749	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
750	\label{tab:ranking-stability}
751	\small
752	\begin{tabular}{ll cc l}
753	\toprule
754	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
755	\midrule
756	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
757	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
758	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
759	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
760	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
761	\bottomrule
762	\end{tabular}
763	\end{table}
764	
765	\begin{table}[t]
766	\centering
767	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
768	\label{tab:sigma-comparison}
769	\small
770	\begin{tabular}{l cc cc}
771	\toprule
772	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
773	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
774	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
775	\midrule
776	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
777	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
778	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
779	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
780	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
781	\midrule
782	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
783	\bottomrule
784	\end{tabular}
785	\end{table}
786	
787	Signal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}).
788	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
789	
790	\section{Cross-Dataset OOD Analysis}\label{app:ood}
791	
792	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
793	
794	\begin{table}[t]
795	\centering
796	\small
797	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
798	\label{tab:ood}
799	\begin{tabular}{l ccc ccc}
800	\toprule
801	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
802	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
803	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
804	\midrule
805	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
806	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
807	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
808	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
809	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
810	\bottomrule
811	\end{tabular}
812	\end{table}
813	
814	\paragraph{Wider-to-narrower schema transfer.}
815	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
816	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
817	
818	\paragraph{Narrower-to-wider schema transfer (excluded).}
819	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
820	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).
821	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
822	These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
823	
824	\paragraph{Asymmetry interpretation.}
825	The directional asymmetry is driven by schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
826	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
827	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cd501e5-4e61-425b-9c50-61ccaa9ac9a0",
  "isSidechain": true,
  "promptId": "f0761dfb-f475-41b7-a8eb-19baaed9c8e0",
  "agentId": "a2dc3436d334616ab",
  "type": "user",
  "uuid": "f2c1e687-1b06-40db-9c2e-d9b75cb87b7f",
  "sourceToolAssistantUUID": "8cd501e5-4e61-425b-9c50-61ccaa9ac9a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan"
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-15T19:58:55.966Z_

Perfect! Now I have comprehensive data. Let me compile the 8B model results for both datasets:

## 8B Model SCS Inference Results Summary

**SciERC (Qwen3-8B, N=8, T=1.0):**
- Experiment: mvp_pilot_004
- Greedy F1: NER 0.6671, RE 0.4208
- Oracle F1: NER 0.7756, RE 0.5882
- SJ_rho: NER full 0.3825 / cond 0.3762, RE full 0.2441 / cond 0.3161
- FK_rho: NER full 0.259 / cond 0.2352, RE full 0.2782 / cond 0.3067
- Checkpoint: qwen3-8b-scierc-merged-v2

**CoNLL-2003 (Qwen3-8B, N=8, T=1.0):**
- Experiment: exp_002
- Greedy F1: 0.9123
- Oracle F1: 0.9543
- SJ_rho: full 0.4357 / cond 0.4511
- FK_rho: full 0.3998 / cond 0.4064
- LP_rho: full 0.3157 / cond 0.3562
- Model: qwen3-8b-conll2003-merged
- 2756 valid instances (from 3453 total)

**LLaMA-3.1-8B (Comparison):**

SciERC (N=8):
- Experiment: exp_007_llama_inference
- Greedy F1: NER 0.66, RE 0.434
- Oracle F1: NER 0.781, RE 0.568
- SJ_rho: NER full 0.363 / cond 0.311, RE full 0.299 / cond 0.405

CoNLL (N=8):
- Experiment: exp_017_llama_conll_infer
- Greedy F1: 0.9266
- Oracle F1: 0.9443
- SJ_rho: full 0.4314 / cond 0.4356
- FK_rho: full 0.4277 / cond 0.431
- Model: LLaMA-3.1-8B-Instruct fine-tuned on CoNLL

**Paper (experiments.tex) - Table 1 Quality Estimation (N=8, seed=42):**
- SciERC NER SJ ρ: 0.360
- CoNLL (Qwen) SJ ρ: 0.436
- CoNLL (LLaMA) SJ ρ: 0.431
- CoNLL (Qwen) EM ρ: 0.451 (best per column)
- CoNLL (LLaMA) LP ρ: 0.307

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2c1e687-1b06-40db-9c2e-d9b75cb87b7f",
  "isSidechain": true,
  "agentId": "a2dc3436d334616ab",
  "requestId": "req_011Cb4ws1hc1PTLHUMThuQ4c",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "85354c74-a5e0-4d13-bc59-8ac228e004c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "d0212965-0813-4b00-b854-06bcbf049b50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delegated-watching-kahan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017tvYR62Be4g3iqsFZwjakW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 22904,
      "cache_read_input_tokens": 58619,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22904
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 747,
          "cache_read_input_tokens": 58619,
          "cache_creation_input_tokens": 22904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22904,
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
