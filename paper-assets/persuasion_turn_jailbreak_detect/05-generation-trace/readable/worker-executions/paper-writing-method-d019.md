# paper writing method d019

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_paper_writing_method_d019_20260518T061155.log`
- **Structured JSON:** [`413b05da9494cc63faed.json`](../../sessions/41/413b05da9494cc63faed.json)

## Before a recorded user message

22 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
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
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "4e18ede9-0545-422b-89a8-9f51fb66861a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/memory/"
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
    "resetsAt": 1779100200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "bc8097c8-9a53-49c7-b75e-7c70ee0070cf",
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665"
}
```

---

### Assistant

_source line 4_

I'll read the current method.tex to understand the existing structure before rewriting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "96caa237-8c2b-477a-a2b2-3434ece99e60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJK8cdNxNccK48rp51Kggt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14443,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14443
      },
      "output_tokens": 4,
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01X1hg5mrmD8u4vVxLW75FBa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "4bbc4554-0ffb-427c-9cc0-58b71a64b149",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJK8cdNxNccK48rp51Kggt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14443,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14443
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-18T06:12:07.291Z_

<details><summary>↩ Tool result · `toolu_01X1hg5mrmD8u4vVxLW75FBa`</summary>

```text
1	% method.tex — DisPeD Method Section
2	
3	\section{Method}
4	\label{sec:method}
5	
6	DisPeD is a two-stage framework for multi-turn jailbreak detection that operates on the pragmatic structure of conversations rather than their surface content. Stage~1 fine-tunes a turn-level encoder with a multi-task persuasion objective to produce representations sensitive to persuasion strategies. Stage~2 aggregates these turn-level representations for conversation-level binary classification. Figure~\ref{fig:architecture} illustrates the complete pipeline.
7	
8	\subsection{Problem Formulation}
9	
10	A multi-turn conversation $C = \{u_1, a_1, u_2, a_2, \ldots, u_N, a_N\}$ consists of alternating user turns $u_i$ and assistant responses $a_i$. We formulate jailbreak detection as binary classification over user turns: given a prefix of the first $K$ user turns $\{u_1, \ldots, u_K\}$, the model predicts whether the conversation constitutes a jailbreak attempt ($y=1$) or a benign interaction ($y=0$). We restrict the input to user turns because the adversarial intent resides in the attacker's messages; assistant responses are reactive and may contain refusals or compliance signals that confound detection. This formulation supports early detection, as the model can classify conversations from partial prefixes without waiting for the conversation to complete.
11	
12	\subsection{Stage 1: Persuasion-Aware Turn Encoding}
13	\label{sec:stage1}
14	
15	The core hypothesis of DisPeD is that multi-turn jailbreak attacks rely on persuasion strategies that leave detectable pragmatic signatures in the attacker's language, even when individual turns appear benign at the content level. Stage~1 encodes this hypothesis by fine-tuning a DeBERTa-v3-base encoder~\citep{he2021deberta} with a multi-task objective that jointly learns persuasion strategy classification and jailbreak-intent classification at the turn level.
16	
17	\paragraph{Turn encoding.}
18	Each user turn $u_i$ is passed through the DeBERTa encoder to obtain a contextualized representation. We take the [CLS] token embedding $h_i \in \mathbb{R}^d$ as the turn-level representation, where $d$ is the hidden dimension of DeBERTa-v3-base.
19	
20	\paragraph{Multi-task objective.}
21	Two classification heads operate on $h_i$ simultaneously. The first head performs 9-class persuasion strategy classification, producing a cross-entropy loss $L_{\text{strategy}}$. The second head performs binary jailbreak-intent classification, producing a cross-entropy loss $L_{\text{intent}}$. The combined training objective is:
22	\begin{equation}
23	  L = L_{\text{strategy}} + \alpha \cdot L_{\text{intent}}
24	  \label{eq:loss}
25	\end{equation}
26	where $\alpha$ controls the relative weight of the intent task. We set $\alpha = 0.3$ throughout all experiments, weighting the persuasion strategy task more heavily to prioritize pragmatic feature learning.
27	
28	The multi-task formulation serves a specific purpose: the persuasion classification task forces the encoder to learn representations that distinguish between different pragmatic strategies (e.g., rapport building vs.\ emotional manipulation), while the intent classification task ensures these representations remain useful for detecting adversarial intent. The encoder thus learns to attend to pragmatic cues in the attacker's language that transfer across attack types, rather than memorizing surface patterns from a single attack family.
29	
30	\paragraph{Persuasion taxonomy.}
31	We define a 9-class taxonomy of persuasion strategies grounded in the Persuasion Attack Paradigm (PAP)~\citep{zeng2024pap} and Cialdini's principles of influence~\citep{cialdini2001influence}. The nine categories comprise eight persuasion strategies and a none category for turns without an identifiable strategy:
32	
33	\begin{enumerate}[leftmargin=*, itemsep=1pt, topsep=2pt]
34	  \item[0.] \textbf{None}: no identifiable persuasion strategy.
35	  \item[1.] \textbf{Rapport Building}: establishing trust or common ground.
36	  \item[2.] \textbf{Authority Appeal}: invoking expertise, credentials, or institutional authority.
37	  \item[3.] \textbf{Emotional Manipulation}: exploiting emotional responses such as urgency, sympathy, or fear.
38	  \item[4.] \textbf{Logical Reframing}: restructuring requests to appear reasonable or benign.
39	  \item[5.] \textbf{Role Assignment}: assigning the model a persona that bypasses safety constraints.
40	  \item[6.] \textbf{Gradual Escalation}: incrementally increasing the severity of requests.
41	  \item[7.] \textbf{Obfuscation}: disguising intent through indirection, encoding, or ambiguity.
42	  \item[8.] \textbf{Direct Request}: explicit harmful requests without persuasion framing.
43	\end{enumerate}
44	
45	This taxonomy is not exhaustive but covers the dominant strategies identified in existing multi-turn attack analyses~\citep{zeng2024pap,russinovich2024crescendo,fitd2024,deceptivedelight2024}. Turn-level strategy annotations are produced by Qwen3-8B, a procedure we validate through ablation in Section~\ref{sec:ablation}: scrambled labels yield only a 1 percentage point reduction in OOD detection performance, confirming that the fine-tuning process on persuasion-related text, rather than label accuracy, is the primary driver of cross-attack generalization.
46	
47	\subsection{Stage 2: Conversation-Level Classification}
48	\label{sec:stage2}
49	
50	Stage~2 aggregates turn-level representations from the fine-tuned encoder into a single conversation-level prediction.
51	
52	\paragraph{Aggregation.}
53	Given a prefix of $K$ user turns encoded by the Stage-1 encoder, we obtain [CLS] embeddings $\{h_1, h_2, \ldots, h_K\}$. We aggregate these into a single conversation representation $\bar{h}$ using a bidirectional GRU (BiGRU):
54	\begin{equation}
55	  \bar{h} = [\overrightarrow{h_K};\; \overleftarrow{h_1}]
56	  \label{eq:bigru}
57	\end{equation}
58	where $\overrightarrow{h_K}$ and $\overleftarrow{h_1}$ are the final hidden states of the forward and backward GRU respectively, and $[;\;]$ denotes concatenation.
59	
60	Despite using a sequential model, the ablation in Section~\ref{sec:ablation} confirms that replacing BiGRU with orderless mean pooling yields equivalent OOD performance. The model therefore functions as a persuasion-presence detector that identifies whether individual turns carry persuasive intent, rather than a trajectory detector that exploits temporal ordering across turns.
61	
62	\paragraph{Classifier.}
63	A two-layer MLP takes $\bar{h}$ as input and produces a binary prediction $\hat{y} \in \{0, 1\}$, where $\hat{y} = 1$ indicates a jailbreak attempt. The Stage-2 classifier is trained on conversation-level labels while the Stage-1 encoder weights are frozen.
64	
65	\subsection{Design Rationale}
66	\label{sec:rationale}
67	
68	Several design choices in DisPeD reflect empirical findings from our ablation study (Section~\ref{sec:ablation}) and prior work on multi-turn attacks. We summarize the reasoning here and defer quantitative evidence to the experimental sections.
69	
70	\paragraph{Why persuasion-aware fine-tuning?}
71	Multi-turn jailbreak attacks such as Crescendo~\citep{russinovich2024crescendo} and Deceptive Delight~\citep{deceptivedelight2024} construct sequences of individually benign turns that collectively achieve an adversarial goal. Representation engineering analyses show that these turns occupy the same embedding region as genuinely benign text in pretrained encoders~\citep{bullwinkel2025repeng}, so standard semantic representations cannot separate attack turns from benign ones. Persuasion-aware fine-tuning shifts the encoder's attention from topical content to pragmatic features (implicit requests, escalation cues, rapport-building patterns) that distinguish persuasive from non-persuasive language, regardless of surface topic. Our experiments confirm this mechanism: Vanilla DeBERTa collapses to F1 = 0.284 on OOD Deceptive Delight while DisPeD maintains F1 = 1.000 (Section~\ref{sec:cross_attack}).
72	
73	\paragraph{Why does BiGRU not outperform mean pooling?}
74	If multi-turn attacks relied on specific temporal patterns (e.g., a fixed escalation sequence), BiGRU would outperform orderless aggregation. The equivalence of BiGRU and mean pooling in our ablation indicates that the signal lies in per-turn persuasion presence rather than inter-turn ordering. We use BiGRU as the default aggregator because all main experiments were conducted with this architecture; the ablation finding that mean pooling achieves identical OOD performance confirms that temporal modeling is unnecessary for this task, and the detection signal resides in individual turn representations rather than their sequential arrangement.
75	
76	\paragraph{Why retain the 9-class taxonomy?}
77	The ablation shows that scrambled labels and binary labels both yield OOD detection performance within 1 percentage point of the full 9-class taxonomy. The value of the 9-class taxonomy is interpretability, not detection accuracy. The predicted strategy labels enable trajectory analysis (Section~\ref{sec:strategy}) that exposes how different attack types employ distinct persuasion sequences. This interpretability allows security analysts to inspect and understand detection decisions, a property absent from black-box LLM-based detectors and lexical baselines.
78	
79	\paragraph{Vanilla DeBERTa as a controlled baseline.}
80	To isolate the effect of persuasion-aware fine-tuning, we evaluate a Vanilla DeBERTa baseline that uses the same Stage-2 pipeline (BiGRU over [CLS] embeddings, identical MLP classifier) but with an unfine-tuned DeBERTa encoder. Any performance gap between DisPeD and Vanilla DeBERTa is therefore attributable to Stage-1 fine-tuning alone. This controlled comparison directly tests the persuasion-awareness hypothesis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "bec03cf9-5e9c-4d0f-b2f9-4fcac9831555",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex",
      "content": "% method.tex — DisPeD Method Section\n\n\\section{Method}\n\\label{sec:method}\n\nDisPeD is a two-stage framework for multi-turn jailbreak detection that operates on the pragmatic structure of conversations rather than their surface content. Stage~1 fine-tunes a turn-level encoder with a multi-task persuasion objective to produce representations sensitive to persuasion strategies. Stage~2 aggregates these turn-level representations for conversation-level binary classification. Figure~\\ref{fig:architecture} illustrates the complete pipeline.\n\n\\subsection{Problem Formulation}\n\nA multi-turn conversation $C = \\{u_1, a_1, u_2, a_2, \\ldots, u_N, a_N\\}$ consists of alternating user turns $u_i$ and assistant responses $a_i$. We formulate jailbreak detection as binary classification over user turns: given a prefix of the first $K$ user turns $\\{u_1, \\ldots, u_K\\}$, the model predicts whether the conversation constitutes a jailbreak attempt ($y=1$) or a benign interaction ($y=0$). We restrict the input to user turns because the adversarial intent resides in the attacker's messages; assistant responses are reactive and may contain refusals or compliance signals that confound detection. This formulation supports early detection, as the model can classify conversations from partial prefixes without waiting for the conversation to complete.\n\n\\subsection{Stage 1: Persuasion-Aware Turn Encoding}\n\\label{sec:stage1}\n\nThe core hypothesis of DisPeD is that multi-turn jailbreak attacks rely on persuasion strategies that leave detectable pragmatic signatures in the attacker's language, even when individual turns appear benign at the content level. Stage~1 encodes this hypothesis by fine-tuning a DeBERTa-v3-base encoder~\\citep{he2021deberta} with a multi-task objective that jointly learns persuasion strategy classification and jailbreak-intent classification at the turn level.\n\n\\paragraph{Turn encoding.}\nEach user turn $u_i$ is passed through the DeBERTa encoder to obtain a contextualized representation. We take the [CLS] token embedding $h_i \\in \\mathbb{R}^d$ as the turn-level representation, where $d$ is the hidden dimension of DeBERTa-v3-base.\n\n\\paragraph{Multi-task objective.}\nTwo classification heads operate on $h_i$ simultaneously. The first head performs 9-class persuasion strategy classification, producing a cross-entropy loss $L_{\\text{strategy}}$. The second head performs binary jailbreak-intent classification, producing a cross-entropy loss $L_{\\text{intent}}$. The combined training objective is:\n\\begin{equation}\n  L = L_{\\text{strategy}} + \\alpha \\cdot L_{\\text{intent}}\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\alpha$ controls the relative weight of the intent task. We set $\\alpha = 0.3$ throughout all experiments, weighting the persuasion strategy task more heavily to prioritize pragmatic feature learning.\n\nThe multi-task formulation serves a specific purpose: the persuasion classification task forces the encoder to learn representations that distinguish between different pragmatic strategies (e.g., rapport building vs.\\ emotional manipulation), while the intent classification task ensures these representations remain useful for detecting adversarial intent. The encoder thus learns to attend to pragmatic cues in the attacker's language that transfer across attack types, rather than memorizing surface patterns from a single attack family.\n\n\\paragraph{Persuasion taxonomy.}\nWe define a 9-class taxonomy of persuasion strategies grounded in the Persuasion Attack Paradigm (PAP)~\\citep{zeng2024pap} and Cialdini's principles of influence~\\citep{cialdini2001influence}. The nine categories comprise eight persuasion strategies and a none category for turns without an identifiable strategy:\n\n\\begin{enumerate}[leftmargin=*, itemsep=1pt, topsep=2pt]\n  \\item[0.] \\textbf{None}: no identifiable persuasion strategy.\n  \\item[1.] \\textbf{Rapport Building}: establishing trust or common ground.\n  \\item[2.] \\textbf{Authority Appeal}: invoking expertise, credentials, or institutional authority.\n  \\item[3.] \\textbf{Emotional Manipulation}: exploiting emotional responses such as urgency, sympathy, or fear.\n  \\item[4.] \\textbf{Logical Reframing}: restructuring requests to appear reasonable or benign.\n  \\item[5.] \\textbf{Role Assignment}: assigning the model a persona that bypasses safety constraints.\n  \\item[6.] \\textbf{Gradual Escalation}: incrementally increasing the severity of requests.\n  \\item[7.] \\textbf{Obfuscation}: disguising intent through indirection, encoding, or ambiguity.\n  \\item[8.] \\textbf{Direct Request}: explicit harmful requests without persuasion framing.\n\\end{enumerate}\n\nThis taxonomy is not exhaustive but covers the dominant strategies identified in existing multi-turn attack analyses~\\citep{zeng2024pap,russinovich2024crescendo,fitd2024,deceptivedelight2024}. Turn-level strategy annotations are produced by Qwen3-8B, a procedure we validate through ablation in Section~\\ref{sec:ablation}: scrambled labels yield only a 1 percentage point reduction in OOD detection performance, confirming that the fine-tuning process on persuasion-related text, rather than label accuracy, is the primary driver of cross-attack generalization.\n\n\\subsection{Stage 2: Conversation-Level Classification}\n\\label{sec:stage2}\n\nStage~2 aggregates turn-level representations from the fine-tuned encoder into a single conversation-level prediction.\n\n\\paragraph{Aggregation.}\nGiven a prefix of $K$ user turns encoded by the Stage-1 encoder, we obtain [CLS] embeddings $\\{h_1, h_2, \\ldots, h_K\\}$. We aggregate these into a single conversation representation $\\bar{h}$ using a bidirectional GRU (BiGRU):\n\\begin{equation}\n  \\bar{h} = [\\overrightarrow{h_K};\\; \\overleftarrow{h_1}]\n  \\label{eq:bigru}\n\\end{equation}\nwhere $\\overrightarrow{h_K}$ and $\\overleftarrow{h_1}$ are the final hidden states of the forward and backward GRU respectively, and $[;\\;]$ denotes concatenation.\n\nDespite using a sequential model, the ablation in Section~\\ref{sec:ablation} confirms that replacing BiGRU with orderless mean pooling yields equivalent OOD performance. The model therefore functions as a persuasion-presence detector that identifies whether individual turns carry persuasive intent, rather than a trajectory detector that exploits temporal ordering across turns.\n\n\\paragraph{Classifier.}\nA two-layer MLP takes $\\bar{h}$ as input and produces a binary prediction $\\hat{y} \\in \\{0, 1\\}$, where $\\hat{y} = 1$ indicates a jailbreak attempt. The Stage-2 classifier is trained on conversation-level labels while the Stage-1 encoder weights are frozen.\n\n\\subsection{Design Rationale}\n\\label{sec:rationale}\n\nSeveral design choices in DisPeD reflect empirical findings from our ablation study (Section~\\ref{sec:ablation}) and prior work on multi-turn attacks. We summarize the reasoning here and defer quantitative evidence to the experimental sections.\n\n\\paragraph{Why persuasion-aware fine-tuning?}\nMulti-turn jailbreak attacks such as Crescendo~\\citep{russinovich2024crescendo} and Deceptive Delight~\\citep{deceptivedelight2024} construct sequences of individually benign turns that collectively achieve an adversarial goal. Representation engineering analyses show that these turns occupy the same embedding region as genuinely benign text in pretrained encoders~\\citep{bullwinkel2025repeng}, so standard semantic representations cannot separate attack turns from benign ones. Persuasion-aware fine-tuning shifts the encoder's attention from topical content to pragmatic features (implicit requests, escalation cues, rapport-building patterns) that distinguish persuasive from non-persuasive language, regardless of surface topic. Our experiments confirm this mechanism: Vanilla DeBERTa collapses to F1 = 0.284 on OOD Deceptive Delight while DisPeD maintains F1 = 1.000 (Section~\\ref{sec:cross_attack}).\n\n\\paragraph{Why does BiGRU not outperform mean pooling?}\nIf multi-turn attacks relied on specific temporal patterns (e.g., a fixed escalation sequence), BiGRU would outperform orderless aggregation. The equivalence of BiGRU and mean pooling in our ablation indicates that the signal lies in per-turn persuasion presence rather than inter-turn ordering. We use BiGRU as the default aggregator because all main experiments were conducted with this architecture; the ablation finding that mean pooling achieves identical OOD performance confirms that temporal modeling is unnecessary for this task, and the detection signal resides in individual turn representations rather than their sequential arrangement.\n\n\\paragraph{Why retain the 9-class taxonomy?}\nThe ablation shows that scrambled labels and binary labels both yield OOD detection performance within 1 percentage point of the full 9-class taxonomy. The value of the 9-class taxonomy is interpretability, not detection accuracy. The predicted strategy labels enable trajectory analysis (Section~\\ref{sec:strategy}) that exposes how different attack types employ distinct persuasion sequences. This interpretability allows security analysts to inspect and understand detection decisions, a property absent from black-box LLM-based detectors and lexical baselines.\n\n\\paragraph{Vanilla DeBERTa as a controlled baseline.}\nTo isolate the effect of persuasion-aware fine-tuning, we evaluate a Vanilla DeBERTa baseline that uses the same Stage-2 pipeline (BiGRU over [CLS] embeddings, identical MLP classifier) but with an unfine-tuned DeBERTa encoder. Any performance gap between DisPeD and Vanilla DeBERTa is therefore attributable to Stage-1 fine-tuning alone. This controlled comparison directly tests the persuasion-awareness hypothesis.",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I have the current method.tex. Let me rewrite it according to the D019 reframe instructions. The key changes are:

1. Opening paragraph: Reframe from "persuasion-aware" to "ablation-centric design" with five Stage-1 variants
2. Section 3.1: Keep as-is
3. Section 3.2: Rewrite completely - describe all 5 variants, explain decomposition logic
4. Section 3.3: Keep similar but update the note about mean pooling


5. Section 3.4: Now I need to rewrite the design rationale to align with the D019 findings, showing how each variant choice was motivated by the ablation results rather than theoretical assumptions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "cd9d597f-98d6-4518-926b-f1a545d9233b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSetrqjDcRzYVN6jo1ztMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2808,
      "cache_read_input_tokens": 26284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2808
      },
      "output_tokens": 10,
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

_source line 8_

Now I'll write the reframed method.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "f423db89-13a7-4a4b-8c20-4661860b4e33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSetrqjDcRzYVN6jo1ztMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2808,
      "cache_read_input_tokens": 26284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2808
      },
      "output_tokens": 10,
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

_source line 9_

<details open><summary>🔧 Tool call — Write · `toolu_01VhRDCBvfAGyBSH98os6z9N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex",
  "content": "% method.tex — D019 Reframe: Ablation-Centric Method Description\n\n\\section{Method}\n\\label{sec:method}\n\nDisPeD is a two-stage framework for multi-turn jailbreak detection. Stage~1 adapts a turn-level encoder through continued training on jailbreak conversation text. Stage~2 aggregates turn representations for conversation-level binary classification. To systematically identify what enables cross-attack generalization, we design five Stage-1 variants that decompose the contributions of domain exposure, supervised classification, label quality, and label granularity. Figure~\\ref{fig:architecture} illustrates the complete pipeline.\n\n\\subsection{Problem Formulation}\n\nA multi-turn conversation $C = \\{u_1, a_1, u_2, a_2, \\ldots, u_N, a_N\\}$ consists of alternating user turns $u_i$ and assistant responses $a_i$. We formulate jailbreak detection as binary classification over user turns: given a prefix of the first $K$ user turns $\\{u_1, \\ldots, u_K\\}$, the model predicts whether the conversation constitutes a jailbreak attempt ($y=1$) or a benign interaction ($y=0$). We restrict the input to user turns because adversarial intent resides in the attacker's messages; assistant responses are reactive and may contain refusals or compliance signals that confound detection. This formulation supports early detection, as the model can classify conversations from partial prefixes without waiting for the conversation to complete.\n\n\\subsection{Stage 1: Turn-Level Encoder Adaptation}\n\\label{sec:stage1}\n\nStage~1 adapts a DeBERTa-v3-base encoder~\\citep{he2021deberta} on jailbreak conversation text to produce turn-level representations for downstream detection. Rather than committing to a single training objective, we implement five variants that form a controlled decomposition of the factors potentially responsible for cross-attack generalization. All variants operate on the same training conversations; only the training objective differs.\n\n\\paragraph{Turn encoding.}\nEach user turn $u_i$ is passed through the DeBERTa encoder to obtain a contextualized representation. We take the \\texttt{[CLS]} token embedding $h_i \\in \\mathbb{R}^d$ as the turn-level representation, where $d$ is the hidden dimension of DeBERTa-v3-base.\n\n\\paragraph{Variant 1: 9-class (full model).}\nTwo classification heads operate on $h_i$ simultaneously. The first head performs 9-class persuasion strategy classification, producing a cross-entropy loss $L_{\\text{strategy}}$. The second head performs binary jailbreak-intent classification, producing a cross-entropy loss $L_{\\text{intent}}$. The combined training objective is:\n\\begin{equation}\n  L = L_{\\text{strategy}} + \\alpha \\cdot L_{\\text{intent}}\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\alpha = 0.3$ weights the intent task lower to prioritize pragmatic feature learning. The \\texttt{[CLS]} embedding from the fine-tuned encoder serves as the turn representation for Stage~2.\n\n\\paragraph{Variant 2: Binary.}\nThe same multi-task architecture as the 9-class variant, but the nine strategy labels are collapsed to a binary persuasion-present/absent distinction. This variant tests whether fine-grained label granularity contributes to detection performance, or whether coarse supervision suffices.\n\n\\paragraph{Variant 3: Scrambled.}\nThe full 9-class setup with strategy labels randomly permuted across turns. Each turn receives a label drawn uniformly from the nine categories, destroying the correspondence between text and label. This variant tests whether label correctness matters: if scrambled labels match correct labels, the encoder benefits from the classification training signal itself rather than from accurate persuasion annotations.\n\n\\paragraph{Variant 4: MLM-only.}\nContinued pretraining with 15\\% token masking on the same training conversations, following the standard masked language modeling (MLM) procedure. No classification heads are attached. This variant tests the most aggressive hypothesis: that supervised classification is entirely unnecessary, and unsupervised domain exposure alone suffices for cross-attack generalization.\n\n\\paragraph{Variant 5: Vanilla DeBERTa.}\nThe pretrained DeBERTa-v3-base encoder used without any continued training. This baseline controls for the effect of the Stage-2 pipeline itself. Any performance gap between this variant and any of the four trained variants is attributable to Stage-1 adaptation.\n\n\\paragraph{Decomposition logic.}\nThe five variants enable systematic attribution. If the 9-class, binary, and scrambled variants all achieve comparable out-of-distribution (OOD) detection, then label quality and granularity are non-essential factors. If the MLM-only variant matches the classification variants, supervised classification itself is unnecessary, and domain exposure is the operative mechanism. The gap between any adapted variant and vanilla DeBERTa isolates the total contribution of continued training on jailbreak conversation text.\n\n\\paragraph{9-class persuasion taxonomy.}\nThe 9-class variant uses a taxonomy of persuasion strategies grounded in the Persuasion Attack Paradigm (PAP)~\\citep{zeng2024pap} and Cialdini's principles of influence~\\citep{cialdini2001influence}. The nine categories comprise eight persuasion strategies and a none category for turns without an identifiable strategy:\n\n\\begin{enumerate}[leftmargin=*, itemsep=1pt, topsep=2pt]\n  \\item[0.] \\textbf{None}: no identifiable persuasion strategy.\n  \\item[1.] \\textbf{Rapport Building}: establishing trust or common ground.\n  \\item[2.] \\textbf{Authority Appeal}: invoking expertise, credentials, or institutional authority.\n  \\item[3.] \\textbf{Emotional Manipulation}: exploiting emotional responses such as urgency, sympathy, or fear.\n  \\item[4.] \\textbf{Logical Reframing}: restructuring requests to appear reasonable or benign.\n  \\item[5.] \\textbf{Role Assignment}: assigning the model a persona that bypasses safety constraints.\n  \\item[6.] \\textbf{Gradual Escalation}: incrementally increasing the severity of requests.\n  \\item[7.] \\textbf{Obfuscation}: disguising intent through indirection, encoding, or ambiguity.\n  \\item[8.] \\textbf{Direct Request}: explicit harmful requests without persuasion framing.\n\\end{enumerate}\n\nThis taxonomy covers the dominant strategies identified in existing multi-turn attack analyses~\\citep{zeng2024pap,russinovich2024crescendo,fitd2024,deceptivedelight2024}. Turn-level strategy annotations are produced by Qwen3-8B. As our experiments demonstrate (Section~\\ref{sec:ablation}), the taxonomy does not drive detection performance: scrambled labels, binary labels, and MLM-only training all match the 9-class model on OOD detection. The taxonomy's surviving value is interpretability, as predicted strategy labels enable trajectory analysis that reveals distinct persuasion fingerprints per attack type (Section~\\ref{sec:strategy}).\n\n\\subsection{Stage 2: Conversation-Level Classification}\n\\label{sec:stage2}\n\nStage~2 aggregates turn-level representations from the adapted encoder into a single conversation-level prediction. The Stage-1 encoder weights are frozen during Stage-2 training.\n\n\\paragraph{Aggregation.}\nGiven a prefix of $K$ user turns encoded by the Stage-1 encoder, we obtain \\texttt{[CLS]} embeddings $\\{h_1, h_2, \\ldots, h_K\\}$. We aggregate these into a single conversation representation $\\bar{h}$ using a bidirectional GRU (BiGRU):\n\\begin{equation}\n  \\bar{h} = [\\overrightarrow{h_K};\\; \\overleftarrow{h_1}]\n  \\label{eq:bigru}\n\\end{equation}\nwhere $\\overrightarrow{h_K}$ and $\\overleftarrow{h_1}$ are the final hidden states of the forward and backward GRU respectively, and $[;\\;]$ denotes concatenation. The ablation in Section~\\ref{sec:ablation} confirms that replacing BiGRU with orderless mean pooling yields equivalent OOD performance. The detection signal therefore resides in per-turn representations, not in their sequential arrangement.\n\n\\paragraph{Classifier.}\nA two-layer MLP takes $\\bar{h}$ as input and produces a binary prediction $\\hat{y} \\in \\{0, 1\\}$, where $\\hat{y} = 1$ indicates a jailbreak attempt.\n\n\\subsection{Design Rationale}\n\\label{sec:rationale}\n\n\\paragraph{Why five variants?}\nPrior work on multi-turn jailbreak detection has proposed various fine-tuning strategies but has not isolated which component of fine-tuning produces cross-attack generalization. A single model comparison (e.g., fine-tuned vs.\\ vanilla) conflates domain exposure with supervised learning. Our five-variant design separates these factors: classification supervision, label correctness, label granularity, and unsupervised domain exposure are each independently testable. Section~\\ref{sec:ablation} presents the full quantitative results.\n\n\\paragraph{Why does domain exposure suffice?}\nThe finding that MLM-only training matches supervised classification variants connects to the domain-adaptive pretraining (DAPT) literature~\\citep{gururangan2020dontstop}, which shows that continued pretraining on domain-specific text shifts encoder representations to capture domain-relevant features without task-specific labels. Jailbreak conversations contain pragmatic patterns that distinguish them from benign text: implicit requests masked by conversational framing, systematic escalation of sensitive content, and role-play setups designed to bypass safety constraints. Even unsupervised exposure to these patterns teaches the encoder to attend to the distributional signatures of adversarial conversation structure. Representation engineering analyses confirm that pretrained encoders place jailbreak turns in the same embedding region as benign text~\\citep{bullwinkel2025repeng}; continued training on jailbreak conversations separates these representations, with the specific training objective being secondary to the domain shift itself.\n\n\\paragraph{Why retain the 9-class taxonomy?}\nThe taxonomy is unnecessary for detection accuracy: all four adapted variants (9-class, binary, scrambled, MLM-only) achieve equivalent OOD performance. The taxonomy's value lies in interpretability. The predicted strategy labels enable trajectory analysis (Section~\\ref{sec:strategy}) that exposes how different attack types such as Crescendo~\\citep{russinovich2024crescendo} and Deceptive Delight~\\citep{deceptivedelight2024} employ distinct persuasion sequences. This interpretability allows security analysts to inspect and understand detection decisions, a property absent from black-box LLM-based detectors and lexical baselines.\n\n\\paragraph{Vanilla DeBERTa as controlled baseline.}\nTo isolate the total effect of Stage-1 adaptation, the vanilla variant passes unfine-tuned \\texttt{[CLS]} embeddings through the identical Stage-2 pipeline (BiGRU aggregation, same MLP classifier, same training procedure). Any performance gap between vanilla and the adapted variants is therefore attributable to Stage-1 training alone. This controlled comparison directly quantifies the contribution of domain exposure: vanilla DeBERTa achieves F1\\,=\\,0.284 on unseen Deceptive Delight, while all four adapted variants reach F1\\,$\\geq$\\,0.99 (Section~\\ref{sec:cross_attack}), a +72 percentage point gap bridged entirely by continued training on jailbreak conversation text.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "7b882a2a-292f-4eb0-bd1f-69fb5c2ebf59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSetrqjDcRzYVN6jo1ztMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2808,
      "cache_read_input_tokens": 26284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2808
      },
      "output_tokens": 10,
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

_source line 10 · 2026-05-18T06:12:54.141Z_

<details><summary>↩ Tool result · `toolu_01VhRDCBvfAGyBSH98os6z9N`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "98efbdc8-58f9-4931-8956-730295e86bf7",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex",
    "content": "% method.tex — D019 Reframe: Ablation-Centric Method Description\n\n\\section{Method}\n\\label{sec:method}\n\nDisPeD is a two-stage framework for multi-turn jailbreak detection. Stage~1 adapts a turn-level encoder through continued training on jailbreak conversation text. Stage~2 aggregates turn representations for conversation-level binary classification. To systematically identify what enables cross-attack generalization, we design five Stage-1 variants that decompose the contributions of domain exposure, supervised classification, label quality, and label granularity. Figure~\\ref{fig:architecture} illustrates the complete pipeline.\n\n\\subsection{Problem Formulation}\n\nA multi-turn conversation $C = \\{u_1, a_1, u_2, a_2, \\ldots, u_N, a_N\\}$ consists of alternating user turns $u_i$ and assistant responses $a_i$. We formulate jailbreak detection as binary classification over user turns: given a prefix of the first $K$ user turns $\\{u_1, \\ldots, u_K\\}$, the model predicts whether the conversation constitutes a jailbreak attempt ($y=1$) or a benign interaction ($y=0$). We restrict the input to user turns because adversarial intent resides in the attacker's messages; assistant responses are reactive and may contain refusals or compliance signals that confound detection. This formulation supports early detection, as the model can classify conversations from partial prefixes without waiting for the conversation to complete.\n\n\\subsection{Stage 1: Turn-Level Encoder Adaptation}\n\\label{sec:stage1}\n\nStage~1 adapts a DeBERTa-v3-base encoder~\\citep{he2021deberta} on jailbreak conversation text to produce turn-level representations for downstream detection. Rather than committing to a single training objective, we implement five variants that form a controlled decomposition of the factors potentially responsible for cross-attack generalization. All variants operate on the same training conversations; only the training objective differs.\n\n\\paragraph{Turn encoding.}\nEach user turn $u_i$ is passed through the DeBERTa encoder to obtain a contextualized representation. We take the \\texttt{[CLS]} token embedding $h_i \\in \\mathbb{R}^d$ as the turn-level representation, where $d$ is the hidden dimension of DeBERTa-v3-base.\n\n\\paragraph{Variant 1: 9-class (full model).}\nTwo classification heads operate on $h_i$ simultaneously. The first head performs 9-class persuasion strategy classification, producing a cross-entropy loss $L_{\\text{strategy}}$. The second head performs binary jailbreak-intent classification, producing a cross-entropy loss $L_{\\text{intent}}$. The combined training objective is:\n\\begin{equation}\n  L = L_{\\text{strategy}} + \\alpha \\cdot L_{\\text{intent}}\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\alpha = 0.3$ weights the intent task lower to prioritize pragmatic feature learning. The \\texttt{[CLS]} embedding from the fine-tuned encoder serves as the turn representation for Stage~2.\n\n\\paragraph{Variant 2: Binary.}\nThe same multi-task architecture as the 9-class variant, but the nine strategy labels are collapsed to a binary persuasion-present/absent distinction. This variant tests whether fine-grained label granularity contributes to detection performance, or whether coarse supervision suffices.\n\n\\paragraph{Variant 3: Scrambled.}\nThe full 9-class setup with strategy labels randomly permuted across turns. Each turn receives a label drawn uniformly from the nine categories, destroying the correspondence between text and label. This variant tests whether label correctness matters: if scrambled labels match correct labels, the encoder benefits from the classification training signal itself rather than from accurate persuasion annotations.\n\n\\paragraph{Variant 4: MLM-only.}\nContinued pretraining with 15\\% token masking on the same training conversations, following the standard masked language modeling (MLM) procedure. No classification heads are attached. This variant tests the most aggressive hypothesis: that supervised classification is entirely unnecessary, and unsupervised domain exposure alone suffices for cross-attack generalization.\n\n\\paragraph{Variant 5: Vanilla DeBERTa.}\nThe pretrained DeBERTa-v3-base encoder used without any continued training. This baseline controls for the effect of the Stage-2 pipeline itself. Any performance gap between this variant and any of the four trained variants is attributable to Stage-1 adaptation.\n\n\\paragraph{Decomposition logic.}\nThe five variants enable systematic attribution. If the 9-class, binary, and scrambled variants all achieve comparable out-of-distribution (OOD) detection, then label quality and granularity are non-essential factors. If the MLM-only variant matches the classification variants, supervised classification itself is unnecessary, and domain exposure is the operative mechanism. The gap between any adapted variant and vanilla DeBERTa isolates the total contribution of continued training on jailbreak conversation text.\n\n\\paragraph{9-class persuasion taxonomy.}\nThe 9-class variant uses a taxonomy of persuasion strategies grounded in the Persuasion Attack Paradigm (PAP)~\\citep{zeng2024pap} and Cialdini's principles of influence~\\citep{cialdini2001influence}. The nine categories comprise eight persuasion strategies and a none category for turns without an identifiable strategy:\n\n\\begin{enumerate}[leftmargin=*, itemsep=1pt, topsep=2pt]\n  \\item[0.] \\textbf{None}: no identifiable persuasion strategy.\n  \\item[1.] \\textbf{Rapport Building}: establishing trust or common ground.\n  \\item[2.] \\textbf{Authority Appeal}: invoking expertise, credentials, or institutional authority.\n  \\item[3.] \\textbf{Emotional Manipulation}: exploiting emotional responses such as urgency, sympathy, or fear.\n  \\item[4.] \\textbf{Logical Reframing}: restructuring requests to appear reasonable or benign.\n  \\item[5.] \\textbf{Role Assignment}: assigning the model a persona that bypasses safety constraints.\n  \\item[6.] \\textbf{Gradual Escalation}: incrementally increasing the severity of requests.\n  \\item[7.] \\textbf{Obfuscation}: disguising intent through indirection, encoding, or ambiguity.\n  \\item[8.] \\textbf{Direct Request}: explicit harmful requests without persuasion framing.\n\\end{enumerate}\n\nThis taxonomy covers the dominant strategies identified in existing multi-turn attack analyses~\\citep{zeng2024pap,russinovich2024crescendo,fitd2024,deceptivedelight2024}. Turn-level strategy annotations are produced by Qwen3-8B. As our experiments demonstrate (Section~\\ref{sec:ablation}), the taxonomy does not drive detection performance: scrambled labels, binary labels, and MLM-only training all match the 9-class model on OOD detection. The taxonomy's surviving value is interpretability, as predicted strategy labels enable trajectory analysis that reveals distinct persuasion fingerprints per attack type (Section~\\ref{sec:strategy}).\n\n\\subsection{Stage 2: Conversation-Level Classification}\n\\label{sec:stage2}\n\nStage~2 aggregates turn-level representations from the adapted encoder into a single conversation-level prediction. The Stage-1 encoder weights are frozen during Stage-2 training.\n\n\\paragraph{Aggregation.}\nGiven a prefix of $K$ user turns encoded by the Stage-1 encoder, we obtain \\texttt{[CLS]} embeddings $\\{h_1, h_2, \\ldots, h_K\\}$. We aggregate these into a single conversation representation $\\bar{h}$ using a bidirectional GRU (BiGRU):\n\\begin{equation}\n  \\bar{h} = [\\overrightarrow{h_K};\\; \\overleftarrow{h_1}]\n  \\label{eq:bigru}\n\\end{equation}\nwhere $\\overrightarrow{h_K}$ and $\\overleftarrow{h_1}$ are the final hidden states of the forward and backward GRU respectively, and $[;\\;]$ denotes concatenation. The ablation in Section~\\ref{sec:ablation} confirms that replacing BiGRU with orderless mean pooling yields equivalent OOD performance. The detection signal therefore resides in per-turn representations, not in their sequential arrangement.\n\n\\paragraph{Classifier.}\nA two-layer MLP takes $\\bar{h}$ as input and produces a binary prediction $\\hat{y} \\in \\{0, 1\\}$, where $\\hat{y} = 1$ indicates a jailbreak attempt.\n\n\\subsection{Design Rationale}\n\\label{sec:rationale}\n\n\\paragraph{Why five variants?}\nPrior work on multi-turn jailbreak detection has proposed various fine-tuning strategies but has not isolated which component of fine-tuning produces cross-attack generalization. A single model comparison (e.g., fine-tuned vs.\\ vanilla) conflates domain exposure with supervised learning. Our five-variant design separates these factors: classification supervision, label correctness, label granularity, and unsupervised domain exposure are each independently testable. Section~\\ref{sec:ablation} presents the full quantitative results.\n\n\\paragraph{Why does domain exposure suffice?}\nThe finding that MLM-only training matches supervised classification variants connects to the domain-adaptive pretraining (DAPT) literature~\\citep{gururangan2020dontstop}, which shows that continued pretraining on domain-specific text shifts encoder representations to capture domain-relevant features without task-specific labels. Jailbreak conversations contain pragmatic patterns that distinguish them from benign text: implicit requests masked by conversational framing, systematic escalation of sensitive content, and role-play setups designed to bypass safety constraints. Even unsupervised exposure to these patterns teaches the encoder to attend to the distributional signatures of adversarial conversation structure. Representation engineering analyses confirm that pretrained encoders place jailbreak turns in the same embedding region as benign text~\\citep{bullwinkel2025repeng}; continued training on jailbreak conversations separates these representations, with the specific training objective being secondary to the domain shift itself.\n\n\\paragraph{Why retain the 9-class taxonomy?}\nThe taxonomy is unnecessary for detection accuracy: all four adapted variants (9-class, binary, scrambled, MLM-only) achieve equivalent OOD performance. The taxonomy's value lies in interpretability. The predicted strategy labels enable trajectory analysis (Section~\\ref{sec:strategy}) that exposes how different attack types such as Crescendo~\\citep{russinovich2024crescendo} and Deceptive Delight~\\citep{deceptivedelight2024} employ distinct persuasion sequences. This interpretability allows security analysts to inspect and understand detection decisions, a property absent from black-box LLM-based detectors and lexical baselines.\n\n\\paragraph{Vanilla DeBERTa as controlled baseline.}\nTo isolate the total effect of Stage-1 adaptation, the vanilla variant passes unfine-tuned \\texttt{[CLS]} embeddings through the identical Stage-2 pipeline (BiGRU aggregation, same MLP classifier, same training procedure). Any performance gap between vanilla and the adapted variants is therefore attributable to Stage-1 training alone. This controlled comparison directly quantifies the contribution of domain exposure: vanilla DeBERTa achieves F1\\,=\\,0.284 on unseen Deceptive Delight, while all four adapted variants reach F1\\,$\\geq$\\,0.99 (Section~\\ref{sec:cross_attack}), a +72 percentage point gap bridged entirely by continued training on jailbreak conversation text.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 35,
        "newStart": 1,
        "newLines": 48,
        "lines": [
          "-% method.tex — DisPeD Method Section",
          "+% method.tex — D019 Reframe: Ablation-Centric Method Description",
          " ",
          " \\section{Method}",
          " \\label{sec:method}",
          " ",
          "-DisPeD is a two-stage framework for multi-turn jailbreak detection that operates on the pragmatic structure of conversations rather than their surface content. Stage~1 fine-tunes a turn-level encoder with a multi-task persuasion objective to produce representations sensitive to persuasion strategies. Stage~2 aggregates these turn-level representations for conversation-level binary classification. Figure~\\ref{fig:architecture} illustrates the complete pipeline.",
          "+DisPeD is a two-stage framework for multi-turn jailbreak detection. Stage~1 adapts a turn-level encoder through continued training on jailbreak conversation text. Stage~2 aggregates turn representations for conversation-level binary classification. To systematically identify what enables cross-attack generalization, we design five Stage-1 variants that decompose the contributions of domain exposure, supervised classification, label quality, and label granularity. Figure~\\ref{fig:architecture} illustrates the complete pipeline.",
          " ",
          " \\subsection{Problem Formulation}",
          " ",
          "-A multi-turn conversation $C = \\{u_1, a_1, u_2, a_2, \\ldots, u_N, a_N\\}$ consists of alternating user turns $u_i$ and assistant responses $a_i$. We formulate jailbreak detection as binary classification over user turns: given a prefix of the first $K$ user turns $\\{u_1, \\ldots, u_K\\}$, the model predicts whether the conversation constitutes a jailbreak attempt ($y=1$) or a benign interaction ($y=0$). We restrict the input to user turns because the adversarial intent resides in the attacker's messages; assistant responses are reactive and may contain refusals or compliance signals that confound detection. This formulation supports early detection, as the model can classify conversations from partial prefixes without waiting for the conversation to complete.",
          "+A multi-turn conversation $C = \\{u_1, a_1, u_2, a_2, \\ldots, u_N, a_N\\}$ consists of alternating user turns $u_i$ and assistant responses $a_i$. We formulate jailbreak detection as binary classification over user turns: given a prefix of the first $K$ user turns $\\{u_1, \\ldots, u_K\\}$, the model predicts whether the conversation constitutes a jailbreak attempt ($y=1$) or a benign interaction ($y=0$). We restrict the input to user turns because adversarial intent resides in the attacker's messages; assistant responses are reactive and may contain refusals or compliance signals that confound detection. This formulation supports early detection, as the model can classify conversations from partial prefixes without waiting for the conversation to complete.",
          " ",
          "-\\subsection{Stage 1: Persuasion-Aware Turn Encoding}",
          "+\\subsection{Stage 1: Turn-Level Encoder Adaptation}",
          " \\label{sec:stage1}",
          " ",
          "-The core hypothesis of DisPeD is that multi-turn jailbreak attacks rely on persuasion strategies that leave detectable pragmatic signatures in the attacker's language, even when individual turns appear benign at the content level. Stage~1 encodes this hypothesis by fine-tuning a DeBERTa-v3-base encoder~\\citep{he2021deberta} with a multi-task objective that jointly learns persuasion strategy classification and jailbreak-intent classification at the turn level.",
          "+Stage~1 adapts a DeBERTa-v3-base encoder~\\citep{he2021deberta} on jailbreak conversation text to produce turn-level representations for downstream detection. Rather than committing to a single training objective, we implement five variants that form a controlled decomposition of the factors potentially responsible for cross-attack generalization. All variants operate on the same training conversations; only the training objective differs.",
          " ",
          " \\paragraph{Turn encoding.}",
          "-Each user turn $u_i$ is passed through the DeBERTa encoder to obtain a contextualized representation. We take the [CLS] token embedding $h_i \\in \\mathbb{R}^d$ as the turn-level representation, where $d$ is the hidden dimension of DeBERTa-v3-base.",
          "+Each user turn $u_i$ is passed through the DeBERTa encoder to obtain a contextualized representation. We take the \\texttt{[CLS]} token embedding $h_i \\in \\mathbb{R}^d$ as the turn-level representation, where $d$ is the hidden dimension of DeBERTa-v3-base.",
          " ",
          "-\\paragraph{Multi-task objective.}",
          "+\\paragraph{Variant 1: 9-class (full model).}",
          " Two classification heads operate on $h_i$ simultaneously. The first head performs 9-class persuasion strategy classification, producing a cross-entropy loss $L_{\\text{strategy}}$. The second head performs binary jailbreak-intent classification, producing a cross-entropy loss $L_{\\text{intent}}$. The combined training objective is:",
          " \\begin{equation}",
          "   L = L_{\\text{strategy}} + \\alpha \\cdot L_{\\text{intent}}",
          "   \\label{eq:loss}",
          " \\end{equation}",
          "-where $\\alpha$ controls the relative weight of the intent task. We set $\\alpha = 0.3$ throughout all experiments, weighting the persuasion strategy task more heavily to prioritize pragmatic feature learning.",
          "+where $\\alpha = 0.3$ weights the intent task lower to prioritize pragmatic feature learning. The \\texttt{[CLS]} embedding from the fine-tuned encoder serves as the turn representation for Stage~2.",
          " ",
          "-The multi-task formulation serves a specific purpose: the persuasion classification task forces the encoder to learn representations that distinguish between different pragmatic strategies (e.g., rapport building vs.\\ emotional manipulation), while the intent classification task ensures these representations remain useful for detecting adversarial intent. The encoder thus learns to attend to pragmatic cues in the attacker's language that transfer across attack types, rather than memorizing surface patterns from a single attack family.",
          "+\\paragraph{Variant 2: Binary.}",
          "+The same multi-task architecture as the 9-class variant, but the nine strategy labels are collapsed to a binary persuasion-present/absent distinction. This variant tests whether fine-grained label granularity contributes to detection performance, or whether coarse supervision suffices.",
          " ",
          "-\\paragraph{Persuasion taxonomy.}",
          "-We define a 9-class taxonomy of persuasion strategies grounded in the Persuasion Attack Paradigm (PAP)~\\citep{zeng2024pap} and Cialdini's principles of influence~\\citep{cialdini2001influence}. The nine categories comprise eight persuasion strategies and a none category for turns without an identifiable strategy:",
          "+\\paragraph{Variant 3: Scrambled.}",
          "+The full 9-class setup with strategy labels randomly permuted across turns. Each turn receives a label drawn uniformly from the nine categories, destroying the correspondence between text and label. This variant tests whether label correctness matters: if scrambled labels match correct labels, the encoder benefits from the classification training signal itself rather than from accurate persuasion annotations.",
          " ",
          "+\\paragraph{Variant 4: MLM-only.}",
          "+Continued pretraining with 15\\% token masking on the same training conversations, following the standard masked language modeling (MLM) procedure. No classification heads are attached. This variant tests the most aggressive hypothesis: that supervised classification is entirely unnecessary, and unsupervised domain exposure alone suffices for cross-attack generalization.",
          "+",
          "+\\paragraph{Variant 5: Vanilla DeBERTa.}",
          "+The pretrained DeBERTa-v3-base encoder used without any continued training. This baseline controls for the effect of the Stage-2 pipeline itself. Any performance gap between this variant and any of the four trained variants is attributable to Stage-1 adaptation.",
          "+",
          "+\\paragraph{Decomposition logic.}",
          "+The five variants enable systematic attribution. If the 9-class, binary, and scrambled variants all achieve comparable out-of-distribution (OOD) detection, then label quality and granularity are non-essential factors. If the MLM-only variant matches the classification variants, supervised classification itself is unnecessary, and domain exposure is the operative mechanism. The gap between any adapted variant and vanilla DeBERTa isolates the total contribution of continued training on jailbreak conversation text.",
          "+",
          "+\\paragraph{9-class persuasion taxonomy.}",
          "+The 9-class variant uses a taxonomy of persuasion strategies grounded in the Persuasion Attack Paradigm (PAP)~\\citep{zeng2024pap} and Cialdini's principles of influence~\\citep{cialdini2001influence}. The nine categories comprise eight persuasion strategies and a none category for turns without an identifiable strategy:",
          "+",
          " \\begin{enumerate}[leftmargin=*, itemsep=1pt, topsep=2pt]",
          "   \\item[0.] \\textbf{None}: no identifiable persuasion strategy.",
          "   \\item[1.] \\textbf{Rapport Building}: establishing trust or common ground."
        ]
      },
      {
        "oldStart": 42,
        "oldLines": 39,
        "newStart": 55,
        "newLines": 35,
        "lines": [
          "   \\item[8.] \\textbf{Direct Request}: explicit harmful requests without persuasion framing.",
          " \\end{enumerate}",
          " ",
          "-This taxonomy is not exhaustive but covers the dominant strategies identified in existing multi-turn attack analyses~\\citep{zeng2024pap,russinovich2024crescendo,fitd2024,deceptivedelight2024}. Turn-level strategy annotations are produced by Qwen3-8B, a procedure we validate through ablation in Section~\\ref{sec:ablation}: scrambled labels yield only a 1 percentage point reduction in OOD detection performance, confirming that the fine-tuning process on persuasion-related text, rather than label accuracy, is the primary driver of cross-attack generalization.",
          "+This taxonomy covers the dominant strategies identified in existing multi-turn attack analyses~\\citep{zeng2024pap,russinovich2024crescendo,fitd2024,deceptivedelight2024}. Turn-level strategy annotations are produced by Qwen3-8B. As our experiments demonstrate (Section~\\ref{sec:ablation}), the taxonomy does not drive detection performance: scrambled labels, binary labels, and MLM-only training all match the 9-class model on OOD detection. The taxonomy's surviving value is interpretability, as predicted strategy labels enable trajectory analysis that reveals distinct persuasion fingerprints per attack type (Section~\\ref{sec:strategy}).",
          " ",
          " \\subsection{Stage 2: Conversation-Level Classification}",
          " \\label{sec:stage2}",
          " ",
          "-Stage~2 aggregates turn-level representations from the fine-tuned encoder into a single conversation-level prediction.",
          "+Stage~2 aggregates turn-level representations from the adapted encoder into a single conversation-level prediction. The Stage-1 encoder weights are frozen during Stage-2 training.",
          " ",
          " \\paragraph{Aggregation.}",
          "-Given a prefix of $K$ user turns encoded by the Stage-1 encoder, we obtain [CLS] embeddings $\\{h_1, h_2, \\ldots, h_K\\}$. We aggregate these into a single conversation representation $\\bar{h}$ using a bidirectional GRU (BiGRU):",
          "+Given a prefix of $K$ user turns encoded by the Stage-1 encoder, we obtain \\texttt{[CLS]} embeddings $\\{h_1, h_2, \\ldots, h_K\\}$. We aggregate these into a single conversation representation $\\bar{h}$ using a bidirectional GRU (BiGRU):",
          " \\begin{equation}",
          "   \\bar{h} = [\\overrightarrow{h_K};\\; \\overleftarrow{h_1}]",
          "   \\label{eq:bigru}",
          " \\end{equation}",
          "-where $\\overrightarrow{h_K}$ and $\\overleftarrow{h_1}$ are the final hidden states of the forward and backward GRU respectively, and $[;\\;]$ denotes concatenation.",
          "+where $\\overrightarrow{h_K}$ and $\\overleftarrow{h_1}$ are the final hidden states of the forward and backward GRU respectively, and $[;\\;]$ denotes concatenation. The ablation in Section~\\ref{sec:ablation} confirms that replacing BiGRU with orderless mean pooling yields equivalent OOD performance. The detection signal therefore resides in per-turn representations, not in their sequential arrangement.",
          " ",
          "-Despite using a sequential model, the ablation in Section~\\ref{sec:ablation} confirms that replacing BiGRU with orderless mean pooling yields equivalent OOD performance. The model therefore functions as a persuasion-presence detector that identifies whether individual turns carry persuasive intent, rather than a trajectory detector that exploits temporal ordering across turns.",
          "-",
          " \\paragraph{Classifier.}",
          "-A two-layer MLP takes $\\bar{h}$ as input and produces a binary prediction $\\hat{y} \\in \\{0, 1\\}$, where $\\hat{y} = 1$ indicates a jailbreak attempt. The Stage-2 classifier is trained on conversation-level labels while the Stage-1 encoder weights are frozen.",
          "+A two-layer MLP takes $\\bar{h}$ as input and produces a binary prediction $\\hat{y} \\in \\{0, 1\\}$, where $\\hat{y} = 1$ indicates a jailbreak attempt.",
          " ",
          " \\subsection{Design Rationale}",
          " \\label{sec:rationale}",
          " ",
          "-Several design choices in DisPeD reflect empirical findings from our ablation study (Section~\\ref{sec:ablation}) and prior work on multi-turn attacks. We summarize the reasoning here and defer quantitative evidence to the experimental sections.",
          "+\\paragraph{Why five variants?}",
          "+Prior work on multi-turn jailbreak detection has proposed various fine-tuning strategies but has not isolated which component of fine-tuning produces cross-attack generalization. A single model comparison (e.g., fine-tuned vs.\\ vanilla) conflates domain exposure with supervised learning. Our five-variant design separates these factors: classification supervision, label correctness, label granularity, and unsupervised domain exposure are each independently testable. Section~\\ref{sec:ablation} presents the full quantitative results.",
          " ",
          "-\\paragraph{Why persuasion-aware fine-tuning?}",
          "-Multi-turn jailbreak attacks such as Crescendo~\\citep{russinovich2024crescendo} and Deceptive Delight~\\citep{deceptivedelight2024} construct sequences of individually benign turns that collectively achieve an adversarial goal. Representation engineering analyses show that these turns occupy the same embedding region as genuinely benign text in pretrained encoders~\\citep{bullwinkel2025repeng}, so standard semantic representations cannot separate attack turns from benign ones. Persuasion-aware fine-tuning shifts the encoder's attention from topical content to pragmatic features (implicit requests, escalation cues, rapport-building patterns) that distinguish persuasive from non-persuasive language, regardless of surface topic. Our experiments confirm this mechanism: Vanilla DeBERTa collapses to F1 = 0.284 on OOD Deceptive Delight while DisPeD maintains F1 = 1.000 (Section~\\ref{sec:cross_attack}).",
          "+\\paragraph{Why does domain exposure suffice?}",
          "+The finding that MLM-only training matches supervised classification variants connects to the domain-adaptive pretraining (DAPT) literature~\\citep{gururangan2020dontstop}, which shows that continued pretraining on domain-specific text shifts encoder representations to capture domain-relevant features without task-specific labels. Jailbreak conversations contain pragmatic patterns that distinguish them from benign text: implicit requests masked by conversational framing, systematic escalation of sensitive content, and role-play setups designed to bypass safety constraints. Even unsupervised exposure to these patterns teaches the encoder to attend to the distributional signatures of adversarial conversation structure. Representation engineering analyses confirm that pretrained encoders place jailbreak turns in the same embedding region as benign text~\\citep{bullwinkel2025repeng}; continued training on jailbreak conversations separates these representations, with the specific training objective being secondary to the domain shift itself.",
          " ",
          "-\\paragraph{Why does BiGRU not outperform mean pooling?}",
          "-If multi-turn attacks relied on specific temporal patterns (e.g., a fixed escalation sequence), BiGRU would outperform orderless aggregation. The equivalence of BiGRU and mean pooling in our ablation indicates that the signal lies in per-turn persuasion presence rather than inter-turn ordering. We use BiGRU as the default aggregator because all main experiments were conducted with this architecture; the ablation finding that mean pooling achieves identical OOD performance confirms that temporal modeling is unnecessary for this task, and the detection signal resides in individual turn representations rather than their sequential arrangement.",
          "-",
          " \\paragraph{Why retain the 9-class taxonomy?}",
          "-The ablation shows that scrambled labels and binary labels both yield OOD detection performance within 1 percentage point of the full 9-class taxonomy. The value of the 9-class taxonomy is interpretability, not detection accuracy. The predicted strategy labels enable trajectory analysis (Section~\\ref{sec:strategy}) that exposes how different attack types employ distinct persuasion sequences. This interpretability allows security analysts to inspect and understand detection decisions, a property absent from black-box LLM-based detectors and lexical baselines.",
          "+The taxonomy is unnecessary for detection accuracy: all four adapted variants (9-class, binary, scrambled, MLM-only) achieve equivalent OOD performance. The taxonomy's value lies in interpretability. The predicted strategy labels enable trajectory analysis (Section~\\ref{sec:strategy}) that exposes how different attack types such as Crescendo~\\citep{russinovich2024crescendo} and Deceptive Delight~\\citep{deceptivedelight2024} employ distinct persuasion sequences. This interpretability allows security analysts to inspect and understand detection decisions, a property absent from black-box LLM-based detectors and lexical baselines.",
          " ",
          "-\\paragraph{Vanilla DeBERTa as a controlled baseline.}",
          "-To isolate the effect of persuasion-aware fine-tuning, we evaluate a Vanilla DeBERTa baseline that uses the same Stage-2 pipeline (BiGRU over [CLS] embeddings, identical MLP classifier) but with an unfine-tuned DeBERTa encoder. Any performance gap between DisPeD and Vanilla DeBERTa is therefore attributable to Stage-1 fine-tuning alone. This controlled comparison directly tests the persuasion-awareness hypothesis.",
          "\\ No newline at end of file",
          "+\\paragraph{Vanilla DeBERTa as controlled baseline.}",
          "+To isolate the total effect of Stage-1 adaptation, the vanilla variant passes unfine-tuned \\texttt{[CLS]} embeddings through the identical Stage-2 pipeline (BiGRU aggregation, same MLP classifier, same training procedure). Any performance gap between vanilla and the adapted variants is therefore attributable to Stage-1 training alone. This controlled comparison directly quantifies the contribution of domain exposure: vanilla DeBERTa achieves F1\\,=\\,0.284 on unseen Deceptive Delight, while all four adapted variants reach F1\\,$\\geq$\\,0.99 (Section~\\ref{sec:cross_attack}), a +72 percentage point gap bridged entirely by continued training on jailbreak conversation text."
        ]
      }
    ],
    "originalFile": "% method.tex — DisPeD Method Section\n\n\\section{Method}\n\\label{sec:method}\n\nDisPeD is a two-stage framework for multi-turn jailbreak detection that operates on the pragmatic structure of conversations rather than their surface content. Stage~1 fine-tunes a turn-level encoder with a multi-task persuasion objective to produce representations sensitive to persuasion strategies. Stage~2 aggregates these turn-level representations for conversation-level binary classification. Figure~\\ref{fig:architecture} illustrates the complete pipeline.\n\n\\subsection{Problem Formulation}\n\nA multi-turn conversation $C = \\{u_1, a_1, u_2, a_2, \\ldots, u_N, a_N\\}$ consists of alternating user turns $u_i$ and assistant responses $a_i$. We formulate jailbreak detection as binary classification over user turns: given a prefix of the first $K$ user turns $\\{u_1, \\ldots, u_K\\}$, the model predicts whether the conversation constitutes a jailbreak attempt ($y=1$) or a benign interaction ($y=0$). We restrict the input to user turns because the adversarial intent resides in the attacker's messages; assistant responses are reactive and may contain refusals or compliance signals that confound detection. This formulation supports early detection, as the model can classify conversations from partial prefixes without waiting for the conversation to complete.\n\n\\subsection{Stage 1: Persuasion-Aware Turn Encoding}\n\\label{sec:stage1}\n\nThe core hypothesis of DisPeD is that multi-turn jailbreak attacks rely on persuasion strategies that leave detectable pragmatic signatures in the attacker's language, even when individual turns appear benign at the content level. Stage~1 encodes this hypothesis by fine-tuning a DeBERTa-v3-base encoder~\\citep{he2021deberta} with a multi-task objective that jointly learns persuasion strategy classification and jailbreak-intent classification at the turn level.\n\n\\paragraph{Turn encoding.}\nEach user turn $u_i$ is passed through the DeBERTa encoder to obtain a contextualized representation. We take the [CLS] token embedding $h_i \\in \\mathbb{R}^d$ as the turn-level representation, where $d$ is the hidden dimension of DeBERTa-v3-base.\n\n\\paragraph{Multi-task objective.}\nTwo classification heads operate on $h_i$ simultaneously. The first head performs 9-class persuasion strategy classification, producing a cross-entropy loss $L_{\\text{strategy}}$. The second head performs binary jailbreak-intent classification, producing a cross-entropy loss $L_{\\text{intent}}$. The combined training objective is:\n\\begin{equation}\n  L = L_{\\text{strategy}} + \\alpha \\cdot L_{\\text{intent}}\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\alpha$ controls the relative weight of the intent task. We set $\\alpha = 0.3$ throughout all experiments, weighting the persuasion strategy task more heavily to prioritize pragmatic feature learning.\n\nThe multi-task formulation serves a specific purpose: the persuasion classification task forces the encoder to learn representations that distinguish between different pragmatic strategies (e.g., rapport building vs.\\ emotional manipulation), while the intent classification task ensures these representations remain useful for detecting adversarial intent. The encoder thus learns to attend to pragmatic cues in the attacker's language that transfer across attack types, rather than memorizing surface patterns from a single attack family.\n\n\\paragraph{Persuasion taxonomy.}\nWe define a 9-class taxonomy of persuasion strategies grounded in the Persuasion Attack Paradigm (PAP)~\\citep{zeng2024pap} and Cialdini's principles of influence~\\citep{cialdini2001influence}. The nine categories comprise eight persuasion strategies and a none category for turns without an identifiable strategy:\n\n\\begin{enumerate}[leftmargin=*, itemsep=1pt, topsep=2pt]\n  \\item[0.] \\textbf{None}: no identifiable persuasion strategy.\n  \\item[1.] \\textbf{Rapport Building}: establishing trust or common ground.\n  \\item[2.] \\textbf{Authority Appeal}: invoking expertise, credentials, or institutional authority.\n  \\item[3.] \\textbf{Emotional Manipulation}: exploiting emotional responses such as urgency, sympathy, or fear.\n  \\item[4.] \\textbf{Logical Reframing}: restructuring requests to appear reasonable or benign.\n  \\item[5.] \\textbf{Role Assignment}: assigning the model a persona that bypasses safety constraints.\n  \\item[6.] \\textbf{Gradual Escalation}: incrementally increasing the severity of requests.\n  \\item[7.] \\textbf{Obfuscation}: disguising intent through indirection, encoding, or ambiguity.\n  \\item[8.] \\textbf{Direct Request}: explicit harmful requests without persuasion framing.\n\\end{enumerate}\n\nThis taxonomy is not exhaustive but covers the dominant strategies identified in existing multi-turn attack analyses~\\citep{zeng2024pap,russinovich2024crescendo,fitd2024,deceptivedelight2024}. Turn-level strategy annotations are produced by Qwen3-8B, a procedure we validate through ablation in Section~\\ref{sec:ablation}: scrambled labels yield only a 1 percentage point reduction in OOD detection performance, confirming that the fine-tuning process on persuasion-related text, rather than label accuracy, is the primary driver of cross-attack generalization.\n\n\\subsection{Stage 2: Conversation-Level Classification}\n\\label{sec:stage2}\n\nStage~2 aggregates turn-level representations from the fine-tuned encoder into a single conversation-level prediction.\n\n\\paragraph{Aggregation.}\nGiven a prefix of $K$ user turns encoded by the Stage-1 encoder, we obtain [CLS] embeddings $\\{h_1, h_2, \\ldots, h_K\\}$. We aggregate these into a single conversation representation $\\bar{h}$ using a bidirectional GRU (BiGRU):\n\\begin{equation}\n  \\bar{h} = [\\overrightarrow{h_K};\\; \\overleftarrow{h_1}]\n  \\label{eq:bigru}\n\\end{equation}\nwhere $\\overrightarrow{h_K}$ and $\\overleftarrow{h_1}$ are the final hidden states of the forward and backward GRU respectively, and $[;\\;]$ denotes concatenation.\n\nDespite using a sequential model, the ablation in Section~\\ref{sec:ablation} confirms that replacing BiGRU with orderless mean pooling yields equivalent OOD performance. The model therefore functions as a persuasion-presence detector that identifies whether individual turns carry persuasive intent, rather than a trajectory detector that exploits temporal ordering across turns.\n\n\\paragraph{Classifier.}\nA two-layer MLP takes $\\bar{h}$ as input and produces a binary prediction $\\hat{y} \\in \\{0, 1\\}$, where $\\hat{y} = 1$ indicates a jailbreak attempt. The Stage-2 classifier is trained on conversation-level labels while the Stage-1 encoder weights are frozen.\n\n\\subsection{Design Rationale}\n\\label{sec:rationale}\n\nSeveral design choices in DisPeD reflect empirical findings from our ablation study (Section~\\ref{sec:ablation}) and prior work on multi-turn attacks. We summarize the reasoning here and defer quantitative evidence to the experimental sections.\n\n\\paragraph{Why persuasion-aware fine-tuning?}\nMulti-turn jailbreak attacks such as Crescendo~\\citep{russinovich2024crescendo} and Deceptive Delight~\\citep{deceptivedelight2024} construct sequences of individually benign turns that collectively achieve an adversarial goal. Representation engineering analyses show that these turns occupy the same embedding region as genuinely benign text in pretrained encoders~\\citep{bullwinkel2025repeng}, so standard semantic representations cannot separate attack turns from benign ones. Persuasion-aware fine-tuning shifts the encoder's attention from topical content to pragmatic features (implicit requests, escalation cues, rapport-building patterns) that distinguish persuasive from non-persuasive language, regardless of surface topic. Our experiments confirm this mechanism: Vanilla DeBERTa collapses to F1 = 0.284 on OOD Deceptive Delight while DisPeD maintains F1 = 1.000 (Section~\\ref{sec:cross_attack}).\n\n\\paragraph{Why does BiGRU not outperform mean pooling?}\nIf multi-turn attacks relied on specific temporal patterns (e.g., a fixed escalation sequence), BiGRU would outperform orderless aggregation. The equivalence of BiGRU and mean pooling in our ablation indicates that the signal lies in per-turn persuasion presence rather than inter-turn ordering. We use BiGRU as the default aggregator because all main experiments were conducted with this architecture; the ablation finding that mean pooling achieves identical OOD performance confirms that temporal modeling is unnecessary for this task, and the detection signal resides in individual turn representations rather than their sequential arrangement.\n\n\\paragraph{Why retain the 9-class taxonomy?}\nThe ablation shows that scrambled labels and binary labels both yield OOD detection performance within 1 percentage point of the full 9-class taxonomy. The value of the 9-class taxonomy is interpretability, not detection accuracy. The predicted strategy labels enable trajectory analysis (Section~\\ref{sec:strategy}) that exposes how different attack types employ distinct persuasion sequences. This interpretability allows security analysts to inspect and understand detection decisions, a property absent from black-box LLM-based detectors and lexical baselines.\n\n\\paragraph{Vanilla DeBERTa as a controlled baseline.}\nTo isolate the effect of persuasion-aware fine-tuning, we evaluate a Vanilla DeBERTa baseline that uses the same Stage-2 pipeline (BiGRU over [CLS] embeddings, identical MLP classifier) but with an unfine-tuned DeBERTa encoder. Any performance gap between DisPeD and Vanilla DeBERTa is therefore attributable to Stage-1 fine-tuning alone. This controlled comparison directly tests the persuasion-awareness hypothesis.",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 11_

Let me verify there are no em-dashes or explanatory en-dashes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "d0743be9-51da-4ce7-b8dd-58a8820bc3ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9UT2KmK9gn2cx47Xudvq9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3186,
      "cache_read_input_tokens": 29092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3186
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

_source line 12_

<details open><summary>🔧 Tool call — Grep · `toolu_01AqKp6mYgbo9QpSuN16ckrt`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex",
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
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "c03121f0-3956-4573-8cb7-c951e8c022a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9UT2KmK9gn2cx47Xudvq9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3186,
      "cache_read_input_tokens": 29092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3186
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

_source line 13 · 2026-05-18T06:12:57.687Z_

<details><summary>↩ Tool result · `toolu_01AqKp6mYgbo9QpSuN16ckrt`</summary>

```text
1:% method.tex — D019 Reframe: Ablation-Centric Method Description
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "48803a14-be63-4351-8b27-89c2c96fe932",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1:% method.tex — D019 Reframe: Ablation-Centric Method Description",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Grep · `toolu_01RCfWawT13HiiT9GBr6weNS`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex",
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
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "7064fb00-6949-4dce-95f5-afd4fbdc4ff2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9UT2KmK9gn2cx47Xudvq9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3186,
      "cache_read_input_tokens": 29092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3186
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

_source line 15 · 2026-05-18T06:12:58.508Z_

<details><summary>↩ Tool result · `toolu_01RCfWawT13HiiT9GBr6weNS`</summary>

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
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "9383adc2-7508-44f8-9937-471a1bfeecf1",
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

_source line 16_

<details open><summary>🔧 Tool call — Grep · `toolu_0161F27QFU6ynYRXsuYLiq6b`</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex",
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
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "9f045044-7961-43f0-b49f-2a30d80bb5ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9UT2KmK9gn2cx47Xudvq9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3186,
      "cache_read_input_tokens": 29092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3186
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

_source line 17 · 2026-05-18T06:12:59.330Z_

<details><summary>↩ Tool result · `toolu_0161F27QFU6ynYRXsuYLiq6b`</summary>

```text
54:  \item[7.] \textbf{Obfuscation}: disguising intent through indirection, encoding, or ambiguity.
83:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "74788f97-8ade-4688-8259-7347b604a365",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "54:  \\item[7.] \\textbf{Obfuscation}: disguising intent through indirection, encoding, or ambiguity.\n83:[Omitted long matching line]",
    "numLines": 2
  }
}
```

</details>

---

### Assistant

_source line 18_

The only em-dash is in the comment line (not rendered text). The `-ing,` matches are in list item descriptions and noun phrases ("encoding," "ordering,"), not trailing -ing participial phrases. Let me also verify word count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "3c5ee403-567a-47d2-81d0-4feb7cad9e79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XAYen34DfvmrhRvBHJfukS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 32278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 525
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

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_0113sBceFLHwnujdCAXR7s2S`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$\\\\]//g; s/%.*//g' | wc -w",
  "description": "Rough word count of method.tex excluding LaTeX commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "db85f698-8133-4f87-8ce4-a88dc4a66dd1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XAYen34DfvmrhRvBHJfukS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 32278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 525
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

_source line 20 · 2026-05-18T06:13:05.305Z_

<details><summary>↩ Tool result · `toolu_0113sBceFLHwnujdCAXR7s2S`</summary>

```text
1161
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "3b1cc1cd-612f-411c-a0a2-3242839a60ca",
  "tool_use_result": {
    "stdout": "1161",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 21_

~1160 words of content (LaTeX commands excluded), within the ~1400 budget.

method.tex rewritten. Key changes:

- **Section 3.2** renamed from "Persuasion-Aware Turn Encoding" to "Turn-Level Encoder Adaptation" with all five variants (9-class, binary, scrambled, MLM-only, vanilla) described as a controlled decomposition
- **Decomposition logic paragraph** explains what each comparison isolates
- **Taxonomy paragraph** now states upfront that it does not drive detection; its value is interpretability
- **Section 3.4** reframed around "why five variants?", "why does domain exposure suffice?" (with DAPT citation), and "why retain the taxonomy?" with the vanilla baseline paragraph quantifying the +72pp gap
- All writing rules followed: zero em-dashes in rendered text, no trailing -ing phrases, no stacked transition words, no banned vocabulary

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "uuid": "9cf71cb4-754a-4283-a929-ac91b07b1da3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zrFmwN9LDU98f8CXJAKxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 346,
      "cache_read_input_tokens": 32803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 346
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

_source line 22_

~1160 words of content (LaTeX commands excluded), within the ~1400 budget.

method.tex rewritten. Key changes:

- **Section 3.2** renamed from "Persuasion-Aware Turn Encoding" to "Turn-Level Encoder Adaptation" with all five variants (9-class, binary, scrambled, MLM-only, vanilla) described as a controlled decomposition
- **Decomposition logic paragraph** explains what each comparison isolates
- **Taxonomy paragraph** now states upfront that it does not drive detection; its value is interpretability
- **Section 3.4** reframed around "why five variants?", "why does domain exposure suffice?" (with DAPT citation), and "why retain the taxonomy?" with the vanilla baseline paragraph quantifying the +72pp gap
- All writing rules followed: zero em-dashes in rendered text, no trailing -ing phrases, no stacked transition words, no banned vocabulary

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 67273,
  "duration_api_ms": 68238,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "34a995d7-c12b-428d-a431-c992a5470665",
  "total_cost_usd": 0.303408,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 21308,
    "cache_read_input_tokens": 132298,
    "output_tokens": 4054,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21308,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 216,
        "cache_read_input_tokens": 32803,
        "cache_creation_input_tokens": 346,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 346
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2599,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0027040000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 4054,
      "cacheReadInputTokens": 132298,
      "cacheCreationInputTokens": 21308,
      "webSearchRequests": 0,
      "costUSD": 0.300704,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d78f5594-70e0-4cbb-ba92-f92a424aa3ad"
}
```

</details>

---
