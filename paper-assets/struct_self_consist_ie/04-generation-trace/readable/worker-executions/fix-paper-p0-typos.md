# fix paper p0 typos

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_fix_paper_p0_typos_20260519T135358.log`
- **Structured JSON:** [`93f9094b6db171d847ec.json`](../../sessions/93/93f9094b6db171d847ec.json)

## Before a recorded user message

43 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "975d168c-805d-4624-8f2d-4db0989ec4ba",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779211800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0cb3ab22-f6bf-4f30-a8b4-c521ae100947",
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the relevant files to find the exact strings that need to be changed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "206ba6ad-75f2-4e8b-8657-663db4572803",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsaH36rgyDAfhSk5TgwZs8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11960,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11960
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

Let me read the relevant lines in the files to find the exact strings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "cbfd2c97-7103-49e0-9f3b-ad71e6b51e96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsaH36rgyDAfhSk5TgwZs8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11960,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11960
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_013ePstz4i43DCG88KUxCxYH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 95,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "08f5128e-e77c-4a75-b173-fe698f8cbdf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsaH36rgyDAfhSk5TgwZs8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11960,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11960
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T13:54:09.755Z_

<details><summary>↩ Tool result · `toolu_013ePstz4i43DCG88KUxCxYH`</summary>

```text
95	
96	\paragraph{LP: the sole per-sample signal also fails.}
97	On SciERC ($n{=}529$, 2-seed sign tests\footnote{MDE${\approx}$1.5~pp at 80\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.
98	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \textit{degradation} (Appendix~\ref{app:tost}).
99	Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\S\ref{sec:fewnerd}), while structural signals still degrade selection.
100	
101	\paragraph{Qualitative factors governing selection effectiveness.}
102	Three factors qualitatively shape LP selection gains: (1)~\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\%, CoNLL 48.4\%; Table~\ref{tab:fewnerd}); (2)~\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\approx}2$\,pp vs.\ SciERC 13.1\,pp); (3)~\textit{LP-quality alignment}, measured as within-instance $\rho(\text{LP}, \text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\rho{\approx}0.5$--$0.7$ vs.\ SciERC $\rho{\approx}0.26$).
103	These factors are consistent with the observed pattern (Table~\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\pm}0.48$\,pp, 3-seed; Table~\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\% of instances yield F1${=}0$.
104	Yet QE remains effective on WNUT-17 (VC $\rho{=}0.730$; Table~\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.
105	This characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\S\ref{sec:fewnerd}, \S\ref{sec:discussion}).
106	
107	%% ============================================================
108	\subsection{Cross-Dataset Contrast: Few-NERD}
109	\label{sec:fewnerd}
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\ref{tab:multiseed}). $p$: paired bootstrap.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "a5acf593-92eb-411c-9c3a-479792aede3f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\n\\paragraph{LP: the sole per-sample signal also fails.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n\n\\paragraph{Qualitative factors governing selection effectiveness.}\nThree factors qualitatively shape LP selection gains: (1)~\\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\\%, CoNLL 48.4\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\\approx}2$\\,pp vs.\\ SciERC 13.1\\,pp); (3)~\\textit{LP-quality alignment}, measured as within-instance $\\rho(\\text{LP}, \\text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nThese factors are consistent with the observed pattern (Table~\\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\\pm}0.48$\\,pp, 3-seed; Table~\\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\\% of instances yield F1${=}0$.\nYet QE remains effective on WNUT-17 (VC $\\rho{=}0.730$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.\nThis characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}",
      "numLines": 20,
      "startLine": 95,
      "totalLines": 259
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01BZWLCUtwbYAm3knWHbJPkm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 0,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "bfa60a95-9a53-4125-ace6-d01c429b724e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsaH36rgyDAfhSk5TgwZs8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11960,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11960
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T13:54:10.253Z_

<details><summary>↩ Tool result · `toolu_01BZWLCUtwbYAm3knWHbJPkm`</summary>

```text
0	\section{Experiments}
1	\label{sec:experiments}
2	
3	\subsection{Experimental Setup}
4	\label{sec:setup}
5	
6	\paragraph{Datasets.}
7	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
8	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
9	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
12	
13	\paragraph{Models and sampling.}
14	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
16	
17	%% ============================================================
18	\subsection{Quality Estimation Results}
19	\label{sec:qe_results}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "f68fe52d-c608-4ea1-bd69-7140749f4d64",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 52\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\n\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}",
      "numLines": 20,
      "startLine": 0,
      "totalLines": 259
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01HiBZJHUKs4Aj7kTgTP599v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
  "offset": 0,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "3c104d12-036b-4bc7-85c6-acce7b410dbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsaH36rgyDAfhSk5TgwZs8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11960,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11960
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T13:54:11.073Z_

<details><summary>↩ Tool result · `toolu_01HiBZJHUKs4Aj7kTgTP599v`</summary>

```text
0	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
1	All experiments use English-language datasets; cross-lingual generalization remains untested.
2	Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
3	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.
4	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
5	
6	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
7	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
8	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
9	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
10	We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
11	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
12	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
13	We tested one remedy for LP compression (entity-token-only LP, excluding format/schema tokens) which fails to improve selection despite increasing within-instance variance on SciERC ($4{\times}$); LP${\times}$VC combinations also fail to recover selection (\S\ref{sec:discussion}). Our supervised signal combination baseline uses only the five unsupervised signals studied; a DeBERTa verifier encoding input-output pairs also fails to close the gap (preliminary, SciERC $n{=}106$), hidden state probes on the generating model's representations improve correlation ($+37$\% on SciERC) but do not improve selection (gap closure $-5.1$\%; Appendix~\ref{app:hidden_probe}), ; the bottleneck extends to model-internal access. Entity embeddings and calibration-based approaches remain untested.
14	Other per-sample scoring methods exist but were not evaluated: Self-Certainty \cite{kang2025selfcertainty} (consistency of token-level self-evaluation) and P(True) \cite{kadavath2022language} (model's own probability estimate of correctness) both produce per-sample scores and could in principle address the alignment bottleneck; whether they suffer from similar compression under fine-tuning is unknown.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "1c175570-ca82-4144-8dbc-d7f54546944a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.\nAll experiments use English-language datasets; cross-lingual generalization remains untested.\nEntity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\\% F1${=}0$), this precondition fails and construction cannot improve over greedy.\nWe cover 4B\\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.\nOur supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.\n\nWe evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\\ref{app:n_scaling}).\nThe free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\\ref{app:re_extension}.\nQwen3-8B's SciERC checkpoint used empty \\texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nLP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.\nWe tested verbalized confidence \\cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\\ref{app:verbalized_confidence}).\nAd-hoc LP${\\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \\S\\ref{sec:discussion}); whether \\textit{learned} combinations could close the gap remains open.\nThe $\\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.\nWe tested one remedy for LP compression (entity-token-only LP, excluding format/schema tokens) which fails to improve selection despite increasing within-instance variance on SciERC ($4{\\times}$); LP${\\times}$VC combinations also fail to recover selection (\\S\\ref{sec:discussion}). Our supervised signal combination baseline uses only the five unsupervised signals studied; a DeBERTa verifier encoding input-output pairs also fails to close the gap (preliminary, SciERC $n{=}106$), hidden state probes on the generating model's representations improve correlation ($+37$\\% on SciERC) but do not improve selection (gap closure $-5.1$\\%; Appendix~\\ref{app:hidden_probe}), ; the bottleneck extends to model-internal access. Entity embeddings and calibration-based approaches remain untested.\nOther per-sample scoring methods exist but were not evaluated: Self-Certainty \\cite{kang2025selfcertainty} (consistency of token-level self-evaluation) and P(True) \\cite{kadavath2022language} (model's own probability estimate of correctness) both produce per-sample scores and could in principle address the alignment bottleneck; whether they suffer from similar compression under fine-tuning is unknown.",
      "numLines": 15,
      "startLine": 0,
      "totalLines": 18
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I have the exact strings. Let me make the edits:

1. **Fix 1**: Line 104 in experiments.tex: `VC $\rho{=}0.730$` → `VC $\rho{=}0.724$`
2. **Fix 2**: Line 11 in experiments.tex: `52\% zero F1` → `51\% zero F1`

The other locations (experiments.tex:103 and limitations.tex:2) already say "51%", so only experiments.tex:11 needs changing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "ed453b5c-a287-4287-a683-76926ffc8699",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmZsoPXXVfqL87zHwYJVZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3087,
      "cache_read_input_tokens": 23801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3087
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 13_

Found the exact strings. Making both fixes now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "f8f5bde3-73b4-42c9-a1fc-994da075b667",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmZsoPXXVfqL87zHwYJVZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3087,
      "cache_read_input_tokens": 23801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3087
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Edit · `toolu_01TfK37nSWHvtY8MdrK72qXk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "VC $\\rho{=}0.730$",
  "new_string": "VC $\\rho{=}0.724$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "7ca138b2-697d-44d0-b180-cce828d07aae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmZsoPXXVfqL87zHwYJVZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3087,
      "cache_read_input_tokens": 23801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3087
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T13:54:17.006Z_

<details><summary>↩ Tool result · `toolu_01TfK37nSWHvtY8MdrK72qXk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "652c14c6-3ac2-447d-a121-8b776e0ca01a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "oldString": "VC $\\rho{=}0.730$",
    "newString": "VC $\\rho{=}0.724$",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 52\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\n\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models ($\\varepsilon$-free; $\\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\\ref{app:epsilon_robustness}).\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nThis collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nFour of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\\S\\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.\nThe empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.\nLP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\nCross-instance $\\rho$ (Table~\\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}. $^\\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.775 \\pm 0.001$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & n/a$^\\dagger$ \\\\\nVC           & $0.623 \\pm 0.004$ & n/a$^\\dagger$ \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho$ (seed 42); line with error bars: $\\Delta$F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\nInstance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best.\n\n\\paragraph{LP: the sole per-sample signal also fails.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n\n\\paragraph{Qualitative factors governing selection effectiveness.}\nThree factors qualitatively shape LP selection gains: (1)~\\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\\%, CoNLL 48.4\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\\approx}2$\\,pp vs.\\ SciERC 13.1\\,pp); (3)~\\textit{LP-quality alignment}, measured as within-instance $\\rho(\\text{LP}, \\text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nThese factors are consistent with the observed pattern (Table~\\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\\pm}0.48$\\,pp, 3-seed; Table~\\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\\% of instances yield F1${=}0$.\nYet QE remains effective on WNUT-17 (VC $\\rho{=}0.730$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.\nThis characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}\n\\label{tab:fewnerd}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrccccr@{}}\n\\toprule\nDataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n\\midrule\nWNUT-17 & 1{,}287 & .452 & 67.9\\% & $-$.446 & $-$0.45\\,pp & .72 \\\\\nCoNLL & 2{,}756 & .908 & 48.4\\% & .302 & $-$0.85\\,pp & 1.0 \\\\\nSciERC & 529 & .644 & 17.8\\% & .205 & $+$0.61\\,pp & .193 \\\\\nFew-NERD & 32{,}565 & .748 & 13.8\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\\ref{tab:cross_selection}).\nTraining convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\\% and halves LP gains (Appendix~\\ref{app:epoch_confound}).\n\n\\paragraph{Degeneracy alone does not predict LP selection direction.}\nAcross 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\nCross-dataset prediction requires LP signal quality: Few-NERD ($\\rho{\\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\\rho{\\approx}0.26$) does not (Appendix~\\ref{app:conditional_decomp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nStructural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\\ref{app:n_scaling}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nWith Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\nDegeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nLoRA rank${=}8$ (vs.\\ 32) lowers degeneracy to 7.2\\% but LP remains below greedy ($\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$); temperature manipulation ($T{=}1.2$; \\S\\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.\n\n\\paragraph{Supervised signal combination and hidden probes.}\nSupervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\\ref{app:supervised_combination}).\nHidden state probes improve correlation ($+37$\\% on SciERC) but not selection (gap closure $-5.1$\\%; Appendix~\\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.\n\n%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nWe evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp).}\n\\label{tab:scale_comparison}\n\\begin{tabular}{@{}llcccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\\\\n       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$2 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nZero-shot 72B produces lower greedy F1 but larger oracle headroom (Table~\\ref{tab:scale_comparison}). LP $\\rho$ drops from $0.205$ to $0.081$ on SciERC and from $0.302$ to near zero on CoNLL; LP selection fails in both datasets (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), confirming that the gap is a structural property of the task rather than a fine-tuning artifact.\nStructural signals remain positive but reduced (VC $\\rho{=}0.277$ on SciERC, SJ $\\rho{=}0.304$ on CoNLL). LP-weighted construction partially compensates on SciERC ($+1.5$\\,pp, 41.4\\% vs.\\ 39.9\\% greedy) but not on CoNLL ($-0.37$\\,pp), where limited headroom (5.3~pp) leaves little room for aggregation.\n\n\\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot.}\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\columnwidth]{figures/fig_scaling_curve.pdf}\n\\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\\rho$. Separate lines for fine-tuned vs.\\ zero-shot.}\n\\caption{\\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\\theta{=}2/N$ (${\\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\\theta$ stable within $[0.15, 0.35]$; Appendix~\\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\\,pp, CoNLL $-0.92$\\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\\,pp; \\S\\ref{sec:scaling}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. Best in \\textbf{bold}.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & LP & $.646{\\pm}.002$ & $\\mathbf{.656{\\pm}.003}$ & $+1.02{\\pm}0.49$\\,pp & .004 \\\\\n       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\n         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP-weighted construction improves over greedy on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$; Table~\\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\\approx}$8\\% (SciERC) and 11\\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\\ref{app:n_scaling}).\n\n\\paragraph{LP-alignment gating (preliminary diagnostic).}\nConstruction and LP selection are complementary: construction dominates on SciERC ($+1.02$\\,pp vs.\\ LP $+0.04{\\pm}0.48$\\,pp, n.s.; $\\rho{\\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\\ $+1.39$\\,pp; $\\rho{\\approx}0.5$--$0.7$).\nWe estimate within-instance $\\rho(\\text{LP}, \\text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\\rho_{\\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\\approx}0$ (n.s.).\nThe protocol performs three-way routing: (1)~$\\rho_{\\text{adj}} \\geq \\tau{=}0.3$: apply LP selection; (2)~$\\rho_{\\text{adj}} < \\tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.\nThis routes Few-NERD to LP selection ($+1.39$\\,pp); SciERC, CoNLL, and WNUT-17 fall below $\\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\\,pp) for protection against negative outcomes (CoNLL $-0.39$\\,pp, WNUT-17 n.s.).\nRouting is stable across $\\tau{\\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: at 80\\% coverage, filtering low-confidence instances yields $+5$--$8$\\,pp F1 (AUPRC 0.70--0.92; Table~\\ref{tab:cross_selection}).\n\n\\phantomsection\\label{sec:selection_results}\n",
    "structuredPatch": [
      {
        "oldStart": 101,
        "oldLines": 7,
        "newStart": 101,
        "newLines": 7,
        "lines": [
          " \\paragraph{Qualitative factors governing selection effectiveness.}",
          " Three factors qualitatively shape LP selection gains: (1)~\\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\\%, CoNLL 48.4\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\\approx}2$\\,pp vs.\\ SciERC 13.1\\,pp); (3)~\\textit{LP-quality alignment}, measured as within-instance $\\rho(\\text{LP}, \\text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).",
          " These factors are consistent with the observed pattern (Table~\\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\\pm}0.48$\\,pp, 3-seed; Table~\\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\\% of instances yield F1${=}0$.",
          "-Yet QE remains effective on WNUT-17 (VC $\\rho{=}0.730$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.",
          "+Yet QE remains effective on WNUT-17 (VC $\\rho{=}0.724$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.",
          " This characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).",
          " ",
          " %% ============================================================"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_01G8dEiiSkN31AX7dqjzqfxK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "52\\% zero F1",
  "new_string": "51\\% zero F1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "c56b9fd4-c004-4396-a143-fc8903e9ab22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmZsoPXXVfqL87zHwYJVZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3087,
      "cache_read_input_tokens": 23801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3087
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T13:54:17.712Z_

<details><summary>↩ Tool result · `toolu_01G8dEiiSkN31AX7dqjzqfxK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "db5b06b2-b80b-43dd-ade2-0010130f97cf",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "oldString": "52\\% zero F1",
    "newString": "51\\% zero F1",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 52\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\n\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models ($\\varepsilon$-free; $\\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\\ref{app:epsilon_robustness}).\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nThis collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nFour of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\\S\\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.\nThe empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.\nLP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\nCross-instance $\\rho$ (Table~\\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}. $^\\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.775 \\pm 0.001$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & n/a$^\\dagger$ \\\\\nVC           & $0.623 \\pm 0.004$ & n/a$^\\dagger$ \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho$ (seed 42); line with error bars: $\\Delta$F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\nInstance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best.\n\n\\paragraph{LP: the sole per-sample signal also fails.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n\n\\paragraph{Qualitative factors governing selection effectiveness.}\nThree factors qualitatively shape LP selection gains: (1)~\\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\\%, CoNLL 48.4\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\\approx}2$\\,pp vs.\\ SciERC 13.1\\,pp); (3)~\\textit{LP-quality alignment}, measured as within-instance $\\rho(\\text{LP}, \\text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nThese factors are consistent with the observed pattern (Table~\\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\\pm}0.48$\\,pp, 3-seed; Table~\\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\\% of instances yield F1${=}0$.\nYet QE remains effective on WNUT-17 (VC $\\rho{=}0.724$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.\nThis characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}\n\\label{tab:fewnerd}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrccccr@{}}\n\\toprule\nDataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n\\midrule\nWNUT-17 & 1{,}287 & .452 & 67.9\\% & $-$.446 & $-$0.45\\,pp & .72 \\\\\nCoNLL & 2{,}756 & .908 & 48.4\\% & .302 & $-$0.85\\,pp & 1.0 \\\\\nSciERC & 529 & .644 & 17.8\\% & .205 & $+$0.61\\,pp & .193 \\\\\nFew-NERD & 32{,}565 & .748 & 13.8\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\\ref{tab:cross_selection}).\nTraining convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\\% and halves LP gains (Appendix~\\ref{app:epoch_confound}).\n\n\\paragraph{Degeneracy alone does not predict LP selection direction.}\nAcross 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\nCross-dataset prediction requires LP signal quality: Few-NERD ($\\rho{\\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\\rho{\\approx}0.26$) does not (Appendix~\\ref{app:conditional_decomp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nStructural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\\ref{app:n_scaling}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nWith Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\nDegeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nLoRA rank${=}8$ (vs.\\ 32) lowers degeneracy to 7.2\\% but LP remains below greedy ($\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$); temperature manipulation ($T{=}1.2$; \\S\\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.\n\n\\paragraph{Supervised signal combination and hidden probes.}\nSupervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\\ref{app:supervised_combination}).\nHidden state probes improve correlation ($+37$\\% on SciERC) but not selection (gap closure $-5.1$\\%; Appendix~\\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.\n\n%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nWe evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp).}\n\\label{tab:scale_comparison}\n\\begin{tabular}{@{}llcccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\\\\n       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$2 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nZero-shot 72B produces lower greedy F1 but larger oracle headroom (Table~\\ref{tab:scale_comparison}). LP $\\rho$ drops from $0.205$ to $0.081$ on SciERC and from $0.302$ to near zero on CoNLL; LP selection fails in both datasets (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), confirming that the gap is a structural property of the task rather than a fine-tuning artifact.\nStructural signals remain positive but reduced (VC $\\rho{=}0.277$ on SciERC, SJ $\\rho{=}0.304$ on CoNLL). LP-weighted construction partially compensates on SciERC ($+1.5$\\,pp, 41.4\\% vs.\\ 39.9\\% greedy) but not on CoNLL ($-0.37$\\,pp), where limited headroom (5.3~pp) leaves little room for aggregation.\n\n\\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot.}\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\columnwidth]{figures/fig_scaling_curve.pdf}\n\\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\\rho$. Separate lines for fine-tuned vs.\\ zero-shot.}\n\\caption{\\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\\theta{=}2/N$ (${\\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\\theta$ stable within $[0.15, 0.35]$; Appendix~\\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\\,pp, CoNLL $-0.92$\\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\\,pp; \\S\\ref{sec:scaling}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. Best in \\textbf{bold}.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & LP & $.646{\\pm}.002$ & $\\mathbf{.656{\\pm}.003}$ & $+1.02{\\pm}0.49$\\,pp & .004 \\\\\n       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\n         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP-weighted construction improves over greedy on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$; Table~\\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\\approx}$8\\% (SciERC) and 11\\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\\ref{app:n_scaling}).\n\n\\paragraph{LP-alignment gating (preliminary diagnostic).}\nConstruction and LP selection are complementary: construction dominates on SciERC ($+1.02$\\,pp vs.\\ LP $+0.04{\\pm}0.48$\\,pp, n.s.; $\\rho{\\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\\ $+1.39$\\,pp; $\\rho{\\approx}0.5$--$0.7$).\nWe estimate within-instance $\\rho(\\text{LP}, \\text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\\rho_{\\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\\approx}0$ (n.s.).\nThe protocol performs three-way routing: (1)~$\\rho_{\\text{adj}} \\geq \\tau{=}0.3$: apply LP selection; (2)~$\\rho_{\\text{adj}} < \\tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.\nThis routes Few-NERD to LP selection ($+1.39$\\,pp); SciERC, CoNLL, and WNUT-17 fall below $\\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\\,pp) for protection against negative outcomes (CoNLL $-0.39$\\,pp, WNUT-17 n.s.).\nRouting is stable across $\\tau{\\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: at 80\\% coverage, filtering low-confidence instances yields $+5$--$8$\\,pp F1 (AUPRC 0.70--0.92; Table~\\ref{tab:cross_selection}).\n\n\\phantomsection\\label{sec:selection_results}\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " \\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.",
          " \\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).",
          " \\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.",
          "-\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 52\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.",
          "+\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.",
          " ",
          " \\paragraph{Models and sampling.}",
          " \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound})."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 18_

Verifying consistency across all files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "63df972c-39be-4c71-b847-da89f40d68ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZy9WFD7CfnjiLbeTK44nm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 26888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 619
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Grep · `toolu_017quT7i7d5nezzNRQHopmEp`</summary>

```json
{
  "pattern": "0\\.730",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "9cbc7c94-102c-4be3-9592-c1268daac644",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZy9WFD7CfnjiLbeTK44nm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 26888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 619
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T13:54:21.735Z_

<details><summary>↩ Tool result · `toolu_017quT7i7d5nezzNRQHopmEp`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "02265d19-cb1c-430d-8387-fb25c9f91bdb",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Grep · `toolu_01XEDkM31z1HRmdkhbxHEhGL`</summary>

```json
{
  "pattern": "0\\.724",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "edb137d9-29ca-432a-a8f6-501134a8adb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZy9WFD7CfnjiLbeTK44nm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 26888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 619
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T13:54:22.616Z_

<details><summary>↩ Tool result · `toolu_01XEDkM31z1HRmdkhbxHEhGL`</summary>

```text
docs/paper/sections/experiments.tex:48:At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
docs/paper/sections/experiments.tex:104:Yet QE remains effective on WNUT-17 (VC $\rho{=}0.724$; Table~\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.
docs/paper/sections/appendix.tex:226:VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\rho{=}0.350$ is the highest among all signals on the non-zero subset, full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "f0aaf4ae-8e06-465e-9c6b-8f6a0992e6ba",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/experiments.tex:48:At the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\ndocs/paper/sections/experiments.tex:104:Yet QE remains effective on WNUT-17 (VC $\\rho{=}0.724$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.\ndocs/paper/sections/appendix.tex:226:VC's high full-set $\\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\\rho{=}0.350$ is the highest among all signals on the non-zero subset, full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Grep · `toolu_018ohpzjEXy1XDRR91hDsA3P`</summary>

```json
{
  "pattern": "52\\\\?%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "996b85a5-199c-4feb-a0bd-3538700a6bc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZy9WFD7CfnjiLbeTK44nm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 26888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 619
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T13:54:23.058Z_

<details><summary>↩ Tool result · `toolu_018ohpzjEXy1XDRR91hDsA3P`</summary>

```text
docs/paper/sections/experiments.tex:49:This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.
docs/paper/sections/appendix.tex:321:WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "009c990b-9495-4304-9862-bd19664e2388",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/experiments.tex:49:This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\ndocs/paper/sections/appendix.tex:321:WNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Grep · `toolu_01RDy9E4yTqviVdnqXaUejNU`</summary>

```json
{
  "pattern": "51\\\\?%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "41b38f49-bfdf-4df7-b0ac-efe6be60b5bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZy9WFD7CfnjiLbeTK44nm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 26888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 619
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T13:54:23.865Z_

<details><summary>↩ Tool result · `toolu_01RDy9E4yTqviVdnqXaUejNU`</summary>

```text
docs/paper/sections/experiments.tex:12:\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
docs/paper/sections/experiments.tex:103:[Omitted long matching line]
docs/paper/sections/limitations.tex:3:Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "72ee6db8-002b-4fdd-aef8-76b153b9e986",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/experiments.tex:12:\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\ndocs/paper/sections/experiments.tex:103:[Omitted long matching line]\ndocs/paper/sections/limitations.tex:3:Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\\% F1${=}0$), this precondition fails and construction cannot improve over greedy.",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Fix 1 is clean — 0.730 no longer appears, all 3 instances of 0.724 are consistent.

Fix 2 has an issue: experiments.tex:49 and appendix.tex:321 still say "52%". The task said to unify to 51%, but I only changed line 12. Let me check:

- experiments.tex:12 — now says 51% ✓
- experiments.tex:49 — still says 52% ✗


- experiments.tex:103 — says 51% ✓
- limitations.tex:3 — says 51% ✓
- appendix.tex:321 — says 52% ✗

I need to fix those two remaining instances in experiments.tex:49 and appendix.tex:321.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "ee5a4998-d06e-4cf6-a122-f6ca7d5de0ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014f8NN3sSn85EpfxH7P2CXD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1221,
      "cache_read_input_tokens": 27507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1221
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 28_

Two more occurrences of "52%" need fixing — experiments.tex:49 and appendix.tex:321.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "954f995b-22ab-4a2d-b5b5-a77c10912602",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014f8NN3sSn85EpfxH7P2CXD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1221,
      "cache_read_input_tokens": 27507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1221
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01DfJmW2ADbDAsJrhXHLHeBs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 47,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "68fb93ef-e6d4-4672-b120-aee9170d9eac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014f8NN3sSn85EpfxH7P2CXD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1221,
      "cache_read_input_tokens": 27507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1221
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T13:54:30.910Z_

<details><summary>↩ Tool result · `toolu_01DfJmW2ADbDAsJrhXHLHeBs`</summary>

```text
47	On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
48	At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
49	This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.
50	
51	%% ============================================================
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "032676c4-d1b3-4249-a0a7-1ed6fdf17ed0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "On CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nThis collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\n\n%% ============================================================",
      "numLines": 5,
      "startLine": 47,
      "totalLines": 259
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_014NoH7Qj8rpjfpjRbGbVW2P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 319,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "ff940440-38c8-46af-8451-236a78112a45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014f8NN3sSn85EpfxH7P2CXD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1221,
      "cache_read_input_tokens": 27507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1221
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T13:54:31.558Z_

<details><summary>↩ Tool result · `toolu_014NoH7Qj8rpjfpjRbGbVW2P`</summary>

```text
319	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
320	On CoNLL, diversity collapses: 59\% (Qwen) to 89\% (LLaMA) of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect where single-sample F1 already exceeds 0.90.
321	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
322	
323	\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "0a22186c-9305-4872-a1e0-1040731ae674",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "LLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 59\\% (Qwen) to 89\\% (LLaMA) of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect where single-sample F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]",
      "numLines": 5,
      "startLine": 319,
      "totalLines": 1572
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01Ma4SMgLDNb64j7drn3TJ83`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "52\\% of instances yield zero F1 across all samples",
  "new_string": "51\\% of instances yield zero F1 across all samples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "de8c7fad-78d9-4537-9ee4-ff10dbf38ccd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiaTWmZ4FbE8TaR8JTzWrG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 876,
      "cache_read_input_tokens": 28728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 876
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T13:54:35.029Z_

<details><summary>↩ Tool result · `toolu_01Ma4SMgLDNb64j7drn3TJ83`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "aa12b767-a743-470f-9154-f8c67ef8d665",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "oldString": "52\\% of instances yield zero F1 across all samples",
    "newString": "51\\% of instances yield zero F1 across all samples",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\n\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models ($\\varepsilon$-free; $\\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\\ref{app:epsilon_robustness}).\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nThis collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nFour of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\\S\\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.\nThe empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.\nLP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\nCross-instance $\\rho$ (Table~\\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}. $^\\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.775 \\pm 0.001$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & n/a$^\\dagger$ \\\\\nVC           & $0.623 \\pm 0.004$ & n/a$^\\dagger$ \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho$ (seed 42); line with error bars: $\\Delta$F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\nInstance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best.\n\n\\paragraph{LP: the sole per-sample signal also fails.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n\n\\paragraph{Qualitative factors governing selection effectiveness.}\nThree factors qualitatively shape LP selection gains: (1)~\\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\\%, CoNLL 48.4\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\\approx}2$\\,pp vs.\\ SciERC 13.1\\,pp); (3)~\\textit{LP-quality alignment}, measured as within-instance $\\rho(\\text{LP}, \\text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nThese factors are consistent with the observed pattern (Table~\\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\\pm}0.48$\\,pp, 3-seed; Table~\\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\\% of instances yield F1${=}0$.\nYet QE remains effective on WNUT-17 (VC $\\rho{=}0.724$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.\nThis characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}\n\\label{tab:fewnerd}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrccccr@{}}\n\\toprule\nDataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n\\midrule\nWNUT-17 & 1{,}287 & .452 & 67.9\\% & $-$.446 & $-$0.45\\,pp & .72 \\\\\nCoNLL & 2{,}756 & .908 & 48.4\\% & .302 & $-$0.85\\,pp & 1.0 \\\\\nSciERC & 529 & .644 & 17.8\\% & .205 & $+$0.61\\,pp & .193 \\\\\nFew-NERD & 32{,}565 & .748 & 13.8\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\\ref{tab:cross_selection}).\nTraining convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\\% and halves LP gains (Appendix~\\ref{app:epoch_confound}).\n\n\\paragraph{Degeneracy alone does not predict LP selection direction.}\nAcross 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\nCross-dataset prediction requires LP signal quality: Few-NERD ($\\rho{\\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\\rho{\\approx}0.26$) does not (Appendix~\\ref{app:conditional_decomp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nStructural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\\ref{app:n_scaling}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nWith Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\nDegeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nLoRA rank${=}8$ (vs.\\ 32) lowers degeneracy to 7.2\\% but LP remains below greedy ($\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$); temperature manipulation ($T{=}1.2$; \\S\\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.\n\n\\paragraph{Supervised signal combination and hidden probes.}\nSupervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\\ref{app:supervised_combination}).\nHidden state probes improve correlation ($+37$\\% on SciERC) but not selection (gap closure $-5.1$\\%; Appendix~\\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.\n\n%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nWe evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp).}\n\\label{tab:scale_comparison}\n\\begin{tabular}{@{}llcccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\\\\n       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$2 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nZero-shot 72B produces lower greedy F1 but larger oracle headroom (Table~\\ref{tab:scale_comparison}). LP $\\rho$ drops from $0.205$ to $0.081$ on SciERC and from $0.302$ to near zero on CoNLL; LP selection fails in both datasets (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), confirming that the gap is a structural property of the task rather than a fine-tuning artifact.\nStructural signals remain positive but reduced (VC $\\rho{=}0.277$ on SciERC, SJ $\\rho{=}0.304$ on CoNLL). LP-weighted construction partially compensates on SciERC ($+1.5$\\,pp, 41.4\\% vs.\\ 39.9\\% greedy) but not on CoNLL ($-0.37$\\,pp), where limited headroom (5.3~pp) leaves little room for aggregation.\n\n\\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot.}\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\columnwidth]{figures/fig_scaling_curve.pdf}\n\\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\\rho$. Separate lines for fine-tuned vs.\\ zero-shot.}\n\\caption{\\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\\theta{=}2/N$ (${\\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\\theta$ stable within $[0.15, 0.35]$; Appendix~\\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\\,pp, CoNLL $-0.92$\\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\\,pp; \\S\\ref{sec:scaling}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. Best in \\textbf{bold}.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & LP & $.646{\\pm}.002$ & $\\mathbf{.656{\\pm}.003}$ & $+1.02{\\pm}0.49$\\,pp & .004 \\\\\n       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\n         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP-weighted construction improves over greedy on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$; Table~\\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\\approx}$8\\% (SciERC) and 11\\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\\ref{app:n_scaling}).\n\n\\paragraph{LP-alignment gating (preliminary diagnostic).}\nConstruction and LP selection are complementary: construction dominates on SciERC ($+1.02$\\,pp vs.\\ LP $+0.04{\\pm}0.48$\\,pp, n.s.; $\\rho{\\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\\ $+1.39$\\,pp; $\\rho{\\approx}0.5$--$0.7$).\nWe estimate within-instance $\\rho(\\text{LP}, \\text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\\rho_{\\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\\approx}0$ (n.s.).\nThe protocol performs three-way routing: (1)~$\\rho_{\\text{adj}} \\geq \\tau{=}0.3$: apply LP selection; (2)~$\\rho_{\\text{adj}} < \\tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.\nThis routes Few-NERD to LP selection ($+1.39$\\,pp); SciERC, CoNLL, and WNUT-17 fall below $\\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\\,pp) for protection against negative outcomes (CoNLL $-0.39$\\,pp, WNUT-17 n.s.).\nRouting is stable across $\\tau{\\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: at 80\\% coverage, filtering low-confidence instances yields $+5$--$8$\\,pp F1 (AUPRC 0.70--0.92; Table~\\ref{tab:cross_selection}).\n\n\\phantomsection\\label{sec:selection_results}\n",
    "structuredPatch": [
      {
        "oldStart": 46,
        "oldLines": 7,
        "newStart": 46,
        "newLines": 7,
        "lines": [
          " On SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).",
          " On CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).",
          " At the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).",
          "-This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.",
          "+This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 51\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.",
          " ",
          " %% ============================================================",
          " \\subsection{The Correlation-Selection Gap}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_01GunidH6zoTtqB5jSK6F9zc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "driven by the 52\\% zero-F1 rate",
  "new_string": "driven by the 51\\% zero-F1 rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "c57da192-9b1d-49b9-ac71-6264858366d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiaTWmZ4FbE8TaR8JTzWrG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 876,
      "cache_read_input_tokens": 28728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 876
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T13:54:35.813Z_

<details><summary>↩ Tool result · `toolu_01GunidH6zoTtqB5jSK6F9zc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "f5a21bc0-a799-403b-90a0-1d802f2fc6cb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "oldString": "driven by the 52\\% zero-F1 rate",
    "newString": "driven by the 51\\% zero-F1 rate",
    "originalFile": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\nWe exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\\%; SciERC: 22/551, 4.0\\%).\nFor these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\\rho$ depending on signal behavior at the boundary.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\quad LP & $T{=}0.7$ & 0.249 & --- \\\\\n\\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.474{\\pm}0.009$ & --- \\\\\n\\quad FK &  & $0.467{\\pm}0.009$ & --- \\\\\n\\quad EM &  & $0.473{\\pm}0.010$ & --- \\\\\n\\quad VC &  & $0.470{\\pm}0.006$ & --- \\\\\n\\quad LP &  & $0.311{\\pm}0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.\nFK NER $\\rho$ drops by 0.022, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nLP exhibits the largest temperature effect on NER ($\\rho{=}0.249$ at $T{=}0.7$ vs.\\ $0.205$ at $T{=}1.0$, $\\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.\nAcross all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent (LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$), though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, $\\Delta\\rho{=}0.069$; permutation $p{=}0.06$, borderline).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$),\\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.474{\\pm}0.009$ vs.\\ LP $0.311{\\pm}0.003$, $\\Delta{=}{+}0.163$).\n\n\\paragraph{FK independence: instance-level permutation test.}\\label{app:fk_independence}\n\nTo verify that Fleiss' $\\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.\nFor each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}\n\\label{tab:fk_independence}\n\\begin{tabular}{lrcccc}\n\\toprule\nConfig & $n$ & FK mean & 95\\% CI & $t$ & Split-half $r$ \\\\\n\\midrule\nSciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\\\\nCoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\\\\nCoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fk_independence} reports the results.\nAll configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), FK captures genuine inter-sample agreement rather than chance label co-occurrence.\nSplit-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.\nThe higher FK means on CoNLL ($0.720$--$0.927$) vs.\\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives. This is a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$): longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$, all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$; the two selection rules are equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{SJ normalizer robustness.}\nEquation~\\ref{eq:sj} uses $\\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \\cup g_j|$.\nTable~\\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\\Delta\\rho|{<}0.01$ in every case, the choice between max and union normalization does not affect conclusions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\n\\label{tab:sj_normalizer}\n\\begin{tabular}{@{}ll ccc@{}}\n\\toprule\nDataset & Model & $\\rho$(max) & $\\rho$(union) & $\\Delta\\rho$ \\\\\n\\midrule\nCoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\\\\nCoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\\\\nCoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\\\\nSciERC & Qwen3-8B & .360 & .365 & $-$.005 \\\\\nSciERC & Qwen3-4B & .422 & .423 & $-$.001 \\\\\nSciERC & LLaMA-8B & .363 & .372 & $-$.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\\Delta\\rho{=}{-}0.005$, $p{=}0.53$; preliminary).\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations: SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$). This holds despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set, where the model demonstrably produces varied outputs, exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\\rho$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho$ reflects binary success prediction; conditional $\\rho$ measures quality gradation. LP's conditional $\\rho$ is highest despite negative full-set $\\rho$.}\n\\label{tab:wnut}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & .913 & .038 & .487 \\\\\nFK      & .125 & .555 & .169 & .002 \\\\\nSJ      & .089 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\nThe full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.\nVC's high full-set $\\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\\rho{=}0.350$ is the highest among all signals on the non-zero subset, full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to five additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn LLaMA FewNERD ($n{=}32{,}565$, 3-seed mean), LP is the only signal with positive selection ($+0.36$~pp), confirming LP as the most robust selection signal across model families (Qwen FewNERD: $+1.39$~pp, Table~\\ref{tab:fewnerd}). All structural signals degrade selection (VC $-2.39$~pp, SJ $-0.52$~pp), consistent with the Qwen pattern. LLaMA FewNERD degeneracy ($23.4{\\pm}4.7$\\%, 3 seeds) is higher than Qwen ($12.7$\\%), illustrating the capability-diversity tension: LLaMA achieves stronger greedy F1 ($0.784$ vs.\\ $0.748$, $+3.6$~pp) but at the cost of higher degeneracy ($+10.7$~pp) and reduced oracle headroom ($10.0$ vs.\\ $12.4$~pp).\nOn CoNLL, 48--87\\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\n\\addlinespace\nLLaMA/FewNERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \\textbf{.788} & .760 \\\\\n\\addlinespace\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .957 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals use $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, each additional comparison yields diminishing information.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound (more draws raise the probability of a high-quality candidate), but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\nWhile quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\nVC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).\nThese gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\nThis reinforces the primary finding: even under the most favorable conditions (high baseline performance, more candidates, and aggregated multi-seed evidence), signal-based selection recovers only a fraction of the oracle headroom available.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, the structural advantage reported in \\S\\ref{sec:qe_results} is robust.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant; these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\nAt $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.\nOn SciERC NER ($n{=}529$), SJ--FK ($\\Delta\\rho{=}0.147$--$0.160$, all $p{\\leq}0.002$) and VC--FK ($\\Delta\\rho{=}0.138$--$0.188$, all $p{\\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\\Delta\\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).\nOn CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\\Delta\\rho{=}0.071$ ($p{<}0.001$), SJ $\\Delta\\rho{=}0.056$ ($p{<}0.001$), VC $\\Delta\\rho{=}0.022$ ($p{=}0.040$).\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n% fig_selection_gap promoted to main text (\\S\\ref{sec:selection_gap})\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 59\\% (Qwen) to 89\\% (LLaMA) of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect where single-sample F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding single-sample\\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \\S\\ref{sec:evaluation}); the diversity quantification in Table~\\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, consistent with the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP, the only per-sample signal, achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{Instance degeneracy statistics.}\nTable~\\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}\n\\label{tab:degeneracy}\n\\begin{tabular}{lccc}\n\\toprule\n& \\shortstack{SciERC 8B\\\\($N{=}8$)} & \\shortstack{SciERC 4B\\\\($N{=}8$)} & \\shortstack{CoNLL 8B\\\\($N{=}16$)} \\\\\n\\midrule\nConstant F1 & 17.8\\% & 10.4\\% & 48.4\\% \\\\\nConstant utility & 13\\% & 7.0\\% & 49\\% \\\\\nOracle gap closed (non-deg.) & 23\\% & 25.2\\% & 41\\% \\\\\nWithin-inst.\\ SJ $\\rho$ (median) & 0.524 & 0.550 & 0.994 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{TOST equivalence testing.}\\label{app:tost}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\\delta$.\nThe $\\delta$ values are contextualized against oracle headroom (12--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThese proportions use the same test data that defines the headroom, introducing circularity: $\\delta$ is anchored to the very quantity it contextualizes.\nWe address this below with externally anchored equivalence margins.\nThe breakpoint $\\delta^*$, the minimum equivalence margin at which each signal passes TOST, ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ single-sample).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{External equivalence margins.}\nThe oracle-headroom anchors above introduce circularity: $\\delta$ is calibrated against the very quantity it contextualizes.\nTo resolve this, we supplement with three externally grounded margins:\n(1) $\\delta_{\\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), which represents measurement noise;\n(2) $\\delta_{\\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \\cite{ratinov2009design};\n(3) $\\delta_{\\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \\cite{bergkirkpatrick2012empirical}.\n\nResults under these external anchors diverge sharply by configuration.\nOn LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\\Delta|{\\leq}0.1$~pp) and tight CIs at this sample size.\nOn Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, which exceeds even $\\delta_{\\mathrm{literature}}$.\nOn SciERC NER ($n{=}529$), only SJ passes at $\\delta_{\\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.\nThese external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.\n\n\\paragraph{Multiple comparison considerations.}\\label{app:multiple_comparisons}\nOur primary selection analysis involves ${\\sim}$20 comparisons (5 signals $\\times$ 3--4 configurations).\nSince all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hochberg correction can only make these results more conservative, strengthening the ``no signal beats greedy'' conclusion.\nThe sole positive finding, the non-tied LP subset ($+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion}), survives Bonferroni correction over the 5 signal comparisons ($p_{\\mathrm{adj}}{=}0.020 < 0.05$). However, the $\\varepsilon{=}0.05$ threshold is selected post-hoc from a 7-point sweep (Appendix~\\ref{app:epsilon_robustness}); joint correction across thresholds and signals yields $p_{\\mathrm{adj}}{=}0.14$, so this finding is exploratory.\nFor quality estimation signal rankings, differences between the top signals (e.g., VC vs.\\ SJ on SciERC) should be interpreted as descriptive rather than as statistically confirmed orderings, given the limited power of 3-seed comparisons.\n\n\\paragraph{When would consistency-based selection work?}\\label{app:when_selection_works}\nOur negative results are specific to fine-tuned models with constrained decoding on structured IE. Several conditions outside our experimental scope could restore selection headroom.\n(a)~Models with poor calibration or in-context learning setups (without fine-tuning) produce more diverse outputs, widening the gap between candidates that consistency signals can exploit.\n(b)~Closed-source APIs where log-probabilities are unavailable make consistency signals the only viable selection mechanism; our structural signals (SJ, VC, FK, EM) provide quality estimation ($\\rho$ up to 0.45) even without model-internal access.\n(c)~Ensemble or mixture-of-experts settings generate structurally diverse candidates by design, reducing instance degeneracy below the levels observed in our single-model sampling.\n(d)~Tasks where the model exhibits systematic overconfidence (e.g., hallucination-prone generation) may benefit from consensus filtering, as disagreement among samples would carry more discriminative signal than in our well-calibrated fine-tuned regime.\n\n\\section{Supervised and Model-Internal Signal Analysis}\\label{app:supervised_combination}\n\n\\subsection{Supervised Signal Combination}\n\nSupervised classifiers (logistic regression, MLP, random forest) trained on all five signals (5-fold CV, 3-seed mean, SciERC, $N{=}16$, $+17.9$~pp headroom) all perform at or below greedy (F1${=}0.644$; LR: $-0.4$~pp; MLP: $-1.6$~pp; RF: $-3.1$~pp).\nAdding pairwise interaction features does not help (AUROC 0.634 vs.\\ 0.638).\nTo test whether richer representations could close the gap, we train a DeBERTa-v3-base verifier that encodes input-output pairs and predicts per-sample F1.\nDeBERTa achieves $\\rho{=}0.329{\\pm}0.087$ (5-fold CV, 3 seeds). Despite moderate quality prediction, selection utility is poor: on SciERC, DeBERTa closes $-26.5{\\pm}26.5$\\% of the oracle gap (13 of 15 runs negative; vs.\\ LP's $+4.2{\\pm}10.7$\\%); on Few-NERD, DeBERTa recovers only $+3.5$\\% (single 80/20 split; vs.\\ LP's $+16.3$\\%).\nCross-dataset transfer fails entirely ($-27$\\% to $-72$\\% gap closure).\nNeither handcrafted signal combinations nor learned text representations close the selection gap; only model-internal log-probability provides meaningful selection signal, consistent with an information asymmetry between the generating model and external observers.\n\n\\subsection{Hidden State Probes}\\label{app:hidden_probe}\n\nThe preceding negative results suggest the bottleneck is model-internal rather than a feature engineering problem.\nWe test this directly by training probes on the generating model's hidden representations.\n\n\\paragraph{Setup.}\nFor each of $N{=}8$ samples per instance, we extract the mean-pooled final-layer hidden state ($d{=}4096$) from the generating Qwen3-8B model and train a linear probe and a two-layer MLP (hidden dim${=}256$) to predict per-sample F1 (5-fold CV, 3 seeds).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hidden state probes vs.\\ LP for sample selection (5-fold CV ${\\times}$ 3 seeds). $\\rho$: Spearman correlation with per-sample F1. Sel.\\ F1: selection F1. Gap\\%: oracle gap closure. SciERC greedy${=}0.644$, oracle${=}0.775$.}\n\\label{tab:hidden_probe}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l ccc cc@{}}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{Few-NERD}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\nMethod & $\\rho$ & Sel.\\ F1 & Gap\\% & $\\rho$ & Gap\\% \\\\\n\\midrule\nLP & .283 & $\\mathbf{.650}$ & $+$4.8 & .606 & 12.3 \\\\\nHidden Linear & $.179{\\pm}.019$ & $.613{\\pm}.002$ & $-$23.4 & \\multicolumn{2}{c}{---} \\\\\nHidden MLP & $\\mathbf{.388{\\pm}.013}$ & $.637{\\pm}.003$ & $-$5.1 & $\\mathbf{.629{\\pm}.007}$ & 11.7 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Cross-dataset asymmetry.}\nOn SciERC, the MLP probe achieves higher quality correlation than LP ($\\rho{=}0.388$ vs.\\ $0.283$, $+37$\\%); hidden states encode information beyond what LP captures.\nYet higher correlation does not yield better selection: MLP selection F1 ($0.637$) falls below LP's ($0.650$), with gap closure turning negative ($-5.1$\\% vs.\\ $+4.8$\\%; Table~\\ref{tab:hidden_probe}).\nThe linear probe performs worse still ($\\rho{=}0.179$, gap closure $-23.4$\\%).\nOn Few-NERD, the MLP provides no increment over LP (gap closure $11.7$\\% vs.\\ $12.3$\\%).\nA learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\\% vs.\\ $55.8$\\%); LP's bottleneck is not token aggregation.\nThe correlation-selection gap extends to model-internal representations: in the high-capability regime (greedy F1${=}0.644$), inter-sample F1 differences are small enough that improved ranking provides no marginal selection value, consistent with the capability-diversity tension (\\S\\ref{sec:discussion}).\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .579${\\pm}$.008 & .600${\\pm}$.016 & .659${\\pm}$.016 & .677${\\pm}$.011 & .631${\\pm}$.013 \\\\\nLLaMA & .565${\\pm}$.008 & .593${\\pm}$.006 & .632${\\pm}$.012 & .673${\\pm}$.009 & .606${\\pm}$.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{dong2024xgrammar, willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Thinking Token Impact Analysis}\\label{app:thinking_token}\n\nQwen3-8B's SciERC checkpoint was trained with empty \\texttt{&lt;think>&lt;/think>} blocks prepended to each response (\\S\\ref{sec:setup}).\nWe quantify the potential impact on LP scores through three complementary arguments.\n\n\\paragraph{LP shift magnitude.}\nEmpty thinking tokens (mean 4.5 per sample) constitute 2.1\\% of tokens on SciERC.\nThe estimated LP shift is 0.001 nats per token (2.68\\% of the median within-instance LP range of 0.041 nats).\nBecause all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\\%$ of instances.\n\n\\paragraph{Constant prefix cancellation.}\nAll $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.\nAny LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \\textit{rankings} unchanged.\n\n\\paragraph{CoNLL control group.}\nCoNLL and WNUT-17 checkpoints were trained without thinking tokens (\\texttt{enable\\_thinking=False}).\nIf thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.\nInstead, CoNLL shows \\textit{higher} tied fractions at both temperatures (86.8\\% at $T{=}1.0$, 95.8\\% at $T{=}0.7$) than SciERC (60.3\\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats; we use $\\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.\nAt this cutpoint, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\\varepsilon$, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}); compression is a pervasive regime rather than a bimodal split.\nThis compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\\%$ (vs.\\ seed${=}42$: $0.041$ nats, $60.3\\%$).\nSeed~456 uses a different subtask flag (joint vs.\\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\\ 8.20 nats; Mann--Whitney $p{=}0.55$); the subtask change does not affect compression.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold; SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_lp_range_cdf}\n\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n\\label{fig:lp_range_cdf}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nAs a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\\% of instances achieve $p{<}0.05$ significance, and $\\rho(\\text{LP range}, \\text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability. LP carries information, but compression limits its exploitation.\nA free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\n\n\\paragraph{$\\varepsilon$ sensitivity sweep (post-hoc exploratory).}\nTable~\\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.\nThe tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.\n$\\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\\varepsilon{\\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\\leq}36$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\\%'' = fraction with within-instance LP range ${<}\\varepsilon$. $\\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\\varepsilon{=}0.05$ yields the strongest statistical separation.}\n\\label{tab:epsilon_sweep}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\varepsilon$ & Tied\\% & Non-tied $n$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n0.01 & 1.1\\% & 523 & $+$0.58 & .21 \\\\\n0.02 & 13.6\\% & 457 & $+$0.83 & .15 \\\\\n0.03 & 31.8\\% & 361 & $+$1.31 & .079 \\\\\n\\textbf{0.05} & \\textbf{60.3\\%} & \\textbf{210} & \\textbf{$+$2.86} & \\textbf{.004} \\\\\n0.10 & 83.9\\% & 85 & $+$3.69 & .034 \\\\\n0.15 & 93.2\\% & 36 & $+$4.15 & .11 \\\\\n0.20 & 96.4\\% & 19 & $+$4.59 & .13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\varepsilon$ robustness of selection F1.}\\label{app:epsilon_robustness}\nThe preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\\varepsilon$ to define MBR-style proximity in selection.\nTable~\\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\\varepsilon \\in [0, 0.2]$ for all signals and configurations.\nAt $\\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.\nSpearman $\\rho$, the primary quality estimation metric throughout, is a continuous rank correlation that does not depend on any discretization threshold; the $\\varepsilon$ parameter affects only the selection analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Maximum selection F1 variation (pp) across $\\varepsilon \\in [0, 0.2]$. At $\\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}\n\\label{tab:epsilon_robustness}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & Qwen & LLaMA & Qwen & LLaMA \\\\\n\\midrule\nSJ & 0.92 & 1.45 & 0.99 & 0.18 \\\\\nFK & 1.03 & 0.93 & 0.60 & 0.15 \\\\\nVC & 2.33 & 0.53 & 0.72 & 0.18 \\\\\nEM & 0.00 & 0.00 & 0.00 & 0.00 \\\\\nLP & 3.65 & 2.58 & 3.00 & 0.31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset analysis.}\nTable~\\ref{tab:nontied_main} presents the non-tied subset analysis referenced in \\S\\ref{sec:discussion}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\\varepsilon{=}0.05$. Within-instance $\\rho$ and selection gain both concentrate in the non-tied subset. Full $\\varepsilon$ sweep in Table~\\ref{tab:epsilon_sweep}.}\n\\label{tab:nontied_main}\n\\begin{tabular}{lccc}\n\\toprule\nSubset & $n$ & $\\rho$(LP,F1) & LP $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nTied (range ${<}0.05$) & 319 & 0.08 & ${\\approx}0$ \\\\\nNon-tied (range ${\\geq}0.05$) & 210 & 0.39 & $+$2.9~pp ($p{=}0.004$) \\\\\n\\midrule\nAll instances & 529 & 0.248 & $+$0.2~pp ($p{=}0.29$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Within-instance LP-quality alignment.}\\label{app:within_instance_rho}\n\nTable~\\ref{tab:within_rho} reports median within-instance $\\rho(\\text{LP}, \\text{F1})$ across datasets, computed over non-degenerate instances (those with ${\\geq}2$ distinct F1 values across $N{=}8$ samples).\nFew-NERD exhibits substantially stronger alignment ($\\rho{=}0.667$) than SciERC ($\\rho{=}0.262$), directly explaining why LP selection succeeds only on Few-NERD.\nCoNLL alignment is moderate ($\\rho{\\approx}0.51$), but the valid-instance fraction is low (41\\% for Qwen, 11\\% for LLaMA) because degeneracy eliminates most headroom before alignment can operate.\nLP-quality alignment is the primary predictor of selection direction; degeneracy constrains headroom but does not independently predict whether LP selection gains materialize (\\S\\ref{sec:discussion}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\\text{valid}}$: ${\\geq}2$ distinct F1 values).}\n\\label{tab:within_rho}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nDataset & Model & Med.\\ $\\rho$ & $n_{\\text{valid}}$ / $n_{\\text{total}}$ & Valid\\% \\\\\n\\midrule\nSciERC & Qwen3-8B & 0.262 & 435 / 529 & 82\\% \\\\\nFew-NERD & Qwen3-8B & 0.667 & 28{,}055 / 32{,}565 & 86\\% \\\\\nCoNLL & Qwen3-8B & 0.506 & 1{,}124 / 2{,}756 & 41\\% \\\\\nCoNLL & LLaMA-3.1-8B & 0.512 & 298 / 2{,}756 & 11\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Consistency-Stratified Selection Analysis}\\label{app:vc_quartile}\n\nTable~\\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\\Delta$ (gain over single-sample) for LP and SJ.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Selection $\\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}\n\\label{tab:vc_quartile}\n\\begin{tabular}{lcccc}\n\\toprule\nQuartile & Mean VC & LP $\\Delta$ & SJ $\\Delta$ & Oracle (pp) \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{NER}} \\\\\nQ1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\\\\nQ2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\\\\nQ3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\\\\nQ4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$^\\dagger$RE}} \\\\\nQ1 (low) & --- & $-$3.56 & --- & --- \\\\\nQ4 (high) & --- & $+$4.01 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe NER pattern reveals two complementary failure modes rather than a monotonic relationship between consistency and selection gain:\n\\begin{itemize}\n\\item \\textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp. Samples have already converged, leaving little room for any signal to improve selection.\n\\item \\textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, and LP rankings produce inconsistent $\\Delta$ signs across quartiles.\n\\end{itemize}\n\nOn $^\\dagger$RE, the pattern differs: Q4 LP achieves $+4.01$~pp; LP may recover selection ability when high consistency coincides with structured output diversity. This is a single-dataset observation and should be interpreted cautiously.\n\nOn CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), and $\\Delta{=}0$ universally; this ceiling effect is even more extreme than SciERC Q4.\n\n\\section{Exploratory Extension to Relation Extraction}\\label{app:re_extension}\n\nWe extend the NER evaluation to relation extraction (RE) on SciERC as an exploratory single-benchmark analysis.\nRE produces sets of (head, relation, tail) triples with partial overlap; 40\\% of RE instances receive zero F1, and entity span errors account for 55.5\\% of RE false negatives, a prerequisite failure that consistency signals cannot detect (\\S\\ref{app:additional}).\nAll RE results use Qwen3-8B unless noted; single-seed ($\\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.\n\n\\paragraph{Quality estimation.}\nRE quality estimation is reported in Table~\\ref{tab:multiseed} (3-seed means).\nThe signal ranking differs from NER: VC leads ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM, a reversal reflecting RE's higher sensitivity to per-sample scoring.\nRE miscalibration is more severe than NER (ECE 0.109--0.339; Figure~\\ref{fig:reliability}).\n\n\\paragraph{Selection.}\nTable~\\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.\nAt $N{=}16$ (Qwen3-4B, Table~\\ref{tab:re_n16_selection}), LP is the sole positive signal ($\\Delta{=}{+}0.7$~pp, $p{=}0.058$), consistent with LP being the strongest RE selection signal across scales.\n\n\\paragraph{Scale ablation.}\nAt 4B scale (Qwen3-4B, $N{=}8$, $\\text{seed}{=}42$), RE quality estimation shows FK $\\rho{=}0.359$ and LP $\\rho{=}0.351$, both above their 8B counterparts (FK 0.275, LP 0.266), while SJ declines ($0.267$ vs.\\ $0.250$).\nSelection remains below single-sample on RE ($\\Delta$ up to $-3.4$~pp) despite 17.1~pp of oracle headroom.\n\n\\paragraph{Free-form decoding.}\nRE LP selection consistently reverses direction under free-form decoding ($+1.8{\\pm}0.1$~pp across 4 seeds vs.\\ $-0.9$~pp under constrained decoding at 8B; \\S\\ref{app:freeform_ablation}); constrained decoding's fixed template likely obscures LP signal in RE (\\S\\ref{app:mbr_discussion}).\n\n\\subsection{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform single-sample on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{RE $N{=}16$ Selection Analysis}\\label{app:re_n16_selection}\n\nTable~\\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.\nAll four consistency signals underperform single-sample, with EM showing the largest deficit ($\\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).\nLP is the only positive signal ($\\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).\nEven the most favorable seed captures only ${\\sim}9\\%$ of the 17.1~pp oracle headroom.\nThis cross-task consistency (LP as the only viable selection signal on both NER and RE) reinforces the persistent limitation of instance-level signals for candidate ranking across tested regimes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$, $n{=}551$). Fisher combined $p$ vs.\\ greedy. LP is the only signal with positive $\\Delta$. $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:re_n16_selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & F1 & $\\Delta$ (pp) & $p$(Fisher) \\\\\n\\midrule\nOracle & $.463{\\pm}.006$ & $+$17.1 & --- \\\\\n\\midrule\nLP & $\\mathbf{.299}{\\pm}.007$ & $+$0.7 & .058 \\\\\nVC & $.284{\\pm}.002$ & $-$0.8 & .973 \\\\\nFK & $.283{\\pm}.005$ & $-$0.9 & .985 \\\\\nSJ & $.281{\\pm}.005$ & $-$1.0 & .993 \\\\\nEM & $.277{\\pm}.007$ & $-$1.5 & .999 \\\\\n\\midrule\nGreedy & $.291{\\pm}.000$ & --- & --- \\\\\nRandom & $.262{\\pm}.001$ & $-$2.9 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{MBR Decoding and Task-Specific Interactions}\\label{app:mbr_discussion}\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy, the core of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Task-specific decoding interactions.}\nThe free-form ablation reveals divergent behavior across tasks.\nOn RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nThis ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.\nThe non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472: 87 instances newly gain LP discrimination while others lose it, and the newly non-tied subset shows a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible. Score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\\ $-0.68$~pp constrained.\nThe constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\\pm}0.12$~pp).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}\n\\toprule\nTask & Method & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{NER}\n  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\\\\n  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\\\\n  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\\\\n\\midrule\n\\multirow{3}{*}{RE}\n  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\\\\n  & LP-selected   & 0.2845 & 0.3050 & \\textbf{$+$0.0205} \\\\\n  & Selection gap & $-$0.0068 & $+$0.0169 & \\textbf{$+$0.0237} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel C: QE Signal Quality (Spearman $\\rho$)}}\n\\vspace{2pt}\n\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{NER ($n{=}529$)} & \\multicolumn{3}{c}{RE ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & Constr. & Free & $\\Delta$ & Constr. & Free & $\\Delta$ \\\\\n\\midrule\nSJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\\\\nFK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\\\\nLP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\\\\nEM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\\\\nVC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel D: Parse Rate (Free-form)}}\n\\vspace{2pt}\n\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal samples          & 4408 \\\\\nParse rate             & 99.95\\% \\\\\nInstances 8/8 valid    & 549\\,/\\,551 (99.6\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\n\\end{table*}\n\n\\paragraph{CoNLL NER free-form results.}\nExtending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\\pm}0.007$ across seeds, higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\\% tied fraction under constrained decoding.\nFree-form decoding reduces the tied fraction modestly, yet selection remains below single-sample: LP-selected F1${=}0.896$ vs.\\ single-sample $0.904$ ($\\Delta{=}{-}0.77$~pp).\nQuality estimation under free-form decoding yields SJ $\\rho{=}0.461$, EM $\\rho{=}0.471$, LP $\\rho{=}0.326$, comparable to constrained results (Table~\\ref{tab:quality_estimation}).\nThe failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (5.0~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.\n\n\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\n\nWe analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n\n\\paragraph{Pairwise overlap.}\nLP selection failures (instances where LP-selected F1 $<$ single-sample F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46); failures are partially systematic (driven by instance complexity) but not fully deterministic.\nThe 3-way intersection contains 34 instances (27.9\\% of any-seed failures), which constitutes a stable failure core.\n\n\\paragraph{Instance complexity drives failure.}\nTable~\\ref{tab:stable_failures} stratifies instances by failure stability.\nStable failures (all 3 seeds) involve more gold relations (2.12 vs.\\ 1.62 for never-fail instances) and higher single-sample F1 (0.688 vs.\\ 0.429); LP mis-selects on instances where the model already performs well, precisely the instances where selection would be most valuable.\nFailure rate increases monotonically with gold relation count: 4.3\\% at 1 relation, 20.7\\% at 3 relations, 26.2\\% at 6 relations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}\n\\label{tab:stable_failures}\n\\begin{tabular}{lcccc}\n\\toprule\nGroup & $n$ & Gold rels & Greedy F1 & LP $\\Delta$F1 \\\\\n\\midrule\nStable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\\\\nFail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\\\\nFail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\\\\nNever fail & 429 & 1.62 & 0.429 & $+$0.041 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Flip instances.}\nOnly 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\nThese instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.\n\n\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\n\nTables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\n\\label{tab:n-scaling}\n\\small\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{NER} $\\rho$} & \\multicolumn{3}{c}{\\textbf{RE} $\\rho$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ \\\\\n\\midrule\nSJ & 0.3641 & 0.4105 & \\textbf{+0.0464} & 0.2485 & 0.2758 & \\textbf{+0.0273} \\\\\nFK & 0.2536 & 0.2833 & \\textbf{+0.0297} & 0.2903 & 0.2964 & \\textbf{+0.0061} \\\\\nVC & 0.3861 & 0.4092 & \\textbf{+0.0231} & 0.3088 & 0.3738 & \\textbf{+0.0650} \\\\\nLP & 0.2167 & 0.2393 & \\textbf{+0.0226} & 0.2970 & 0.3100 & \\textbf{+0.0130} \\\\\nEM & 0.3071 & 0.3395 & \\textbf{+0.0324} & 0.1353 & 0.1506 & \\textbf{+0.0153} \\\\\n\\midrule\nMean & 0.3055 & 0.3364 & \\textbf{+0.0308} & 0.2560 & 0.2813 & \\textbf{+0.0253} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\n\\label{tab:ranking-stability}\n\\small\n\\begin{tabular}{ll cc l}\n\\toprule\nModel & Task & $N$ & Kendall's $W$ & Consensus ranking \\\\\n\\midrule\nQwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\nQwen  & NER & 16 & 0.956 & SJ $\\approx$ VC $>$ EM $>$ FK $>$ LP \\\\\nQwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nQwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nLLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\n\\label{tab:sigma-comparison}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{NER} $\\sigma_\\rho$} & \\multicolumn{2}{c}{\\textbf{RE} $\\sigma_\\rho$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $N\\!=\\!8$ & $N\\!=\\!16$ \\\\\n\\midrule\nSJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\\\\nFK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\\\\nVC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\\\\nEM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\\\\nLP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\\\\n\\midrule\nMean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSignal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.\nDoubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER); additional samples stabilize structural signals more than LP.\n\n\\paragraph{$N$-scaling: selection headroom vs.\\ selection gain.}\nTable~\\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.\nOracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+20.0$~pp at $N{=}32$).\nLP selection improves monotonically with $N$ ($+0.39$~pp at $N{=}8$ to $+0.95$~pp at $N{=}32$), but even at $N{=}32$, where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}20$~pp, the best signal captures less than 5\\% of the available improvement.\nDegeneracy drops monotonically (43\\% at $N{=}2$ to 4\\% at $N{=}32$), yet reduced degeneracy does not unlock selection, consistent with the LoRA-rank ablation finding (\\S\\ref{sec:robustness_main}).\nVC selection degrades with increasing $N$ ($-2.66$~pp at $N{=}2$ to $-4.35$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\\_025).\\protect\\footnotemark\\ ``Best $\\Delta$'': highest selection gain across all 5 signals. Per-signal $\\Delta$ in pp vs.~greedy.}\n\\label{tab:n_scaling_selection}\n\\begin{tabular}{ccccccccc}\n\\toprule\n$N$ & Degen.\\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\\Delta$ \\\\\n\\midrule\n2 & 42.7\\% & $+$4.4 & $-$0.89 & $-$2.72 & $-$2.72 & $-$2.72 & $-$2.66 & $-$0.89 \\\\\n4 & 21.0\\% & $+$10.2 & $+$0.03 & $-$0.31 & $-$0.40 & $-$0.74 & $-$2.16 & $+$0.03 \\\\\n8 & 11.0\\% & $+$14.5 & $+$0.39 & $+$0.20 & $+$0.15 & $-$0.77 & $-$2.87 & $+$0.39 \\\\\n16 & 7.4\\% & $+$17.7 & $+$0.78 & $+$0.24 & $-$0.02 & $-$0.06 & $-$3.95 & $+$0.78 \\\\\n32 & 4.0\\% & $+$20.0 & $+$0.95 & $+$0.35 & $+$0.65 & $+$0.22 & $-$4.35 & $+$0.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\\footnotetext{$N$-scaling analysis uses gold-filtered evaluation ($n{=}529$, greedy F1${=}0.640$). Values differ slightly from Table~\\ref{tab:selection} (0.645) and Table~\\ref{tab:fewnerd} (0.644) due to seed and aggregation differences; relative trends are consistent.}\n\n\\paragraph{Bootstrap significance at $N{=}32$.}\nTable~\\ref{tab:bootstrap_n32} reports bootstrap confidence intervals and $p$-values for selection at $N{=}32$ ($B{=}10{,}000$, $n{=}529$).\nNo signal achieves significant improvement over greedy at $\\alpha{=}0.05$ (LP: $p{=}0.091$; FK: $p{=}0.101$), while VC is significantly \\textit{worse} ($-4.36$~pp, $p{=}1.0$).\nHowever, all signals except VC significantly outperform random selection ($p{<}0.001$, permutation test); the signals carry meaningful quality information yet fail to translate it into reliable selection gains.\nThe oracle gap ($+20.0$~pp, $p{<}0.001$) confirms substantial unrealized headroom.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap significance test at $N{=}32$ (SciERC NER, Qwen3-8B, $T{=}1.0$, $B{=}10{,}000$, $n{=}529$ gold-non-empty instances; 22 instances with no gold entities are excluded as they contribute zero selection differential). $\\Delta$: selection gain vs.\\ greedy. CI: 95\\% bootstrap percentile interval. $p_{\\text{greedy}}$: one-sided $p$-value vs.\\ greedy; $p_{\\text{rand}}$: permutation test vs.\\ random selection.}\n\\label{tab:bootstrap_n32}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\Delta$ (pp) & 95\\% CI & $p_{\\text{greedy}}$ & $p_{\\text{rand}}$ \\\\\n\\midrule\nLP & $+$0.95 & [$-$0.41, $+$2.34] & 0.091 & ${<}$0.001 \\\\\nFK & $+$0.66 & [$-$0.36, $+$1.67] & 0.101 & ${<}$0.001 \\\\\nSJ & $+$0.36 & [$-$0.66, $+$1.38] & 0.244 & ${<}$0.001 \\\\\nEM & $+$0.22 & [$-$0.99, $+$1.44] & 0.355 & ${<}$0.001 \\\\\nVC & $-$4.36 & [$-$6.26, $-$2.37] & 1.000 & 0.741 \\\\\n\\midrule\nOracle & $+$20.00 & [$+$17.98, $+$22.10] & ${<}$0.001 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Temperature Ablation}\\label{app:t_ablation}\n\nTable~\\ref{tab:t_ablation} reports the effect of sampling temperature on QE signals, oracle headroom, and output quality across four temperatures on SciERC NER.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\\rho$ across four temperatures. $\\kappa$: Fleiss' $\\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}\n\\label{tab:t_ablation}\n\\begin{tabular}{ccccccc}\n\\toprule\n$T$ & Oracle gap (pp) & SJ $\\rho$ & LP $\\rho$ & $\\kappa$ & Sample F1 \\\\\n\\midrule\n0.5 & $+$9.1 & 0.297 & 0.218 & 0.577 & 0.636 \\\\\n0.8 & $+$12.5 & 0.359 & 0.253 & 0.451 & 0.622 \\\\\n1.0 & $+$13.0 & 0.360 & 0.205 & ${\\approx}$0.39 & ${\\approx}$0.612 \\\\\n1.2 & $+$14.6 & 0.377 & 0.196 & 0.356 & 0.594 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOracle headroom increases monotonically with temperature ($+9.1$~pp at $T{=}0.5$ to $+14.6$~pp at $T{=}1.2$), confirming that higher temperature consistently expands the oracle ceiling under constrained structured decoding.\nStructural QE signals improve with temperature: SJ $\\rho$ rises from $0.297$ ($T{=}0.5$) to $0.377$ ($T{=}1.2$), consistent with more diverse outputs providing richer pairwise evidence.\nLP $\\rho$ peaks at $T{=}0.8$ ($0.253$) then degrades to $0.196$ at $T{=}1.2$.\nThis divergence confirms that LP compression is model-intrinsic: higher temperature increases between-instance LP variance (benefiting structural signals) but does not resolve within-instance compression, degrading LP's discriminative power.\nInter-sample agreement ($\\kappa$) decreases monotonically ($0.577$ to $0.356$); higher temperature generates more diverse outputs. Mean sample F1 also decreases ($0.636$ to $0.594$), consistent with the quality--diversity trade-off.\nThe $T{=}0.7$ and $T{=}1.0$ comparison in Table~\\ref{tab:robustness} is consistent with the trends reported here.\n\n\\paragraph{Temperature controls degeneracy and LP spread.}\nTable~\\ref{tab:t_degeneracy} reports instance degeneracy (constant F1, gold-filtered) and median within-instance LP range across four temperatures on SciERC.\nBoth quantities are strictly monotonic in $T$: degeneracy falls from 41.4\\% ($T{=}0.5$) to 14.9\\% ($T{=}1.2$), while LP range increases from 0.015 to 0.058 nats.\nTemperature thus provides a direct lever for practitioners to shift the degeneracy regime.\nHowever, even at $T{=}1.2$ where degeneracy (14.9\\%) approaches Few-NERD levels (${\\sim}$14\\%), within-instance $\\rho(\\text{LP}, \\text{F1})$ remains at 0.225, far below Few-NERD's ${\\sim}$0.5.\nThis confirms that temperature controls degeneracy but cannot improve LP-quality alignment, which is largely determined by task structure and remains relatively stable across generation configurations (\\S\\ref{app:epoch_confound}). LP-quality alignment, not degeneracy, is the primary predictor of LP selection direction (\\S\\ref{sec:discussion}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Temperature sensitivity of degeneracy and LP spread (SciERC NER, Qwen3-8B, $N{=}8$). Degeneracy: constant-F1, gold-filtered. LP range: median within-instance range.}\n\\label{tab:t_degeneracy}\n\\begin{tabular}{ccccc}\n\\toprule\n$T$ & Degen.\\% & LP range (nats) & Fleiss' $\\kappa$ & SJ mean \\\\\n\\midrule\n0.5 & 41.4 & 0.015 & 0.572 & 0.830 \\\\\n0.8 & 23.8 & 0.031 & 0.471 & 0.752 \\\\\n1.0 & 17.8 & 0.042 & 0.405 & 0.700 \\\\\n1.2 & 14.9 & 0.058 & 0.352 & 0.647 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\n\nTo test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\n\\label{tab:ood}\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{SciERC$\\to$CoNLL}} & \\multicolumn{3}{c}{\\textbf{CoNLL$\\to$SciERC}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $\\rho$ & In-dom. & $\\Delta$ & $\\rho$ & In-dom. & $\\Delta$ \\\\\n\\midrule\nVC & .469\\textsuperscript{***} & .379 & +.090 & +.105\\textsuperscript{*} & .379 & $-$.274 \\\\\nSJ & .378\\textsuperscript{***} & .360 & +.018 & $-$.186\\textsuperscript{***} & .360 & $-$.546 \\\\\nEM & .300\\textsuperscript{***} & .295 & +.005 & $-$.202\\textsuperscript{***} & .295 & $-$.497 \\\\\nFK & .285\\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\\\\nLP & .246\\textsuperscript{***} & .205 & +.041 & $-$.152\\textsuperscript{***} & .205 & $-$.357 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Wider-to-narrower schema transfer.}\nWhen the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.379$, $\\Delta{=}{+}0.090$), SJ $\\rho{=}0.378$ (in-domain $0.360$, $\\Delta{=}{+}0.018$), and FK $\\rho{=}0.285$ (in-domain $0.267$, $\\Delta{=}{+}0.018$).\nThe wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.\n\n\\paragraph{Narrower-to-wider schema transfer (excluded).}\nThe reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.\nThe CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (single-sample NER F1${=}0.009$, RE F1${=}0.001$).\nUnder this regime, most signals flip to negative or near-zero correlations (Table~\\ref{tab:ood}); only VC retains weak positive correlation ($\\rho{=}0.105$, $p{=}0.016$).\nThese negative correlations reflect the model systematically generating confident but incorrect outputs, a capability failure analogous to WNUT-17 (\\S\\ref{sec:qe_results}) and not evidence against signal utility.\n\n\\paragraph{Asymmetry interpretation.}\nThe directional asymmetry is driven by schema coverage: wider$\\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.\nThis extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.\n\n\\section{Verbalized Confidence}\\label{app:verbalized_confidence}\n\nWe evaluate verbalized confidence (VerbConf) as a second per-sample signal following \\citet{lin2022teaching} and \\citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.\nTable~\\ref{tab:verbconf} reports quality estimation and selection results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Verbalized confidence (VerbConf) vs.\\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}\n\\label{tab:verbconf}\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{CoNLL NER}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nMetric & VerbConf & LP & VerbConf & LP \\\\\n\\midrule\n$\\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\\\\nAUROC & 0.681 & 0.578 & 0.747 & 0.753 \\\\\nSelection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\\\\n$\\Delta$ vs.\\ greedy & $-$2.45\\,pp & $+$0.2\\,pp & $-$1.93\\,pp & $-$0.77\\,pp \\\\\n\\midrule\nMean score & 8.58\\,/\\,10 & --- & 9.24\\,/\\,10 & --- \\\\\nParse fail rate & 0.26\\% & --- & 0\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Severe overconfidence.}\nVerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (single-sample F1${=}0.645$) and 9.24/10 on CoNLL (single-sample F1${=}0.904$), with most scores concentrated in the 8--10 range.\nThis compression is more severe than LP (which spans a 0.041-nat median range); score compression is a general property of model self-assessment, not an artifact of log-probability computation.\n\n\\paragraph{QE--selection decoupling.}\nVerbConf achieves higher $\\rho$ than LP on both datasets (SciERC: 0.297 vs.\\ 0.205; CoNLL: 0.337 vs.\\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\\ 0.578; CoNLL: 0.747 vs.\\ 0.753), yet yields the worst selection among all signals ($\\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).\nThis dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.\nThe AUROC--$\\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\\rho$ at 0.337) reflects differing sensitivity to binary vs.\\ ordinal discrimination.\n\n\\section{LLaMA-3.2-3B Scale Ablation}\\label{app:llama3b}\n\nTo extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\\ref{tab:llama3b}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}\n\\label{tab:llama3b}\n\\begin{tabular}{l cc cc}\n\\toprule\nSignal & $\\rho$ & AUROC & Sel.\\ F1 & $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nVC & \\textbf{.460} & .743 & 0.611 & $-$1.54\\,pp \\\\\nSJ & .375 & .738 & \\textbf{0.633} & $+$0.61\\,pp \\\\\nEM & .334 & \\textbf{.776} & --- & --- \\\\\nFK & .268 & .671 & 0.630 & $+$0.28\\,pp \\\\\nLP & .266 & .633 & 0.628 & $+$0.12\\,pp \\\\\n\\midrule\nGreedy & --- & --- & 0.627 & --- \\\\\nOracle & --- & --- & 0.763 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\\ref{tab:quality_estimation}); ranking stability holds across two model families spanning 3B--8B.\nAUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), consistent with the $\\rho$--AUROC dissociation noted in the main text.\nDespite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC, the strongest QE signal, yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.\n\n\\section{Few-NERD Full Results}\\label{app:fewnerd}\n\nTable~\\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).\nAfter gold-filtering (removing instances with no gold entities), the evaluation set contains $n{=}32{,}565$ instances across 8 coarse entity types; 11.9\\% receive zero F1 under greedy decoding.\nInstance degeneracy is 13.8\\% (vs.\\ 17.8\\% on SciERC, 48.4\\% on CoNLL).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\\ $\\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\\% confidence interval.}\n\\label{tab:fewnerd_full}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ & Sample AUROC & Sel.\\ $\\Delta$ & 95\\% CI \\\\\n\\midrule\nLP & .220 & .578 & $\\mathbf{+1.39}$\\,pp & [+1.18, +1.53] \\\\\nVC & .386 & --- & $-$1.79\\,pp & --- \\\\\nFK & .313 & --- & $-$2.26\\,pp & --- \\\\\nSJ & .300 & --- & $-$2.14\\,pp & --- \\\\\nEM & .287 & --- & $-$3.85\\,pp & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{Greedy: 0.748 \\quad Oracle: 0.872} & \\multicolumn{2}{l}{Headroom: 12.4\\,pp} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Key observations.}\n(1)~All five signals achieve positive QE ($\\rho$ 0.22--0.39); quality estimation works on Few-NERD. VC leads ($\\rho{=}0.39$), followed by FK ($0.31$), SJ ($0.30$), EM ($0.29$), LP ($0.22$); the ranking matches SciERC where structural signals also outperform LP for quality estimation.\n(2)~LP is the only signal achieving significant positive selection ($+1.39$~pp, $p{<}0.001$, CI excludes zero). The sample-level AUROC of 0.578 confirms LP provides per-sample discriminability beyond instance-level quality prediction.\n(3)~Despite positive $\\rho$, all structural signals degrade selection ($-1.79$ to $-3.85$~pp), further confirming that the correlation-selection gap is not an artifact of weak QE.\n(4)~Low degeneracy (13.8\\%) combined with strong LP-quality alignment ($\\rho{\\approx}0.5$--$0.7$) enables LP selection: candidates differ in F1 more often, and LP can rank them effectively. This contrasts with SciERC (17.8\\% degeneracy but weak alignment $\\rho{\\approx}0.24$, LP $+0.61$~pp) and CoNLL (48.4\\%, LP $-0.85$~pp).\n\n\\section{Per-Entity-Type LP Selection Analysis}\\label{app:per_type_lp}\n\nTable~\\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.\nThe degeneracy-gating mechanism holds at entity-type granularity: 7 of 8 types show positive LP selection gains, and the sole negative type (Art, $-0.17$~pp) has the highest degeneracy (19.8\\%).\nThe correlation between per-type degeneracy and oracle headroom is strong and significant (Spearman $\\rho{=}{-}0.881$, $p{=}0.004$; exact permutation $p{=}0.005$); degeneracy directly constrains the headroom available for selection.\nUnder a conservative $\\text{df}{=}4$ adjustment for within-type dependence, the correlation remains significant ($p{=}0.033$).\nEntity types show near-zero intra-class correlation (ICC $= -0.004$), supporting the independence assumption underlying per-type analysis.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\\Delta$; Art (highest degeneracy) is the sole exception.}\n\\label{tab:per_type_lp}\n\\begin{tabular}{lrrrrrrr}\n\\toprule\nEntity Type & $n$ & Degen.\\% & Greedy & LP Sel & $\\Delta$ (pp) & LP $\\rho$ & Headroom \\\\\n\\midrule\nEvent & 1{,}306 & 6.0 & .655 & .662 & $+$0.65 & .457 & 16.1\\,pp \\\\\nOther & 3{,}433 & 6.6 & .637 & .685 & $\\mathbf{+4.73}$ & .491 & 19.4\\,pp \\\\\nOrganization & 6{,}647 & 6.7 & .720 & .732 & $+$1.21 & .509 & 13.3\\,pp \\\\\nBuilding & 1{,}587 & 7.2 & .702 & .705 & $+$0.23 & .478 & 14.9\\,pp \\\\\nProduct & 2{,}276 & 8.2 & .656 & .677 & $+$2.01 & .483 & 15.8\\,pp \\\\\nLocation & 8{,}023 & 11.4 & .793 & .798 & $+$0.53 & .520 & 10.3\\,pp \\\\\nPerson & 8{,}016 & 13.4 & .822 & .835 & $+$1.25 & .544 & 9.2\\,pp \\\\\nArt & 1{,}277 & 19.8 & .756 & .754 & $-$0.17 & .451 & 9.2\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{CoNLL-2003 per-type LP selection (Qwen3-8B, $N{=}16$, $T{=}1.0$). All types exceed 20\\% degeneracy and show negative LP selection, consistent with the dataset's ceiling-regime performance (F1 $>$ 90\\%).}\n\\label{tab:per_type_lp_conll}\n\\begin{tabular}{lrrr}\n\\toprule\nEntity Type & Degen.\\% & LP $\\Delta$ (pp) \\\\\n\\midrule\nMISC & 23.2 & $-$2.19 \\\\\nPER & 42.6 & $-$1.08 \\\\\nLOC & 47.5 & $-$0.62 \\\\\nORG & 54.3 & $-$0.55 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SciERC per-type LP selection (Qwen3-8B, $N{=}8$, $T{=}1.0$). Within-dataset, degeneracy alone does not predict LP effectiveness (Spearman $\\rho{=}0.14$, $p{=}0.79$); additional type-specific factors likely modulate selection at this granularity.}\n\\label{tab:per_type_lp_scierc}\n\\begin{tabular}{lrrr}\n\\toprule\nEntity Type & Degen.\\% & LP $\\Delta$ (pp) \\\\\n\\midrule\nTask & 10.1 & $+$2.58 \\\\\nGeneric & 10.0 & $+$2.07 \\\\\nMaterial & 20.0 & $+$0.91 \\\\\nMetric & 12.5 & $-$0.06 \\\\\nMethod & 16.3 & $-$0.03 \\\\\nOtherScientificTerm & 6.2 & $-$0.57 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe cross-dataset degeneracy gradient (48.4\\% $\\to$ 17.8\\% $\\to$ 13.8\\%) is inversely associated with LP selection effectiveness at the macro level ($n{=}3$ datasets; exploratory).\\footnote{Partial Spearman correlation controlling for entity-type frequency yields $\\rho{=}{-}0.47$ (vs.\\ raw $\\rho{=}{-}0.38$); type frequency does not confound the degeneracy--LP relationship.}\nAt finer per-type granularity, selection depends on the interaction of degeneracy, oracle headroom, and type-specific LP-quality alignment.\nA Kruskal-Wallis test finds no significant per-type heterogeneity in LP selection gains on SciERC ($p{=}0.796$), consistent with the small per-type sample sizes ($n{=}54$--$296$).\nLow degeneracy alone does not ensure selection gains: CoNLL MISC (23\\%, headroom 12.6~pp) and SciERC OtherScientificTerm (6.2\\%, headroom 12.5~pp) both show negative LP selection despite available headroom; LP correlation strength with the type-specific quality function is an additional prerequisite.\n\n\\section{Calibration Baseline}\\label{app:calibration_baseline}\n\nStandard calibration methods are monotonic transforms of log-probability and therefore preserve within-instance sample rankings: Platt scaling \\cite{platt1999probabilistic} fits a logistic regression $\\sigma(a \\cdot \\text{LP} + b)$, and temperature scaling \\cite{guo2017calibration} divides logits by a scalar $\\tau$.\nSince both preserve the argmax, selection F1 is identical to raw LP on all three datasets (Table~\\ref{tab:calibration}).\n\nTo break monotonicity, we fit a multi-feature Platt model (MF-Platt) using LP, token count, and entity count as inputs, trained on a held-out calibration split (20\\% of the test set, 5-fold cross-validation on the remainder).\nMF-Platt can reorder candidates within an instance, yet yields no significant selection improvement: $\\Delta{=}{-}1.1$~pp on SciERC ($p{=}0.72$), $+0.3$~pp on CoNLL ($p{=}0.31$), and $-0.6$~pp on Few-NERD ($p{=}0.83$).\nPlatt scaling substantially improves probability calibration (ECE drops from 0.26--0.39 to 0.01--0.08), but better-calibrated probabilities do not translate to better selection.\nThis parallels the supervised signal combination result (\\S\\ref{sec:robustness_main}): neither stronger aggregation nor additional features can compensate for weak per-sample discriminative signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Calibration baseline results ($N{=}8$, $T{=}1.0$). Platt and TempScale are monotonic transforms of LP that preserve the within-instance argmax (selection F1 $\\equiv$ Raw LP, omitted). MF-Platt uses LP $+$ token count $+$ entity count; $p$: bootstrap test vs.\\ Raw LP.}\n\\label{tab:calibration}\n\\begin{tabular}{l cccc cc}\n\\toprule\n& & \\multicolumn{2}{c}{Selection F1} & & \\multicolumn{2}{c}{ECE} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){6-7}\nDataset & Greedy & Raw LP & MF-Platt ($p$) & & Raw & Platt \\\\\n\\midrule\nSciERC & .644 & .650 & .639 (.72) & & .260 & .048 \\\\\nCoNLL & .909 & .898 & .901 (.31) & & .392 & .012 \\\\\nFew-NERD & .771 & .785 & .778 (.83) & & .262 & .080 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Epoch Confound Analysis}\\label{app:epoch_confound}\n\n\\paragraph{Training convergence modulates degeneracy.}\nTable~\\ref{tab:epoch_confound} compares the 3-epoch model (used throughout the main text) with a 5-epoch variant on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$).\nExtended training increases greedy F1 by $+2.95$~pp (0.748 $\\to$ 0.777) but nearly triples instance degeneracy (11.1\\% $\\to$ 31.3\\%), reducing the fraction of instances with non-degenerate outputs from 85.6\\% to 68.7\\%.\nLP selection gains drop correspondingly ($+1.37$~pp $\\to$ $+0.62$~pp), consistent with the degeneracy-gating mechanism identified in the main text (\\S\\ref{sec:discussion}).\nWithin-instance LP-quality alignment is relatively stable under this convergence shift (mean $\\rho$: $0.524 \\to 0.407$; median $\\rho$: $0.667 \\to 0.615$), consistent with alignment being determined primarily by task structure rather than training duration.\n\nEvaluation loss increases after epoch 3 (0.032 $\\to$ 0.041 at epoch 5), and the best checkpoint by validation loss occurs at step 32{,}000 (approximately epoch 3.9).\nStandard early stopping practice thus naturally selects the low-degeneracy regime where LP selection is most effective.\nThis finding refines the narrative: degeneracy is not a fixed property of datasets but is modulated by the degree of training convergence. Over-trained models compress their output distributions, collapsing diversity even on datasets that support it under well-regularized training.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$). Evaluated on the exp\\_027 5K subsample (gold-filtered $n{=}4{,}351$); main-table results (Table~\\ref{tab:fewnerd}) use the full test set ($n{=}32{,}565$, gold-filtered), yielding slightly different degeneracy (13.8\\% vs.\\ 11.1\\% here). ``Degen.'': constant-F1 instance degeneracy (gold-filtered). ``Valid'': fraction of instances with non-degenerate outputs. ``$\\rho$ mean/med'': within-instance LP-quality correlation. The 3-epoch model corresponds to standard early stopping; the 5-epoch model is a controlled ablation.}\n\\label{tab:epoch_confound}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & 3-epoch & 5-epoch \\\\\n\\midrule\nGreedy F1 & 0.748 & 0.777 \\\\\nInstance degen.\\ (\\%) & 11.1 & 31.3 \\\\\nValid instances & 3{,}723 / 4{,}351 (85.6\\%) & 2{,}988 / 4{,}351 (68.7\\%) \\\\\nLP $\\Delta$ (pp) & $+$1.37 & $+$0.62 \\\\\nWithin-inst.\\ $\\rho$ (mean) & 0.524 & 0.407 \\\\\nWithin-inst.\\ $\\rho$ (median) & 0.667 & 0.615 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{SciERC epoch curve.}\nTable~\\ref{tab:epoch_scierc} extends the analysis to SciERC with a 3-point curve (3, 5, 10 epochs; Qwen3-8B, $N{=}8$, $T{=}1.0$).\nDegeneracy increases monotonically (6.4\\% $\\to$ 17.8\\% $\\to$ 47.8\\%), and within-instance LP-quality correlation degrades in tandem (median $\\rho$: 0.319 $\\to$ 0.262 $\\to$ 0.112; mean $\\rho$: 0.273 $\\to$ 0.179 $\\to$ 0.066), confirming that overtraining erodes both diversity and LP alignment simultaneously.\nThe fraction of instances with positive LP-quality correlation also declines (76.4\\% at 3 epochs $\\to$ 64.1\\% at 5 epochs $\\to$ 54.0\\% at 10 epochs).\nLP selection does not yield significant gains at any training duration ($-1.24$, $+0.64$, $+1.02$~pp; all below the ${\\approx}$1.5~pp MDE), despite oracle headroom ranging from 8.4 to 15.0~pp.\nThe 3-epoch model has higher within-instance alignment ($\\rho{=}0.319$) than the 5-epoch model ($\\rho{=}0.262$), yet LP selection is worse ($-1.24$ vs.\\ $+0.64$~pp): at 6.4\\% degeneracy, more non-degenerate instances enter the candidate pool, but LP ranking precision is too low to exploit them, so the broader pool hurts rather than helps. This illustrates that low degeneracy does not ensure selection gains; LP-quality alignment determines selection direction.\nAt 10 epochs, the model retains competitive greedy F1 (0.649 vs.\\ 0.650 at 3 epochs) yet conditions are unfavorable: 47.8\\% degenerate instances and $\\rho{=}0.112$.\nThe gradient confirms that degeneracy is convergence-driven rather than a fixed dataset property: extended training compresses output distributions, degrading both diversity and within-instance alignment. However, the epoch-to-epoch alignment variation ($\\Delta\\rho_{\\text{median}}{=}0.057$) is small relative to the cross-dataset gap (SciERC ${\\sim}$0.3 vs.\\ Few-NERD ${\\sim}$0.5), consistent with alignment being primarily dataset-intrinsic: training convergence modulates alignment at the margin but cannot shift a dataset into the strong-alignment regime.\nEven at the most favorable epoch (3-epoch, $\\rho{=}0.319$), SciERC alignment remains below the ${\\sim}$0.5 threshold associated with successful LP selection on Few-NERD.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SciERC NER epoch curve (Qwen3-8B, $N{=}8$, $T{=}1.0$). Training duration modulates both instance degeneracy and within-instance LP-quality alignment. ``Degen.'': constant-F1 instance degeneracy (gold-filtered). ``LP $\\Delta$'': LP selection gain over greedy (gold-filtered; none reaches the ${\\approx}$1.5~pp MDE). ``$\\rho$ med'': median within-instance LP-quality correlation. Greedy F1 uses span-based evaluation consistent with Tables 1--3; $\\rho$ and LP $\\Delta$ use text-based matching consistent with Table~\\ref{tab:within_rho}.}\n\\label{tab:epoch_scierc}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 3-epoch & 5-epoch & 10-epoch \\\\\n\\midrule\nGreedy F1 & 0.650 & 0.644 & 0.649 \\\\\nInstance degen.\\ (\\%) & 6.4 & 17.8 & 47.8 \\\\\nLP $\\Delta$ (pp) & $-$1.24 & $+$0.64 & $+$1.02 \\\\\nWithin-inst.\\ $\\rho$ (median) & 0.319 & 0.262 & 0.112 \\\\\nWithin-inst.\\ $\\rho$ (mean) & 0.273 & 0.179 & 0.066 \\\\\n\\% positive $\\rho$ & 76.4 & 64.1 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Limitations.}\nThe Few-NERD epoch analysis covers 2 points (3 vs.\\ 5 epochs); the SciERC curve provides a 3-point gradient showing monotonic degeneracy increase with simultaneous within-instance alignment degradation.\nCoNLL epoch variation remains unverified; high-degeneracy datasets (CoNLL at 59--89\\%) may exhibit a ceiling effect where additional training has limited marginal impact.\nAll Few-NERD results in the main text use the 3-epoch model (standard early stopping); the 5-epoch comparison is a controlled ablation.\nAll SciERC results use the 5-epoch model; the 3- and 10-epoch variants serve as controlled ablations.\n\n\\subsection{Degeneracy-Aware LP Selection}\\label{app:dals}\n\nThe non-tied subset analysis (Table~\\ref{tab:nontied_main}) identifies within-instance LP range (max minus min LP across $N$ samples) as a per-instance degeneracy proxy: instances with near-zero LP range carry no discriminative signal.\nDegeneracy-aware LP selection (DALS) operationalizes this: when LP range exceeds $\\tau{=}0.05$ (the threshold independently motivated by the non-tied analysis; Appendix~\\ref{app:epsilon_robustness}), select the highest-LP sample; otherwise fall back to greedy.\nOn SciERC, DALS yields $+0.71{\\pm}0.48$~pp (3-seed mean; individual seeds: $+0.19$ to $+1.14$~pp); on Few-NERD, $+0.30$~pp ($p{<}0.001$; gain remains positive across $\\tau \\in [0.01, 0.15]$); on CoNLL, where pure LP selection degrades F1 ($-0.85$~pp), DALS shows comparable degradation (Qwen: $-0.87$~pp; LLaMA: neutral).\nDALS improves over pure LP selection when degeneracy is moderate, provides partial damage control when LP selection is harmful, and defaults to greedy when LP range signals no information.\nWhile gains are modest and seed-sensitive, LP range serves as an operationally accessible degeneracy proxy, though the mixed cross-dataset results confirm that degeneracy gating alone cannot ensure positive selection outcomes.\n\n\\paragraph{LOO $\\tau$ sensitivity.}\nLeave-one-out (LOO) cross-validation across datasets reveals that the optimal $\\tau$ spans two orders of magnitude: $\\tau^*{=}0.001$ on Few-NERD, $0.05$ on SciERC, and $0.10$ on CoNLL.\nLOO regret (the gap between oracle and LOO-selected $\\tau$) ranges from 0.51 to 1.21~pp.\nThe best single cross-dataset $\\tau$ ($\\tau{=}0.05$) matches the independently motivated non-tied threshold, but yields dataset-specific suboptimality: even with oracle $\\tau$, CoNLL remains at $-0.31$~pp.\nThis sensitivity reinforces the diagnostic framing of DALS: per-dataset $\\tau$ tuning is required for positive gains, and even optimally tuned DALS cannot overcome weak LP-quality alignment on high-degeneracy datasets.\n\n\\subsection{Conditional Decomposition of LP Selection}\\label{app:conditional_decomp}\n\nTo test whether LP-quality alignment drives selection gains within datasets, we restrict LP selection to the favorable subset: non-degenerate instances whose within-instance LP range exceeds the dataset-specific median (SciERC: 0.040 nats, CoNLL: 0.062, Few-NERD: 0.067).\nTable~\\ref{tab:conditional_decomp} reports results across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LP selection on the favorable subset (non-degenerate instances with LP range above the dataset-specific median) per dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$). CI: bootstrap 95\\% confidence interval.}\n\\label{tab:conditional_decomp}\n\\begin{tabular}{lccc}\n\\toprule\nDataset & LP $\\Delta$ (pp) & 95\\% CI & Interpretation \\\\\n\\midrule\nSciERC & $+$2.47 & [$+$0.30, $+$4.70] & significant positive \\\\\nFew-NERD & $+$0.63 & [$-$0.02, $+$1.30] & marginal positive \\\\\nCoNLL & $-$1.78 & [$-$2.83, $-$0.76] & significant negative \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn SciERC, restricting to the favorable subset recovers a significant LP gain, consistent with LP-quality alignment driving selection within the non-degenerate pool.\nOn Few-NERD, the trend is directionally consistent but the confidence interval crosses zero; the full-dataset result ($+1.39$~pp, $p{<}0.001$) reflects the larger sample size rather than a stronger per-instance effect.\nCoNLL remains negative even on the favorable subset, consistent with the ceiling-regime interpretation: at $>$90\\% greedy F1, residual errors are idiosyncratic and LP cannot rank corrections.\n\n\\subsection{Entity-Token LP Decomposition}\\label{app:entity_token_lp}\n\nFull-sequence LP averages over all output tokens, diluting entity-relevant signal with formatting and schema tokens.\nEntity-token LP restricts the average to tokens within entity text and type spans, yielding $4{\\times}$ higher within-instance variance (median 0.000644 vs.\\ 0.000161).\nTable~\\ref{tab:entity_token_lp} compares the two aggregation strategies on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Full-sequence vs.\\ entity-token LP on SciERC NER (Qwen3-8B, $N{=}8$, $T{=}1.0$). Entity-token LP has higher variance and stronger correlation, yet selection degrades.}\n\\label{tab:entity_token_lp}\n\\begin{tabular}{lcccc}\n\\toprule\nAggregation & Med.\\ var. & $\\rho$ & AUROC & $\\Delta$ (pp) \\\\\n\\midrule\nFull-sequence & 0.000161 & 0.297 & 0.642 & $+$0.35 \\\\\nEntity text+type & 0.000644 & 0.440 & 0.719 & $-$0.73 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite stronger correlation ($+$48\\%) and higher AUROC, entity-token LP produces worse selection, reinforcing that compression operates at the representation level rather than token aggregation: the correlation-selection gap persists even with a more targeted signal.\n\n\\subsection{Entity-Level Majority Voting}\\label{app:entity_merge}\n\nEntity-level majority voting constructs a merged output by including all (text, type) entity tuples that appear in at least $k$ of $N$ samples (with $k = N/2$ as the default majority threshold).\nUnlike best-of-$N$ selection (which picks one complete sample), merge combines evidence across samples at entity granularity.\nWe sweep $k \\in \\{2, 3, \\ldots, 8\\}$ on each dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$) and report the best threshold per dataset.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Entity-level majority voting results (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Greedy'': $T{=}0$ baseline. ``Best merge'': optimal $k$ per dataset from sweep $k \\in \\{2, \\ldots, 8\\}$. ``$\\Delta$'': merge F1 minus greedy. ``Recovery'': $\\Delta$ / (oracle $-$ greedy). Only SciERC shows positive recovery; even with oracle $k$, CoNLL and Few-NERD degrade.}\n\\label{tab:entity_merge}\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & Greedy & Best merge ($k^*$) & $\\Delta$ (pp) & Recovery (\\%) \\\\\n\\midrule\nSciERC & 0.644 & 0.660 ($k{=}3$) & $+$1.57 & $+$11.9 \\\\\nCoNLL & 0.907 & 0.903 ($k{=}3$) & $-$0.38 & $-$9.0 \\\\\nFew-NERD & 0.748 & 0.744 ($k{=}2$) & $-$0.43 & $-$3.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn degenerate subsets (instances where all $N$ samples yield identical F1), merge is uniformly negative across all three datasets, confirming that entity-level aggregation cannot bypass the diversity bottleneck identified in the main text (\\S\\ref{sec:discussion}).\n\n\\subsection{Entity Construction Threshold Sensitivity}\n\\label{app:theta_sweep}\n\nTable~\\ref{tab:theta_sweep} reports entity construction F1 as a function of the confirmation threshold $\\theta$ across three datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$). The default $\\theta{=}2/N{=}0.25$ achieves the best LP-weighted $\\Delta$F1 on Few-NERD and is within 0.04\\,pp of the optimum on SciERC. Performance is stable across $\\theta \\in [0.15, 0.35]$; below 0.15, spurious entities degrade precision, and above 0.40, aggressive filtering removes correct low-frequency entities.\n\n\\begin{table}[h]\n\\caption{Entity construction threshold sensitivity ($N{=}8$, Qwen3-8B, $T{=}1.0$). $\\Delta$: F1 difference vs.\\ greedy in percentage points. Best $\\Delta$ per dataset--weighting pair in \\textbf{bold}.}\n\\label{tab:theta_sweep}\n\\centering\n\\small\n\\begin{tabular}{ll rr rr}\n\\toprule\nDataset & $\\theta$ & LP-w F1 & Unif.\\ F1 & $\\Delta$ LP-w & $\\Delta$ Unif.\\ \\\\\n\\midrule\n\\multirow{8}{*}{SciERC}\n & 0.10 & .620 & .620 & $-$2.37 & $-$2.37 \\\\\n & 0.15 & .659 & .659 & $+$1.54 & $+$1.54 \\\\\n & 0.20 & .659 & .659 & $+$1.54 & $+$1.54 \\\\\n & 0.25 & .661 & .659 & $+$1.67 & $+$1.54 \\\\\n & 0.30 & .661 & .661 & \\textbf{$+$1.71} & \\textbf{$+$1.71} \\\\\n & 0.35 & .661 & .661 & \\textbf{$+$1.71} & \\textbf{$+$1.71} \\\\\n & 0.40 & .653 & .654 & $+$0.94 & $+$0.97 \\\\\n & 0.50 & .649 & .654 & $+$0.46 & $+$0.97 \\\\\n\\midrule\n\\multirow{8}{*}{Few-NERD}\n & 0.10 & .677 & .676 & $-$7.12 & $-$7.15 \\\\\n & 0.15 & .751 & .751 & $+$0.32 & $+$0.32 \\\\\n & 0.20 & .751 & .751 & $+$0.32 & $+$0.32 \\\\\n & 0.25 & .757 & .751 & \\textbf{$+$0.88} & $+$0.32 \\\\\n & 0.30 & .750 & .750 & $+$0.21 & $+$0.21 \\\\\n & 0.35 & .750 & .750 & $+$0.21 & $+$0.21 \\\\\n & 0.40 & .729 & .728 & $-$1.90 & $-$2.01 \\\\\n & 0.50 & .725 & .728 & $-$2.25 & $-$2.01 \\\\\n\\midrule\n\\multirow{8}{*}{CoNLL}\n & 0.10 & .844 & .842 & $-$6.44 & $-$6.56 \\\\\n & 0.15 & .896 & .896 & $-$1.19 & $-$1.19 \\\\\n & 0.20 & .896 & .896 & $-$1.19 & $-$1.19 \\\\\n & 0.25 & .901 & .896 & $-$0.71 & $-$1.19 \\\\\n & 0.30 & .904 & .904 & \\textbf{$-$0.39} & \\textbf{$-$0.39} \\\\\n & 0.35 & .904 & .904 & $-$0.41 & \\textbf{$-$0.39} \\\\\n & 0.40 & .900 & .899 & $-$0.83 & $-$0.94 \\\\\n & 0.50 & .897 & .899 & $-$1.12 & $-$0.94 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 318,
        "oldLines": 7,
        "newStart": 318,
        "newLines": 7,
        "lines": [
          " On SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.",
          " LLaMA shows similar diversity (39\\% unique, F1 std 0.11).",
          " On CoNLL, diversity collapses: 59\\% (Qwen) to 89\\% (LLaMA) of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect where single-sample F1 already exceeds 0.90.",
          "-WNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.",
          "+WNUT-17 shows 55\\% identical outputs, driven by the 51\\% zero-F1 rate.",
          " ",
          " \\begin{table}[t]",
          " \\centering"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 37_

Final verification:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "c16ee441-a936-4b66-ae9a-25dbc60579fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7Br6XjULUUmEBkgM19YsT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 478,
      "cache_read_input_tokens": 29604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 478
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Grep · `toolu_01NVt5J4mxRYnvYgVAaTs4Nu`</summary>

```json
{
  "pattern": "52\\\\%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "947a63bd-6437-497d-bfd6-7a77b7d57f41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7Br6XjULUUmEBkgM19YsT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 478,
      "cache_read_input_tokens": 29604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 478
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T13:54:40.008Z_

<details><summary>↩ Tool result · `toolu_01NVt5J4mxRYnvYgVAaTs4Nu`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "98c4eb07-66c0-4a71-a76a-0daeb9975a43",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Grep · `toolu_013CuJqbbDgJSr8u2k3CCZhU`</summary>

```json
{
  "pattern": "0\\.730",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "b7be2366-8c97-4481-9bac-e821d1bc1bdf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7Br6XjULUUmEBkgM19YsT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 478,
      "cache_read_input_tokens": 29604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 478
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T13:54:40.482Z_

<details><summary>↩ Tool result · `toolu_013CuJqbbDgJSr8u2k3CCZhU`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "f65f61cb-9bae-4e26-bbbc-e8f8437b2928",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 42_

两个修复完成：

1. **VC ρ 打字错误**: `0.730` → `0.724`（experiments.tex:104），全文 3 处 0.724 一致，0.730 不再出现。
2. **zero-F1 率统一**: 4 处 `52%` → `51%`（experiments.tex:12/49/103, limitations.tex:3, appendix.tex:321），全文不再有 `52%`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "uuid": "57f3b55f-944c-403c-9d8b-a5d2295d5030",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4vcnHmXg13i2vtTKyEksm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 298,
      "cache_read_input_tokens": 30082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 298
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 43_

两个修复完成：

1. **VC ρ 打字错误**: `0.730` → `0.724`（experiments.tex:104），全文 3 处 0.724 一致，0.730 不再出现。
2. **zero-F1 率统一**: 4 处 `52%` → `51%`（experiments.tex:12/49/103, limitations.tex:3, appendix.tex:321），全文不再有 `52%`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 40606,
  "duration_api_ms": 43806,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "26898e1a-02c7-4fd5-94e2-f5e98c12adf5",
  "total_cost_usd": 0.26611025,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 18539,
    "cache_read_input_tokens": 178451,
    "output_tokens": 2381,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 18539,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 128,
        "cache_read_input_tokens": 30082,
        "cache_creation_input_tokens": 298,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 298
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1351,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001446,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 2381,
      "cacheReadInputTokens": 178451,
      "cacheCreationInputTokens": 18539,
      "webSearchRequests": 0,
      "costUSD": 0.26466425,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c85c283c-bba9-45f3-a04a-fad1d79f7dc0"
}
```

</details>

---
