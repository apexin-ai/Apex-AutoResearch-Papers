# Research conversation: Read lines 250-491 of /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/app

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6464752dec190ef4.jsonl`
- **Structured JSON:** [`30dd7472213c7e4ee62f.json`](../../sessions/30/30dd7472213c7e4ee62f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-25T19:42:10.620Z_

Read lines 250-491 of /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex and extract EVERY numerical value that appears. For each number, report:
- The exact value as it appears in the text
- The line number
- Whether it's in a table, figure caption, or body text
- What it represents (metric name, statistic type, etc.)

Be exhaustive - include percentages, counts, p-values, correlation coefficients, ratios, standard deviations, everything. Group them by table/section for clarity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "00884a06-3250-4c87-b491-3b7baf3c5516",
  "agentId": "a6464752dec190ef4",
  "type": "user",
  "uuid": "12eae469-ac55-438d-8494-8ef025d9b750",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T19:42:12.324Z_

I'll read the specified lines from the appendix and extract all numerical values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12eae469-ac55-438d-8494-8ef025d9b750",
  "isSidechain": true,
  "agentId": "a6464752dec190ef4",
  "requestId": "req_011CbPrgcgTutfBDquoxJ4eS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "49c44471-9464-4a38-8e0d-1b5d49370a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NMNnuaLpnwReCzC8JXZK75",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 567,
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

_source line 3 · 2026-05-25T19:42:12.878Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VxAdfoqHUVUrX4Nx86AcrD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
  "offset": 250,
  "limit": 242
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49c44471-9464-4a38-8e0d-1b5d49370a50",
  "isSidechain": true,
  "agentId": "a6464752dec190ef4",
  "requestId": "req_011CbPrgcgTutfBDquoxJ4eS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "42576876-71b3-474d-8ee3-46e54282c77f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NMNnuaLpnwReCzC8JXZK75",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 39102,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 567
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 141,
          "cache_read_input_tokens": 39102,
          "cache_creation_input_tokens": 567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 567,
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

_source line 4 · 2026-05-25T19:42:12.890Z_

<details><summary>↩ Tool result · `toolu_01VxAdfoqHUVUrX4Nx86AcrD`</summary>

```text
250	\label{tab:test_tax}
251	\small
252	\resizebox{\columnwidth}{!}{%
253	\begin{tabular}{lcccc}
254	\toprule
255	\textbf{Model} & \textbf{With-evi} & \textbf{No-evi} & \textbf{Test Tax} & \textbf{Dev Tax} \\
256	\midrule
257	Qwen3-1.7B & 25.79 & 20.93 & $-$4.86 & $-$5.63 \\
258	Qwen3-4B & 22.32 & 22.19 & $-$0.13 & +0.25 \\
259	Qwen3-8B & 31.06 & 29.35 & $-$1.71 & +0.04 \\
260	Qwen3-14B & 38.86 & 38.54 & $-$0.32 & +0.03 \\
261	LLaMA-3.1-8B & 34.20 & 29.26 & $-$4.94 & $-$5.19 \\
262	\bottomrule
263	\end{tabular}%
264	}
265	\end{table}
266	
267	\paragraph{RSFT test-set evidence tax.}
268	Table~\ref{tab:rsft_test_tax} reports the inference-time evidence tax for RSFT models on the Re-DocRED test set (same RSFT model evaluated with vs.\ without evidence output; per-seed s42 values). Figure~\ref{fig:evidence_tax} presents multi-seed means with error bars where $\geq$2 seeds are available. At 1.7B, RSFT preserves a strong evidence benefit ($-$5.01$\pm$0.59pp, two-seed mean), comparable to the SFT tax ($-$4.86pp). At 4B, the tax is mildly positive (+1.65$\pm$0.29pp, three-seed mean; s42: +1.51pp), the Qwen3 scale with the largest positive RSFT test tax; this contrasts with the near-neutral SFT tax at 4B ($-$0.13pp). At 8B, RSFT compresses the tax magnitude relative to SFT ($-$0.91$\pm$0.74pp, three-seed mean, vs.\ SFT $-$1.71pp). At 14B, the three-seed mean tax is +0.12$\pm$0.64pp (s42: +0.77pp, s43: +0.08pp, s44: $-$0.50pp), reversing sign relative to dev ($-$1.53$\pm$2.79pp, three-seed mean); the small test magnitude and high inter-seed variance may reflect noise or evaluation protocol differences given the 2.82$\times$ annotation density gap between dev and test. LLaMA-3.1-8B shows partial compression from SFT ($-$4.94pp $\to$ $-$1.46$\pm$0.40pp, two-seed mean).
269	
270	\begin{table}[t]
271	\centering
272	\caption{RSFT inference-time evidence tax on Re-DocRED test set (Ign-F1 \%). Tax $=$ no-evi $-$ with-evi; positive $=$ cost. Per-seed s42 except where noted.}
273	\label{tab:rsft_test_tax}
274	\small
275	\resizebox{\columnwidth}{!}{%
276	\begin{tabular}{lccc}
277	\toprule
278	\textbf{Model} & \textbf{RSFT w/ evi} & \textbf{RSFT no-evi} & \textbf{RSFT Tax} \\
279	\midrule
280	Qwen3-1.7B & 29.02{\scriptsize$\pm$0.45}$^{(2)}$ & 24.00{\scriptsize$\pm$0.14}$^{(2)}$ & $-$5.01{\scriptsize$\pm$0.59}$^{(2)}$ \\
281	Qwen3-4B & 25.01 & 26.52 & +1.51 \\
282	Qwen3-8B & 33.53 & 33.19 & $-$0.34 \\
283	Qwen3-14B & 38.49 & 39.26 & +0.77$^\dagger$ \\
284	LLaMA-3.1-8B & 35.54 & 33.80 & $-$1.74 \\
285	\bottomrule
286	\end{tabular}%
287	}
288	\vspace{1mm}
289	{\raggedright\footnotesize $^{(2)}$Two-seed mean$\pm$std (s42, s43). $^\dagger$14B shows dev-test sign reversal (dev tax $-$1.53$\pm$2.79pp, three-seed mean); three-seed test mean +0.12$\pm$0.64pp. All other scales preserve dev-test direction consistency.\par}
290	\end{table}
291	
292	\paragraph{Comparison to supervised methods.}
293	Table~\ref{tab:encoder_comparison} directly compares encoder-based methods with our LLM-based approach. Encoder methods achieve substantially higher extraction performance (Rel-F1 63--65 vs.\ our 46--60), reflecting decades of architecture-specific optimization for the classification formulation. However, their evidence identification operates as binary sentence classification, producing Evi-F1 of 52--56 under a joint evaluation protocol. Our TP-only Evi-F1 exceeds 80\%, indicating that when the model correctly identifies a triple, it produces higher-quality evidence than encoder methods. The joint Evi-F1 gap (36.1 vs.\ 54.15) is driven primarily by extraction performance rather than evidence quality: false-positive and false-negative triples dilute the denominator. The extraction gap varies with scale (16--18pp Ign-F1 at 4B, narrowing to $<$5pp at 14B), reflecting the rapid scaling of generative approaches relative to encoder methods. Further closing this gap at smaller scales requires improving extraction capability of LLM-based methods, an orthogonal direction to the evidence faithfulness problem we address.
294	
295	\begin{table}[t]
296	\centering
297	\caption{Comparison with encoder-based methods on DocRED dev set. Encoder methods use RoBERTa-large; LLM methods use Qwen3. Evi-F1 for encoder methods uses joint evaluation (all triples in denominator); our joint Evi-F1 follows the same protocol for fair comparison. TP-only Evi-F1 conditions on correctly predicted triples. Rel-F1 is reported in percentage for all methods.}
298	\label{tab:encoder_comparison}
299	\small
300	\resizebox{\columnwidth}{!}{%
301	\begin{tabular}{llcccc}
302	\toprule
303	\textbf{Method} & \textbf{Type} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1 (joint)} & \textbf{Evi-F1 (TP)} \\
304	\midrule
305	ATLOP & Encoder & 61.32 & 63.18 & -- & -- \\
306	EIDER & Encoder & 62.34 & 64.27 & 52.54 & -- \\
307	SAIS & Encoder & 62.23 & 65.17 & 55.84 & -- \\
308	DREEAM & Encoder & 61.71 & 63.49 & 54.15 & -- \\
309	\midrule
310	Ours (4B RSFT) & LLM & 44.82 & 45.80 & 36.1 & 80.96 \\
311	Ours (8B RSFT) & LLM & 54.33 & 56.07 & -- & 81.54 \\
312	Ours (14B RSFT) & LLM & 57.85 & 59.17 & 48.57 & 83.37 \\
313	\bottomrule
314	\end{tabular}%
315	}
316	\end{table}
317	
318	
319	\section{Decoupling Spectrum Data}
320	\label{sec:spectrum_data}
321	
322	Table~\ref{tab:spectrum} presents the full decoupling spectrum across all optimization paradigms evaluated on Qwen3-4B, quantified by EDCR and severity classification.
323	
324	\begin{table}[t]
325	\centering
326	\caption{Evidence-extraction decoupling across RL paradigms (Qwen3-4B). Severity indicates the degree of extraction collapse relative to evidence improvement.}
327	\label{tab:spectrum}
328	\small
329	\resizebox{\columnwidth}{!}{%
330	\begin{tabular}{llcccc}
331	\toprule
332	\textbf{Paradigm} & \textbf{Config} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Severity} \\
333	\midrule
334	GRPO & QLoRA $G{=}4$ & 1.38 & 85.04 & 0.9876 & Catastrophic \\
335	GRPO & bf16 $G{=}8$ & 45.49 & 80.86 & 0.6318 & Mild \\
336	DPO & bf16 1ep & 33.37 & 80.90 & 0.8123 & Gradual \\
337	DPO & bf16 3ep & 31.45 & 84.84 & 0.7503 & Gradual \\
338	\midrule
339	SFT & baseline$^\ddagger$ & 44.39 & 79.61 & 0.6797 & None \\
340	RSFT & CED$^\ddagger$ & 45.80 & 80.96 & 0.6487 & None \\
341	\bottomrule
342	\end{tabular}%
343	}
344	\vspace{1mm}
345	{\raggedright\footnotesize $^\ddagger$Three-seed mean. DPO at @2048 (matched); others at @1024. Severity reflects training trajectory stability, not final EDCR.\par}
346	\end{table}
347	
348	
349	\section{GRPO Training Dynamics}
350	\label{sec:grpo_dynamics}
351	
352	Figure~\ref{fig:grpo_dynamics} traces Rel-F1, Evi-F1, and EDCR across training checkpoints for two GRPO configurations, illustrating how catastrophic decoupling emerges under constrained optimization (G=4 QLoRA) but not under full-precision training (G=8 bf16).
353	
354	\begin{figure*}[t]
355	\centering
356	\includegraphics[width=\linewidth]{fig_grpo_dynamics.pdf}
357	\caption{Training dynamics of GRPO under different configurations. (a)~Relation F1 across checkpoints: G=4 QLoRA suffers catastrophic collapse at step~10, while G=8 bf16 remains stable. (b)~Evidence F1 stays intact for G=8 bf16, confirming the generation mechanism itself does not fail. (c)~Evidence-Decoupling Ratio (EDCR) reveals near-total decoupling in G=4 QLoRA (extraction collapses to Rel-F1 1.4), while G=8 bf16 maintains healthy ratios.}
358	\label{fig:grpo_dynamics}
359	\end{figure*}
360	
361	
362	\section{Error Analysis: SFT vs.\ RSFT}
363	\label{sec:error_analysis}
364	
365	Table~\ref{tab:error_analysis} decomposes the extraction improvements from RSFT into error categories across three scales. Three mechanisms drive the gains consistently:
366	
367	\paragraph{Truncation false negatives.} SFT models frequently hit the generation length limit, producing incomplete outputs that miss triples. RSFT training on compact, high-quality outputs reduces this truncation rate. The effect is strongest at 1.7B ($-841$ truncation FN, $-22$\%), where the SFT model's output length is least controlled.
368	
369	\paragraph{Hallucinated false positives.} CED-based filtering removes training examples with unfaithful predictions, reducing the rate of hallucinated triples at inference. LLaMA benefits most ($-593$ hallucinated FP, $-11.8$\%), suggesting cross-architecture variation in hallucination susceptibility.
370	
371	\paragraph{Duplicate predictions.} RSFT training data, selected for quality, contains fewer repetitive patterns. This propagates to inference, reducing duplicate triples by $11$--$20$\% across scales, with 1.7B showing the largest reduction ($-20.2$\%).
372	
373	\paragraph{Evidence quality unchanged.} Despite substantial extraction improvements, evidence exact-match F1 changes by less than 0.4pp at every scale. RSFT selects for joint extraction-evidence quality, but the evidence signal in CED scoring does not translate into measurable evidence improvement. This suggests that evidence grounding requires targeted optimization (e.g., evidence-specific rewards in RL) rather than data selection alone.
374	
375	\paragraph{Residual difficulty.} The proportion of ``other'' false negatives (triples missed for reasons beyond truncation or formatting) increases by 13--15\% in relative terms after RSFT. As easy errors (truncation, duplication) are eliminated, the remaining error distribution shifts toward harder cases: cross-sentence reasoning, implicit relations, and long-tail entity pairs. The relation types with the largest RSFT gains (participant, conflict, league, screenwriter, operator, contains\_administrative\_territory) involve cross-sentence reasoning or long-tail entities, consistent with RSFT's selection pressure toward diverse, high-quality outputs.
376	
377	\begin{table}[t]
378	\centering
379	\caption{Error pattern changes from SFT to RSFT across scales. $\Delta$\% shows relative change. Truncation FN, hallucinated FP, and duplicates all decrease; evidence quality and residual FN difficulty are unchanged.}
380	\label{tab:error_analysis}
381	\small
382	\resizebox{\columnwidth}{!}{%
383	\begin{tabular}{llccc}
384	\toprule
385	\textbf{Error Category} & \textbf{Direction} & \textbf{1.7B} & \textbf{4B} & \textbf{8B / LLaMA} \\
386	\midrule
387	Truncation FN & $\downarrow$ & $-$22\% & $-$16\% & $-$18\% \\
388	Hallucinated FP & $\downarrow$ & $-$8\% & $-$6\% & $-$12\% \\
389	Duplicates & $\downarrow$ & $-$20\% & $-$11\% & $-$14\% \\
390	Evidence (exact) & $\approx$ & $<$0.4pp & $<$0.4pp & $<$0.4pp \\
391	FN: other & $\uparrow$ & +13\% & +15\% & +14\% \\
392	\bottomrule
393	\end{tabular}%
394	}
395	\end{table}
396	
397	
398	\section{Per-Relation EDCR Distribution}
399	\label{sec:edcr_per_relation}
400	
401	Computing EDCR for each of the 76 relation types with $\geq$5 evaluation samples (from the RSFT CED s42 model) reveals that per-relation EDCR correlates strongly with per-relation Rel-F1 ($\rho = -0.79$, $n = 76$, $p < 0.001$), confirming its utility as a difficulty indicator. Filtering to types with $\geq$5 predictions strengthens the correlation ($\rho = -0.85$, $n = 74$, $p < 0.001$). Per-relation EDCR is statistically independent of Evi-F1 ($\rho = -0.06$, $p = 0.58$), and Evi-F1 itself shows no association with Rel-F1 ($\rho = -0.01$, $p = 0.91$). These null correlations establish that evidence quality and extraction ability are fully decoupled across relation types. Extreme cases illustrate the diagnostic power: \texttt{date\_of\_birth} has EDCR $= 0.118$ (highly faithful, with extraction and evidence tightly coupled), while \texttt{head\_of\_government} reaches $0.956$ (highly decoupled). This per-relation analysis avoids the shared-component concern present in cross-method EDCR-vs-Rel-F1 correlation, providing independent validation of EDCR's diagnostic utility. A permutation test (10,000 iterations) on the per-relation correlation yields $p < 0.0001$, confirming that the association is not an artifact of the shared TP component.
402	
403	\paragraph{Partial correlations controlling for TP.}
404	Because EDCR shares TP (true positives) in both numerator and denominator with Rel-F1, we report partial correlations controlling for Evi-Recall$_\text{TP}$. At the cross-method level ($n = 17$ seed-specific configurations), the partial Spearman $\rho = -0.8541$ ($p = 0.000025$), virtually unchanged from the raw $\rho = -0.8554$ (0.15\% reduction). Removing the GRPO QLoRA outlier yields partial $\rho = -0.8681$ ($n = 16$, $p = 0.000027$). Aggregating to $n = 7$ unique methods: raw $\rho = -0.9643$, partial $\rho = -0.9617$. These results confirm that the EDCR--Rel-F1 association is not driven by the shared TP component. Note that seed-level configurations ($n = 17$) are not fully independent; the $n = 7$ unique-method analysis provides a conservative estimate.
405	
406	\paragraph{Similar-TP, different-EDCR pairs.}
407	To further validate that EDCR captures information beyond what TP alone provides, we identify configuration pairs with similar Evi-Recall$_\text{TP}$ ($|\Delta| < 5$pp) but substantially different EDCR ($|\Delta| > 5$pp). Forty-eight such pairs exist across all configurations. The most illustrative: DPO-CED 1-epoch (Evi-Recall$_\text{TP} = 0.833$) vs.\ RSFT CED LLaMA s43 (Evi-Recall$_\text{TP} = 0.829$) differ by only 2.4pp in TP-conditioned evidence recall but 13.6pp in EDCR, reflecting the substantial extraction gap between these methods. This pattern demonstrates that EDCR captures extraction-evidence alignment that aggregate TP metrics miss.
408	
409	\begin{figure}[t]
410	\centering
411	\includegraphics[width=\linewidth]{fig_edcr_relations.pdf}
412	\caption{Per-relation EDCR distribution across all 93 relation types observed in the development set (of 96 defined in DocRED). The correlation analysis in the text uses the 76 types with $\geq$5 samples for statistical reliability. Red bars indicate EDCR $\geq$ 0.70 (severe decoupling), green bars indicate EDCR $<$ 0.30 (healthy evidence grounding). Seven types exhibit EDCR = 1.0.}
413	\label{fig:edcr_relations}
414	\end{figure}
415	
416	
417	\section{Qualitative Analysis}
418	\label{sec:qualitative}
419	
420	We present representative examples illustrating three phenomena: evidence quality differences between SFT and RSFT, GRPO format gaming under catastrophic collapse, and per-relation EDCR diagnostics.
421	
422	\paragraph{Case 1: Evidence quality.}
423	Table~\ref{tab:case_evidence} compares evidence citations from SFT and RSFT on three documents. SFT tends to cite many sentences indiscriminately, including distractors unrelated to the target triple, while RSFT selects precisely the gold evidence sentences. For \emph{America's Sweetheart}, SFT cites 6 sentences (precision 0.17) whereas RSFT cites only the single correct sentence (precision 1.00). The pattern is consistent: SFT achieves evidence precision of 0.00--0.20 across these examples, while RSFT achieves 1.00 in all three cases.
424	
425	\begin{table}[t]
426	\centering
427	\caption{Evidence citation comparison between SFT and RSFT. Precision measures the fraction of cited sentences that match gold evidence.}
428	\label{tab:case_evidence}
429	\small
430	\resizebox{\columnwidth}{!}{%
431	\begin{tabular}{llccc}
432	\toprule
433	\textbf{Document} & \textbf{Triple} & \textbf{SFT Prec.} & \textbf{RSFT Prec.} & \textbf{SFT \#Cited} \\
434	\midrule
435	Oleg Tinkov & (Oleg Tinkov, country of citizenship, Russia) & 0.00 & 1.00 & 3 \\
436	America's Sweetheart & (record label, country, United States) & 0.17 & 1.00 & 6 \\
437	Jade (Mortal Kombat) & (Jade, present in work, Mortal Kombat) & 0.20 & 1.00 & 5 \\
438	\bottomrule
439	\end{tabular}%
440	}
441	\end{table}
442	
443	\paragraph{Case 2: GRPO format gaming.}
444	Under catastrophic collapse (GRPO QLoRA $G{=}4$), the model abandons the DocRED 96-type relation ontology and generates free-text relation labels. On the document \emph{Something to Believe In}, the model produces 35 predicted triples with relations such as ``is a'', ``honor'', and ``location'', none of which belong to the target ontology. All 35 predictions are incorrect. Similarly, for \emph{J\'{o}zef Pi\l{}sudski Monument}, 28 predictions use non-standard relations with 0 correct matches. The model retains the structural format of triple-with-evidence output but fills it with fabricated relation types. The model produces well-formed evidence for these non-existent relations.
445	
446	\paragraph{Case 3: EDCR diagnostics.}
447	Per-relation EDCR identifies specific relation types where extraction and evidence are misaligned. For \texttt{date\_of\_birth} (EDCR $= 0.118$), the model's evidence consistently matches gold annotations: both extraction and evidence point to the same biographical sentence. In contrast, \texttt{notable\_work} (EDCR $= 0.941$) exhibits severe decoupling: the model cites sentence [0] (a general introduction) instead of the gold evidence sentence [3] (which contains the actual work attribution). High-EDCR relations tend to involve indirect or multi-hop reasoning where surface-level context misleads the evidence generator.
448	
449	
450	\section{Inference Efficiency Analysis}
451	\label{sec:inference_efficiency}
452	
453	Table~\ref{tab:inference_efficiency} reports wall-clock inference time for SFT models with and without evidence output under matched evaluation settings (batch size 4, \texttt{max\_new\_tokens}$=$2048, DocRED dev, 985 documents, single RTX 5090 GPU).
454	
455	\begin{table}[t]
456	\centering
457	\caption{Inference time (seconds) for SFT with vs.\ without evidence output. Overhead $=$ (with-evi $-$ no-evi) / no-evi; negative means with-evidence is faster. 1.7B--8B use batch size 4; 14B uses batch size 1.}
458	\label{tab:inference_efficiency}
459	\small
460	\resizebox{\columnwidth}{!}{%
461	\begin{tabular}{lcccc}
462	\toprule
463	\textbf{Model} & \textbf{With-evi} & \textbf{No-evi} & \textbf{Overhead} & \textbf{\#Pred (w/no)} \\
464	\midrule
465	Qwen3-1.7B & 6,424 & 7,438 & $-$13.6\% & 25.5k / 44.6k \\
466	Qwen3-4B & 8,887 & 7,606 & +16.8\% & 24.7k / 25.6k \\
467	Qwen3-8B & 10,486 & 10,901 & $-$3.8\% & 25.0k / 31.1k \\
468	\midrule
469	Qwen3-14B & 18,011 & 14,498 & +24.2\% & --- \\
470	\bottomrule
471	\end{tabular}}
472	\end{table}
473	
474	The evidence overhead is scale-dependent and non-monotonic. At 1.7B, removing evidence \emph{increases} inference time by 13.6\%: without the structural constraint of evidence fields, the model generates 1.75$\times$ more predictions (44.6k vs.\ 25.5k), producing verbose output that takes longer to decode. At 14B, evidence generation adds 24.2\% overhead, consistent with the expected cost of generating additional tokens. The crossover occurs around 4B--8B, where the prediction count differential narrows and the costs approximately balance.
475	
476	Inference time scales sub-linearly with model size: 1.7B$\to$8B (4.7$\times$ parameters) increases wall-clock time by only 1.63$\times$ at batch size 4, reflecting the memory-bound nature of autoregressive generation. Test-set inference is 2--3$\times$ slower per document than dev (e.g., 24--42 s/doc test vs.\ 7--18 s/doc dev at batch size 1), attributable to the 2.82$\times$ higher annotation density in Re-DocRED test requiring longer generated outputs.
477	
478	
479	\section{Use of AI Assistants}
480	\label{app:ai-assistants}
481	
482	We used Claude (Anthropic) as an AI coding and writing assistant
483	throughout this work. Specifically:
484	\begin{itemize}
485	    \item \textbf{Code:} drafting experiment scripts, data-processing
486	    pipelines, and analysis utilities; debugging and refactoring.
487	    \item \textbf{Writing:} drafting and revising paper sections,
488	    polishing prose, and reformatting LaTeX.
489	    \item \textbf{Literature:} summarizing related papers to inform
490	    the related-work section.
491	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42576876-71b3-474d-8ee3-46e54282c77f",
  "isSidechain": true,
  "promptId": "00884a06-3250-4c87-b491-3b7baf3c5516",
  "agentId": "a6464752dec190ef4",
  "type": "user",
  "uuid": "9430bcdb-a179-4721-8c89-13a921effaf6",
  "sourceToolAssistantUUID": "42576876-71b3-474d-8ee3-46e54282c77f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-25T19:43:03.238Z_

Perfect! I now have the complete section (lines 250-491). Let me extract all numerical values systematically.

## Extracted Numerical Values from Lines 250-491

### Table 1: SFT Test-Set Evidence Tax (Lines 250-265)
**Location:** Table tab:test_tax (Lines 250-265)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 257 | 25.79 | Qwen3-1.7B With-evi (F1 %) | Table cell |
| 257 | 20.93 | Qwen3-1.7B No-evi (F1 %) | Table cell |
| 257 | -4.86 | Qwen3-1.7B Test Tax | Table cell |
| 257 | -5.63 | Qwen3-1.7B Dev Tax | Table cell |
| 258 | 22.32 | Qwen3-4B With-evi (F1 %) | Table cell |
| 258 | 22.19 | Qwen3-4B No-evi (F1 %) | Table cell |
| 258 | -0.13 | Qwen3-4B Test Tax | Table cell |
| 258 | +0.25 | Qwen3-4B Dev Tax | Table cell |
| 259 | 31.06 | Qwen3-8B With-evi (F1 %) | Table cell |
| 259 | 29.35 | Qwen3-8B No-evi (F1 %) | Table cell |
| 259 | -1.71 | Qwen3-8B Test Tax | Table cell |
| 259 | +0.04 | Qwen3-8B Dev Tax | Table cell |
| 260 | 38.86 | Qwen3-14B With-evi (F1 %) | Table cell |
| 260 | 38.54 | Qwen3-14B No-evi (F1 %) | Table cell |
| 260 | -0.32 | Qwen3-14B Test Tax | Table cell |
| 260 | +0.03 | Qwen3-14B Dev Tax | Table cell |
| 261 | 34.20 | LLaMA-3.1-8B With-evi (F1 %) | Table cell |
| 261 | 29.26 | LLaMA-3.1-8B No-evi (F1 %) | Table cell |
| 261 | -4.94 | LLaMA-3.1-8B Test Tax | Table cell |
| 261 | -5.19 | LLaMA-3.1-8B Dev Tax | Table cell |

### Body Text - RSFT Test Tax Analysis (Lines 267-268)
**Location:** Paragraph titled "RSFT test-set evidence tax" (body text, lines 267-268)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 268 | 5.01 ± 0.59 | Qwen3-1.7B RSFT tax with mean ± std (pp) | Body text statistic |
| 268 | 2 | Number of seeds (Qwen3-1.7B) | Body text |
| 268 | -4.86 | Qwen3-1.7B SFT tax reference | Body text |
| 268 | 1.65 ± 0.29 | Qwen3-4B RSFT tax, three-seed mean (pp) | Body text statistic |
| 268 | 3 | Number of seeds (Qwen3-4B) | Body text |
| 268 | 1.51 | Qwen3-4B RSFT tax s42 value (pp) | Body text |
| 268 | -0.13 | Qwen3-4B SFT tax | Body text |
| 268 | 0.91 ± 0.74 | Qwen3-8B RSFT tax, three-seed mean (pp) | Body text statistic |
| 268 | -1.71 | Qwen3-8B SFT tax | Body text |
| 268 | 0.12 ± 0.64 | Qwen3-14B three-seed mean test tax (pp) | Body text statistic |
| 268 | 0.77 | Qwen3-14B s42 tax | Body text |
| 268 | 0.08 | Qwen3-14B s43 tax | Body text |
| 268 | -0.50 | Qwen3-14B s44 tax | Body text |
| 268 | -1.53 ± 2.79 | Qwen3-14B dev tax, three-seed mean (pp) | Body text statistic |
| 268 | 2.82 | Annotation density ratio (test/dev) | Body text |
| 268 | -4.94 | LLaMA-3.1-8B SFT tax | Body text |
| 268 | -1.46 ± 0.40 | LLaMA-3.1-8B RSFT tax, two-seed mean (pp) | Body text statistic |
| 268 | 2 | Number of seeds (LLaMA) | Body text |

### Table 2: RSFT Inference-Time Evidence Tax (Lines 270-290)
**Location:** Table tab:rsft_test_tax (Lines 280-284)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 280 | 29.02 ± 0.45 | Qwen3-1.7B RSFT w/ evi (Ign-F1 %) ± std | Table cell |
| 280 | 2 | Superscript: seed count | Table cell |
| 280 | 24.00 ± 0.14 | Qwen3-1.7B RSFT no-evi ± std | Table cell |
| 280 | -5.01 ± 0.59 | Qwen3-1.7B RSFT Tax ± std | Table cell |
| 281 | 25.01 | Qwen3-4B RSFT w/ evi (Ign-F1 %) | Table cell |
| 281 | 26.52 | Qwen3-4B RSFT no-evi | Table cell |
| 281 | +1.51 | Qwen3-4B RSFT Tax | Table cell |
| 282 | 33.53 | Qwen3-8B RSFT w/ evi (Ign-F1 %) | Table cell |
| 282 | 33.19 | Qwen3-8B RSFT no-evi | Table cell |
| 282 | -0.34 | Qwen3-8B RSFT Tax | Table cell |
| 283 | 38.49 | Qwen3-14B RSFT w/ evi (Ign-F1 %) | Table cell |
| 283 | 39.26 | Qwen3-14B RSFT no-evi | Table cell |
| 283 | +0.77 | Qwen3-14B RSFT Tax (dagger notation) | Table cell |
| 284 | 35.54 | LLaMA-3.1-8B RSFT w/ evi (Ign-F1 %) | Table cell |
| 284 | 33.80 | LLaMA-3.1-8B RSFT no-evi | Table cell |
| 284 | -1.74 | LLaMA-3.1-8B RSFT Tax | Table cell |

### Footnote to Table 2 (Line 289)
**Location:** Table footnote (body text, line 289)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 289 | 2 | Two-seed mean reference | Footnote |
| 289 | -1.53 ± 2.79 | 14B dev tax, three-seed mean (pp) | Footnote |
| 289 | 0.12 ± 0.64 | 14B three-seed test mean (pp) | Footnote |

### Comparison to Supervised Methods - Body Text (Line 293)
**Location:** Paragraph body text (lines 292-293)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 293 | 63–65 | Rel-F1 range for encoder methods (%) | Body text |
| 293 | 46–60 | Rel-F1 range for our LLM approach (%) | Body text |
| 293 | 52–56 | Evi-F1 range for encoder methods (%) | Body text |
| 293 | 80 | Our TP-only Evi-F1 threshold (%) | Body text |
| 293 | 36.1 | Joint Evi-F1 for our method (%) | Body text |
| 293 | 54.15 | Encoder joint Evi-F1 (%) | Body text |
| 293 | 16–18 | Ign-F1 gap at 4B (pp) | Body text |
| 293 | 5 | Ign-F1 gap threshold at 14B (pp) | Body text |

### Table 3: Encoder Comparison (Lines 305-312)
**Location:** Table tab:encoder_comparison

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 305 | 61.32 | ATLOP Ign-F1 (%) | Table cell |
| 305 | 63.18 | ATLOP Rel-F1 (%) | Table cell |
| 306 | 62.34 | EIDER Ign-F1 (%) | Table cell |
| 306 | 64.27 | EIDER Rel-F1 (%) | Table cell |
| 306 | 52.54 | EIDER Evi-F1 (joint) (%) | Table cell |
| 307 | 62.23 | SAIS Ign-F1 (%) | Table cell |
| 307 | 65.17 | SAIS Rel-F1 (%) | Table cell |
| 307 | 55.84 | SAIS Evi-F1 (joint) (%) | Table cell |
| 308 | 61.71 | DREEAM Ign-F1 (%) | Table cell |
| 308 | 63.49 | DREEAM Rel-F1 (%) | Table cell |
| 308 | 54.15 | DREEAM Evi-F1 (joint) (%) | Table cell |
| 310 | 44.82 | Ours 4B RSFT Ign-F1 (%) | Table cell |
| 310 | 45.80 | Ours 4B RSFT Rel-F1 (%) | Table cell |
| 310 | 36.1 | Ours 4B RSFT Evi-F1 (joint) (%) | Table cell |
| 310 | 80.96 | Ours 4B RSFT Evi-F1 (TP) (%) | Table cell |
| 311 | 54.33 | Ours 8B RSFT Ign-F1 (%) | Table cell |
| 311 | 56.07 | Ours 8B RSFT Rel-F1 (%) | Table cell |
| 311 | 81.54 | Ours 8B RSFT Evi-F1 (TP) (%) | Table cell |
| 312 | 57.85 | Ours 14B RSFT Ign-F1 (%) | Table cell |
| 312 | 59.17 | Ours 14B RSFT Rel-F1 (%) | Table cell |
| 312 | 48.57 | Ours 14B RSFT Evi-F1 (joint) (%) | Table cell |
| 312 | 83.37 | Ours 14B RSFT Evi-F1 (TP) (%) | Table cell |

### Decoupling Spectrum Section - Body Text (Line 322)
**Location:** Body text (lines 319-322)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 322 | 4 | Qwen3-4B scale being evaluated | Body text |
| 322 | 76 | Number of relation types with ≥5 samples | Body text |

### Table 4: Decoupling Spectrum (Lines 334-340)
**Location:** Table tab:spectrum (lines 334-340)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 334 | 1.38 | GRPO QLoRA G=4 Rel-F1 (%) | Table cell |
| 334 | 85.04 | GRPO QLoRA G=4 Evi-F1 (%) | Table cell |
| 334 | 0.9876 | GRPO QLoRA G=4 EDCR | Table cell |
| 335 | 45.49 | GRPO bf16 G=8 Rel-F1 (%) | Table cell |
| 335 | 80.86 | GRPO bf16 G=8 Evi-F1 (%) | Table cell |
| 335 | 0.6318 | GRPO bf16 G=8 EDCR | Table cell |
| 336 | 33.37 | DPO bf16 1ep Rel-F1 (%) | Table cell |
| 336 | 80.90 | DPO bf16 1ep Evi-F1 (%) | Table cell |
| 336 | 0.8123 | DPO bf16 1ep EDCR | Table cell |
| 337 | 31.45 | DPO bf16 3ep Rel-F1 (%) | Table cell |
| 337 | 84.84 | DPO bf16 3ep Evi-F1 (%) | Table cell |
| 337 | 0.7503 | DPO bf16 3ep EDCR | Table cell |
| 339 | 44.39 | SFT baseline Rel-F1 (%) | Table cell |
| 339 | 79.61 | SFT baseline Evi-F1 (%) | Table cell |
| 339 | 0.6797 | SFT baseline EDCR | Table cell |
| 340 | 45.80 | RSFT CED Rel-F1 (%) | Table cell |
| 340 | 80.96 | RSFT CED Evi-F1 (%) | Table cell |
| 340 | 0.6487 | RSFT CED EDCR | Table cell |

### Footnote to Table 4 (Line 345)
**Location:** Table footnote (line 345)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 345 | 2048 | Token count for DPO (matched) | Footnote |
| 345 | 1024 | Token count for others | Footnote |

### GRPO Training Dynamics - Body Text (Line 352)
**Location:** Section body text (line 352)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 352 | 4 | GRPO G=4 QLoRA parameter | Body text |
| 352 | 8 | GRPO G=8 bf16 parameter | Body text |

### Figure Caption (Lines 356-358)
**Location:** Figure fig_grpo_dynamics caption (lines 356-358)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 357 | 10 | Training step where G=4 QLoRA collapses | Figure caption |
| 357 | 1.4 | Rel-F1 collapse value for G=4 QLoRA | Figure caption |

### Error Analysis - Body Text (Lines 365-375)
**Location:** Paragraph sections (lines 365-375)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 367 | 841 | Truncation FN reduction at 1.7B | Body text |
| 367 | 22 | Percentage truncation FN reduction at 1.7B (%) | Body text |
| 369 | 593 | Hallucinated FP reduction for LLaMA | Body text |
| 369 | 11.8 | Percentage hallucinated FP reduction (%) | Body text |
| 371 | 11–20 | Duplicate prediction reduction range (%) | Body text |
| 371 | 20.2 | Largest duplicate reduction at 1.7B (%) | Body text |
| 373 | 0.4 | Evidence exact-match F1 change threshold (pp) | Body text |
| 375 | 13–15 | Relative increase in "other" FN (%) | Body text |

### Table 5: Error Pattern Analysis (Lines 387-391)
**Location:** Table tab:error_analysis (lines 387-391)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 387 | 22 | Truncation FN change at 1.7B (%) | Table cell |
| 387 | 16 | Truncation FN change at 4B (%) | Table cell |
| 387 | 18 | Truncation FN change at 8B/LLaMA (%) | Table cell |
| 388 | 8 | Hallucinated FP change at 1.7B (%) | Table cell |
| 388 | 6 | Hallucinated FP change at 4B (%) | Table cell |
| 388 | 12 | Hallucinated FP change at 8B/LLaMA (%) | Table cell |
| 389 | 20 | Duplicate change at 1.7B (%) | Table cell |
| 389 | 11 | Duplicate change at 4B (%) | Table cell |
| 389 | 14 | Duplicate change at 8B/LLaMA (%) | Table cell |
| 390 | 0.4 | Evidence exact-match threshold (pp) | Table cell |
| 391 | 13 | FN: other change at 1.7B (%) | Table cell |
| 391 | 15 | FN: other change at 4B (%) | Table cell |
| 391 | 14 | FN: other change at 8B/LLaMA (%) | Table cell |

### Per-Relation EDCR Distribution - Body Text (Lines 401-408)
**Location:** Section body text (lines 401-408)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 401 | 76 | Relation types with ≥5 evaluation samples | Body text |
| 401 | -0.79 | Spearman correlation (EDCR vs Rel-F1) | Body text statistic |
| 401 | 76 | Sample count (n) | Body text |
| 401 | 0.001 | P-value significance threshold | Body text |
| 401 | 74 | Relation types with ≥5 predictions | Body text |
| 401 | -0.85 | Spearman correlation (filtered) | Body text statistic |
| 401 | -0.06 | EDCR vs Evi-F1 correlation | Body text statistic |
| 401 | 0.58 | P-value for EDCR-Evi-F1 correlation | Body text |
| 401 | -0.01 | Evi-F1 vs Rel-F1 correlation | Body text statistic |
| 401 | 0.91 | P-value for Evi-F1-Rel-F1 correlation | Body text |
| 401 | 0.118 | EDCR for date_of_birth | Body text |
| 401 | 0.956 | EDCR for head_of_government | Body text |
| 401 | 10000 | Permutation test iterations | Body text |
| 401 | 0.0001 | P-value threshold for permutation test | Body text |
| 404 | 17 | Cross-method configurations (n) | Body text |
| 404 | -0.8541 | Partial Spearman correlation (raw ρ) | Body text statistic |
| 404 | 0.000025 | P-value for partial correlation | Body text |
| 404 | -0.8554 | Raw Spearman correlation for comparison | Body text statistic |
| 404 | 0.15 | Percentage reduction from raw to partial (%) | Body text |
| 404 | 16 | Sample count after removing outlier | Body text |
| 404 | 0.000027 | P-value after removing outlier | Body text |
| 404 | 7 | Unique methods count | Body text |
| 404 | -0.9643 | Raw correlation at method level | Body text statistic |
| 404 | -0.9617 | Partial correlation at method level | Body text statistic |
| 407 | 5 | TP difference threshold (pp) | Body text |
| 407 | 5 | EDCR difference threshold (pp) | Body text |
| 407 | 48 | Number of similar-TP, different-EDCR pairs | Body text |
| 407 | 0.833 | DPO-CED Evi-Recall_TP | Body text |
| 407 | 0.829 | RSFT CED LLaMA s43 Evi-Recall_TP | Body text |
| 407 | 2.4 | TP-conditioned evidence recall difference (pp) | Body text |
| 407 | 13.6 | EDCR difference (pp) | Body text |

### Figure Caption (Lines 410-413)
**Location:** Figure fig_edcr_relations caption (lines 410-413)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 413 | 93 | Total relation types in development set | Figure caption |
| 413 | 96 | Defined relation types in DocRED | Figure caption |
| 413 | 76 | Relation types with ≥5 samples (for analysis) | Figure caption |
| 413 | 0.70 | EDCR threshold for severe decoupling | Figure caption |
| 413 | 0.30 | EDCR threshold for healthy grounding | Figure caption |
| 413 | 7 | Relation types with EDCR = 1.0 | Figure caption |

### Qualitative Analysis - Evidence Quality (Lines 422-423)
**Location:** Body text (lines 422-423)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 423 | 6 | SFT cited sentences for America's Sweetheart | Body text |
| 423 | 0.17 | SFT citation precision for America's Sweetheart | Body text |
| 423 | 1 | RSFT cited sentence for America's Sweetheart | Body text |
| 423 | 1.00 | RSFT citation precision for America's Sweetheart | Body text |
| 423 | 0.00–0.20 | SFT evidence precision range across examples | Body text |

### Table 6: Case Evidence (Lines 435-437)
**Location:** Table tab:case_evidence

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 435 | 0.00 | SFT Precision for Oleg Tinkov | Table cell |
| 435 | 1.00 | RSFT Precision for Oleg Tinkov | Table cell |
| 435 | 3 | SFT #Cited for Oleg Tinkov | Table cell |
| 436 | 0.17 | SFT Precision for America's Sweetheart | Table cell |
| 436 | 1.00 | RSFT Precision for America's Sweetheart | Table cell |
| 436 | 6 | SFT #Cited for America's Sweetheart | Table cell |
| 437 | 0.20 | SFT Precision for Jade (Mortal Kombat) | Table cell |
| 437 | 1.00 | RSFT Precision for Jade (Mortal Kombat) | Table cell |
| 437 | 5 | SFT #Cited for Jade (Mortal Kombat) | Table cell |

### Format Gaming Analysis - Body Text (Lines 443-444)
**Location:** Paragraph body text (lines 443-444)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 444 | 35 | Predicted triples for "Something to Believe In" | Body text |
| 444 | 0 | Correct matches for "Something to Believe In" | Body text |
| 444 | 28 | Predicted triples for "Józef Piłsudski Monument" | Body text |
| 444 | 0 | Correct matches for "Józef Piłsudski Monument" | Body text |

### EDCR Diagnostics - Body Text (Lines 446-447)
**Location:** Paragraph body text (lines 446-447)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 447 | 0.118 | EDCR for date_of_birth | Body text |
| 447 | 0.941 | EDCR for notable_work | Body text |

### Inference Efficiency Analysis - Body Text (Lines 450-476)
**Location:** Section body text (lines 450-476)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 453 | 4 | Batch size for inference | Body text |
| 453 | 2048 | max_new_tokens | Body text |
| 453 | 985 | Number of documents in DocRED dev | Body text |
| 453 | 1 | GPU count (RTX 5090) | Body text |
| 457 | 4 | Batch size for 1.7B–8B models | Body text |
| 457 | 1 | Batch size for 14B model | Body text |

### Table 7: Inference Efficiency (Lines 465-469)
**Location:** Table tab:inference_efficiency

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 465 | 6424 | Qwen3-1.7B With-evi inference time (seconds) | Table cell |
| 465 | 7438 | Qwen3-1.7B No-evi inference time (seconds) | Table cell |
| 465 | -13.6 | Qwen3-1.7B Overhead (%) | Table cell |
| 465 | 25.5 | Qwen3-1.7B Predictions with-evi (k) | Table cell |
| 465 | 44.6 | Qwen3-1.7B Predictions no-evi (k) | Table cell |
| 466 | 8887 | Qwen3-4B With-evi inference time (seconds) | Table cell |
| 466 | 7606 | Qwen3-4B No-evi inference time (seconds) | Table cell |
| 466 | 16.8 | Qwen3-4B Overhead (%) | Table cell |
| 466 | 24.7 | Qwen3-4B Predictions with-evi (k) | Table cell |
| 466 | 25.6 | Qwen3-4B Predictions no-evi (k) | Table cell |
| 467 | 10486 | Qwen3-8B With-evi inference time (seconds) | Table cell |
| 467 | 10901 | Qwen3-8B No-evi inference time (seconds) | Table cell |
| 467 | -3.8 | Qwen3-8B Overhead (%) | Table cell |
| 467 | 25.0 | Qwen3-8B Predictions with-evi (k) | Table cell |
| 467 | 31.1 | Qwen3-8B Predictions no-evi (k) | Table cell |
| 469 | 18011 | Qwen3-14B With-evi inference time (seconds) | Table cell |
| 469 | 14498 | Qwen3-14B No-evi inference time (seconds) | Table cell |
| 469 | 24.2 | Qwen3-14B Overhead (%) | Table cell |

### Inference Efficiency Analysis Continued - Body Text (Lines 474-476)
**Location:** Body text (lines 474-476)

| Line | Value | Represents | Type |
|------|-------|-----------|------|
| 474 | 13.6 | 1.7B inference time increase without evidence (%) | Body text |
| 474 | 1.75 | Prediction count multiplier (44.6k vs 25.5k) | Body text |
| 474 | 44.6 | Predictions without evidence at 1.7B (k) | Body text |
| 474 | 25.5 | Predictions with evidence at 1.7B (k) | Body text |
| 474 | 24.2 | 14B overhead when adding evidence (%) | Body text |
| 474 | 4.7 | Parameter multiplier (1.7B to 8B) | Body text |
| 474 | 1.63 | Wall-clock time increase (1.7B to 8B) | Body text |
| 475 | 2–3 | Slowdown factor for test vs dev inference (x) | Body text |
| 475 | 24–42 | Test inference time per document (s/doc, batch size 1) | Body text |
| 475 | 7–18 | Dev inference time per document (s/doc, batch size 4) | Body text |
| 476 | 2.82 | Annotation density ratio (test vs dev) | Body text |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9430bcdb-a179-4721-8c89-13a921effaf6",
  "isSidechain": true,
  "agentId": "a6464752dec190ef4",
  "requestId": "req_011CbPrgnDhFLcEwTqsUn72C",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d471cd0b-b8f4-4a7f-a15a-d2bde58a9c67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014bjXnAPX1Eu5pazoD4MpVu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8147,
      "cache_read_input_tokens": 39669,
      "output_tokens": 7843,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8147
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 7843,
          "cache_read_input_tokens": 39669,
          "cache_creation_input_tokens": 8147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8147,
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
