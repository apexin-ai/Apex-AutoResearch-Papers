# paper patch new results

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_patch-new-results_20260515T042607.log`
- **Structured JSON:** [`94f86aa2e98f1df2bd09.json`](../../sessions/94/94f86aa2e98f1df2bd09.json)

## Before a recorded user message

33 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe",
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
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
  "uuid": "caa20b9d-a36b-4823-bf8d-f9eb553338fe",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-agent-progress-probe/memory/"
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
    "resetsAt": 1778836800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "fb20b54d-1d12-4c41-8f85-314fc1770c46",
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65"
}
```

---

### Assistant

_source line 4_

Let me start by reading the relevant paper sections to understand the current structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "7055c69b-5997-4bc1-ac7b-61634bed5e0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKcUKNVhpEyeN1AUav6omT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12349,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12349
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01WPQVbsP6HnEDmYPGc2c19v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "da8df453-f600-4211-b0b0-01985b0fb0e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKcUKNVhpEyeN1AUav6omT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12349,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12349
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

_source line 6 · 2026-05-15T04:26:16.198Z_

<details><summary>↩ Tool result · `toolu_01WPQVbsP6HnEDmYPGc2c19v`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Circular Evaluation and Its Implications}
5	\label{sec:circular}
6	
7	The structural RF's 0.995 macro-F1 (\S\ref{sec:main_results}) is a predictable consequence of feature--label overlap, not a detection achievement.
8	The 30 structural features include repetition ratios and file operation counts---the same signals $\lambda_1$ and $\lambda_2$ consume to produce silver labels.
9	This score therefore represents an upper bound on LF reverse-engineering fidelity (a feature overlap ablation in \S\ref{sec:feature_overlap} quantifies this decomposition).
10	
11	Three evaluation settings break this circularity.
12	First, cross-coding-agent transfer: GB trained on SWE-Agent LF distributions achieves 0.967 macro-F1 on OpenHands, where LF firing patterns differ substantially (e.g., cmd\_rep votes stagnation on 5.4\% vs.\ 65.5\% of windows).
13	The model cannot memorize LF outputs when tested on a different agent's distribution.
14	Second, instance isolation: removing 284 SWE-bench task instances (8.3\% of OH test data) that appear in both training and test sets changes all cross-coding-agent macro-F1 by ${<}$0.1\,pp (Table~\ref{tab:instance_isolation}), ruling out instance memorization as an explanation for transfer performance.
15	Third, a human-annotated gold set (\S\ref{sec:gold_set}) will provide definitive non-circular ground truth.
16	Until then, all in-domain structural metrics should be interpreted as LF-agreement scores rather than detection accuracy.
17	
18	\subsection{Feature Overlap Ablation}
19	\label{sec:feature_overlap}
20	
21	To quantify how much of the structural classifier's performance derives from LF-overlapping features versus residual signal, we partition the 30 features into two groups.
22	A feature is classified as \emph{LF-overlapping} if it directly computes the same function as any labeling function: command uniqueness and repetition ratios, adjacent command similarity scores ($\lambda_1$), edit and search command counts and ratios, file display counts ($\lambda_2$), and the short-trajectory indicator ($\lambda_3$).
23	This yields 11 LF-overlapping and 19 residual features (full classification in Appendix Table~\ref{tab:feature_defs}).
24	Table~\ref{tab:feature_overlap} reports GB performance for each subset.
25	
26	\begin{table}[t]
27	\centering
28	\small
29	\begin{tabular}{lccc}
30	\toprule
31	\textbf{Feature Set} & \textbf{\#Feat} & \textbf{In-Dom.} & \textbf{Cross-Ag.} \\
32	\midrule
33	Full (all 30) & 30 & 0.9951 & 0.9674 \\
34	LF-overlap only & 11 & 0.9937 & 0.9770 \\
35	Residual only & 19 & 0.9515 & 0.5656 \\
36	\bottomrule
37	\end{tabular}
38	\caption{Feature overlap ablation (GB). In-Dom.\ = SWE-Agent in-domain macro-F1; Cross-Ag.\ = SWE-Agent $\to$ OpenHands zero-shot. LF-overlap features alone exceed the full model cross-coding-agent (+1.0\,pp); residual features collapse.}
39	\label{tab:feature_overlap}
40	\end{table}
41	
42	Three findings emerge.
43	First, 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1---exceeding the full 30-feature model (0.967) by 1.0\,pp.
44	This is the opposite of what label leakage would predict: if these features merely reconstructed the labeling pipeline, adding more features could only help or be neutral, not hurt.
45	The improvement under fewer features reflects a regularization effect: the 19 residual features encode agent-specific patterns that introduce noise harmful to cross-coding-agent generalization.
46	
47	Second, residual features retain non-trivial in-domain signal: 19 features achieve 0.952 macro-F1, confirming that stagnation manifests in patterns beyond what the three LFs capture---text length statistics, trajectory counts, and output statistics carry independent diagnostic value.
48	However, this signal is agent-specific: cross-coding-agent F1 collapses to 0.566, near the majority baseline (${\sim}$0.55).
49	
50	Third, LF alignment is evidence of correct LF design, not circularity.
51	The features that generalize across coding agents are precisely those encoding universal stagnation signals---command repetition patterns and file operation dynamics---rather than agent-specific idiosyncrasies captured by residual features.
52	One might object that LF-overlapping features merely reconstruct the label-generation pipeline rather than detecting real stagnation.
53	Two observations counter this.
54	First, the cross-coding-agent evaluation is itself non-circular: the SWE-Agent LF firing distribution differs drastically from OpenHands (e.g., cmd\_rep fires on 65.5\% vs.\ 5.4\% of windows), so a model that merely memorizes LF outputs would fail on the target agent---yet structural GB achieves 0.967.
55	Second, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.
56	
57	\subsection{Why No Label Model Improves Over Majority Vote}
58	\label{sec:why_tlm_fail}
59	
60	Despite clear temporal structure in LF activations (\S\ref{sec:lf_temporal}), no label model---temporal or generative---improves downstream detection over majority vote (\S\ref{sec:temporal_label_models}).
61	The failure spans five models with distinct inductive biases: TWV and Lag-HMM model temporal dynamics, HMM captures latent state transitions, while FlyingSquid and Snorkel MeTaL assume conditional independence.
62	All fail for the same root cause: three binary LFs produce at most $2^3{=}8$ voting patterns, and conf${\geq}$2 windows dominate the training set, leaving insufficient inter-LF conflict for any aggregation method to exploit.
63	
64	The failure modes differ by model class.
65	Temporal models either introduce noise (TWV: $-$2.57\,pp downstream despite $+$0.6\,pp self-evaluated) or overpredict stagnation (HMM: $-$14.4\,pp).
66	Generative models fare worse: FlyingSquid ($-$11.3\,pp) introduces systematic stagnation bias, and Snorkel MeTaL collapses catastrophically ($-$63.6\,pp, 42.3\% MV agreement).
67	Both assume conditional independence among LFs---violated by the shared behavioral signals underlying our three functions---and lack sequential structure to recover from this misspecification.
68	
69	The bottleneck is LF quantity, not aggregation sophistication.
70	Three binary LFs represent a realistic operating point for domain-specific agent monitoring, where each LF requires expert knowledge of agent failure modes.
71	Our finding that temporal label models fail in this low-LF regime has direct implications for practitioners who cannot afford to design ${>}$10 labeling functions: majority vote is not merely a convenient baseline but the recommended aggregation strategy.
72	Scaling to a richer LF set with higher disagreement rates would be needed to create the ambiguity where advanced aggregation could add value \citep{ratner2017snorkel}.
73	
74	\subsection{Error Analysis}
75	\label{sec:error_analysis}
76	
77	We analyze errors of the ProgressProbe (GRU) on the SWE-Agent conf${\geq}$2 test set under the stagnation-positive convention (positive = stagnation throughout).
78	The model misclassifies 131 of 1,824 windows (7.2\% error rate): 85 false negatives (predicted progress, actual stagnation; 64.9\% of errors) and 46 false positives (predicted stagnation, actual progress; 35.1\%).
79	
80	The recall bottleneck is the dominant failure mode: $P_\text{stag}{=}0.897$ vs.\ $R_\text{stag}{=}0.825$.
81	Missed stagnation windows (FN) are not borderline cases---the model assigns them a mean stagnation probability of only 0.078 (i.e., high progress confidence of 0.922), with 73\% receiving $>$0.9 progress probability.
82	These windows feature agents performing diverse edits and varied commands that mimic progress patterns while making no effective headway, constituting a systematic blind spot.
83	False positives arise when agents repeat specific command patterns during genuine progress.
84	
85	LF conflict is a strong error predictor: 39.7\% of error windows have at least one LF disagreeing, compared to a 31\% base rate.
86	The cmd\_rep LF contributes the highest per-LF error rate (12.75\%).
87	Errors concentrate in trajectory midpoints (10.2\% error rate vs.\ 6.5\% at endpoints), where the boundary between exploration and stagnation is most ambiguous.
88	Error mass is also non-uniform across trajectories: the two highest-error trajectories account for 18.3\% of all misclassifications.
89	
90	\subsection{Cross-Agent Error Patterns}
91	\label{sec:cross_agent_errors}
92	
93	We extend error analysis to cross-coding-agent transfer, evaluating the SWE-trained probe and structural GB on the full OH conf${\geq}$2 set (43,376 windows).
94	The probe misclassifies 19.9\% of windows, while structural GB errs on only 0.51\% (223 windows)---a nearly 40$\times$ gap that quantifies the distributional shift penalty for learned embeddings.
95	Of the probe's errors, 80.5\% are false positives (predicting stagnation on progress windows), indicating that the probe systematically misreads OH action patterns as stagnation signals learned from SWE-Agent.
96	
97	The two models' errors are nearly disjoint: only 2.2\% of probe errors overlap with structural errors (192 of 8,643 probe-error windows).
98	Structural features, being agent-agnostic by construction, are immune to the embedding distribution shift that drives probe failures.
99	
100	The probe's cross-coding-agent errors are not borderline: 62\% occur at high confidence ($>$0.9 or $<$0.1), ruling out threshold tuning as a remedy.
101	The embedding space encodes SWE-Agent--specific stagnation patterns that confidently misfire on OH distributions, explaining why even 5\% target fine-tuning (reaching 0.850 macro-F1) dramatically outperforms zero-shot transfer.
102	
103	\subsection{Outcome Backpropagation as Distant Supervision}
104	\label{sec:ob_analysis}
105	
106	Outcome backpropagation ($\lambda_3$) is a privileged signal that uses task outcome, unavailable at inference time.
107	A 3-seed split-isolated holdout removing $\lambda_3$ yields macro-F1 of $0.770{\pm}0.022$, a 7.7\,pp drop from the 3-LF baseline of 0.847.
108	$\lambda_3$ contributes 33.5\% of conf${\geq}$2 labels (5,158 of 15,401 windows).
109	
110	However, $\lambda_3$ functions as a coverage expander rather than an independent corrector: across 43,402 windows where both 2-LF and 3-LF configurations produce labels, their agreement is 100\%.
111	$\lambda_3$ never flips a majority vote---it only promotes conf${=}1$ windows to conf${=}2$ by adding a third agreeing vote.
112	This suggests that additional real-time LFs targeting the same coverage gaps could replace the privileged outcome signal without sacrificing label quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "be73893c-9f5e-4638-8fd4-77c628410f3f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Circular Evaluation and Its Implications}\n\\label{sec:circular}\n\nThe structural RF's 0.995 macro-F1 (\\S\\ref{sec:main_results}) is a predictable consequence of feature--label overlap, not a detection achievement.\nThe 30 structural features include repetition ratios and file operation counts---the same signals $\\lambda_1$ and $\\lambda_2$ consume to produce silver labels.\nThis score therefore represents an upper bound on LF reverse-engineering fidelity (a feature overlap ablation in \\S\\ref{sec:feature_overlap} quantifies this decomposition).\n\nThree evaluation settings break this circularity.\nFirst, cross-coding-agent transfer: GB trained on SWE-Agent LF distributions achieves 0.967 macro-F1 on OpenHands, where LF firing patterns differ substantially (e.g., cmd\\_rep votes stagnation on 5.4\\% vs.\\ 65.5\\% of windows).\nThe model cannot memorize LF outputs when tested on a different agent's distribution.\nSecond, instance isolation: removing 284 SWE-bench task instances (8.3\\% of OH test data) that appear in both training and test sets changes all cross-coding-agent macro-F1 by ${<}$0.1\\,pp (Table~\\ref{tab:instance_isolation}), ruling out instance memorization as an explanation for transfer performance.\nThird, a human-annotated gold set (\\S\\ref{sec:gold_set}) will provide definitive non-circular ground truth.\nUntil then, all in-domain structural metrics should be interpreted as LF-agreement scores rather than detection accuracy.\n\n\\subsection{Feature Overlap Ablation}\n\\label{sec:feature_overlap}\n\nTo quantify how much of the structural classifier's performance derives from LF-overlapping features versus residual signal, we partition the 30 features into two groups.\nA feature is classified as \\emph{LF-overlapping} if it directly computes the same function as any labeling function: command uniqueness and repetition ratios, adjacent command similarity scores ($\\lambda_1$), edit and search command counts and ratios, file display counts ($\\lambda_2$), and the short-trajectory indicator ($\\lambda_3$).\nThis yields 11 LF-overlapping and 19 residual features (full classification in Appendix Table~\\ref{tab:feature_defs}).\nTable~\\ref{tab:feature_overlap} reports GB performance for each subset.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{\\#Feat} & \\textbf{In-Dom.} & \\textbf{Cross-Ag.} \\\\\n\\midrule\nFull (all 30) & 30 & 0.9951 & 0.9674 \\\\\nLF-overlap only & 11 & 0.9937 & 0.9770 \\\\\nResidual only & 19 & 0.9515 & 0.5656 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature overlap ablation (GB). In-Dom.\\ = SWE-Agent in-domain macro-F1; Cross-Ag.\\ = SWE-Agent $\\to$ OpenHands zero-shot. LF-overlap features alone exceed the full model cross-coding-agent (+1.0\\,pp); residual features collapse.}\n\\label{tab:feature_overlap}\n\\end{table}\n\nThree findings emerge.\nFirst, 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1---exceeding the full 30-feature model (0.967) by 1.0\\,pp.\nThis is the opposite of what label leakage would predict: if these features merely reconstructed the labeling pipeline, adding more features could only help or be neutral, not hurt.\nThe improvement under fewer features reflects a regularization effect: the 19 residual features encode agent-specific patterns that introduce noise harmful to cross-coding-agent generalization.\n\nSecond, residual features retain non-trivial in-domain signal: 19 features achieve 0.952 macro-F1, confirming that stagnation manifests in patterns beyond what the three LFs capture---text length statistics, trajectory counts, and output statistics carry independent diagnostic value.\nHowever, this signal is agent-specific: cross-coding-agent F1 collapses to 0.566, near the majority baseline (${\\sim}$0.55).\n\nThird, LF alignment is evidence of correct LF design, not circularity.\nThe features that generalize across coding agents are precisely those encoding universal stagnation signals---command repetition patterns and file operation dynamics---rather than agent-specific idiosyncrasies captured by residual features.\nOne might object that LF-overlapping features merely reconstruct the label-generation pipeline rather than detecting real stagnation.\nTwo observations counter this.\nFirst, the cross-coding-agent evaluation is itself non-circular: the SWE-Agent LF firing distribution differs drastically from OpenHands (e.g., cmd\\_rep fires on 65.5\\% vs.\\ 5.4\\% of windows), so a model that merely memorizes LF outputs would fail on the target agent---yet structural GB achieves 0.967.\nSecond, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \\emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.\n\n\\subsection{Why No Label Model Improves Over Majority Vote}\n\\label{sec:why_tlm_fail}\n\nDespite clear temporal structure in LF activations (\\S\\ref{sec:lf_temporal}), no label model---temporal or generative---improves downstream detection over majority vote (\\S\\ref{sec:temporal_label_models}).\nThe failure spans five models with distinct inductive biases: TWV and Lag-HMM model temporal dynamics, HMM captures latent state transitions, while FlyingSquid and Snorkel MeTaL assume conditional independence.\nAll fail for the same root cause: three binary LFs produce at most $2^3{=}8$ voting patterns, and conf${\\geq}$2 windows dominate the training set, leaving insufficient inter-LF conflict for any aggregation method to exploit.\n\nThe failure modes differ by model class.\nTemporal models either introduce noise (TWV: $-$2.57\\,pp downstream despite $+$0.6\\,pp self-evaluated) or overpredict stagnation (HMM: $-$14.4\\,pp).\nGenerative models fare worse: FlyingSquid ($-$11.3\\,pp) introduces systematic stagnation bias, and Snorkel MeTaL collapses catastrophically ($-$63.6\\,pp, 42.3\\% MV agreement).\nBoth assume conditional independence among LFs---violated by the shared behavioral signals underlying our three functions---and lack sequential structure to recover from this misspecification.\n\nThe bottleneck is LF quantity, not aggregation sophistication.\nThree binary LFs represent a realistic operating point for domain-specific agent monitoring, where each LF requires expert knowledge of agent failure modes.\nOur finding that temporal label models fail in this low-LF regime has direct implications for practitioners who cannot afford to design ${>}$10 labeling functions: majority vote is not merely a convenient baseline but the recommended aggregation strategy.\nScaling to a richer LF set with higher disagreement rates would be needed to create the ambiguity where advanced aggregation could add value \\citep{ratner2017snorkel}.\n\n\\subsection{Error Analysis}\n\\label{sec:error_analysis}\n\nWe analyze errors of the ProgressProbe (GRU) on the SWE-Agent conf${\\geq}$2 test set under the stagnation-positive convention (positive = stagnation throughout).\nThe model misclassifies 131 of 1,824 windows (7.2\\% error rate): 85 false negatives (predicted progress, actual stagnation; 64.9\\% of errors) and 46 false positives (predicted stagnation, actual progress; 35.1\\%).\n\nThe recall bottleneck is the dominant failure mode: $P_\\text{stag}{=}0.897$ vs.\\ $R_\\text{stag}{=}0.825$.\nMissed stagnation windows (FN) are not borderline cases---the model assigns them a mean stagnation probability of only 0.078 (i.e., high progress confidence of 0.922), with 73\\% receiving $>$0.9 progress probability.\nThese windows feature agents performing diverse edits and varied commands that mimic progress patterns while making no effective headway, constituting a systematic blind spot.\nFalse positives arise when agents repeat specific command patterns during genuine progress.\n\nLF conflict is a strong error predictor: 39.7\\% of error windows have at least one LF disagreeing, compared to a 31\\% base rate.\nThe cmd\\_rep LF contributes the highest per-LF error rate (12.75\\%).\nErrors concentrate in trajectory midpoints (10.2\\% error rate vs.\\ 6.5\\% at endpoints), where the boundary between exploration and stagnation is most ambiguous.\nError mass is also non-uniform across trajectories: the two highest-error trajectories account for 18.3\\% of all misclassifications.\n\n\\subsection{Cross-Agent Error Patterns}\n\\label{sec:cross_agent_errors}\n\nWe extend error analysis to cross-coding-agent transfer, evaluating the SWE-trained probe and structural GB on the full OH conf${\\geq}$2 set (43,376 windows).\nThe probe misclassifies 19.9\\% of windows, while structural GB errs on only 0.51\\% (223 windows)---a nearly 40$\\times$ gap that quantifies the distributional shift penalty for learned embeddings.\nOf the probe's errors, 80.5\\% are false positives (predicting stagnation on progress windows), indicating that the probe systematically misreads OH action patterns as stagnation signals learned from SWE-Agent.\n\nThe two models' errors are nearly disjoint: only 2.2\\% of probe errors overlap with structural errors (192 of 8,643 probe-error windows).\nStructural features, being agent-agnostic by construction, are immune to the embedding distribution shift that drives probe failures.\n\nThe probe's cross-coding-agent errors are not borderline: 62\\% occur at high confidence ($>$0.9 or $<$0.1), ruling out threshold tuning as a remedy.\nThe embedding space encodes SWE-Agent--specific stagnation patterns that confidently misfire on OH distributions, explaining why even 5\\% target fine-tuning (reaching 0.850 macro-F1) dramatically outperforms zero-shot transfer.\n\n\\subsection{Outcome Backpropagation as Distant Supervision}\n\\label{sec:ob_analysis}\n\nOutcome backpropagation ($\\lambda_3$) is a privileged signal that uses task outcome, unavailable at inference time.\nA 3-seed split-isolated holdout removing $\\lambda_3$ yields macro-F1 of $0.770{\\pm}0.022$, a 7.7\\,pp drop from the 3-LF baseline of 0.847.\n$\\lambda_3$ contributes 33.5\\% of conf${\\geq}$2 labels (5,158 of 15,401 windows).\n\nHowever, $\\lambda_3$ functions as a coverage expander rather than an independent corrector: across 43,402 windows where both 2-LF and 3-LF configurations produce labels, their agreement is 100\\%.\n$\\lambda_3$ never flips a majority vote---it only promotes conf${=}1$ windows to conf${=}2$ by adding a third agreeing vote.\nThis suggests that additional real-time LFs targeting the same coverage gaps could replace the privileged outcome signal without sacrificing label quality.",
      "numLines": 112,
      "startLine": 1,
      "totalLines": 112
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_016ThobHcHBYFw81t1wKZTgt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "0dd197a3-c4f3-4f0d-89ce-654fddc87a22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKcUKNVhpEyeN1AUav6omT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12349,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12349
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

_source line 8 · 2026-05-15T04:26:16.601Z_

<details><summary>↩ Tool result · `toolu_016ThobHcHBYFw81t1wKZTgt`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We organize results around three questions:
5	(1)~which method best detects stagnation across deployment scenarios? (\S\ref{sec:main_results}--\S\ref{sec:robustness});
6	(2)~what drives label quality and cross-coding-agent transfer bottlenecks? (\S\ref{sec:lf_temporal}--\S\ref{sec:cmd_rep_ablation});
7	(3)~can temporal structure in LFs improve labels? (\S\ref{sec:temporal_label_models}).
8	All reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\S\ref{sec:method}).
9	
10	\paragraph{Circular evaluation caveat.}
11	Structural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.
12	Consequently, the in-domain structural F1 of 0.995 reflects an upper bound on how well these features can \emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.
13	The cross-coding-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\S\ref{sec:cmd_rep_ablation}).
14	A human-annotated gold set provides the definitive non-circular evaluation (\S\ref{sec:gold_set}).
15	
16	%-------------------------------------------------------------------
17	\subsection{Experimental Setup}
18	\label{sec:setup}
19	
20	\paragraph{Datasets.}
21	We extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.
22	\textbf{SWE-Agent} trajectories from SWE-bench \citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\%.
23	\textbf{OpenHands} (OH) trajectories \citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 20.9\%.
24	Silver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).
25	Train/validation/test splits are constructed at the trajectory level (by SWE-bench instance ID, 70/15/15\%), ensuring no windows from the same task appear across splits.
26	Unless stated otherwise, evaluation uses the conf${\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.
27	
28	\begin{table}[t]
29	\centering
30	\small
31	\begin{tabular}{llrrc}
32	\toprule
33	\textbf{Agent} & \textbf{Source} & \textbf{Windows} & \textbf{Stag\,\%} & \textbf{Conf${\geq}$2} \\
34	\midrule
35	SWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\
36	OpenHands & CodeAct   & 150,652 & 20.9 & 43,376 \\
37	\bottomrule
38	\end{tabular}
39	\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}
40	\label{tab:dataset_stats}
41	\end{table}
42	
43	\paragraph{Detection methods.}
44	(1)~\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).
45	(2)~\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \citep{cho2014gru} with attention \citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.
46	(3)~\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.
47	(4)~\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\$11.66 API cost for the SWE test set).
48	(5)~\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.
49	
50	\paragraph{Metrics.}
51	Macro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\textsubscript{stag}) and progress (F1\textsubscript{prog}).
52	
53	%-------------------------------------------------------------------
54	\subsection{Main Results}
55	\label{sec:main_results}
56	
57	Table~\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\geq}$2 test set and cross-coding-agent transfer to OpenHands.
58	
59	\begin{table*}[t]
60	\centering
61	\small
62	\begin{tabular}{l ccc cc}
63	\toprule
64	& \multicolumn{3}{c}{\textbf{SWE-Agent In-Domain} (conf${\geq}$2)} & \multicolumn{2}{c}{\textbf{OpenHands Transfer}} \\
65	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
66	\textbf{Method} & Macro-F1 & F1\textsubscript{stag} & F1\textsubscript{prog} & All & Conf${\geq}$2 \\
67	\midrule
68	Structural RF$^\dagger$       & \textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \textbf{0.9959} \\
69	Structural GB$^\dagger$       & \textbf{0.9951} & 0.9928 & 0.9974 & \textbf{0.9674} & \underline{0.9918} \\
70	Structural LR$^\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\
71	ProgressProbe (GRU)           & \underline{0.9055} & 0.8593 & 0.9518 & 0.598$^a$ & 0.598$^a$ \\
72	\quad + full OH fine-tune      & ---    & ---    & ---    & 0.976$^b$ & 0.976$^b$ \\
73	Mean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\
74	LLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\
75	Cosine Similarity             & 0.5606 & ---    & ---    & 0.447  & 0.393 \\
76	\bottomrule
77	\end{tabular}
78	\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-coding-agent transfer to OpenHands. $^\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). $^a$Probe zero-shot transfer is evaluated on the standard 15\% test split ($N{=}6{,}122$); structural models are evaluated on all OH windows ($N{=}150{,}652$) and the conf${\geq}$2 subset ($N{=}43{,}376$). The structural conf${\geq}$2 numbers provide the most comparable evaluation scope. Probe macro-F1 is identical on all-windows and conf${\geq}$2 subsets (0.598 to three decimal places). For reference, probe zero-shot on the full conf${\geq}$2 set (all 43,376 windows, not just the test split) yields 0.581 macro-F1, consistent with the test-split estimate. $^b$Probe fine-tuned macro-F1 confirmed on conf${\geq}$2 via paired bootstrap with GB ($p{<}0.001$); all-windows value from the same model. Best in \textbf{bold}, second-best \underline{underlined}.}
79	\label{tab:main_results}
80	\end{table*}
81	
82	In-domain, structural RF achieves 0.995 macro-F1, exceeding the GRU probe by 8.96\,pp.
83	However, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.
84	The more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.
85	The zero-shot LLM judge (0.663) underperforms all learned methods despite substantially higher cost (\$11.66 per test set).
86	Extended evaluation with few-shot prompting and an alternative model (Appendix~\ref{sec:llm_extended}) yields a best LLM macro-F1 of 0.751 (SWE-Agent in-domain), still 21.6\,pp below structural cross-coding-agent transfer (0.967 on OpenHands)---the structural advantage holds even comparing the LLM's easier in-domain setting against the structural model's harder cross-coding-agent regime.
87	
88	%-------------------------------------------------------------------
89	\subsection{Cross-Agent Transfer}
90	\label{sec:cross_agent}
91	
92	Table~\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.
93	Structural GB transfers best, achieving 0.967 macro-F1 on all OH windows.
94	RF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.
95	Both structural models exceed 0.99 macro-F1 on conf${\geq}$2 OH windows (GB 0.992, RF 0.996), where label noise is lower.
96	
97	The probe's zero-shot transfer (0.598) lags structural GB by 36.9\,pp---cosine similarity collapses further to 0.447---but full OH fine-tuning closes this gap dramatically: the fine-tuned probe reaches 0.976 macro-F1 on all OH windows, surpassing structural GB (0.967) by 0.9\,pp (\S\ref{sec:cmd_rep_ablation}).
98	The asymmetry between structural and learned methods is thus stage-dependent: in the zero-data regime, structural features transfer naturally while learned embeddings do not (+36.9\,pp gap); with target-domain fine-tuning, the probe surpasses structural features (+0.9\,pp on all windows).
99	The practical implication is a deployment trade-off: use structural features when no labeled data is available; invest in probe fine-tuning when annotation budget permits.
100	
101	\paragraph{Multi-seed stability.}
102	Structural RF: $0.995{\pm}0.000$ in-domain (3 seeds, zero variance); GB cross-coding-agent: $0.968{\pm}0.002$.
103	The probe shows higher variance: $0.919{\pm}0.011$, though all seeds exceed 0.90.
104	
105	%-------------------------------------------------------------------
106	\subsection{Robustness Analysis}
107	\label{sec:robustness}
108	
109	\paragraph{Encoder ablation.}
110	Replacing Qwen3-0.6B with BGE-M3 \citep{chen2024bgem3} or E5-large-v2 \citep{wang2024e5} yields probe macro-F1 of 0.941 and 0.936, respectively (vs.\ 0.906 for Qwen3).
111	All encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\ref{tab:encoder_ablation}.
112	We use Qwen3-Embedding-0.6B (released May 2025) as our primary encoder for recency; BGE-M3 achieves higher F1 (0.941 vs.\ 0.906), confirming encoder-agnostic findings.
113	
114	\paragraph{Architecture ablation.}
115	Replacing the GRU with a Transformer encoder (2-layer, 4-head, same hidden dimension) yields 0.934 macro-F1 vs.\ 0.933 for GRU ($+$0.18\,pp, not significant under paired bootstrap $p{=}0.82$).
116	The two architectures are functionally equivalent on 5-step windows, suggesting that the sequential inductive bias of the GRU provides no advantage at this window length.
117	
118	\paragraph{Window size.}
119	$k{=}5$ is optimal (0.931 macro-F1); $k{=}3$ drops 5.9\,pp and $k{=}7$ drops 1.8\,pp.
120	Shorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.
121	The 0.931 figure differs from the main table's 0.906 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.
122	Details in Appendix Table~\ref{tab:window_ablation}.
123	
124	\paragraph{Data scaling.}
125	Figure~\ref{fig:data_scaling} compares data efficiency across methods.
126	Structural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\% training data, fully saturating by 50\%.
127	The probe scales monotonically from 0.805 (10\%) to 0.906 (100\%) but has not plateaued---a 10.1\,pp drop that is roughly 20$\times$ the structural degradation (${\sim}$0.4--0.8\,pp).
128	This data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.
129	
130	\begin{figure}[t]
131	\centering
132	\includegraphics[width=\columnwidth]{../../figures/paper/fig_data_scaling.pdf}
133	\caption{Macro-F1 vs.\ training data fraction. Structural classifiers (RF, GB) saturate by 50\% data; the probe scales monotonically but remains 9\,pp below at 100\%.}
134	\label{fig:data_scaling}
135	\end{figure}
136	
137	%-------------------------------------------------------------------
138	\subsection{Labeling Function Temporal Dynamics}
139	\label{sec:lf_temporal}
140	
141	We analyze when each LF first fires relative to the onset of stagnation episodes (Table~\ref{tab:lf_temporal}, Figure~\ref{fig:lf_temporal}).
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\begin{tabular}{lrrrr}
147	\toprule
148	\textbf{LF} & \textbf{Lag} & \textbf{Lead\,\%} & \textbf{Conc.\,\%} & \textbf{Lag\,\%} \\
149	\midrule
150	cmd\_rep      & $-1.87$ & 36.1 & --- & --- \\
151	file\_diff    & $-1.20$ & 17.1 & --- & --- \\
152	outcome\_bp   & $+6.70$ & ---  & --- & 48.4 \\
153	\bottomrule
154	\end{tabular}
155	\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}
156	\label{tab:lf_temporal}
157	\end{table}
158	
159	The three LFs occupy distinct temporal niches.
160	Command repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.
161	File diff is near-concurrent ($-1.20$ steps).
162	Outcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.
163	
164	All pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\_rep vs.\ file\_diff $p{=}1.44{\times}10^{-26}$, cmd\_rep vs.\ outcome\_bp $p{=}6.67{\times}10^{-39}$, file\_diff vs.\ outcome\_bp $p{=}3.47{\times}10^{-47}$).
165	
166	\paragraph{Cross-agent reversal.}
167	On OpenHands, cmd\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).
168	Under corrected OH labels (\S\ref{sec:cmd_rep_ablation}), cmd\_rep fires on only 5.4\% of OH windows with 97.9\% precision---a high-precision, low-recall detector whose temporal role differs fundamentally from its SWE-Agent behavior.
169	
170	\begin{figure}[t]
171	\centering
172	\includegraphics[width=\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}
173	\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\_rep leads ($-1.87$ steps), file\_diff is near-concurrent ($-1.20$), outcome\_bp lags ($+6.70$). Inset: OH reversal where cmd\_rep becomes lagging.}
174	\label{fig:lf_temporal}
175	\end{figure}
176	
177	%-------------------------------------------------------------------
178	\subsection{Label Quality and cmd\_rep Coverage}
179	\label{sec:cmd_rep_ablation}
180	
181	A label quality audit revealed that the OH embedding vectors used for silver labeling contained a version mismatch, causing systematic label errors.
182	After correction, the OH stagnation rate on the embedding subset (143,057 windows; short trajectories excluded) shifted from 6.56\% to 21.4\%, with 21,898 window labels flipping.
183	This section quantifies how label quality and cmd\_rep coverage jointly affect probe transfer.
184	
185	\paragraph{Label correction impact on probe transfer.}
186	With corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.976 (previously 0.7512 under corrupted labels).
187	The improvement is most dramatic at low data fractions: 5\% fine-tuning reaches 0.850, exceeding the old 50\% result (0.69) by 16.0\,pp.
188	The probe converges rapidly: at 50\% OH data it reaches 0.968, essentially matching structural GB (0.967) and demonstrating that the structural advantage is specific to zero-data deployment (full curve in Appendix Table~\ref{tab:cross_agent_cmdrep}).
189	Label quality, not model capacity, was the transfer bottleneck.
190	
191	\paragraph{Prevalence-matched ablation.}
192	To isolate cmd\_rep's contribution, we compare 3-LF and 2-LF (no cmd\_rep) models on the same test set with matched class prevalence.
193	
194	\begin{table}[t]
195	\centering
196	\small
197	\begin{tabular}{lccc}
198	\toprule
199	\textbf{LF Config} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} \\
200	\midrule
201	3-LF (w/ cmd\_rep) & \textbf{0.9763} & 0.9600 & 0.9930 \\
202	2-LF (no cmd\_rep) & 0.6822 & 0.4810 & 0.8840 \\
203	\midrule
204	$\Delta$ & $-29.4$\,pp & $-47.9$\,pp & $-10.9$\,pp \\
205	\bottomrule
206	\end{tabular}
207	\caption{Prevalence-matched ablation on the same OH test set ($N{=}6{,}122$, stag rate 19.3\%). Removing cmd\_rep drops macro-F1 by 29.4\,pp (McNemar $\chi^2{=}1551$, $p{\approx}0$).}
208	\label{tab:cmd_rep_ablation}
209	\end{table}
210	
211	Removing cmd\_rep drops macro-F1 by 29.4\,pp (McNemar $\chi^2{=}1551$, $p{\approx}0$), a statistically significant degradation driven primarily by stagnation recall ($-47.9$\,pp F1\textsubscript{stag}).
212	
213	\paragraph{Coverage, not label quality, explains the gap.}
214	The 29.4\,pp drop is not caused by cmd\_rep improving label accuracy.
215	After correction, cmd\_rep fires on only 5.39\% of OH windows (down from the previously reported 92.2\% under corrupted embeddings) with 97.91\% precision---a high-precision, low-recall signal.
216	On the 4,070 windows where both 2-LF and 3-LF labels are defined, the two configurations agree on 100\% of labels: cmd\_rep does not change any label where the other two LFs already vote.
217	Its contribution is purely \emph{coverage}: including cmd\_rep expands the training set from ${\sim}$4K to ${\sim}$43K windows (a ${\sim}$10$\times$ increase).
218	The 2-LF model's low F1 reflects data volume collapse---too few training examples to learn the stagnation distribution---rather than label corruption.
219	
220	\paragraph{Implications for weak supervision.}
221	These results reframe how labeling functions contribute to weak supervision pipelines.
222	A high-precision, low-recall LF like cmd\_rep may appear redundant when its labels are a subset of the majority vote, yet removing it causes training data to collapse by an order of magnitude.
223	In prevalence-matched evaluation, this data reduction manifests as a 29.4\,pp F1 drop.
224	The core contribution of such LFs is coverage provision, not label refinement: they extend the labelable portion of the input space rather than correcting other LFs' errors.
225	
226	%-------------------------------------------------------------------
227	\subsection{Temporal Label Models}
228	\label{sec:temporal_label_models}
229	
230	We investigate whether any label aggregation method---temporal or generative---improves over majority vote (MV).
231	Table~\ref{tab:temporal_models} compares five label models: three temporal (TWV, Lag-HMM, HMM) \citep{ratner2017snorkel,safranchik2020linkedhmm} and two generative i.i.d.\ models (FlyingSquid \citep{fu2020flyingsquid}, Snorkel MeTaL \citep{ratner2019snorkelmetal}).
232	
233	\begin{table}[t]
234	\centering
235	\small
236	\begin{tabular}{lcccc}
237	\toprule
238	\textbf{Method} & \textbf{MV Agr.} & \textbf{Conf${\geq}$2 F1} & \textbf{$\Delta$ vs MV} & \textbf{Probe F1$^\ddagger$} \\
239	\midrule
240	MV (baseline) & 1.000 & 0.8946$^\ast$ & --- & 0.8468 \\
241	\midrule
242	\multicolumn{5}{l}{\emph{Temporal}} \\
243	TWV ($\sigma{=}2$) & 0.885 & \textbf{0.9003} & $+$0.6\,pp & 0.8211 \\
244	Lag-HMM & 0.820 & 0.8936 & $-$0.1\,pp & --- \\
245	HMM & 0.685 & 0.7502 & $-$14.4\,pp & 0.6564 \\
246	\midrule
247	\multicolumn{5}{l}{\emph{Generative (i.i.d.)}} \\
248	FlyingSquid & 0.820 & 0.7820 & $-$11.3\,pp & --- \\
249	Snorkel MeTaL & 0.423 & 0.2580 & $-$63.6\,pp & --- \\
250	\bottomrule
251	\end{tabular}
252	\caption{Label model comparison. Conf${\geq}$2 F1: each model's labels evaluated against MV labels on conf${\geq}$2 windows. $^\ast$MV conf${\geq}$2 F1 (0.8946) reflects downstream probe performance when trained on MV labels, not self-agreement (which would be 1.0). $^\ddagger$Downstream probe trained on each method's full labels, evaluated on the SWE-Agent test set ($N{=}8{,}101$) against MV labels. ``---'' = not evaluated downstream. No model consistently improves over MV.}
253	\label{tab:temporal_models}
254	\end{table}
255	
256	\paragraph{Temporal models.}
257	TWV achieves the highest conf${\geq}$2 F1 (0.900, $+$0.6\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.821 vs.\ 0.847 for MV-trained ($-$2.57\,pp).
258	TWV flips 14.1\% of conf${=}$1 labels, introducing noise that hurts probe training.
259	The Gaussian kernel bandwidth $\sigma$ is critical: $\sigma{=}2$ is optimal; $\sigma{=}1$ drops to 0.811 and $\sigma{=}5$ to 0.808, making TWV impractical as a drop-in MV replacement.
260	HMM overpredicts stagnation (29,176 vs.\ 25,633 progress windows), degrading conf${\geq}$2 F1 by 14.4\,pp and downstream performance to 0.656.
261	Lag-HMM closely tracks MV ($-$0.1\,pp) despite explicitly modeling temporal offsets.
262	
263	\paragraph{Generative (i.i.d.) models.}
264	FlyingSquid \citep{fu2020flyingsquid}, a closed-form triplet-based model, drops 11.3\,pp below MV.
265	On the full dataset, agreement with MV is 82\%; all divergent labels flip progress$\to$stagnation, introducing systematic stagnation bias.
266	Snorkel MeTaL \citep{ratner2019snorkelmetal} fails catastrophically ($-$63.6\,pp), with only 42.3\% MV agreement.
267	Both models assume conditional independence among LFs---an assumption violated by the shared behavioral signals underlying our three LFs---and lack the sequential structure to recover from this misspecification.
268	
269	\paragraph{Root cause: insufficient inter-LF conflict.}
270	These results constitute a negative finding: five label models spanning temporal aggregation and generative modeling all fail to improve over majority vote.
271	Three binary LFs produce at most $2^3{=}8$ voting patterns; conf${\geq}$2 windows dominate the training set, leaving insufficient ambiguity for any aggregation method to exploit.
272	The bottleneck is LF quantity, not aggregation sophistication---scaling to ${>}$10 LFs with higher disagreement rates is needed before advanced label models can add value.
273	In the current 3-LF, low-conflict regime (conf${\geq}$2 agreement rate 95.1\%), temporal alignment gains are offset by noise introduction.
274	With 5--10 LFs generating higher disagreement rates, temporal models may add value---this remains an open question.
275	
276	%-------------------------------------------------------------------
277	\subsection{Gold Set Validation}
278	\label{sec:gold_set}
279	We construct a stratified gold set of 650 windows for non-circular evaluation.
280	Windows are sampled along two axes: \emph{confidence} (balanced across conf${=}1$, conf${=}2$, and conf${=}3$ strata to capture the full ambiguity spectrum) and \emph{trajectory position} (early, middle, and late thirds, since stagnation dynamics differ across trajectory phases; \S\ref{sec:error_analysis}).
281	
282	\paragraph{Annotation protocol.}
283	Two annotators independently label each window as stagnation or progress using an operational definition: \emph{a window is stagnation if the agent's actions within it do not make meaningful progress toward solving the task, regardless of whether the actions appear diverse or purposeful}.
284	Annotators receive the $k{=}5$ action descriptions with full command outputs and file diffs, but \emph{not} the task outcome (resolved/unresolved), preventing information leakage from $\lambda_3$.
285	Disagreements are resolved by a third annotator.
286	Gold validation results are pending; in the interim, cross-coding-agent transfer (\S\ref{sec:cross_agent}) and the feature overlap ablation (\S\ref{sec:feature_overlap}) provide non-circular evidence that structural features encode genuine stagnation signals rather than LF artifacts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "65215f6a-63c8-4a24-ab62-6d7fe49e7f6f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe organize results around three questions:\n(1)~which method best detects stagnation across deployment scenarios? (\\S\\ref{sec:main_results}--\\S\\ref{sec:robustness});\n(2)~what drives label quality and cross-coding-agent transfer bottlenecks? (\\S\\ref{sec:lf_temporal}--\\S\\ref{sec:cmd_rep_ablation});\n(3)~can temporal structure in LFs improve labels? (\\S\\ref{sec:temporal_label_models}).\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.995 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-coding-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 20.9\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nTrain/validation/test splits are constructed at the trajectory level (by SWE-bench instance ID, 70/15/15\\%), ensuring no windows from the same task appear across splits.\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 20.9 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-coding-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9918} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.598$^a$ & 0.598$^a$ \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.976$^b$ & 0.976$^b$ \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & 0.447  & 0.393 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-coding-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). $^a$Probe zero-shot transfer is evaluated on the standard 15\\% test split ($N{=}6{,}122$); structural models are evaluated on all OH windows ($N{=}150{,}652$) and the conf${\\geq}$2 subset ($N{=}43{,}376$). The structural conf${\\geq}$2 numbers provide the most comparable evaluation scope. Probe macro-F1 is identical on all-windows and conf${\\geq}$2 subsets (0.598 to three decimal places). For reference, probe zero-shot on the full conf${\\geq}$2 set (all 43,376 windows, not just the test split) yields 0.581 macro-F1, consistent with the test-split estimate. $^b$Probe fine-tuned macro-F1 confirmed on conf${\\geq}$2 via paired bootstrap with GB ($p{<}0.001$); all-windows value from the same model. Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.995 macro-F1, exceeding the GRU probe by 8.96\\,pp.\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe zero-shot LLM judge (0.663) underperforms all learned methods despite substantially higher cost (\\$11.66 per test set).\nExtended evaluation with few-shot prompting and an alternative model (Appendix~\\ref{sec:llm_extended}) yields a best LLM macro-F1 of 0.751 (SWE-Agent in-domain), still 21.6\\,pp below structural cross-coding-agent transfer (0.967 on OpenHands)---the structural advantage holds even comparing the LLM's easier in-domain setting against the structural model's harder cross-coding-agent regime.\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows.\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models exceed 0.99 macro-F1 on conf${\\geq}$2 OH windows (GB 0.992, RF 0.996), where label noise is lower.\n\nThe probe's zero-shot transfer (0.598) lags structural GB by 36.9\\,pp---cosine similarity collapses further to 0.447---but full OH fine-tuning closes this gap dramatically: the fine-tuned probe reaches 0.976 macro-F1 on all OH windows, surpassing structural GB (0.967) by 0.9\\,pp (\\S\\ref{sec:cmd_rep_ablation}).\nThe asymmetry between structural and learned methods is thus stage-dependent: in the zero-data regime, structural features transfer naturally while learned embeddings do not (+36.9\\,pp gap); with target-domain fine-tuning, the probe surpasses structural features (+0.9\\,pp on all windows).\nThe practical implication is a deployment trade-off: use structural features when no labeled data is available; invest in probe fine-tuning when annotation budget permits.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.995{\\pm}0.000$ in-domain (3 seeds, zero variance); GB cross-coding-agent: $0.968{\\pm}0.002$.\nThe probe shows higher variance: $0.919{\\pm}0.011$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.941 and 0.936, respectively (vs.\\ 0.906 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\nWe use Qwen3-Embedding-0.6B (released May 2025) as our primary encoder for recency; BGE-M3 achieves higher F1 (0.941 vs.\\ 0.906), confirming encoder-agnostic findings.\n\n\\paragraph{Architecture ablation.}\nReplacing the GRU with a Transformer encoder (2-layer, 4-head, same hidden dimension) yields 0.934 macro-F1 vs.\\ 0.933 for GRU ($+$0.18\\,pp, not significant under paired bootstrap $p{=}0.82$).\nThe two architectures are functionally equivalent on 5-step windows, suggesting that the sequential inductive bias of the GRU provides no advantage at this window length.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.931 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nThe 0.931 figure differs from the main table's 0.906 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} compares data efficiency across methods.\nStructural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\\% training data, fully saturating by 50\\%.\nThe probe scales monotonically from 0.805 (10\\%) to 0.906 (100\\%) but has not plateaued---a 10.1\\,pp drop that is roughly 20$\\times$ the structural degradation (${\\sim}$0.4--0.8\\,pp).\nThis data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Macro-F1 vs.\\ training data fraction. Structural classifiers (RF, GB) saturate by 50\\% data; the probe scales monotonically but remains 9\\,pp below at 100\\%.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nUnder corrected OH labels (\\S\\ref{sec:cmd_rep_ablation}), cmd\\_rep fires on only 5.4\\% of OH windows with 97.9\\% precision---a high-precision, low-recall detector whose temporal role differs fundamentally from its SWE-Agent behavior.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Label Quality and cmd\\_rep Coverage}\n\\label{sec:cmd_rep_ablation}\n\nA label quality audit revealed that the OH embedding vectors used for silver labeling contained a version mismatch, causing systematic label errors.\nAfter correction, the OH stagnation rate on the embedding subset (143,057 windows; short trajectories excluded) shifted from 6.56\\% to 21.4\\%, with 21,898 window labels flipping.\nThis section quantifies how label quality and cmd\\_rep coverage jointly affect probe transfer.\n\n\\paragraph{Label correction impact on probe transfer.}\nWith corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.976 (previously 0.7512 under corrupted labels).\nThe improvement is most dramatic at low data fractions: 5\\% fine-tuning reaches 0.850, exceeding the old 50\\% result (0.69) by 16.0\\,pp.\nThe probe converges rapidly: at 50\\% OH data it reaches 0.968, essentially matching structural GB (0.967) and demonstrating that the structural advantage is specific to zero-data deployment (full curve in Appendix Table~\\ref{tab:cross_agent_cmdrep}).\nLabel quality, not model capacity, was the transfer bottleneck.\n\n\\paragraph{Prevalence-matched ablation.}\nTo isolate cmd\\_rep's contribution, we compare 3-LF and 2-LF (no cmd\\_rep) models on the same test set with matched class prevalence.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & \\textbf{0.9763} & 0.9600 & 0.9930 \\\\\n2-LF (no cmd\\_rep) & 0.6822 & 0.4810 & 0.8840 \\\\\n\\midrule\n$\\Delta$ & $-29.4$\\,pp & $-47.9$\\,pp & $-10.9$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prevalence-matched ablation on the same OH test set ($N{=}6{,}122$, stag rate 19.3\\%). Removing cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$).}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$), a statistically significant degradation driven primarily by stagnation recall ($-47.9$\\,pp F1\\textsubscript{stag}).\n\n\\paragraph{Coverage, not label quality, explains the gap.}\nThe 29.4\\,pp drop is not caused by cmd\\_rep improving label accuracy.\nAfter correction, cmd\\_rep fires on only 5.39\\% of OH windows (down from the previously reported 92.2\\% under corrupted embeddings) with 97.91\\% precision---a high-precision, low-recall signal.\nOn the 4,070 windows where both 2-LF and 3-LF labels are defined, the two configurations agree on 100\\% of labels: cmd\\_rep does not change any label where the other two LFs already vote.\nIts contribution is purely \\emph{coverage}: including cmd\\_rep expands the training set from ${\\sim}$4K to ${\\sim}$43K windows (a ${\\sim}$10$\\times$ increase).\nThe 2-LF model's low F1 reflects data volume collapse---too few training examples to learn the stagnation distribution---rather than label corruption.\n\n\\paragraph{Implications for weak supervision.}\nThese results reframe how labeling functions contribute to weak supervision pipelines.\nA high-precision, low-recall LF like cmd\\_rep may appear redundant when its labels are a subset of the majority vote, yet removing it causes training data to collapse by an order of magnitude.\nIn prevalence-matched evaluation, this data reduction manifests as a 29.4\\,pp F1 drop.\nThe core contribution of such LFs is coverage provision, not label refinement: they extend the labelable portion of the input space rather than correcting other LFs' errors.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether any label aggregation method---temporal or generative---improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares five label models: three temporal (TWV, Lag-HMM, HMM) \\citep{ratner2017snorkel,safranchik2020linkedhmm} and two generative i.i.d.\\ models (FlyingSquid \\citep{fu2020flyingsquid}, Snorkel MeTaL \\citep{ratner2019snorkelmetal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{MV Agr.} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{$\\Delta$ vs MV} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 1.000 & 0.8946$^\\ast$ & --- & 0.8468 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Temporal}} \\\\\nTWV ($\\sigma{=}2$) & 0.885 & \\textbf{0.9003} & $+$0.6\\,pp & 0.8211 \\\\\nLag-HMM & 0.820 & 0.8936 & $-$0.1\\,pp & --- \\\\\nHMM & 0.685 & 0.7502 & $-$14.4\\,pp & 0.6564 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Generative (i.i.d.)}} \\\\\nFlyingSquid & 0.820 & 0.7820 & $-$11.3\\,pp & --- \\\\\nSnorkel MeTaL & 0.423 & 0.2580 & $-$63.6\\,pp & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Label model comparison. Conf${\\geq}$2 F1: each model's labels evaluated against MV labels on conf${\\geq}$2 windows. $^\\ast$MV conf${\\geq}$2 F1 (0.8946) reflects downstream probe performance when trained on MV labels, not self-agreement (which would be 1.0). $^\\ddagger$Downstream probe trained on each method's full labels, evaluated on the SWE-Agent test set ($N{=}8{,}101$) against MV labels. ``---'' = not evaluated downstream. No model consistently improves over MV.}\n\\label{tab:temporal_models}\n\\end{table}\n\n\\paragraph{Temporal models.}\nTWV achieves the highest conf${\\geq}$2 F1 (0.900, $+$0.6\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.821 vs.\\ 0.847 for MV-trained ($-$2.57\\,pp).\nTWV flips 14.1\\% of conf${=}$1 labels, introducing noise that hurts probe training.\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal; $\\sigma{=}1$ drops to 0.811 and $\\sigma{=}5$ to 0.808, making TWV impractical as a drop-in MV replacement.\nHMM overpredicts stagnation (29,176 vs.\\ 25,633 progress windows), degrading conf${\\geq}$2 F1 by 14.4\\,pp and downstream performance to 0.656.\nLag-HMM closely tracks MV ($-$0.1\\,pp) despite explicitly modeling temporal offsets.\n\n\\paragraph{Generative (i.i.d.) models.}\nFlyingSquid \\citep{fu2020flyingsquid}, a closed-form triplet-based model, drops 11.3\\,pp below MV.\nOn the full dataset, agreement with MV is 82\\%; all divergent labels flip progress$\\to$stagnation, introducing systematic stagnation bias.\nSnorkel MeTaL \\citep{ratner2019snorkelmetal} fails catastrophically ($-$63.6\\,pp), with only 42.3\\% MV agreement.\nBoth models assume conditional independence among LFs---an assumption violated by the shared behavioral signals underlying our three LFs---and lack the sequential structure to recover from this misspecification.\n\n\\paragraph{Root cause: insufficient inter-LF conflict.}\nThese results constitute a negative finding: five label models spanning temporal aggregation and generative modeling all fail to improve over majority vote.\nThree binary LFs produce at most $2^3{=}8$ voting patterns; conf${\\geq}$2 windows dominate the training set, leaving insufficient ambiguity for any aggregation method to exploit.\nThe bottleneck is LF quantity, not aggregation sophistication---scaling to ${>}$10 LFs with higher disagreement rates is needed before advanced label models can add value.\nIn the current 3-LF, low-conflict regime (conf${\\geq}$2 agreement rate 95.1\\%), temporal alignment gains are offset by noise introduction.\nWith 5--10 LFs generating higher disagreement rates, temporal models may add value---this remains an open question.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\nWe construct a stratified gold set of 650 windows for non-circular evaluation.\nWindows are sampled along two axes: \\emph{confidence} (balanced across conf${=}1$, conf${=}2$, and conf${=}3$ strata to capture the full ambiguity spectrum) and \\emph{trajectory position} (early, middle, and late thirds, since stagnation dynamics differ across trajectory phases; \\S\\ref{sec:error_analysis}).\n\n\\paragraph{Annotation protocol.}\nTwo annotators independently label each window as stagnation or progress using an operational definition: \\emph{a window is stagnation if the agent's actions within it do not make meaningful progress toward solving the task, regardless of whether the actions appear diverse or purposeful}.\nAnnotators receive the $k{=}5$ action descriptions with full command outputs and file diffs, but \\emph{not} the task outcome (resolved/unresolved), preventing information leakage from $\\lambda_3$.\nDisagreements are resolved by a third annotator.\nGold validation results are pending; in the interim, cross-coding-agent transfer (\\S\\ref{sec:cross_agent}) and the feature overlap ablation (\\S\\ref{sec:feature_overlap}) provide non-circular evidence that structural features encode genuine stagnation signals rather than LF artifacts.",
      "numLines": 286,
      "startLine": 1,
      "totalLines": 286
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the current state. Let me analyze what needs to be done:

1. **Instance-Level Cross-Agent Isolation**: Looking at line 14 in `analysis.tex`, there's already a sentence about instance isolation: "removing 284 SWE-bench task instances (8.3% of OH test data) that appear in both training and test sets changes all cross-coding-agent macro-F1 by ${<}$0.1\,pp (Table~\ref{tab:instance_isolation})". It references `Table~\ref{tab:instance_isolation}` which doesn't seem to exist yet. 

The data is already mentioned but the table needs to be created to support this claim.

2. **Feature Overlap Ablation**: Looking at `analysis.tex` lines 18-55, there's already a full subsection `\subsection{Feature Overlap Ablation}` with Table~\ref{tab:feature_overlap}. The data matches what's provided. But the task says to add per-feature ablation data (removing cmd_rep, file_diff, outcome_bp features individually). Let me check if those are mentioned.

Looking more carefully at the task requirements:

For **Instance Isolation**:
- The mention in analysis.tex line 14 already has the key numbers (284 instances, 8.3%, <0.1pp impact), but I need to verify these numbers match the provided data and create the corresponding table.
- The table should include the SWE-bench training instances (1,386) and OH instances (3,409) with their respective F1 scores before and after isolation.

For **Feature Overlap Ablation**:
- The main table and discussion already exist in the paper.
- But I'm missing the per-feature removal ablation results that show the individual impact of removing cmd_rep, file_diff, and outcome_bp features—these need to be added to expand the analysis and show which features are most critical.

Now I need to check the introduction and conclusion to see if they reference these sections and whether they need updates to reflect the new ablation details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "d61f75fa-8906-45d0-96e4-6d4d32c366fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZKGXoZKP4VDG8huW2y7VP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11389,
      "cache_read_input_tokens": 24190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11389
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

_source line 10_

Now let me check the introduction, conclusion, and appendix for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "ad96a92a-1f40-4e32-b459-a9a92421b5dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZKGXoZKP4VDG8huW2y7VP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11389,
      "cache_read_input_tokens": 24190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11389
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_011tUqA9M3omXcQa8t1yVZxh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "a69e622f-80c1-4180-9a9c-ba8f4e01d77c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZKGXoZKP4VDG8huW2y7VP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11389,
      "cache_read_input_tokens": 24190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11389
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

_source line 12 · 2026-05-15T04:26:34.648Z_

<details><summary>↩ Tool result · `toolu_011tUqA9M3omXcQa8t1yVZxh`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on multi-file codebases across dozens of editing rounds \citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.
5	As these deployments scale, a critical failure mode has emerged that is qualitatively different from crashes or syntax errors: the agent \emph{stagnates}---continuing to produce actions that appear purposeful while making no meaningful progress toward the task goal.
6	\citet{orlanski2026slopcodebench} document this degradation on SlopCodeBench, recording verbosity increases of 77\% and quality drops of 75.5\% in long-horizon coding trajectories, with no agent fully solving any benchmark problem end-to-end.
7	Crucially, the dominant failure pattern is not simple repetition but what we term \emph{semantic stagnation}: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.
8	This ``looks busy but going in circles'' pattern defeats existing monitoring tools, because surface-level action diversity masks the underlying lack of progress.
9	We observe this phenomenon at scale: across trajectories from two architecturally distinct agents---SWE-Agent \citep{yang2024sweagent} and OpenHands \citep{wang2025openhands}---on SWE-bench tasks \citep{jimenez2024swebench}, 28.5\% and 20.9\% of sliding windows exhibit stagnation under our silver labeling scheme, respectively, confirming that the failure mode is both prevalent and highly agent-dependent.
10	
11	Existing approaches address aspects of this problem but fall short in three ways.
12	First, \emph{repetition detectors} such as cycle detection \citep{george2025cycledetection} and SpecRA \citep{pipis2025reasoningloop} identify structural repetition---exact or near-exact loops in action sequences---but by design miss semantically diverse stagnation where the agent varies its surface behavior while remaining functionally stuck.
13	Second, \emph{step-level scoring} via process reward models \citep{xi2025agentprm} evaluates individual actions in isolation, discarding the window-level temporal dynamics that distinguish transient setbacks from sustained stagnation---a distinction that requires reasoning over sequences of consecutive actions \citep{chen2025monitoring}.
14	A sequence of failed commands followed by a strategy switch, for instance, carries different diagnostic information than the same commands evaluated independently.
15	Third, \emph{LLM self-evaluation} \citep{shinn2023reflexion} is both expensive and fundamentally limited by the stuck model's own judgment; our LLM-as-judge baseline achieves only 0.663 macro-F1 at \$11.66 per test set, well below lightweight feature-based alternatives.
16	More fundamentally, none of these approaches asks the prior question: \emph{what signals actually carry stagnation information?}
17	No systematic study has investigated whether detecting subtle agent failure requires sophisticated semantic understanding or whether simpler structural patterns suffice.
18	
19	We address this question through a systematic empirical study (Figure~\ref{fig:pipeline}).
20	Using a weak supervision framework \citep{ratner2016dataprogramming,ratner2017snorkel}, we construct silver-labeled datasets from over 205K windows spanning SWE-Agent (54,809 windows, 28.5\% silver-labeled stagnation) and OpenHands (150,652 windows, 20.9\% stagnation).
21	Three labeling functions provide complementary noisy votes: command repetition ($\lambda_1$) targets repetitive behavior, file diff delta ($\lambda_2$) targets output productivity, and outcome backpropagation ($\lambda_3$) propagates task-level outcomes backward through the trajectory.
22	Majority vote aggregation produces window-level binary labels with confidence scores.
23	Our window-level formulation ($k{=}5$ consecutive actions, stride 1) captures short-range temporal patterns---such as repeated failures followed by strategy changes---that step-level approaches cannot express, while providing the granularity to pinpoint \emph{when} stagnation begins and ends within a trajectory, enabling targeted interventions.
24	Against these silver labels, we systematically compare hand-crafted structural features, a neural embedding probe, and an LLM-as-judge baseline.
25	
26	Our study yields three principal findings.
27	
28	\textbf{Finding 1: Structural features enable effective zero-data cross-coding-agent transfer, but probes surpass them with fine-tuning.}
29	Thirty hand-crafted features---command repetition rates, file operation counts, edit distances---achieve 0.995 macro-F1 in-domain (Random Forest) and 0.967 cross-coding-agent macro-F1 (Gradient Boosting, SWE-Agent $\to$ OpenHands) with zero target data, outperforming the GRU embedding probe \citep{cho2014gru} zero-shot by 36.9\,pp (0.598 on OpenHands, near chance) and the best LLM judge (in-domain) by 21.6\,pp.
30	However, with 100\% target fine-tuning the probe reaches 0.976 macro-F1, surpassing the structural baseline (0.967)---demonstrating that probe representations recover cross-coding-agent generalization with sufficient adaptation data.
31	We note that in-domain evaluation uses silver labels (\S\ref{sec:circular}); cross-coding-agent transfer and a pending gold set (\S\ref{sec:gold_set}) provide non-circular validation.
32	The structural advantage is encoder-agnostic: three embedding backbones \citep{zhang2025qwen3embedding} all yield probe F1 above 0.90, confirming that the probe's temporal architecture rather than a specific pretrained encoder drives performance.
33	The in-domain score of 0.995 reflects circular evaluation---structural features overlap with LF inputs---but the cross-coding-agent score of 0.967, where models trained on one agent's LF distribution are tested on another with substantially different firing patterns, breaks this circularity.
34	A feature overlap ablation (\S\ref{sec:feature_overlap}) confirms that the 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1---exceeding the full model by 1.0\,pp---while 19 residual features collapse to 0.566: the features that generalize encode universal stagnation signals, and their LF alignment reflects correct LF design rather than circularity.
35	This finding challenges the prevailing intuition that detecting subtle agent failures requires complex language understanding, and suggests that lightweight structural monitoring---no GPU, under 5\,ms per window---may be more practical than neural or LLM-based approaches for real-time agent oversight.
36	
37	\textbf{Finding 2: Label quality, not LF selection, is the dominant cross-coding-agent transfer bottleneck.}
38	Labeling functions exhibit systematic temporal dynamics that reverse across agents: command repetition ($\lambda_1$) leads stagnation onset on SWE-Agent by $-1.87$ steps but lags on OpenHands by $+3.32$ steps.
39	A label quality audit reveals that fixing OH label version bias---correcting stagnation rate from 6.56\% to 21.4\%---improves 5\% fine-tuning F1 from 0.570 (under previous label version) to 0.850.
40	Prevalence-matched ablation shows that $\lambda_1$'s core value is coverage ($-29.4$\,pp when removed, $p \approx 0$), not label precision: it fires on only 5.39\% of OH windows with precision 97.91\% (FP rate 2.3\%).
41	
42	\textbf{Finding 3: No label model improves over majority vote.}
43	Five label models---three temporal (TWV, HMM \citep{safranchik2020linkedhmm}, lag-aware HMM) and two generative (FlyingSquid \citep{fu2020flyingsquid}, Snorkel MeTaL \citep{ratner2019snorkelmetal})---all fail to surpass majority vote on downstream detection.
44	TWV achieves marginally higher self-evaluated F1 but degrades downstream probe performance by 2.57\,pp; Snorkel MeTaL collapses catastrophically ($-$63.6\,pp).
45	The bottleneck is LF quantity, not aggregation sophistication: three binary LFs produce too little inter-LF conflict for any method to exploit.
46	
47	Our contributions are:
48	\begin{enumerate}
49	    \item \textbf{Weak supervision methodology for agent monitoring.} We design a silver-labeling pipeline (3 LFs + majority vote) over 205K+ windows from two coding agents, enabling systematic comparison of detection methods without manual annotation.
50	    \item \textbf{Label quality as transfer bottleneck.} We show that labeling functions exhibit agent-specific temporal reversals and that fixing label version bias (stag rate 6.56\%$\to$21.4\% on the embedding subset) is the dominant factor for cross-coding-agent transfer, informing future weak-supervision design on sequential agent data.
51	    \item \textbf{Label model negative finding.} We show that five label models---three temporal and two generative---fail to improve over majority vote for downstream detection. The bottleneck is LF quantity, not aggregation method: the 3-LF regime produces insufficient inter-LF conflict for any approach to add value.
52	    \item \textbf{Deployment-regime trade-off.} In zero-data settings, 30 structural features outperform the neural probe by 36.9\,pp and the best LLM judge (in-domain) by 21.6\,pp on silver labels (no GPU, ${<}$5\,ms per window). With target-agent fine-tuning, the probe surpasses structural features (0.976 vs.\ 0.967 macro-F1), delineating when structural monitoring suffices and when fine-tuning is warranted.
53	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "776fea60-d25f-47a0-9bad-19e3d00d09c2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLLM agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on multi-file codebases across dozens of editing rounds \\citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.\nAs these deployments scale, a critical failure mode has emerged that is qualitatively different from crashes or syntax errors: the agent \\emph{stagnates}---continuing to produce actions that appear purposeful while making no meaningful progress toward the task goal.\n\\citet{orlanski2026slopcodebench} document this degradation on SlopCodeBench, recording verbosity increases of 77\\% and quality drops of 75.5\\% in long-horizon coding trajectories, with no agent fully solving any benchmark problem end-to-end.\nCrucially, the dominant failure pattern is not simple repetition but what we term \\emph{semantic stagnation}: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.\nThis ``looks busy but going in circles'' pattern defeats existing monitoring tools, because surface-level action diversity masks the underlying lack of progress.\nWe observe this phenomenon at scale: across trajectories from two architecturally distinct agents---SWE-Agent \\citep{yang2024sweagent} and OpenHands \\citep{wang2025openhands}---on SWE-bench tasks \\citep{jimenez2024swebench}, 28.5\\% and 20.9\\% of sliding windows exhibit stagnation under our silver labeling scheme, respectively, confirming that the failure mode is both prevalent and highly agent-dependent.\n\nExisting approaches address aspects of this problem but fall short in three ways.\nFirst, \\emph{repetition detectors} such as cycle detection \\citep{george2025cycledetection} and SpecRA \\citep{pipis2025reasoningloop} identify structural repetition---exact or near-exact loops in action sequences---but by design miss semantically diverse stagnation where the agent varies its surface behavior while remaining functionally stuck.\nSecond, \\emph{step-level scoring} via process reward models \\citep{xi2025agentprm} evaluates individual actions in isolation, discarding the window-level temporal dynamics that distinguish transient setbacks from sustained stagnation---a distinction that requires reasoning over sequences of consecutive actions \\citep{chen2025monitoring}.\nA sequence of failed commands followed by a strategy switch, for instance, carries different diagnostic information than the same commands evaluated independently.\nThird, \\emph{LLM self-evaluation} \\citep{shinn2023reflexion} is both expensive and fundamentally limited by the stuck model's own judgment; our LLM-as-judge baseline achieves only 0.663 macro-F1 at \\$11.66 per test set, well below lightweight feature-based alternatives.\nMore fundamentally, none of these approaches asks the prior question: \\emph{what signals actually carry stagnation information?}\nNo systematic study has investigated whether detecting subtle agent failure requires sophisticated semantic understanding or whether simpler structural patterns suffice.\n\nWe address this question through a systematic empirical study (Figure~\\ref{fig:pipeline}).\nUsing a weak supervision framework \\citep{ratner2016dataprogramming,ratner2017snorkel}, we construct silver-labeled datasets from over 205K windows spanning SWE-Agent (54,809 windows, 28.5\\% silver-labeled stagnation) and OpenHands (150,652 windows, 20.9\\% stagnation).\nThree labeling functions provide complementary noisy votes: command repetition ($\\lambda_1$) targets repetitive behavior, file diff delta ($\\lambda_2$) targets output productivity, and outcome backpropagation ($\\lambda_3$) propagates task-level outcomes backward through the trajectory.\nMajority vote aggregation produces window-level binary labels with confidence scores.\nOur window-level formulation ($k{=}5$ consecutive actions, stride 1) captures short-range temporal patterns---such as repeated failures followed by strategy changes---that step-level approaches cannot express, while providing the granularity to pinpoint \\emph{when} stagnation begins and ends within a trajectory, enabling targeted interventions.\nAgainst these silver labels, we systematically compare hand-crafted structural features, a neural embedding probe, and an LLM-as-judge baseline.\n\nOur study yields three principal findings.\n\n\\textbf{Finding 1: Structural features enable effective zero-data cross-coding-agent transfer, but probes surpass them with fine-tuning.}\nThirty hand-crafted features---command repetition rates, file operation counts, edit distances---achieve 0.995 macro-F1 in-domain (Random Forest) and 0.967 cross-coding-agent macro-F1 (Gradient Boosting, SWE-Agent $\\to$ OpenHands) with zero target data, outperforming the GRU embedding probe \\citep{cho2014gru} zero-shot by 36.9\\,pp (0.598 on OpenHands, near chance) and the best LLM judge (in-domain) by 21.6\\,pp.\nHowever, with 100\\% target fine-tuning the probe reaches 0.976 macro-F1, surpassing the structural baseline (0.967)---demonstrating that probe representations recover cross-coding-agent generalization with sufficient adaptation data.\nWe note that in-domain evaluation uses silver labels (\\S\\ref{sec:circular}); cross-coding-agent transfer and a pending gold set (\\S\\ref{sec:gold_set}) provide non-circular validation.\nThe structural advantage is encoder-agnostic: three embedding backbones \\citep{zhang2025qwen3embedding} all yield probe F1 above 0.90, confirming that the probe's temporal architecture rather than a specific pretrained encoder drives performance.\nThe in-domain score of 0.995 reflects circular evaluation---structural features overlap with LF inputs---but the cross-coding-agent score of 0.967, where models trained on one agent's LF distribution are tested on another with substantially different firing patterns, breaks this circularity.\nA feature overlap ablation (\\S\\ref{sec:feature_overlap}) confirms that the 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1---exceeding the full model by 1.0\\,pp---while 19 residual features collapse to 0.566: the features that generalize encode universal stagnation signals, and their LF alignment reflects correct LF design rather than circularity.\nThis finding challenges the prevailing intuition that detecting subtle agent failures requires complex language understanding, and suggests that lightweight structural monitoring---no GPU, under 5\\,ms per window---may be more practical than neural or LLM-based approaches for real-time agent oversight.\n\n\\textbf{Finding 2: Label quality, not LF selection, is the dominant cross-coding-agent transfer bottleneck.}\nLabeling functions exhibit systematic temporal dynamics that reverse across agents: command repetition ($\\lambda_1$) leads stagnation onset on SWE-Agent by $-1.87$ steps but lags on OpenHands by $+3.32$ steps.\nA label quality audit reveals that fixing OH label version bias---correcting stagnation rate from 6.56\\% to 21.4\\%---improves 5\\% fine-tuning F1 from 0.570 (under previous label version) to 0.850.\nPrevalence-matched ablation shows that $\\lambda_1$'s core value is coverage ($-29.4$\\,pp when removed, $p \\approx 0$), not label precision: it fires on only 5.39\\% of OH windows with precision 97.91\\% (FP rate 2.3\\%).\n\n\\textbf{Finding 3: No label model improves over majority vote.}\nFive label models---three temporal (TWV, HMM \\citep{safranchik2020linkedhmm}, lag-aware HMM) and two generative (FlyingSquid \\citep{fu2020flyingsquid}, Snorkel MeTaL \\citep{ratner2019snorkelmetal})---all fail to surpass majority vote on downstream detection.\nTWV achieves marginally higher self-evaluated F1 but degrades downstream probe performance by 2.57\\,pp; Snorkel MeTaL collapses catastrophically ($-$63.6\\,pp).\nThe bottleneck is LF quantity, not aggregation sophistication: three binary LFs produce too little inter-LF conflict for any method to exploit.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Weak supervision methodology for agent monitoring.} We design a silver-labeling pipeline (3 LFs + majority vote) over 205K+ windows from two coding agents, enabling systematic comparison of detection methods without manual annotation.\n    \\item \\textbf{Label quality as transfer bottleneck.} We show that labeling functions exhibit agent-specific temporal reversals and that fixing label version bias (stag rate 6.56\\%$\\to$21.4\\% on the embedding subset) is the dominant factor for cross-coding-agent transfer, informing future weak-supervision design on sequential agent data.\n    \\item \\textbf{Label model negative finding.} We show that five label models---three temporal and two generative---fail to improve over majority vote for downstream detection. The bottleneck is LF quantity, not aggregation method: the 3-LF regime produces insufficient inter-LF conflict for any approach to add value.\n    \\item \\textbf{Deployment-regime trade-off.} In zero-data settings, 30 structural features outperform the neural probe by 36.9\\,pp and the best LLM judge (in-domain) by 21.6\\,pp on silver labels (no GPU, ${<}$5\\,ms per window). With target-agent fine-tuning, the probe surpasses structural features (0.976 vs.\\ 0.967 macro-F1), delineating when structural monitoring suffices and when fine-tuning is warranted.\n\\end{enumerate}",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01JK39WHBpL2Wam7jBY5n7un`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "c11b7ba3-04a4-42f2-bee9-6e3290ba004a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZKGXoZKP4VDG8huW2y7VP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11389,
      "cache_read_input_tokens": 24190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11389
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

_source line 14 · 2026-05-15T04:26:35.117Z_

<details><summary>↩ Tool result · `toolu_01JK39WHBpL2Wam7jBY5n7un`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented a systematic study of progress stagnation detection in LLM coding agents, comparing structural features, neural embedding probes, and LLM-as-judge approaches across deployment regimes using a weak supervision methodology.
5	Three findings emerge.
6	
7	First, a deployment-regime trade-off governs method selection.
8	In zero-data cross-coding-agent transfer (SWE-Agent $\to$ OpenHands on SWE-bench), 30 structural features achieve 0.967 macro-F1 on silver labels, outperforming neural probes by 36.9\,pp and the best LLM judge (in-domain) by 21.6\,pp (the in-domain structural score of 0.995 is a circular upper bound on LF agreement).
9	With target-agent fine-tuning the probe surpasses structural features (0.976 vs.\ 0.967), demonstrating that the structural advantage is specific to zero-data deployment.
10	A feature overlap ablation confirms that 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1, exceeding the full 30-feature model (+1.0\,pp), while 19 residual features collapse to 0.566; LF alignment reflects correct LF design rather than label leakage.
11	
12	Second, labeling functions exhibit agent-specific temporal dynamics.
13	Command repetition leads stagnation onset by 1.87 steps on SWE-Agent but lags by 3.32 steps on OpenHands.
14	A label quality audit reveals cmd\_rep is a high-precision detector (97.91\% precision) whose core value is coverage: prevalence-matched ablation shows removing it collapses training data 10$\times$ (43K$\to$4K) and costs $-$29.4\,pp (p$\approx$0).
15	Label version bias---not LF noise---was the dominant transfer bottleneck.
16	
17	Third, no label model improves over majority vote.
18	Five label models---three temporal (TWV, HMM, lag-aware HMM) and two generative (FlyingSquid, Snorkel MeTaL)---all fail to surpass majority vote; Snorkel MeTaL collapses catastrophically ($-$63.6\,pp).
19	The bottleneck is LF quantity, not aggregation method: three binary LFs produce insufficient inter-LF conflict for any approach to exploit.
20	
21	Agent monitoring should therefore prioritize lightweight structural features ({<}5\,ms per window, no GPU) for zero-data deployment; when labeled target-agent data is available, neural probes become competitive and eventually surpass structural baselines.
22	All reported results are evaluated on silver labels derived from our labeling functions; cross-coding-agent transfer and a feature overlap ablation provide non-circular evidence.
23	
24	Future work includes extending evaluation to non-software-engineering agent domains (web navigation, data analysis), online integration with early termination or strategy switching, scaling to ${>}$10 labeling functions to test whether temporal aggregation becomes useful, and human-annotated gold set validation.
25	
26	\paragraph{Reproducibility.}
27	Code, silver labels, and trained models will be released upon acceptance.
28	All agent trajectories are derived from publicly available SWE-bench runs \citep{jimenez2024swebench}; labeling functions and feature extraction are fully deterministic given the trajectory data.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "daa785e9-95ab-4a3a-bfb0-7dafcf1cafd8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a systematic study of progress stagnation detection in LLM coding agents, comparing structural features, neural embedding probes, and LLM-as-judge approaches across deployment regimes using a weak supervision methodology.\nThree findings emerge.\n\nFirst, a deployment-regime trade-off governs method selection.\nIn zero-data cross-coding-agent transfer (SWE-Agent $\\to$ OpenHands on SWE-bench), 30 structural features achieve 0.967 macro-F1 on silver labels, outperforming neural probes by 36.9\\,pp and the best LLM judge (in-domain) by 21.6\\,pp (the in-domain structural score of 0.995 is a circular upper bound on LF agreement).\nWith target-agent fine-tuning the probe surpasses structural features (0.976 vs.\\ 0.967), demonstrating that the structural advantage is specific to zero-data deployment.\nA feature overlap ablation confirms that 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1, exceeding the full 30-feature model (+1.0\\,pp), while 19 residual features collapse to 0.566; LF alignment reflects correct LF design rather than label leakage.\n\nSecond, labeling functions exhibit agent-specific temporal dynamics.\nCommand repetition leads stagnation onset by 1.87 steps on SWE-Agent but lags by 3.32 steps on OpenHands.\nA label quality audit reveals cmd\\_rep is a high-precision detector (97.91\\% precision) whose core value is coverage: prevalence-matched ablation shows removing it collapses training data 10$\\times$ (43K$\\to$4K) and costs $-$29.4\\,pp (p$\\approx$0).\nLabel version bias---not LF noise---was the dominant transfer bottleneck.\n\nThird, no label model improves over majority vote.\nFive label models---three temporal (TWV, HMM, lag-aware HMM) and two generative (FlyingSquid, Snorkel MeTaL)---all fail to surpass majority vote; Snorkel MeTaL collapses catastrophically ($-$63.6\\,pp).\nThe bottleneck is LF quantity, not aggregation method: three binary LFs produce insufficient inter-LF conflict for any approach to exploit.\n\nAgent monitoring should therefore prioritize lightweight structural features ({<}5\\,ms per window, no GPU) for zero-data deployment; when labeled target-agent data is available, neural probes become competitive and eventually surpass structural baselines.\nAll reported results are evaluated on silver labels derived from our labeling functions; cross-coding-agent transfer and a feature overlap ablation provide non-circular evidence.\n\nFuture work includes extending evaluation to non-software-engineering agent domains (web navigation, data analysis), online integration with early termination or strategy switching, scaling to ${>}$10 labeling functions to test whether temporal aggregation becomes useful, and human-annotated gold set validation.\n\n\\paragraph{Reproducibility.}\nCode, silver labels, and trained models will be released upon acceptance.\nAll agent trajectories are derived from publicly available SWE-bench runs \\citep{jimenez2024swebench}; labeling functions and feature extraction are fully deterministic given the trajectory data.\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_0117M3joYvnkY7SHUZ7Tn9mi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "7d5c67cc-3c99-4e7f-b3b4-cdb08e83c708",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZKGXoZKP4VDG8huW2y7VP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11389,
      "cache_read_input_tokens": 24190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11389
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

_source line 16 · 2026-05-15T04:26:35.459Z_

<details><summary>↩ Tool result · `toolu_0117M3joYvnkY7SHUZ7Tn9mi`</summary>

```text
1	\section{Supplementary Results}
2	\label{sec:appendix}
3	
4	%-------------------------------------------------------------------
5	\subsection{Encoder Ablation}
6	\label{sec:app_encoder}
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	\textbf{Encoder} & \textbf{Dim} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} & \textbf{Best Ep.} \\
14	\midrule
15	Qwen3-0.6B & 1024 & 0.9055 & --- & --- & --- \\
16	E5-large-v2 & 1024 & 0.9363 & 0.9067 & 0.9660 & 4 \\
17	BGE-M3 & 1024 & \textbf{0.9413} & \textbf{0.9147} & \textbf{0.9679} & 5 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Encoder ablation on SWE-Agent conf${\geq}$2 ($N{=}1{,}824$). All models use the same GRU architecture (2-layer, hidden$=$256, dropout$=$0.1, lr$=$1e-3, batch$=$32, early stopping patience~5). All encoders exceed 0.90 macro-F1, confirming the probe's temporal architecture drives performance rather than a specific encoder. BGE-M3 achieves the highest score ($+$3.6\,pp over Qwen3), but the gap between encoders (0.5\,pp) is small relative to the structural--probe gap (8.96\,pp). ``---'' for Qwen3 indicates per-class scores were not logged in the initial sweep; macro-F1 is computed from the checkpoint with lowest validation loss.}
21	\label{tab:encoder_ablation}
22	\end{table}
23	
24	%-------------------------------------------------------------------
25	\subsection{Window Size Ablation}
26	\label{sec:app_window}
27	
28	\begin{table}[h]
29	\centering
30	\small
31	\begin{tabular}{ccccc}
32	\toprule
33	\textbf{Window $k$} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} & \textbf{$\Delta$ vs.\ $k{=}5$} \\
34	\midrule
35	3 & 0.8721 & 0.7784 & 0.9659 & $-$5.9\,pp \\
36	\textbf{5} & \textbf{0.9309} & \textbf{0.8917} & \textbf{0.9701} & --- \\
37	7 & 0.9133 & 0.8791 & 0.9475 & $-$1.8\,pp \\
38	\bottomrule
39	\end{tabular}
40	\caption{Window size ablation on SWE-Agent conf${\geq}$2 using the Qwen3-0.6B encoder (seed~42). $k{=}5$ is optimal. $k{=}3$ lacks sufficient context for stagnation detection (F1\textsubscript{stag} drops 11.3\,pp). $k{=}7$ dilutes signal by spanning both progress and stagnation phases.}
41	\label{tab:window_ablation}
42	\end{table}
43	
44	%-------------------------------------------------------------------
45	\subsection{Multi-Seed Stability}
46	\label{sec:app_multiseed}
47	
48	\begin{table}[h]
49	\centering
50	\small
51	\begin{tabular}{lcccc}
52	\toprule
53	\textbf{Method} & \textbf{In-Domain F1} & \textbf{Seeds} & \textbf{Cross-Agent F1} & \textbf{Seeds} \\
54	\midrule
55	Structural RF & $0.9951 \pm 0.0000$ & 5 & --- & --- \\
56	Structural GB & --- & --- & $0.9678 \pm 0.0015$ & 5 \\
57	ProgressProbe (GRU) & $0.9185 \pm 0.0113$ & 5 & --- & --- \\
58	\bottomrule
59	\end{tabular}
60	\caption{Multi-seed stability (mean $\pm$ std). In-domain: SWE-Agent conf${\geq}$2; cross-coding-agent: SWE-Agent $\to$ OpenHands zero-shot transfer. Structural classifiers show zero or near-zero variance. The probe exhibits higher variance ($\sigma{=}0.011$) but all seeds exceed 0.90. ``---'' indicates the setting was not evaluated: RF is evaluated in-domain only, GB cross-coding-agent only, and the probe in-domain only.}
61	\label{tab:multiseed}
62	\end{table}
63	
64	%-------------------------------------------------------------------
65	\subsection{Cross-Agent Label Quality and Few-Shot Transfer}
66	\label{sec:app_cmdrep}
67	
68	Table~\ref{tab:cross_agent_cmdrep} extends the label quality analysis from \S\ref{sec:cmd_rep_ablation}, showing probe fine-tuning performance across data fractions under corrected OH labels.
69	
70	\begin{table}[h]
71	\centering
72	\small
73	\begin{tabular}{lc}
74	\toprule
75	\textbf{OH Data Fraction} & \textbf{Probe Macro-F1} \\
76	\midrule
77	0\% (zero-shot) & 0.598 \\
78	5\% & 0.850 \\
79	10\% & 0.918 \\
80	20\% & 0.948 \\
81	50\% & 0.968 \\
82	100\% & 0.976 \\
83	\bottomrule
84	\end{tabular}
85	\caption{Probe fine-tuning on corrected OH labels across data fractions. The zero-shot--to--5\% jump ($+$25.2\,pp) and rapid convergence toward structural GB (0.992 on conf${\geq}$2) demonstrate that label quality, not model capacity, was the transfer bottleneck. Under old (corrupted) labels, 5\% fine-tuning reached only 0.570.}
86	\label{tab:cross_agent_cmdrep}
87	\end{table}
88	
89	The probe reaches 0.948 macro-F1 at 20\% OH data---within 5\,pp of structural GB on conf${\geq}$2 windows (0.992)---and at 50\% (0.968) closes to within 2.5\,pp of structural GB on conf${\geq}$2 (0.992).
90	This rapid convergence under corrected labels contrasts sharply with the old label regime, where even 100\% fine-tuning reached only 0.751.
91	The improvement is driven entirely by label quality: the model architecture and training procedure are identical.
92	
93	Under the prevalence-matched ablation (\S\ref{sec:cmd_rep_ablation}), 3-LF and 2-LF label sets agree on 100\% of overlapping windows, confirming that cmd\_rep's contribution is coverage (expanding conf${\geq}$2 training data from ${\sim}$4K to ${\sim}$43K windows) rather than label refinement.
94	The $-29.4$\,pp drop upon removing cmd\_rep (McNemar $\chi^2{=}1{,}551$, $p{\approx}0$) is thus attributable to data volume collapse, not label noise.
95	
96	%-------------------------------------------------------------------
97	\subsection{Structural Feature Definitions}
98	\label{sec:app_features}
99	
100	Table~\ref{tab:feature_defs} lists all 30 structural features with their categories and LF overlap classification.
101	A feature is classified as LF-overlapping if it is computed from the same signal space that any labeling function uses as input (\S\ref{sec:feature_overlap}).
102	
103	\begin{table*}[h]
104	\centering
105	\small
106	\begin{tabular}{rlll}
107	\toprule
108	\textbf{\#} & \textbf{Feature} & \textbf{Category} & \textbf{LF Overlap} \\
109	\midrule
110	1  & num\_steps             & Trajectory stats    & --- \\
111	2  & num\_actions           & Trajectory stats    & --- \\
112	3  & num\_observations      & Trajectory stats    & --- \\
113	4  & action\_ratio          & Trajectory stats    & --- \\
114	5  & mean\_text\_len        & Text statistics     & --- \\
115	6  & std\_text\_len         & Text statistics     & --- \\
116	7  & max\_text\_len         & Text statistics     & --- \\
117	8  & min\_text\_len         & Text statistics     & --- \\
118	9  & mean\_action\_len      & Text statistics     & --- \\
119	10 & mean\_obs\_len         & Text statistics     & --- \\
120	11 & text\_len\_trend       & Text statistics     & --- \\
121	12 & num\_commands          & Command stats       & --- \\
122	13 & mean\_cmd\_len         & Command stats       & --- \\
123	14 & max\_cmd\_len          & Command stats       & --- \\
124	15 & unique\_cmd\_ratio     & Repetition          & $\lambda_1$ \\
125	16 & max\_repeat\_ratio     & Repetition          & $\lambda_1$ \\
126	17 & num\_edit\_cmds        & File operations     & $\lambda_2$ \\
127	18 & num\_search\_cmds      & File operations     & $\lambda_2$ \\
128	19 & num\_nav\_cmds         & File operations     & --- \\
129	20 & num\_submit\_cmds      & File operations     & --- \\
130	21 & edit\_ratio            & File operations     & $\lambda_2$ \\
131	22 & search\_ratio          & File operations     & $\lambda_2$ \\
132	23 & avg\_adjacent\_cmd\_sim & Edit distance       & $\lambda_1$ \\
133	24 & max\_adjacent\_cmd\_sim & Edit distance       & $\lambda_1$ \\
134	25 & max\_consec\_similar   & Edit distance       & $\lambda_1$ \\
135	26 & num\_errors            & Output statistics   & --- \\
136	27 & num\_test\_outputs     & Output statistics   & --- \\
137	28 & num\_file\_displays    & Output statistics   & $\lambda_2$ \\
138	29 & num\_nonzero\_exits    & Output statistics   & --- \\
139	30 & is\_short\_trajectory  & Trajectory stats    & $\lambda_3$ \\
140	\bottomrule
141	\end{tabular}
142	\caption{Complete structural feature definitions ($N{=}30$). LF Overlap indicates which labeling function's signal space the feature shares: $\lambda_1$ (command repetition), $\lambda_2$ (file diff), $\lambda_3$ (outcome backpropagation), or ``---'' (no overlap). 11 features overlap with at least one LF; 19 are residual.}
143	\label{tab:feature_defs}
144	\end{table*}
145	
146	%-------------------------------------------------------------------
147	\subsection{Instance Isolation}
148	\label{sec:app_instance_isolation}
149	
150	\begin{table}[h]
151	\centering
152	\small
153	\begin{tabular}{lccc}
154	\toprule
155	\textbf{Model} & \textbf{Full} & \textbf{Unseen-only} & \textbf{$\Delta$} \\
156	\midrule
157	GB all & 0.9674 & 0.9669 & $-$0.05\,pp \\
158	RF all & 0.9123 & 0.9121 & $-$0.01\,pp \\
159	GB conf${\geq}$2 & 0.9919 & 0.9917 & $-$0.02\,pp \\
160	RF conf${\geq}$2 & 0.9959 & 0.9962 & $+$0.03\,pp \\
161	\bottomrule
162	\end{tabular}
163	\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 overlapping SWE-bench instances (8.3\% of OH test data). All $|\Delta| < 0.1$\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}
164	\label{tab:instance_isolation}
165	\end{table}
166	
167	%-------------------------------------------------------------------
168	\subsection{Extended LLM-as-Judge Evaluation}
169	\label{sec:llm_extended}
170	
171	Table~\ref{tab:llm_extended} extends the zero-shot LLM-as-judge baseline (Table~\ref{tab:main_results}) with few-shot prompting and an alternative model, all evaluated on the SWE-Agent conf${\geq}$2 test set ($N{=}1{,}824$).
172	
173	\begin{table}[h]
174	\centering
175	\small
176	\begin{tabular}{llccc}
177	\toprule
178	\textbf{Model} & \textbf{Setting} & \textbf{Macro-F1} & \textbf{Parse Fail} & \textbf{Cost} \\
179	\midrule
180	Claude Sonnet 4.6 & zero-shot & 0.6625 & 0\% & \$11.66 \\
181	Claude Sonnet 4.6 & 5-shot & 0.751 & 0\% & \$36.08 \\
182	GPT-5.5 & zero-shot & 0.746 & 22.4\% & \$11.62 \\
183	\bottomrule
184	\end{tabular}
185	\caption{Extended LLM-as-judge evaluation on SWE-Agent conf${\geq}$2 ($N{=}1{,}824$). The zero-shot and 5-shot rows use the same Claude Sonnet 4.6 model; few-shot prompting improves performance by 8.9\,pp but triples cost. For GPT-5.5, 22.4\% of responses failed to parse; macro-F1 is computed over the 77.6\% with valid outputs. The best LLM configuration (0.751, in-domain) trails structural cross-coding-agent transfer (GB 0.967 on OpenHands) by 21.6\,pp, despite the LLM's in-domain advantage.}
186	\label{tab:llm_extended}
187	\end{table}
188	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "d47a70e7-0e3f-4916-b453-a7641cddb4dc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/appendix.tex",
      "content": "\\section{Supplementary Results}\n\\label{sec:appendix}\n\n%-------------------------------------------------------------------\n\\subsection{Encoder Ablation}\n\\label{sec:app_encoder}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Dim} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} & \\textbf{Best Ep.} \\\\\n\\midrule\nQwen3-0.6B & 1024 & 0.9055 & --- & --- & --- \\\\\nE5-large-v2 & 1024 & 0.9363 & 0.9067 & 0.9660 & 4 \\\\\nBGE-M3 & 1024 & \\textbf{0.9413} & \\textbf{0.9147} & \\textbf{0.9679} & 5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Encoder ablation on SWE-Agent conf${\\geq}$2 ($N{=}1{,}824$). All models use the same GRU architecture (2-layer, hidden$=$256, dropout$=$0.1, lr$=$1e-3, batch$=$32, early stopping patience~5). All encoders exceed 0.90 macro-F1, confirming the probe's temporal architecture drives performance rather than a specific encoder. BGE-M3 achieves the highest score ($+$3.6\\,pp over Qwen3), but the gap between encoders (0.5\\,pp) is small relative to the structural--probe gap (8.96\\,pp). ``---'' for Qwen3 indicates per-class scores were not logged in the initial sweep; macro-F1 is computed from the checkpoint with lowest validation loss.}\n\\label{tab:encoder_ablation}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Window Size Ablation}\n\\label{sec:app_window}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Window $k$} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} & \\textbf{$\\Delta$ vs.\\ $k{=}5$} \\\\\n\\midrule\n3 & 0.8721 & 0.7784 & 0.9659 & $-$5.9\\,pp \\\\\n\\textbf{5} & \\textbf{0.9309} & \\textbf{0.8917} & \\textbf{0.9701} & --- \\\\\n7 & 0.9133 & 0.8791 & 0.9475 & $-$1.8\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Window size ablation on SWE-Agent conf${\\geq}$2 using the Qwen3-0.6B encoder (seed~42). $k{=}5$ is optimal. $k{=}3$ lacks sufficient context for stagnation detection (F1\\textsubscript{stag} drops 11.3\\,pp). $k{=}7$ dilutes signal by spanning both progress and stagnation phases.}\n\\label{tab:window_ablation}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Multi-Seed Stability}\n\\label{sec:app_multiseed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{In-Domain F1} & \\textbf{Seeds} & \\textbf{Cross-Agent F1} & \\textbf{Seeds} \\\\\n\\midrule\nStructural RF & $0.9951 \\pm 0.0000$ & 5 & --- & --- \\\\\nStructural GB & --- & --- & $0.9678 \\pm 0.0015$ & 5 \\\\\nProgressProbe (GRU) & $0.9185 \\pm 0.0113$ & 5 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-seed stability (mean $\\pm$ std). In-domain: SWE-Agent conf${\\geq}$2; cross-coding-agent: SWE-Agent $\\to$ OpenHands zero-shot transfer. Structural classifiers show zero or near-zero variance. The probe exhibits higher variance ($\\sigma{=}0.011$) but all seeds exceed 0.90. ``---'' indicates the setting was not evaluated: RF is evaluated in-domain only, GB cross-coding-agent only, and the probe in-domain only.}\n\\label{tab:multiseed}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Label Quality and Few-Shot Transfer}\n\\label{sec:app_cmdrep}\n\nTable~\\ref{tab:cross_agent_cmdrep} extends the label quality analysis from \\S\\ref{sec:cmd_rep_ablation}, showing probe fine-tuning performance across data fractions under corrected OH labels.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{OH Data Fraction} & \\textbf{Probe Macro-F1} \\\\\n\\midrule\n0\\% (zero-shot) & 0.598 \\\\\n5\\% & 0.850 \\\\\n10\\% & 0.918 \\\\\n20\\% & 0.948 \\\\\n50\\% & 0.968 \\\\\n100\\% & 0.976 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Probe fine-tuning on corrected OH labels across data fractions. The zero-shot--to--5\\% jump ($+$25.2\\,pp) and rapid convergence toward structural GB (0.992 on conf${\\geq}$2) demonstrate that label quality, not model capacity, was the transfer bottleneck. Under old (corrupted) labels, 5\\% fine-tuning reached only 0.570.}\n\\label{tab:cross_agent_cmdrep}\n\\end{table}\n\nThe probe reaches 0.948 macro-F1 at 20\\% OH data---within 5\\,pp of structural GB on conf${\\geq}$2 windows (0.992)---and at 50\\% (0.968) closes to within 2.5\\,pp of structural GB on conf${\\geq}$2 (0.992).\nThis rapid convergence under corrected labels contrasts sharply with the old label regime, where even 100\\% fine-tuning reached only 0.751.\nThe improvement is driven entirely by label quality: the model architecture and training procedure are identical.\n\nUnder the prevalence-matched ablation (\\S\\ref{sec:cmd_rep_ablation}), 3-LF and 2-LF label sets agree on 100\\% of overlapping windows, confirming that cmd\\_rep's contribution is coverage (expanding conf${\\geq}$2 training data from ${\\sim}$4K to ${\\sim}$43K windows) rather than label refinement.\nThe $-29.4$\\,pp drop upon removing cmd\\_rep (McNemar $\\chi^2{=}1{,}551$, $p{\\approx}0$) is thus attributable to data volume collapse, not label noise.\n\n%-------------------------------------------------------------------\n\\subsection{Structural Feature Definitions}\n\\label{sec:app_features}\n\nTable~\\ref{tab:feature_defs} lists all 30 structural features with their categories and LF overlap classification.\nA feature is classified as LF-overlapping if it is computed from the same signal space that any labeling function uses as input (\\S\\ref{sec:feature_overlap}).\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\begin{tabular}{rlll}\n\\toprule\n\\textbf{\\#} & \\textbf{Feature} & \\textbf{Category} & \\textbf{LF Overlap} \\\\\n\\midrule\n1  & num\\_steps             & Trajectory stats    & --- \\\\\n2  & num\\_actions           & Trajectory stats    & --- \\\\\n3  & num\\_observations      & Trajectory stats    & --- \\\\\n4  & action\\_ratio          & Trajectory stats    & --- \\\\\n5  & mean\\_text\\_len        & Text statistics     & --- \\\\\n6  & std\\_text\\_len         & Text statistics     & --- \\\\\n7  & max\\_text\\_len         & Text statistics     & --- \\\\\n8  & min\\_text\\_len         & Text statistics     & --- \\\\\n9  & mean\\_action\\_len      & Text statistics     & --- \\\\\n10 & mean\\_obs\\_len         & Text statistics     & --- \\\\\n11 & text\\_len\\_trend       & Text statistics     & --- \\\\\n12 & num\\_commands          & Command stats       & --- \\\\\n13 & mean\\_cmd\\_len         & Command stats       & --- \\\\\n14 & max\\_cmd\\_len          & Command stats       & --- \\\\\n15 & unique\\_cmd\\_ratio     & Repetition          & $\\lambda_1$ \\\\\n16 & max\\_repeat\\_ratio     & Repetition          & $\\lambda_1$ \\\\\n17 & num\\_edit\\_cmds        & File operations     & $\\lambda_2$ \\\\\n18 & num\\_search\\_cmds      & File operations     & $\\lambda_2$ \\\\\n19 & num\\_nav\\_cmds         & File operations     & --- \\\\\n20 & num\\_submit\\_cmds      & File operations     & --- \\\\\n21 & edit\\_ratio            & File operations     & $\\lambda_2$ \\\\\n22 & search\\_ratio          & File operations     & $\\lambda_2$ \\\\\n23 & avg\\_adjacent\\_cmd\\_sim & Edit distance       & $\\lambda_1$ \\\\\n24 & max\\_adjacent\\_cmd\\_sim & Edit distance       & $\\lambda_1$ \\\\\n25 & max\\_consec\\_similar   & Edit distance       & $\\lambda_1$ \\\\\n26 & num\\_errors            & Output statistics   & --- \\\\\n27 & num\\_test\\_outputs     & Output statistics   & --- \\\\\n28 & num\\_file\\_displays    & Output statistics   & $\\lambda_2$ \\\\\n29 & num\\_nonzero\\_exits    & Output statistics   & --- \\\\\n30 & is\\_short\\_trajectory  & Trajectory stats    & $\\lambda_3$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Complete structural feature definitions ($N{=}30$). LF Overlap indicates which labeling function's signal space the feature shares: $\\lambda_1$ (command repetition), $\\lambda_2$ (file diff), $\\lambda_3$ (outcome backpropagation), or ``---'' (no overlap). 11 features overlap with at least one LF; 19 are residual.}\n\\label{tab:feature_defs}\n\\end{table*}\n\n%-------------------------------------------------------------------\n\\subsection{Instance Isolation}\n\\label{sec:app_instance_isolation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Full} & \\textbf{Unseen-only} & \\textbf{$\\Delta$} \\\\\n\\midrule\nGB all & 0.9674 & 0.9669 & $-$0.05\\,pp \\\\\nRF all & 0.9123 & 0.9121 & $-$0.01\\,pp \\\\\nGB conf${\\geq}$2 & 0.9919 & 0.9917 & $-$0.02\\,pp \\\\\nRF conf${\\geq}$2 & 0.9959 & 0.9962 & $+$0.03\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 overlapping SWE-bench instances (8.3\\% of OH test data). All $|\\Delta| < 0.1$\\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}\n\\label{tab:instance_isolation}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Extended LLM-as-Judge Evaluation}\n\\label{sec:llm_extended}\n\nTable~\\ref{tab:llm_extended} extends the zero-shot LLM-as-judge baseline (Table~\\ref{tab:main_results}) with few-shot prompting and an alternative model, all evaluated on the SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Setting} & \\textbf{Macro-F1} & \\textbf{Parse Fail} & \\textbf{Cost} \\\\\n\\midrule\nClaude Sonnet 4.6 & zero-shot & 0.6625 & 0\\% & \\$11.66 \\\\\nClaude Sonnet 4.6 & 5-shot & 0.751 & 0\\% & \\$36.08 \\\\\nGPT-5.5 & zero-shot & 0.746 & 22.4\\% & \\$11.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Extended LLM-as-judge evaluation on SWE-Agent conf${\\geq}$2 ($N{=}1{,}824$). The zero-shot and 5-shot rows use the same Claude Sonnet 4.6 model; few-shot prompting improves performance by 8.9\\,pp but triples cost. For GPT-5.5, 22.4\\% of responses failed to parse; macro-F1 is computed over the 77.6\\% with valid outputs. The best LLM configuration (0.751, in-domain) trails structural cross-coding-agent transfer (GB 0.967 on OpenHands) by 21.6\\,pp, despite the LLM's in-domain advantage.}\n\\label{tab:llm_extended}\n\\end{table}\n",
      "numLines": 188,
      "startLine": 1,
      "totalLines": 188
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me analyze what already exists and what needs to be added:

**Instance Isolation:**
- `analysis.tex` line 14 already mentions it briefly in the circular evaluation section
- `appendix.tex` lines 147-165 already has `Table~\ref{tab:instance_isolation}` with the exact data
- So the instance isolation data is already in the paper! It has the table in the appendix and a mention in the analysis section.

But wait, the task says "新增段落" (new paragraph). Let me re-read the mention in analysis.tex more carefully:


The existing sentence at line 14 already covers the instance isolation results—it reports that removing 284 instances (8.3% of test data) causes minimal changes to cross-coding-agent macro-F1, with the table reference already pointing to the appendix. So this content is already integrated into the paper.

**Feature Overlap Ablation:**
Looking at lines 18-55 in `analysis.tex`, there's already a full subsection with the ablation table showing three rows of results.

However, I notice the per-feature removal ablation data—removing cmd_rep, file_diff, and outcome_bp features individually—doesn't appear anywhere in the paper yet. These granular ablations show much larger performance drops (ranging from -0.2pp to -40.6pp on cross-agent GB) compared to the aggregate feature group results, so they'd be worth including if space allows. Looking at the instance isolation data, the appendix table already contains all the key numbers and the analysis section references it, so that part seems adequately covered. For feature overlap, I need to integrate the per-feature removal results—specifically the individual F1 scores when each feature is removed—into the structural signal analysis section of the paper. I need to verify the feature counts for the per-feature removal ablations—when we remove cmd_rep features, that leaves 25 features total, and similarly for the others. Let me trace through the feature classifications to make sure I'm interpreting the task data correctly before deciding where to integrate these results. , 16, 23, 24, 25 = 5 features
- λ2 (file_diff): features 17, 18, 21, 22, 28 = 5 features
- λ3 (outcome_bp): feature 30 = 1 feature
Total: 5 + 5 + 1 = 11 ✓

So removing cmd_rep features: 30 - 5 = 25 features
Removing file_diff features: 30 - 5 = 25 features
Removing outcome_bp features: 30 - 1 = 29 features

This is a leave-one-group-out ablation. Let me add this to the feature overlap subsection.

Now I need to update the feature overlap table with per-LF-group removal rows and write a paragraph discussing the results. For the instance isolation part, the existing text already covers the key claim about no instance-level leakage with the right numbers, so I'll keep that as is and focus on the ablation table updates. Generating the ablation table... Now I'm looking at the instance isolation setup more carefully—I should include the actual instance counts in the appendix caption to be more precise. That means specifying that 284 of the 3,409 OH test instances overlap with the 1,386 SWE-bench training instances, which gives better context for that 8.3% figure. I'll make these three edits: expand the feature ablation table with per-group breakdowns, add analysis discussing how cmd_rep features dominate the transfer performance while outcome_bp contributes almost nothing, and update the instance isolation caption with those specific counts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "435ef891-4e2f-44d1-a77a-9cfbbc4e1723",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oUyB4Z2SQAVNVQKNQhs6F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8371,
      "cache_read_input_tokens": 35579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8371
      },
      "output_tokens": 9,
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

_source line 18_

The instance isolation results are already in the paper (analysis.tex line 14 + appendix Table 5). The feature overlap main ablation (full/LF-overlap/residual) is also there. What's missing is the **per-LF-group removal ablation** (cmd_rep, file_diff, outcome_bp individually removed). Let me add that.

I'll expand the feature overlap table and add a paragraph, plus enhance the appendix instance isolation caption with the instance counts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "0315b8b6-9698-4fc9-803e-64d778391db9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oUyB4Z2SQAVNVQKNQhs6F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8371,
      "cache_read_input_tokens": 35579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8371
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Edit · `toolu_013D2U6raMKcgrBQxyoGZwuU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex",
  "old_string": "\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{\\#Feat} & \\textbf{In-Dom.} & \\textbf{Cross-Ag.} \\\\\n\\midrule\nFull (all 30) & 30 & 0.9951 & 0.9674 \\\\\nLF-overlap only & 11 & 0.9937 & 0.9770 \\\\\nResidual only & 19 & 0.9515 & 0.5656 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature overlap ablation (GB). In-Dom.\\ = SWE-Agent in-domain macro-F1; Cross-Ag.\\ = SWE-Agent $\\to$ OpenHands zero-shot. LF-overlap features alone exceed the full model cross-coding-agent (+1.0\\,pp); residual features collapse.}\n\\label{tab:feature_overlap}\n\\end{table}",
  "new_string": "\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{\\#Feat} & \\textbf{In-Dom.} & \\textbf{Cross-Ag.} \\\\\n\\midrule\nFull (all 30) & 30 & 0.9951 & 0.9674 \\\\\nLF-overlap only & 11 & 0.9937 & \\textbf{0.9770} \\\\\nResidual only & 19 & 0.9515 & 0.5656 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Leave-one-group-out (cross-coding-agent)}} \\\\\n$-$ cmd\\_rep ($\\lambda_1$) & 25 & --- & 0.5620 \\\\\n$-$ file\\_diff ($\\lambda_2$) & 25 & --- & 0.6590 \\\\\n$-$ outcome\\_bp ($\\lambda_3$) & 29 & --- & 0.9660 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature overlap ablation (GB). In-Dom.\\ = SWE-Agent in-domain macro-F1; Cross-Ag.\\ = SWE-Agent $\\to$ OpenHands zero-shot. Top: LF-overlap features alone exceed the full model cross-coding-agent (+1.0\\,pp); residual features collapse. Bottom: removing each LF-group individually; cmd\\_rep features account for the largest transfer drop ($-$40.6\\,pp).}\n\\label{tab:feature_overlap}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "4c5743e9-15bc-4d67-865d-f3e30376477e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oUyB4Z2SQAVNVQKNQhs6F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8371,
      "cache_read_input_tokens": 35579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8371
      },
      "output_tokens": 9,
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

_source line 20 · 2026-05-15T04:27:37.299Z_

<details><summary>↩ Tool result · `toolu_013D2U6raMKcgrBQxyoGZwuU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "a736323b-9269-455e-bf68-4de49da0c9f7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex",
    "oldString": "\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{\\#Feat} & \\textbf{In-Dom.} & \\textbf{Cross-Ag.} \\\\\n\\midrule\nFull (all 30) & 30 & 0.9951 & 0.9674 \\\\\nLF-overlap only & 11 & 0.9937 & 0.9770 \\\\\nResidual only & 19 & 0.9515 & 0.5656 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature overlap ablation (GB). In-Dom.\\ = SWE-Agent in-domain macro-F1; Cross-Ag.\\ = SWE-Agent $\\to$ OpenHands zero-shot. LF-overlap features alone exceed the full model cross-coding-agent (+1.0\\,pp); residual features collapse.}\n\\label{tab:feature_overlap}\n\\end{table}",
    "newString": "\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{\\#Feat} & \\textbf{In-Dom.} & \\textbf{Cross-Ag.} \\\\\n\\midrule\nFull (all 30) & 30 & 0.9951 & 0.9674 \\\\\nLF-overlap only & 11 & 0.9937 & \\textbf{0.9770} \\\\\nResidual only & 19 & 0.9515 & 0.5656 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Leave-one-group-out (cross-coding-agent)}} \\\\\n$-$ cmd\\_rep ($\\lambda_1$) & 25 & --- & 0.5620 \\\\\n$-$ file\\_diff ($\\lambda_2$) & 25 & --- & 0.6590 \\\\\n$-$ outcome\\_bp ($\\lambda_3$) & 29 & --- & 0.9660 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature overlap ablation (GB). In-Dom.\\ = SWE-Agent in-domain macro-F1; Cross-Ag.\\ = SWE-Agent $\\to$ OpenHands zero-shot. Top: LF-overlap features alone exceed the full model cross-coding-agent (+1.0\\,pp); residual features collapse. Bottom: removing each LF-group individually; cmd\\_rep features account for the largest transfer drop ($-$40.6\\,pp).}\n\\label{tab:feature_overlap}\n\\end{table}",
    "originalFile": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Circular Evaluation and Its Implications}\n\\label{sec:circular}\n\nThe structural RF's 0.995 macro-F1 (\\S\\ref{sec:main_results}) is a predictable consequence of feature--label overlap, not a detection achievement.\nThe 30 structural features include repetition ratios and file operation counts---the same signals $\\lambda_1$ and $\\lambda_2$ consume to produce silver labels.\nThis score therefore represents an upper bound on LF reverse-engineering fidelity (a feature overlap ablation in \\S\\ref{sec:feature_overlap} quantifies this decomposition).\n\nThree evaluation settings break this circularity.\nFirst, cross-coding-agent transfer: GB trained on SWE-Agent LF distributions achieves 0.967 macro-F1 on OpenHands, where LF firing patterns differ substantially (e.g., cmd\\_rep votes stagnation on 5.4\\% vs.\\ 65.5\\% of windows).\nThe model cannot memorize LF outputs when tested on a different agent's distribution.\nSecond, instance isolation: removing 284 SWE-bench task instances (8.3\\% of OH test data) that appear in both training and test sets changes all cross-coding-agent macro-F1 by ${<}$0.1\\,pp (Table~\\ref{tab:instance_isolation}), ruling out instance memorization as an explanation for transfer performance.\nThird, a human-annotated gold set (\\S\\ref{sec:gold_set}) will provide definitive non-circular ground truth.\nUntil then, all in-domain structural metrics should be interpreted as LF-agreement scores rather than detection accuracy.\n\n\\subsection{Feature Overlap Ablation}\n\\label{sec:feature_overlap}\n\nTo quantify how much of the structural classifier's performance derives from LF-overlapping features versus residual signal, we partition the 30 features into two groups.\nA feature is classified as \\emph{LF-overlapping} if it directly computes the same function as any labeling function: command uniqueness and repetition ratios, adjacent command similarity scores ($\\lambda_1$), edit and search command counts and ratios, file display counts ($\\lambda_2$), and the short-trajectory indicator ($\\lambda_3$).\nThis yields 11 LF-overlapping and 19 residual features (full classification in Appendix Table~\\ref{tab:feature_defs}).\nTable~\\ref{tab:feature_overlap} reports GB performance for each subset.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{\\#Feat} & \\textbf{In-Dom.} & \\textbf{Cross-Ag.} \\\\\n\\midrule\nFull (all 30) & 30 & 0.9951 & 0.9674 \\\\\nLF-overlap only & 11 & 0.9937 & 0.9770 \\\\\nResidual only & 19 & 0.9515 & 0.5656 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature overlap ablation (GB). In-Dom.\\ = SWE-Agent in-domain macro-F1; Cross-Ag.\\ = SWE-Agent $\\to$ OpenHands zero-shot. LF-overlap features alone exceed the full model cross-coding-agent (+1.0\\,pp); residual features collapse.}\n\\label{tab:feature_overlap}\n\\end{table}\n\nThree findings emerge.\nFirst, 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1---exceeding the full 30-feature model (0.967) by 1.0\\,pp.\nThis is the opposite of what label leakage would predict: if these features merely reconstructed the labeling pipeline, adding more features could only help or be neutral, not hurt.\nThe improvement under fewer features reflects a regularization effect: the 19 residual features encode agent-specific patterns that introduce noise harmful to cross-coding-agent generalization.\n\nSecond, residual features retain non-trivial in-domain signal: 19 features achieve 0.952 macro-F1, confirming that stagnation manifests in patterns beyond what the three LFs capture---text length statistics, trajectory counts, and output statistics carry independent diagnostic value.\nHowever, this signal is agent-specific: cross-coding-agent F1 collapses to 0.566, near the majority baseline (${\\sim}$0.55).\n\nThird, LF alignment is evidence of correct LF design, not circularity.\nThe features that generalize across coding agents are precisely those encoding universal stagnation signals---command repetition patterns and file operation dynamics---rather than agent-specific idiosyncrasies captured by residual features.\nOne might object that LF-overlapping features merely reconstruct the label-generation pipeline rather than detecting real stagnation.\nTwo observations counter this.\nFirst, the cross-coding-agent evaluation is itself non-circular: the SWE-Agent LF firing distribution differs drastically from OpenHands (e.g., cmd\\_rep fires on 65.5\\% vs.\\ 5.4\\% of windows), so a model that merely memorizes LF outputs would fail on the target agent---yet structural GB achieves 0.967.\nSecond, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \\emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.\n\n\\subsection{Why No Label Model Improves Over Majority Vote}\n\\label{sec:why_tlm_fail}\n\nDespite clear temporal structure in LF activations (\\S\\ref{sec:lf_temporal}), no label model---temporal or generative---improves downstream detection over majority vote (\\S\\ref{sec:temporal_label_models}).\nThe failure spans five models with distinct inductive biases: TWV and Lag-HMM model temporal dynamics, HMM captures latent state transitions, while FlyingSquid and Snorkel MeTaL assume conditional independence.\nAll fail for the same root cause: three binary LFs produce at most $2^3{=}8$ voting patterns, and conf${\\geq}$2 windows dominate the training set, leaving insufficient inter-LF conflict for any aggregation method to exploit.\n\nThe failure modes differ by model class.\nTemporal models either introduce noise (TWV: $-$2.57\\,pp downstream despite $+$0.6\\,pp self-evaluated) or overpredict stagnation (HMM: $-$14.4\\,pp).\nGenerative models fare worse: FlyingSquid ($-$11.3\\,pp) introduces systematic stagnation bias, and Snorkel MeTaL collapses catastrophically ($-$63.6\\,pp, 42.3\\% MV agreement).\nBoth assume conditional independence among LFs---violated by the shared behavioral signals underlying our three functions---and lack sequential structure to recover from this misspecification.\n\nThe bottleneck is LF quantity, not aggregation sophistication.\nThree binary LFs represent a realistic operating point for domain-specific agent monitoring, where each LF requires expert knowledge of agent failure modes.\nOur finding that temporal label models fail in this low-LF regime has direct implications for practitioners who cannot afford to design ${>}$10 labeling functions: majority vote is not merely a convenient baseline but the recommended aggregation strategy.\nScaling to a richer LF set with higher disagreement rates would be needed to create the ambiguity where advanced aggregation could add value \\citep{ratner2017snorkel}.\n\n\\subsection{Error Analysis}\n\\label{sec:error_analysis}\n\nWe analyze errors of the ProgressProbe (GRU) on the SWE-Agent conf${\\geq}$2 test set under the stagnation-positive convention (positive = stagnation throughout).\nThe model misclassifies 131 of 1,824 windows (7.2\\% error rate): 85 false negatives (predicted progress, actual stagnation; 64.9\\% of errors) and 46 false positives (predicted stagnation, actual progress; 35.1\\%).\n\nThe recall bottleneck is the dominant failure mode: $P_\\text{stag}{=}0.897$ vs.\\ $R_\\text{stag}{=}0.825$.\nMissed stagnation windows (FN) are not borderline cases---the model assigns them a mean stagnation probability of only 0.078 (i.e., high progress confidence of 0.922), with 73\\% receiving $>$0.9 progress probability.\nThese windows feature agents performing diverse edits and varied commands that mimic progress patterns while making no effective headway, constituting a systematic blind spot.\nFalse positives arise when agents repeat specific command patterns during genuine progress.\n\nLF conflict is a strong error predictor: 39.7\\% of error windows have at least one LF disagreeing, compared to a 31\\% base rate.\nThe cmd\\_rep LF contributes the highest per-LF error rate (12.75\\%).\nErrors concentrate in trajectory midpoints (10.2\\% error rate vs.\\ 6.5\\% at endpoints), where the boundary between exploration and stagnation is most ambiguous.\nError mass is also non-uniform across trajectories: the two highest-error trajectories account for 18.3\\% of all misclassifications.\n\n\\subsection{Cross-Agent Error Patterns}\n\\label{sec:cross_agent_errors}\n\nWe extend error analysis to cross-coding-agent transfer, evaluating the SWE-trained probe and structural GB on the full OH conf${\\geq}$2 set (43,376 windows).\nThe probe misclassifies 19.9\\% of windows, while structural GB errs on only 0.51\\% (223 windows)---a nearly 40$\\times$ gap that quantifies the distributional shift penalty for learned embeddings.\nOf the probe's errors, 80.5\\% are false positives (predicting stagnation on progress windows), indicating that the probe systematically misreads OH action patterns as stagnation signals learned from SWE-Agent.\n\nThe two models' errors are nearly disjoint: only 2.2\\% of probe errors overlap with structural errors (192 of 8,643 probe-error windows).\nStructural features, being agent-agnostic by construction, are immune to the embedding distribution shift that drives probe failures.\n\nThe probe's cross-coding-agent errors are not borderline: 62\\% occur at high confidence ($>$0.9 or $<$0.1), ruling out threshold tuning as a remedy.\nThe embedding space encodes SWE-Agent--specific stagnation patterns that confidently misfire on OH distributions, explaining why even 5\\% target fine-tuning (reaching 0.850 macro-F1) dramatically outperforms zero-shot transfer.\n\n\\subsection{Outcome Backpropagation as Distant Supervision}\n\\label{sec:ob_analysis}\n\nOutcome backpropagation ($\\lambda_3$) is a privileged signal that uses task outcome, unavailable at inference time.\nA 3-seed split-isolated holdout removing $\\lambda_3$ yields macro-F1 of $0.770{\\pm}0.022$, a 7.7\\,pp drop from the 3-LF baseline of 0.847.\n$\\lambda_3$ contributes 33.5\\% of conf${\\geq}$2 labels (5,158 of 15,401 windows).\n\nHowever, $\\lambda_3$ functions as a coverage expander rather than an independent corrector: across 43,402 windows where both 2-LF and 3-LF configurations produce labels, their agreement is 100\\%.\n$\\lambda_3$ never flips a majority vote---it only promotes conf${=}1$ windows to conf${=}2$ by adding a third agreeing vote.\nThis suggests that additional real-time LFs targeting the same coverage gaps could replace the privileged outcome signal without sacrificing label quality.",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 11,
        "newStart": 31,
        "newLines": 16,
        "lines": [
          " \\textbf{Feature Set} & \\textbf{\\#Feat} & \\textbf{In-Dom.} & \\textbf{Cross-Ag.} \\\\",
          " \\midrule",
          " Full (all 30) & 30 & 0.9951 & 0.9674 \\\\",
          "-LF-overlap only & 11 & 0.9937 & 0.9770 \\\\",
          "+LF-overlap only & 11 & 0.9937 & \\textbf{0.9770} \\\\",
          " Residual only & 19 & 0.9515 & 0.5656 \\\\",
          "+\\midrule",
          "+\\multicolumn{4}{l}{\\emph{Leave-one-group-out (cross-coding-agent)}} \\\\",
          "+$-$ cmd\\_rep ($\\lambda_1$) & 25 & --- & 0.5620 \\\\",
          "+$-$ file\\_diff ($\\lambda_2$) & 25 & --- & 0.6590 \\\\",
          "+$-$ outcome\\_bp ($\\lambda_3$) & 29 & --- & 0.9660 \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Feature overlap ablation (GB). In-Dom.\\ = SWE-Agent in-domain macro-F1; Cross-Ag.\\ = SWE-Agent $\\to$ OpenHands zero-shot. LF-overlap features alone exceed the full model cross-coding-agent (+1.0\\,pp); residual features collapse.}",
          "+\\caption{Feature overlap ablation (GB). In-Dom.\\ = SWE-Agent in-domain macro-F1; Cross-Ag.\\ = SWE-Agent $\\to$ OpenHands zero-shot. Top: LF-overlap features alone exceed the full model cross-coding-agent (+1.0\\,pp); residual features collapse. Bottom: removing each LF-group individually; cmd\\_rep features account for the largest transfer drop ($-$40.6\\,pp).}",
          " \\label{tab:feature_overlap}",
          " \\end{table}",
          " "
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

_source line 21_

Now add a paragraph discussing the per-group removal results after the existing three findings:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "87f32097-e19f-4d52-9163-b215afc37777",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQemmmCFrSjbELZQoF3Ai8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3654,
      "cache_read_input_tokens": 43950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3654
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

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01CYni2GWhARdHTq2ALf6TZj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex",
  "old_string": "Second, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \\emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.\n\n\\subsection{Why No Label Model Improves Over Majority Vote}",
  "new_string": "Second, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \\emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.\n\nA leave-one-group-out ablation (Table~\\ref{tab:feature_overlap}, bottom) further localizes the transfer signal.\nRemoving the five cmd\\_rep features ($\\lambda_1$: repetition ratios and adjacent command similarity) drops cross-coding-agent F1 by 40.6\\,pp to 0.562; removing the five file\\_diff features ($\\lambda_2$: edit/search counts and file display) drops it by 30.8\\,pp to 0.659.\nIn contrast, removing the single outcome\\_bp feature ($\\lambda_3$: is\\_short\\_trajectory) costs only 0.2\\,pp (0.966).\nCommand repetition patterns are thus the dominant carrier of cross-coding-agent transfer, consistent with their role as a universal stagnation signal (\\S\\ref{sec:lf_temporal}).\n\n\\subsection{Why No Label Model Improves Over Majority Vote}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "a280ea20-2e0c-4e99-b8d6-0752e2b23766",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQemmmCFrSjbELZQoF3Ai8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3654,
      "cache_read_input_tokens": 43950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3654
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

_source line 23 · 2026-05-15T04:27:48.765Z_

<details><summary>↩ Tool result · `toolu_01CYni2GWhARdHTq2ALf6TZj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "89171d09-2321-4c2c-a56b-f9747146ccb8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex",
    "oldString": "Second, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \\emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.\n\n\\subsection{Why No Label Model Improves Over Majority Vote}",
    "newString": "Second, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \\emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.\n\nA leave-one-group-out ablation (Table~\\ref{tab:feature_overlap}, bottom) further localizes the transfer signal.\nRemoving the five cmd\\_rep features ($\\lambda_1$: repetition ratios and adjacent command similarity) drops cross-coding-agent F1 by 40.6\\,pp to 0.562; removing the five file\\_diff features ($\\lambda_2$: edit/search counts and file display) drops it by 30.8\\,pp to 0.659.\nIn contrast, removing the single outcome\\_bp feature ($\\lambda_3$: is\\_short\\_trajectory) costs only 0.2\\,pp (0.966).\nCommand repetition patterns are thus the dominant carrier of cross-coding-agent transfer, consistent with their role as a universal stagnation signal (\\S\\ref{sec:lf_temporal}).\n\n\\subsection{Why No Label Model Improves Over Majority Vote}",
    "originalFile": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Circular Evaluation and Its Implications}\n\\label{sec:circular}\n\nThe structural RF's 0.995 macro-F1 (\\S\\ref{sec:main_results}) is a predictable consequence of feature--label overlap, not a detection achievement.\nThe 30 structural features include repetition ratios and file operation counts---the same signals $\\lambda_1$ and $\\lambda_2$ consume to produce silver labels.\nThis score therefore represents an upper bound on LF reverse-engineering fidelity (a feature overlap ablation in \\S\\ref{sec:feature_overlap} quantifies this decomposition).\n\nThree evaluation settings break this circularity.\nFirst, cross-coding-agent transfer: GB trained on SWE-Agent LF distributions achieves 0.967 macro-F1 on OpenHands, where LF firing patterns differ substantially (e.g., cmd\\_rep votes stagnation on 5.4\\% vs.\\ 65.5\\% of windows).\nThe model cannot memorize LF outputs when tested on a different agent's distribution.\nSecond, instance isolation: removing 284 SWE-bench task instances (8.3\\% of OH test data) that appear in both training and test sets changes all cross-coding-agent macro-F1 by ${<}$0.1\\,pp (Table~\\ref{tab:instance_isolation}), ruling out instance memorization as an explanation for transfer performance.\nThird, a human-annotated gold set (\\S\\ref{sec:gold_set}) will provide definitive non-circular ground truth.\nUntil then, all in-domain structural metrics should be interpreted as LF-agreement scores rather than detection accuracy.\n\n\\subsection{Feature Overlap Ablation}\n\\label{sec:feature_overlap}\n\nTo quantify how much of the structural classifier's performance derives from LF-overlapping features versus residual signal, we partition the 30 features into two groups.\nA feature is classified as \\emph{LF-overlapping} if it directly computes the same function as any labeling function: command uniqueness and repetition ratios, adjacent command similarity scores ($\\lambda_1$), edit and search command counts and ratios, file display counts ($\\lambda_2$), and the short-trajectory indicator ($\\lambda_3$).\nThis yields 11 LF-overlapping and 19 residual features (full classification in Appendix Table~\\ref{tab:feature_defs}).\nTable~\\ref{tab:feature_overlap} reports GB performance for each subset.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{\\#Feat} & \\textbf{In-Dom.} & \\textbf{Cross-Ag.} \\\\\n\\midrule\nFull (all 30) & 30 & 0.9951 & 0.9674 \\\\\nLF-overlap only & 11 & 0.9937 & \\textbf{0.9770} \\\\\nResidual only & 19 & 0.9515 & 0.5656 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Leave-one-group-out (cross-coding-agent)}} \\\\\n$-$ cmd\\_rep ($\\lambda_1$) & 25 & --- & 0.5620 \\\\\n$-$ file\\_diff ($\\lambda_2$) & 25 & --- & 0.6590 \\\\\n$-$ outcome\\_bp ($\\lambda_3$) & 29 & --- & 0.9660 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature overlap ablation (GB). In-Dom.\\ = SWE-Agent in-domain macro-F1; Cross-Ag.\\ = SWE-Agent $\\to$ OpenHands zero-shot. Top: LF-overlap features alone exceed the full model cross-coding-agent (+1.0\\,pp); residual features collapse. Bottom: removing each LF-group individually; cmd\\_rep features account for the largest transfer drop ($-$40.6\\,pp).}\n\\label{tab:feature_overlap}\n\\end{table}\n\nThree findings emerge.\nFirst, 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1---exceeding the full 30-feature model (0.967) by 1.0\\,pp.\nThis is the opposite of what label leakage would predict: if these features merely reconstructed the labeling pipeline, adding more features could only help or be neutral, not hurt.\nThe improvement under fewer features reflects a regularization effect: the 19 residual features encode agent-specific patterns that introduce noise harmful to cross-coding-agent generalization.\n\nSecond, residual features retain non-trivial in-domain signal: 19 features achieve 0.952 macro-F1, confirming that stagnation manifests in patterns beyond what the three LFs capture---text length statistics, trajectory counts, and output statistics carry independent diagnostic value.\nHowever, this signal is agent-specific: cross-coding-agent F1 collapses to 0.566, near the majority baseline (${\\sim}$0.55).\n\nThird, LF alignment is evidence of correct LF design, not circularity.\nThe features that generalize across coding agents are precisely those encoding universal stagnation signals---command repetition patterns and file operation dynamics---rather than agent-specific idiosyncrasies captured by residual features.\nOne might object that LF-overlapping features merely reconstruct the label-generation pipeline rather than detecting real stagnation.\nTwo observations counter this.\nFirst, the cross-coding-agent evaluation is itself non-circular: the SWE-Agent LF firing distribution differs drastically from OpenHands (e.g., cmd\\_rep fires on 65.5\\% vs.\\ 5.4\\% of windows), so a model that merely memorizes LF outputs would fail on the target agent---yet structural GB achieves 0.967.\nSecond, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \\emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.\n\n\\subsection{Why No Label Model Improves Over Majority Vote}\n\\label{sec:why_tlm_fail}\n\nDespite clear temporal structure in LF activations (\\S\\ref{sec:lf_temporal}), no label model---temporal or generative---improves downstream detection over majority vote (\\S\\ref{sec:temporal_label_models}).\nThe failure spans five models with distinct inductive biases: TWV and Lag-HMM model temporal dynamics, HMM captures latent state transitions, while FlyingSquid and Snorkel MeTaL assume conditional independence.\nAll fail for the same root cause: three binary LFs produce at most $2^3{=}8$ voting patterns, and conf${\\geq}$2 windows dominate the training set, leaving insufficient inter-LF conflict for any aggregation method to exploit.\n\nThe failure modes differ by model class.\nTemporal models either introduce noise (TWV: $-$2.57\\,pp downstream despite $+$0.6\\,pp self-evaluated) or overpredict stagnation (HMM: $-$14.4\\,pp).\nGenerative models fare worse: FlyingSquid ($-$11.3\\,pp) introduces systematic stagnation bias, and Snorkel MeTaL collapses catastrophically ($-$63.6\\,pp, 42.3\\% MV agreement).\nBoth assume conditional independence among LFs---violated by the shared behavioral signals underlying our three functions---and lack sequential structure to recover from this misspecification.\n\nThe bottleneck is LF quantity, not aggregation sophistication.\nThree binary LFs represent a realistic operating point for domain-specific agent monitoring, where each LF requires expert knowledge of agent failure modes.\nOur finding that temporal label models fail in this low-LF regime has direct implications for practitioners who cannot afford to design ${>}$10 labeling functions: majority vote is not merely a convenient baseline but the recommended aggregation strategy.\nScaling to a richer LF set with higher disagreement rates would be needed to create the ambiguity where advanced aggregation could add value \\citep{ratner2017snorkel}.\n\n\\subsection{Error Analysis}\n\\label{sec:error_analysis}\n\nWe analyze errors of the ProgressProbe (GRU) on the SWE-Agent conf${\\geq}$2 test set under the stagnation-positive convention (positive = stagnation throughout).\nThe model misclassifies 131 of 1,824 windows (7.2\\% error rate): 85 false negatives (predicted progress, actual stagnation; 64.9\\% of errors) and 46 false positives (predicted stagnation, actual progress; 35.1\\%).\n\nThe recall bottleneck is the dominant failure mode: $P_\\text{stag}{=}0.897$ vs.\\ $R_\\text{stag}{=}0.825$.\nMissed stagnation windows (FN) are not borderline cases---the model assigns them a mean stagnation probability of only 0.078 (i.e., high progress confidence of 0.922), with 73\\% receiving $>$0.9 progress probability.\nThese windows feature agents performing diverse edits and varied commands that mimic progress patterns while making no effective headway, constituting a systematic blind spot.\nFalse positives arise when agents repeat specific command patterns during genuine progress.\n\nLF conflict is a strong error predictor: 39.7\\% of error windows have at least one LF disagreeing, compared to a 31\\% base rate.\nThe cmd\\_rep LF contributes the highest per-LF error rate (12.75\\%).\nErrors concentrate in trajectory midpoints (10.2\\% error rate vs.\\ 6.5\\% at endpoints), where the boundary between exploration and stagnation is most ambiguous.\nError mass is also non-uniform across trajectories: the two highest-error trajectories account for 18.3\\% of all misclassifications.\n\n\\subsection{Cross-Agent Error Patterns}\n\\label{sec:cross_agent_errors}\n\nWe extend error analysis to cross-coding-agent transfer, evaluating the SWE-trained probe and structural GB on the full OH conf${\\geq}$2 set (43,376 windows).\nThe probe misclassifies 19.9\\% of windows, while structural GB errs on only 0.51\\% (223 windows)---a nearly 40$\\times$ gap that quantifies the distributional shift penalty for learned embeddings.\nOf the probe's errors, 80.5\\% are false positives (predicting stagnation on progress windows), indicating that the probe systematically misreads OH action patterns as stagnation signals learned from SWE-Agent.\n\nThe two models' errors are nearly disjoint: only 2.2\\% of probe errors overlap with structural errors (192 of 8,643 probe-error windows).\nStructural features, being agent-agnostic by construction, are immune to the embedding distribution shift that drives probe failures.\n\nThe probe's cross-coding-agent errors are not borderline: 62\\% occur at high confidence ($>$0.9 or $<$0.1), ruling out threshold tuning as a remedy.\nThe embedding space encodes SWE-Agent--specific stagnation patterns that confidently misfire on OH distributions, explaining why even 5\\% target fine-tuning (reaching 0.850 macro-F1) dramatically outperforms zero-shot transfer.\n\n\\subsection{Outcome Backpropagation as Distant Supervision}\n\\label{sec:ob_analysis}\n\nOutcome backpropagation ($\\lambda_3$) is a privileged signal that uses task outcome, unavailable at inference time.\nA 3-seed split-isolated holdout removing $\\lambda_3$ yields macro-F1 of $0.770{\\pm}0.022$, a 7.7\\,pp drop from the 3-LF baseline of 0.847.\n$\\lambda_3$ contributes 33.5\\% of conf${\\geq}$2 labels (5,158 of 15,401 windows).\n\nHowever, $\\lambda_3$ functions as a coverage expander rather than an independent corrector: across 43,402 windows where both 2-LF and 3-LF configurations produce labels, their agreement is 100\\%.\n$\\lambda_3$ never flips a majority vote---it only promotes conf${=}1$ windows to conf${=}2$ by adding a third agreeing vote.\nThis suggests that additional real-time LFs targeting the same coverage gaps could replace the privileged outcome signal without sacrificing label quality.",
    "structuredPatch": [
      {
        "oldStart": 59,
        "oldLines": 6,
        "newStart": 59,
        "newLines": 11,
        "lines": [
          " First, the cross-coding-agent evaluation is itself non-circular: the SWE-Agent LF firing distribution differs drastically from OpenHands (e.g., cmd\\_rep fires on 65.5\\% vs.\\ 5.4\\% of windows), so a model that merely memorizes LF outputs would fail on the target agent---yet structural GB achieves 0.967.",
          " Second, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \\emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.",
          " ",
          "+A leave-one-group-out ablation (Table~\\ref{tab:feature_overlap}, bottom) further localizes the transfer signal.",
          "+Removing the five cmd\\_rep features ($\\lambda_1$: repetition ratios and adjacent command similarity) drops cross-coding-agent F1 by 40.6\\,pp to 0.562; removing the five file\\_diff features ($\\lambda_2$: edit/search counts and file display) drops it by 30.8\\,pp to 0.659.",
          "+In contrast, removing the single outcome\\_bp feature ($\\lambda_3$: is\\_short\\_trajectory) costs only 0.2\\,pp (0.966).",
          "+Command repetition patterns are thus the dominant carrier of cross-coding-agent transfer, consistent with their role as a universal stagnation signal (\\S\\ref{sec:lf_temporal}).",
          "+",
          " \\subsection{Why No Label Model Improves Over Majority Vote}",
          " \\label{sec:why_tlm_fail}",
          " "
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

_source line 24_

Now update the appendix instance isolation table caption with the instance counts:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "bbc9e238-9c3c-4211-9bfa-89dba1ed8f6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YU2e2ywFpHxD2s5kVCHgPz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 47604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01VNXDYRvhPh29iZKGro1VdF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/appendix.tex",
  "old_string": "\\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 overlapping SWE-bench instances (8.3\\% of OH test data). All $|\\Delta| < 0.1$\\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}",
  "new_string": "\\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 SWE-bench task instances that overlap between the 1,386 SWE-bench training instances and 3,409 OH test instances (8.3\\% of OH). All $|\\Delta| < 0.1$\\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "8f4becb2-13f0-4652-bffc-4c448687eb1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YU2e2ywFpHxD2s5kVCHgPz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 47604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
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

_source line 26 · 2026-05-15T04:27:54.586Z_

<details><summary>↩ Tool result · `toolu_01VNXDYRvhPh29iZKGro1VdF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "cbfdd8a5-5c7b-459a-a38f-0161de5663a7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/appendix.tex",
    "oldString": "\\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 overlapping SWE-bench instances (8.3\\% of OH test data). All $|\\Delta| < 0.1$\\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}",
    "newString": "\\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 SWE-bench task instances that overlap between the 1,386 SWE-bench training instances and 3,409 OH test instances (8.3\\% of OH). All $|\\Delta| < 0.1$\\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}",
    "originalFile": "\\section{Supplementary Results}\n\\label{sec:appendix}\n\n%-------------------------------------------------------------------\n\\subsection{Encoder Ablation}\n\\label{sec:app_encoder}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Dim} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} & \\textbf{Best Ep.} \\\\\n\\midrule\nQwen3-0.6B & 1024 & 0.9055 & --- & --- & --- \\\\\nE5-large-v2 & 1024 & 0.9363 & 0.9067 & 0.9660 & 4 \\\\\nBGE-M3 & 1024 & \\textbf{0.9413} & \\textbf{0.9147} & \\textbf{0.9679} & 5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Encoder ablation on SWE-Agent conf${\\geq}$2 ($N{=}1{,}824$). All models use the same GRU architecture (2-layer, hidden$=$256, dropout$=$0.1, lr$=$1e-3, batch$=$32, early stopping patience~5). All encoders exceed 0.90 macro-F1, confirming the probe's temporal architecture drives performance rather than a specific encoder. BGE-M3 achieves the highest score ($+$3.6\\,pp over Qwen3), but the gap between encoders (0.5\\,pp) is small relative to the structural--probe gap (8.96\\,pp). ``---'' for Qwen3 indicates per-class scores were not logged in the initial sweep; macro-F1 is computed from the checkpoint with lowest validation loss.}\n\\label{tab:encoder_ablation}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Window Size Ablation}\n\\label{sec:app_window}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Window $k$} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} & \\textbf{$\\Delta$ vs.\\ $k{=}5$} \\\\\n\\midrule\n3 & 0.8721 & 0.7784 & 0.9659 & $-$5.9\\,pp \\\\\n\\textbf{5} & \\textbf{0.9309} & \\textbf{0.8917} & \\textbf{0.9701} & --- \\\\\n7 & 0.9133 & 0.8791 & 0.9475 & $-$1.8\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Window size ablation on SWE-Agent conf${\\geq}$2 using the Qwen3-0.6B encoder (seed~42). $k{=}5$ is optimal. $k{=}3$ lacks sufficient context for stagnation detection (F1\\textsubscript{stag} drops 11.3\\,pp). $k{=}7$ dilutes signal by spanning both progress and stagnation phases.}\n\\label{tab:window_ablation}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Multi-Seed Stability}\n\\label{sec:app_multiseed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{In-Domain F1} & \\textbf{Seeds} & \\textbf{Cross-Agent F1} & \\textbf{Seeds} \\\\\n\\midrule\nStructural RF & $0.9951 \\pm 0.0000$ & 5 & --- & --- \\\\\nStructural GB & --- & --- & $0.9678 \\pm 0.0015$ & 5 \\\\\nProgressProbe (GRU) & $0.9185 \\pm 0.0113$ & 5 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-seed stability (mean $\\pm$ std). In-domain: SWE-Agent conf${\\geq}$2; cross-coding-agent: SWE-Agent $\\to$ OpenHands zero-shot transfer. Structural classifiers show zero or near-zero variance. The probe exhibits higher variance ($\\sigma{=}0.011$) but all seeds exceed 0.90. ``---'' indicates the setting was not evaluated: RF is evaluated in-domain only, GB cross-coding-agent only, and the probe in-domain only.}\n\\label{tab:multiseed}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Label Quality and Few-Shot Transfer}\n\\label{sec:app_cmdrep}\n\nTable~\\ref{tab:cross_agent_cmdrep} extends the label quality analysis from \\S\\ref{sec:cmd_rep_ablation}, showing probe fine-tuning performance across data fractions under corrected OH labels.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{OH Data Fraction} & \\textbf{Probe Macro-F1} \\\\\n\\midrule\n0\\% (zero-shot) & 0.598 \\\\\n5\\% & 0.850 \\\\\n10\\% & 0.918 \\\\\n20\\% & 0.948 \\\\\n50\\% & 0.968 \\\\\n100\\% & 0.976 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Probe fine-tuning on corrected OH labels across data fractions. The zero-shot--to--5\\% jump ($+$25.2\\,pp) and rapid convergence toward structural GB (0.992 on conf${\\geq}$2) demonstrate that label quality, not model capacity, was the transfer bottleneck. Under old (corrupted) labels, 5\\% fine-tuning reached only 0.570.}\n\\label{tab:cross_agent_cmdrep}\n\\end{table}\n\nThe probe reaches 0.948 macro-F1 at 20\\% OH data---within 5\\,pp of structural GB on conf${\\geq}$2 windows (0.992)---and at 50\\% (0.968) closes to within 2.5\\,pp of structural GB on conf${\\geq}$2 (0.992).\nThis rapid convergence under corrected labels contrasts sharply with the old label regime, where even 100\\% fine-tuning reached only 0.751.\nThe improvement is driven entirely by label quality: the model architecture and training procedure are identical.\n\nUnder the prevalence-matched ablation (\\S\\ref{sec:cmd_rep_ablation}), 3-LF and 2-LF label sets agree on 100\\% of overlapping windows, confirming that cmd\\_rep's contribution is coverage (expanding conf${\\geq}$2 training data from ${\\sim}$4K to ${\\sim}$43K windows) rather than label refinement.\nThe $-29.4$\\,pp drop upon removing cmd\\_rep (McNemar $\\chi^2{=}1{,}551$, $p{\\approx}0$) is thus attributable to data volume collapse, not label noise.\n\n%-------------------------------------------------------------------\n\\subsection{Structural Feature Definitions}\n\\label{sec:app_features}\n\nTable~\\ref{tab:feature_defs} lists all 30 structural features with their categories and LF overlap classification.\nA feature is classified as LF-overlapping if it is computed from the same signal space that any labeling function uses as input (\\S\\ref{sec:feature_overlap}).\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\begin{tabular}{rlll}\n\\toprule\n\\textbf{\\#} & \\textbf{Feature} & \\textbf{Category} & \\textbf{LF Overlap} \\\\\n\\midrule\n1  & num\\_steps             & Trajectory stats    & --- \\\\\n2  & num\\_actions           & Trajectory stats    & --- \\\\\n3  & num\\_observations      & Trajectory stats    & --- \\\\\n4  & action\\_ratio          & Trajectory stats    & --- \\\\\n5  & mean\\_text\\_len        & Text statistics     & --- \\\\\n6  & std\\_text\\_len         & Text statistics     & --- \\\\\n7  & max\\_text\\_len         & Text statistics     & --- \\\\\n8  & min\\_text\\_len         & Text statistics     & --- \\\\\n9  & mean\\_action\\_len      & Text statistics     & --- \\\\\n10 & mean\\_obs\\_len         & Text statistics     & --- \\\\\n11 & text\\_len\\_trend       & Text statistics     & --- \\\\\n12 & num\\_commands          & Command stats       & --- \\\\\n13 & mean\\_cmd\\_len         & Command stats       & --- \\\\\n14 & max\\_cmd\\_len          & Command stats       & --- \\\\\n15 & unique\\_cmd\\_ratio     & Repetition          & $\\lambda_1$ \\\\\n16 & max\\_repeat\\_ratio     & Repetition          & $\\lambda_1$ \\\\\n17 & num\\_edit\\_cmds        & File operations     & $\\lambda_2$ \\\\\n18 & num\\_search\\_cmds      & File operations     & $\\lambda_2$ \\\\\n19 & num\\_nav\\_cmds         & File operations     & --- \\\\\n20 & num\\_submit\\_cmds      & File operations     & --- \\\\\n21 & edit\\_ratio            & File operations     & $\\lambda_2$ \\\\\n22 & search\\_ratio          & File operations     & $\\lambda_2$ \\\\\n23 & avg\\_adjacent\\_cmd\\_sim & Edit distance       & $\\lambda_1$ \\\\\n24 & max\\_adjacent\\_cmd\\_sim & Edit distance       & $\\lambda_1$ \\\\\n25 & max\\_consec\\_similar   & Edit distance       & $\\lambda_1$ \\\\\n26 & num\\_errors            & Output statistics   & --- \\\\\n27 & num\\_test\\_outputs     & Output statistics   & --- \\\\\n28 & num\\_file\\_displays    & Output statistics   & $\\lambda_2$ \\\\\n29 & num\\_nonzero\\_exits    & Output statistics   & --- \\\\\n30 & is\\_short\\_trajectory  & Trajectory stats    & $\\lambda_3$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Complete structural feature definitions ($N{=}30$). LF Overlap indicates which labeling function's signal space the feature shares: $\\lambda_1$ (command repetition), $\\lambda_2$ (file diff), $\\lambda_3$ (outcome backpropagation), or ``---'' (no overlap). 11 features overlap with at least one LF; 19 are residual.}\n\\label{tab:feature_defs}\n\\end{table*}\n\n%-------------------------------------------------------------------\n\\subsection{Instance Isolation}\n\\label{sec:app_instance_isolation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Full} & \\textbf{Unseen-only} & \\textbf{$\\Delta$} \\\\\n\\midrule\nGB all & 0.9674 & 0.9669 & $-$0.05\\,pp \\\\\nRF all & 0.9123 & 0.9121 & $-$0.01\\,pp \\\\\nGB conf${\\geq}$2 & 0.9919 & 0.9917 & $-$0.02\\,pp \\\\\nRF conf${\\geq}$2 & 0.9959 & 0.9962 & $+$0.03\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 overlapping SWE-bench instances (8.3\\% of OH test data). All $|\\Delta| < 0.1$\\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}\n\\label{tab:instance_isolation}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Extended LLM-as-Judge Evaluation}\n\\label{sec:llm_extended}\n\nTable~\\ref{tab:llm_extended} extends the zero-shot LLM-as-judge baseline (Table~\\ref{tab:main_results}) with few-shot prompting and an alternative model, all evaluated on the SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Setting} & \\textbf{Macro-F1} & \\textbf{Parse Fail} & \\textbf{Cost} \\\\\n\\midrule\nClaude Sonnet 4.6 & zero-shot & 0.6625 & 0\\% & \\$11.66 \\\\\nClaude Sonnet 4.6 & 5-shot & 0.751 & 0\\% & \\$36.08 \\\\\nGPT-5.5 & zero-shot & 0.746 & 22.4\\% & \\$11.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Extended LLM-as-judge evaluation on SWE-Agent conf${\\geq}$2 ($N{=}1{,}824$). The zero-shot and 5-shot rows use the same Claude Sonnet 4.6 model; few-shot prompting improves performance by 8.9\\,pp but triples cost. For GPT-5.5, 22.4\\% of responses failed to parse; macro-F1 is computed over the 77.6\\% with valid outputs. The best LLM configuration (0.751, in-domain) trails structural cross-coding-agent transfer (GB 0.967 on OpenHands) by 21.6\\,pp, despite the LLM's in-domain advantage.}\n\\label{tab:llm_extended}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 160,
        "oldLines": 7,
        "newStart": 160,
        "newLines": 7,
        "lines": [
          " RF conf${\\geq}$2 & 0.9959 & 0.9962 & $+$0.03\\,pp \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 overlapping SWE-bench instances (8.3\\% of OH test data). All $|\\Delta| < 0.1$\\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}",
          "+\\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 SWE-bench task instances that overlap between the 1,386 SWE-bench training instances and 3,409 OH test instances (8.3\\% of OH). All $|\\Delta| < 0.1$\\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}",
          " \\label{tab:instance_isolation}",
          " \\end{table}",
          " "
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

_source line 27_

Let me verify the edits look correct:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "a7857cf8-43d9-4cff-a943-76e9bf2d4e8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Whv5GrAWmbxGGMBiXZibe6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 48323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 374
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

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_015NN1R7drkzXHAA9c3VRuMF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex",
  "offset": 25,
  "limit": 35
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "3bd832ca-2e3d-4043-afb8-33ee349769e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Whv5GrAWmbxGGMBiXZibe6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 48323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 374
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

_source line 29 · 2026-05-15T04:27:57.850Z_

<details><summary>↩ Tool result · `toolu_015NN1R7drkzXHAA9c3VRuMF`</summary>

```text
25	
26	\begin{table}[t]
27	\centering
28	\small
29	\begin{tabular}{lccc}
30	\toprule
31	\textbf{Feature Set} & \textbf{\#Feat} & \textbf{In-Dom.} & \textbf{Cross-Ag.} \\
32	\midrule
33	Full (all 30) & 30 & 0.9951 & 0.9674 \\
34	LF-overlap only & 11 & 0.9937 & \textbf{0.9770} \\
35	Residual only & 19 & 0.9515 & 0.5656 \\
36	\midrule
37	\multicolumn{4}{l}{\emph{Leave-one-group-out (cross-coding-agent)}} \\
38	$-$ cmd\_rep ($\lambda_1$) & 25 & --- & 0.5620 \\
39	$-$ file\_diff ($\lambda_2$) & 25 & --- & 0.6590 \\
40	$-$ outcome\_bp ($\lambda_3$) & 29 & --- & 0.9660 \\
41	\bottomrule
42	\end{tabular}
43	\caption{Feature overlap ablation (GB). In-Dom.\ = SWE-Agent in-domain macro-F1; Cross-Ag.\ = SWE-Agent $\to$ OpenHands zero-shot. Top: LF-overlap features alone exceed the full model cross-coding-agent (+1.0\,pp); residual features collapse. Bottom: removing each LF-group individually; cmd\_rep features account for the largest transfer drop ($-$40.6\,pp).}
44	\label{tab:feature_overlap}
45	\end{table}
46	
47	Three findings emerge.
48	First, 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1---exceeding the full 30-feature model (0.967) by 1.0\,pp.
49	This is the opposite of what label leakage would predict: if these features merely reconstructed the labeling pipeline, adding more features could only help or be neutral, not hurt.
50	The improvement under fewer features reflects a regularization effect: the 19 residual features encode agent-specific patterns that introduce noise harmful to cross-coding-agent generalization.
51	
52	Second, residual features retain non-trivial in-domain signal: 19 features achieve 0.952 macro-F1, confirming that stagnation manifests in patterns beyond what the three LFs capture---text length statistics, trajectory counts, and output statistics carry independent diagnostic value.
53	However, this signal is agent-specific: cross-coding-agent F1 collapses to 0.566, near the majority baseline (${\sim}$0.55).
54	
55	Third, LF alignment is evidence of correct LF design, not circularity.
56	The features that generalize across coding agents are precisely those encoding universal stagnation signals---command repetition patterns and file operation dynamics---rather than agent-specific idiosyncrasies captured by residual features.
57	One might object that LF-overlapping features merely reconstruct the label-generation pipeline rather than detecting real stagnation.
58	Two observations counter this.
59	First, the cross-coding-agent evaluation is itself non-circular: the SWE-Agent LF firing distribution differs drastically from OpenHands (e.g., cmd\_rep fires on 65.5\% vs.\ 5.4\% of windows), so a model that merely memorizes LF outputs would fail on the target agent---yet structural GB achieves 0.967.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "954cc4a6-6a56-41b3-8227-af28dd97ddb8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex",
      "content": "\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{\\#Feat} & \\textbf{In-Dom.} & \\textbf{Cross-Ag.} \\\\\n\\midrule\nFull (all 30) & 30 & 0.9951 & 0.9674 \\\\\nLF-overlap only & 11 & 0.9937 & \\textbf{0.9770} \\\\\nResidual only & 19 & 0.9515 & 0.5656 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Leave-one-group-out (cross-coding-agent)}} \\\\\n$-$ cmd\\_rep ($\\lambda_1$) & 25 & --- & 0.5620 \\\\\n$-$ file\\_diff ($\\lambda_2$) & 25 & --- & 0.6590 \\\\\n$-$ outcome\\_bp ($\\lambda_3$) & 29 & --- & 0.9660 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature overlap ablation (GB). In-Dom.\\ = SWE-Agent in-domain macro-F1; Cross-Ag.\\ = SWE-Agent $\\to$ OpenHands zero-shot. Top: LF-overlap features alone exceed the full model cross-coding-agent (+1.0\\,pp); residual features collapse. Bottom: removing each LF-group individually; cmd\\_rep features account for the largest transfer drop ($-$40.6\\,pp).}\n\\label{tab:feature_overlap}\n\\end{table}\n\nThree findings emerge.\nFirst, 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1---exceeding the full 30-feature model (0.967) by 1.0\\,pp.\nThis is the opposite of what label leakage would predict: if these features merely reconstructed the labeling pipeline, adding more features could only help or be neutral, not hurt.\nThe improvement under fewer features reflects a regularization effect: the 19 residual features encode agent-specific patterns that introduce noise harmful to cross-coding-agent generalization.\n\nSecond, residual features retain non-trivial in-domain signal: 19 features achieve 0.952 macro-F1, confirming that stagnation manifests in patterns beyond what the three LFs capture---text length statistics, trajectory counts, and output statistics carry independent diagnostic value.\nHowever, this signal is agent-specific: cross-coding-agent F1 collapses to 0.566, near the majority baseline (${\\sim}$0.55).\n\nThird, LF alignment is evidence of correct LF design, not circularity.\nThe features that generalize across coding agents are precisely those encoding universal stagnation signals---command repetition patterns and file operation dynamics---rather than agent-specific idiosyncrasies captured by residual features.\nOne might object that LF-overlapping features merely reconstruct the label-generation pipeline rather than detecting real stagnation.\nTwo observations counter this.\nFirst, the cross-coding-agent evaluation is itself non-circular: the SWE-Agent LF firing distribution differs drastically from OpenHands (e.g., cmd\\_rep fires on 65.5\\% vs.\\ 5.4\\% of windows), so a model that merely memorizes LF outputs would fail on the target agent---yet structural GB achieves 0.967.",
      "numLines": 35,
      "startLine": 25,
      "totalLines": 122
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01MGJgcYdiahwBs9KWFnz3zB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex",
  "offset": 58,
  "limit": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "5e1ba33f-554f-4afc-8957-029880c77b26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014aDTk4Xjqw3mcjPpvtwwXQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 48697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1060
      },
      "output_tokens": 71,
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

_source line 31 · 2026-05-15T04:28:00.900Z_

<details><summary>↩ Tool result · `toolu_01MGJgcYdiahwBs9KWFnz3zB`</summary>

```text
58	Two observations counter this.
59	First, the cross-coding-agent evaluation is itself non-circular: the SWE-Agent LF firing distribution differs drastically from OpenHands (e.g., cmd\_rep fires on 65.5\% vs.\ 5.4\% of windows), so a model that merely memorizes LF outputs would fail on the target agent---yet structural GB achieves 0.967.
60	Second, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.
61	
62	A leave-one-group-out ablation (Table~\ref{tab:feature_overlap}, bottom) further localizes the transfer signal.
63	Removing the five cmd\_rep features ($\lambda_1$: repetition ratios and adjacent command similarity) drops cross-coding-agent F1 by 40.6\,pp to 0.562; removing the five file\_diff features ($\lambda_2$: edit/search counts and file display) drops it by 30.8\,pp to 0.659.
64	In contrast, removing the single outcome\_bp feature ($\lambda_3$: is\_short\_trajectory) costs only 0.2\,pp (0.966).
65	Command repetition patterns are thus the dominant carrier of cross-coding-agent transfer, consistent with their role as a universal stagnation signal (\S\ref{sec:lf_temporal}).
66	
67	\subsection{Why No Label Model Improves Over Majority Vote}
68	\label{sec:why_tlm_fail}
69	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "5257a3d8-4154-48f1-ae2b-29d0586e556d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex",
      "content": "Two observations counter this.\nFirst, the cross-coding-agent evaluation is itself non-circular: the SWE-Agent LF firing distribution differs drastically from OpenHands (e.g., cmd\\_rep fires on 65.5\\% vs.\\ 5.4\\% of windows), so a model that merely memorizes LF outputs would fail on the target agent---yet structural GB achieves 0.967.\nSecond, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \\emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.\n\nA leave-one-group-out ablation (Table~\\ref{tab:feature_overlap}, bottom) further localizes the transfer signal.\nRemoving the five cmd\\_rep features ($\\lambda_1$: repetition ratios and adjacent command similarity) drops cross-coding-agent F1 by 40.6\\,pp to 0.562; removing the five file\\_diff features ($\\lambda_2$: edit/search counts and file display) drops it by 30.8\\,pp to 0.659.\nIn contrast, removing the single outcome\\_bp feature ($\\lambda_3$: is\\_short\\_trajectory) costs only 0.2\\,pp (0.966).\nCommand repetition patterns are thus the dominant carrier of cross-coding-agent transfer, consistent with their role as a universal stagnation signal (\\S\\ref{sec:lf_temporal}).\n\n\\subsection{Why No Label Model Improves Over Majority Vote}\n\\label{sec:why_tlm_fail}\n",
      "numLines": 12,
      "startLine": 58,
      "totalLines": 122
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

All edits look correct. Let me check if the introduction or conclusion need updates. The introduction (line 34) mentions the feature overlap ablation but only the top-level result (11 LF-overlap features at 0.977 vs full model). The per-group detail is an analysis-section concern and doesn't need to be in the intro/conclusion — it's a supporting decomposition rather than a new finding.

Summary of changes:

1. **`analysis.tex` Table 3 (feature_overlap)**: Added 3 leave-one-group-out rows showing cross-agent GB F1 when removing cmd_rep features (0.562, -40.6pp), file_diff features (0.659, -30.8pp), and outcome_bp feature (0.966, -0.2pp). Updated caption.

2. **`analysis.tex` new paragraph** (line 62-65): Added 4-sentence paragraph after the existing feature overlap discussion, interpreting the per-group ablation — cmd_rep features are the dominant carrier of cross-agent transfer.

3. **`appendix.tex` Table 5 caption**: Added instance counts (1,386 SWE-bench training, 3,409 OH test) for precision.

No changes needed to introduction or conclusion — the per-LF-group decomposition is a supporting detail within the analysis section, and the instance isolation was already well-integrated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "uuid": "f1a62bf5-c2e5-4b00-946b-601dfd48789a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UAYSXnJ7PwuwEeF9HWHxoy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 568,
      "cache_read_input_tokens": 49757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 568
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

### Task result

_source line 33_

All edits look correct. Let me check if the introduction or conclusion need updates. The introduction (line 34) mentions the feature overlap ablation but only the top-level result (11 LF-overlap features at 0.977 vs full model). The per-group detail is an analysis-section concern and doesn't need to be in the intro/conclusion — it's a supporting decomposition rather than a new finding.

Summary of changes:

1. **`analysis.tex` Table 3 (feature_overlap)**: Added 3 leave-one-group-out rows showing cross-agent GB F1 when removing cmd_rep features (0.562, -40.6pp), file_diff features (0.659, -30.8pp), and outcome_bp feature (0.966, -0.2pp). Updated caption.

2. **`analysis.tex` new paragraph** (line 62-65): Added 4-sentence paragraph after the existing feature overlap discussion, interpreting the per-group ablation — cmd_rep features are the dominant carrier of cross-agent transfer.

3. **`appendix.tex` Table 5 caption**: Added instance counts (1,386 SWE-bench training, 3,409 OH test) for precision.

No changes needed to introduction or conclusion — the per-LF-group decomposition is a supporting detail within the analysis section, and the instance isolation was already well-integrated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 116832,
  "duration_api_ms": 117873,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "a71c65a6-51a1-481c-a6a6-17ea3c97af65",
  "total_cost_usd": 0.5487645000000001,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 38484,
    "cache_read_input_tokens": 309941,
    "output_tokens": 6063,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38484,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 322,
        "cache_read_input_tokens": 49757,
        "cache_creation_input_tokens": 568,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 568
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1564,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001644,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 6063,
      "cacheReadInputTokens": 309941,
      "cacheCreationInputTokens": 38484,
      "webSearchRequests": 0,
      "costUSD": 0.5471205,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e3fce95c-05d1-4f1a-a958-81fa055ad927"
}
```

</details>

---
