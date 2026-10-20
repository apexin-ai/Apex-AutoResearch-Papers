# Research conversation: Read the following three files in full and report their COMPLETE contents: 1. /home/ubuntu/.agent-ml-research-idea_gen_0

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9d8a4993fef2b75d.jsonl`
- **Structured JSON:** [`8e574018b9db4a369eff.json`](../../sessions/8e/8e574018b9db4a369eff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

9 recorded events

### User

_source line 1 · 2026-05-22T09:17:06.707Z_

Read the following three files in full and report their COMPLETE contents:

1. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex

For each file, report the FULL text content with line numbers. These are LaTeX files for an academic paper. I need to see every word to audit claim-evidence alignment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fbe38d04-4c6a-4da2-a4b2-2d119f4253b2",
  "agentId": "a9d8a4993fef2b75d",
  "type": "user",
  "uuid": "5bf9c4cf-6f15-418f-8a9f-dfe13fd6f5de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "f72b7019-154f-4c8d-b246-9228aa0daf12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-plotting-book"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T09:17:08.244Z_

I'll read all three LaTeX files in full for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bf9c4cf-6f15-418f-8a9f-dfe13fd6f5de",
  "isSidechain": true,
  "agentId": "a9d8a4993fef2b75d",
  "requestId": "req_011CbHMbHupTyuRTZn1X8rZg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9a05047b-18ae-4df1-9e14-95f9e5a62aae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "f72b7019-154f-4c8d-b246-9228aa0daf12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-plotting-book",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0141GWeyKyejU9WgRB5AUHna",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21216,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21216,
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

_source line 3 · 2026-05-22T09:17:08.493Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ranuwii3AK3ngyNWCoMtp4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a05047b-18ae-4df1-9e14-95f9e5a62aae",
  "isSidechain": true,
  "agentId": "a9d8a4993fef2b75d",
  "requestId": "req_011CbHMbHupTyuRTZn1X8rZg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ee046169-efca-49e4-9120-525fbc104856",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "f72b7019-154f-4c8d-b246-9228aa0daf12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-plotting-book",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0141GWeyKyejU9WgRB5AUHna",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21216,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21216,
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

_source line 4 · 2026-05-22T09:17:08.504Z_

<details><summary>↩ Tool result · `toolu_01Ranuwii3AK3ngyNWCoMtp4`</summary>

```text
1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but the boundary conditions governing its effectiveness for structured prediction remain uncharacterized.
3	Using named entity recognition (four datasets, four model families, 4B--72B) and relation extraction as case studies, we systematically characterize when test-time scaling succeeds and fails for set-valued outputs.
4	Quality estimation signals effectively predict output quality (AUROC up to $0.82$ across nine method categories), yet instance-level selection yields ${<}1$\,pp even at $N{=}64$, revealing a \textbf{correlation-selection gap}.
5	A diagnostic cascade identifies two boundary conditions: output convergence (degeneracy $12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$), which jointly determine scaling returns.
6	Cross-task validation on RE reveals a distinct bottleneck---$40$\% zero-F1 from upstream errors rather than degeneracy---confirming task-specific failure modes within structured prediction.
7	Exploratory entity-level construction partially bypasses the sample-level bottleneck ($+1.40$\,pp where low degeneracy and signal alignment provide headroom).
8	The central finding is a \textit{capability-diversity tension}: as model capability increases, output convergence rises and test-time scaling returns diminish---a general constraint for structured prediction.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee046169-efca-49e4-9120-525fbc104856",
  "isSidechain": true,
  "promptId": "fbe38d04-4c6a-4da2-a4b2-2d119f4253b2",
  "agentId": "a9d8a4993fef2b75d",
  "type": "user",
  "uuid": "05e8c042-4b6c-4450-85c7-91bcb19bc8a2",
  "sourceToolAssistantUUID": "ee046169-efca-49e4-9120-525fbc104856",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "f72b7019-154f-4c8d-b246-9228aa0daf12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-plotting-book"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T09:17:08.668Z_

<details open><summary>🔧 Tool call — Read · `toolu_0138YcL8UPGHENn9r6m5sHUg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05e8c042-4b6c-4450-85c7-91bcb19bc8a2",
  "isSidechain": true,
  "agentId": "a9d8a4993fef2b75d",
  "requestId": "req_011CbHMbHupTyuRTZn1X8rZg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "78caea46-03e4-4afd-a1c3-6b88785dfb21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "f72b7019-154f-4c8d-b246-9228aa0daf12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-plotting-book",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0141GWeyKyejU9WgRB5AUHna",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21216,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21216,
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

_source line 6 · 2026-05-22T09:17:08.681Z_

<details><summary>↩ Tool result · `toolu_0138YcL8UPGHENn9r6m5sHUg`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For structured prediction, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work \cite{yao2026consistency, yun2025price} provides initial observations but no systematic characterization of instance-level failure.
5	
6	Using NER (four datasets, four model families, 4B--72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals effectively predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet instance-level selection yields ${<}1$\,pp across $N{=}8$--$64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
7	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; \S\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}: the information exists but cannot be leveraged for selection.
8	A diagnostic cascade localizes the failure to two boundary conditions---output convergence (degeneracy $12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$)---which jointly prevent selection; nine method categories fail across three datasets and two model families (Table~\ref{tab:method_summary}).
9	The optimal strategy is dataset-dependent (LP: $+1.39$\,pp on Few-NERD; MV: $+0.61$\,pp on CoNLL at $N{=}64$), and RE reveals a distinct bottleneck ($40$\% zero-F1 from upstream errors; Appendix~\ref{app:re_extension}).
10	Exploratory entity-level construction partially bypasses the bottleneck ($+0.32$\textendash$1.40$\,pp on Few-NERD; Holm $p_{\text{adj}}{=}0.006$) where low degeneracy and LP-F1 alignment hold; $\theta_{\text{crit}}{=}0.70$ predicts when gains vanish.
11	
12	The central finding is a \textit{capability-diversity tension}: as model capability increases, output convergence rises and test-time scaling returns diminish---a general constraint for structured prediction.
13	These findings rest on four NER benchmarks, two primary model families (Qwen3-8B, LLaMA-3.1-8B) with 4B/14B ablations, $N {\in} \{2, \ldots, 64\}$, and preliminary cross-scale evidence from Qwen2.5-72B and GPT-5.5 zero-shot (\S\ref{sec:scaling}), RE\footnote{RE F1 is confounded by entity span errors: the majority of zero-F1 RE instances reflect upstream NER mismatches rather than relation classification failure (Appendix~\ref{app:re_extension}).}, and SQL parsing ($87.2$\% degeneracy).
14	
15	\begin{figure*}[t]
16	\centering
17	\includegraphics[width=\textwidth]{fig_overview}
18	\caption{Overview of the correlation-selection gap (diagnostic sequence, not causal chain; Qwen3-8B fine-tuned, Few-NERD, $N{=}8$, $T{=}1.0$). \textbf{Left}: consistency signals estimate instance quality ($\rho$ up to 0.45; Table~\ref{tab:quality_estimation}). \textbf{Center}: instance-level signals assign identical scores to all $N$ candidates, so selection cannot outperform greedy. \textbf{Right}: LP-weighted entity construction ($\theta{=}2/N$) bypasses the bottleneck ($+1.40$\,pp on Few-NERD; \S\ref{sec:prescriptive}).}
19	\label{fig:overview}
20	\end{figure*}
21	
22	Our investigation proceeds in three stages:
23	\begin{enumerate}
24	    \item \textbf{Discover} [Empirical] (\S\ref{sec:qe_results}, \S\ref{sec:mechanistic}).
25	    Five QE signals achieve AUROC up to $0.82$; a hidden-state probe reveals an introspection boundary (AUROC $0.63$\textendash$0.88$ vs.\ self-judgment $0.51$): quality information exists but cannot be accessed through prompting.
26	
27	    \item \textbf{Diagnose} [Diagnostic] (\S\ref{sec:selection_gap}, \S\ref{sec:adaptive}).
28	    A four-stage cascade identifies boundary conditions for test-time scaling: output convergence and signal alignment collapse ($\alpha{\to}0$) jointly determine the boundary.
29	    Validated across NER and RE, revealing task-specific bottlenecks (degeneracy vs.\ zero-F1 dominance).
30	
31	    \item \textbf{Explore bypasses} [Exploratory] (\S\ref{sec:prescriptive}, \S\ref{sec:theory}).
32	    Entity-level construction ($+0.32$\,--\,$1.40$\,pp on Few-NERD), cross-model ensemble ($+0.42$\,pp), and regime-specific LP selection ($+1.39$\,pp) partially bypass sample-level selection where headroom allows. $\theta_{\text{crit}}{=}0.70$ predicts when gains vanish.
33	\end{enumerate}
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78caea46-03e4-4afd-a1c3-6b88785dfb21",
  "isSidechain": true,
  "promptId": "fbe38d04-4c6a-4da2-a4b2-2d119f4253b2",
  "agentId": "a9d8a4993fef2b75d",
  "type": "user",
  "uuid": "00a879e9-f8b7-4cd0-a9c5-179bb759fdff",
  "sourceToolAssistantUUID": "78caea46-03e4-4afd-a1c3-6b88785dfb21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "f72b7019-154f-4c8d-b246-9228aa0daf12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-plotting-book"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T09:17:08.806Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NtJJdtDzh6tTA7RwbRs274`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00a879e9-f8b7-4cd0-a9c5-179bb759fdff",
  "isSidechain": true,
  "agentId": "a9d8a4993fef2b75d",
  "requestId": "req_011CbHMbHupTyuRTZn1X8rZg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4db727b7-b11e-46d8-8529-8c26f113b930",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "f72b7019-154f-4c8d-b246-9228aa0daf12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-plotting-book",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0141GWeyKyejU9WgRB5AUHna",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21216,
      "cache_read_input_tokens": 0,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21216
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 253,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 21216,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21216,
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

_source line 8 · 2026-05-22T09:17:08.820Z_

<details><summary>↩ Tool result · `toolu_01NtJJdtDzh6tTA7RwbRs274`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	\paragraph{Why test-time scaling fails for structured outputs.}
4	For discrete-answer reasoning, sample diversity reflects diverse reasoning paths that self-consistency can filter.
5	For structured outputs, fine-tuned model diversity largely reflects noise: output convergence (degeneracy $12$--$68$\%) eliminates candidate diversity, while signal alignment collapse ($\alpha{\to}0$) prevents residual variation from being ranked.
6	This \textit{capability-diversity tension} explains why the gap persists across model families (5.5--74\% degeneracy; Table~\ref{tab:frontier_sc_cross}) and scales (4B--72B; \S\ref{sec:scaling}).
7	On CoNLL, pretrained MV captures ${\sim}98$\% of oracle headroom versus ${<}2$\% finetuned (Appendix~\ref{app:cross_scale}), directly demonstrating capability-induced convergence.
8	
9	\paragraph{Practical implications.}
10	The cascade provides a pre-deployment diagnostic: measure degeneracy and LP-F1 alignment with $N{=}8$ samples before investing in $N{\times}$ inference.
11	When degeneracy exceeds $\theta_{\text{crit}}{=}0.70$, aggregation is unlikely to help; when both conditions are favorable ($D{<}22\%$, LP $\rho{>}0.2$), exploratory entity-level construction offers modest gains.
12	These findings are primarily validated on 7--14B fine-tuned NER models; generalization to other structured tasks requires further investigation.
13	
14	\paragraph{Conclusion.}
15	We characterize the boundary conditions under which test-time compute scaling fails for structured prediction, using NER and RE as case studies.
16	The correlation-selection gap is governed by output convergence and signal alignment collapse, not signal quality per se; our contribution is an empirical characterization, not a new method.
17	The exploratory bypasses demonstrate that the boundary can be partially circumvented at entity granularity, but the capability-diversity tension remains an open challenge for inference-time scaling of structured outputs.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4db727b7-b11e-46d8-8529-8c26f113b930",
  "isSidechain": true,
  "promptId": "fbe38d04-4c6a-4da2-a4b2-2d119f4253b2",
  "agentId": "a9d8a4993fef2b75d",
  "type": "user",
  "uuid": "71408479-916a-43bb-a294-d1aa594402c8",
  "sourceToolAssistantUUID": "4db727b7-b11e-46d8-8529-8c26f113b930",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "f72b7019-154f-4c8d-b246-9228aa0daf12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-plotting-book"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-22T09:17:35.760Z_

Here are the complete contents of the three LaTeX files:

## 1. abstract.tex

```
1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but the boundary conditions governing its effectiveness for structured prediction remain uncharacterized.
3	Using named entity recognition (four datasets, four model families, 4B--72B) and relation extraction as case studies, we systematically characterize when test-time scaling succeeds and fails for set-valued outputs.
4	Quality estimation signals effectively predict output quality (AUROC up to $0.82$ across nine method categories), yet instance-level selection yields ${<}1$\,pp even at $N{=}64$, revealing a \textbf{correlation-selection gap}.
5	A diagnostic cascade identifies two boundary conditions: output convergence (degeneracy $12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$), which jointly determine scaling returns.
6	Cross-task validation on RE reveals a distinct bottleneck---$40$\% zero-F1 from upstream errors rather than degeneracy---confirming task-specific failure modes within structured prediction.
7	Exploratory entity-level construction partially bypasses the sample-level bottleneck ($+1.40$\,pp where low degeneracy and signal alignment provide headroom).
8	The central finding is a \textit{capability-diversity tension}: as model capability increases, output convergence rises and test-time scaling returns diminish---a general constraint for structured prediction.
9	\end{abstract}
```

## 2. introduction.tex

```
1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For structured prediction, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work \cite{yao2026consistency, yun2025price} provides initial observations but no systematic characterization of instance-level failure.
5	
6	Using NER (four datasets, four model families, 4B--72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals effectively predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet instance-level selection yields ${<}1$\,pp across $N{=}8$--$64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
7	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; \S\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}: the information exists but cannot be leveraged for selection.
8	A diagnostic cascade localizes the failure to two boundary conditions---output convergence (degeneracy $12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$)---which jointly prevent selection; nine method categories fail across three datasets and two model families (Table~\ref{tab:method_summary}).
9	The optimal strategy is dataset-dependent (LP: $+1.39$\,pp on Few-NERD; MV: $+0.61$\,pp on CoNLL at $N{=}64$), and RE reveals a distinct bottleneck ($40$\% zero-F1 from upstream errors; Appendix~\ref{app:re_extension}).
10	Exploratory entity-level construction partially bypasses the bottleneck ($+0.32$\textendash$1.40$\,pp on Few-NERD; Holm $p_{\text{adj}}{=}0.006$) where low degeneracy and LP-F1 alignment hold; $\theta_{\text{crit}}{=}0.70$ predicts when gains vanish.
11	
12	The central finding is a \textit{capability-diversity tension}: as model capability increases, output convergence rises and test-time scaling returns diminish---a general constraint for structured prediction.
13	These findings rest on four NER benchmarks, two primary model families (Qwen3-8B, LLaMA-3.1-8B) with 4B/14B ablations, $N {\in} \{2, \ldots, 64\}$, and preliminary cross-scale evidence from Qwen2.5-72B and GPT-5.5 zero-shot (\S\ref{sec:scaling}), RE\footnote{RE F1 is confounded by entity span errors: the majority of zero-F1 RE instances reflect upstream NER mismatches rather than relation classification failure (Appendix~\ref{app:re_extension}).}, and SQL parsing ($87.2$\% degeneracy).
14	
15	\begin{figure*}[t]
16	\centering
17	\includegraphics[width=\textwidth]{fig_overview}
18	\caption{Overview of the correlation-selection gap (diagnostic sequence, not causal chain; Qwen3-8B fine-tuned, Few-NERD, $N{=}8$, $T{=}1.0$). \textbf{Left}: consistency signals estimate instance quality ($\rho$ up to 0.45; Table~\ref{tab:quality_estimation}). \textbf{Center}: instance-level signals assign identical scores to all $N$ candidates, so selection cannot outperform greedy. \textbf{Right}: LP-weighted entity construction ($\theta{=}2/N$) bypasses the bottleneck ($+1.40$\,pp on Few-NERD; \S\ref{sec:prescriptive}).}
19	\label{fig:overview}
20	\end{figure*}
21	
22	Our investigation proceeds in three stages:
23	\begin{enumerate}
24	    \item \textbf{Discover} [Empirical] (\S\ref{sec:qe_results}, \S\ref{sec:mechanistic}).
25	    Five QE signals achieve AUROC up to $0.82$; a hidden-state probe reveals an introspection boundary (AUROC $0.63$\textendash$0.88$ vs.\ self-judgment $0.51$): quality information exists but cannot be accessed through prompting.
26	
27	    \item \textbf{Diagnose} [Diagnostic] (\S\ref{sec:selection_gap}, \S\ref{sec:adaptive}).
28	    A four-stage cascade identifies boundary conditions for test-time scaling: output convergence and signal alignment collapse ($\alpha{\to}0$) jointly determine the boundary.
29	    Validated across NER and RE, revealing task-specific bottlenecks (degeneracy vs.\ zero-F1 dominance).
30	
31	    \item \textbf{Explore bypasses} [Exploratory] (\S\ref{sec:prescriptive}, \S\ref{sec:theory}).
32	    Entity-level construction ($+0.32$\,--\,$1.40$\,pp on Few-NERD), cross-model ensemble ($+0.42$\,pp), and regime-specific LP selection ($+1.39$\,pp) partially bypass sample-level selection where headroom allows. $\theta_{\text{crit}}{=}0.70$ predicts when gains vanish.
33	\end{enumerate}
```

## 3. discussion.tex

```
1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	\paragraph{Why test-time scaling fails for structured outputs.}
4	For discrete-answer reasoning, sample diversity reflects diverse reasoning paths that self-consistency can filter.
5	For structured outputs, fine-tuned model diversity largely reflects noise: output convergence (degeneracy $12$--$68$\%) eliminates candidate diversity, while signal alignment collapse ($\alpha{\to}0$) prevents residual variation from being ranked.
6	This \textit{capability-diversity tension} explains why the gap persists across model families (5.5--74\% degeneracy; Table~\ref{tab:frontier_sc_cross}) and scales (4B--72B; \S\ref{sec:scaling}).
7	On CoNLL, pretrained MV captures ${\sim}98$\% of oracle headroom versus ${<}2$\% finetuned (Appendix~\ref{app:cross_scale}), directly demonstrating capability-induced convergence.
8	
9	\paragraph{Practical implications.}
10	The cascade provides a pre-deployment diagnostic: measure degeneracy and LP-F1 alignment with $N{=}8$ samples before investing in $N{\times}$ inference.
11	When degeneracy exceeds $\theta_{\text{crit}}{=}0.70$, aggregation is unlikely to help; when both conditions are favorable ($D{<}22\%$, LP $\rho{>}0.2$), exploratory entity-level construction offers modest gains.
12	These findings are primarily validated on 7--14B fine-tuned NER models; generalization to other structured tasks requires further investigation.
13	
14	\paragraph{Conclusion.}
15	We characterize the boundary conditions under which test-time compute scaling fails for structured prediction, using NER and RE as case studies.
16	The correlation-selection gap is governed by output convergence and signal alignment collapse, not signal quality per se; our contribution is an empirical characterization, not a new method.
17	The exploratory bypasses demonstrate that the boundary can be partially circumvented at entity granularity, but the capability-diversity tension remains an open challenge for inference-time scaling of structured outputs.
18	(File ends)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71408479-916a-43bb-a294-d1aa594402c8",
  "isSidechain": true,
  "agentId": "a9d8a4993fef2b75d",
  "requestId": "req_011CbHMbSymke4YqPvVQYMnf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3964c357-85d9-4149-bc80-103fb4a491ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "f72b7019-154f-4c8d-b246-9228aa0daf12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-plotting-book",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018xgzGedMmQrC2uNiyM2hcz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3552,
      "cache_read_input_tokens": 21216,
      "output_tokens": 2437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3552
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2437,
          "cache_read_input_tokens": 21216,
          "cache_creation_input_tokens": 3552,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3552,
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
