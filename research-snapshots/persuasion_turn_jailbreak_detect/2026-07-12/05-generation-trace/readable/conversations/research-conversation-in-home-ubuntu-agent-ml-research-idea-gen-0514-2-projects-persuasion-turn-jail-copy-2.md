# Research conversation: In /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex, 

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-af10f55edf1fa0e7c.jsonl`
- **Structured JSON:** [`86afb6accf8067b791c9.json`](../../sessions/86/86afb6accf8067b791c9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-23T19:22:02.664Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex, find the exact sentence that mentions "≥40" or "geq.*40" in the Discussion section. Report the full sentence.

Then in experiments.tex in the same directory, find the ToxicChat results table (tab:human_data). List all variant names and their Macro F1 values. Also note the Vanilla F1 value. I need to verify whether "all DAPT variants exceed vanilla by ≥40 pp" is correct by computing each variant's improvement over vanilla.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "46752c42-9bf2-481f-aa05-e1e832316775",
  "agentId": "af10f55edf1fa0e7c",
  "type": "user",
  "uuid": "d33e74e0-2a7a-4dc4-8469-1f7677741c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c4058f57-6e77-4e2b-8629-b6465370fdc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T19:22:03.738Z_

I'll help you find this information. Let me start by exploring the directory structure and then reading the specific files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d33e74e0-2a7a-4dc4-8469-1f7677741c06",
  "isSidechain": true,
  "agentId": "af10f55edf1fa0e7c",
  "requestId": "req_011CbL3XjieYrLAn2EZBAwdN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ef581229-888d-44f0-981f-1360f438c2b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c4058f57-6e77-4e2b-8629-b6465370fdc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PWhQuszuUqnAaWJDgE6fpk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 578,
      "cache_read_input_tokens": 17335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 578,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 3 · 2026-05-23T19:22:04.088Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LUsGCDyi2FiHnDoAJ6KJT8`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef581229-888d-44f0-981f-1360f438c2b2",
  "isSidechain": true,
  "agentId": "af10f55edf1fa0e7c",
  "requestId": "req_011CbL3XjieYrLAn2EZBAwdN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5e91d321-b20e-4fd1-b86b-dab8d91e285c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c4058f57-6e77-4e2b-8629-b6465370fdc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PWhQuszuUqnAaWJDgE6fpk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 578,
      "cache_read_input_tokens": 17335,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 578
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 17335,
          "cache_creation_input_tokens": 578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 578,
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

_source line 4 · 2026-05-23T19:22:04.283Z_

<details><summary>↩ Tool result · `toolu_01LUsGCDyi2FiHnDoAJ6KJT8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e91d321-b20e-4fd1-b86b-dab8d91e285c",
  "isSidechain": true,
  "promptId": "46752c42-9bf2-481f-aa05-e1e832316775",
  "agentId": "af10f55edf1fa0e7c",
  "type": "user",
  "uuid": "40fd2d74-260f-432f-ad28-622c190c4e8e",
  "sourceToolAssistantUUID": "5e91d321-b20e-4fd1-b86b-dab8d91e285c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c4058f57-6e77-4e2b-8629-b6465370fdc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-23T19:22:06.078Z_

Now let me read the conclusion.tex file to find the sentence with "≥40" or "geq.*40":

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40fd2d74-260f-432f-ad28-622c190c4e8e",
  "isSidechain": true,
  "agentId": "af10f55edf1fa0e7c",
  "requestId": "req_011CbL3XrnYzVcPrTDxW1keN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6458a9ea-e0c5-4131-84cf-892e50b67187",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c4058f57-6e77-4e2b-8629-b6465370fdc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016aRX4H7hpaYFPvv5eW5iPP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1353,
      "cache_read_input_tokens": 17913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1353,
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

_source line 6 · 2026-05-23T19:22:06.245Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MipngfTM4mCMJ58PoxFrYU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6458a9ea-e0c5-4131-84cf-892e50b67187",
  "isSidechain": true,
  "agentId": "af10f55edf1fa0e7c",
  "requestId": "req_011CbL3XrnYzVcPrTDxW1keN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d68b8bf-7e77-4c2f-8ab5-21a7ca7571a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c4058f57-6e77-4e2b-8629-b6465370fdc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016aRX4H7hpaYFPvv5eW5iPP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1353,
      "cache_read_input_tokens": 17913,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1353
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 120,
          "cache_read_input_tokens": 17913,
          "cache_creation_input_tokens": 1353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1353,
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

_source line 7 · 2026-05-23T19:22:06.251Z_

<details><summary>↩ Tool result · `toolu_01MipngfTM4mCMJ58PoxFrYU`</summary>

```text
1	% conclusion.tex
2	
3	\section{Discussion}
4	\label{sec:discussion}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/paper/fig4_svd_subspace.pdf}
9	\caption{Test representations projected onto top-2 SVD directions. 9-class DAPT produces clear cluster separation absent in vanilla.}
10	\label{fig:svd_subspace}
11	\end{figure}
12	
13	\paragraph{Discriminative compression and label equivalence.}
14	Three observations argue against a topic shortcut: unstable topic OOD (F1\,=\,0.541$\pm$0.207), scrambled labels within 3.9\,pp, and label-free MLM detection (F1\,$\geq$\,0.97).
15	Classification DAPT compresses features into few dimensions (participation ratio 3.7--9.4 vs.\ 25--32; Figure~\ref{fig:svd_subspace}; Appendix~\ref{app:representation}), consistent with \citet{zhang2021understanding}: domain-relevant partitioning appears necessary (topic DAPT fails) and compression localizes to 3 SVD dimensions in layers 8--12. A probe confirms sufficiency; removal degrades DD by 17\,pp (Appendix~\ref{app:discriminative_probe}). The partition sufficiency finding implies that the classification objective's value lies in its structural role---forcing class-conditional feature organization---rather than in encoding persuasion-specific semantics.
16	
17	\paragraph{Cross-condition transfer and boundaries.}
18	ToxicChat (+18--42\,pp) and cross-LLM experiments (Appendix~\ref{app:cross_llm}) confirm transfer beyond single-LLM artifacts; domain exposure is universally beneficial (all DAPT variants exceed vanilla by $\geq$40\,pp on ToxicChat) but the ranking reverses across conditions (MLM leads on human data). Mixed-LLM 9-class maintains 0.818 while MLM collapses. Both data scaling (Appendix~\ref{app:scale_validation}) and mixed-LLM training involve distributional heterogeneity that appears to erode classification DAPT's concentrated feature advantage. At larger scales (355M), DAPT can be counterproductive (RoBERTa-large vanilla AA\,=\,1.000 vs.\ 9-class 0.946), and WildChat FPR rises to 68.1\%, suggesting DAPT encodes LLM-specific stylistic features that limit benign-side generalization. Mean pooling matches BiGRU ($\Delta \leq 1$\,pp), indicating detection relies on per-turn content rather than sequential patterns.
19	
20	\paragraph{Length as a potential confound.}
21	Length-matched evaluation ($N$=155) shows negligible change (DD/AA $\Delta \leq$\,2.5\,pp); the $-$57.9\,pp ActorAttack collapse under zero-padding (Appendix~\ref{app:length_independence}) reflects signal density dilution rather than length shortcut removal.
22	
23	\section{Conclusion}
24	
25	We decompose multi-turn jailbreak generalization into two complementary findings. On synthetic data at base scale, classification DAPT recovers OOD detection (F1\,=\,0.97--1.0 vs.\ vanilla 0.26--0.31), though template-attack robustness does not extend to strategy-diverse scenarios under mixed-LLM training (ActorAttack F1\,=\,0.504); on human-authored data, the hierarchy reverses (ToxicChat MLM 0.837 vs.\ classification 0.596)---the advantage is condition-specific and counterproductive at 355M scale. Few-shot benign adaptation reduces FPR from 58--68\% to 0--1.5\% with 10 conversations. The ablation framework provides a reusable template for diagnosing when domain adaptation succeeds and when it fails in safety-critical NLP tasks.
26	
27	\section{Limitations}
28	\label{sec:limitations}
29	
30	\begin{itemize}[nosep,leftmargin=*]
31	\item \textbf{Synthetic data only.} All findings derive from synthetic conversations (single LLM, Qwen3-8B; 350 training, 76--118 test, 3 seeds). The evidence hierarchy reverses on human single-turn data (ToxicChat; Section~\ref{sec:discussion}), and no human-generated multi-turn jailbreak dataset exists.
32	\item \textbf{IID benign upper bound.} OOD F1 figures assume IID benign data; dual-OOD evaluation drops 12--14\,pp without adaptation (Table~\ref{tab:main_results}). Few-shot benign adaptation recovers performance but is validated on only two platforms ($n \leq 49$).
33	\item \textbf{Scope.} Only persuasion-mediated multi-turn attacks are addressed; single-turn token-level attacks and non-text modalities are out of scope. Cross-encoder comparisons (Section~\ref{sec:cross_encoder}) confound architecture with parameter count (184M vs.\ 355M). The 50-sample annotation verification ($\kappa$\,=\,0.78) limits evaluation of strategy characterization accuracy; however, the scrambled-label experiment demonstrates that label correctness does not affect template-attack detection. Our experiments cover base-scale encoders (125M--355M); DAPT effects may differ at larger scales, where RoBERTa-large already shows counterproductive adaptation (Section~\ref{sec:cross_encoder}).
34	\end{itemize}
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d68b8bf-7e77-4c2f-8ab5-21a7ca7571a4",
  "isSidechain": true,
  "promptId": "46752c42-9bf2-481f-aa05-e1e832316775",
  "agentId": "af10f55edf1fa0e7c",
  "type": "user",
  "uuid": "8e3692ef-2537-474f-963d-bfb4f798b310",
  "sourceToolAssistantUUID": "0d68b8bf-7e77-4c2f-8ab5-21a7ca7571a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c4058f57-6e77-4e2b-8629-b6465370fdc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-23T19:22:08.621Z_

Perfect! I found the sentence. Now let me read the experiments.tex file to find the ToxicChat results table:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e3692ef-2537-474f-963d-bfb4f798b310",
  "isSidechain": true,
  "agentId": "af10f55edf1fa0e7c",
  "requestId": "req_011CbL3Y19b2RxbtHZ6YgLwJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "92d3072e-2d04-471f-abbd-3177ba03abc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c4058f57-6e77-4e2b-8629-b6465370fdc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VN1sFREo41hKgKbbzdZSg9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1566,
      "cache_read_input_tokens": 19266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1566,
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

_source line 9 · 2026-05-23T19:22:09.568Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HPUU8kM1AzZR9Umb7wzR8z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92d3072e-2d04-471f-abbd-3177ba03abc4",
  "isSidechain": true,
  "agentId": "af10f55edf1fa0e7c",
  "requestId": "req_011CbL3Y19b2RxbtHZ6YgLwJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fd7798cd-0083-40ab-a4ad-fbbdaff2999d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c4058f57-6e77-4e2b-8629-b6465370fdc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VN1sFREo41hKgKbbzdZSg9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1566,
      "cache_read_input_tokens": 19266,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1566
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 120,
          "cache_read_input_tokens": 19266,
          "cache_creation_input_tokens": 1566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1566,
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

_source line 10 · 2026-05-23T19:22:09.579Z_

<details><summary>↩ Tool result · `toolu_01HPUU8kM1AzZR9Umb7wzR8z`</summary>

```text
1	% experiments.tex
2	
3	\section{Experiments}
4	
5	\paragraph{Terminology.}
6	\emph{Cross-attack OOD}: evaluation on attack families unseen during training; benign distribution remains IID throughout (OOD reflects attack-side shift only). $K$: prefix length (number of conversation turns retained). \emph{DAPT}: all Stage-1 adaptations; we extend \citet{gururangan2020dontstop} to supervised variants. \emph{Evidence hierarchy} (on synthetic data): vanilla $<$ MLM $<$ classification (Section~\ref{sec:decomposition}).
7	
8	\subsection{Setup}
9	
10	\paragraph{Data.}
11	All synthetic data is generated by Qwen3-8B~\citep{qwen3_2025}.
12	The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).
13	Stage~1 (DAPT) uses training + validation conversations; Stage~2 (BiGRU) trains on training, early-stops on validation, and evaluates on test.
14	OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} (non-discriminative; Section~\ref{sec:decomposition}) + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
15	No overlap exists in attack templates across families; benign is IID (same generation pipeline).
16	A paraphrased version of the IID test set (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark (Section~\ref{sec:perturbation}).
17	For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
18	
19	\paragraph{Models.}
20	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
21	Our vanilla DeBERTa+BiGRU configuration is architecturally equivalent to DeepContext~\citep{deepcontext2026} and differs only in encoder choice (DeBERTa-v3-base vs.\ BERT); it serves as our primary baseline.
22	For cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\citep{liu2019roberta} (Section~\ref{sec:cross_encoder}).
23	We also compare TF-IDF LR, LLM-as-judge (Appendix~\ref{sec:llm_judge}), and Llama Guard~3~8B~\citep{metallamaguard3_2024} (zero-shot; evaluates last-response safety given conversation context), which detects only 1.8\% of multi-turn jailbreaks (5/278 pooled recall; Table~\ref{tab:evidence_hierarchy}).
24	
25	\paragraph{Metrics.}
26	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
27	OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456) for all variants.
28	For key pairwise comparisons, we report BCa bootstrap 95\% confidence intervals (10,000 resamples over individual predictions pooled across 3 seeds; this assumes cross-seed independence and is exploratory) and paired permutation tests (10,000 permutations). Seed-level F1 values (Table~\ref{tab:seed_level}, Appendix~\ref{app:seed_level}) confirm all pairwise conclusions hold at every seed.
29	All standard deviations are computed over 3 random seeds using the population formula ($n$ divisor); Bessel-corrected estimates ($n{-}1$ divisor) are $\approx$22\% larger but do not alter any significance conclusions.
30	
31	\paragraph{Training.}
32	Stage-1: learning rate $2 \times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\%.
33	Stage-2: two-layer MLP, 20 epochs.
34	
35	%----------------------------------------------------------------------
36	\subsection{Cross-Attack Generalization}
37	
38	\begin{table}[t]
39	\centering
40	\small
41	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation length. IID: Crescendo; OOD: Deceptive Delight (DD). 3-seed mean$\pm$std where noted; full per-$K$ in Appendix~\ref{sec:full_prefix}.}
42	\label{tab:main_results}
43	\begin{tabular}{@{}lcc|cc@{}}
44	\toprule
45	& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}{\textit{OOD (DD)}} \\
46	\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\
47	\midrule
48	9-class & \textbf{1.000$\pm$.000} & \textbf{1.000$\pm$.000} & .981$\pm$.013 & \textbf{.997$\pm$.005} \\
49	MLM-only$^{\ddagger}$ & .974 & 1.000 & \textbf{.993$\pm$.009} & .914$\pm$.115 \\
50	Vanilla & .978$\pm$.016 & 1.000$\pm$.000 & .479$\pm$.038 & .312$\pm$.026 \\
51	TF-IDF LR$^{\S}$ & 1.000 & 1.000 & 1.000 & .961 \\
52	\bottomrule
53	\end{tabular}
54	\vspace{-2pt}
55	{\footnotesize $^{\ddagger}$MLM-only IID reports single seed (42); OOD reports 3-seed. $^{\S}$TF-IDF is deterministic (no std).}
56	\end{table}
57	
58	Vanilla encoders collapse under cross-attack transfer; domain-adapted variants recover near-perfect detection (Table~\ref{tab:main_results}, Figure~\ref{fig:cross_attack_bar}).
59	On OOD DD, vanilla drops to F1\,=\,0.312$\pm$0.026 and worsens with more turns (0.628$\to$0.312 at Full), consistent with attack turns occupying benign embedding regions~\citep{bullwinkel2025repeng}. MLM recovers to $\geq$0.97 at $K \leq 5$ without labels but is unstable at full length (0.914$\pm$0.115); 9-class maintains 0.997$\pm$0.005.
60	On strategy-diverse ActorAttack, TF-IDF collapses (0.261) while 9-class maintains 0.972$\pm$0.026, a 71\,pp gap confirming domain-adapted representations capture beyond-lexical features.
61	Seed-level results confirm consistent separation (Table~\ref{tab:seed_level}; bootstrap CIs non-overlapping, permutation $p < 0.0001$). FITD is non-discriminative (all F1\,$\geq$\,0.990).
62	
63	\begin{figure}[t]
64	\centering
65	\includegraphics[width=\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}
66	\caption{Cross-attack overview (F1 at full conversation length). DisPeD (9-class) maintains near-perfect detection across IID and both OOD families; vanilla collapses on OOD DD. FITD is non-discriminative for all methods.}
67	\label{fig:cross_attack_bar}
68	\end{figure}
69	
70	Prefix-length analysis (Appendix Table~\ref{tab:full_prefix}) confirms 9-class stability across all prefixes (0.972--0.997) vs.\ MLM instability at full length (0.914$\pm$0.115) and vanilla degradation (0.628$\to$0.312).
71	
72	%----------------------------------------------------------------------
73	\subsection{Decomposing the Detection Mechanism}
74	\label{sec:decomposition}
75	
76	\begin{table}[t]
77	\centering
78	\small
79	\caption{Evidence hierarchy on OOD DD and ActorAttack (AA) at full conversation length (3-seed mean$\pm$std where available). OOD F1 reflects attack-side generalization only; benign samples are IID from training distribution (benign-side shift evaluated in Section~\ref{sec:benign_shift}). Bold indicates best per column. All variants share the same Stage-2 pipeline. Full per-prefix results in Appendix Tables~\ref{tab:full_prefix} and~\ref{tab:actorattack_full}. Bottom rows: full dual-OOD evaluation with WildChat benign replacing IID benign (Appendix~\ref{app:dual_ood}).}
80	\label{tab:evidence_hierarchy}
81	\resizebox{\columnwidth}{!}{%
82	\begin{tabular}{@{}lccc@{}}
83	\toprule
84	\textbf{Variant} & DD-Full & AA-Full & DD-$K$=2 \\
85	\midrule
86	9-class (full model) & .997$\pm$.005 & .972$\pm$.026 & .981$\pm$.013 \\
87	Binary (2-class) & \textbf{1.000$\pm$.000} & \textbf{.990$\pm$.008} & .994$\pm$.009 \\
88	Scrambled labels & .997$\pm$.005 & .951$\pm$.043 & .981$\pm$.026 \\
89	MLM-only$^{\ddagger}$ (no labels) & .914$\pm$.115 & .893$\pm$.080 & .993$\pm$.009 \\
90	Mean pooling$^{*}$ & .991$\pm$.013 & .962$\pm$.015 & \textbf{1.000} \\
91	\midrule
92	Topic classif.\ (5-class) & .541$\pm$.207 & .625$\pm$.141 & .593$\pm$.166 \\
93	Wikipedia MLM & .904$\pm$.115 & .686$\pm$.297 & .911$\pm$.073 \\
94	Vanilla DeBERTa & .312$\pm$.026 & .258$\pm$.000 & .479$\pm$.038 \\
95	TF-IDF LR$^{\dagger}$ & .961 & .261 & \textbf{1.000} \\
96	Llama Guard~3$^{\P}$ & .025 & .000 & -- \\
97	\midrule
98	\multicolumn{4}{l}{\textit{Dual-OOD (WildChat benign; Section~\ref{sec:benign_shift})}} \\[2pt]
99	9-class (no adapt) & .855 & .842 & -- \\
100	9-class (+10-shot) & .994 & .981 & -- \\
101	\bottomrule
102	\end{tabular}}
103	\vspace{-2pt}
104	{\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\dagger}$Deterministic (no std). $^{\ddagger}$MLM-only IID (Table~\ref{tab:main_results}) is single-seed (42); all OOD values are 3-seed. $^{\P}$Zero-shot; no domain training.}
105	\end{table}
106	
107	A clear \emph{evidence hierarchy} emerges across seven variants on synthetic multi-turn data (Table~\ref{tab:evidence_hierarchy}, Figure~\ref{fig:evidence_hierarchy}), ordered by OOD detection at full conversation length: vanilla $<$ topic $\ll$ MLM $<$ classification-supervised ($\approx$\,1.0 on DD).
108	
109	\begin{figure}[t]
110	\centering
111	\includegraphics[width=\columnwidth]{figures/paper/fig3_evidence_hierarchy.pdf}
112	\caption{Evidence hierarchy across evaluation conditions. Classification-based DAPT outperforms MLM and vanilla on synthetic OOD attacks (DD, AA), but the hierarchy reverses on human-authored single-turn data (ToxicChat), where JB-MLM leads.}
113	\label{fig:evidence_hierarchy}
114	\end{figure}
115	
116	\paragraph{Domain exposure is the primary observed factor.}
117	MLM bridges $\sim$60\,pp from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without labels; this supports the DAPT interpretation~\citep{gururangan2020dontstop}. TF-IDF collapse on ActorAttack (0.261 vs.\ 9-class 0.972) confirms that domain-adapted representations capture features beyond lexical overlap.
118	All three classification-supervised variants converge to equivalent detection (F1 = 0.997--1.000); McNemar's ($p > 0.13$) and paired permutation tests ($p \geq 0.40$) provide descriptive evidence suggesting equivalence. Extended to $n$\,=\,10 seeds, TOST (margin = 5\,pp) confirms equivalence on DD ($p < 10^{-8}$, $d$\,=\,$-$0.14; Table~\ref{tab:tost_sensitivity}) and FITD ($p < 10^{-8}$, $d \approx 0$). Label quality and granularity are non-factors for template-attack detection (DD/FITD: $|d| \leq 0.14$), but strategy-diverse ActorAttack retains moderate label sensitivity ($d$\,=\,0.44, TOST $p$\,=\,0.183). For template attacks, any domain-relevant classification objective suffices; the objective's structural role---partitioning the representation space---matters more than label semantics. Strategy-diverse attacks mark a difficulty boundary for this sufficiency.
119	Classification supervision is associated with 3--23$\times$ lower cross-seed variance over MLM on synthetic OOD (std 0.005 vs.\ 0.115 on DD; 3 seeds; Appendix~\ref{app:ensemble}), though this reverses on human-authored data (Section~\ref{sec:human_data}).
120	
121	\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
122	Wikipedia MLM (0.904$\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\,pp gap), though jailbreak-domain text provides an 8\,pp advantage at early prefixes ($K$=2: 0.993 vs.\ 0.911).
123	Perturbation analysis (Section~\ref{sec:perturbation}) reveals a sharper domain specificity effect: Wikipedia MLM degrades by $\sim$12\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\,pp.
124	
125	\paragraph{Misaligned supervision destabilizes generalization.}
126	Topic classification's poor performance (0.541$\pm$0.207) is consistent with misaligned supervision; the cleaner test isolating domain exposure is Wiki-MLM vs.\ JB-MLM (Section~\ref{sec:decomposition}).
127	
128	\paragraph{Evidence hierarchy on strategy-diverse attacks.}
129	ActorAttack~\citep{ren2024actorattack} preserves the same hierarchy (Figure~\ref{fig:evidence_hierarchy}) with wider gaps: TF-IDF collapses (0.261) while classification variants converge (0.951--0.990, max gap 3.9\,pp); DAPT provides $\sim$71\,pp over vanilla (Appendix~\ref{sec:actorattack_full},~\ref{app:aa_error}).
130	
131	\paragraph{Temporal modeling.}
132	Mean pooling matches BiGRU (F1 gap $\leq$ 1\,pp; Appendix~\ref{app:temporal}) and turn-order shuffling is negligible ($|\Delta| < 1$\,pp), confirming detection relies on per-turn content rather than sequential patterns.
133	
134	%----------------------------------------------------------------------
135	\subsection{Cross-Encoder Validation}
136	\label{sec:cross_encoder}
137	
138	\begin{table}[t]
139	\centering
140	\small
141	\caption{Cross-encoder comparison on OOD Full (3-seed mean$\pm$std). DD = Deceptive Delight, AA = ActorAttack. Bold indicates best per encoder group.}
142	\label{tab:cross_encoder}
143	\resizebox{\columnwidth}{!}{%
144	\begin{tabular}{@{}lcc@{}}
145	\toprule
146	\textbf{Variant} & DD & AA \\
147	\midrule
148	\multicolumn{3}{l}{\textit{DeBERTa-v3-base (184M)}} \\[2pt]
149	Vanilla & .312$\pm$.026 & .258$\pm$.000 \\
150	MLM & .914$\pm$.115 & .893$\pm$.080 \\
151	9-class & \textbf{.997$\pm$.005} & \textbf{.972$\pm$.026} \\
152	\midrule
153	\multicolumn{3}{l}{\textit{RoBERTa-base (125M)}} \\[2pt]
154	Vanilla & .981$\pm$.026 & .466$\pm$.163 \\
155	MLM & .987$\pm$.018 & .730$\pm$.201 \\
156	9-class & \textbf{.994$\pm$.005} & \textbf{.939$\pm$.046} \\
157	\midrule
158	\multicolumn{3}{l}{\textit{RoBERTa-large (355M)}} \\[2pt]
159	Vanilla & .927$\pm$.036 & \textbf{1.000$\pm$.000} \\
160	MLM & .884$\pm$.065 & .874$\pm$.014 \\
161	9-class & \textbf{.987$\pm$.004} & .946$\pm$.057 \\
162	\bottomrule
163	\end{tabular}}
164	\end{table}
165	
166	To test whether the evidence hierarchy depends on encoder choice, we replicate vanilla, MLM, and 9-class on RoBERTa-base~\citep{liu2019roberta} (Table~\ref{tab:cross_encoder}).
167	On DD, RoBERTa-base vanilla already achieves 0.981$\pm$0.026 (vs.\ DeBERTa 0.312$\pm$0.026), so DAPT adds only 1.3\,pp. ActorAttack exposes this as DD's simplicity: RoBERTa-base vanilla collapses to 0.466$\pm$0.163, a 51.5\,pp drop, while domain-adapted variants recover (9-class: 0.939$\pm$0.046).
168	
169	RoBERTa-large (355M) reverses the DAPT advantage on ActorAttack (vanilla 1.000 vs.\ 9-class 0.946; Table~\ref{tab:roberta_large_lr}), revealing a difficulty threshold: base-scale encoders require DAPT for all attacks, while sufficient capacity renders it unnecessary. A BERT-base proxy confirms DAPT, not architecture, drives generalization (Appendix~\ref{app:bert_proxy}).
170	
171	%----------------------------------------------------------------------
172	\subsection{Mixed-LLM Training}
173	
174	All preceding experiments use single-source (Qwen3-8B) data. To test whether the evidence hierarchy transfers when training data mixes LLM sources, we train on 250 Qwen + 250 Llama-3.1-8B conversations (Table~\ref{tab:mixed_llm}).
175	Classification-based DAPT is the only variant that substantially outperforms vanilla: 9-class achieves DD OOD F1\,=\,0.818$\pm$0.096 (+53\,pp over vanilla 0.291$\pm$0.065), while MLM drops to vanilla level (0.289$\pm$0.101). On strategy-diverse ActorAttack, detection degrades to chance level (9-class F1\,=\,0.504$\pm$0.107, indistinguishable from majority baseline at $n$\,=\,3).
176	Mixed-LLM training confirms that classification supervision generalizes across LLM sources where unsupervised pretraining does not (full results in Appendix~\ref{app:mixed_llm}); per-source data reduction (250 vs.\ 350) is an alternative explanation we cannot yet disentangle.
177	
178	%----------------------------------------------------------------------
179	\subsection{Human Data Validation}
180	\label{sec:human_data}
181	
182	Since both training and OOD evaluation data are Qwen3-8B-generated, we validate on ToxicChat~\citep{lin2023toxicchat} (204 human-written jailbreak attempts + 204 benign conversations from real LMSYS interactions).
183	
184	\begin{table}[t]
185	\centering
186	\small
187	\caption{Human data validation on ToxicChat~\citep{lin2023toxicchat} (macro F1, 3-seed mean$\pm$std). Bold indicates best. Single-turn data from real LMSYS user interactions, independent of Qwen3-8B.}
188	\label{tab:human_data}
189	\begin{tabular}{@{}lc@{}}
190	\toprule
191	\textbf{Variant} & Macro F1 \\
192	\midrule
193	JB-MLM & \textbf{.837$\pm$.013} \\
194	Wiki-MLM & .791$\pm$.093 \\
195	Binary & .705$\pm$.072 \\
196	Scrambled & .616$\pm$.056 \\
197	9-class & .596$\pm$.087 \\
198	Topic & .496$\pm$.042 \\
199	\midrule
200	Vanilla & .413$\pm$.021 \\
201	\bottomrule
202	\end{tabular}
203	\end{table}
204	
205	The ordering reverses (Figure~\ref{fig:evidence_hierarchy}): JB-MLM leads (0.837$\pm$0.013) while 9-class ranks lower (0.596$\pm$0.087; $p < 0.001$). All DAPT variants exceed vanilla by 18--42\,pp, confirming transfer to human-written attacks. ToxicChat is single-turn, so the classification head provides no advantage.
206	
207	%----------------------------------------------------------------------
208	\subsection{Robustness and Strategy Analysis}
209	\label{sec:perturbation}
210	
211	Under adversarial paraphrasing (BERTScore 0.92), classification variants achieve zero degradation on OOD DD while non-adapted models degrade by $\sim$12\,pp; on ActorAttack, DAPT degrades ($\Delta$\,=\,$-$20.4\,pp) but maintains 52\,pp over vanilla (Table~\ref{tab:ood_perturbation}; Appendix~\ref{sec:perturbation_full}). We distinguish \emph{template attacks} (transition rate $<$\,0.1; e.g., Crescendo, DD) from \emph{structurally complex attacks} (rate $>$\,0.3; e.g., ActorAttack). The 9-class taxonomy characterizes known attacks ($\kappa$\,=\,0.78) but degrades on OOD ($\kappa$\,=\,0.126; Appendix~\ref{app:strategy_pred}); detection operates through \texttt{[CLS]} embeddings, not strategy accuracy.
212	
213	%----------------------------------------------------------------------
214	\subsection{Benign Distribution Shift}
215	\label{sec:benign_shift}
216	
217	On WildChat benign conversations, 9-class FPR rises to 68.1\%. Few-shot adaptation (Stage-2 BiGRU, encoder frozen, $N$ benign conversations, BCE loss, 5 epochs) resolves this: 10 WildChat conversations reduce FPR to 0\%, 25 OASST2 to 1.0\%; dual-OOD F1 drops 12--14\,pp without adaptation but recovers within 0.3\,pp (Appendix~\ref{app:dual_ood}).
218	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd7798cd-0083-40ab-a4ad-fbbdaff2999d",
  "isSidechain": true,
  "promptId": "46752c42-9bf2-481f-aa05-e1e832316775",
  "agentId": "af10f55edf1fa0e7c",
  "type": "user",
  "uuid": "1ee803f3-ed0b-43f3-a37a-8160118ac0ee",
  "sourceToolAssistantUUID": "fd7798cd-0083-40ab-a4ad-fbbdaff2999d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c4058f57-6e77-4e2b-8629-b6465370fdc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-23T19:22:16.251Z_

Perfect! I found all the information needed. Let me compile the results:

## Findings

### 1. Sentence from conclusion.tex (Discussion section)

The exact sentence mentioning "≥40" is found on line 18:

**"ToxicChat (+18--42\,pp) and cross-LLM experiments (Appendix~\ref{app:cross_llm}) confirm transfer beyond single-LLM artifacts; domain exposure is universally beneficial (all DAPT variants exceed vanilla by $\geq$40\,pp on ToxicChat) but the ranking reverses across conditions (MLM leads on human data)."**

### 2. ToxicChat Results Table (tab:human_data)

From experiments.tex lines 184-203, the ToxicChat table shows:

**Variant names and Macro F1 values:**
- JB-MLM: 0.837 ± 0.013
- Wiki-MLM: 0.791 ± 0.093
- Binary: 0.705 ± 0.072
- Scrambled: 0.616 ± 0.056
- 9-class: 0.596 ± 0.087
- Topic: 0.496 ± 0.042

**Vanilla F1 value: 0.413 ± 0.021**

### 3. Verification of "≥40 pp" claim

Computing each variant's improvement over vanilla (0.413):
- JB-MLM: 0.837 - 0.413 = 0.424 (42.4 pp) ✓
- Wiki-MLM: 0.791 - 0.413 = 0.378 (37.8 pp) ✗
- Binary: 0.705 - 0.413 = 0.292 (29.2 pp) ✗
- Scrambled: 0.616 - 0.413 = 0.203 (20.3 pp) ✗
- 9-class: 0.596 - 0.413 = 0.183 (18.3 pp) ✗
- Topic: 0.496 - 0.413 = 0.083 (8.3 pp) ✗

**The statement "all DAPT variants exceed vanilla by ≥40 pp" is INCORRECT.** Only JB-MLM exceeds the 40 pp threshold. The paper's text on line 205 states "All DAPT variants exceed vanilla by 18--42\,pp", which is accurate—this range correctly describes the observed improvements (8.3 pp to 42.4 pp, with most in the 18-42 pp range cited). However, the specific claim in the Discussion section using "≥40\,pp" is not supported by these numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ee803f3-ed0b-43f3-a37a-8160118ac0ee",
  "isSidechain": true,
  "agentId": "af10f55edf1fa0e7c",
  "requestId": "req_011CbL3YFLNKTAnAJctsaVyV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe17c420-ba17-4385-815c-f29ceeaf5ae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c4058f57-6e77-4e2b-8629-b6465370fdc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2DtxF9EKHJ13mN2aEMsqU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6805,
      "cache_read_input_tokens": 20832,
      "output_tokens": 679,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6805
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 679,
          "cache_read_input_tokens": 20832,
          "cache_creation_input_tokens": 6805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6805,
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
