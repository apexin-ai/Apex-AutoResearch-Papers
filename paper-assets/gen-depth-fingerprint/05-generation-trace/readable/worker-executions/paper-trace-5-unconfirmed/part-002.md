# paper trace 5 unconfirmed — Part 2 of 2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../paper-trace-5-unconfirmed.md) · [Structured JSON](../../../sessions/82/828130237c596c935f3b.json)

## Round 1

### Tool call

_source line 158_

<details open><summary>🔧 Tool call — Read · `toolu_01GP4VFbpondY1TE2SQL7LxJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "727cbce6-9768-410b-9211-4635321ab6fe",
  "uuid": "5cf45449-06e7-4da1-8aa9-4a2c8227c194",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bgMbiTkQJqTFjYPwz9S4d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7489,
      "cache_read_input_tokens": 114294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7489
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

_source line 159 · 2026-05-23T19:44:00.696Z_

<details><summary>↩ Tool result · `toolu_01GP4VFbpondY1TE2SQL7LxJ`</summary>

```text
1	We analyze misclassification patterns in the binary LOGO task (gen-1 vs.\ gen-2+) across 29,095 test samples (overall error rate 28.1\%).
2	
3	\paragraph{Error asymmetry.}
4	The error distribution is highly asymmetric: 86.2\% of errors are false negatives (gen-2+ predicted as gen-1), while only 13.8\% are false positives (Table~\ref{tab:error-analysis}).
5	The classifier systematically under-predicts depth, consistent with the DDR pattern: shallow gen-2+ samples that have not yet accumulated sufficient distributional drift are indistinguishable from gen-1.
6	Among generators, Mistral-7B shows the highest error rate (45.0\%), while Pythia-1B is easiest (18.2\%), suggesting that larger models produce gen-2+ text closer to the gen-1 distribution.
7	
8	\begin{table}[H]
9	\centering
10	\small
11	\caption{Binary classification error analysis (gen-1 vs.\ gen-2+) under LOGO cross-validation. FP: gen-1 misclassified as gen-2+; FN: gen-2+ misclassified as gen-1. Errors are dominated by false negatives (86.2\%).}
12	\label{tab:error-analysis}
13	\begin{tabular}{lrrrr}
14	\toprule
15	\textbf{Generator} & $N$ & \textbf{FP} & \textbf{FN} & \textbf{Err.\%} \\
16	\midrule
17	Pythia-1B & 3560 & 188 & 460 & 18.2 \\
18	Pythia-2.8B & 3614 & 129 & 737 & 24.0 \\
19	OLMo-2-1B & 3718 & 154 & 900 & 28.3 \\
20	Qwen3-0.6B & 3542 & 234 & 511 & 21.0 \\
21	Qwen3-1.7B & 3621 & 175 & 639 & 22.5 \\
22	Qwen3-8B & 3502 & 93 & 1104 & 34.2 \\
23	Llama-3.2-3B & 3685 & 82 & 1030 & 30.2 \\
24	Mistral-7B & 3853 & 75 & 1659 & 45.0 \\
25	\midrule
26	\textbf{Overall} & 29095 & 1130 & 7040 & 28.1 \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
31	\paragraph{Per-depth error rates.}
32	Error rates decrease monotonically with depth (Table~\ref{tab:error-depth}): depth-2 samples are the primary failure point (48.4\% error rate), followed by depth-3 (29.2\%) and depth-4 (20.3\%).
33	The monotonic decrease confirms that deeper generations accumulate progressively stronger depth signatures; the gen-1$\to$gen-2 transition is the hardest boundary.
34	
35	\begin{table}[H]
36	\centering
37	\small
38	\caption{Error rate by generation depth in binary classification. Depth-2 exhibits the highest misclassification rate (48.4\%), confirming the gen-1$\to$gen-2 transition as the primary confusion boundary.}
39	\label{tab:error-depth}
40	\begin{tabular}{crrrl}
41	\toprule
42	\textbf{Depth} & $N$ & \textbf{Errors} & \textbf{Rate (\%)} & \textbf{Type} \\
43	\midrule
44	1 & 7896 & 1130 & 14.3 & FP \\
45	2 & 7512 & 3637 & 48.4 & FN \\
46	3 & 7032 & 2051 & 29.2 & FN \\
47	4 & 6655 & 1352 & 20.3 & FN \\
48	\bottomrule
49	\end{tabular}
50	\end{table}
51	
52	\paragraph{Feature-level explanation.}
53	Misclassified samples occupy the overlap zone between gen-1 and gen-2+ distributions (Table~\ref{tab:error-features}): they exhibit elevated entropy ($\bar{H}$: 2.26 vs.\ 1.57, $p<10^{-300}$) and lexical diversity (TTR: 0.464 vs.\ 0.302), retaining gen-1-like characteristics.
54	In contrast, shape features show no discriminating power: entropy max ($p = \text{n.s.}$) and tail decay ($p = \text{n.s.}$), consistent with the DDR pattern (\S\ref{sec:results-differential}).
55	
56	\begin{table}[H]
57	\centering
58	\small
59	\caption{Feature comparison between correctly and incorrectly classified samples. Misclassified samples show significantly higher entropy and lexical diversity but no difference in shape features.}
60	\label{tab:error-features}
61	\begin{tabular}{lcccl}
62	\toprule
63	\textbf{Feature} & \textbf{Correct} & \textbf{Incorrect} & $\Delta$ & $p$ \\
64	\midrule
65	$\bar{H}$ & 1.5700 & 2.2618 & +0.6918 & $<10^{-300}$ $^{***}$ \\
66	$\sigma_H$ & 1.6227 & 1.7413 & +0.1186 & $<10^{-300}$ $^{***}$ \\
67	$H_{\min}$ & 0.0281 & 0.0330 & +0.0049 & 1.0e-294 $^{***}$ \\
68	$H_{\max}$ & 7.5255 & 7.5251 & -0.0004 & n.s. \\
69	$\beta_{\mathrm{tail}}$ & -0.0023 & -0.0023 & +0.0000 & n.s. \\
70	TTR & 0.3024 & 0.4635 & +0.1612 & $<10^{-300}$ $^{***}$ \\
71	Hapax & 0.1760 & 0.3131 & +0.1371 & $<10^{-300}$ $^{***}$ \\
72	\bottomrule
73	\end{tabular}
74	\end{table}
75	
76	\paragraph{3-class confusion matrix.}
77	Table~\ref{tab:confusion-3class} shows the aggregated confusion matrix: gen-0 is near-perfectly classified ($>$99\%), while gen-1 and gen-2+ exhibit substantial cross-contamination (30.2\% of gen-2+ predicted as gen-1), consistent with the binary error analysis.
78	
79	\begin{table}[H]
80	\centering
81	\small
82	\caption{Aggregated 3-class confusion matrix (\%) across 8-fold LOGO. Gen-0 is near-perfectly classified, while gen-2+ is frequently confused with gen-1.}
83	\label{tab:confusion-3class}
84	\begin{tabular}{l|ccc}
85	\toprule
86	 & \multicolumn{3}{c}{\textbf{Predicted}} \\
87	\textbf{True} & gen-0 & gen-1 & gen-2+ \\
88	\midrule
89	gen-0 & 99.2 & 0.8 & 0.1 \\
90	gen-1 & 7.3 & 78.4 & 14.3 \\
91	gen-2+ & 3.0 & 30.2 & 66.7 \\
92	\bottomrule
93	\end{tabular}
94	\end{table}
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "727cbce6-9768-410b-9211-4635321ab6fe",
  "uuid": "88927ca1-e5bc-4519-a60e-bb31c60fa3be",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex",
      "content": "We analyze misclassification patterns in the binary LOGO task (gen-1 vs.\\ gen-2+) across 29,095 test samples (overall error rate 28.1\\%).\n\n\\paragraph{Error asymmetry.}\nThe error distribution is highly asymmetric: 86.2\\% of errors are false negatives (gen-2+ predicted as gen-1), while only 13.8\\% are false positives (Table~\\ref{tab:error-analysis}).\nThe classifier systematically under-predicts depth, consistent with the DDR pattern: shallow gen-2+ samples that have not yet accumulated sufficient distributional drift are indistinguishable from gen-1.\nAmong generators, Mistral-7B shows the highest error rate (45.0\\%), while Pythia-1B is easiest (18.2\\%), suggesting that larger models produce gen-2+ text closer to the gen-1 distribution.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{Binary classification error analysis (gen-1 vs.\\ gen-2+) under LOGO cross-validation. FP: gen-1 misclassified as gen-2+; FN: gen-2+ misclassified as gen-1. Errors are dominated by false negatives (86.2\\%).}\n\\label{tab:error-analysis}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Generator} & $N$ & \\textbf{FP} & \\textbf{FN} & \\textbf{Err.\\%} \\\\\n\\midrule\nPythia-1B & 3560 & 188 & 460 & 18.2 \\\\\nPythia-2.8B & 3614 & 129 & 737 & 24.0 \\\\\nOLMo-2-1B & 3718 & 154 & 900 & 28.3 \\\\\nQwen3-0.6B & 3542 & 234 & 511 & 21.0 \\\\\nQwen3-1.7B & 3621 & 175 & 639 & 22.5 \\\\\nQwen3-8B & 3502 & 93 & 1104 & 34.2 \\\\\nLlama-3.2-3B & 3685 & 82 & 1030 & 30.2 \\\\\nMistral-7B & 3853 & 75 & 1659 & 45.0 \\\\\n\\midrule\n\\textbf{Overall} & 29095 & 1130 & 7040 & 28.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Per-depth error rates.}\nError rates decrease monotonically with depth (Table~\\ref{tab:error-depth}): depth-2 samples are the primary failure point (48.4\\% error rate), followed by depth-3 (29.2\\%) and depth-4 (20.3\\%).\nThe monotonic decrease confirms that deeper generations accumulate progressively stronger depth signatures; the gen-1$\\to$gen-2 transition is the hardest boundary.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{Error rate by generation depth in binary classification. Depth-2 exhibits the highest misclassification rate (48.4\\%), confirming the gen-1$\\to$gen-2 transition as the primary confusion boundary.}\n\\label{tab:error-depth}\n\\begin{tabular}{crrrl}\n\\toprule\n\\textbf{Depth} & $N$ & \\textbf{Errors} & \\textbf{Rate (\\%)} & \\textbf{Type} \\\\\n\\midrule\n1 & 7896 & 1130 & 14.3 & FP \\\\\n2 & 7512 & 3637 & 48.4 & FN \\\\\n3 & 7032 & 2051 & 29.2 & FN \\\\\n4 & 6655 & 1352 & 20.3 & FN \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Feature-level explanation.}\nMisclassified samples occupy the overlap zone between gen-1 and gen-2+ distributions (Table~\\ref{tab:error-features}): they exhibit elevated entropy ($\\bar{H}$: 2.26 vs.\\ 1.57, $p<10^{-300}$) and lexical diversity (TTR: 0.464 vs.\\ 0.302), retaining gen-1-like characteristics.\nIn contrast, shape features show no discriminating power: entropy max ($p = \\text{n.s.}$) and tail decay ($p = \\text{n.s.}$), consistent with the DDR pattern (\\S\\ref{sec:results-differential}).\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{Feature comparison between correctly and incorrectly classified samples. Misclassified samples show significantly higher entropy and lexical diversity but no difference in shape features.}\n\\label{tab:error-features}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Feature} & \\textbf{Correct} & \\textbf{Incorrect} & $\\Delta$ & $p$ \\\\\n\\midrule\n$\\bar{H}$ & 1.5700 & 2.2618 & +0.6918 & $<10^{-300}$ $^{***}$ \\\\\n$\\sigma_H$ & 1.6227 & 1.7413 & +0.1186 & $<10^{-300}$ $^{***}$ \\\\\n$H_{\\min}$ & 0.0281 & 0.0330 & +0.0049 & 1.0e-294 $^{***}$ \\\\\n$H_{\\max}$ & 7.5255 & 7.5251 & -0.0004 & n.s. \\\\\n$\\beta_{\\mathrm{tail}}$ & -0.0023 & -0.0023 & +0.0000 & n.s. \\\\\nTTR & 0.3024 & 0.4635 & +0.1612 & $<10^{-300}$ $^{***}$ \\\\\nHapax & 0.1760 & 0.3131 & +0.1371 & $<10^{-300}$ $^{***}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{3-class confusion matrix.}\nTable~\\ref{tab:confusion-3class} shows the aggregated confusion matrix: gen-0 is near-perfectly classified ($>$99\\%), while gen-1 and gen-2+ exhibit substantial cross-contamination (30.2\\% of gen-2+ predicted as gen-1), consistent with the binary error analysis.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{Aggregated 3-class confusion matrix (\\%) across 8-fold LOGO. Gen-0 is near-perfectly classified, while gen-2+ is frequently confused with gen-1.}\n\\label{tab:confusion-3class}\n\\begin{tabular}{l|ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{Predicted}} \\\\\n\\textbf{True} & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\ngen-0 & 99.2 & 0.8 & 0.1 \\\\\ngen-1 & 7.3 & 78.4 & 14.3 \\\\\ngen-2+ & 3.0 & 30.2 & 66.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 95,
      "startLine": 1,
      "totalLines": 95
    }
  }
}
```

</details>

---


### Assistant

_source line 160_

<details><summary>Logged reasoning block</summary>

```text
The error_analysis appendix has no mention of "±3-4% batch estimation" or "prevalence estimation". The error analysis is purely about classification errors, not corpus-level prevalence estimation.

Now let me check if there's a separate downstream/prevalence appendix. Let me also read the conclusion and its reference more carefully.

The conclusion says: "corpus auditing (±3–4% batch estimation; Appendix~\ref{app:error-analysis})"

So the ±3-4% claim is attributed to Appendix error-analysis, but that appendix doesn't contain any prevalence estimation results! 

And the actual prevalence estimation results (from corpus_prevalence_demo.json) show:


- Best MAE = 9.45pp (not 3-4pp)
- Conclusion: "not viable"

Let me also check the appendix_downstream.tex which might contain the prevalence information. And I need to look at the ANOVA ratio calculation for item 5 in the cross_model_anova.csv file to see the effect sizes across different features.

Computing the ratios to verify the ">48×" requirement for depth versus generator effects: entropy_mean shows a 365× difference, ttr is 55×, and hapax_ratio is 51×—all well above the threshold. Now checking entropy_std to complete the analysis.

The entropy_std ratio comes out to only 9.18×, which falls short of the 48× claim. This reveals a tension: if the paper is making a general claim about depth explaining >48× more variance than generator identity across all features, entropy_std contradicts this since it has substantial depth effects but a much smaller ratio. The three strongest location features do meet the threshold individually, but entropy_std's significant depth effect (η² = 0.0826, p < 10^-70) makes it harder to justify excluding it from a blanket ">48×" statement. The exact calculations confirm hapax_ratio at roughly 51× and ttr at roughly 55×, making the minimum among those top three features around 51×. So the ">48×" claim holds up for these strongest features, though it's definitely misleading without that qualification. Now I should check what the appendix says about this.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "727cbce6-9768-410b-9211-4635321ab6fe",
  "uuid": "d11cf6a0-b20a-47eb-8183-cba2ba79490f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgGjFSJG2fxRKxokNCP2EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9506,
      "cache_read_input_tokens": 121783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9506
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

_source line 161_

<details open><summary>🔧 Tool call — Read · `toolu_01Qebv9F5ADdSnxcYwJWn1e1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "727cbce6-9768-410b-9211-4635321ab6fe",
  "uuid": "ebf7138f-9fd3-4265-829c-32b2e490a372",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgGjFSJG2fxRKxokNCP2EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9506,
      "cache_read_input_tokens": 121783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9506
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

_source line 162 · 2026-05-23T19:44:29.173Z_

<details><summary>↩ Tool result · `toolu_01Qebv9F5ADdSnxcYwJWn1e1`</summary>

```text
1	Can depth-aware data curation improve downstream language model quality?
2	We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\ref{tab:downstream}).
3	
4	\begin{table}[ht]
5	\centering
6	\small
7	\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}
8	\label{tab:downstream}
9	\begin{tabular}{lrc}
10	\toprule
11	\textbf{Variant} & \textbf{$n$} & \textbf{Test PPL} \\
12	\midrule
13	All depths            & 12{,}299 & 2.335 $\pm$ 0.000 \\
14	Size-matched (random) & 3{,}951  & 2.367 $\pm$ 0.000 \\
15	Depth 0--1 only       & 3{,}951  & 2.387 $\pm$ 0.001 \\
16	Binary-filtered       & 3{,}951  & 2.389 $\pm$ 0.000 \\
17	Depth 0 only          & 797      & 2.681 $\pm$ 0.001 \\
18	\bottomrule
19	\end{tabular}
20	\end{table}
21	
22	The results are unambiguous: data quantity dominates depth composition.
23	Training on all 12{,}299 samples yields the lowest perplexity (2.335).
24	At equal sample count ($n$\,=\,3{,}951), random subsampling (2.367) \emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).
25	Cross-seed variance is below 0.002 across all variants, which confirms the robustness of this null result.
26	
27	Restricting training to human-only text (depth 0, $n$\,=\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\times$ reduction in data volume rather than depth composition per se.
28	
29	\paragraph{Equivalence testing.}
30	We apply a two one-sided $t$-test (TOST) with a $\pm$2\% relative margin (equivalence bounds $\pm$0.047 on the ppl scale) to formally assess whether the depth-aware and random subsampling conditions produce practically indistinguishable perplexity.
31	At equal sample count ($n$\,=\,3{,}951): size-matched (random) ppl\,=\,2.367 vs.\ depth 0--1 ppl\,=\,2.387, $\Delta$\,=\,0.020.
32	TOST confirms equivalence ($p = 1.1 \times 10^{-4}$); the two curation strategies yield practically indistinguishable downstream quality within the $\pm$2\% margin.
33	Cross-seed standard deviation is below 0.001 for both variants.
34	
35	Comparing the full dataset ($n$\,=\,12{,}299, ppl\,=\,2.335) against the depth-filtered subset ($n$\,=\,3{,}951, ppl\,=\,2.387): TOST \emph{rejects} equivalence (minimum equivalence margin\,=\,0.053, exceeding the $\pm$2\% bound), which confirms that data quantity drives perplexity reduction beyond what depth-aware selection can recover.
36	
37	Knowing the generation depth of a document does not, by itself, make it more or less useful for training; at fixed sample count, depth-aware curation is statistically equivalent to uninformed random subsampling.
38	
39	\subsection*{Margin Sensitivity Analysis}
40	
41	To assess the robustness of the equivalence conclusion to margin choice, we repeat the TOST procedure across multiple equivalence margins \cite{lakens_equivalence}, following the recommendation to report sensitivity across plausible bounds rather than relying on a single threshold (Table~\ref{tab:tost-margins}).
42	
43	\begin{table}[ht]
44	\centering
45	\small
46	\caption{TOST equivalence testing across multiple margins. ``Equiv?'' indicates whether equivalence is established at $\alpha = 0.05$.}
47	\label{tab:tost-margins}
48	\resizebox{\linewidth}{!}{%
49	\begin{tabular}{llcc}
50	\toprule
51	\textbf{Comparison} & \textbf{Margin} & \textbf{Equiv?} & \textbf{TOST $p$} \\
52	\midrule
53	Full (12{,}299) vs.\ Random (3{,}951) & $\pm$1\% & No & 1.0 \\
54	                                        & $\pm$2\% & Yes & $1 \times 10^{-6}$ \\
55	                                        & $\pm$3\% & Yes & $< 10^{-10}$ \\
56	                                        & $\pm$5\% & Yes & $< 10^{-10}$ \\
57	\midrule
58	Full (12{,}299) vs.\ Depth 0--1 (3{,}951) & $\pm$1\% & No & 1.0 \\
59	                                            & $\pm$2\% & No & 1.0 \\
60	                                            & $\pm$3\% & Yes & $< 10^{-10}$ \\
61	                                            & $\pm$5\% & Yes & $< 10^{-10}$ \\
62	\bottomrule
63	\end{tabular}}
64	\end{table}
65	
66	The full dataset vs.\ random subsample comparison passes equivalence at the $\pm$2\% margin ($p = 10^{-6}$), while the full vs.\ depth 0--1 comparison requires a $\pm$3\% margin.
67	In absolute terms, perplexity differences are small: $\Delta$\,=\,0.032 (full vs.\ random, 1.4\% of baseline) and $\Delta$\,=\,0.052 (full vs.\ depth 0--1, 2.2\% of baseline).
68	
69	Cohen's $d$ values are 86.0 (full vs.\ random) and 119.7 (full vs.\ depth 0--1).
70	These appear large but are unreliable: with only $n$\,=\,3 seeds per condition, the pooled standard deviation is extremely small ($<$0.001), artificially inflating $d$.
71	The inflated effect sizes reflect low seed-level variance (confirming reproducibility) rather than practically meaningful perplexity differences.
72	The TOST framework with pre-specified relative margins provides a more appropriate assessment than Cohen's $d$ in this low-seed regime.
73	However, with only $n{=}3$ seeds per condition, the TOST results have limited generalizability: the test is valid given observed variance but the conclusion generalizes over only three random seeds. We characterize this as a preliminary observation rather than a definitive null result.
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "727cbce6-9768-410b-9211-4635321ab6fe",
  "uuid": "65ca96bd-bd27-4c96-acfc-d1e7c1115a2c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex",
      "content": "Can depth-aware data curation improve downstream language model quality?\nWe fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\\ref{tab:downstream}).\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}\n\\label{tab:downstream}\n\\begin{tabular}{lrc}\n\\toprule\n\\textbf{Variant} & \\textbf{$n$} & \\textbf{Test PPL} \\\\\n\\midrule\nAll depths            & 12{,}299 & 2.335 $\\pm$ 0.000 \\\\\nSize-matched (random) & 3{,}951  & 2.367 $\\pm$ 0.000 \\\\\nDepth 0--1 only       & 3{,}951  & 2.387 $\\pm$ 0.001 \\\\\nBinary-filtered       & 3{,}951  & 2.389 $\\pm$ 0.000 \\\\\nDepth 0 only          & 797      & 2.681 $\\pm$ 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe results are unambiguous: data quantity dominates depth composition.\nTraining on all 12{,}299 samples yields the lowest perplexity (2.335).\nAt equal sample count ($n$\\,=\\,3{,}951), random subsampling (2.367) \\emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).\nCross-seed variance is below 0.002 across all variants, which confirms the robustness of this null result.\n\nRestricting training to human-only text (depth 0, $n$\\,=\\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\\times$ reduction in data volume rather than depth composition per se.\n\n\\paragraph{Equivalence testing.}\nWe apply a two one-sided $t$-test (TOST) with a $\\pm$2\\% relative margin (equivalence bounds $\\pm$0.047 on the ppl scale) to formally assess whether the depth-aware and random subsampling conditions produce practically indistinguishable perplexity.\nAt equal sample count ($n$\\,=\\,3{,}951): size-matched (random) ppl\\,=\\,2.367 vs.\\ depth 0--1 ppl\\,=\\,2.387, $\\Delta$\\,=\\,0.020.\nTOST confirms equivalence ($p = 1.1 \\times 10^{-4}$); the two curation strategies yield practically indistinguishable downstream quality within the $\\pm$2\\% margin.\nCross-seed standard deviation is below 0.001 for both variants.\n\nComparing the full dataset ($n$\\,=\\,12{,}299, ppl\\,=\\,2.335) against the depth-filtered subset ($n$\\,=\\,3{,}951, ppl\\,=\\,2.387): TOST \\emph{rejects} equivalence (minimum equivalence margin\\,=\\,0.053, exceeding the $\\pm$2\\% bound), which confirms that data quantity drives perplexity reduction beyond what depth-aware selection can recover.\n\nKnowing the generation depth of a document does not, by itself, make it more or less useful for training; at fixed sample count, depth-aware curation is statistically equivalent to uninformed random subsampling.\n\n\\subsection*{Margin Sensitivity Analysis}\n\nTo assess the robustness of the equivalence conclusion to margin choice, we repeat the TOST procedure across multiple equivalence margins \\cite{lakens_equivalence}, following the recommendation to report sensitivity across plausible bounds rather than relying on a single threshold (Table~\\ref{tab:tost-margins}).\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{TOST equivalence testing across multiple margins. ``Equiv?'' indicates whether equivalence is established at $\\alpha = 0.05$.}\n\\label{tab:tost-margins}\n\\resizebox{\\linewidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Margin} & \\textbf{Equiv?} & \\textbf{TOST $p$} \\\\\n\\midrule\nFull (12{,}299) vs.\\ Random (3{,}951) & $\\pm$1\\% & No & 1.0 \\\\\n                                        & $\\pm$2\\% & Yes & $1 \\times 10^{-6}$ \\\\\n                                        & $\\pm$3\\% & Yes & $< 10^{-10}$ \\\\\n                                        & $\\pm$5\\% & Yes & $< 10^{-10}$ \\\\\n\\midrule\nFull (12{,}299) vs.\\ Depth 0--1 (3{,}951) & $\\pm$1\\% & No & 1.0 \\\\\n                                            & $\\pm$2\\% & No & 1.0 \\\\\n                                            & $\\pm$3\\% & Yes & $< 10^{-10}$ \\\\\n                                            & $\\pm$5\\% & Yes & $< 10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe full dataset vs.\\ random subsample comparison passes equivalence at the $\\pm$2\\% margin ($p = 10^{-6}$), while the full vs.\\ depth 0--1 comparison requires a $\\pm$3\\% margin.\nIn absolute terms, perplexity differences are small: $\\Delta$\\,=\\,0.032 (full vs.\\ random, 1.4\\% of baseline) and $\\Delta$\\,=\\,0.052 (full vs.\\ depth 0--1, 2.2\\% of baseline).\n\nCohen's $d$ values are 86.0 (full vs.\\ random) and 119.7 (full vs.\\ depth 0--1).\nThese appear large but are unreliable: with only $n$\\,=\\,3 seeds per condition, the pooled standard deviation is extremely small ($<$0.001), artificially inflating $d$.\nThe inflated effect sizes reflect low seed-level variance (confirming reproducibility) rather than practically meaningful perplexity differences.\nThe TOST framework with pre-specified relative margins provides a more appropriate assessment than Cohen's $d$ in this low-seed regime.\nHowever, with only $n{=}3$ seeds per condition, the TOST results have limited generalizability: the test is valid given observed variance but the conclusion generalizes over only three random seeds. We characterize this as a preliminary observation rather than a definitive null result.\n",
      "numLines": 74,
      "startLine": 1,
      "totalLines": 74
    }
  }
}
```

</details>

---


### Tool call

_source line 163_

<details open><summary>🔧 Tool call — Read · `toolu_01JLQKL18Cz9uptKtG3uSFFc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "727cbce6-9768-410b-9211-4635321ab6fe",
  "uuid": "ee5d0748-c637-4147-882c-60c06151e920",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgGjFSJG2fxRKxokNCP2EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9506,
      "cache_read_input_tokens": 121783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9506
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

_source line 164 · 2026-05-23T19:44:29.464Z_

<details><summary>↩ Tool result · `toolu_01JLQKL18Cz9uptKtG3uSFFc`</summary>

```text
1	\vspace{-4mm}
2	\section{Conclusion}
3	\label{sec:conclusion}
4	\vspace{-3mm}
5	
6	\looseness=-2 Recursive generation produces a decomposable depth response---location features drift while shape is approximately preserved---enabling cross-generator depth classification (F1\,=\,0.694--0.762) within the base-model scope.
7	Cross-model chains confirm generalization across architectures (F1\,=\,0.830; ANOVA: depth explains ${>}48{\times}$ more variance than generator identity).
8	QLoRA recovery (F1\,=\,0.89--0.91) suggests tractable extension to instruct models; DDR connects depth profiling to model collapse analysis and corpus auditing (${\pm}3$--$4$\% batch estimation; Appendix~\ref{app:error-analysis}).
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "727cbce6-9768-410b-9211-4635321ab6fe",
  "uuid": "c06f87bd-a386-4b9e-be82-c99e2b9f93c9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex",
      "content": "\\vspace{-4mm}\n\\section{Conclusion}\n\\label{sec:conclusion}\n\\vspace{-3mm}\n\n\\looseness=-2 Recursive generation produces a decomposable depth response---location features drift while shape is approximately preserved---enabling cross-generator depth classification (F1\\,=\\,0.694--0.762) within the base-model scope.\nCross-model chains confirm generalization across architectures (F1\\,=\\,0.830; ANOVA: depth explains ${>}48{\\times}$ more variance than generator identity).\nQLoRA recovery (F1\\,=\\,0.89--0.91) suggests tractable extension to instruct models; DDR connects depth profiling to model collapse analysis and corpus auditing (${\\pm}3$--$4$\\% batch estimation; Appendix~\\ref{app:error-analysis}).\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---


### Assistant

_source line 165_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me compile my complete report.

The conclusion says:
"corpus auditing (±3–4% batch estimation; Appendix~\ref{app:error-analysis})"

But Appendix error-analysis (which I just read) contains NO mention of batch estimation or prevalence estimation. The error analysis is purely about classification errors. And the actual prevalence estimation (corpus_prevalence_demo.json) shows:
- Best MAE = 9.45pp (not 3-4pp)
- Conclusion: "not viable"

So the ±3-4% claim is:
1. Not supported by the referenced appendix (error-analysis)


2. Directly contradicted by the actual prevalence estimation results, which show a much larger error of 9.45pp

Now I'm examining the ANOVA ratios from the cross-model analysis to see how much more variance depth explains compared to the generator across different linguistic features—the effect sizes are dramatically different, with entropy showing the largest disparity at over 365 times greater.

The minimum ratio among the three strongest features is hapax_ratio at 50.9×, which could support the ">48×" claim, but this only covers three features and ignores several others where the generator actually dominates or shows minimal depth effects. The paper's wording suggests a universal claim about depth explaining more variance, but the data shows this only holds for specific features.

Now I need to compile the full report and also verify the QLoRA details—the paper mentions 6-generator LOGO but the actual data shows 4 generators with 5-fold stratified cross-validation, so I'm checking the plan file to clarify what the actual experimental setup was. The XGBoost baseline shows a 3-class macro F1 of 0.7815 using LOGO evaluation, but it's also on 4 generators—not 6 as the paper claims. This means the comparison is fundamentally flawed: QLoRA achieved 0.905 using 5-fold stratified cross-validation on 4 generators, while the XGBoost baseline used LOGO on the same 4 generators, making these different evaluation protocols incomparable.

Looking at the paper's appendix, the 0.789 figure appears to come from either the 6-generator LOGO results or the LOFO ablation reference, while the 0.905 comes from the QLoRA plan012 experiment—but the generator counts and evaluation methods don't align between these sources. The 0.789 XGBoost value in the paper's appendix table actually comes from a 6-generator LOGO experiment, not from the matched 4-generator 5-fold CV protocol used for QLoRA, so the comparison isn't apples-to-apples. The properly matched XGBoost baseline under the same protocol shows 0.8048, which would make the actual delta only 10.04 percentage points, not the claimed 11.6. same 5-fold stratified CV, XGBoost achieves 0.805 — so the actual improvement is 10 percentage points, not 11.6. The problem is that the paper seems to be mixing results from different experimental setups: the 0.789 baseline comes from 6-generator LOGO while the 0.905 QLoRA result uses 4-generator 5-fold CV, making the comparison invalid. Let me look more carefully at what the paper actually claims in the appendix to understand if there's a consistent baseline being used throughout.

Actually, I'm noticing the QLoRA results are labeled as "6-generator LOGO" in the text, but the JSON data only shows 4 generators were available. This labeling seems inconsistent with what was actually evaluated. I have enough information now to write up my findings. The F1 score is accurate when rounded, but the methodology description is wrong—it should say 4-generator 5-fold stratified cross-validation instead of 6-generator LOGO. Plus, the comparison against XGBoost uses different experimental setups, making the 11.6 percentage point improvement misleading.

For the XGBoost baseline, the 0.789 F1 score checks out across multiple result files, and it does use the 6-generator LOGO setup as claimed.

Now I'm looking at the instruct LOGO binary F1 claim of 0.487—I can't find this exact value in any of the result files, and the closest approximation I can calculate from the instruct length confound data doesn't match either. Looking at the referenced appendix for the batch estimation claim, it only contains classification error analysis with no prevalence results. The actual prevalence experiment in the corpus_prevalence_demo file shows the best method achieved a mean absolute error of 9.45 percentage points, which contradicts the ±3-4% claim, and the experiment itself concluded the approach wasn't viable. For the variance ratio, I'm checking the cross-model ANOVA data where the entropy_mean shows a depth-to-generator ratio of about 365×.

Now examining the other metrics: type-token ratio gives 55.3×, hapax ratio yields 50.9×, entropy standard deviation is 9.18×, but entropy minimum actually flips with the generator explaining more variance, and tail decay is dominated by the generator as well. The paper's claim about depth explaining >48× more variance holds for some features but not universally across all metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "727cbce6-9768-410b-9211-4635321ab6fe",
  "uuid": "d4e266f0-b196-41c2-8ae2-bb7d8af82bb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JUERCezdUjp6gTM4MiQMw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3477,
      "cache_read_input_tokens": 131289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3477
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

_source line 166_

Now I have all the data needed for the complete report. Here's the synthesis:

---

## 逐项追溯报告

### 1. QLoRA F1=0.905 的实验协议

**源文件**: `results/plan012_qwen06b_results.json`
- `macro_f1_3class: 0.9052`
- `cv_type: "5-fold_stratified"`
- `generators: ["pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b"]` — **4 个 generator**
- `n_samples: 18423`

**论文描述** (appendix_qlora.tex:25): "QLoRA achieves 3-class LOGO F1=0.905 under **6-generator LOGO**"

**判定: 数值正确，协议描述错误**
- 实际是 **4-gen 5-fold stratified CV**，不是 "6-generator LOGO"
- 论文表格中 XGBoost baseline=0.789 来自不同实验 (`8gen_logo_results.json > baseline_6gen_3class_f1: 0.7893`，6-gen LOGO)
- 匹配协议的 XGBoost baseline (`plan012_xgboost_matched.json`) = **0.8048** (4-gen, 5-fold stratified)
- 实际 delta 应为 0.905−0.805 = **+10.0pp**，不是论文声称的 +11.6pp

**应改为**: "4-generator 5-fold stratified CV, F1=0.905, +10.0pp vs matched XGBoost baseline (0.805)"

---

### 2. XGBoost 3-class F1=0.789

**源文件**:
- `results/8gen_logo_results.json` → `baseline_6gen_3class_f1: 0.7893`
- `results/lofo_ablation_results.json` → `reference_f1: 0.789`
- `results/appendix_classifier.tex:17` 确认一致引用

**判定: 准确** ✓
- 0.7893 四舍五入到 0.789，6-gen LOGO 协议正确
- 6 generators: olmo-2-1b, pythia-1b, pythia-2.8b, qwen3-0.6b, qwen3-1.7b, qwen3-8b

---

### 3. Instruct LOGO binary F1=0.487

**论文描述** (appendix_instruct.tex:50): "Three-generator instruct LOGO yields binary F1=0.487"

**源文件: 未找到**

逐个文件排查，最接近的值:
| 文件 | 描述 | 值 |
|------|------|-----|
| `instruct_length_confound.json` | qwen3-0.6b-inst held-out binary | 0.5519 |
| `instruct_length_confound.json` | qwen3-1.7b-inst held-out binary | 0.5058 |
| `instruct_length_confound.json` | olmo-inst held-out binary | 0.3506 |
| 以上三者平均 | | **0.4694** |
| `review_p1c_olmo_instruct.json` | olmo-inst binary LOGO F1 | 0.4255 |
| `p1c_instruct_logo_f1.json` | qwen3-1.7b-inst binary F1 | 0.6582 |
| `8gen_finer_depth.json` | 5-class finer depth logo_avg | 0.4878 |

**判定: 来源不可追溯**
- 0.487 不出现在任何 JSON 结果文件中
- 三个 instruct generator 的 held-out binary F1 均值为 0.469（非 0.487）
- 可能是未保存的计算结果或笔误
- **需要复现或更正**

---

### 4. ±3-4% batch estimation

**论文描述** (conclusion.tex:8): "corpus auditing (±3–4% batch estimation; Appendix~\ref{app:error-analysis})"

**实际数据**:
- Appendix error-analysis (`appendix_error_analysis.tex`): **不包含任何 batch/prevalence estimation 内容**，仅分析分类错误模式
- 实际 prevalence estimation 实验: `results/corpus_prevalence_demo.json`
  - Best method: EMQ, **MAE = 9.45pp**
  - `conclusion: "not viable"`
  - 各比例点 EMQ 误差: 0%→2.3pp, 25%→8.9pp, 50%→11.7pp, 75%→13.2pp, 100%→11.2pp

**判定: 错误** ✗
1. 引用的 Appendix 不含相关实验
2. 实际实验结果 MAE=9.45pp，远超 3-4%
3. 实验自身结论为 "not viable"
4. **此声明必须删除或根据实际数据重写**

---

### 5. >48× 方差比

**源文件**: `data/cross-model-chains/cross_model_anova.csv` (两因素 ANOVA)

| Feature | η²_depth | η²_generator | 比值 |
|---------|----------|------------|------|
| entropy_mean | 0.2989 | 0.000818 | **365.4×** |
| ttr | 0.1921 | 0.003477 | **55.3×** |
| hapax_ratio | 0.1526 | 0.002996 | **50.9×** |
| entropy_std | 0.0826 | 0.008999 | **9.2×** |
| entropy_max | 0.00215 | 0.000476 | 4.5× |
| entropy_min | 0.00195 | 0.002936 | 0.66× |
| tail_decay | 0.000349 | 0.006508 | 0.054× |

**论文描述** (conclusion.tex:7): "ANOVA: depth explains >48× more variance than generator identity"（无特征限定）

**判定: 部分正确，措辞需限定**
- ">48×" 仅对 3 个最强 location 特征成立 (entropy_mean/ttr/hapax_ratio，最小 50.9×)
- entropy_std 仅 9.2×
- entropy_min 和 tail_decay 中 generator 方差反而大于 depth
- **应改为**: "for the three strongest location features, depth explains >48× more variance…" 或报告范围 "51–365×"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "727cbce6-9768-410b-9211-4635321ab6fe",
  "uuid": "28b0b797-c461-4e9b-800f-d7ace4dbdb17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JUERCezdUjp6gTM4MiQMw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3477,
      "cache_read_input_tokens": 131289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3477
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


### Task result

_source line 167_

Now I have all the data needed for the complete report. Here's the synthesis:

---

## 逐项追溯报告

### 1. QLoRA F1=0.905 的实验协议

**源文件**: `results/plan012_qwen06b_results.json`
- `macro_f1_3class: 0.9052`
- `cv_type: "5-fold_stratified"`
- `generators: ["pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b"]` — **4 个 generator**
- `n_samples: 18423`

**论文描述** (appendix_qlora.tex:25): "QLoRA achieves 3-class LOGO F1=0.905 under **6-generator LOGO**"

**判定: 数值正确，协议描述错误**
- 实际是 **4-gen 5-fold stratified CV**，不是 "6-generator LOGO"
- 论文表格中 XGBoost baseline=0.789 来自不同实验 (`8gen_logo_results.json > baseline_6gen_3class_f1: 0.7893`，6-gen LOGO)
- 匹配协议的 XGBoost baseline (`plan012_xgboost_matched.json`) = **0.8048** (4-gen, 5-fold stratified)
- 实际 delta 应为 0.905−0.805 = **+10.0pp**，不是论文声称的 +11.6pp

**应改为**: "4-generator 5-fold stratified CV, F1=0.905, +10.0pp vs matched XGBoost baseline (0.805)"

---

### 2. XGBoost 3-class F1=0.789

**源文件**:
- `results/8gen_logo_results.json` → `baseline_6gen_3class_f1: 0.7893`
- `results/lofo_ablation_results.json` → `reference_f1: 0.789`
- `results/appendix_classifier.tex:17` 确认一致引用

**判定: 准确** ✓
- 0.7893 四舍五入到 0.789，6-gen LOGO 协议正确
- 6 generators: olmo-2-1b, pythia-1b, pythia-2.8b, qwen3-0.6b, qwen3-1.7b, qwen3-8b

---

### 3. Instruct LOGO binary F1=0.487

**论文描述** (appendix_instruct.tex:50): "Three-generator instruct LOGO yields binary F1=0.487"

**源文件: 未找到**

逐个文件排查，最接近的值:
| 文件 | 描述 | 值 |
|------|------|-----|
| `instruct_length_confound.json` | qwen3-0.6b-inst held-out binary | 0.5519 |
| `instruct_length_confound.json` | qwen3-1.7b-inst held-out binary | 0.5058 |
| `instruct_length_confound.json` | olmo-inst held-out binary | 0.3506 |
| 以上三者平均 | | **0.4694** |
| `review_p1c_olmo_instruct.json` | olmo-inst binary LOGO F1 | 0.4255 |
| `p1c_instruct_logo_f1.json` | qwen3-1.7b-inst binary F1 | 0.6582 |
| `8gen_finer_depth.json` | 5-class finer depth logo_avg | 0.4878 |

**判定: 来源不可追溯**
- 0.487 不出现在任何 JSON 结果文件中
- 三个 instruct generator 的 held-out binary F1 均值为 0.469（非 0.487）
- 可能是未保存的计算结果或笔误
- **需要复现或更正**

---

### 4. ±3-4% batch estimation

**论文描述** (conclusion.tex:8): "corpus auditing (±3–4% batch estimation; Appendix~\ref{app:error-analysis})"

**实际数据**:
- Appendix error-analysis (`appendix_error_analysis.tex`): **不包含任何 batch/prevalence estimation 内容**，仅分析分类错误模式
- 实际 prevalence estimation 实验: `results/corpus_prevalence_demo.json`
  - Best method: EMQ, **MAE = 9.45pp**
  - `conclusion: "not viable"`
  - 各比例点 EMQ 误差: 0%→2.3pp, 25%→8.9pp, 50%→11.7pp, 75%→13.2pp, 100%→11.2pp

**判定: 错误** ✗
1. 引用的 Appendix 不含相关实验
2. 实际实验结果 MAE=9.45pp，远超 3-4%
3. 实验自身结论为 "not viable"
4. **此声明必须删除或根据实际数据重写**

---

### 5. >48× 方差比

**源文件**: `data/cross-model-chains/cross_model_anova.csv` (两因素 ANOVA)

| Feature | η²_depth | η²_generator | 比值 |
|---------|----------|------------|------|
| entropy_mean | 0.2989 | 0.000818 | **365.4×** |
| ttr | 0.1921 | 0.003477 | **55.3×** |
| hapax_ratio | 0.1526 | 0.002996 | **50.9×** |
| entropy_std | 0.0826 | 0.008999 | **9.2×** |
| entropy_max | 0.00215 | 0.000476 | 4.5× |
| entropy_min | 0.00195 | 0.002936 | 0.66× |
| tail_decay | 0.000349 | 0.006508 | 0.054× |

**论文描述** (conclusion.tex:7): "ANOVA: depth explains >48× more variance than generator identity"（无特征限定）

**判定: 部分正确，措辞需限定**
- ">48×" 仅对 3 个最强 location 特征成立 (entropy_mean/ttr/hapax_ratio，最小 50.9×)
- entropy_std 仅 9.2×
- entropy_min 和 tail_decay 中 generator 方差反而大于 depth
- **应改为**: "for the three strongest location features, depth explains >48× more variance…" 或报告范围 "51–365×"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 450421,
  "duration_api_ms": 448809,
  "num_turns": 57,
  "stop_reason": "end_turn",
  "session_id": "727cbce6-9768-410b-9211-4635321ab6fe",
  "total_cost_usd": 1.94731295,
  "usage": {
    "input_tokens": 18,
    "cache_creation_input_tokens": 122925,
    "cache_read_input_tokens": 1117224,
    "output_tokens": 21478,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 122925,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 5486,
        "cache_read_input_tokens": 131289,
        "cache_creation_input_tokens": 3477,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3477
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2591,
      "outputTokens": 3758,
      "cacheReadInputTokens": 70687,
      "cacheCreationInputTokens": 43944,
      "webSearchRequests": 0,
      "costUSD": 0.0833797,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 18,
      "outputTokens": 21478,
      "cacheReadInputTokens": 1117224,
      "cacheCreationInputTokens": 122925,
      "webSearchRequests": 0,
      "costUSD": 1.8639332499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "11b09a40-2d0f-48d0-993c-366d7a9e851e"
}
```

</details>

---
