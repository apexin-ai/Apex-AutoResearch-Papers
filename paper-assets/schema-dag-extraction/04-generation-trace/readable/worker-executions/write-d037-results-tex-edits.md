# write d037 results tex edits

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 99
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/workers/worker_write_d037_results_tex_edits_20260516T034134.log`
- **Structured JSON:** [`03b1d52257b4e94c1b5a.json`](../../sessions/03/03b1d52257b4e94c1b5a.json)

## Before a recorded user message

99 recorded events

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
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
  "uuid": "b4a3cc91-e22c-484c-9b78-d23b11e4886d",
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
  "uuid": "2bb248f4-d7fc-4da4-994f-7b273293fa19",
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5"
}
```

---

### Assistant

_source line 4_

Let me start by reading the current results.tex file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "86eb93d3-019a-4ebd-929e-98171ba5e55b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdCn5EZut2LugatAsvHwn5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12813,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12813
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

<details open><summary>🔧 Tool call — Read · `toolu_0155iayhyAsCNukSuzjFa2zJ`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "b51b1db3-266c-4fd3-9c90-346393cf51b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdCn5EZut2LugatAsvHwn5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12813,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12813
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

_source line 6 · 2026-05-16T03:41:54.398Z_

<details><summary>↩ Tool result · `toolu_0155iayhyAsCNukSuzjFa2zJ`</summary>

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
25	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\,=\,22$ to 0.551 at count${}\,=\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
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
60	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$, meaning pairwise confusability explains roughly 1.5\% of the variance in type confusion. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\S\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.
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
119	\paragraph{Cross-model validation.}
120	The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\,pp at count${}\,=\,8$ (low-BCS 78.1\% vs.\ high-BCS 51.0\%) and $-$23.9\,pp at count${}\,=\,16$ (75.5\% vs.\ 51.6\%), reaching 77--87\% of Qwen3-32B's $-$31.2\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\approx$51\% under high confusability (count${}\,=\,8$: 51.0\% vs.\ 51.0\%; count${}\,=\,16$: 51.6\% vs.\ 51.6\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.
121	
122	\subsection{Multi-Channel Degradation}
123	\label{sec:multi_channel}
124	
125	We decompose extraction errors into an error taxonomy (full data in Table~\ref{tab:error_taxonomy}, Appendix~\ref{sec:appendix_figures}; see also Figure~\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\%), but NER rates are substantially higher (43--65\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.
126	
127	These results establish two degradation channels: \textbf{Channel~1} (count $\to$ recall decline, \S\ref{sec:count_curves}) and \textbf{Channel~2} (confusability $\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.
128	
129	\subsection{Centrality Confound on Homogeneous Schemas}
130	\label{sec:centrality_confound}
131	
132	Per-type analysis on MAVEN reveals an anomalous \emph{positive} BCS--error correlation (Qwen3 $\rho = +0.184$, $p = 0.025$; MiniLM $\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "b42a71b8-b535-486a-b334-2a617c4219df",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\\,=\\,22$ to 0.551 at count${}\\,=\\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
      "numLines": 132,
      "startLine": 1,
      "totalLines": 132
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
Let me now examine the full file to understand all the content, and search for specific patterns I need to modify.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "5aab5606-40f8-4f7a-a012-35cc896f8385",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLcid1MKuZsHUBJDbC9QYP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5351,
      "cache_read_input_tokens": 24654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5351
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

_source line 8_

Now let me search for all occurrences of "31.2" and "framework" in this file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "733ec15f-63e1-4488-bb43-074d4c8cf935",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLcid1MKuZsHUBJDbC9QYP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5351,
      "cache_read_input_tokens": 24654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5351
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

_source line 9_

<details open><summary>🔧 Tool call — Grep · `toolu_01Wxq4wFF6HZF7vVvXa7pv8b`</summary>

```json
{
  "pattern": "31\\.2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "6f2b5c8b-e7db-4157-abb0-addb42ebbeeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLcid1MKuZsHUBJDbC9QYP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5351,
      "cache_read_input_tokens": 24654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5351
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

_source line 10 · 2026-05-16T03:42:00.732Z_

<details><summary>↩ Tool result · `toolu_01Wxq4wFF6HZF7vVvXa7pv8b`</summary>

```text
64:[Omitted long matching line]
80:80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
81:80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
84:\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\,pp at 16 relations to 31.2\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
88:[Omitted long matching line]
117:[Omitted long matching line]
120:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "84ac113c-f7a4-4331-9649-15dfc0667b19",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "64:[Omitted long matching line]\n80:80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n81:80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n84:\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n88:[Omitted long matching line]\n117:[Omitted long matching line]\n120:[Omitted long matching line]",
    "numLines": 7
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Grep · `toolu_01VSqU8qT1Kaaojae6pYVvxB`</summary>

```json
{
  "pattern": "framework",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "1586a4af-901d-4492-8c06-6623b6444405",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLcid1MKuZsHUBJDbC9QYP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5351,
      "cache_read_input_tokens": 24654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5351
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

_source line 12 · 2026-05-16T03:42:01.708Z_

<details><summary>↩ Tool result · `toolu_01VSqU8qT1Kaaojae6pYVvxB`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "d5812051-0443-4093-aa4a-bd22045817f9",
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

_source line 13_

<details open><summary>🔧 Tool call — Grep · `toolu_014ttqdiANW5fNFyBqqjC6vS`</summary>

```json
{
  "pattern": "fig:error_taxonomy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "a270ccf8-b8ac-486b-b286-a390de608fa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLcid1MKuZsHUBJDbC9QYP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5351,
      "cache_read_input_tokens": 24654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5351
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

_source line 14 · 2026-05-16T03:42:02.221Z_

<details><summary>↩ Tool result · `toolu_014ttqdiANW5fNFyBqqjC6vS`</summary>

```text
125:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "6346f46f-3e75-4f12-af83-5d6e4e260142",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "125:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
No "framework" in results.tex. Let me check the exact lines for 31.2 mentions and the fig:error_taxonomy reference. Let me also check for any labels that might be relevant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "34872a63-c516-4458-891f-84f81aca7757",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gT8oF2ypCBLBjDBoKvFBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 30005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 786
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

_source line 16_

No "framework" found in results.tex — item 8 is already done. Let me check references and existing labels more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "a1e496da-552b-4b67-bb5d-a037f552fd67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gT8oF2ypCBLBjDBoKvFBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 30005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 786
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

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_012QGbDYAaov98J8hdK9Hshp`</summary>

```json
{
  "pattern": "sec:model|sec:appendix_prompts|sec:appendix_figures",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "9cec7ca4-c63f-4f93-ae8e-bbed1b0b6f95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gT8oF2ypCBLBjDBoKvFBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 30005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 786
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

_source line 18 · 2026-05-16T03:42:08.513Z_

<details><summary>↩ Tool result · `toolu_012QGbDYAaov98J8hdK9Hshp`</summary>

```text
125:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "e3953bd6-04ba-4038-ab01-5c4bc73421d3",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "125:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Grep · `toolu_01VyYf9TXRrrvryVeSSPrfzz`</summary>

```json
{
  "pattern": "sec:model|sec:appendix_prompts|sec:appendix_figures",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "2165a8dc-169e-4be9-9f49-80df98831e27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gT8oF2ypCBLBjDBoKvFBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 30005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 786
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

_source line 20 · 2026-05-16T03:42:09.522Z_

<details><summary>↩ Tool result · `toolu_01VyYf9TXRrrvryVeSSPrfzz`</summary>

```text
docs/paper/main.tex:59:\label{sec:appendix_figures}
docs/paper/main.tex:74:\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
docs/paper/checklist.tex:33:Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \cite{vllm-2023}, and all-MiniLM-L6-v2 \cite{minilm-2020} are cited in \S\ref{sec:datasets} and \S\ref{sec:model}.
docs/paper/checklist.tex:63:Yes. \S\ref{sec:model}: Qwen3-32B (32B parameters, FP8) and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on a single RTX PRO 6000 Blackwell GPU (96\,GB) served via vLLM. Total compute was approximately 48 GPU-hours of inference (no training).
docs/paper/checklist.tex:67:Yes. \S\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \S\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.
docs/paper/checklist.tex:71:Yes. All key metrics include 95\% bootstrap confidence intervals (1{,}000 resamples, percentile method) as stated in \S\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \S\ref{sec:count_curves}--\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.
docs/paper/checklist.tex:75:Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
docs/paper/prompt_appendix.tex:2:\label{sec:appendix_prompts}
docs/paper/prompt_appendix.tex:95:\item \textbf{Offset fields removed.} The \texttt{start}/\texttt{end} integer fields are dropped from both the natural-language instruction and the JSON schema. In v1, 96.5\% of predicted offsets were hallucinated (\S\ref{sec:model}).
docs/paper/experimental_setup.tex:81:\label{sec:model}
docs/paper/main.aux:431:\newlabel{sec:model}{{3.5}{4}{Model and Inference}{subsection.3.5}{}}
docs/paper/main.aux:1218:\newlabel{sec:appendix_figures}{{A}{12}{Additional Figures}{appendix.A}{}}
docs/paper/main.aux:1219:[Omitted long matching line]
docs/paper/main.aux:1220:\newlabel{tab:cross_model}{{5}{12}{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S \ref {sec:model}) for fair cross-model comparison; the count-curve results in \S \ref {sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1}{table.caption.33}{}}
docs/paper/main.aux:1375:\newlabel{sec:appendix_prompts}{{F}{14}{Prompt Templates}{appendix.F}{}}
docs/paper/results.tex:125:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "7ea1f563-e660-4b40-8284-286a867bdb23",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:59:\\label{sec:appendix_figures}\ndocs/paper/main.tex:74:\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\ndocs/paper/checklist.tex:33:Yes. Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, MAVEN \\cite{maven-2020}, Qwen3-32B \\cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \\cite{vllm-2023}, and all-MiniLM-L6-v2 \\cite{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.\ndocs/paper/checklist.tex:63:Yes. \\S\\ref{sec:model}: Qwen3-32B (32B parameters, FP8) and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on a single RTX PRO 6000 Blackwell GPU (96\\,GB) served via vLLM. Total compute was approximately 48 GPU-hours of inference (no training).\ndocs/paper/checklist.tex:67:Yes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\ndocs/paper/checklist.tex:71:Yes. All key metrics include 95\\% bootstrap confidence intervals (1{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.\ndocs/paper/checklist.tex:75:Yes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\ndocs/paper/prompt_appendix.tex:2:\\label{sec:appendix_prompts}\ndocs/paper/prompt_appendix.tex:95:\\item \\textbf{Offset fields removed.} The \\texttt{start}/\\texttt{end} integer fields are dropped from both the natural-language instruction and the JSON schema. In v1, 96.5\\% of predicted offsets were hallucinated (\\S\\ref{sec:model}).\ndocs/paper/experimental_setup.tex:81:\\label{sec:model}\ndocs/paper/main.aux:431:\\newlabel{sec:model}{{3.5}{4}{Model and Inference}{subsection.3.5}{}}\ndocs/paper/main.aux:1218:\\newlabel{sec:appendix_figures}{{A}{12}{Additional Figures}{appendix.A}{}}\ndocs/paper/main.aux:1219:[Omitted long matching line]\ndocs/paper/main.aux:1220:\\newlabel{tab:cross_model}{{5}{12}{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S \\ref {sec:model}) for fair cross-model comparison; the count-curve results in \\S \\ref {sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1}{table.caption.33}{}}\ndocs/paper/main.aux:1375:\\newlabel{sec:appendix_prompts}{{F}{14}{Prompt Templates}{appendix.F}{}}\ndocs/paper/results.tex:125:[Omitted long matching line]",
    "numLines": 16
  }
}
```

</details>

---

### Assistant

_source line 21_

Good. Now I have a complete picture. Let me also check the full line 125 and the Figure ref context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "245b51df-822a-49f8-b451-c510eea7880c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeJDMmhfSy91HmZzGfAw3N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1594,
      "cache_read_input_tokens": 30791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1594
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

<details open><summary>🔧 Tool call — Read · `toolu_01Pg8tJjaFJAaKTGRRv7Ztpr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": 122,
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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "49c391b8-0c3f-4b9e-934d-016e70dfc027",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeJDMmhfSy91HmZzGfAw3N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1594,
      "cache_read_input_tokens": 30791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1594
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

_source line 23 · 2026-05-16T03:42:13.123Z_

<details><summary>↩ Tool result · `toolu_01Pg8tJjaFJAaKTGRRv7Ztpr`</summary>

```text
122	\subsection{Multi-Channel Degradation}
123	\label{sec:multi_channel}
124	
125	We decompose extraction errors into an error taxonomy (full data in Table~\ref{tab:error_taxonomy}, Appendix~\ref{sec:appendix_figures}; see also Figure~\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\%), but NER rates are substantially higher (43--65\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.
126	
127	These results establish two degradation channels: \textbf{Channel~1} (count $\to$ recall decline, \S\ref{sec:count_curves}) and \textbf{Channel~2} (confusability $\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.
128	
129	\subsection{Centrality Confound on Homogeneous Schemas}
130	\label{sec:centrality_confound}
131	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "3f1b5121-ef72-4253-9ded-b8902b99c21e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n",
      "numLines": 10,
      "startLine": 122,
      "totalLines": 132
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

Now I have all the information needed. Let me apply all the edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "9891727b-695b-4037-bfa1-f199a923b55b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUr1yYmTixAvdZtwBSNWC3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 32385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 731
      },
      "output_tokens": 3,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011E78TueeahT3LtSLQS53sg`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "e13944ef-7c4b-42c5-989f-aca1cc9a8fa0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUr1yYmTixAvdZtwBSNWC3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 32385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 731
      },
      "output_tokens": 3,
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

_source line 26 · 2026-05-16T03:42:16.814Z_

<details><summary>↩ Tool result · `toolu_011E78TueeahT3LtSLQS53sg`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "92a9555d-4ab4-422c-81f6-a1cbd92ab585",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Let me track progress with todos and then start making all the edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "5c19b833-5ed3-45e4-a046-4f96a6631c8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9MwriHbeFfEJe5P8K3U43",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2483,
      "cache_read_input_tokens": 33116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2483
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01TwJHEMjJVwfvQKGJgw2zbd`</summary>

```json
{
  "todos": [
    {
      "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
      "status": "in_progress",
      "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
    },
    {
      "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
      "status": "pending",
      "activeForm": "Adding cluster-robust CI to §4.2"
    },
    {
      "content": "Edit 3: W2 practical effect paragraph in §4.3",
      "status": "pending",
      "activeForm": "Adding practical magnitude paragraph to §4.3"
    },
    {
      "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
      "status": "pending",
      "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
    },
    {
      "content": "Edit 5: C1 prompt version annotation",
      "status": "pending",
      "activeForm": "Adding v1 prompt annotation to §4"
    },
    {
      "content": "Edit 6: MW4 Figure 2 appendix ref",
      "status": "pending",
      "activeForm": "Fixing Figure ref to include Appendix"
    },
    {
      "content": "Edit 7: framework → pattern (verify no occurrences)",
      "status": "pending",
      "activeForm": "Checking framework→pattern replacement"
    },
    {
      "content": "Compile and verify",
      "status": "pending",
      "activeForm": "Compiling LaTeX and verifying"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "1323beb2-d935-4e48-8347-c317e201edbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9MwriHbeFfEJe5P8K3U43",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2483,
      "cache_read_input_tokens": 33116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2483
      },
      "output_tokens": 23,
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

_source line 29 · 2026-05-16T03:42:26.618Z_

<details><summary>↩ Tool result · `toolu_01TwJHEMjJVwfvQKGJgw2zbd`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "7ea7699c-01f5-45ce-9d2a-cad19c419457",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "in_progress",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "pending",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "pending",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "pending",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "pending",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "pending",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "pending",
        "activeForm": "Checking framework→pattern replacement"
      },
      {
        "content": "Compile and verify",
        "status": "pending",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 30_

Starting edits. Edit 1: §4.1 count curve recall numbers → macro-avg with CI.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "2d706873-15d1-4e19-b951-1219b8c3e850",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCJAjVoXk3YMRZkdHQabHe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 499,
      "cache_read_input_tokens": 35599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 499
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

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_01D2kmUnnnNu6h1JkGEZ3YDm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\\,=\\,22$ to 0.551 at count${}\\,=\\,44$)",
  "new_string": "with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "b780cd59-fc02-4ee1-b67a-8afc1c28129a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCJAjVoXk3YMRZkdHQabHe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 499,
      "cache_read_input_tokens": 35599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 499
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

_source line 32 · 2026-05-16T03:42:33.136Z_

<details><summary>↩ Tool result · `toolu_01D2kmUnnnNu6h1JkGEZ3YDm`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "e374a783-4349-4f26-b422-6a15241d271b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\\,=\\,22$ to 0.551 at count${}\\,=\\,44$)",
    "newString": "with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability)",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\\,=\\,22$ to 0.551 at count${}\\,=\\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 22,
        "oldLines": 7,
        "newStart": 22,
        "newLines": 7,
        "lines": [
          " We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).",
          " ",
          " \\paragraph{NER (Few-NERD).}",
          "-Recall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\\,=\\,22$ to 0.551 at count${}\\,=\\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.",
          "+Recall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.",
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

_source line 33_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_013ixphnj7xAfns2xRFec5ER`</summary>

```json
{
  "todos": [
    {
      "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
      "status": "completed",
      "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
    },
    {
      "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
      "status": "in_progress",
      "activeForm": "Adding cluster-robust CI to §4.2"
    },
    {
      "content": "Edit 3: W2 practical effect paragraph in §4.3",
      "status": "pending",
      "activeForm": "Adding practical magnitude paragraph to §4.3"
    },
    {
      "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
      "status": "pending",
      "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
    },
    {
      "content": "Edit 5: C1 prompt version annotation",
      "status": "pending",
      "activeForm": "Adding v1 prompt annotation to §4"
    },
    {
      "content": "Edit 6: MW4 Figure 2 appendix ref",
      "status": "pending",
      "activeForm": "Fixing Figure ref to include Appendix"
    },
    {
      "content": "Edit 7: framework → pattern (verify no occurrences)",
      "status": "pending",
      "activeForm": "Checking framework→pattern replacement"
    },
    {
      "content": "Compile and verify",
      "status": "pending",
      "activeForm": "Compiling LaTeX and verifying"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "018e7cd7-e72e-4e8f-a5c9-1d75af02aea7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvZfHbpyJibsX9yJmd3Bcs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 36098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
      },
      "output_tokens": 65,
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

_source line 34 · 2026-05-16T03:42:38.759Z_

<details><summary>↩ Tool result · `toolu_013ixphnj7xAfns2xRFec5ER`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "9c55441f-2ed8-4469-918a-16b70de85663",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "in_progress",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "pending",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "pending",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "pending",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "pending",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "pending",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "pending",
        "activeForm": "Checking framework→pattern replacement"
      },
      {
        "content": "Compile and verify",
        "status": "pending",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "newTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "completed",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "in_progress",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "pending",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "pending",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "pending",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "pending",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "pending",
        "activeForm": "Checking framework→pattern replacement"
      },
      {
        "content": "Compile and verify",
        "status": "pending",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 35_

Edit 2: Add cluster-robust CI to §4.2 after the pairwise discussion paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "a22bab68-315e-496c-a714-da1c5d7cdc73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJoieqC6cHTPCGkREDAGvs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 36460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
      },
      "output_tokens": 5,
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

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_018ssqNzA6MdzJJtJTVAhLdB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "The correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.",
  "new_string": "The correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "3137268e-2035-48ad-adef-07caf8193647",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJoieqC6cHTPCGkREDAGvs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 36460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
      },
      "output_tokens": 5,
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

_source line 37 · 2026-05-16T03:42:50.463Z_

<details><summary>↩ Tool result · `toolu_018ssqNzA6MdzJJtJTVAhLdB`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "b9566f48-06f4-4c3a-a604-727257cc2654",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "The correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.",
    "newString": "The correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 57,
        "oldLines": 7,
        "newStart": 57,
        "newLines": 7,
        "lines": [
          " \\label{tab:pairwise}",
          " \\end{table}",
          " ",
          "-The correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.",
          "+The correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.",
          " ",
          " Spearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.",
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

<details open><summary>🔧 Tool call — TodoWrite · `toolu_019EdB7pPXB4bPTHboSeaNPz`</summary>

```json
{
  "todos": [
    {
      "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
      "status": "completed",
      "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
    },
    {
      "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
      "status": "completed",
      "activeForm": "Adding cluster-robust CI to §4.2"
    },
    {
      "content": "Edit 3: W2 practical effect paragraph in §4.3",
      "status": "in_progress",
      "activeForm": "Adding practical magnitude paragraph to §4.3"
    },
    {
      "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
      "status": "pending",
      "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
    },
    {
      "content": "Edit 5: C1 prompt version annotation",
      "status": "pending",
      "activeForm": "Adding v1 prompt annotation to §4"
    },
    {
      "content": "Edit 6: MW4 Figure 2 appendix ref",
      "status": "pending",
      "activeForm": "Fixing Figure ref to include Appendix"
    },
    {
      "content": "Edit 7: framework → pattern (verify no occurrences)",
      "status": "pending",
      "activeForm": "Checking framework→pattern replacement"
    },
    {
      "content": "Compile and verify",
      "status": "pending",
      "activeForm": "Compiling LaTeX and verifying"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "3171f7a1-4a16-4803-b021-34c3c91564e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014QAqXXCmrkm6k1VZMnkVNi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 36927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
      },
      "output_tokens": 72,
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

_source line 39 · 2026-05-16T03:42:55.692Z_

<details><summary>↩ Tool result · `toolu_019EdB7pPXB4bPTHboSeaNPz`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "5b38a990-a4b3-4231-8c59-fb3766ac17e0",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "completed",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "in_progress",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "pending",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "pending",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "pending",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "pending",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "pending",
        "activeForm": "Checking framework→pattern replacement"
      },
      {
        "content": "Compile and verify",
        "status": "pending",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "newTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "completed",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "completed",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "in_progress",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "pending",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "pending",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "pending",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "pending",
        "activeForm": "Checking framework→pattern replacement"
      },
      {
        "content": "Compile and verify",
        "status": "pending",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 40_

Edit 3: Add practical magnitude paragraph in §4.3, after the within-pool discussion and before cross-model validation. I need to insert it between the within-pool paragraph and the cross-model paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "9174596b-d3c5-4d64-bc38-349647e1c2c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5pCvPKX6Qw7i2YDx4SiBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 37529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
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

_source line 41_

<details open><summary>🔧 Tool call — Edit · `toolu_01V5f7DzKo5TuFe6guTkrfwM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct",
  "new_string": "\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "d0a371fe-b52e-47b3-8f5f-cdeb18cb90d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5pCvPKX6Qw7i2YDx4SiBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 37529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
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

_source line 42 · 2026-05-16T03:43:07.207Z_

<details><summary>↩ Tool result · `toolu_01V5f7DzKo5TuFe6guTkrfwM`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "5e8ab3b0-4950-4f33-8645-deb17cfc866e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct",
    "newString": "\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 116,
        "oldLines": 6,
        "newStart": 116,
        "newLines": 10,
        "lines": [
          " ",
          " The within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.",
          " ",
          "+\\paragraph{Practical magnitude.}",
          "+\\label{sec:practical_magnitude}",
          "+For representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.",
          "+",
          " \\paragraph{Cross-model validation.}",
          " The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.",
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

_source line 43_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01RYFqG58iWVLd6zESem27o9`</summary>

```json
{
  "todos": [
    {
      "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
      "status": "completed",
      "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
    },
    {
      "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
      "status": "completed",
      "activeForm": "Adding cluster-robust CI to §4.2"
    },
    {
      "content": "Edit 3: W2 practical effect paragraph in §4.3",
      "status": "completed",
      "activeForm": "Adding practical magnitude paragraph to §4.3"
    },
    {
      "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
      "status": "in_progress",
      "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
    },
    {
      "content": "Edit 5: C1 prompt version annotation",
      "status": "pending",
      "activeForm": "Adding v1 prompt annotation to §4"
    },
    {
      "content": "Edit 6: MW4 Figure 2 appendix ref",
      "status": "pending",
      "activeForm": "Fixing Figure ref to include Appendix"
    },
    {
      "content": "Edit 7: framework → pattern (verify no occurrences)",
      "status": "pending",
      "activeForm": "Checking framework→pattern replacement"
    },
    {
      "content": "Compile and verify",
      "status": "pending",
      "activeForm": "Compiling LaTeX and verifying"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "53737b39-e1fe-4114-9e13-0fb53d9de2be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9deEny38hXrkViuu6NDcB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 37996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 515
      },
      "output_tokens": 72,
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

_source line 44 · 2026-05-16T03:43:12.183Z_

<details><summary>↩ Tool result · `toolu_01RYFqG58iWVLd6zESem27o9`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "2fccb72e-441f-4762-b1c4-fc2fbcd644be",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "completed",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "completed",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "in_progress",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "pending",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "pending",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "pending",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "pending",
        "activeForm": "Checking framework→pattern replacement"
      },
      {
        "content": "Compile and verify",
        "status": "pending",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "newTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "completed",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "completed",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "completed",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "in_progress",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "pending",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "pending",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "pending",
        "activeForm": "Checking framework→pattern replacement"
      },
      {
        "content": "Compile and verify",
        "status": "pending",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 45_

Edit 4: Add extreme-batch caveats to 31.2pp occurrences. Let me find all current occurrences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "4ad1fbee-3958-4afe-9018-816ccf07467d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXHATV85Uw7vevkNvyutZ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 38511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
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

_source line 46_

<details open><summary>🔧 Tool call — Grep · `toolu_01KMTuPu92A3QTyEMAVCPZ7D`</summary>

```json
{
  "pattern": "31\\.2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "827b63f4-efa0-46b8-b773-d92ea69afb18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXHATV85Uw7vevkNvyutZ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 38511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
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

_source line 47 · 2026-05-16T03:43:15.882Z_

<details><summary>↩ Tool result · `toolu_01KMTuPu92A3QTyEMAVCPZ7D`</summary>

```text
64:[Omitted long matching line]
80:80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
81:80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
84:\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\,pp at 16 relations to 31.2\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
88:[Omitted long matching line]
117:[Omitted long matching line]
121:[Omitted long matching line]
124:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "d5bc5ead-2551-4843-b4ba-5574223d3890",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "64:[Omitted long matching line]\n80:80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n81:80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n84:\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n88:[Omitted long matching line]\n117:[Omitted long matching line]\n121:[Omitted long matching line]\n124:[Omitted long matching line]",
    "numLines": 8
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01GucS8o6WkH8yE4jo9XYW6V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": 60,
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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "be36e314-6fb7-4b05-8e8a-23f35d86b5de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZsBcNjm2Pb19gxQdPKWEQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 38978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
      },
      "output_tokens": 65,
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

_source line 49 · 2026-05-16T03:43:19.175Z_

<details><summary>↩ Tool result · `toolu_01GucS8o6WkH8yE4jo9XYW6V`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "6ebdbfed-c852-483e-9079-40988aad7b46",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "The correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.",
      "numLines": 10,
      "startLine": 60,
      "totalLines": 136
    }
  }
}
```

</details>

---

### Assistant

_source line 50_

Now let me handle each 31.2 occurrence. Line 64 — in §4.2 pairwise discussion:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "7f8b5d54-c34a-4be5-8845-a9427961cfae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UoAW1wYPwHEJiUG1DSed83",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 39408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 886
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

_source line 51_

<details open><summary>🔧 Tool call — Edit · `toolu_01JUxXRD5EXVqf4WCSr6BfKR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.",
  "new_string": "the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "57b28590-4bac-44dc-bffa-f79d0cfb67a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UoAW1wYPwHEJiUG1DSed83",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 39408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 886
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

_source line 52 · 2026-05-16T03:43:25.383Z_

<details><summary>↩ Tool result · `toolu_01JUxXRD5EXVqf4WCSr6BfKR`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "c36e4360-c452-4ad3-89e7-79df47a7a2d6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.",
    "newString": "the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 61,
        "oldLines": 7,
        "newStart": 61,
        "newLines": 7,
        "lines": [
          " ",
          " Spearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.",
          " ",
          "-The remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.",
          "+The remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.",
          " ",
          " \\subsection{BCS-Controlled Experiments}",
          " \\label{sec:bcs_controlled}"
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

_source line 53_

Line 84 — Table 3 caption:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "abf8564e-a901-4448-8039-46f090e8f15f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019yrzvvKb4zCpgRDD66HX5s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 40294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
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

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_017tpwwSUQrzcQ2inV8W7MN9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations.",
  "new_string": "The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "2121ad54-21a3-4280-b1a5-30d82f0f9bd1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019yrzvvKb4zCpgRDD66HX5s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 40294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
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

_source line 55 · 2026-05-16T03:43:29.794Z_

<details><summary>↩ Tool result · `toolu_017tpwwSUQrzcQ2inV8W7MN9`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "e5775334-425b-4d60-b183-d58951d9ea16",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations.",
    "newString": "The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 81,
        "oldLines": 7,
        "newStart": 81,
        "newLines": 7,
        "lines": [
          " 80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\",
          " \\bottomrule",
          " \\end{tabular}}",
          "-\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}",
          "+\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}",
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

### Assistant

_source line 56_

Line 88 — §4.3 first paragraph "the gap reaches 31.2\,pp":

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "fddbdd06-846f-4c8d-b570-39e6fbf44408",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5TcASwwrUfs7QgHepDNDu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 298,
      "cache_read_input_tokens": 40635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 298
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

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_014kQsRR5o2QhwdFezEwFCNZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": 86,
  "limit": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "bdd90316-1bee-49d6-8751-f83a0058cd50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5TcASwwrUfs7QgHepDNDu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 298,
      "cache_read_input_tokens": 40635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 298
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

_source line 58 · 2026-05-16T03:43:35.431Z_

<details><summary>↩ Tool result · `toolu_014kQsRR5o2QhwdFezEwFCNZ`</summary>

```text
86	\end{table}
87	
88	At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\,pp (95\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\,=\,16$, the gap remains 31.2\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\,=\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\,pp (count 8) and $-$31.8\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.
89	
90	The larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\S\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.
91	
92	\paragraph{Within-pool controlled comparison.}
93	\label{sec:within_pool}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "d9700486-cd96-497c-8a98-12b151382ef9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}",
      "numLines": 8,
      "startLine": 86,
      "totalLines": 136
    }
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Edit · `toolu_018LHnV4zgN1sgVcnu9skqs6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]).",
  "new_string": "At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6])."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "2ecf2965-46fb-4ef5-80cb-e582538a975d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K45Bki8JfeKrPo6eToy3xe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 530,
      "cache_read_input_tokens": 40933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 530
      },
      "output_tokens": 72,
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

_source line 60 · 2026-05-16T03:43:39.882Z_

<details><summary>↩ Tool result · `toolu_018LHnV4zgN1sgVcnu9skqs6`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "f5fa992b-19ce-4ce9-a1c0-0d2b341223f5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]).",
    "newString": "At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 85,
        "oldLines": 7,
        "newStart": 85,
        "newLines": 7,
        "lines": [
          " \\label{tab:bcs_controlled}",
          " \\end{table}",
          " ",
          "-At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.",
          "+At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.",
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

_source line 61_

Now line 117 and 121 — the within-pool reinterpretation and cross-model paragraphs:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "3da4cbc6-4b3f-4531-bcc6-dfbae249f916",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015AkaJd8PwEZnzyP3auh7h5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 41463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 638
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

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_01WDLqurBRzXJ7J6Le4hZjds`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": 115,
  "limit": 18
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "fe2e3f84-454e-4555-88b7-85bf7aca77a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015AkaJd8PwEZnzyP3auh7h5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 41463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 638
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

_source line 63 · 2026-05-16T03:43:43.622Z_

<details><summary>↩ Tool result · `toolu_01WDLqurBRzXJ7J6Le4hZjds`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "75c6a76d-b72b-4191-9cb7-813ff6fc08b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n",
      "numLines": 18,
      "startLine": 115,
      "totalLines": 136
    }
  }
}
```

</details>

---

### Assistant

_source line 64_

Line 117: the within-pool 31.2 already has context about "wider BCS range" — add explicit "(extreme-batch comparison)".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "f71b0ec0-8f9b-4099-91f5-e28598e0b269",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lr8F86bKykFsP1q9cphRCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1338,
      "cache_read_input_tokens": 42101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1338
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

_source line 65_

<details open><summary>🔧 Tool call — Edit · `toolu_01MdZwYyy6iTkcVyNNfzScf9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.",
  "new_string": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "ce6ea7ad-e14b-4975-b2b3-2c39bd172584",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lr8F86bKykFsP1q9cphRCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1338,
      "cache_read_input_tokens": 42101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1338
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

_source line 66 · 2026-05-16T03:43:51.433Z_

<details><summary>↩ Tool result · `toolu_01MdZwYyy6iTkcVyNNfzScf9`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "f5ec1e68-227f-484a-9d4f-739f132e7d9c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.",
    "newString": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 114,
        "oldLines": 7,
        "newStart": 114,
        "newLines": 7,
        "lines": [
          " \\label{tab:within_pool}",
          " \\end{table}",
          " ",
          "-The within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.",
          "+The within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
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

### Assistant

_source line 67_

Line 124: cross-model "Qwen3-32B's $-$31.2\,pp" — add caveat:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "68e75610-0eb6-4d08-908d-f26dbdb95cd5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoKjRih9duB5v1Yzge9z9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 335,
      "cache_read_input_tokens": 43439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 335
      },
      "output_tokens": 3,
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

_source line 68_

<details open><summary>🔧 Tool call — Edit · `toolu_017NBtjBTpSqfC7B9QmM3wzq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp.",
  "new_string": "reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "1297b414-6a87-4bb9-8fb4-65da66958332",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoKjRih9duB5v1Yzge9z9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 335,
      "cache_read_input_tokens": 43439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 335
      },
      "output_tokens": 3,
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

_source line 69 · 2026-05-16T03:43:56.306Z_

<details><summary>↩ Tool result · `toolu_017NBtjBTpSqfC7B9QmM3wzq`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "d698f29d-99dc-4abc-bb85-3f37b6f9c047",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp.",
    "newString": "reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap.",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 121,
        "oldLines": 7,
        "newStart": 121,
        "newLines": 7,
        "lines": [
          " For representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.",
          " ",
          " \\paragraph{Cross-model validation.}",
          "-The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.",
          "+The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.",
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

_source line 70_

Line 121 (practical magnitude paragraph) already has "extreme-batch" caveats built in. Now edits 5, 6, 7.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "f985d8c7-cce6-49ee-947c-ca76744bc36f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sQsimtgVV4GXrYdkXrfSH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 281,
      "cache_read_input_tokens": 43774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 281
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

_source line 71_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01TncGfoeAjPutzGx2UfPwUm`</summary>

```json
{
  "todos": [
    {
      "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
      "status": "completed",
      "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
    },
    {
      "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
      "status": "completed",
      "activeForm": "Adding cluster-robust CI to §4.2"
    },
    {
      "content": "Edit 3: W2 practical effect paragraph in §4.3",
      "status": "completed",
      "activeForm": "Adding practical magnitude paragraph to §4.3"
    },
    {
      "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
      "status": "completed",
      "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
    },
    {
      "content": "Edit 5: C1 prompt version annotation",
      "status": "in_progress",
      "activeForm": "Adding v1 prompt annotation to §4"
    },
    {
      "content": "Edit 6: MW4 Figure 2 appendix ref",
      "status": "pending",
      "activeForm": "Fixing Figure ref to include Appendix"
    },
    {
      "content": "Edit 7: framework → pattern (verify no occurrences)",
      "status": "pending",
      "activeForm": "Checking framework→pattern replacement"
    },
    {
      "content": "Compile and verify",
      "status": "pending",
      "activeForm": "Compiling LaTeX and verifying"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "b8666fb8-e10c-4249-adb8-dfe131dd016c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sQsimtgVV4GXrYdkXrfSH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 281,
      "cache_read_input_tokens": 43774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 281
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

_source line 72 · 2026-05-16T03:44:04.255Z_

<details><summary>↩ Tool result · `toolu_01TncGfoeAjPutzGx2UfPwUm`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "18d9d29d-cba8-4e31-9fcc-4715e7fcaede",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "completed",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "completed",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "completed",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "in_progress",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "pending",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "pending",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "pending",
        "activeForm": "Checking framework→pattern replacement"
      },
      {
        "content": "Compile and verify",
        "status": "pending",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "newTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "completed",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "completed",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "completed",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "completed",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "in_progress",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "pending",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "pending",
        "activeForm": "Checking framework→pattern replacement"
      },
      {
        "content": "Compile and verify",
        "status": "pending",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 73_

Edit 5: Add v1 prompt annotation at the start of §4. The section starts with `\section{Results}`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "a1e18764-108e-484a-a82e-28fca185ec4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QG9B8nVe32sQLbefwfSZps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 502,
      "cache_read_input_tokens": 44055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 502
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

_source line 74_

<details open><summary>🔧 Tool call — Edit · `toolu_01AKC7X1rDYtz3AUUJn9npss`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}",
  "new_string": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "bfbb5b5f-82a0-478b-907e-6437d7a441ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QG9B8nVe32sQLbefwfSZps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 502,
      "cache_read_input_tokens": 44055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 502
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

_source line 75 · 2026-05-16T03:44:10.536Z_

<details><summary>↩ Tool result · `toolu_01AKC7X1rDYtz3AUUJn9npss`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "905d66a2-9c39-4221-9f78-4d759ed7fb05",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}",
    "newString": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 8,
        "lines": [
          " \\section{Results}",
          " \\label{sec:results}",
          " ",
          "+Unless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).",
          "+",
          " \\subsection{Count-Degradation Curves}",
          " \\label{sec:count_curves}",
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

_source line 76_

Edit 6: Fix Figure ref to include Appendix reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "8904e1b1-0ad4-4616-b8ba-e431d482d54c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2YEGdW1kjLTdiAZsGLkmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 319,
      "cache_read_input_tokens": 44557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 319
      },
      "output_tokens": 5,
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

_source line 77_

<details open><summary>🔧 Tool call — Edit · `toolu_012EYXgGxdvPjXiZA73ogBVK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "see also Figure~\\ref{fig:error_taxonomy})",
  "new_string": "see also Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "4b530b12-8f52-47ed-854a-9a9f0dbba068",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2YEGdW1kjLTdiAZsGLkmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 319,
      "cache_read_input_tokens": 44557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 319
      },
      "output_tokens": 5,
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

_source line 78 · 2026-05-16T03:44:14.451Z_

<details><summary>↩ Tool result · `toolu_012EYXgGxdvPjXiZA73ogBVK`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "8844c5c3-17c9-4983-99d9-a8e689ef0ec2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "see also Figure~\\ref{fig:error_taxonomy})",
    "newString": "see also Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures})",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.057, 0.190]; MAVEN: [0.070, 0.139]; $B = 10{,}000$); the pair-level CIs in Table~\\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled}; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (extreme-batch comparison; 95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\\,pp vs.\\ $-$7.42\\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\\ 0.65--0.90; see Appendix~\\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the 31.2\\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\\%, versus 78.9\\% for top-quartile batches, a gap of 3.9\\,pp. The 31.2\\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\\,pp.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp extreme-batch gap. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--error correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 128,
        "oldLines": 7,
        "newStart": 128,
        "newLines": 7,
        "lines": [
          " \\subsection{Multi-Channel Degradation}",
          " \\label{sec:multi_channel}",
          " ",
          "-We decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.",
          "+We decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.",
          " ",
          " These results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.",
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

_source line 79_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01XRijs3b1AUErJ7jv248EeS`</summary>

```json
{
  "todos": [
    {
      "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
      "status": "completed",
      "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
    },
    {
      "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
      "status": "completed",
      "activeForm": "Adding cluster-robust CI to §4.2"
    },
    {
      "content": "Edit 3: W2 practical effect paragraph in §4.3",
      "status": "completed",
      "activeForm": "Adding practical magnitude paragraph to §4.3"
    },
    {
      "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
      "status": "completed",
      "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
    },
    {
      "content": "Edit 5: C1 prompt version annotation",
      "status": "completed",
      "activeForm": "Adding v1 prompt annotation to §4"
    },
    {
      "content": "Edit 6: MW4 Figure 2 appendix ref",
      "status": "completed",
      "activeForm": "Fixing Figure ref to include Appendix"
    },
    {
      "content": "Edit 7: framework → pattern (verify no occurrences)",
      "status": "completed",
      "activeForm": "No occurrences of framework in results.tex"
    },
    {
      "content": "Compile and verify",
      "status": "in_progress",
      "activeForm": "Compiling LaTeX and verifying"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "a9e993c5-59e8-4001-8156-fa9d5d17389c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMVyD3yULtAFXESW2mFPa1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 44876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 251
      },
      "output_tokens": 73,
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

_source line 80 · 2026-05-16T03:44:19.914Z_

<details><summary>↩ Tool result · `toolu_01XRijs3b1AUErJ7jv248EeS`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "e10a8e55-eca3-4421-a5aa-a5b0966111fc",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "completed",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "completed",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "completed",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "completed",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "in_progress",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "pending",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "pending",
        "activeForm": "Checking framework→pattern replacement"
      },
      {
        "content": "Compile and verify",
        "status": "pending",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "newTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "completed",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "completed",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "completed",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "completed",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "completed",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "completed",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "completed",
        "activeForm": "No occurrences of framework in results.tex"
      },
      {
        "content": "Compile and verify",
        "status": "in_progress",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 81_

All edits applied. "framework" had zero occurrences in results.tex — nothing to change. Now let me verify the final file looks correct, then compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "815887f4-b55e-4b4c-9b0f-18421c32bc5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJM8qNGiX56oeWCgMZ2hWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 45127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 468
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

_source line 82_

<details open><summary>🔧 Tool call — Read · `toolu_01NZoyjuBgTzBPkCH5Vjaz2k`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "80bde6da-e3b0-48f6-b0d2-14a75cef49c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJM8qNGiX56oeWCgMZ2hWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 45127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 468
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

_source line 83 · 2026-05-16T03:44:23.764Z_

<details><summary>↩ Tool result · `toolu_01NZoyjuBgTzBPkCH5Vjaz2k`</summary>

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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "1c008c13-c59a-4ff7-b90a-7a4d4ddfdbf1",
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

_source line 84_

File looks correct. Now compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "31947b61-feae-48be-9338-b4975d326550",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJ4GzSHvr1xGtEqWFqzYQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5889,
      "cache_read_input_tokens": 45595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5889
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

_source line 85_

<details open><summary>🔧 Tool call — Bash · `toolu_01RhwjQR6VKGoA29oJUvMYS1`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "First pdflatex pass",
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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "fa923db1-e469-4ab3-b777-e6a17fd9d5bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJ4GzSHvr1xGtEqWFqzYQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5889,
      "cache_read_input_tokens": 45595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5889
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

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b1i9wan56",
  "tool_use_id": "toolu_01RhwjQR6VKGoA29oJUvMYS1",
  "description": "First pdflatex pass",
  "task_type": "local_bash",
  "uuid": "38dd1b00-741b-4d36-a7ea-8824d2abb2db",
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5"
}
```

---

### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b1i9wan56",
  "tool_use_id": "toolu_01RhwjQR6VKGoA29oJUvMYS1",
  "status": "completed",
  "output_file": "",
  "summary": "First pdflatex pass",
  "uuid": "bec259b4-9e39-4b01-92fd-34003e15205d",
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5"
}
```

---

### Tool result

_source line 88 · 2026-05-16T03:44:33.192Z_

<details><summary>↩ Tool result · `toolu_01RhwjQR6VKGoA29oJUvMYS1`</summary>

```text
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/u
tmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (15 pages, 385600 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "af0305c8-9001-4ecf-aa05-352688b4b933",
  "tool_use_result": {
    "stdout": "share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/u\ntmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (15 pages, 385600 bytes).\nTranscript written on main.log.",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01T9vyy7HRm1CvpVRY5ksU63`</summary>

```json
{
  "command": "bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
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
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "1d23237e-3759-4a39-8f31-f01824fbd995",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Czf9ZDwH9A2AgGoPCpS9TK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 908,
      "cache_read_input_tokens": 51484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 908
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

### System

_source line 90_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bamcfqzqw",
  "tool_use_id": "toolu_01T9vyy7HRm1CvpVRY5ksU63",
  "description": "bibtex + two more pdflatex passes",
  "task_type": "local_bash",
  "uuid": "5a454ca8-f4c8-4e10-91ff-5f07d0892a60",
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5"
}
```

---

### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bamcfqzqw",
  "tool_use_id": "toolu_01T9vyy7HRm1CvpVRY5ksU63",
  "status": "completed",
  "output_file": "",
  "summary": "bibtex + two more pdflatex passes",
  "uuid": "3fba8881-536c-468b-a47a-421544cdabfd",
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5"
}
```

---

### Tool result

_source line 92 · 2026-05-16T03:44:43.090Z_

<details><summary>↩ Tool result · `toolu_01T9vyy7HRm1CvpVRY5ksU63`</summary>

```text
Database file #1: references.bib
Warning--I didn't find a database entry for "ding-fewnerd-2021"
Warning--I didn't find a database entry for "wang-maven-2020"
Warning--I didn't find a database entry for "han-fewrel-2018"
(There were 3 warnings)
onts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (15 pages, 385637 bytes).
Transcript written on main.log.
onts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (15 pages, 385555 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "3c58e47e-0eb3-4fed-a661-6bf83478f74f",
  "tool_use_result": {
    "stdout": "Database file #1: references.bib\nWarning--I didn't find a database entry for \"ding-fewnerd-2021\"\nWarning--I didn't find a database entry for \"wang-maven-2020\"\nWarning--I didn't find a database entry for \"han-fewrel-2018\"\n(There were 3 warnings)\nonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (15 pages, 385637 bytes).\nTranscript written on main.log.\nonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (15 pages, 385555 bytes).\nTranscript written on main.log.",
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

_source line 93_

Let me verify no LaTeX errors occurred.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "b3713331-4507-403e-b53e-4d0b489357e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DfFZBr4H5xjfuDGQsUeZtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 346,
      "cache_read_input_tokens": 52392,
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

### Tool call

_source line 94_

<details open><summary>🔧 Tool call — Bash · `toolu_01KFZ6djhUCY4o1F9cppYqvt`</summary>

```json
{
  "command": "grep -c \"^!\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.log",
  "description": "Count LaTeX errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "1f26fed9-9993-4865-a075-2d9cd3c6e8ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DfFZBr4H5xjfuDGQsUeZtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 346,
      "cache_read_input_tokens": 52392,
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

### Tool result

_source line 95 · 2026-05-16T03:44:46.520Z_

<details><summary>↩ Tool result · `toolu_01KFZ6djhUCY4o1F9cppYqvt`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "58d22063-0750-413d-9db2-1726535963d3",
  "tool_use_result": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 96_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01LFrMcvRRYQh7Wa17usFtcN`</summary>

```json
{
  "todos": [
    {
      "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
      "status": "completed",
      "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
    },
    {
      "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
      "status": "completed",
      "activeForm": "Adding cluster-robust CI to §4.2"
    },
    {
      "content": "Edit 3: W2 practical effect paragraph in §4.3",
      "status": "completed",
      "activeForm": "Adding practical magnitude paragraph to §4.3"
    },
    {
      "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
      "status": "completed",
      "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
    },
    {
      "content": "Edit 5: C1 prompt version annotation",
      "status": "completed",
      "activeForm": "Adding v1 prompt annotation to §4"
    },
    {
      "content": "Edit 6: MW4 Figure 2 appendix ref",
      "status": "completed",
      "activeForm": "Fixing Figure ref to include Appendix"
    },
    {
      "content": "Edit 7: framework → pattern (verify no occurrences)",
      "status": "completed",
      "activeForm": "No occurrences of framework in results.tex"
    },
    {
      "content": "Compile and verify",
      "status": "completed",
      "activeForm": "Compiling LaTeX and verifying"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "f4cd7ab5-3349-495c-aeb0-8fe754961da6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nF3wfTyybHsZ2h8ZZ4Ani",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 135,
      "cache_read_input_tokens": 52738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 135
      },
      "output_tokens": 42,
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

_source line 97 · 2026-05-16T03:44:56.026Z_

<details><summary>↩ Tool result · `toolu_01LFrMcvRRYQh7Wa17usFtcN`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "7fb2b707-2fca-4e29-8c34-229e0936c06e",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "completed",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "completed",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "completed",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "completed",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "completed",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "completed",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "completed",
        "activeForm": "No occurrences of framework in results.tex"
      },
      {
        "content": "Compile and verify",
        "status": "in_progress",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "newTodos": [
      {
        "content": "Edit 1: W4 count curves macro-avg + CI (§4.1 line 25)",
        "status": "completed",
        "activeForm": "Editing §4.1 count curves with macro-avg recall and CI"
      },
      {
        "content": "Edit 2: W3 cluster bootstrap CI in §4.2 pairwise discussion",
        "status": "completed",
        "activeForm": "Adding cluster-robust CI to §4.2"
      },
      {
        "content": "Edit 3: W2 practical effect paragraph in §4.3",
        "status": "completed",
        "activeForm": "Adding practical magnitude paragraph to §4.3"
      },
      {
        "content": "Edit 4: C3 caveat on all 31.2pp occurrences",
        "status": "completed",
        "activeForm": "Adding extreme-batch caveats to 31.2pp mentions"
      },
      {
        "content": "Edit 5: C1 prompt version annotation",
        "status": "completed",
        "activeForm": "Adding v1 prompt annotation to §4"
      },
      {
        "content": "Edit 6: MW4 Figure 2 appendix ref",
        "status": "completed",
        "activeForm": "Fixing Figure ref to include Appendix"
      },
      {
        "content": "Edit 7: framework → pattern (verify no occurrences)",
        "status": "completed",
        "activeForm": "No occurrences of framework in results.tex"
      },
      {
        "content": "Compile and verify",
        "status": "completed",
        "activeForm": "Compiling LaTeX and verifying"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 98_

全部完成。编译 0 错误，15 页。

改动摘要：
1. **§4.1 NER**: recall 改为 macro-avg (0.52/0.55)，加 bootstrap CI + permutation p=0.31 + 重叠说明
2. **§4.2 pairwise**: 在 Table 2 后讨论中加 cluster-robust CI（Few-NERD [0.057,0.190]，MAVEN [0.070,0.139]），Table 保留 pair-level CI
3. **§4.3 新段 Practical magnitude**: IQR=0.054 → 2.2pp gap，quartile 对比 3.9pp，P10-P90 4.2pp，明确 31.2pp 是 extreme-batch
4. **31.2pp 所有出现**（6处）均加 "extreme-batch" caveat 或指向 §practical_magnitude
5. **§4 开头**: 加 v1 prompt 总注
6. **§4.4**: Figure ref 改为 "Figure X in Appendix A"
7. **framework→pattern**: results.tex 中无 "framework"，无需改动
8. bibtex 有 3 个预存 warning（cite key 不匹配），非本次引入

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "uuid": "96365ca0-cb0f-43eb-aa3a-5641b0e0297d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDHR5mTD8fUivAXLipaKdG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 52873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 466
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

_source line 99_

全部完成。编译 0 错误，15 页。

改动摘要：
1. **§4.1 NER**: recall 改为 macro-avg (0.52/0.55)，加 bootstrap CI + permutation p=0.31 + 重叠说明
2. **§4.2 pairwise**: 在 Table 2 后讨论中加 cluster-robust CI（Few-NERD [0.057,0.190]，MAVEN [0.070,0.139]），Table 保留 pair-level CI
3. **§4.3 新段 Practical magnitude**: IQR=0.054 → 2.2pp gap，quartile 对比 3.9pp，P10-P90 4.2pp，明确 31.2pp 是 extreme-batch
4. **31.2pp 所有出现**（6处）均加 "extreme-batch" caveat 或指向 §practical_magnitude
5. **§4 开头**: 加 v1 prompt 总注
6. **§4.4**: Figure ref 改为 "Figure X in Appendix A"
7. **framework→pattern**: results.tex 中无 "framework"，无需改动
8. bibtex 有 3 个预存 warning（cite key 不匹配），非本次引入

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 195783,
  "duration_api_ms": 187229,
  "num_turns": 34,
  "stop_reason": "end_turn",
  "session_id": "adce43c8-ca9c-4cd9-adb6-934161c9e8a5",
  "total_cost_usd": 1.0964005,
  "usage": {
    "input_tokens": 35,
    "cache_creation_input_tokens": 41498,
    "cache_read_input_tokens": 1226634,
    "output_tokens": 8830,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 41498,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 346,
        "cache_read_input_tokens": 52873,
        "cache_creation_input_tokens": 466,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 466
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2686,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002796,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 35,
      "outputTokens": 8830,
      "cacheReadInputTokens": 1226634,
      "cacheCreationInputTokens": 41498,
      "webSearchRequests": 0,
      "costUSD": 1.0936044999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "efa1890d-eda2-468d-b359-061017689615"
}
```

</details>

---
