# write d037 stats integration

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 107
- **Recorded user turns:** 0
- **Tool calls:** 38
- **Original source:** `logs/workers/worker_write_d037_stats_integration_20260516T034255.log`
- **Structured JSON:** [`c7325824db90900275ea.json`](../../sessions/c7/c7325824db90900275ea.json)

## Before a recorded user message

107 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
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
  "uuid": "ca89c472-cfea-4b4d-9693-bc55f1226d41",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "resetsAt": 1778903400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b0e14cf2-9b7c-43a3-a7aa-724b6b637374",
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848"
}
```

---

### Assistant

_source line 4_

Let me start by reading the two files I need to edit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "3f27bbee-b077-4493-9c32-bda60bdc10dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YPqWrcGTxApGKF6d277f7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12795,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12795
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

<details open><summary>🔧 Tool call — Read · `toolu_01Vei5hryg7Sk7M3sUX8rKmi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "d632a231-4c9a-447d-936a-af81325093e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YPqWrcGTxApGKF6d277f7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12795,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12795
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

_source line 6 · 2026-05-16T03:43:14.761Z_

<details><summary>↩ Tool result · `toolu_01Vei5hryg7Sk7M3sUX8rKmi`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Count-Degradation Curves}
5	\label{sec:count_curves}
6	
7	\begin{figure}[t]
8	\centering
9	\begin{minipage}[t]{0.48\columnwidth}
10	\centering
11	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
12	\end{minipage}
13	\hfill
14	\begin{minipage}[t]{0.48\columnwidth}
15	\centering
16	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
17	\end{minipage}
18	\caption{\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}
19	\label{fig:main_results}
20	\end{figure}
21	
22	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
23	
24	\paragraph{NER (Few-NERD).}
25	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\,=\,22$ to 0.55 at count${}\,=\,44$; 95\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
26	
27	\paragraph{RE (FewRel).}
28	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)
29	
30	\paragraph{ED (MAVEN).}
31	In contrast to NER and RE, MAVEN relaxed F1 \emph{increases} from 0.106 at count${}\,=\,1$ to 0.247 at count${}\,=\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \S\ref{sec:centrality_confound}.
32	
33	\paragraph{Cross-model replication.}
34	Channel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\,pp recall decline (0.702 at count${}\,=\,1$ to 0.273 at count${}\,=\,64$), compared to $-$34\,pp for Qwen3-32B (Table~\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.
35	
36	\paragraph{Summary.}
37	Schema size degrades extraction quality for NER and RE (Channel~1: count $\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\S\ref{sec:bcs_controlled}).
38	
39	\subsection{Pairwise Confusability and Type Confusion}
40	\label{sec:pairwise}
41	
42	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
43	
44	\begin{table}[t]
45	\centering
46	\small
47	\resizebox{\columnwidth}{!}{%
48	\begin{tabular}{llrrrrr}
49	\toprule
50	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
51	\midrule
52	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\
53	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\
54	\bottomrule
55	\end{tabular}}
56	\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}
57	\label{tab:pairwise}
58	\end{table}
59	
60	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$, meaning pairwise confusability explains roughly 1.5\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\S\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.
61	
62	Spearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\rho = 0.168$ ($p = 7.3 \times 10^{-14}$) and MiniLM yields $\rho = 0.144$ ($p = 1.7 \times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\rho = 0.272$ for Qwen3 and $\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\rho = 0.27\text{--}0.31$) characterize the signal among types the model actually confuses.
63	
64	The remaining ${\sim}$98\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\,pp (\S\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.
65	
66	\subsection{BCS-Controlled Experiments}
67	\label{sec:bcs_controlled}
68	
69	To move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.
70	
71	\begin{table}[t]
72	\centering
73	\small
74	\resizebox{\columnwidth}{!}{%
75	\begin{tabular}{lcrrrr}
76	\toprule
77	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
78	\midrule
79	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
80	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
81	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
82	\bottomrule
83	\end{tabular}}
84	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\,pp at 16 relations to 31.2\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
85	\label{tab:bcs_controlled}
86	\end{table}
87	
88	At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\,pp (95\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\,=\,16$, the gap remains 31.2\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\,=\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\,pp (count 8) and $-$31.8\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.
89	
90	The larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\S\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.
91	
92	\paragraph{Within-pool controlled comparison.}
93	\label{sec:within_pool}
94	A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\ref{tab:within_pool}).
95	
96	\begin{table}[t]
97	\centering
98	\small
99	\resizebox{\columnwidth}{!}{%
100	\begin{tabular}{lrrrrrrr}
101	\toprule
102	& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
103	\cmidrule(lr){2-5} \cmidrule(lr){6-7}
104	\textbf{Setting} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
105	\midrule
106	Independent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\
107	80-pool $\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\
108	Full 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\
109	\midrule
110	\multicolumn{7}{l}{\footnotesize Permutation test (16-rel vs.\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\
111	\bottomrule
112	\end{tabular}}
113	\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
114	\label{tab:within_pool}
115	\end{table}
116	
117	The within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\,pp vs.\ $-$7.42\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\ 0.65--0.90; see Appendix~\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\,pp vs.\ 9.1\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.
118	
119	\paragraph{Practical magnitude.}
120	\label{sec:practical_magnitude}
121	For representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0]), roughly 7\% of the 31.2\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\%, versus 78.9\% for top-quartile batches, a gap of 3.9\,pp. The 31.2\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\,pp.
122	
123	\paragraph{Cross-model validation.}
124	The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\,pp at count${}\,=\,8$ (low-BCS 78.1\% vs.\ high-BCS 51.0\%) and $-$23.9\,pp at count${}\,=\,16$ (75.5\% vs.\ 51.6\%), reaching 77--87\% of Qwen3-32B's $-$31.2\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\approx$51\% under high confusability (count${}\,=\,8$: 51.0\% vs.\ 51.0\%; count${}\,=\,16$: 51.6\% vs.\ 51.6\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.
125	
126	\subsection{Multi-Channel Degradation}
127	\label{sec:multi_channel}
128	
129	We decompose extraction errors into an error taxonomy (full data in Table~\ref{tab:error_taxonomy}, Appendix~\ref{sec:appendix_figures}; see also Figure~\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\%), but NER rates are substantially higher (43--65\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.
130	
131	These results establish two degradation channels: \textbf{Channel~1} (count $\to$ recall decline, \S\ref{sec:count_curves}) and \textbf{Channel~2} (confusability $\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.
132	
133	\subsection{Centrality Confound on Homogeneous Schemas}
134	\label{sec:centrality_confound}
135	
136	Per-type analysis on MAVEN reveals an anomalous \emph{positive} BCS--error correlation (Qwen3 $\rho = +0.184$, $p = 0.025$; MiniLM $\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "fd1da26e-56e6-4776-9202-04ca8ed80b44",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
      "numLines": 136,
      "startLine": 1,
      "totalLines": 136
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01PpDcbZp4PPxsRQNt2QAfSP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "63335932-5756-4d00-af95-342c363f91d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YPqWrcGTxApGKF6d277f7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12795,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12795
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

_source line 8 · 2026-05-16T03:43:15.080Z_

<details><summary>↩ Tool result · `toolu_01PpDcbZp4PPxsRQNt2QAfSP`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection (same-domain schemas are subject to a centrality confound). The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), while the wider BCS range at 80 types produces larger absolute accuracy gaps (31.2 vs.\ 9.1\,pp). Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "60b93237-868f-4cbf-9341-f0fee46db3ac",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTraining-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection (same-domain schemas are subject to a centrality confound). The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), while the wider BCS range at 80 types produces larger absolute accuracy gaps (31.2 vs.\\ 9.1\\,pp). Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.\n\\end{abstract}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
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
Now I have both files. Let me analyze each change needed:

### 2A: W4 metric correction — §4.1 count curves (results.tex)
Looking at line 25, the current text already has macro-avg values and CIs:
"e.g., 0.52 at count${}\,=\,22$ to 0.55 at count${}\,=\,44$; 95\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability"


But the task specifies different values: 0.522 at count=22 and 0.549 at count=44, so I need to update these to match the exact metrics provided. I need to update the exact values from 0.52 and 0.55 to 0.522 and 0.549 respectively, and change "permutation p = 0.31" to "bootstrap 95% CIs overlap" to match the requested phrasing more closely. The confidence intervals and the message about sampling variability are already in place, so I'm just refining the numbers and terminology to align with what was asked. I'm checking the practical magnitude section against what's needed. The current text discusses the typical BCS span from the 80-relation pool and compares quartiles, but I need to integrate the independent 16-relation pool results and clarify that both effects are meaningful yet modest compared to the extreme 31.2 pp gap. I'm tracking down all the places where the 9.1pp figure appears in the results section—it's in the table, the caption, and a couple of explanatory sentences. The task is to shift these from just citing the raw number to framing them within the slope consistency narrative, so I need to update the abstract and results file accordingly. I see the distinction now—the table data at line 79 shows the actual measured difference of -9.1pp from the extreme-batch comparison, which should remain unchanged since it's empirical data. The task is asking me to replace narrative references to 9.1pp in §4.3 with the bootstrapped quartile gap of -7.42pp from Table 4, which comes from a different analytical approach. These are separate analyses with different methodologies, so I need to be careful about which occurrences get replaced and which stay as measured values. I need to be strategic about which numbers to keep and which to reframe. The -9.1 is actual measured data from the extreme-batch comparison in the table, so that stays. But I should reframe how I present it in the caption and narrative to emphasize the regression slopes and consistency across pools rather than treating the extreme-batch gap as the main finding. For line 88, I can keep the description of the table data but should add context about the bootstrapped confidence intervals or point toward the within-pool analysis instead.

For line 117, I need to shift away from comparing the raw gaps (31.2 vs 9.1) and instead reference the quartile gaps from Table 4, which gives a more principled comparison that doesn't depend on which batch extremes I'm looking at. The task is asking me to find all instances of "9.1" in results.tex and handle each one—some stay as table data, others get reframed to reference the bootstrapped estimates or quartile-based comparisons. I'm settling on keeping the -9.1pp as the measured extreme-batch comparison in the table since that's the actual data, but shifting the narrative focus away from it toward the -7.42pp quartile gap or slope consistency findings instead. Now I'm searching through the document for all instances of "31.2" to identify what needs reframing there—I see it appears in the figure caption, main text comparisons, table values, and confidence intervals across multiple locations. I'm working through several revisions to the paper. For the MAVEN abstract section, I need to expand the mention of same-domain schemas to include more detail about the centrality confound. I'm also replacing instances of "model-invariant" with clearer phrasing like "consistent across tested models" in both the results and abstract sections. Finally, I'm checking whether the results file mentions v1/v2 prompts explicitly so I can add the appropriate appendix reference where needed.

Now I'm planning out the specific edits to results.tex, starting with updating the numerical values and confidence interval descriptions on line 25, then working through the remaining changes systematically. the 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range, while regression slopes remain consistent across pools. The 16-relation condition used a single extreme batch per BCS level, which limits the bootstrap confidence intervals. At the 16-relation scale, the extreme-batch gap is 9.1\,pp, but at 80 relations this widens substantially to 31.2\,pp (95\% CI: [17.7, 42.7]), with the larger gap driven by the broader range of batch compositions tested. I'm working through specific edits to clarify terminology and improve precision. For line 124, I need to replace "model-invariant" with "consistent across tested models" in the first instance where it describes high-BCS accuracy, while leaving the second occurrence that uses different phrasing. Then I'm moving on to revise the abstract.tex file with similar clarity improvements. I'm working through the precision and recall metrics for the 2A figure—recall drops from 0.72 to 0.42 as candidate types increase, while precision rises from 0.11 to 0.52, creating an inverted-U shape in F1 at intermediate counts where the trade-off is most balanced. I need to refine some of the numerical precision in the confidence intervals and update the statistical language from permutation testing to bootstrap CIs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "58f175de-61a0-44ee-8da9-7d841f8e918d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6Qwv9Sh6TCa6N2uXjavGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6253,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6253
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

I'll now make all the edits. Let me start with the results.tex changes, then abstract.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "d63eacde-1633-488c-80d0-da53f822d10d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6Qwv9Sh6TCa6N2uXjavGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6253,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6253
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

<details open><summary>🔧 Tool call — Edit · `toolu_01HrvVVhPG9No9oW9iBwFpBj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability",
  "new_string": "0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "c0ca8034-ce49-48a8-8a9f-9b42a9fb74bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6Qwv9Sh6TCa6N2uXjavGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6253,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6253
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

_source line 12 · 2026-05-16T03:44:50.325Z_

<details><summary>↩ Tool result · reported error · `toolu_01HrvVVhPG9No9oW9iBwFpBj`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "0f665f84-65fe-434f-9160-82016d8b82f6",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01JcYpiPXSUs7gRPxrfV2E7e`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled})",
  "new_string": "accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "c77968d5-247c-4bb0-862c-f54e4e4251c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6Qwv9Sh6TCa6N2uXjavGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6253,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6253
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

_source line 14 · 2026-05-16T03:44:51.510Z_

<details><summary>↩ Tool result · reported error · `toolu_01JcYpiPXSUs7gRPxrfV2E7e`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "bf633da2-428e-4b58-9cc1-bc197de340e8",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_01LLnnGj9Rru4LvqiL9hEN7u`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.",
  "new_string": "The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "36c4c824-b082-4eda-8035-1f20ad5a53eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6Qwv9Sh6TCa6N2uXjavGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6253,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6253
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

_source line 16 · 2026-05-16T03:44:53.403Z_

<details><summary>↩ Tool result · reported error · `toolu_01LLnnGj9Rru4LvqiL9hEN7u`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "6dff2615-0fb6-4627-ba42-4d0845121889",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_01DHmkKe5ojUPqHkV8U5RdoN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]).",
  "new_string": "At the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool}). At 80 relations, the extreme-batch gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7])."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "0a4755df-4fc0-46ec-959a-080f4ee2f369",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6Qwv9Sh6TCa6N2uXjavGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6253,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6253
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

_source line 18 · 2026-05-16T03:44:56.017Z_

<details><summary>↩ Tool result · reported error · `toolu_01DHmkKe5ojUPqHkV8U5RdoN`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "baa49b0e-621a-4c1e-96d7-33c640626c7f",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_019XbAGShhr8t1VsvEisH8jX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.",
  "new_string": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\\,pp vs.\\ $-$7.42\\,pp; Table~\\ref{tab:within_pool})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "b0601414-3ae6-47e2-8387-d3875267c240",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6Qwv9Sh6TCa6N2uXjavGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6253,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6253
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

_source line 20 · 2026-05-16T03:44:57.246Z_

<details><summary>↩ Tool result · reported error · `toolu_019XbAGShhr8t1VsvEisH8jX`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "715d8bf6-bcaa-4d48-9aa7-95f443ca7124",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_012zD3WxeVmZHWXwpvPdQtir`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "high-BCS accuracy is model-invariant: both models converge",
  "new_string": "high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "403b9d00-53be-4fbb-942c-a4062184ee4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6Qwv9Sh6TCa6N2uXjavGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6253,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6253
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

_source line 22 · 2026-05-16T03:44:58.647Z_

<details><summary>↩ Tool result · reported error · `toolu_012zD3WxeVmZHWXwpvPdQtir`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "ca1cefe6-2840-42a1-bd5c-e831da266fbd",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01PTxoHTevVF6UCqn6vdTYL4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp",
  "new_string": "reaching 77--87\\% of Qwen3-32B's extreme-batch gap ($-$31.2\\,pp)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "6682b77b-45b3-4b13-a1c5-973447716573",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6Qwv9Sh6TCa6N2uXjavGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6253,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6253
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

_source line 24 · 2026-05-16T03:45:00.014Z_

<details><summary>↩ Tool result · reported error · `toolu_01PTxoHTevVF6UCqn6vdTYL4`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "3f0dea8e-55c4-4a50-88d3-69b385b90a20",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01W7SKTcxGYJMEBNpXZgGyfN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "a task-inherent difficulty floor independent of model scale.",
  "new_string": "a task-inherent difficulty floor consistent across the tested models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "1fc55af8-72cf-4bc0-88b1-a5fec725b2c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6Qwv9Sh6TCa6N2uXjavGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6253,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6253
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

_source line 26 · 2026-05-16T03:45:00.800Z_

<details><summary>↩ Tool result · reported error · `toolu_01W7SKTcxGYJMEBNpXZgGyfN`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "56dff866-13e8-4e7d-961f-d9b5018715c1",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Assistant

_source line 27_

Files were modified externally. Let me re-read both files and retry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "de14ead2-2ea7-438c-b195-65fa7d955f69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5g4irHmFNg8EGNW6uAXGh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7736,
      "cache_read_input_tokens": 30889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7736
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

<details open><summary>🔧 Tool call — Read · `toolu_01Rw1EJTJDcLnAm254tu1s6B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "d7b8898c-1142-4716-94c5-59c8109a7d43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5g4irHmFNg8EGNW6uAXGh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7736,
      "cache_read_input_tokens": 30889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7736
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

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01QzkSxujWEUjTCmTPbBJo55`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "de740a92-2b14-49d8-969e-56a833ad8bce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5g4irHmFNg8EGNW6uAXGh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7736,
      "cache_read_input_tokens": 30889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7736
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

_source line 30 · 2026-05-16T03:45:04.615Z_

<details><summary>↩ Tool result · `toolu_01QzkSxujWEUjTCmTPbBJo55`</summary>

```text
File unchanged since last read. The content from the earlier Read tool_result in this conversation is still current — refer to that instead of re-reading.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "7fd6c8b8-bcdb-43df-a7db-6999ff52dac4",
  "tool_use_result": {
    "type": "file_unchanged",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
    }
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T03:45:04.624Z_

<details><summary>↩ Tool result · `toolu_01Rw1EJTJDcLnAm254tu1s6B`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
25	
26	\paragraph{NER (Few-NERD).}
27	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\,=\,22$ to 0.55 at count${}\,=\,44$; 95\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
28	
29	\paragraph{RE (FewRel).}
30	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)
31	
32	\paragraph{ED (MAVEN).}
33	In contrast to NER and RE, MAVEN relaxed F1 \emph{increases} from 0.106 at count${}\,=\,1$ to 0.247 at count${}\,=\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \S\ref{sec:centrality_confound}.
34	
35	\paragraph{Cross-model replication.}
36	Channel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\,pp recall decline (0.702 at count${}\,=\,1$ to 0.273 at count${}\,=\,64$), compared to $-$34\,pp for Qwen3-32B (Table~\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.
37	
38	\paragraph{Summary.}
39	Schema size degrades extraction quality for NER and RE (Channel~1: count $\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\S\ref{sec:bcs_controlled}).
40	
41	\subsection{Pairwise Confusability and Type Confusion}
42	\label{sec:pairwise}
43	
44	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
45	
46	\begin{table}[t]
47	\centering
48	\small
49	\resizebox{\columnwidth}{!}{%
50	\begin{tabular}{llrrrrr}
51	\toprule
52	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
53	\midrule
54	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\
55	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\
56	\bottomrule
57	\end{tabular}}
58	\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}
59	\label{tab:pairwise}
60	\end{table}
61	
62	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$, meaning pairwise confusability explains roughly 1.5\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\S\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.
63	
64	Spearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\rho = 0.168$ ($p = 7.3 \times 10^{-14}$) and MiniLM yields $\rho = 0.144$ ($p = 1.7 \times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\rho = 0.272$ for Qwen3 and $\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\rho = 0.27\text{--}0.31$) characterize the signal among types the model actually confuses.
65	
66	The remaining ${\sim}$98\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\,pp under extreme-batch comparison (\S\ref{sec:bcs_controlled}; typical-batch gap ${\approx}\,2\text{--}4$\,pp, \S\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.
67	
68	\subsection{BCS-Controlled Experiments}
69	\label{sec:bcs_controlled}
70	
71	To move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.
72	
73	\begin{table}[t]
74	\centering
75	\small
76	\resizebox{\columnwidth}{!}{%
77	\begin{tabular}{lcrrrr}
78	\toprule
79	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
80	\midrule
81	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
82	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
83	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
84	\bottomrule
85	\end{tabular}}
86	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\,pp at 16 relations to 31.2\,pp at 80 relations (extreme-batch comparison; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
87	\label{tab:bcs_controlled}
88	\end{table}
89	
90	At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\,pp (extreme-batch comparison; 95\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\,=\,16$, the gap remains 31.2\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\,=\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\,pp (count 8) and $-$31.8\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.
91	
92	The larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\S\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.
93	
94	\paragraph{Within-pool controlled comparison.}
95	\label{sec:within_pool}
96	A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\ref{tab:within_pool}).
97	
98	\begin{table}[t]
99	\centering
100	\small
101	\resizebox{\columnwidth}{!}{%
102	\begin{tabular}{lrrrrrrr}
103	\toprule
104	& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
105	\cmidrule(lr){2-5} \cmidrule(lr){6-7}
106	\textbf{Setting} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
107	\midrule
108	Independent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\
109	80-pool $\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\
110	Full 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\
111	\midrule
112	\multicolumn{7}{l}{\footnotesize Permutation test (16-rel vs.\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\
113	\bottomrule
114	\end{tabular}}
115	\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
116	\label{tab:within_pool}
117	\end{table}
118	
119	The within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\,pp vs.\ $-$7.42\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\ 0.65--0.90; see Appendix~\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\,pp vs.\ 9.1\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \S\ref{sec:practical_magnitude} for typical-batch magnitudes).
120	
121	\paragraph{Practical magnitude.}
122	\label{sec:practical_magnitude}
123	For representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0]), roughly 7\% of the 31.2\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\%, versus 78.9\% for top-quartile batches, a gap of 3.9\,pp. The 31.2\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\,pp.
124	
125	\paragraph{Cross-model validation.}
126	The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\,pp at count${}\,=\,8$ (low-BCS 78.1\% vs.\ high-BCS 51.0\%) and $-$23.9\,pp at count${}\,=\,16$ (75.5\% vs.\ 51.6\%), reaching 77--87\% of Qwen3-32B's $-$31.2\,pp extreme-batch gap. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\approx$51\% under high confusability (count${}\,=\,8$: 51.0\% vs.\ 51.0\%; count${}\,=\,16$: 51.6\% vs.\ 51.6\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.
127	
128	\subsection{Multi-Channel Degradation}
129	\label{sec:multi_channel}
130	
131	We decompose extraction errors into an error taxonomy (full data in Table~\ref{tab:error_taxonomy}, Appendix~\ref{sec:appendix_figures}; see also Figure~\ref{fig:error_taxonomy} in Appendix~\ref{sec:appendix_figures}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\%), but NER rates are substantially higher (43--65\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.
132	
133	These results establish two degradation channels: \textbf{Channel~1} (count $\to$ recall decline, \S\ref{sec:count_curves}) and \textbf{Channel~2} (confusability $\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.
134	
135	\subsection{Centrality Confound on Homogeneous Schemas}
136	\label{sec:centrality_confound}
137	
138	Per-type analysis on MAVEN reveals an anomalous \emph{positive} BCS--error correlation (Qwen3 $\rho = +0.184$, $p = 0.025$; MiniLM $\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "2c16d37b-156c-49d5-98ca-277a0c5df006",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
      "numLines": 138,
      "startLine": 1,
      "totalLines": 138
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
The file has been modified by the other worker. Let me compare with my first read:

Changes I can see:
1. Line 4 added: "Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts})." — This handles C1 (prompt appendix reference).
2. Line 66: Already changed to "accuracy gaps reaching 31.2\,pp under extreme-batch comparison (\S\ref{sec:bcs_controlled}; typical-batch gap ${\approx}\,2\text{--}4$\,pp, \S\ref{sec:practical_magnitude})" — C3 partially done here.


3. Several more locations have been updated with the extreme-batch caveat and cross-references: the figure caption at line 86, the text at line 90 with confidence intervals, line 119 comparing the gap magnitudes, and line 126 starting to reference the performance comparison.
4. Line 131 now includes a reference to the error taxonomy figure in the appendix.
5. Looking at what remains, I need to check line 27 in results.tex — it still needs precision updates on those decimal values and a switch to bootstrap confidence intervals language, plus removal of the permutation p-value.
6. For the C2 section around lines 86 and 90, I need to reframe how the 9.1 percentage point gap is described and ensure the batch comparison language is complete.

7. Line 119 needs the same treatment—replacing the 9.1pp reference with the quartile gap framing.

8. The C3 section shows mixed progress: line 66 is done, line 86 needs the "from 9.1pp to 31.2pp" framing replaced, line 90 already has the caveat, line 119 still needs updating, and line 126 is complete.

9. For W12, I'm checking the model-invariant section starting at line 126, which appears to be cut off mid-sentence.

Now I'm going through the remaining edits systematically—the W12 model-invariant phrasing, W7 MAVEN in the abstract, W12's "model-invariant floor" in the abstract, and C2's "31.2 vs. 9.1pp" comparison all still need to be addressed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "8b8cabd3-5eb4-4886-9765-3d3c4eb45501",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aUKxARZzVQtDbED7CESBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 60,
      "cache_creation_input_tokens": 5958,
      "cache_read_input_tokens": 38625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5958
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

_source line 33_

The other worker has already made some changes. Let me apply the remaining edits. Starting with results.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "22d34c72-baaf-4be8-9271-951a619a8b43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aUKxARZzVQtDbED7CESBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 60,
      "cache_creation_input_tokens": 5958,
      "cache_read_input_tokens": 38625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5958
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

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_018kXSLNc8xYGm55jewHD95R`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability",
  "new_string": "0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "fdc13f9b-7f85-4502-afc2-8f9b4165c1db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aUKxARZzVQtDbED7CESBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 60,
      "cache_creation_input_tokens": 5958,
      "cache_read_input_tokens": 38625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5958
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

_source line 35 · 2026-05-16T03:45:29.391Z_

<details><summary>↩ Tool result · `toolu_018kXSLNc8xYGm55jewHD95R`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "ab68a436-bdb5-455c-acf6-a0886d217af0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability",
    "newString": "0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 24,
        "oldLines": 7,
        "newStart": 24,
        "newLines": 7,
        "lines": [
          " We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).",
          " ",
          " \\paragraph{NER (Few-NERD).}",
          "-Recall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.",
          "+Recall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.",
          " ",
          " \\paragraph{RE (FewRel).}",
          " Accuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)"
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

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_014bg1Fwe9EoY1vcJSLwFUk4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
  "new_string": "The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "d6e0a223-8f87-40f2-be69-a89febb1b220",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aUKxARZzVQtDbED7CESBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 60,
      "cache_creation_input_tokens": 5958,
      "cache_read_input_tokens": 38625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5958
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

_source line 37 · 2026-05-16T03:45:32.202Z_

<details><summary>↩ Tool result · `toolu_014bg1Fwe9EoY1vcJSLwFUk4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "f7ce610a-621d-4b59-8807-d85dc108e11c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
    "newString": "The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 83,
        "oldLines": 7,
        "newStart": 83,
        "newLines": 7,
        "lines": [
          " 80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\",
          " \\bottomrule",
          " \\end{tabular}}",
          "-\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}",
          "+\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}",
          " \\label{tab:bcs_controlled}",
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

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_01B94ZRv3HYF598shZSnLAjJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points.",
  "new_string": "At the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "32d89dc5-03c9-4dc2-b4e8-7a5bad4494be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aUKxARZzVQtDbED7CESBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 60,
      "cache_creation_input_tokens": 5958,
      "cache_read_input_tokens": 38625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5958
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

_source line 39 · 2026-05-16T03:45:34.526Z_

<details><summary>↩ Tool result · `toolu_01B94ZRv3HYF598shZSnLAjJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "03e23581-0717-44a9-aa07-3b1561bb9c8e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points.",
    "newString": "At the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool}).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 87,
        "oldLines": 7,
        "newStart": 87,
        "newLines": 7,
        "lines": [
          " \\label{tab:bcs_controlled}",
          " \\end{table}",
          " ",
          "-At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.",
          "+At the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool}). At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.",
          " ",
          " The larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.",
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

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_011evJEu3AwBMnkmhKEd2m2e`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
  "new_string": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\\,pp vs.\\ $-$7.42\\,pp; Table~\\ref{tab:within_pool})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "3d3fb506-2522-4e8f-bf74-7793fb5abd85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aUKxARZzVQtDbED7CESBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 60,
      "cache_creation_input_tokens": 5958,
      "cache_read_input_tokens": 38625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5958
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

_source line 41 · 2026-05-16T03:45:36.417Z_

<details><summary>↩ Tool result · `toolu_011evJEu3AwBMnkmhKEd2m2e`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "1131c6e8-49ec-4540-a4eb-30cf7a75a489",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
    "newString": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\\,pp vs.\\ $-$7.42\\,pp; Table~\\ref{tab:within_pool}).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool}). At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 116,
        "oldLines": 7,
        "newStart": 116,
        "newLines": 7,
        "lines": [
          " \\label{tab:within_pool}",
          " \\end{table}",
          " ",
          "-The within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
          "+The within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\\,pp vs.\\ $-$7.42\\,pp; Table~\\ref{tab:within_pool}).",
          " ",
          " \\paragraph{Practical magnitude.}",
          " \\label{sec:practical_magnitude}"
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

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01M1CWYPM1oVBrYVXgKnxv6a`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "high-BCS accuracy is model-invariant: both models converge",
  "new_string": "high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "e20d8cf7-c0b9-48ba-926c-d01f1fd860b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aUKxARZzVQtDbED7CESBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 60,
      "cache_creation_input_tokens": 5958,
      "cache_read_input_tokens": 38625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5958
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

_source line 43 · 2026-05-16T03:45:37.843Z_

<details><summary>↩ Tool result · `toolu_01M1CWYPM1oVBrYVXgKnxv6a`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "b9d289ad-89d2-4c19-a293-e67d145169bd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "high-BCS accuracy is model-invariant: both models converge",
    "newString": "high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool}). At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\\,pp vs.\\ $-$7.42\\,pp; Table~\\ref{tab:within_pool}).\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 123,
        "oldLines": 7,
        "newStart": 123,
        "newLines": 7,
        "lines": [
          " For representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.",
          " ",
          " \\paragraph{Cross-model validation.}",
          "-The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.",
          "+The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.",
          " ",
          " \\subsection{Multi-Channel Degradation}",
          " \\label{sec:multi_channel}"
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

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_013uSc5rgaQgPZeoJmcckoGE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "a task-inherent difficulty floor independent of model scale.",
  "new_string": "a task-inherent difficulty floor consistent across the tested models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "dab12e58-bd45-4130-8b99-508b0c275029",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aUKxARZzVQtDbED7CESBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 60,
      "cache_creation_input_tokens": 5958,
      "cache_read_input_tokens": 38625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5958
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

_source line 45 · 2026-05-16T03:45:39.055Z_

<details><summary>↩ Tool result · `toolu_013uSc5rgaQgPZeoJmcckoGE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "5c1fb874-f394-4407-8adb-d01224337e8c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "a task-inherent difficulty floor independent of model scale.",
    "newString": "a task-inherent difficulty floor consistent across the tested models.",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool}). At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\\,pp vs.\\ $-$7.42\\,pp; Table~\\ref{tab:within_pool}).\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 123,
        "oldLines": 7,
        "newStart": 123,
        "newLines": 7,
        "lines": [
          " For representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.",
          " ",
          " \\paragraph{Cross-model validation.}",
          "-The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.",
          "+The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor consistent across the tested models.",
          " ",
          " \\subsection{Multi-Channel Degradation}",
          " \\label{sec:multi_channel}"
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

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Good, results.tex edits done. Now let me do the abstract.tex edits. Let me re-read it first since it might have been modified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "51d5e27d-8314-40cb-9c85-d29960f9d669",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gu2zfEa61CrECxRvfgUffk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 44583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3018
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

_source line 47_

Now the abstract.tex edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "771a6c3d-98d4-4979-b9b2-b2c3d7bfdffb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gu2zfEa61CrECxRvfgUffk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 44583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3018
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

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_0115zNVpPb4gkfu3uXR18Ukb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "b8e17c82-d3f4-4a2f-8cc5-6a7b8a80d48e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gu2zfEa61CrECxRvfgUffk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 44583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3018
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

_source line 49 · 2026-05-16T03:45:44.909Z_

<details><summary>↩ Tool result · `toolu_0115zNVpPb4gkfu3uXR18Ukb`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), with the quartile gap reaching $-$7.4\,pp (95\% CI: [$-$9.4, $-$5.5]) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant (\S\ref{sec:centrality_confound}). Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "10fa6b67-cd1c-4728-91a6-811b244b14fd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTraining-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), with the quartile gap reaching $-$7.4\\,pp (95\\% CI: [$-$9.4, $-$5.5]) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant (\\S\\ref{sec:centrality_confound}). Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.\n\\end{abstract}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Assistant

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
The abstract has already been significantly modified by the other worker. Let me check what's already done and what still needs my attention:

1. **C2 (9.1pp replacement)**: Already done — "31.2 vs.\ 9.1\,pp" is gone, replaced with "the quartile gap reaching $-$7.4\,pp (95\% CI: [$-$9.4, $-$5.5]) on the independent 16-relation pool"

2. **W7 (MAVEN in abstract)**: Already done — "On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant (\S\ref{sec:centrality_confound})"
   
   But wait, the task says abstracts can't have \S references. I need to remove that cross-reference and either replace it with the section number directly or just drop the reference entirely.

3. **W12 (model-invariant)**: Already done — changed to "a floor consistent across both tested models"

4. **C3 (31.2pp caveat)**: The 31.2 percentage point figure is no longer in the abstract, replaced with the quartile gap instead. The task originally wanted that caveat included, but the current version is actually cleaner and more informative by focusing on the quartile gap with confidence intervals. I think this revision works better.

Looking at what still needs fixing: the `\S\ref{sec:centrality_confound}` needs to go since abstracts should be self-contained without cross-references.

Actually, wait — the task says abstracts can't have `\S` references but then suggests using `(\S4.5)` as a hard-coded alternative. That's still a section reference, just not dynamic. Looking at the abstract, it already has the reference in place, and since many ML papers do include section citations in their abstracts, this might be acceptable as-is.

Let me reconsider the structure though. The original text about "same-domain schemas are subject to a centrality confound" got replaced with the MAVEN sentence, which splits the idea across two sentences now. That's actually cleaner — the confusability impact on NER stands alone, and the MAVEN finding follows separately. I should verify the current state matches this structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "46637e53-fbad-4c09-a08e-ac0afbdaa325",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ckDKja6QZ658eQmmGJwfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 47601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 639
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

_source line 51_

The abstract has already been updated by the other worker for C2, W7, and W12. One remaining issue: the abstract uses `\S\ref{sec:centrality_confound}` which should not use cross-references in an abstract. Let me fix that.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "f8814c0c-7ed0-4eb3-915c-cf084036a301",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ckDKja6QZ658eQmmGJwfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 47601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 639
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

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01PXxVLX4eWA5pkQm5j9rmiR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "old_string": "though pairwise confusability remains significant (\\S\\ref{sec:centrality_confound})",
  "new_string": "though pairwise confusability remains significant"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "fee29454-c06e-44b1-9e32-94318fcaa5d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ckDKja6QZ658eQmmGJwfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 47601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 639
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

_source line 53 · 2026-05-16T03:46:10.304Z_

<details><summary>↩ Tool result · `toolu_01PXxVLX4eWA5pkQm5j9rmiR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "37ec73a6-7427-4be0-8c34-fcc59d6cc2cf",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "oldString": "though pairwise confusability remains significant (\\S\\ref{sec:centrality_confound})",
    "newString": "though pairwise confusability remains significant",
    "originalFile": "\\begin{abstract}\nTraining-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), with the quartile gap reaching $-$7.4\\,pp (95\\% CI: [$-$9.4, $-$5.5]) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant (\\S\\ref{sec:centrality_confound}). Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.\n\\end{abstract}",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\begin{abstract}",
          "-Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), with the quartile gap reaching $-$7.4\\,pp (95\\% CI: [$-$9.4, $-$5.5]) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant (\\S\\ref{sec:centrality_confound}). Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.",
          "+Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), with the quartile gap reaching $-$7.4\\,pp (95\\% CI: [$-$9.4, $-$5.5]) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.",
          " \\end{abstract}",
          "\\ No newline at end of file"
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

_source line 54_

Now let me verify results.tex for any remaining "9.1" or "model-invariant" occurrences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "27edcece-7433-46d5-872e-3d9df92beb73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159upmufdhQCqShF5YVhaaG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 48240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1411
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

_source line 55_

<details open><summary>🔧 Tool call — Grep · `toolu_01GHCqsSERD269T4vyo3Dspy`</summary>

```json
{
  "pattern": "9\\.1",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
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
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "d6510589-dc24-4d67-bf06-2cc16758bcf7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159upmufdhQCqShF5YVhaaG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 48240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1411
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

_source line 56 · 2026-05-16T03:46:14.070Z_

<details><summary>↩ Tool result · `toolu_01GHCqsSERD269T4vyo3Dspy`</summary>

```text
81:16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
90:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "37c2bce5-d58e-412b-b40e-a4826d014eee",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "81:16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n90:[Omitted long matching line]",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Grep · `toolu_01VChL7tYpAehVpQFxnZGEHX`</summary>

```json
{
  "pattern": "model-invariant",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
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
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "2862175e-1db1-44d9-9322-3b7e0893572b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159upmufdhQCqShF5YVhaaG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 48240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1411
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

_source line 58 · 2026-05-16T03:46:14.561Z_

<details><summary>↩ Tool result · `toolu_01VChL7tYpAehVpQFxnZGEHX`</summary>

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
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "80b3423a-0f70-4c2a-b295-6ec1a919d25b",
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

_source line 59_

<details open><summary>🔧 Tool call — Grep · `toolu_01Wy9Yu5WDKfB2cpHQPZsSfb`</summary>

```json
{
  "pattern": "model-invariant",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
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
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "6700e314-7a58-4da3-8a83-f10bc88aadbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159upmufdhQCqShF5YVhaaG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 48240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1411
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

_source line 60 · 2026-05-16T03:46:15.466Z_

<details><summary>↩ Tool result · `toolu_01Wy9Yu5WDKfB2cpHQPZsSfb`</summary>

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
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "28c6b08f-8159-4c31-9cfe-e54ea30f53f4",
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

_source line 61_

<details open><summary>🔧 Tool call — Grep · `toolu_01UbVuqbQDZavYLqFo1dsMXN`</summary>

```json
{
  "pattern": "31\\.2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
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
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "70272032-3888-4033-ae92-e7bcabdee5e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159upmufdhQCqShF5YVhaaG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 48240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1411
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

_source line 62 · 2026-05-16T03:46:16.195Z_

<details><summary>↩ Tool result · `toolu_01UbVuqbQDZavYLqFo1dsMXN`</summary>

```text
66:[Omitted long matching line]
82:80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
83:80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
86:\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
90:[Omitted long matching line]
119:[Omitted long matching line]
123:[Omitted long matching line]
126:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "d9a3c3fb-cc19-4b11-bb08-6560cb48d7c7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "66:[Omitted long matching line]\n82:80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n83:80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n86:\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n90:[Omitted long matching line]\n119:[Omitted long matching line]\n123:[Omitted long matching line]\n126:[Omitted long matching line]",
    "numLines": 8
  }
}
```

</details>

---

### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Let me check the 9.1 occurrences:
- Line 81: Table data `$-$9.1` — this is actual measured data in the table, keep it.
- Line 90: Let me check what line 90 says now.

And for 31.2:
- Line 66: Already has "extreme-batch comparison" caveat
- Lines 82-83: Table data, keep
- Line 86: Caption already reframed
- Line 90: Need to check
- Line 119: Already updated


- Lines 123 and 126: Both already have "extreme-batch gap" context

Let me verify lines 90 and 119 to make sure they're consistent with the rest.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "5eca9f31-cd11-4f3d-a2c6-c16621592163",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSTASNTVsPz1P6GZ4HAo6C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 915,
      "cache_read_input_tokens": 49651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 915
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

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_01GjcsgyPFW6F6pnoFKWVRf3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": 88,
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
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "a99e5f4e-1c2a-487c-9ece-14d90fda0b73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSTASNTVsPz1P6GZ4HAo6C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 915,
      "cache_read_input_tokens": 49651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 915
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

_source line 65 · 2026-05-16T03:46:22.343Z_

<details><summary>↩ Tool result · `toolu_01GjcsgyPFW6F6pnoFKWVRf3`</summary>

```text
88	\end{table}
89	
90	At the 16-relation scale, the extreme-batch gap is 9.1\,pp (single batch per level; Table~\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\,pp (CI: [$-$9.40, $-$5.54]; Table~\ref{tab:within_pool}). At 80 relations, the gap reaches 31.2\,pp (extreme-batch comparison; 95\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\,=\,16$, the gap remains 31.2\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\,=\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\,pp (count 8) and $-$31.8\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.
91	
92	The larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\S\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "f8bbe27e-aba8-41ff-bcde-2282a862cbde",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\end{table}\n\nAt the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool}). At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.",
      "numLines": 5,
      "startLine": 88,
      "totalLines": 138
    }
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_01RCznPzgBYQbuweNsrAaJkj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": 117,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "257fefeb-815e-454b-8d53-0fa078412ab2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSTASNTVsPz1P6GZ4HAo6C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 915,
      "cache_read_input_tokens": 49651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 915
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

_source line 67 · 2026-05-16T03:46:22.773Z_

<details><summary>↩ Tool result · `toolu_01RCznPzgBYQbuweNsrAaJkj`</summary>

```text
117	\end{table}
118	
119	The within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\,pp vs.\ $-$7.42\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\ 0.65--0.90; see Appendix~\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\,pp vs.\ $-$7.42\,pp; Table~\ref{tab:within_pool}).
120	
121	\paragraph{Practical magnitude.}
122	\label{sec:practical_magnitude}
123	For representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0]), roughly 7\% of the 31.2\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\%, versus 78.9\% for top-quartile batches, a gap of 3.9\,pp. The 31.2\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\,pp.
124	
125	\paragraph{Cross-model validation.}
126	The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\,pp at count${}\,=\,8$ (low-BCS 78.1\% vs.\ high-BCS 51.0\%) and $-$23.9\,pp at count${}\,=\,16$ (75.5\% vs.\ 51.6\%), reaching 77--87\% of Qwen3-32B's $-$31.2\,pp extreme-batch gap. Strikingly, high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge to $\approx$51\% under high confusability (count${}\,=\,8$: 51.0\% vs.\ 51.0\%; count${}\,=\,16$: 51.6\% vs.\ 51.6\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor consistent across the tested models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "cd1877af-fedc-4551-9d1f-e6b3dbb82e31",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\\,pp vs.\\ $-$7.42\\,pp; Table~\\ref{tab:within_pool}).\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor consistent across the tested models.",
      "numLines": 10,
      "startLine": 117,
      "totalLines": 138
    }
  }
}
```

</details>

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
Let me check the status:

**9.1 in results.tex:**
- Line 81: Table data `$-$9.1` — keep (actual measured data)
- Line 90: "the extreme-batch gap is 9.1\,pp (single batch per level; Table~\ref{tab:bcs_controlled})" — this is fine, it's properly contextualized as extreme-batch and supplemented with quartile gap


- Line 90: "The effect is stable across count levels: at count${}\,=\,16$, the gap remains 31.2\,pp (CI: [22.9, 39.6])" — this last mention needs a caveat added to clarify it's the extreme-batch gap.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "8609ccf9-82db-4b44-b5f1-f6c36cc09d76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJk8wNkafkpQkw7n2oWCQG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1771,
      "cache_read_input_tokens": 50566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1771
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

_source line 69_

One remaining 31.2 without caveat on line 90.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "acf795f7-c81a-4257-8444-05f100985cdf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJk8wNkafkpQkw7n2oWCQG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1771,
      "cache_read_input_tokens": 50566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1771
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

_source line 70_

<details open><summary>🔧 Tool call — Edit · `toolu_013DtUjEPy5pfTb5vETY6VR2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "the gap remains 31.2\\,pp (CI: [22.9, 39.6])",
  "new_string": "the extreme-batch gap remains 31.2\\,pp (CI: [22.9, 39.6])"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "21ed6fa8-6f3a-4ba5-bad5-79b4a5577bce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJk8wNkafkpQkw7n2oWCQG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1771,
      "cache_read_input_tokens": 50566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1771
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

_source line 71 · 2026-05-16T03:46:32.349Z_

<details><summary>↩ Tool result · `toolu_013DtUjEPy5pfTb5vETY6VR2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "11a54a43-36e2-43a3-b628-432bddbff409",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "the gap remains 31.2\\,pp (CI: [22.9, 39.6])",
    "newString": "the extreme-batch gap remains 31.2\\,pp (CI: [22.9, 39.6])",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool}). At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\\,pp vs.\\ $-$7.42\\,pp; Table~\\ref{tab:within_pool}).\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor consistent across the tested models.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 87,
        "oldLines": 7,
        "newStart": 87,
        "newLines": 7,
        "lines": [
          " \\label{tab:bcs_controlled}",
          " \\end{table}",
          " ",
          "-At the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool}). At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.",
          "+At the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool}). At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the extreme-batch gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.",
          " ",
          " The larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.",
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

_source line 72_

Now let me compile the paper to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "d12817a2-fea4-4d02-b71d-3c1b7ce584c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeiN3nYcmJpuhZgoYb3Uzt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 52337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 691
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

_source line 73_

<details open><summary>🔧 Tool call — Bash · `toolu_019qSXkfEXCMHzvWPoB3V98K`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "8e7d7493-4011-41d9-9a11-199c3d067a80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeiN3nYcmJpuhZgoYb3Uzt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 52337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 691
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

### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bbe7wrez3",
  "tool_use_id": "toolu_019qSXkfEXCMHzvWPoB3V98K",
  "description": "First pdflatex pass",
  "task_type": "local_bash",
  "uuid": "ae96c86d-4e62-4c10-a036-007dc6e633f2",
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848"
}
```

---

### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bbe7wrez3",
  "tool_use_id": "toolu_019qSXkfEXCMHzvWPoB3V98K",
  "status": "completed",
  "output_file": "",
  "summary": "First pdflatex pass",
  "uuid": "9b7fec7b-7df3-4f76-8965-1c7679193e6e",
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848"
}
```

---

### Tool result

_source line 76 · 2026-05-16T03:46:40.795Z_

<details><summary>↩ Tool result · `toolu_019qSXkfEXCMHzvWPoB3V98K`</summary>

```text
                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...

! Text line contains an invalid character.
l.230 ...^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@
                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...

! Text line contains an invalid character.
l.230 ...^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@
                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...

! Text line contains an invalid character.
l.230 ...^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@
                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...

! Text line contains an invalid character.
l.230 ...^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@
                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...
(That makes 100 errors; please try again.)
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "38bbbb95-766a-4995-b040-6ac0acea1537",
  "tool_use_result": {
    "stdout": "                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...\n\n! Text line contains an invalid character.\nl.230 ...^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@\n                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...\n\n! Text line contains an invalid character.\nl.230 ...^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@\n                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...\n\n! Text line contains an invalid character.\nl.230 ...^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@\n                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...\n\n! Text line contains an invalid character.\nl.230 ...^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@\n                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...\n(That makes 100 errors; please try again.)\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on main.log.",
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

_source line 77_

<details><summary>Logged reasoning block</summary>

```text
There's a binary/null character issue in one of the files. Let me check which file has the problem. The error is at line 230 of what appears to be main.tex or an included file. Let me check main.tex to see what's on/around line 230.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "a4c2afc0-4db7-486c-9b7d-09ca7f7c242e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JktsWer9rCHvT8f6Lu44Bc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 53028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 496
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

_source line 78_

There's a corrupted file with null bytes. Let me investigate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "4d50d108-33da-4d71-95a2-4e08ca3a0f92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JktsWer9rCHvT8f6Lu44Bc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 53028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 496
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

_source line 79_

<details open><summary>🔧 Tool call — Bash · `toolu_01WmXaQcQPS8fzf3ogeAw2ca`</summary>

```json
{
  "command": "grep -rl $'\\x00' *.tex 2>/dev/null || echo \"no null bytes in .tex files\"",
  "description": "Find files with null bytes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "719e86f6-e47c-439c-9a56-b02872da14d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JktsWer9rCHvT8f6Lu44Bc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 53028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 496
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

_source line 80 · 2026-05-16T03:46:46.767Z_

<details><summary>↩ Tool result · `toolu_01WmXaQcQPS8fzf3ogeAw2ca`</summary>

```text
abstract.tex
checklist.tex
conclusion.tex
discussion.tex
experimental_setup.tex
introduction.tex
main.tex
prompt_appendix.tex
related_work.tex
results.tex
sdgd_negative.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "a7f8ef05-6af4-406e-86c4-fb033e8001b1",
  "tool_use_result": {
    "stdout": "abstract.tex\nchecklist.tex\nconclusion.tex\ndiscussion.tex\nexperimental_setup.tex\nintroduction.tex\nmain.tex\nprompt_appendix.tex\nrelated_work.tex\nresults.tex\nsdgd_negative.tex",
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

_source line 81_

<details><summary>Logged reasoning block</summary>

```text
All files have null bytes! This is a serious issue. Let me check if this is some file system issue. Let me check the specific files I edited.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "c34ede70-3c05-48da-8cc6-710fac62a1fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01146hEd5NZT6f2oy1PQ13sP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 53524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 259
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

_source line 82_

All tex files have null bytes — likely a filesystem issue from concurrent edits. Let me check the files I'm responsible for.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "739913dd-d58e-4982-a957-d9dc49c00de1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01146hEd5NZT6f2oy1PQ13sP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 53524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 259
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

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wx7Ap1ShDbXaNhLEHvqnRs`</summary>

```json
{
  "command": "xxd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex | grep '0000 0000' | head -5",
  "description": "Check null byte locations in results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "227d0a2d-f9ca-4260-8cb6-e3d1819a03c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01146hEd5NZT6f2oy1PQ13sP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 53524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 259
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

_source line 84 · 2026-05-16T03:46:52.824Z_

<details><summary>↩ Tool result · `toolu_01Wx7Ap1ShDbXaNhLEHvqnRs`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "a59d2c0e-591c-43e3-9292-088957db2838",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Bash · `toolu_01HKd22dL1rbk7WfpEcqa8us`</summary>

```json
{
  "command": "xxd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | grep '0000 0000' | head -5",
  "description": "Check null byte locations in abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "ad4b8a95-78ee-4970-a78b-382733bbd777",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01146hEd5NZT6f2oy1PQ13sP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 53524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 259
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

_source line 86 · 2026-05-16T03:46:53.483Z_

<details><summary>↩ Tool result · `toolu_01HKd22dL1rbk7WfpEcqa8us`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "1733cf29-b91f-44a4-8c1d-44853bba29d0",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_01EaqV2GaTUQybTauMP6fo2f`</summary>

```json
{
  "command": "xxd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex | grep ' 00' | head -3; echo \"---\"; xxd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | grep ' 00' | head -3",
  "description": "Check for any null bytes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "66399000-bbde-4e5e-8b84-8e42439cbeab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0148ipxsMBYZpyjEH7wxubvU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 380,
      "cache_read_input_tokens": 53783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 380
      },
      "output_tokens": 64,
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

_source line 88 · 2026-05-16T03:46:57.151Z_

<details><summary>↩ Tool result · `toolu_01EaqV2GaTUQybTauMP6fo2f`</summary>

```text
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "706a5827-1c98-4aeb-9f47-c652b2e3c06a",
  "tool_use_result": {
    "stdout": "---",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_019cFuSEG337VaAX6Cz9HB7L`</summary>

```json
{
  "command": "file results.tex abstract.tex main.tex introduction.tex experimental_setup.tex",
  "description": "Check file types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "726734a8-fe75-4c3d-8fc0-4288d7ea8f22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQQeNWF1HWNHZkrgf4bifE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 54163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
      },
      "output_tokens": 63,
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

_source line 90 · 2026-05-16T03:47:00.196Z_

<details><summary>↩ Tool result · `toolu_019cFuSEG337VaAX6Cz9HB7L`</summary>

```text
results.tex:            LaTeX document, ASCII text, with very long lines (1192)
abstract.tex:           LaTeX document, ASCII text, with very long lines (1878)
main.tex:               LaTeX 2e document, ASCII text, with very long lines (781)
introduction.tex:       LaTeX document, ASCII text, with very long lines (1284)
experimental_setup.tex: LaTeX document, ASCII text, with very long lines (1071)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "d46bffc5-61d0-4590-8f8e-528fc3882ea3",
  "tool_use_result": {
    "stdout": "results.tex:            LaTeX document, ASCII text, with very long lines (1192)\nabstract.tex:           LaTeX document, ASCII text, with very long lines (1878)\nmain.tex:               LaTeX 2e document, ASCII text, with very long lines (781)\nintroduction.tex:       LaTeX document, ASCII text, with very long lines (1284)\nexperimental_setup.tex: LaTeX document, ASCII text, with very long lines (1071)",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Bash · `toolu_01HGik98QUjZ9ZSXJPwvLRBw`</summary>

```json
{
  "command": "for f in *.tex; do if file \"$f\" | grep -q -v ASCII; then echo \"BAD: $f\"; file \"$f\"; fi; done",
  "description": "Find non-ASCII tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "66701920-7ada-4871-892c-3e869c497ccc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPyqUfm4gpg94kuCcxFFoo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 206,
      "cache_read_input_tokens": 54450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 206
      },
      "output_tokens": 47,
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

_source line 92 · 2026-05-16T03:47:03.835Z_

<details><summary>↩ Tool result · `toolu_01HGik98QUjZ9ZSXJPwvLRBw`</summary>

```text
BAD: conclusion.tex
conclusion.tex: TeX document, Unicode text, UTF-8 text
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "7a62a613-b888-4249-8b11-485139df022f",
  "tool_use_result": {
    "stdout": "BAD: conclusion.tex\nconclusion.tex: TeX document, Unicode text, UTF-8 text",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01GZ15UcCyNazqT3RgoKaWbf`</summary>

```json
{
  "command": "for f in *.tex; do if LC_ALL=C grep -P '\\x00' \"$f\" > /dev/null 2>&1; then echo \"NULL: $f\"; fi; done",
  "description": "Find files with actual null bytes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "a439fc6e-c110-4b5f-ae34-86097a21f0e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1odQEnsy6rRNa1oGDFgvm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 54656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
      },
      "output_tokens": 62,
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

_source line 94 · 2026-05-16T03:47:07.615Z_

<details><summary>↩ Tool result · `toolu_01GZ15UcCyNazqT3RgoKaWbf`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "85768939-b929-466b-a1fd-5bbffa4a370d",
  "tool_use_result": {
    "stdout": "",
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

_source line 95_

<details><summary>Logged reasoning block</summary>

```text
No actual null bytes. Let me try compiling again — maybe the error was from a previous corrupt state that's been fixed now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "a1555a66-55ab-4a08-adc3-6327f8567f2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMobcRjuJLZmqT9ih246sc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 136,
      "cache_read_input_tokens": 54801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 136
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

_source line 96_

No null bytes found. Let me retry the compilation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "7af8eb8e-b3ca-49db-aac7-6f8957580074",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMobcRjuJLZmqT9ih246sc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 136,
      "cache_read_input_tokens": 54801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 136
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

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gq8XkLifRgn7SBDbkcvtKH`</summary>

```json
{
  "command": "rm -f main.aux main.bbl main.blg main.log main.out main.pdf && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "Clean build first pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "585e462d-48df-4256-87d6-33789412ac27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMobcRjuJLZmqT9ih246sc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 136,
      "cache_read_input_tokens": 54801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 136
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

_source line 98 · 2026-05-16T03:47:14.860Z_

<details><summary>↩ Tool result · `toolu_01Gq8XkLifRgn7SBDbkcvtKH`</summary>

```text
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `main.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/u
crr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (13 pages, 352807 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "92bddb62-f435-4cea-9be8-8f80a6d795cb",
  "tool_use_result": {
    "stdout": "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `main.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/u\ncrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (13 pages, 352807 bytes).\nTranscript written on main.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 99_

<details open><summary>🔧 Tool call — Bash · `toolu_01275KVNhKSwR5oBUY9NFcDW`</summary>

```json
{
  "command": "bibtex main 2>&1 | tail -10 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"(Error|Warning|Output written)\" && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"(Error|Warning|Output written)\"",
  "description": "bibtex + two more pdflatex passes",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "79a8fa1a-1b9b-4986-b7ac-02e82cc1692c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KnofuJU6HoCtoR1HaarKh6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 54937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1074
      },
      "output_tokens": 59,
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

### System

_source line 100_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bs48pvxmn",
  "tool_use_id": "toolu_01275KVNhKSwR5oBUY9NFcDW",
  "description": "bibtex + two more pdflatex passes",
  "task_type": "local_bash",
  "uuid": "fc64a753-281f-4684-8c23-ec04f57671dc",
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848"
}
```

---

### System

_source line 101_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bs48pvxmn",
  "tool_use_id": "toolu_01275KVNhKSwR5oBUY9NFcDW",
  "status": "completed",
  "output_file": "",
  "summary": "bibtex + two more pdflatex passes",
  "uuid": "1e985f19-02bd-478c-9089-335e8d63328c",
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848"
}
```

---

### Tool result

_source line 102 · 2026-05-16T03:47:25.243Z_

<details><summary>↩ Tool result · `toolu_01275KVNhKSwR5oBUY9NFcDW`</summary>

```text
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
Warning--I didn't find a database entry for "ding-fewnerd-2021"
Warning--I didn't find a database entry for "wang-maven-2020"
Warning--I didn't find a database entry for "han-fewrel-2018"
(There were 3 warnings)
Package natbib Warning: Citation `llm4ie-survey-2024' on page 1 undefined on in
Package natbib Warning: Citation `uniner-2024' on page 1 undefined on input lin
Package natbib Warning: Citation `llm-pee-2025' on page 1 undefined on input li
Package natbib Warning: Citation `parse-2025' on page 1 undefined on input line
Package natbib Warning: Citation `llm-pee-2025' on page 1 undefined on input li
Package natbib Warning: Citation `fewnerd-2021' on page 2 undefined on input li
Package natbib Warning: Citation `fewrel-2018' on page 2 undefined on input lin
Package natbib Warning: Citation `maven-2020' on page 2 undefined on input line
Package natbib Warning: Citation `instructuie-2023' on page 2 undefined on inpu
Package natbib Warning: Citation `knowcoder-2024' on page 2 undefined on input 
Package natbib Warning: Citation `codeie-2023' on page 2 undefined on input lin
Package natbib Warning: Citation `gollie-2024' on page 2 undefined on input lin
Package natbib Warning: Citation `adelie-2024' on page 2 undefined on input lin
Package natbib Warning: Citation `slot-2025' on page 2 undefined on input line 
Package natbib Warning: Citation `oneke-2025' on page 2 undefined on input line
Package natbib Warning: Citation `json-schema-bench-2025' on page 2 undefined o
Package natbib Warning: Citation `chatgpt-ie-eval-2023' on page 2 undefined on 
Package natbib Warning: Citation `wadhwa-re-llm-2023' on page 2 undefined on in
Package natbib Warning: Citation `xie-zeroshot-ner-2023' on page 2 undefined on
Package natbib Warning: Citation `promptner-2023' on page 2 undefined on input 
Package natbib Warning: Citation `uniner-2024' on page 2 undefined on input lin
Package natbib Warning: Citation `gliner-2024' on page 2 undefined on input lin
Package natbib Warning: Citation `gliner2-2025' on page 2 undefined on input li
Package natbib Warning: Citation `guidex-2025' on page 2 undefined on input lin
Package natbib Warning: Citation `nuner-2024' on page 2 undefined on input line
Package natbib Warning: Citation `familiarity-2025' on page 2 undefined on inpu
Package natbib Warning: Citation `llm-pee-2025' on page 2 undefined on input li
Package natbib Warning: Citation `iepile-2024' on page 3 undefined on input lin
Package natbib Warning: Citation `parse-2025' on page 3 undefined on input line
Package natbib Warning: Citation `dee-2024' on page 3 undefined on input line 1
Package natbib Warning: Citation `crossagentie-2025' on page 3 undefined on inp
Package natbib Warning: Citation `cmas-ner-2025' on page 3 undefined on input l
Package natbib Warning: Citation `spt-2025' on page 3 undefined on input line 1
Package natbib Warning: Citation `dlisc-2025' on page 3 undefined on input line
Package natbib Warning: Citation `kggen-2025' on page 3 undefined on input line
Package natbib Warning: Citation `reflect-learn-2026' on page 3 undefined on in
Package natbib Warning: Citation `gao-repr-degen-2019' on page 3 undefined on i
Package natbib Warning: Citation `ethayarajh-contextual-2019' on page 3 undefin
Package natbib Warning: Citation `cai-isotropy-clusters-2021' on page 3 undefin
Package natbib Warning: Citation `godey-anisotropy-inherent-2024' on page 3 und
Package natbib Warning: Citation `fewnerd-2021' on page 3 undefined on input li
Package natbib Warning: Citation `fewrel-2018' on page 3 undefined on input lin
Package natbib Warning: Citation `maven-2020' on page 3 undefined on input line
Package natbib Warning: Citation `qwen3-2025' on page 4 undefined on input line
Package natbib Warning: Citation `minilm-2020' on page 4 undefined on input lin
Package natbib Warning: Citation `sentence-bert-2019' on page 4 undefined on in
Package natbib Warning: Citation `qwen3-2025' on page 4 undefined on input line
Package natbib Warning: Citation `vllm-2023' on page 4 undefined on input line 
Package natbib Warning: Citation `sclar-sensitivity-2024' on page 4 undefined o
Package natbib Warning: Citation `lost-in-middle-2024' on page 6 undefined on i
Package natbib Warning: Citation `cai-isotropy-clusters-2021' on page 7 undefin
Package natbib Warning: Citation `llm-calibration-survey-2024' on page 7 undefi
Package natbib Warning: Citation `llm-pee-2025' on page 7 undefined on input li
Package natbib Warning: Citation `fewnerd-2021' on page 9 undefined on input li
Package natbib Warning: Citation `fewrel-2018' on page 9 undefined on input lin
Package natbib Warning: Citation `maven-2020' on page 9 undefined on input line
Package natbib Warning: Citation `qwen3-2025' on page 9 undefined on input line
Package natbib Warning: Citation `vllm-2023' on page 9 undefined on input line 
Package natbib Warning: Citation `minilm-2020' on page 9 undefined on input lin
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
Package lineno Warning: Line number reference failed, re-run to get it right.
Package natbib Warning: Citation `ding-fewnerd-2021' on page 15 undefined on in
Package natbib Warning: Citation `wang-maven-2020' on page 15 undefined on inpu
Package natbib Warning: Citation `han-fewrel-2018' on page 15 undefined on inpu
Package natbib Warning: There were undefined citations.
Package natbib Warning: Citation(s) may have changed.
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
Output written on main.pdf (16 pages, 383584 bytes).
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
Package lineno Warning: Line number reference failed, re-run to get it right.
Package natbib Warning: Citation `ding-fewnerd-2021' on page 16 undefined on in
Package natbib Warning: Citation `wang-maven-2020' on page 16 undefined on inpu
Package natbib Warning: Citation `han-fewrel-2018' on page 16 undefined on inpu
Package natbib Warning: There were undefined citations.
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
Output written on main.pdf (16 pages, 389496 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "5bddd2bb-8eaf-4ca0-99ff-9deb0f53ca1a",
  "tool_use_result": {
    "stdout": "This is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nDatabase file #1: references.bib\nWarning--I didn't find a database entry for \"ding-fewnerd-2021\"\nWarning--I didn't find a database entry for \"wang-maven-2020\"\nWarning--I didn't find a database entry for \"han-fewrel-2018\"\n(There were 3 warnings)\nPackage natbib Warning: Citation `llm4ie-survey-2024' on page 1 undefined on in\nPackage natbib Warning: Citation `uniner-2024' on page 1 undefined on input lin\nPackage natbib Warning: Citation `llm-pee-2025' on page 1 undefined on input li\nPackage natbib Warning: Citation `parse-2025' on page 1 undefined on input line\nPackage natbib Warning: Citation `llm-pee-2025' on page 1 undefined on input li\nPackage natbib Warning: Citation `fewnerd-2021' on page 2 undefined on input li\nPackage natbib Warning: Citation `fewrel-2018' on page 2 undefined on input lin\nPackage natbib Warning: Citation `maven-2020' on page 2 undefined on input line\nPackage natbib Warning: Citation `instructuie-2023' on page 2 undefined on inpu\nPackage natbib Warning: Citation `knowcoder-2024' on page 2 undefined on input \nPackage natbib Warning: Citation `codeie-2023' on page 2 undefined on input lin\nPackage natbib Warning: Citation `gollie-2024' on page 2 undefined on input lin\nPackage natbib Warning: Citation `adelie-2024' on page 2 undefined on input lin\nPackage natbib Warning: Citation `slot-2025' on page 2 undefined on input line \nPackage natbib Warning: Citation `oneke-2025' on page 2 undefined on input line\nPackage natbib Warning: Citation `json-schema-bench-2025' on page 2 undefined o\nPackage natbib Warning: Citation `chatgpt-ie-eval-2023' on page 2 undefined on \nPackage natbib Warning: Citation `wadhwa-re-llm-2023' on page 2 undefined on in\nPackage natbib Warning: Citation `xie-zeroshot-ner-2023' on page 2 undefined on\nPackage natbib Warning: Citation `promptner-2023' on page 2 undefined on input \nPackage natbib Warning: Citation `uniner-2024' on page 2 undefined on input lin\nPackage natbib Warning: Citation `gliner-2024' on page 2 undefined on input lin\nPackage natbib Warning: Citation `gliner2-2025' on page 2 undefined on input li\nPackage natbib Warning: Citation `guidex-2025' on page 2 undefined on input lin\nPackage natbib Warning: Citation `nuner-2024' on page 2 undefined on input line\nPackage natbib Warning: Citation `familiarity-2025' on page 2 undefined on inpu\nPackage natbib Warning: Citation `llm-pee-2025' on page 2 undefined on input li\nPackage natbib Warning: Citation `iepile-2024' on page 3 undefined on input lin\nPackage natbib Warning: Citation `parse-2025' on page 3 undefined on input line\nPackage natbib Warning: Citation `dee-2024' on page 3 undefined on input line 1\nPackage natbib Warning: Citation `crossagentie-2025' on page 3 undefined on inp\nPackage natbib Warning: Citation `cmas-ner-2025' on page 3 undefined on input l\nPackage natbib Warning: Citation `spt-2025' on page 3 undefined on input line 1\nPackage natbib Warning: Citation `dlisc-2025' on page 3 undefined on input line\nPackage natbib Warning: Citation `kggen-2025' on page 3 undefined on input line\nPackage natbib Warning: Citation `reflect-learn-2026' on page 3 undefined on in\nPackage natbib Warning: Citation `gao-repr-degen-2019' on page 3 undefined on i\nPackage natbib Warning: Citation `ethayarajh-contextual-2019' on page 3 undefin\nPackage natbib Warning: Citation `cai-isotropy-clusters-2021' on page 3 undefin\nPackage natbib Warning: Citation `godey-anisotropy-inherent-2024' on page 3 und\nPackage natbib Warning: Citation `fewnerd-2021' on page 3 undefined on input li\nPackage natbib Warning: Citation `fewrel-2018' on page 3 undefined on input lin\nPackage natbib Warning: Citation `maven-2020' on page 3 undefined on input line\nPackage natbib Warning: Citation `qwen3-2025' on page 4 undefined on input line\nPackage natbib Warning: Citation `minilm-2020' on page 4 undefined on input lin\nPackage natbib Warning: Citation `sentence-bert-2019' on page 4 undefined on in\nPackage natbib Warning: Citation `qwen3-2025' on page 4 undefined on input line\nPackage natbib Warning: Citation `vllm-2023' on page 4 undefined on input line \nPackage natbib Warning: Citation `sclar-sensitivity-2024' on page 4 undefined o\nPackage natbib Warning: Citation `lost-in-middle-2024' on page 6 undefined on i\nPackage natbib Warning: Citation `cai-isotropy-clusters-2021' on page 7 undefin\nPackage natbib Warning: Citation `llm-calibration-survey-2024' on page 7 undefi\nPackage natbib Warning: Citation `llm-pee-2025' on page 7 undefined on input li\nPackage natbib Warning: Citation `fewnerd-2021' on page 9 undefined on input li\nPackage natbib Warning: Citation `fewrel-2018' on page 9 undefined on input lin\nPackage natbib Warning: Citation `maven-2020' on page 9 undefined on input line\nPackage natbib Warning: Citation `qwen3-2025' on page 9 undefined on input line\nPackage natbib Warning: Citation `vllm-2023' on page 9 undefined on input line \nPackage natbib Warning: Citation `minilm-2020' on page 9 undefined on input lin\nLaTeX Warning: `h' float specifier changed to `ht'.\nLaTeX Warning: `h' float specifier changed to `ht'.\nLaTeX Warning: `h' float specifier changed to `ht'.\nPackage lineno Warning: Line number reference failed, re-run to get it right.\nPackage natbib Warning: Citation `ding-fewnerd-2021' on page 15 undefined on in\nPackage natbib Warning: Citation `wang-maven-2020' on page 15 undefined on inpu\nPackage natbib Warning: Citation `han-fewrel-2018' on page 15 undefined on inpu\nPackage natbib Warning: There were undefined citations.\nPackage natbib Warning: Citation(s) may have changed.\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\nOutput written on main.pdf (16 pages, 383584 bytes).\nLaTeX Warning: `h' float specifier changed to `ht'.\nLaTeX Warning: `h' float specifier changed to `ht'.\nLaTeX Warning: `h' float specifier changed to `ht'.\nLaTeX Warning: `h' float specifier changed to `ht'.\nLaTeX Warning: `h' float specifier changed to `ht'.\nPackage lineno Warning: Line number reference failed, re-run to get it right.\nPackage natbib Warning: Citation `ding-fewnerd-2021' on page 16 undefined on in\nPackage natbib Warning: Citation `wang-maven-2020' on page 16 undefined on inpu\nPackage natbib Warning: Citation `han-fewrel-2018' on page 16 undefined on inpu\nPackage natbib Warning: There were undefined citations.\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\nOutput written on main.pdf (16 pages, 389496 bytes).",
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

_source line 103_

<details><summary>Logged reasoning block</summary>

```text
Compilation succeeded — no errors, only warnings (undefined citations for 3 missing bib entries and some float/label warnings, all pre-existing). Output: 16 pages.

Let me do one more pass to resolve the remaining cross-reference warning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "6348e499-c7bd-4372-875c-4b5233f5a58c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012J9zDPvRDG6Hi2cLMHyikQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2267,
      "cache_read_input_tokens": 56011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2267
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

_source line 104_

<details open><summary>🔧 Tool call — Bash · `toolu_011m8f7LCJJATWfEhavkaviQ`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"(Error|Output written)\"",
  "description": "Final pdflatex pass to resolve cross-refs",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "f99ebb9c-9fd1-4929-b8d9-b21520d3eba7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012J9zDPvRDG6Hi2cLMHyikQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2267,
      "cache_read_input_tokens": 56011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2267
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

_source line 105 · 2026-05-16T03:47:33.273Z_

<details><summary>↩ Tool result · `toolu_011m8f7LCJJATWfEhavkaviQ`</summary>

```text
Output written on main.pdf (16 pages, 389316 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "c0c08cf7-af96-475b-8e6d-0659ce1cbacb",
  "tool_use_result": {
    "stdout": "Output written on main.pdf (16 pages, 389316 bytes).",
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

_source line 106_

Compilation successful, no errors. 16 pages.

**Summary of edits made:**

**results.tex:**
- **2A**: NER paragraph — 0.52→0.522, 0.55→0.549, added "bootstrap" before CIs, reformatted as "overlap: ... vs.\ ..."
- **C2 (9.1pp)**: Table caption reframed from "widens from 9.1 to 31.2" to slope-consistency narrative; line 90 now shows 9.1pp as extreme-batch with quartile gap $-$7.42pp alongside; line 119 replaced "31.2 vs.\ 9.1" with quartile gaps from Table 4
- **C3 (31.2pp)**: Added "extreme-batch" caveat to all remaining 31.2pp mentions (line 90 count=16 reference)
- **W12**: "model-invariant" → "consistent across tested models (Qwen3-32B and Llama-3.1-8B)" (2 occurrences)

**abstract.tex:**
- Removed `\S\ref{sec:centrality_confound}` cross-reference (abstracts should be self-contained)
- C2, W7, W12 were already applied by the other worker

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "uuid": "6f27e663-ebf8-4cdf-abe5-3aed490451d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkwKpJBxRF3nzqW7GDfH7B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 224,
      "cache_read_input_tokens": 58278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 224
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

_source line 107_

Compilation successful, no errors. 16 pages.

**Summary of edits made:**

**results.tex:**
- **2A**: NER paragraph — 0.52→0.522, 0.55→0.549, added "bootstrap" before CIs, reformatted as "overlap: ... vs.\ ..."
- **C2 (9.1pp)**: Table caption reframed from "widens from 9.1 to 31.2" to slope-consistency narrative; line 90 now shows 9.1pp as extreme-batch with quartile gap $-$7.42pp alongside; line 119 replaced "31.2 vs.\ 9.1" with quartile gaps from Table 4
- **C3 (31.2pp)**: Added "extreme-batch" caveat to all remaining 31.2pp mentions (line 90 count=16 reference)
- **W12**: "model-invariant" → "consistent across tested models (Qwen3-32B and Llama-3.1-8B)" (2 occurrences)

**abstract.tex:**
- Removed `\S\ref{sec:centrality_confound}` cross-reference (abstracts should be self-contained)
- C2, W7, W12 were already applied by the other worker

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 273495,
  "duration_api_ms": 255794,
  "num_turns": 39,
  "stop_reason": "end_turn",
  "session_id": "5b227fbe-375a-4d23-82d2-1d78d3cd0848",
  "total_cost_usd": 1.13971925,
  "usage": {
    "input_tokens": 81,
    "cache_creation_input_tokens": 46661,
    "cache_read_input_tokens": 946600,
    "output_tokens": 14865,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 46661,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 313,
        "cache_read_input_tokens": 58278,
        "cache_creation_input_tokens": 224,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 224
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2668,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0027579999999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 81,
      "outputTokens": 14865,
      "cacheReadInputTokens": 946600,
      "cacheCreationInputTokens": 46661,
      "webSearchRequests": 0,
      "costUSD": 1.13696125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "aa4d59e4-0816-47c5-8e26-86612f8d51e2"
}
```

</details>

---
