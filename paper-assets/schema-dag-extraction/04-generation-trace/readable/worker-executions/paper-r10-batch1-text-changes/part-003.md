# paper r10 batch1 text changes — Part 3 of 3

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

[← Part 2](part-002.md) · [Transcript overview](../paper-r10-batch1-text-changes.md) · [Structured JSON](../../../sessions/b3/b34b875d7c925fcc2ca0.json)

## Before a recorded user message

### Tool result

_source line 195 · 2026-05-17T08:09:49.407Z_

<details><summary>↩ Tool result · `toolu_01SmbvuMWhYLt6jg7czsvnbq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "465ea5cb-046f-4073-b2f1-55842d596106",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "oldString": "the underlying signal---a cautionary note",
    "newString": "the underlying signal, a cautionary note",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Supplementary Material for: Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded association between count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set $\\pm 3$\\,pp as the smallest interaction that would materially alter practitioner decisions: a 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$), confirming that the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level (high-BCS batches contain high-frequency entity types that models extract more reliably) rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r < -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims---the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151]---well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, reflecting the 64/80 base rate).  We fit:\n\\[\n\\text{accuracy} = \\beta_0 + \\beta_{\\text{BCS}} \\cdot \\text{BCS} + \\beta_{\\text{origin}} \\cdot \\text{train\\_origin\\_ratio} + \\varepsilon\n\\]\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Additional Experimental Details}\n\\label{sec:appendix_additional_details}\n\n\\subsection{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\nTo quantify whether performance variability is driven by random batch composition or seed-dependent model inference noise, we decompose total variance into intra-seed (batch) and inter-seed components across three seeds (42, 123, 456), each evaluated on 25 random batches per count level.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition across count levels on FewRel. Batch SD is the root-mean intra-seed variance across 25 random type batches (averaged over 3 seeds). Seed SD is the standard deviation of the 3 per-seed means. Ratio = mean batch variance / seed variance. At count 80, only one batch composition exists (the full schema), so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n2 & 0.1782 & 0.0557 & 10.2 \\\\\n6 & 0.1233 & 0.0160 & 59.2 \\\\\n12 & 0.1063 & 0.0297 & 12.8 \\\\\n22 & 0.0954 & 0.0096 & 99.2 \\\\\n44 & 0.1214 & 0.0143 & 72.4 \\\\\n66 & 0.0016 & 0.0002 & 46.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on Few-NERD (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed standard deviation averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 66 (full schema), only one composition exists, so both components collapse to near-zero.}\n\\label{tab:variance_decomposition_ner}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ on FewRel (mean 125$\\times$, counts 4--64) and 10--99$\\times$ on Few-NERD (mean 51$\\times$, counts 2--44), confirming that random batch composition is the primary source of performance variability on both tasks, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ on FewRel at count 16, 10.2$\\times$ on Few-NERD at count 2) indicates batch composition contributes the majority of observed variance. At count 80 (FewRel) and count 66 (Few-NERD), the full schema admits only one batch composition, collapsing batch variance by construction.\n\n\\subsection{Per-Count-Level Statistics}\n\\label{sec:appendix_per_count_stats}\n\n[Placeholder: per-count-level detailed statistics to be added.]\n\n\\section{Full Results Tables}\n\\label{sec:appendix_full_results}\n\n\\subsection{Count Curve Raw Data (All Seeds)}\n\\label{sec:appendix_count_curve_raw}\n\n[Placeholder: full count-curve data across all seeds to be added.]\n\n\\subsection{BCS-Controlled Raw Data}\n\\label{sec:appendix_bcs_raw}\n\n[Placeholder: BCS-controlled raw data to be added.]\n\n\\bibliography{references}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 228,
        "oldLines": 7,
        "newStart": 228,
        "newLines": 7,
        "lines": [
          " We assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).",
          " ",
          " \\paragraph{RE (FewRel).}",
          "-Under the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.",
          "+Under the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.",
          " ",
          " \\paragraph{NER (Few-NERD).}",
          " The batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level (high-BCS batches contain high-frequency entity types that models extract more reliably) rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability dimension."
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

_source line 196_

Now supplementary.tex: confusability effect---the within-pool:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "d68cdc74-59f5-49e0-9e85-4faf5c9cc717",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019HNo5GhgVPxqgyvH4wjCBm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 527,
      "cache_read_input_tokens": 108396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 527
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

_source line 197_

<details open><summary>🔧 Tool call — Grep · `toolu_01CHzGvmTJcEVLDox983kcnV`</summary>

```json
{
  "pattern": "confusability effect---the",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "bf31b77c-406d-4a32-9554-ff50ad274b9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019HNo5GhgVPxqgyvH4wjCBm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 527,
      "cache_read_input_tokens": 108396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 527
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

_source line 198 · 2026-05-17T08:09:59.021Z_

<details><summary>↩ Tool result · `toolu_01CHzGvmTJcEVLDox983kcnV`</summary>

```text
342:In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "f05e794e-872c-4d09-802b-2bb598909f5a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "342:In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.",
    "numLines": 1
  }
}
```

</details>

---


### Tool call

_source line 199_

<details open><summary>🔧 Tool call — Edit · `toolu_0185Xii4qVzoxgrvdGQGDu62`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "old_string": "confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes",
  "new_string": "confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "b309fa73-f2a2-4b16-9d2b-dbf12d9735d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vivksy1qgKPhkK6iFGR558",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 108923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
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

_source line 200 · 2026-05-17T08:10:05.494Z_

<details><summary>↩ Tool result · `toolu_0185Xii4qVzoxgrvdGQGDu62`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "57893712-080e-42ac-af97-b1540fbcfbaa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "oldString": "confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes",
    "newString": "confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Supplementary Material for: Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded association between count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set $\\pm 3$\\,pp as the smallest interaction that would materially alter practitioner decisions: a 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$), confirming that the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level (high-BCS batches contain high-frequency entity types that models extract more reliably) rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r < -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims---the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151]---well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, reflecting the 64/80 base rate).  We fit:\n\\[\n\\text{accuracy} = \\beta_0 + \\beta_{\\text{BCS}} \\cdot \\text{BCS} + \\beta_{\\text{origin}} \\cdot \\text{train\\_origin\\_ratio} + \\varepsilon\n\\]\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Additional Experimental Details}\n\\label{sec:appendix_additional_details}\n\n\\subsection{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\nTo quantify whether performance variability is driven by random batch composition or seed-dependent model inference noise, we decompose total variance into intra-seed (batch) and inter-seed components across three seeds (42, 123, 456), each evaluated on 25 random batches per count level.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition across count levels on FewRel. Batch SD is the root-mean intra-seed variance across 25 random type batches (averaged over 3 seeds). Seed SD is the standard deviation of the 3 per-seed means. Ratio = mean batch variance / seed variance. At count 80, only one batch composition exists (the full schema), so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n2 & 0.1782 & 0.0557 & 10.2 \\\\\n6 & 0.1233 & 0.0160 & 59.2 \\\\\n12 & 0.1063 & 0.0297 & 12.8 \\\\\n22 & 0.0954 & 0.0096 & 99.2 \\\\\n44 & 0.1214 & 0.0143 & 72.4 \\\\\n66 & 0.0016 & 0.0002 & 46.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on Few-NERD (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed standard deviation averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 66 (full schema), only one composition exists, so both components collapse to near-zero.}\n\\label{tab:variance_decomposition_ner}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ on FewRel (mean 125$\\times$, counts 4--64) and 10--99$\\times$ on Few-NERD (mean 51$\\times$, counts 2--44), confirming that random batch composition is the primary source of performance variability on both tasks, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ on FewRel at count 16, 10.2$\\times$ on Few-NERD at count 2) indicates batch composition contributes the majority of observed variance. At count 80 (FewRel) and count 66 (Few-NERD), the full schema admits only one batch composition, collapsing batch variance by construction.\n\n\\subsection{Per-Count-Level Statistics}\n\\label{sec:appendix_per_count_stats}\n\n[Placeholder: per-count-level detailed statistics to be added.]\n\n\\section{Full Results Tables}\n\\label{sec:appendix_full_results}\n\n\\subsection{Count Curve Raw Data (All Seeds)}\n\\label{sec:appendix_count_curve_raw}\n\n[Placeholder: full count-curve data across all seeds to be added.]\n\n\\subsection{BCS-Controlled Raw Data}\n\\label{sec:appendix_bcs_raw}\n\n[Placeholder: BCS-controlled raw data to be added.]\n\n\\bibliography{references}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 339,
        "oldLines": 7,
        "newStart": 339,
        "newLines": 7,
        "lines": [
          " ",
          " The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).",
          " ",
          "-In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.",
          "+In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.",
          " ",
          " \\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}",
          " \\label{app:scs-ablation}"
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

_source line 201_

Now supplementary.tex: claims---the observed (aggregation sim):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "d4e158c6-acc5-4137-85f5-10ef65b412b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gy6jvgvtmLXEMastA2gd8f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 109194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 257
      },
      "output_tokens": 7,
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

_source line 202_

<details open><summary>🔧 Tool call — Grep · `toolu_01FS2P2oj8xBZ8K1oRgVSbk5`</summary>

```json
{
  "pattern": "our claims---the observed",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "9b225ac5-20d3-4191-82f3-afc6a48169ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gy6jvgvtmLXEMastA2gd8f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 109194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 257
      },
      "output_tokens": 7,
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

_source line 203 · 2026-05-17T08:10:10.674Z_

<details><summary>↩ Tool result · `toolu_01FS2P2oj8xBZ8K1oRgVSbk5`</summary>

```text
370:The following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims---the observed batch-level $R^2 = 0.218$ (\S\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "ef5d0975-49cb-4579-a444-0221f23fe2f1",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "370:The following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims---the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.",
    "numLines": 1
  }
}
```

</details>

---


### Tool call

_source line 204_

<details open><summary>🔧 Tool call — Edit · `toolu_01QDxRQmyK7dGSnK7Piy5Ff4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "old_string": "our claims---the observed batch-level $R^2 = 0.218$",
  "new_string": "our claims; the observed batch-level $R^2 = 0.218$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "0bbc24aa-2e7f-49e1-b1e4-52e43db16fe8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WaHaGTDDC7pyej6kr7x9Re",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 109451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 228
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

_source line 205 · 2026-05-17T08:10:13.814Z_

<details><summary>↩ Tool result · `toolu_01QDxRQmyK7dGSnK7Piy5Ff4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "6de83b36-6031-464f-a66b-d5e50cea6db3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "oldString": "our claims---the observed batch-level $R^2 = 0.218$",
    "newString": "our claims; the observed batch-level $R^2 = 0.218$",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Supplementary Material for: Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded association between count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set $\\pm 3$\\,pp as the smallest interaction that would materially alter practitioner decisions: a 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$), confirming that the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level (high-BCS batches contain high-frequency entity types that models extract more reliably) rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r < -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims---the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151]---well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, reflecting the 64/80 base rate).  We fit:\n\\[\n\\text{accuracy} = \\beta_0 + \\beta_{\\text{BCS}} \\cdot \\text{BCS} + \\beta_{\\text{origin}} \\cdot \\text{train\\_origin\\_ratio} + \\varepsilon\n\\]\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Additional Experimental Details}\n\\label{sec:appendix_additional_details}\n\n\\subsection{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\nTo quantify whether performance variability is driven by random batch composition or seed-dependent model inference noise, we decompose total variance into intra-seed (batch) and inter-seed components across three seeds (42, 123, 456), each evaluated on 25 random batches per count level.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition across count levels on FewRel. Batch SD is the root-mean intra-seed variance across 25 random type batches (averaged over 3 seeds). Seed SD is the standard deviation of the 3 per-seed means. Ratio = mean batch variance / seed variance. At count 80, only one batch composition exists (the full schema), so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n2 & 0.1782 & 0.0557 & 10.2 \\\\\n6 & 0.1233 & 0.0160 & 59.2 \\\\\n12 & 0.1063 & 0.0297 & 12.8 \\\\\n22 & 0.0954 & 0.0096 & 99.2 \\\\\n44 & 0.1214 & 0.0143 & 72.4 \\\\\n66 & 0.0016 & 0.0002 & 46.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on Few-NERD (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed standard deviation averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 66 (full schema), only one composition exists, so both components collapse to near-zero.}\n\\label{tab:variance_decomposition_ner}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ on FewRel (mean 125$\\times$, counts 4--64) and 10--99$\\times$ on Few-NERD (mean 51$\\times$, counts 2--44), confirming that random batch composition is the primary source of performance variability on both tasks, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ on FewRel at count 16, 10.2$\\times$ on Few-NERD at count 2) indicates batch composition contributes the majority of observed variance. At count 80 (FewRel) and count 66 (Few-NERD), the full schema admits only one batch composition, collapsing batch variance by construction.\n\n\\subsection{Per-Count-Level Statistics}\n\\label{sec:appendix_per_count_stats}\n\n[Placeholder: per-count-level detailed statistics to be added.]\n\n\\section{Full Results Tables}\n\\label{sec:appendix_full_results}\n\n\\subsection{Count Curve Raw Data (All Seeds)}\n\\label{sec:appendix_count_curve_raw}\n\n[Placeholder: full count-curve data across all seeds to be added.]\n\n\\subsection{BCS-Controlled Raw Data}\n\\label{sec:appendix_bcs_raw}\n\n[Placeholder: BCS-controlled raw data to be added.]\n\n\\bibliography{references}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 367,
        "oldLines": 7,
        "newStart": 367,
        "newLines": 7,
        "lines": [
          " \\section{Pair-to-Batch Aggregation Simulation}",
          " \\label{app:aggregation-sim}",
          " ",
          "-The following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims---the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.",
          "+The following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.",
          " ",
          " \\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.",
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

_source line 206_

Now supplementary.tex: unconditional baseline em-dash:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "7214542f-0370-455e-ac87-b0185d7a3cb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFv6HhSgbfzpoYwhDkJWAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 109679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 235
      },
      "output_tokens": 7,
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

_source line 207_

<details open><summary>🔧 Tool call — Grep · `toolu_01NKsFcoNV1N9HQbpzNvxhwn`</summary>

```json
{
  "pattern": "0.001--0.151\\]---well below",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "14956cf2-ef6a-4bc4-814d-eb26cc1191f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFv6HhSgbfzpoYwhDkJWAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 109679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 235
      },
      "output_tokens": 7,
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

_source line 208 · 2026-05-17T08:10:16.877Z_

<details><summary>↩ Tool result · `toolu_01NKsFcoNV1N9HQbpzNvxhwn`</summary>

```text
377:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "6ff74dfa-5cdd-4e3a-a056-8de947ed3b10",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "377:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---


### Tool call

_source line 209_

<details open><summary>🔧 Tool call — Edit · `toolu_011os3brLhuzcX71MptD3bjJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "old_string": "0.001--0.151]---well below",
  "new_string": "0.001--0.151], well below"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "5f327f1f-3abf-44b9-a1c2-f5abeae8baff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XbDy7yHSindQR4o4PZWMHe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 170,
      "cache_read_input_tokens": 109914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 170
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

_source line 210 · 2026-05-17T08:10:19.974Z_

<details><summary>↩ Tool result · `toolu_011os3brLhuzcX71MptD3bjJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "1066ad9b-f319-4da5-b13c-c834b6090fbe",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "oldString": "0.001--0.151]---well below",
    "newString": "0.001--0.151], well below",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Supplementary Material for: Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded association between count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set $\\pm 3$\\,pp as the smallest interaction that would materially alter practitioner decisions: a 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$), confirming that the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level (high-BCS batches contain high-frequency entity types that models extract more reliably) rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r < -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151]---well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, reflecting the 64/80 base rate).  We fit:\n\\[\n\\text{accuracy} = \\beta_0 + \\beta_{\\text{BCS}} \\cdot \\text{BCS} + \\beta_{\\text{origin}} \\cdot \\text{train\\_origin\\_ratio} + \\varepsilon\n\\]\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Additional Experimental Details}\n\\label{sec:appendix_additional_details}\n\n\\subsection{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\nTo quantify whether performance variability is driven by random batch composition or seed-dependent model inference noise, we decompose total variance into intra-seed (batch) and inter-seed components across three seeds (42, 123, 456), each evaluated on 25 random batches per count level.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition across count levels on FewRel. Batch SD is the root-mean intra-seed variance across 25 random type batches (averaged over 3 seeds). Seed SD is the standard deviation of the 3 per-seed means. Ratio = mean batch variance / seed variance. At count 80, only one batch composition exists (the full schema), so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n2 & 0.1782 & 0.0557 & 10.2 \\\\\n6 & 0.1233 & 0.0160 & 59.2 \\\\\n12 & 0.1063 & 0.0297 & 12.8 \\\\\n22 & 0.0954 & 0.0096 & 99.2 \\\\\n44 & 0.1214 & 0.0143 & 72.4 \\\\\n66 & 0.0016 & 0.0002 & 46.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on Few-NERD (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed standard deviation averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 66 (full schema), only one composition exists, so both components collapse to near-zero.}\n\\label{tab:variance_decomposition_ner}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ on FewRel (mean 125$\\times$, counts 4--64) and 10--99$\\times$ on Few-NERD (mean 51$\\times$, counts 2--44), confirming that random batch composition is the primary source of performance variability on both tasks, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ on FewRel at count 16, 10.2$\\times$ on Few-NERD at count 2) indicates batch composition contributes the majority of observed variance. At count 80 (FewRel) and count 66 (Few-NERD), the full schema admits only one batch composition, collapsing batch variance by construction.\n\n\\subsection{Per-Count-Level Statistics}\n\\label{sec:appendix_per_count_stats}\n\n[Placeholder: per-count-level detailed statistics to be added.]\n\n\\section{Full Results Tables}\n\\label{sec:appendix_full_results}\n\n\\subsection{Count Curve Raw Data (All Seeds)}\n\\label{sec:appendix_count_curve_raw}\n\n[Placeholder: full count-curve data across all seeds to be added.]\n\n\\subsection{BCS-Controlled Raw Data}\n\\label{sec:appendix_bcs_raw}\n\n[Placeholder: BCS-controlled raw data to be added.]\n\n\\bibliography{references}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 374,
        "oldLines": 7,
        "newStart": 374,
        "newLines": 7,
        "lines": [
          " \\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).",
          " ",
          " \\paragraph{Unconditional baseline.}",
          "-When the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151]---well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.",
          "+When the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.",
          " ",
          " \\section{Split-Origin Covariate Analysis}",
          " \\label{app:split-origin}"
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

_source line 211_

Now supplementary.tex cross-domain section (two-channel → two-dimensional, sole driver → sole predictor, em-dashes):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "6e36e0d7-4293-4648-92c4-014d9b4a5356",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fz9YzEULqaWuixbT3ZcLtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 110084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 218
      },
      "output_tokens": 6,
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

_source line 212_

<details open><summary>🔧 Tool call — Edit · `toolu_01Edz1ZeUYvucbuAEFdTJKAw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "old_string": "Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests",
  "new_string": "Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "9152a4e0-087d-4cfc-8d6b-3243031c2941",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fz9YzEULqaWuixbT3ZcLtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 110084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 218
      },
      "output_tokens": 6,
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

_source line 213 · 2026-05-17T08:10:27.128Z_

<details><summary>↩ Tool result · `toolu_01Edz1ZeUYvucbuAEFdTJKAw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "f3b5cce0-aba1-4b46-acc8-bbb23e1b02e3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "oldString": "Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests",
    "newString": "Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Supplementary Material for: Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded association between count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set $\\pm 3$\\,pp as the smallest interaction that would materially alter practitioner decisions: a 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$), confirming that the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level (high-BCS batches contain high-frequency entity types that models extract more reliably) rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r < -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, reflecting the 64/80 base rate).  We fit:\n\\[\n\\text{accuracy} = \\beta_0 + \\beta_{\\text{BCS}} \\cdot \\text{BCS} + \\beta_{\\text{origin}} \\cdot \\text{train\\_origin\\_ratio} + \\varepsilon\n\\]\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Additional Experimental Details}\n\\label{sec:appendix_additional_details}\n\n\\subsection{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\nTo quantify whether performance variability is driven by random batch composition or seed-dependent model inference noise, we decompose total variance into intra-seed (batch) and inter-seed components across three seeds (42, 123, 456), each evaluated on 25 random batches per count level.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition across count levels on FewRel. Batch SD is the root-mean intra-seed variance across 25 random type batches (averaged over 3 seeds). Seed SD is the standard deviation of the 3 per-seed means. Ratio = mean batch variance / seed variance. At count 80, only one batch composition exists (the full schema), so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n2 & 0.1782 & 0.0557 & 10.2 \\\\\n6 & 0.1233 & 0.0160 & 59.2 \\\\\n12 & 0.1063 & 0.0297 & 12.8 \\\\\n22 & 0.0954 & 0.0096 & 99.2 \\\\\n44 & 0.1214 & 0.0143 & 72.4 \\\\\n66 & 0.0016 & 0.0002 & 46.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on Few-NERD (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed standard deviation averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 66 (full schema), only one composition exists, so both components collapse to near-zero.}\n\\label{tab:variance_decomposition_ner}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ on FewRel (mean 125$\\times$, counts 4--64) and 10--99$\\times$ on Few-NERD (mean 51$\\times$, counts 2--44), confirming that random batch composition is the primary source of performance variability on both tasks, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ on FewRel at count 16, 10.2$\\times$ on Few-NERD at count 2) indicates batch composition contributes the majority of observed variance. At count 80 (FewRel) and count 66 (Few-NERD), the full schema admits only one batch composition, collapsing batch variance by construction.\n\n\\subsection{Per-Count-Level Statistics}\n\\label{sec:appendix_per_count_stats}\n\n[Placeholder: per-count-level detailed statistics to be added.]\n\n\\section{Full Results Tables}\n\\label{sec:appendix_full_results}\n\n\\subsection{Count Curve Raw Data (All Seeds)}\n\\label{sec:appendix_count_curve_raw}\n\n[Placeholder: full count-curve data across all seeds to be added.]\n\n\\subsection{BCS-Controlled Raw Data}\n\\label{sec:appendix_bcs_raw}\n\n[Placeholder: BCS-controlled raw data to be added.]\n\n\\bibliography{references}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 391,
        "oldLines": 7,
        "newStart": 391,
        "newLines": 7,
        "lines": [
          " \\section{Cross-Domain Connections}",
          " \\label{app:cross-domain}",
          " ",
          "-The schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.",
          "+The schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.",
          " ",
          " \\section{Additional Experimental Details}",
          " \\label{sec:appendix_additional_details}"
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

_source line 214_

Now supplementary.tex: "driven by random batch composition":

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "983ce5e2-a799-43b4-b354-a045cf4b1fe4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiWEVkzepArTHygBPKmUiL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 711,
      "cache_read_input_tokens": 110302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 711
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

_source line 215_

<details open><summary>🔧 Tool call — Edit · `toolu_01C9rRQ1hvUbDDS46vtqVv1H`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "old_string": "driven by random batch composition",
  "new_string": "attributable to random batch composition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "85e1408d-57c5-4a85-8d4c-7c02802a521f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiWEVkzepArTHygBPKmUiL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 711,
      "cache_read_input_tokens": 110302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 711
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

_source line 216 · 2026-05-17T08:10:38.445Z_

<details><summary>↩ Tool result · `toolu_01C9rRQ1hvUbDDS46vtqVv1H`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "9f5596a7-b764-430f-8ad7-dfb38218ddf5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "oldString": "driven by random batch composition",
    "newString": "attributable to random batch composition",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Supplementary Material for: Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded association between count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set $\\pm 3$\\,pp as the smallest interaction that would materially alter practitioner decisions: a 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$), confirming that the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level (high-BCS batches contain high-frequency entity types that models extract more reliably) rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r < -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, reflecting the 64/80 base rate).  We fit:\n\\[\n\\text{accuracy} = \\beta_0 + \\beta_{\\text{BCS}} \\cdot \\text{BCS} + \\beta_{\\text{origin}} \\cdot \\text{train\\_origin\\_ratio} + \\varepsilon\n\\]\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Additional Experimental Details}\n\\label{sec:appendix_additional_details}\n\n\\subsection{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\nTo quantify whether performance variability is driven by random batch composition or seed-dependent model inference noise, we decompose total variance into intra-seed (batch) and inter-seed components across three seeds (42, 123, 456), each evaluated on 25 random batches per count level.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition across count levels on FewRel. Batch SD is the root-mean intra-seed variance across 25 random type batches (averaged over 3 seeds). Seed SD is the standard deviation of the 3 per-seed means. Ratio = mean batch variance / seed variance. At count 80, only one batch composition exists (the full schema), so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n2 & 0.1782 & 0.0557 & 10.2 \\\\\n6 & 0.1233 & 0.0160 & 59.2 \\\\\n12 & 0.1063 & 0.0297 & 12.8 \\\\\n22 & 0.0954 & 0.0096 & 99.2 \\\\\n44 & 0.1214 & 0.0143 & 72.4 \\\\\n66 & 0.0016 & 0.0002 & 46.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on Few-NERD (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed standard deviation averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 66 (full schema), only one composition exists, so both components collapse to near-zero.}\n\\label{tab:variance_decomposition_ner}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ on FewRel (mean 125$\\times$, counts 4--64) and 10--99$\\times$ on Few-NERD (mean 51$\\times$, counts 2--44), confirming that random batch composition is the primary source of performance variability on both tasks, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ on FewRel at count 16, 10.2$\\times$ on Few-NERD at count 2) indicates batch composition contributes the majority of observed variance. At count 80 (FewRel) and count 66 (Few-NERD), the full schema admits only one batch composition, collapsing batch variance by construction.\n\n\\subsection{Per-Count-Level Statistics}\n\\label{sec:appendix_per_count_stats}\n\n[Placeholder: per-count-level detailed statistics to be added.]\n\n\\section{Full Results Tables}\n\\label{sec:appendix_full_results}\n\n\\subsection{Count Curve Raw Data (All Seeds)}\n\\label{sec:appendix_count_curve_raw}\n\n[Placeholder: full count-curve data across all seeds to be added.]\n\n\\subsection{BCS-Controlled Raw Data}\n\\label{sec:appendix_bcs_raw}\n\n[Placeholder: BCS-controlled raw data to be added.]\n\n\\bibliography{references}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 399,
        "oldLines": 7,
        "newStart": 399,
        "newLines": 7,
        "lines": [
          " \\subsection{Cross-Seed Variance Decomposition}",
          " \\label{app:variance-decomposition}",
          " ",
          "-To quantify whether performance variability is driven by random batch composition or seed-dependent model inference noise, we decompose total variance into intra-seed (batch) and inter-seed components across three seeds (42, 123, 456), each evaluated on 25 random batches per count level.",
          "+To quantify whether performance variability is attributable to random batch composition or seed-dependent model inference noise, we decompose total variance into intra-seed (batch) and inter-seed components across three seeds (42, 123, 456), each evaluated on 25 random batches per count level.",
          " ",
          " \\begin{table}[h]",
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

_source line 217_

Now P7: supplementary placeholders. I saw placeholders at lines 445-461:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "b5719e1b-fb55-4730-9bd4-7b40b6e337b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBhniMgHqXGfunXcytx2hr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 222,
      "cache_read_input_tokens": 111013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 222
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

_source line 218_

<details open><summary>🔧 Tool call — Read · `toolu_01PQiHwajDQ9TbF96J5Lhihg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "offset": 443,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "5e205d15-db53-472b-a230-645c23fe2a6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBhniMgHqXGfunXcytx2hr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 222,
      "cache_read_input_tokens": 111013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 222
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

_source line 219 · 2026-05-17T08:10:41.968Z_

<details><summary>↩ Tool result · `toolu_01PQiHwajDQ9TbF96J5Lhihg`</summary>

```text
443	Intra-batch variance dominates inter-seed variance by 5--474$\times$ on FewRel (mean 125$\times$, counts 4--64) and 10--99$\times$ on Few-NERD (mean 51$\times$, counts 2--44), confirming that random batch composition is the primary source of performance variability on both tasks, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\times$ on FewRel at count 16, 10.2$\times$ on Few-NERD at count 2) indicates batch composition contributes the majority of observed variance. At count 80 (FewRel) and count 66 (Few-NERD), the full schema admits only one batch composition, collapsing batch variance by construction.
444	
445	\subsection{Per-Count-Level Statistics}
446	\label{sec:appendix_per_count_stats}
447	
448	[Placeholder: per-count-level detailed statistics to be added.]
449	
450	\section{Full Results Tables}
451	\label{sec:appendix_full_results}
452	
453	\subsection{Count Curve Raw Data (All Seeds)}
454	\label{sec:appendix_count_curve_raw}
455	
456	[Placeholder: full count-curve data across all seeds to be added.]
457	
458	\subsection{BCS-Controlled Raw Data}
459	\label{sec:appendix_bcs_raw}
460	
461	[Placeholder: BCS-controlled raw data to be added.]
462	
463	\bibliography{references}
464	
465	\end{document}
466	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "d0d41843-7d07-4ed8-a484-f7feaad14c66",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
      "content": "Intra-batch variance dominates inter-seed variance by 5--474$\\times$ on FewRel (mean 125$\\times$, counts 4--64) and 10--99$\\times$ on Few-NERD (mean 51$\\times$, counts 2--44), confirming that random batch composition is the primary source of performance variability on both tasks, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ on FewRel at count 16, 10.2$\\times$ on Few-NERD at count 2) indicates batch composition contributes the majority of observed variance. At count 80 (FewRel) and count 66 (Few-NERD), the full schema admits only one batch composition, collapsing batch variance by construction.\n\n\\subsection{Per-Count-Level Statistics}\n\\label{sec:appendix_per_count_stats}\n\n[Placeholder: per-count-level detailed statistics to be added.]\n\n\\section{Full Results Tables}\n\\label{sec:appendix_full_results}\n\n\\subsection{Count Curve Raw Data (All Seeds)}\n\\label{sec:appendix_count_curve_raw}\n\n[Placeholder: full count-curve data across all seeds to be added.]\n\n\\subsection{BCS-Controlled Raw Data}\n\\label{sec:appendix_bcs_raw}\n\n[Placeholder: BCS-controlled raw data to be added.]\n\n\\bibliography{references}\n\n\\end{document}\n",
      "numLines": 24,
      "startLine": 443,
      "totalLines": 466
    }
  }
}
```

</details>

---


### Assistant

_source line 220_

Delete the placeholder sections. Let me also check if any of these labels are referenced:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "e4b8f0b1-7b82-4559-add8-0accdcead810",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BayzL94rQjTH2DnL1S8WeU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 111235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

_source line 221_

<details open><summary>🔧 Tool call — Grep · `toolu_01G3bx1juUa8RYgHwB5DagfY`</summary>

```json
{
  "pattern": "appendix_per_count_stats|appendix_full_results|appendix_count_curve_raw|appendix_bcs_raw",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "230b6c75-bc12-42cc-8a5d-0466d7895e42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BayzL94rQjTH2DnL1S8WeU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 111235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

_source line 222 · 2026-05-17T08:10:47.216Z_

<details><summary>↩ Tool result · `toolu_01G3bx1juUa8RYgHwB5DagfY`</summary>

```text
docs/paper/supplementary.tex:446:\label{sec:appendix_per_count_stats}
docs/paper/supplementary.tex:451:\label{sec:appendix_full_results}
docs/paper/supplementary.tex:454:\label{sec:appendix_count_curve_raw}
docs/paper/supplementary.tex:459:\label{sec:appendix_bcs_raw}
docs/paper/supplementary.aux:676:\newlabel{sec:appendix_per_count_stats}{{P.2}{8}{Per-Count-Level Statistics}{subsection.P.2}{}}
docs/paper/supplementary.aux:681:\newlabel{sec:appendix_full_results}{{Q}{8}{Full Results Tables}{appendix.Q}{}}
docs/paper/supplementary.aux:684:\newlabel{sec:appendix_count_curve_raw}{{Q.1}{8}{Count Curve Raw Data (All Seeds)}{subsection.Q.1}{}}
docs/paper/supplementary.aux:689:\newlabel{sec:appendix_bcs_raw}{{Q.2}{8}{BCS-Controlled Raw Data}{subsection.Q.2}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "e43e7bfa-3a13-448d-b307-fd99b32dbf0c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/supplementary.tex:446:\\label{sec:appendix_per_count_stats}\ndocs/paper/supplementary.tex:451:\\label{sec:appendix_full_results}\ndocs/paper/supplementary.tex:454:\\label{sec:appendix_count_curve_raw}\ndocs/paper/supplementary.tex:459:\\label{sec:appendix_bcs_raw}\ndocs/paper/supplementary.aux:676:\\newlabel{sec:appendix_per_count_stats}{{P.2}{8}{Per-Count-Level Statistics}{subsection.P.2}{}}\ndocs/paper/supplementary.aux:681:\\newlabel{sec:appendix_full_results}{{Q}{8}{Full Results Tables}{appendix.Q}{}}\ndocs/paper/supplementary.aux:684:\\newlabel{sec:appendix_count_curve_raw}{{Q.1}{8}{Count Curve Raw Data (All Seeds)}{subsection.Q.1}{}}\ndocs/paper/supplementary.aux:689:\\newlabel{sec:appendix_bcs_raw}{{Q.2}{8}{BCS-Controlled Raw Data}{subsection.Q.2}{}}",
    "numLines": 8
  }
}
```

</details>

---


### Assistant

_source line 223_

Labels only defined, never referenced. Safe to delete.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "6e44afc4-eb89-4f9f-b8eb-d264cb324aef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sWkuLWorFn2H8N1FQo6oE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 111821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 465
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

_source line 224_

<details open><summary>🔧 Tool call — Edit · `toolu_01Vbso4ZWLfZZD1ASYG91Jsw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "old_string": "\\subsection{Per-Count-Level Statistics}\n\\label{sec:appendix_per_count_stats}\n\n[Placeholder: per-count-level detailed statistics to be added.]\n\n\\section{Full Results Tables}\n\\label{sec:appendix_full_results}\n\n\\subsection{Count Curve Raw Data (All Seeds)}\n\\label{sec:appendix_count_curve_raw}\n\n[Placeholder: full count-curve data across all seeds to be added.]\n\n\\subsection{BCS-Controlled Raw Data}\n\\label{sec:appendix_bcs_raw}\n\n[Placeholder: BCS-controlled raw data to be added.]\n\n\\bibliography{references}",
  "new_string": "\\bibliography{references}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "28de767b-104f-4abb-b38a-28a128037fc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sWkuLWorFn2H8N1FQo6oE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 111821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 465
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

_source line 225 · 2026-05-17T08:10:51.708Z_

<details><summary>↩ Tool result · `toolu_01Vbso4ZWLfZZD1ASYG91Jsw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "97a19b88-a42c-4a42-a2c5-2314bc4086fa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "oldString": "\\subsection{Per-Count-Level Statistics}\n\\label{sec:appendix_per_count_stats}\n\n[Placeholder: per-count-level detailed statistics to be added.]\n\n\\section{Full Results Tables}\n\\label{sec:appendix_full_results}\n\n\\subsection{Count Curve Raw Data (All Seeds)}\n\\label{sec:appendix_count_curve_raw}\n\n[Placeholder: full count-curve data across all seeds to be added.]\n\n\\subsection{BCS-Controlled Raw Data}\n\\label{sec:appendix_bcs_raw}\n\n[Placeholder: BCS-controlled raw data to be added.]\n\n\\bibliography{references}",
    "newString": "\\bibliography{references}",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Supplementary Material for: Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded association between count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set $\\pm 3$\\,pp as the smallest interaction that would materially alter practitioner decisions: a 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$), confirming that the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level (high-BCS batches contain high-frequency entity types that models extract more reliably) rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r < -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, reflecting the 64/80 base rate).  We fit:\n\\[\n\\text{accuracy} = \\beta_0 + \\beta_{\\text{BCS}} \\cdot \\text{BCS} + \\beta_{\\text{origin}} \\cdot \\text{train\\_origin\\_ratio} + \\varepsilon\n\\]\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Additional Experimental Details}\n\\label{sec:appendix_additional_details}\n\n\\subsection{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\nTo quantify whether performance variability is attributable to random batch composition or seed-dependent model inference noise, we decompose total variance into intra-seed (batch) and inter-seed components across three seeds (42, 123, 456), each evaluated on 25 random batches per count level.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition across count levels on FewRel. Batch SD is the root-mean intra-seed variance across 25 random type batches (averaged over 3 seeds). Seed SD is the standard deviation of the 3 per-seed means. Ratio = mean batch variance / seed variance. At count 80, only one batch composition exists (the full schema), so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n2 & 0.1782 & 0.0557 & 10.2 \\\\\n6 & 0.1233 & 0.0160 & 59.2 \\\\\n12 & 0.1063 & 0.0297 & 12.8 \\\\\n22 & 0.0954 & 0.0096 & 99.2 \\\\\n44 & 0.1214 & 0.0143 & 72.4 \\\\\n66 & 0.0016 & 0.0002 & 46.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on Few-NERD (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed standard deviation averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 66 (full schema), only one composition exists, so both components collapse to near-zero.}\n\\label{tab:variance_decomposition_ner}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ on FewRel (mean 125$\\times$, counts 4--64) and 10--99$\\times$ on Few-NERD (mean 51$\\times$, counts 2--44), confirming that random batch composition is the primary source of performance variability on both tasks, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ on FewRel at count 16, 10.2$\\times$ on Few-NERD at count 2) indicates batch composition contributes the majority of observed variance. At count 80 (FewRel) and count 66 (Few-NERD), the full schema admits only one batch composition, collapsing batch variance by construction.\n\n\\subsection{Per-Count-Level Statistics}\n\\label{sec:appendix_per_count_stats}\n\n[Placeholder: per-count-level detailed statistics to be added.]\n\n\\section{Full Results Tables}\n\\label{sec:appendix_full_results}\n\n\\subsection{Count Curve Raw Data (All Seeds)}\n\\label{sec:appendix_count_curve_raw}\n\n[Placeholder: full count-curve data across all seeds to be added.]\n\n\\subsection{BCS-Controlled Raw Data}\n\\label{sec:appendix_bcs_raw}\n\n[Placeholder: BCS-controlled raw data to be added.]\n\n\\bibliography{references}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 442,
        "oldLines": 24,
        "newStart": 442,
        "newLines": 6,
        "lines": [
          " ",
          " Intra-batch variance dominates inter-seed variance by 5--474$\\times$ on FewRel (mean 125$\\times$, counts 4--64) and 10--99$\\times$ on Few-NERD (mean 51$\\times$, counts 2--44), confirming that random batch composition is the primary source of performance variability on both tasks, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ on FewRel at count 16, 10.2$\\times$ on Few-NERD at count 2) indicates batch composition contributes the majority of observed variance. At count 80 (FewRel) and count 66 (Few-NERD), the full schema admits only one batch composition, collapsing batch variance by construction.",
          " ",
          "-\\subsection{Per-Count-Level Statistics}",
          "-\\label{sec:appendix_per_count_stats}",
          "-",
          "-[Placeholder: per-count-level detailed statistics to be added.]",
          "-",
          "-\\section{Full Results Tables}",
          "-\\label{sec:appendix_full_results}",
          "-",
          "-\\subsection{Count Curve Raw Data (All Seeds)}",
          "-\\label{sec:appendix_count_curve_raw}",
          "-",
          "-[Placeholder: full count-curve data across all seeds to be added.]",
          "-",
          "-\\subsection{BCS-Controlled Raw Data}",
          "-\\label{sec:appendix_bcs_raw}",
          "-",
          "-[Placeholder: BCS-controlled raw data to be added.]",
          "-",
          " \\bibliography{references}",
          " ",
          " \\end{document}"
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

_source line 226_

Also check if main.tex has matching placeholders:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "ac4fdd5d-9c64-4934-a0e0-bac8e06e0b7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhE68tx7tFxTtjHn75N9PV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 369,
      "cache_read_input_tokens": 112286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 369
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

_source line 227_

<details open><summary>🔧 Tool call — Grep · `toolu_01N1CHnP2U13FjzbmtDh6bHX`</summary>

```json
{
  "pattern": "Placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "c376828d-30af-425f-b6a2-daf14fee99f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhE68tx7tFxTtjHn75N9PV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 369,
      "cache_read_input_tokens": 112286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 369
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

_source line 228 · 2026-05-17T08:10:55.351Z_

<details><summary>↩ Tool result · `toolu_01N1CHnP2U13FjzbmtDh6bHX`</summary>

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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "b4dbb89c-6d7a-40c2-8950-a55c3aaf2a29",
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

_source line 229_

Good, no placeholders in main.tex. Now let me update the todo list and run all the verification greps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "97bf0c54-bdc7-4a45-b614-1d461a12b75b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx7Z2SGqH1Znq26C5Dr6fe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 112655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 230_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01QSKztTMajDULtdDaFN5tGy`</summary>

```json
{
  "todos": [
    {
      "content": "P1A-P1E, P2-P5, P6, P7: All text modifications",
      "status": "completed",
      "activeForm": "Text modifications complete"
    },
    {
      "content": "Verification grep and compile",
      "status": "in_progress",
      "activeForm": "Running verification greps"
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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "178a9eeb-f438-41de-aa2c-2e7391d1894e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx7Z2SGqH1Znq26C5Dr6fe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 112655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 231 · 2026-05-17T08:11:00.260Z_

<details><summary>↩ Tool result · `toolu_01QSKztTMajDULtdDaFN5tGy`</summary>

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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "382e157c-d374-4c1f-902b-8e51bd912b3d",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "P1A: Replace driven/drive/driver across all files",
        "status": "in_progress",
        "activeForm": "Replacing driven/drive/driver"
      },
      {
        "content": "P1B: Replace channel/channels with dimension/dimensions",
        "status": "pending",
        "activeForm": "Replacing channel→dimension"
      },
      {
        "content": "P1C: Replace bounded interaction with bounded association",
        "status": "pending",
        "activeForm": "Replacing bounded interaction→association"
      },
      {
        "content": "P1D: Replace mechanism (5 places)",
        "status": "pending",
        "activeForm": "Replacing mechanism"
      },
      {
        "content": "P1E: Insert predictive framework statement in introduction",
        "status": "pending",
        "activeForm": "Inserting predictive framework statement"
      },
      {
        "content": "P2: Reframe Contribution #2",
        "status": "pending",
        "activeForm": "Reframing Contribution #2"
      },
      {
        "content": "P3: Abstract simplification (remove TOST details)",
        "status": "pending",
        "activeForm": "Simplifying abstract"
      },
      {
        "content": "P4: Compress contribution list",
        "status": "pending",
        "activeForm": "Compressing contribution list"
      },
      {
        "content": "P5: Add BCS qualifier to Contribution #3",
        "status": "pending",
        "activeForm": "Adding BCS qualifier"
      },
      {
        "content": "P6: Replace all prose em-dashes",
        "status": "pending",
        "activeForm": "Replacing em-dashes"
      },
      {
        "content": "P7: Clean up supplementary placeholders",
        "status": "pending",
        "activeForm": "Cleaning supplementary placeholders"
      },
      {
        "content": "Verification grep and compile",
        "status": "pending",
        "activeForm": "Running verification and compilation"
      }
    ],
    "newTodos": [
      {
        "content": "P1A-P1E, P2-P5, P6, P7: All text modifications",
        "status": "completed",
        "activeForm": "Text modifications complete"
      },
      {
        "content": "Verification grep and compile",
        "status": "in_progress",
        "activeForm": "Running verification greps"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 232_

Running all verification greps:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "01d56c7c-b494-4b45-a2e5-b8359360f2a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CycomkNo7t4N41sFPsZwzy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 193,
      "cache_read_input_tokens": 113118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 193
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

_source line 233_

<details open><summary>🔧 Tool call — Bash · `toolu_01GWfx8ZHg2B7c4jhMR1Tbmy`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -rn \"driven\\|drive\\b\" *.tex | grep -v \"schema-driven\" | grep -v \"does not drive\"",
  "description": "Check for remaining driven/drive instances"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "e95fd38d-5d4a-4f44-b742-f39a72c2caa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CycomkNo7t4N41sFPsZwzy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 193,
      "cache_read_input_tokens": 113118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 193
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

_source line 234 · 2026-05-17T08:11:03.883Z_

<details><summary>↩ Tool result · `toolu_01GWfx8ZHg2B7c4jhMR1Tbmy`</summary>

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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "85742f5f-8ba6-4912-8654-42abb575e58f",
  "tool_use_result": {
    "stdout": "",
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

_source line 235_

<details open><summary>🔧 Tool call — Bash · `toolu_01514rvk5sAb32y7BFwUiG6h`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -rn \"channels\\b\\|channel\\b\" *.tex | grep -v \"label{sec:multi_channel}\" | grep -v \"ref{sec:multi_channel}\"",
  "description": "Check for remaining channel/channels instances"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "1025fa50-6b47-4e9a-9511-829cd8fac84e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015hyhjHSVDS9UWWFUVuwE6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 165,
      "cache_read_input_tokens": 113311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 165
      },
      "output_tokens": 68,
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

_source line 236 · 2026-05-17T08:11:07.575Z_

<details><summary>↩ Tool result · `toolu_01514rvk5sAb32y7BFwUiG6h`</summary>

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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "fcdb3755-81c2-42eb-a435-4fd19a23091c",
  "tool_use_result": {
    "stdout": "",
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

_source line 237_

<details open><summary>🔧 Tool call — Bash · `toolu_01EHp3KLJC2mrVBx7TD84hwq`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -rn \"bounded interaction\" *.tex",
  "description": "Check for remaining bounded interaction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "a05ff526-12ae-4015-8d62-79c5ee9226d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJ5vraPvN1GY9jX9bvx2rx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 113476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 168
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

_source line 238 · 2026-05-17T08:11:10.395Z_

<details><summary>↩ Tool result · `toolu_01EHp3KLJC2mrVBx7TD84hwq`</summary>

```text
main.tex:187:To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\sim$ $\log_2$\,count $+$ BCS $+$ count$\times$BCS) across 69 batches from FewRel spanning five count levels ($k \in \{4, 8, 16, 32, 40\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\,pp). A TOST equivalence test with a $\pm 3$\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\text{TOST}} = 0.003$), supporting bounded interaction between count and confusability effects.
results.tex:87:These results establish two dimensions: \textbf{Dimension~1} (count predicts recall decline) and \textbf{Dimension~2} (confusability predicts type confusion), consistent with bounded association in RE but coupled in NER where type ambiguity and boundary ambiguity interact. The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \times 2$ factorial ($n = 54$) as a sensitivity check. TOST equivalence testing confirms bounded interaction (interaction = 0.47\,pp, $p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp; Appendix~\ref{sec:appendix_factorial}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "588f3750-a36a-415b-98db-4a9582067c41",
  "tool_use_result": {
    "stdout": "main.tex:187:To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded interaction between count and confusability effects.\nresults.tex:87:These results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion), consistent with bounded association in RE but coupled in NER where type ambiguity and boundary ambiguity interact. The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. TOST equivalence testing confirms bounded interaction (interaction = 0.47\\,pp, $p_{\\text{TOST}} = 0.003$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}).",
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

_source line 239_

<details><summary>Logged reasoning block</summary>

```text
There are 2 remaining "bounded interaction" instances:
1. main.tex:187 - in the factorial analysis section: "supporting bounded interaction between count and confusability effects"
2. results.tex:87 - "TOST equivalence testing confirms bounded interaction"

Both of these are in the context of reporting TOST results. They should be changed to "bounded association" per P1C.

Wait, let me re-read the instructions more carefully. P1C says:

"bounded interaction" — 替换为 "bounded association"（7 处 + 镜像）

And lists specific locations:
- abstract.tex:4


- introduction.tex:12
- introduction.tex:16
- discussion.tex:13
- results.tex:87 — "bounded interaction in RE" → "bounded association in RE" (两处都改)
- main.tex:44
- supplementary.tex:148

So results.tex:87 was supposed to change both "bounded interaction" instances. Let me check what's on that line now. The first one was changed ("consistent with bounded association in RE"), but the second one ("TOST equivalence testing confirms bounded interaction") was not because the instructions say "(这一行出现两次 "bounded interaction"，都改)". Let me fix these remaining instances.

And main.tex:187 is the factorial analysis section, which has "supporting bounded interaction between count and confusability effects". This mirrors supplementary.tex:148 which I already changed, so I need to update main.tex:187 as well.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "9fd48103-3ff9-4823-960b-b30fa34ba764",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W4iUjAqfVxQoFYAdfCyDpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 113644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 516
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

_source line 240_

Two remaining "bounded interaction" instances need fixing:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "92af0453-4b06-432b-b694-e68870a3b8f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W4iUjAqfVxQoFYAdfCyDpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 113644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 516
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

_source line 241_

<details open><summary>🔧 Tool call — Edit · `toolu_01Di9fNdr5gh6VMC4RKWCitP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "confirms bounded interaction (interaction = 0.47",
  "new_string": "confirms bounded association (interaction = 0.47"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "0744f72d-c6f3-4645-9b77-c64af885bc33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W4iUjAqfVxQoFYAdfCyDpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 113644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 516
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

_source line 242 · 2026-05-17T08:11:22.891Z_

<details><summary>↩ Tool result · `toolu_01Di9fNdr5gh6VMC4RKWCitP`</summary>

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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "6f4f2c20-a339-4f13-8f71-f1f2ee4ee159",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "confirms bounded interaction (interaction = 0.47",
    "newString": "confirms bounded association (interaction = 0.47",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\\pm 1$\\,SD across 3 seeds (42, 123, 456) $\\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\\%$\\to$38.7\\%, $-$56\\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty. The pattern replicates across three seeds (42, 123, 456; max $\\Delta = 10.7$\\,pp, within 1\\,SD); intra-batch variance exceeds inter-seed variance by ${>}$5$\\times$ at every count level (Appendix~\\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$, pooled across three seeds). Count curves (25 batches per level) establish trend direction with error bars; magnitude estimation relies on the higher-powered BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$)---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) is excluded as RE's per-instance format precludes direct comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]; both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}). Notably, the independent MiniLM embedding yields a \\emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\\ Qwen3 $r = 0.138$; Appendix), suggesting that shared-representation bias is conservative rather than inflationary.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Conditional pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ unconditional $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}; we note the conditioning inflates this estimate) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, consistent with a Monte Carlo simulation accounting for inter-pair correlation structure; see Appendix~\\ref{app:aggregation-sim} for the illustrative aggregation model).\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime, suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Dimension~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Dimension~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$), modestly attenuated from v1's extreme-batch gap but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}). The BCS--accuracy correlation holds across four structurally distinct prompt variants at count 32 (all $r < -0.47$; Appendix~\\ref{sec:appendix_prompt_variants}), confirming that the confusability effect is not an artifact of prompt design.\n\n\\subsection{Multi-Dimensional Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion), consistent with bounded association in RE but coupled in NER where type ambiguity and boundary ambiguity interact. The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. TOST equivalence testing confirms bounded interaction (interaction = 0.47\\,pp, $p_{\\text{TOST}} = 0.003$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}).\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality: high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 84,
        "oldLines": 7,
        "newStart": 84,
        "newLines": 7,
        "lines": [
          " ",
          " Error taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.",
          " ",
          "-These results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion), consistent with bounded association in RE but coupled in NER where type ambiguity and boundary ambiguity interact. The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. TOST equivalence testing confirms bounded interaction (interaction = 0.47\\,pp, $p_{\\text{TOST}} = 0.003$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}).",
          "+These results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion), consistent with bounded association in RE but coupled in NER where type ambiguity and boundary ambiguity interact. The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. TOST equivalence testing confirms bounded association (interaction = 0.47\\,pp, $p_{\\text{TOST}} = 0.003$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}).",
          " ",
          " \\subsection{Centrality Confound on Homogeneous Schemas}",
          " \\label{sec:centrality_confound}"
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

_source line 243_

<details open><summary>🔧 Tool call — Edit · `toolu_019KmJEK6V3Sqe5fX1UkG6vX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "supporting bounded interaction between count and confusability effects",
  "new_string": "supporting bounded association between count and confusability effects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "74e0dc4b-c4e7-40c0-9958-6e913a177b12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAt344iy8vWG6xRpu373z7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 114160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 244 · 2026-05-17T08:11:26.760Z_

<details><summary>↩ Tool result · `toolu_019KmJEK6V3Sqe5fX1UkG6vX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "e08ee63d-da2c-4c3f-a1e5-adfd2813e458",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "supporting bounded interaction between count and confusability effects",
    "newString": "supporting bounded association between count and confusability effects",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Factorial interaction tests.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded association ($p_{\\text{TOST}} = 0.003$ at $\\pm 3$\\,pp, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions. For Few-NERD, SCS is computed from the extraction model's own embeddings (Qwen3), creating a shared-representation dependency. MiniLM cross-check yields a conservative but directionally consistent estimate ($r = 0.172$ vs $r = 0.138$; confusion matrix correlation 0.894), suggesting the effect is not an artifact of shared representations.\n\n\\item \\textbf{NER evaluation metric.} Our exact-match NER evaluation conflates boundary errors (partial span overlap) with type errors (correct span, wrong label). Relaxed matching may yield different confusability effect sizes, as boundary ambiguity may correlate with schema complexity independently of type similarity.\n\n\\item \\textbf{RE format specificity.} RE's clean dimension separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally. BCS slope consistency across independent and within-pool conditions (permutation $p = 0.60$) provides a robustness check that is difficult to reconcile with non-uniform contamination, which would differentially affect specific type subsets. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$). Adding train-origin ratio as a covariate leaves the BCS partial effect unchanged ($p = 0.245$ for origin; Appendix~\\ref{app:split-origin}).\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} Following the argument that independent replications do not require family-wise correction \\citep{rothman-1990}, while acknowledging the opposing view \\citep{perneger-1998}, we treat each dataset as a separate test of the same hypothesis. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded interaction between count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set $\\pm 3$\\,pp as the smallest interaction that would materially alter practitioner decisions: a 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$), confirming that the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level (high-BCS batches contain high-frequency entity types that models extract more reliably) rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r < -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, reflecting the 64/80 base rate).  We fit:\n\\[\n\\text{accuracy} = \\beta_0 + \\beta_{\\text{BCS}} \\cdot \\text{BCS} + \\beta_{\\text{origin}} \\cdot \\text{train\\_origin\\_ratio} + \\varepsilon\n\\]\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$), confirming that random batch composition is the primary source of performance variability. At count 80, the full schema admits only one composition, leaving model inference noise as the sole variance source (seed SD = 0.88\\,pp).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 184,
        "oldLines": 7,
        "newStart": 184,
        "newLines": 7,
        "lines": [
          " \\section{Factorial Analysis and Separability Test}",
          " \\label{sec:appendix_factorial}",
          " ",
          "-To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded interaction between count and confusability effects.",
          "+To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded association between count and confusability effects.",
          " ",
          " A separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.",
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

_source line 245_

Check the supplementary mirror:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "789e51fb-f212-4797-b522-c8522797f164",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GyGraxAeMk7Q972ZVQNxuS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 215,
      "cache_read_input_tokens": 114752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 215
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

_source line 246_

<details open><summary>🔧 Tool call — Grep · `toolu_013miCGKTJu6mBoDAHTPepb9`</summary>

```json
{
  "pattern": "bounded interaction",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "4bae9f16-0fd2-4b64-98b0-0573a465127d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GyGraxAeMk7Q972ZVQNxuS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 215,
      "cache_read_input_tokens": 114752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 215
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

_source line 247 · 2026-05-17T08:11:29.469Z_

<details><summary>↩ Tool result · `toolu_013miCGKTJu6mBoDAHTPepb9`</summary>

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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "b020e873-e292-43f7-adf8-eb8acc49c839",
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

_source line 248_

Now check mechanism:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "60ee03b5-44ee-415e-a2ad-c51fd701a54c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQiWGhTRX1Qhpo1zdivYm4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 141,
      "cache_read_input_tokens": 114967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 141
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

_source line 249_

<details open><summary>🔧 Tool call — Bash · `toolu_017XgM38UnNX3WqWuoZ2BonK`</summary>

```json
{
  "command": "grep -rn \"\\bmechanism\\b\" *.tex | grep -v \"Causal mechanism\"",
  "description": "Check for remaining mechanism instances"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "5dea0ca7-6105-4074-8d61-3bf8a06172f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQiWGhTRX1Qhpo1zdivYm4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 141,
      "cache_read_input_tokens": 114967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 141
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

_source line 250 · 2026-05-17T08:11:36.159Z_

<details><summary>↩ Tool result · `toolu_017XgM38UnNX3WqWuoZ2BonK`</summary>

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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "d62bc0c2-623e-4f1a-abee-1cf645cf300f",
  "tool_use_result": {
    "stdout": "",
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


### Assistant

_source line 251_

Now the em-dash verification:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "c08df3d2-900d-4ba9-a7d2-8968f16db754",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYXgj1xuTiyAWfMmKrJ556",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 278,
      "cache_read_input_tokens": 115108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 278
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

_source line 252_

<details open><summary>🔧 Tool call — Bash · `toolu_01HfxtNkCtWASfVpmaGamFvt`</summary>

```json
{
  "command": "grep -n \"\\-\\-\\-\" *.tex | grep -v \"^.*&.*---\" | grep -v \"DEPRECATED\"",
  "description": "Check for remaining prose em-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "5ef28c51-2316-49ff-b6d8-f4b7c3d0c2e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYXgj1xuTiyAWfMmKrJ556",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 278,
      "cache_read_input_tokens": 115108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 278
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

_source line 253 · 2026-05-17T08:11:42.336Z_

<details><summary>↩ Tool result · `toolu_01HfxtNkCtWASfVpmaGamFvt`</summary>

```text
experimental_setup.tex:60:SCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\ref{tab:pairwise}). However, SCS is a partial proxy---context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\S\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.
experimental_setup.tex:76:\textbf{NER}: text-match F1---a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \emph{and} the type matches; partial spans count as incorrect. \textbf{RE}: accuracy---exact match of predicted relation label to gold. \textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.
introduction.tex:4:Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
related_work.tex:10:\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\cite{rastogi2020towards} and SGD-X~\cite{lee2022sgd} document performance degradation with schema linguistic variation. \citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \citet{volkanovska2024ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \citep{deng-2010-imagenet}, label confusion matrices improve text classification \citep{guo-2021-label-confusion}, and classification confusion captures semantic similarity \citep{zhou-2025-rethinking}. Hierarchical label sets reduce class confusion in zero-shot image classification \citep{novack-2023-chils}; enriched type descriptions improve zero-shot NER \citep{cocchieri-2025-zeroner}---both orthogonal to our confusability-aware batching.
related_work.tex:12:\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\%$) is consistent with standards for individual-difference predictors in behavioral research \citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \citep{lakens-2013-effect-size}.
results.tex:29:We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$)---and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
sdgd_negative.tex:21:Oracle routing routes each test instance to the batch containing its gold type, eliminating cross-type confusion within each batch. On FewRel 80-relation RE, oracle-routed decomposition achieves 0.802 accuracy versus 0.504 for the single-pass baseline---a gain of +29.8\,pp (Table~\ref{tab:batch_composition}). This is the strongest positive finding of the decomposition experiments: it demonstrates that type confusability is indeed a key predictor of degradation in RE, and that performance recovers substantially when confusable types are separated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "0d90fb68-fbac-4b85-bd3f-b9e942e535fa",
  "tool_use_result": {
    "stdout": "experimental_setup.tex:60:SCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}). However, SCS is a partial proxy---context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.\nexperimental_setup.tex:76:\\textbf{NER}: text-match F1---a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.\nintroduction.tex:4:Training-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\\footnote{Code and data will be released upon acceptance. Anonymous review materials: \\url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\\% with one relation to 49.5\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\nrelated_work.tex:10:\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \\citep{deng-2010-imagenet}, label confusion matrices improve text classification \\citep{guo-2021-label-confusion}, and classification confusion captures semantic similarity \\citep{zhou-2025-rethinking}. Hierarchical label sets reduce class confusion in zero-shot image classification \\citep{novack-2023-chils}; enriched type descriptions improve zero-shot NER \\citep{cocchieri-2025-zeroner}---both orthogonal to our confusability-aware batching.\nrelated_work.tex:12:\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}.\nresults.tex:29:We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$)---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\nsdgd_negative.tex:21:Oracle routing routes each test instance to the batch containing its gold type, eliminating cross-type confusion within each batch. On FewRel 80-relation RE, oracle-routed decomposition achieves 0.802 accuracy versus 0.504 for the single-pass baseline---a gain of +29.8\\,pp (Table~\\ref{tab:batch_composition}). This is the strongest positive finding of the decomposition experiments: it demonstrates that type confusability is indeed a key predictor of degradation in RE, and that performance recovers substantially when confusable types are separated.",
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

_source line 254_

<details><summary>Logged reasoning block</summary>

```text
I have several remaining em-dashes to fix:

1. **experimental_setup.tex:60** — "a partial proxy---context" → comma
2. **experimental_setup.tex:76** — "text-match F1---a prediction" and "accuracy---exact match" and "relaxed F1---any token overlap" → these are definition-style, use commas or colons
3. **introduction.tex:4** — "(document-level)---near or exceeding halving" → comma


4. **related_work.tex:10** — "NER \citep{cocchieri-2025-zeroner}---both orthogonal" → comma
5. **related_work.tex:12** — "formal definition---pairwise cosine similarity of type name embeddings---with" → parentheses
6. **results.tex:29** — I need to double-check this one since the text seems to cut off mid-sentence after I changed "confusion rate---the fraction..." to use parentheses instead.
7. **sdgd_negative.tex:21** — "baseline---a gain of" → comma

Let me apply these fixes now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "4d8f7bad-1971-4da4-b76d-4c0a2fb88524",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1NHuQwXqi9X9iSAL7a7dZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1471,
      "cache_read_input_tokens": 115386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1471
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

_source line 255_

Several more em-dashes to fix. Let me handle them:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "5e7ebc90-9eb5-4d57-9d0e-792129010ea0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1NHuQwXqi9X9iSAL7a7dZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1471,
      "cache_read_input_tokens": 115386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1471
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

_source line 256_

<details open><summary>🔧 Tool call — Edit · `toolu_01ERAzyuRYtXXtHdfS2Rda7H`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "a partial proxy---context, type frequency",
  "new_string": "a partial proxy; context, type frequency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "5cfc37a8-0ec0-4f49-9678-78fc611c10e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1NHuQwXqi9X9iSAL7a7dZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1471,
      "cache_read_input_tokens": 115386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1471
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

_source line 257 · 2026-05-17T08:11:54.060Z_

<details><summary>↩ Tool result · reported error · `toolu_01ERAzyuRYtXXtHdfS2Rda7H`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "1fcdcff9-62b1-4c25-a8e6-f7e36c667f0d",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---


### Tool call

_source line 258_

<details open><summary>🔧 Tool call — Read · `toolu_01Kd56HiuJiGJXkdoekhNuvF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "offset": 58,
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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "ee010c54-f13e-4b16-be0f-2474813ef484",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTA9KhFYmtuuif8e6imstP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 563,
      "cache_read_input_tokens": 116857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 563
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

_source line 259 · 2026-05-17T08:11:57.489Z_

<details><summary>↩ Tool result · `toolu_01Kd56HiuJiGJXkdoekhNuvF`</summary>

```text
58	\paragraph{SCS as a lightweight proxy.}
59	\label{sec:scs-validation}
60	SCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\ref{tab:pairwise}). However, SCS is a partial proxy---context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\S\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.
61	
62	\subsection{Experimental Design}
63	\label{sec:exp_design}
64	
65	We conduct two complementary experimental paradigms.
66	
67	\paragraph{Experiment 1: Count Curves.}
68	We vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \{1, 2, 6, 12, 22, 44, 64\} for Few-NERD, \{1, 4, 8, 16, 32, 64, 80\} for FewRel, \{1, 4, 8, 16, 32, 64, 96\} for DocRED, and \{1, 6, 12, 22, 44, 64\} for MAVEN.
69	
70	\paragraph{Experiment 2: BCS-Controlled.}
71	We fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\,\in\{6, 12\}$), FewRel (count$\,\in\{8, 16\}$, both 16-relation and 80-relation pools), and DocRED (count$\,\in\{16, 32\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\S\ref{sec:centrality_confound}).
72	
73	\subsection{Evaluation Metrics}
74	\label{sec:metrics}
75	
76	\textbf{NER}: text-match F1---a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \emph{and} the type matches; partial spans count as incorrect. \textbf{RE}: accuracy---exact match of predicted relation label to gold. \textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "a88c3028-ec8e-49ea-b655-c7e1fde8dd24",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
      "content": "\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}). However, SCS is a partial proxy---context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{1, 2, 6, 12, 22, 44, 64\\} for Few-NERD, \\{1, 4, 8, 16, 32, 64, 80\\} for FewRel, \\{1, 4, 8, 16, 32, 64, 96\\} for DocRED, and \\{1, 6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1---a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.\n",
      "numLines": 20,
      "startLine": 58,
      "totalLines": 83
    }
  }
}
```

</details>

---


### Tool call

_source line 260_

<details open><summary>🔧 Tool call — Edit · `toolu_01PiWCutqmLGQsZ2zdE1cF1M`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "a partial proxy---context, type frequency",
  "new_string": "a partial proxy; context, type frequency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "06746559-4a2e-43d5-badd-90e2b1bc31fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5kafRbZRbL3fdvFczk8Ku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 117420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 949
      },
      "output_tokens": 39,
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

_source line 261 · 2026-05-17T08:12:00.453Z_

<details><summary>↩ Tool result · `toolu_01PiWCutqmLGQsZ2zdE1cF1M`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "53207f29-7992-4415-a0dc-82caf9233664",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "oldString": "a partial proxy---context, type frequency",
    "newString": "a partial proxy; context, type frequency",
    "originalFile": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. Few-NERD uses Qwen3 embeddings because its 66 fine-grained types include same-category pairs (e.g., ``person-artist'' vs.\\ ``person-actor'') that MiniLM's 384-d space does not separate well; a cross-embedding check confirms directional consistency (MiniLM $r = 0.172$, Qwen3 $r = 0.138$; Appendix~\\ref{sec:appendix_bcs_sensitivity}). SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \\cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with known autoregressive anisotropy \\cite{ethayarajh-contextual-2019}.\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}). However, SCS is a partial proxy---context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{1, 2, 6, 12, 22, 44, 64\\} for Few-NERD, \\{1, 4, 8, 16, 32, 64, 80\\} for FewRel, \\{1, 4, 8, 16, 32, 64, 96\\} for DocRED, and \\{1, 6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1---a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single 96\\,GB GPU with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which eliminates model-level randomness; bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.\n",
    "structuredPatch": [
      {
        "oldStart": 57,
        "oldLines": 7,
        "newStart": 57,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{SCS as a lightweight proxy.}",
          " \\label{sec:scs-validation}",
          "-SCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}). However, SCS is a partial proxy---context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.",
          "+SCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}). However, SCS is a partial proxy; context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.",
          " ",
          " \\subsection{Experimental Design}",
          " \\label{sec:exp_design}"
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

_source line 262_

<details open><summary>🔧 Tool call — Edit · `toolu_0161cnDmkvTec54ZT2gfy6pT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "text-match F1---a prediction is correct",
  "new_string": "text-match F1, where a prediction is correct"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "add1765f-4f80-4f71-90a7-ce7797500b1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BT9uxipZiwxc74ocK5wtBc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 215,
      "cache_read_input_tokens": 118369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 215
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

_source line 263 · 2026-05-17T08:12:03.091Z_

<details><summary>↩ Tool result · `toolu_0161cnDmkvTec54ZT2gfy6pT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "b74e9c3e-2d3c-4225-baf0-0b837eb30bc1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "oldString": "text-match F1---a prediction is correct",
    "newString": "text-match F1, where a prediction is correct",
    "originalFile": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. Few-NERD uses Qwen3 embeddings because its 66 fine-grained types include same-category pairs (e.g., ``person-artist'' vs.\\ ``person-actor'') that MiniLM's 384-d space does not separate well; a cross-embedding check confirms directional consistency (MiniLM $r = 0.172$, Qwen3 $r = 0.138$; Appendix~\\ref{sec:appendix_bcs_sensitivity}). SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \\cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with known autoregressive anisotropy \\cite{ethayarajh-contextual-2019}.\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}). However, SCS is a partial proxy; context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{1, 2, 6, 12, 22, 44, 64\\} for Few-NERD, \\{1, 4, 8, 16, 32, 64, 80\\} for FewRel, \\{1, 4, 8, 16, 32, 64, 96\\} for DocRED, and \\{1, 6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1---a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single 96\\,GB GPU with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which eliminates model-level randomness; bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.\n",
    "structuredPatch": [
      {
        "oldStart": 73,
        "oldLines": 7,
        "newStart": 73,
        "newLines": 7,
        "lines": [
          " \\subsection{Evaluation Metrics}",
          " \\label{sec:metrics}",
          " ",
          "-\\textbf{NER}: text-match F1---a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.",
          "+\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.",
          " ",
          " ",
          " \\subsection{Model and Inference}"
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

_source line 264_

<details open><summary>🔧 Tool call — Edit · `toolu_015Ua68kRXPKGVFHvvh79cNH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "accuracy---exact match",
  "new_string": "accuracy (exact match"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "d249f98f-036c-4af7-8373-fd128d6727b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019th6eQnvJ63Hw4Hm395yeN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 220,
      "cache_read_input_tokens": 118584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 220
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

_source line 265 · 2026-05-17T08:12:05.877Z_

<details><summary>↩ Tool result · `toolu_015Ua68kRXPKGVFHvvh79cNH`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "2c09d51c-970d-4bcf-ac6b-72743c0cc73c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "oldString": "accuracy---exact match",
    "newString": "accuracy (exact match",
    "originalFile": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. Few-NERD uses Qwen3 embeddings because its 66 fine-grained types include same-category pairs (e.g., ``person-artist'' vs.\\ ``person-actor'') that MiniLM's 384-d space does not separate well; a cross-embedding check confirms directional consistency (MiniLM $r = 0.172$, Qwen3 $r = 0.138$; Appendix~\\ref{sec:appendix_bcs_sensitivity}). SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \\cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with known autoregressive anisotropy \\cite{ethayarajh-contextual-2019}.\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}). However, SCS is a partial proxy; context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{1, 2, 6, 12, 22, 44, 64\\} for Few-NERD, \\{1, 4, 8, 16, 32, 64, 80\\} for FewRel, \\{1, 4, 8, 16, 32, 64, 96\\} for DocRED, and \\{1, 6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single 96\\,GB GPU with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which eliminates model-level randomness; bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.\n",
    "structuredPatch": [
      {
        "oldStart": 73,
        "oldLines": 7,
        "newStart": 73,
        "newLines": 7,
        "lines": [
          " \\subsection{Evaluation Metrics}",
          " \\label{sec:metrics}",
          " ",
          "-\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.",
          "+\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.",
          " ",
          " ",
          " \\subsection{Model and Inference}"
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

_source line 266_

<details open><summary>🔧 Tool call — Read · `toolu_01KKh94XoqHqSXrniNtqyY81`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "offset": 75,
  "limit": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "fe7a16fd-2280-447e-b718-681c17b11564",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmEKasvj5uaA2MYxufJLXQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 207,
      "cache_read_input_tokens": 118804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 207
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


### Tool result

_source line 267 · 2026-05-17T08:12:08.501Z_

<details><summary>↩ Tool result · `toolu_01KKh94XoqHqSXrniNtqyY81`</summary>

```text
75	
76	\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \emph{and} the type matches; partial spans count as incorrect. \textbf{RE}: accuracy (exact match of predicted relation label to gold. \textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "be53e76b-649c-400e-82a8-df046a8cfe63",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
      "content": "\n\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.",
      "numLines": 2,
      "startLine": 75,
      "totalLines": 83
    }
  }
}
```

</details>

---


### Assistant

_source line 268_

I need to close the parenthesis and fix the last em-dash:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "5cef5953-d1ad-43ce-9b3d-847339d4a8a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaFGbLXQsbRWXr57fCQLV2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 119011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 235
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

_source line 269_

<details open><summary>🔧 Tool call — Edit · `toolu_01P17TaTU69vrDCQ8vFEcXkN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "accuracy (exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap",
  "new_string": "accuracy (exact match of predicted relation label to gold). \\textbf{ED}: relaxed F1, where any token overlap"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "03d3c095-1d64-45f6-89f3-955652a7093b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaFGbLXQsbRWXr57fCQLV2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 119011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 235
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

_source line 270 · 2026-05-17T08:12:12.060Z_

<details><summary>↩ Tool result · `toolu_01P17TaTU69vrDCQ8vFEcXkN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "fd07cbd1-efb7-434c-b31d-65c79d688036",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "oldString": "accuracy (exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap",
    "newString": "accuracy (exact match of predicted relation label to gold). \\textbf{ED}: relaxed F1, where any token overlap",
    "originalFile": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. Few-NERD uses Qwen3 embeddings because its 66 fine-grained types include same-category pairs (e.g., ``person-artist'' vs.\\ ``person-actor'') that MiniLM's 384-d space does not separate well; a cross-embedding check confirms directional consistency (MiniLM $r = 0.172$, Qwen3 $r = 0.138$; Appendix~\\ref{sec:appendix_bcs_sensitivity}). SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \\cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with known autoregressive anisotropy \\cite{ethayarajh-contextual-2019}.\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}). However, SCS is a partial proxy; context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{1, 2, 6, 12, 22, 44, 64\\} for Few-NERD, \\{1, 4, 8, 16, 32, 64, 80\\} for FewRel, \\{1, 4, 8, 16, 32, 64, 96\\} for DocRED, and \\{1, 6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single 96\\,GB GPU with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which eliminates model-level randomness; bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.\n",
    "structuredPatch": [
      {
        "oldStart": 73,
        "oldLines": 7,
        "newStart": 73,
        "newLines": 7,
        "lines": [
          " \\subsection{Evaluation Metrics}",
          " \\label{sec:metrics}",
          " ",
          "-\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.",
          "+\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold). \\textbf{ED}: relaxed F1, where any token overlap between predicted and gold trigger spans, with correct event type.",
          " ",
          " ",
          " \\subsection{Model and Inference}"
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

_source line 271_

Now introduction.tex line 4 em-dash:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "40660f24-88d8-4aa0-8df4-e07cb9e331ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrYn7rm3J7A2TvtVp4ns8t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 428,
      "cache_read_input_tokens": 119246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 428
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

_source line 272_

<details open><summary>🔧 Tool call — Edit · `toolu_01GSfjUqCxpkZJ6brBUZUzcy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "(document-level)---near or exceeding halving",
  "new_string": "(document-level), near or exceeding halving"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "ce0fb614-e174-42bf-a3f1-b2cf20984efd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrYn7rm3J7A2TvtVp4ns8t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 428,
      "cache_read_input_tokens": 119246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 428
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

_source line 273 · 2026-05-17T08:12:15.509Z_

<details><summary>↩ Tool result · `toolu_01GSfjUqCxpkZJ6brBUZUzcy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "39b96d94-3cbe-4508-91e0-b6a82eb53235",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "oldString": "(document-level)---near or exceeding halving",
    "newString": "(document-level), near or exceeding halving",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\\footnote{Code and data will be released upon acceptance. Anonymous review materials: \\url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\\% with one relation to 49.5\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat explains this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nThis study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nTo our knowledge, we present the first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS), defined as pairwise embedding cosine similarity, and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield five findings: (1)~degradation operates along two dimensions: count-associated recall decline (up to $-$49\\,pp at intermediate schema sizes for document-level RE) and confusability-associated type substitution (typical-batch gap ${\\approx}\\,2.2$\\,pp; quartile $\\Delta = -5.3$\\,pp), an asymmetric relationship where count dominates, consistent with bounded association in RE (TOST $p = 0.003$ at $\\pm 3$\\,pp) but coupled in NER where NER recall exhibits non-monotonic recovery at full-schema; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification; RE confusability-aware grouping yields no significant improvement over random (+1.4\\,pp, $p \\approx 0.19$, n.s.) despite oracle routing recovering +29.8\\,pp.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Count dominates confusability by ${\\sim}20\\times$ in typical batches.} Stratified design shows count effects ($-$42\\% to $-$56\\% recall) dwarf typical confusability effects (2.2\\,pp). Association is bounded in RE but not in NER, where boundary and type ambiguity couple (\\S\\ref{sec:multi_channel}).\n\\item \\textbf{First controlled validation that embedding similarity predicts type confusion in zero-shot IE.} SCS correlates with confusion rates ($r = 0.112$--$0.129$), with centrality confound identified on homogeneous schemas, invalidating naive per-type aggregation (\\S\\ref{sec:scs-validation}).\n\\item \\textbf{BCS generalizes across RE tasks and schema sizes.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.22\\text{--}0.53$); applicability to span-level tasks (NER, ED) requires confound adjustment (\\S\\ref{sec:bcs_controlled}).\n\\item \\textbf{Schema decomposition exposes systematic routing failure.} NER merge strategies collapse precision; all practical RE routing strategies fall below the single-pass baseline despite oracle routing recovering +29.8\\,pp, because constrained decoding eliminates reliable confidence signals (\\S\\ref{sec:sdgd}).\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " \\section{Introduction}",
          " \\label{sec:introduction}",
          " ",
          "-Training-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\\footnote{Code and data will be released upon acceptance. Anonymous review materials: \\url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\\% with one relation to 49.5\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.",
          "+Training-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\\footnote{Code and data will be released upon acceptance. Anonymous review materials: \\url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\\% with one relation to 49.5\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level), near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.",
          " ",
          " What explains this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).",
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

_source line 274_

related_work.tex remaining em-dashes:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "b2faf1bd-f2b3-4ce0-84db-bd2bb0b9369e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rv3kiLLTSRaYVsqxSRpmdF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 119674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 231
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

_source line 275_

<details open><summary>🔧 Tool call — Edit · `toolu_01MjRx5avugK9jZwyEbWeAmB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "old_string": "cocchieri-2025-zeroner}---both orthogonal",
  "new_string": "cocchieri-2025-zeroner}, both orthogonal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "5e58e2da-515c-49cf-a77d-4964e8bd8705",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rv3kiLLTSRaYVsqxSRpmdF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 119674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 231
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

_source line 276 · 2026-05-17T08:12:19.597Z_

<details><summary>↩ Tool result · `toolu_01MjRx5avugK9jZwyEbWeAmB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "dfe82dff-a0ed-477b-888f-fc7cd23934b0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "oldString": "cocchieri-2025-zeroner}---both orthogonal",
    "newString": "cocchieri-2025-zeroner}, both orthogonal",
    "originalFile": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\nTraining-free LLM IE spans instruction tuning \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \\cite{gollie-2024,adelie-2024}, schema-driven decoding \\cite{slot-2025,oneke-2025}, and constrained JSON decoding \\cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \\cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \\cite{uniner-2024}, and bidirectional encoders \\cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \\cite{relationprompt-2022} and revisits relation extraction in the LLM era \\cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.\n\n\\paragraph{Schema complexity in IE.}\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. Specifically, LLM-PEE employs union merge across sub-schema extractions, which our \\S\\ref{sec:sdgd} analysis shows causes precision to collapse from 0.56 to 0.21 in NER as false positives accumulate across passes; RE avoids this because closed-set classification does not require span reconciliation, explaining why LLM-PEE's decomposition succeeds for relation/event tasks but faces unresolved merge challenges on span-level extraction. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation factors. Concurrently, \\citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \\emph{why} such reduction works: it implicitly lowers batch confusability.\n\n\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \\citep{deng-2010-imagenet}, label confusion matrices improve text classification \\citep{guo-2021-label-confusion}, and classification confusion captures semantic similarity \\citep{zhou-2025-rethinking}. Hierarchical label sets reduce class confusion in zero-shot image classification \\citep{novack-2023-chils}; enriched type descriptions improve zero-shot NER \\citep{cocchieri-2025-zeroner}---both orthogonal to our confusability-aware batching.\n\n\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}.\n\n\\paragraph{Embedding anisotropy.}\nOur centrality confound (\\S\\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \\cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \\cite{cai-isotropy-clusters-2021}, explaining why MAVEN's single-ontology types conflate confusability with centrality.\n\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " \\paragraph{Schema complexity in IE.}",
          " The most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. Specifically, LLM-PEE employs union merge across sub-schema extractions, which our \\S\\ref{sec:sdgd} analysis shows causes precision to collapse from 0.56 to 0.21 in NER as false positives accumulate across passes; RE avoids this because closed-set classification does not require span reconciliation, explaining why LLM-PEE's decomposition succeeds for relation/event tasks but faces unresolved merge challenges on span-level extraction. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation factors. Concurrently, \\citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \\emph{why} such reduction works: it implicitly lowers batch confusability.",
          " ",
          "-\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \\citep{deng-2010-imagenet}, label confusion matrices improve text classification \\citep{guo-2021-label-confusion}, and classification confusion captures semantic similarity \\citep{zhou-2025-rethinking}. Hierarchical label sets reduce class confusion in zero-shot image classification \\citep{novack-2023-chils}; enriched type descriptions improve zero-shot NER \\citep{cocchieri-2025-zeroner}---both orthogonal to our confusability-aware batching.",
          "+\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \\citep{deng-2010-imagenet}, label confusion matrices improve text classification \\citep{guo-2021-label-confusion}, and classification confusion captures semantic similarity \\citep{zhou-2025-rethinking}. Hierarchical label sets reduce class confusion in zero-shot image classification \\citep{novack-2023-chils}; enriched type descriptions improve zero-shot NER \\citep{cocchieri-2025-zeroner}, both orthogonal to our confusability-aware batching.",
          " ",
          " \\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}.",
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

_source line 277_

<details open><summary>🔧 Tool call — Edit · `toolu_015xrdt5S5SGRGjwEWBKmnzr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "old_string": "formal definition---pairwise cosine similarity of type name embeddings---with",
  "new_string": "formal definition (pairwise cosine similarity of type name embeddings) with"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "7ae6736b-8393-48e3-ba37-23e21de27dfc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6P9nuotWQsDV2Xwv2R5un",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 119905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 240
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

_source line 278 · 2026-05-17T08:12:22.802Z_

<details><summary>↩ Tool result · `toolu_015xrdt5S5SGRGjwEWBKmnzr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "3d0e3faf-b315-4979-a4e4-10e4087d4d43",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "oldString": "formal definition---pairwise cosine similarity of type name embeddings---with",
    "newString": "formal definition (pairwise cosine similarity of type name embeddings) with",
    "originalFile": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\nTraining-free LLM IE spans instruction tuning \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \\cite{gollie-2024,adelie-2024}, schema-driven decoding \\cite{slot-2025,oneke-2025}, and constrained JSON decoding \\cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \\cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \\cite{uniner-2024}, and bidirectional encoders \\cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \\cite{relationprompt-2022} and revisits relation extraction in the LLM era \\cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.\n\n\\paragraph{Schema complexity in IE.}\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. Specifically, LLM-PEE employs union merge across sub-schema extractions, which our \\S\\ref{sec:sdgd} analysis shows causes precision to collapse from 0.56 to 0.21 in NER as false positives accumulate across passes; RE avoids this because closed-set classification does not require span reconciliation, explaining why LLM-PEE's decomposition succeeds for relation/event tasks but faces unresolved merge challenges on span-level extraction. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation factors. Concurrently, \\citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \\emph{why} such reduction works: it implicitly lowers batch confusability.\n\n\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \\citep{deng-2010-imagenet}, label confusion matrices improve text classification \\citep{guo-2021-label-confusion}, and classification confusion captures semantic similarity \\citep{zhou-2025-rethinking}. Hierarchical label sets reduce class confusion in zero-shot image classification \\citep{novack-2023-chils}; enriched type descriptions improve zero-shot NER \\citep{cocchieri-2025-zeroner}, both orthogonal to our confusability-aware batching.\n\n\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}.\n\n\\paragraph{Embedding anisotropy.}\nOur centrality confound (\\S\\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \\cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \\cite{cai-isotropy-clusters-2021}, explaining why MAVEN's single-ontology types conflate confusability with centrality.\n\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \\citep{deng-2010-imagenet}, label confusion matrices improve text classification \\citep{guo-2021-label-confusion}, and classification confusion captures semantic similarity \\citep{zhou-2025-rethinking}. Hierarchical label sets reduce class confusion in zero-shot image classification \\citep{novack-2023-chils}; enriched type descriptions improve zero-shot NER \\citep{cocchieri-2025-zeroner}, both orthogonal to our confusability-aware batching.",
          " ",
          "-\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}.",
          "+\\paragraph{SCS novelty.} SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}.",
          " ",
          " \\paragraph{Embedding anisotropy.}",
          " Our centrality confound (\\S\\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \\cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \\cite{cai-isotropy-clusters-2021}, explaining why MAVEN's single-ontology types conflate confusability with centrality."
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

_source line 279_

results.tex line 29 em-dash:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "c4c43dbd-db72-4c44-acf4-546e7fa80e7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7WG5cvSjaN7tY5syejoQU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 120145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 231
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

_source line 280_

<details open><summary>🔧 Tool call — Read · `toolu_01HXncaCKtAbwSqHspFgUbSA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": 28,
  "limit": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "816ab31d-a03f-404b-887e-762699d66e4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7WG5cvSjaN7tY5syejoQU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 120145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 231
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

_source line 281 · 2026-05-17T08:12:25.324Z_

<details><summary>↩ Tool result · `toolu_01HXncaCKtAbwSqHspFgUbSA`</summary>

```text
28	
29	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$)---and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "1b36d371-02a3-405c-9c08-927ca52725f8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$)---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.",
      "numLines": 2,
      "startLine": 28,
      "totalLines": 92
    }
  }
}
```

</details>

---


### Tool call

_source line 282_

<details open><summary>🔧 Tool call — Edit · `toolu_01G7BzMbeNSTea3PY2Pp2e52`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "as $t_j$)---and correlate",
  "new_string": "as $t_j$) and correlate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "9cca9266-2d66-4345-9819-02e321a81628",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S1b4ZQe158LFUir6s6ht7q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 120376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 257
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

_source line 283 · 2026-05-17T08:12:28.010Z_

<details><summary>↩ Tool result · `toolu_01G7BzMbeNSTea3PY2Pp2e52`</summary>

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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "7d6da489-4528-4559-955c-7ab5f05b2dff",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "as $t_j$)---and correlate",
    "newString": "as $t_j$) and correlate",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\\pm 1$\\,SD across 3 seeds (42, 123, 456) $\\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\\%$\\to$38.7\\%, $-$56\\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty. The pattern replicates across three seeds (42, 123, 456; max $\\Delta = 10.7$\\,pp, within 1\\,SD); intra-batch variance exceeds inter-seed variance by ${>}$5$\\times$ at every count level (Appendix~\\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$, pooled across three seeds). Count curves (25 batches per level) establish trend direction with error bars; magnitude estimation relies on the higher-powered BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$)---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) is excluded as RE's per-instance format precludes direct comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]; both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}). Notably, the independent MiniLM embedding yields a \\emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\\ Qwen3 $r = 0.138$; Appendix), suggesting that shared-representation bias is conservative rather than inflationary.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Conditional pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ unconditional $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}; we note the conditioning inflates this estimate) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, consistent with a Monte Carlo simulation accounting for inter-pair correlation structure; see Appendix~\\ref{app:aggregation-sim} for the illustrative aggregation model).\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime, suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Dimension~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Dimension~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$), modestly attenuated from v1's extreme-batch gap but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}). The BCS--accuracy correlation holds across four structurally distinct prompt variants at count 32 (all $r < -0.47$; Appendix~\\ref{sec:appendix_prompt_variants}), confirming that the confusability effect is not an artifact of prompt design.\n\n\\subsection{Multi-Dimensional Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion), consistent with bounded association in RE but coupled in NER where type ambiguity and boundary ambiguity interact. The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. TOST equivalence testing confirms bounded association (interaction = 0.47\\,pp, $p_{\\text{TOST}} = 0.003$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}).\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality: high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 26,
        "oldLines": 7,
        "newStart": 26,
        "newLines": 7,
        "lines": [
          " \\subsection{Pairwise Confusability and Type Confusion}",
          " \\label{sec:pairwise}",
          " ",
          "-We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$)---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.",
          "+We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.",
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

_source line 284_

sdgd_negative.tex line 21 em-dash:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "8a85b5bb-dde3-4cfe-87a9-21eba3c7d388",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjVR8RjnwMK1k2kwjCfEem",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 216,
      "cache_read_input_tokens": 120633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 216
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

_source line 285_

<details open><summary>🔧 Tool call — Edit · `toolu_01SyyFD5Lr1NHakmyWUtjki1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "old_string": "baseline---a gain of +29.8",
  "new_string": "baseline, a gain of +29.8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "4eb7a5c9-1010-4a18-8448-cbc9f3845846",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjVR8RjnwMK1k2kwjCfEem",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 216,
      "cache_read_input_tokens": 120633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 216
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

_source line 286 · 2026-05-17T08:12:32.898Z_

<details><summary>↩ Tool result · `toolu_01SyyFD5Lr1NHakmyWUtjki1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "f6cbfe98-3ce4-4a2d-804d-17e581e3d9d5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "oldString": "baseline---a gain of +29.8",
    "newString": "baseline, a gain of +29.8",
    "originalFile": "\\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}\n\\label{sec:sdgd}\n\nA natural intervention against confusability-associated degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \\textbf{Schema-DAG-Guided Decomposition} (SDGD\\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an adopted abbreviation for schema decomposition and grouping; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\\,=\\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\\ref{tab:sdgd_results}, Appendix~\\ref{sec:appendix_sdgd}).\n\n\\paragraph{Merge amplification in NER.}\nThe core failure mode is \\emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calibrated across passes \\cite{llm-calibration-survey-2024}, the same span may receive conflicting type labels from different passes, or hallucinated entities may appear in passes where the correct type is absent. Union merge retains all predictions, so false positives scale with $k$ while true positives are bounded by the fixed set of gold entities.\n\nQuantitatively, single-pass precision (0.563) collapses to 0.210--0.249 after union merge across 8 batches, while recall gains are modest (0.368 $\\to$ 0.314 for sdgd\\_zero, 0.446 for random batch). The net F1 loss is substantial: 0.445 $\\to$ 0.251 (sdgd\\_zero) or 0.320 (random batch). Per-type extraction (66 batches) pushes recall to 0.586 but precision to 0.194 (F1\\,=\\,0.292), confirming that the precision--recall imbalance intensifies with the number of passes. Random batching outperforms confusability-aware SDGD on NER (0.320 vs.\\ 0.251) because the dominant degradation source (merge amplification) is independent of batch composition; any multi-pass scheme suffers from it regardless of grouping quality.\n\n\\paragraph{Confidence gating does not resolve merge amplification.}\nConfidence-based gating (retaining only predictions above threshold) trades recall for precision but does not recover net F1 (0.251$\\to$0.241), confirming that merge artifacts are systemic rather than confined to low-confidence predictions (Appendix~\\ref{sec:appendix_sdgd}).\n\n\\paragraph{Why NER fails but RE does not.}\nMerge amplification is specific to span-level tasks. Each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. RE avoids this failure mode entirely: under oracle routing, each relation instance receives a single classification from the batch containing its gold type, requiring no span reconciliation and eliminating the multi-pass interference that causes SDGD to fail on NER. This makes RE a clean testbed for evaluating whether confusability-aware decomposition improves accuracy once merge artifacts are removed.\n\n\\enlargethispage*{9\\baselineskip}\n\\paragraph{Oracle routing as performance ceiling.}\nOracle routing routes each test instance to the batch containing its gold type, eliminating cross-type confusion within each batch. On FewRel 80-relation RE, oracle-routed decomposition achieves 0.802 accuracy versus 0.504 for the single-pass baseline---a gain of +29.8\\,pp (Table~\\ref{tab:batch_composition}). This is the strongest positive finding of the decomposition experiments: it demonstrates that type confusability is indeed a key predictor of degradation in RE, and that performance recovers substantially when confusable types are separated.\n\nHowever, oracle routing requires gold labels and is not deployable. The gap between the oracle ceiling and practical routing reveals an important asymmetry: while \\emph{any} decomposition benefits enormously from removing the 80-type bottleneck (+28.4\\,pp for random batching, +29.8\\,pp for graph coloring), the \\emph{additional} benefit of confusability-aware grouping over random grouping is modest (+1.4\\,pp, $p \\approx 0.19$). The confusability-aware strategy ranks 13th out of 15 random seeds, limited by the narrow BCS margin (0.006) between graph-coloring and random batches at this partition granularity. Finer-grained partitioning or alternative confusability metrics may be needed to translate the oracle-demonstrated potential into significant practical gains.\n\n\\paragraph{Practical routing strategies.}\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using a coarser 5-group decomposition (oracle ceiling: 72.4\\%, +22.0\\,pp; cf.\\ +29.8\\,pp under 17-group decomposition in Table~\\ref{tab:batch_composition}): max-confidence (all predictions), max-confidence (positive only), none-aware selection, margin-based routing, and random assignment. All five perform below the single-pass baseline (50.4\\%), with the best practical strategy reaching only 36.5\\% accuracy (Table~\\ref{tab:routing_strategies}, Appendix~\\ref{sec:appendix_routing}). The root cause is constrained decoding: the enum constraint forces the model to produce a confident type prediction for every sub-schema, even when the correct type is absent from the candidate set. As a result, 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, and the none-rate per sub-schema is only 20--40\\%. Because every sub-schema produces high-confidence outputs, confidence signals become unreliable and all confidence-based routing fails. Free-form generation or calibrated confidence estimation may provide more reliable routing signals for future work.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds. Graph coloring yields +1.4\\,pp over random batching ($p \\approx 0.19$, n.s.) with a narrow BCS margin (0.006). The +29.8\\,pp gap between single-pass and decomposed conditions confirms that type separation recovers performance when merge amplification is absent.}\n\\label{tab:batch_composition}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 7,
        "newStart": 18,
        "newLines": 7,
        "lines": [
          " ",
          " \\enlargethispage*{9\\baselineskip}",
          " \\paragraph{Oracle routing as performance ceiling.}",
          "-Oracle routing routes each test instance to the batch containing its gold type, eliminating cross-type confusion within each batch. On FewRel 80-relation RE, oracle-routed decomposition achieves 0.802 accuracy versus 0.504 for the single-pass baseline---a gain of +29.8\\,pp (Table~\\ref{tab:batch_composition}). This is the strongest positive finding of the decomposition experiments: it demonstrates that type confusability is indeed a key predictor of degradation in RE, and that performance recovers substantially when confusable types are separated.",
          "+Oracle routing routes each test instance to the batch containing its gold type, eliminating cross-type confusion within each batch. On FewRel 80-relation RE, oracle-routed decomposition achieves 0.802 accuracy versus 0.504 for the single-pass baseline, a gain of +29.8\\,pp (Table~\\ref{tab:batch_composition}). This is the strongest positive finding of the decomposition experiments: it demonstrates that type confusability is indeed a key predictor of degradation in RE, and that performance recovers substantially when confusable types are separated.",
          " ",
          " However, oracle routing requires gold labels and is not deployable. The gap between the oracle ceiling and practical routing reveals an important asymmetry: while \\emph{any} decomposition benefits enormously from removing the 80-type bottleneck (+28.4\\,pp for random batching, +29.8\\,pp for graph coloring), the \\emph{additional} benefit of confusability-aware grouping over random grouping is modest (+1.4\\,pp, $p \\approx 0.19$). The confusability-aware strategy ranks 13th out of 15 random seeds, limited by the narrow BCS margin (0.006) between graph-coloring and random batches at this partition granularity. Finer-grained partitioning or alternative confusability metrics may be needed to translate the oracle-demonstrated potential into significant practical gains.",
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

_source line 287_

Now re-run the em-dash verification:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "a070a5fc-42e4-465d-8209-591bacd002ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jdbeu2p34VqkcpUJ6Y7fwQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 396,
      "cache_read_input_tokens": 120849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 396
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

_source line 288_

<details open><summary>🔧 Tool call — Bash · `toolu_01GWmgZNfLk4PafUd5EyAxvp`</summary>

```json
{
  "command": "grep -n \"\\-\\-\\-\" *.tex | grep -v \"^.*&.*---\" | grep -v DEPRECATED",
  "description": "Re-check prose em-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "a63f8d1a-e2a9-4192-bee6-e58e2ffc7c7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jdbeu2p34VqkcpUJ6Y7fwQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 396,
      "cache_read_input_tokens": 120849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 396
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

_source line 289 · 2026-05-17T08:12:37.112Z_

<details><summary>↩ Tool result · `toolu_01GWmgZNfLk4PafUd5EyAxvp`</summary>

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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "50e87f2e-abc9-4ddb-b703-4be7774409b2",
  "tool_use_result": {
    "stdout": "",
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


### Assistant

_source line 290_

Zero residual em-dashes in prose. Now compile:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "674209b9-e961-40df-9223-6fedfeb3d14c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Psrz1wDcHg1RppReceKDHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 134,
      "cache_read_input_tokens": 121245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 134
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

_source line 291_

<details open><summary>🔧 Tool call — Bash · `toolu_01YEjsnR8R1gLsgQcdg4mBBW`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "First pdflatex pass on main.tex",
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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "ee061cfd-1b7d-4ce7-aeb3-612b178e42fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Psrz1wDcHg1RppReceKDHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 134,
      "cache_read_input_tokens": 121245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 134
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

_source line 292 · 2026-05-17T08:12:41.725Z_

<details><summary>↩ Tool result · `toolu_01YEjsnR8R1gLsgQcdg4mBBW`</summary>

```text
Package rerunfilecheck Warning: File `main.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (21 pages, 442427 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "38aca4ac-4cad-40bb-a794-b4f9fbd0c9a7",
  "tool_use_result": {
    "stdout": "Package rerunfilecheck Warning: File `main.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (21 pages, 442427 bytes).\nTranscript written on main.log.",
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

_source line 293_

<details open><summary>🔧 Tool call — Bash · `toolu_01DexMHqoruBUCYMkW1Bp1hp`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "Second and third pdflatex passes on main.tex",
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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "c72573c4-edbb-40e2-8a0f-34cab98a1e3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5RrCPtpyWKcbNbuYu7v11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 121379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1025
      },
      "output_tokens": 53,
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

_source line 294 · 2026-05-17T08:12:47.909Z_

<details><summary>↩ Tool result · `toolu_01DexMHqoruBUCYMkW1Bp1hp`</summary>

```text
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (21 pages, 442285 bytes).
Transcript written on main.log.
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (21 pages, 442285 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "29c03510-c429-4246-9713-5263bfe10e12",
  "tool_use_result": {
    "stdout": "re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (21 pages, 442285 bytes).\nTranscript written on main.log.\nre/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (21 pages, 442285 bytes).\nTranscript written on main.log.",
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

_source line 295_

<details open><summary>🔧 Tool call — Bash · `toolu_014FoNZFZz3WuZpn4pYpj2Fs`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode supplementary.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode supplementary.tex 2>&1 | tail -5",
  "description": "Compile supplementary.tex (2 passes)",
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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "49661fd1-76f9-4d1e-9f70-2a536cf97965",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CiiKKurN5u4QLqzq3VU8KF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 122404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 411
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

_source line 296 · 2026-05-17T08:12:54.372Z_

<details><summary>↩ Tool result · `toolu_014FoNZFZz3WuZpn4pYpj2Fs`</summary>

```text
xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmri8a.pfb>
Output written on supplementary.pdf (8 pages, 233668 bytes).
Transcript written on supplementary.log.
type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/ti
mes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on supplementary.pdf (8 pages, 233186 bytes).
Transcript written on supplementary.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "f1a59019-ebee-4baa-81e7-096f244467d8",
  "tool_use_result": {
    "stdout": "xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmri8a.pfb>\nOutput written on supplementary.pdf (8 pages, 233668 bytes).\nTranscript written on supplementary.log.\ntype1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/ti\nmes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on supplementary.pdf (8 pages, 233186 bytes).\nTranscript written on supplementary.log.",
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

_source line 297_

Now check for LaTeX errors and undefined references:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "8ccd3649-997b-4b2b-91c9-06483b3e0732",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyQQ1gNg6b3bcJkt7NGkQD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 429,
      "cache_read_input_tokens": 122815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 429
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

_source line 298_

<details open><summary>🔧 Tool call — Bash · `toolu_01Xr3udMUF4jz4tkuJp1EVgq`</summary>

```json
{
  "command": "grep -c \"^!\" main.log && grep -c \"undefined\" main.log && grep \"^!\" main.log; echo \"---\"; grep -c \"^!\" supplementary.log && grep -c \"undefined\" supplementary.log && grep \"^!\" supplementary.log",
  "description": "Check for LaTeX errors and undefined references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "ec3bdbc3-3bc3-4bb5-8103-74b729565180",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyQQ1gNg6b3bcJkt7NGkQD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 429,
      "cache_read_input_tokens": 122815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 429
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

_source line 299 · 2026-05-17T08:12:57.580Z_

<details><summary>↩ Tool result · `toolu_01Xr3udMUF4jz4tkuJp1EVgq`</summary>

```text
0
---
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "1146d7dd-d5fc-4a6c-967f-b24d50b1ebfe",
  "tool_use_result": {
    "stdout": "0\n---\n0",
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

_source line 300_

<details open><summary>🔧 Tool call — Bash · `toolu_01RCsp9opkwaq12cYzX4BZV7`</summary>

```json
{
  "command": "grep -i \"undefined\" main.log | head -5; echo \"===\"; grep -i \"undefined\" supplementary.log | head -5",
  "description": "Check undefined references in logs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "d4b4d66e-3db1-4607-a333-298f384c5b75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzSATGpJCG2XxdVG4C8xgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 165,
      "cache_read_input_tokens": 123244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 165
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

_source line 301 · 2026-05-17T08:13:00.566Z_

<details><summary>↩ Tool result · `toolu_01RCsp9opkwaq12cYzX4BZV7`</summary>

```text
===
LaTeX Warning: Reference `sec:model' on page 1 undefined on input line 42.
LaTeX Warning: Reference `sec:count_curves' on page 1 undefined on input line 4
LaTeX Warning: Reference `sec:model' on page 1 undefined on input line 42.
LaTeX Warning: Reference `sec:count_curves' on page 1 undefined on input line 4
LaTeX Warning: Reference `tab:batch_composition' on page 2 undefined on input l
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "782b2c26-33ed-4bab-abf5-29a595407c01",
  "tool_use_result": {
    "stdout": "===\nLaTeX Warning: Reference `sec:model' on page 1 undefined on input line 42.\nLaTeX Warning: Reference `sec:count_curves' on page 1 undefined on input line 4\nLaTeX Warning: Reference `sec:model' on page 1 undefined on input line 42.\nLaTeX Warning: Reference `sec:count_curves' on page 1 undefined on input line 4\nLaTeX Warning: Reference `tab:batch_composition' on page 2 undefined on input l",
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

_source line 302_

<details><summary>Logged reasoning block</summary>

```text
The supplementary.tex has undefined references, which is expected since it's a standalone file that references labels defined in the main paper sections (which are not included via \input in supplementary.tex). These are pre-existing warnings, not caused by our edits. Let me verify the main.tex has no undefined references, and check the page count.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "b458a819-3d4e-4591-80ac-13b09506c815",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVvwm1GnXtDmKTMEmqwfVs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 123409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
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

_source line 303_

The supplementary.tex undefined refs are pre-existing (it references labels from main paper sections not included in its standalone build). Main.tex has zero errors and zero undefined references.

Let me check the page count for the main body:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "b9d8fd13-f34d-46bc-b639-ae6ceba9aab0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVvwm1GnXtDmKTMEmqwfVs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 123409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
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

_source line 304_

<details open><summary>🔧 Tool call — Bash · `toolu_01QvMR8nu721aSJGBzKjdN5h`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\appendix\" main.tex | head -3",
  "description": "Find where appendix starts in main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "812c1002-79bf-49c0-894d-37b358f67395",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVvwm1GnXtDmKTMEmqwfVs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 123409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
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

_source line 305 · 2026-05-17T08:13:06.611Z_

<details><summary>↩ Tool result · `toolu_01QvMR8nu721aSJGBzKjdN5h`</summary>

```text
63:\appendix
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "bcb6ceda-4e38-4e29-8373-2e99a5a9bc99",
  "tool_use_result": {
    "stdout": "63:\\appendix",
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

_source line 306_

<details open><summary>🔧 Tool call — Bash · `toolu_01RwZ2NdkdAdqMN88KVEidoV`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\section\\|\\\\\\\\appendix\\|Output written\" main.log | grep -i \"page\\|appendix\\|section\" | head -20",
  "description": "Check section layout in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "daacb8aa-8b60-45c7-a6c3-fa71aab7e0b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q1hSQ35usW621W34NgjMqy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 123642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 404
      },
      "output_tokens": 43,
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

_source line 307 · 2026-05-17T08:13:10.351Z_

<details><summary>↩ Tool result · `toolu_01RwZ2NdkdAdqMN88KVEidoV`</summary>

```text
843:Output written on main.pdf (21 pages, 442285 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "ecd74355-8d9f-42e3-8569-a8b52a2c19de",
  "tool_use_result": {
    "stdout": "843:Output written on main.pdf (21 pages, 442285 bytes).",
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

_source line 308_

<details open><summary>🔧 Tool call — Bash · `toolu_01W8LhKaLggQdjYajn25gB8u`</summary>

```json
{
  "command": "grep \"\\[.*\\]\" main.log | grep -E \"^\\[\" | head -25",
  "description": "Check page numbers in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "90191080-2c3e-4b44-8742-5d34d544703d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TYieWkwTC5tqruHRyCVTK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 142,
      "cache_read_input_tokens": 124046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 142
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

_source line 309 · 2026-05-17T08:13:12.989Z_

<details><summary>↩ Tool result · `toolu_01W8LhKaLggQdjYajn25gB8u`</summary>

```text
grep: main.log: binary file matches
[Loading MPS to PDF converter (version 2006.09.02).]
[]\T1/ptm/m/n/10 (-20) Table 1: |Dataset statis-tics. BCS Range in-di-cates the
[4]) (./results.tex
[6]
[7 <../../figures/paper/fig_error_taxonomy.pdf>]) (./discussion.tex
[8])
[9] (./checklist.tex [10]
[]\T1/ptm/m/n/10 (+20) Dhananjay Ashok and Zachary C. Lip-ton. 2023.
[11] [12]
[]\T1/ptm/m/n/10 (+20) Dong Zhao, Yadong Wang, Xi-ang Chen, Chenxi
[13])
[]\T1/ptm/m/n/10.95 (+20) Single-pass ex-trac-tion achieves F1=0.445
[14]
[18]
[19]
[] \OT1/cmr/m/n/10.95 = \OML/cmm/m/it/10.95 ^^L[] \OT1/cmr/m/n/10.95 + \OML/cmm
[20] [21
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "c5c812c0-e0e6-4bb0-8abd-47f9c142517d",
  "tool_use_result": {
    "stdout": "grep: main.log: binary file matches\n[Loading MPS to PDF converter (version 2006.09.02).]\n[]\\T1/ptm/m/n/10 (-20) Table 1: |Dataset statis-tics. BCS Range in-di-cates the\n[4]) (./results.tex\n[6]\n[7 <../../figures/paper/fig_error_taxonomy.pdf>]) (./discussion.tex\n[8])\n[9] (./checklist.tex [10]\n[]\\T1/ptm/m/n/10 (+20) Dhananjay Ashok and Zachary C. Lip-ton. 2023.\n[11] [12]\n[]\\T1/ptm/m/n/10 (+20) Dong Zhao, Yadong Wang, Xi-ang Chen, Chenxi\n[13])\n[]\\T1/ptm/m/n/10.95 (+20) Single-pass ex-trac-tion achieves F1=0.445\n[14]\n[18]\n[19]\n[] \\OT1/cmr/m/n/10.95 = \\OML/cmm/m/it/10.95 ^^L[] \\OT1/cmr/m/n/10.95 + \\OML/cmm\n[20] [21",
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

_source line 310_

Main body ends at page 8 (discussion.tex finishes on page 8), then checklist starts on page 9. The body content (before checklist/appendix) fits within 8 pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "d47d3452-9a17-4686-b04c-2837e08e1b59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CruXp4K9HM1x7WQePyxdgX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 124188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 434
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

_source line 311_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01K3KtzPHYdG2REYPHV6fixD`</summary>

```json
{
  "todos": [
    {
      "content": "P1A-P1E, P2-P5, P6, P7: All text modifications",
      "status": "completed",
      "activeForm": "Text modifications complete"
    },
    {
      "content": "Verification grep and compile",
      "status": "completed",
      "activeForm": "Verification complete"
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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "88dbf1fc-228a-4934-bc1f-b7f42806364c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CruXp4K9HM1x7WQePyxdgX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 124188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 434
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

_source line 312 · 2026-05-17T08:13:17.365Z_

<details><summary>↩ Tool result · `toolu_01K3KtzPHYdG2REYPHV6fixD`</summary>

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
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "ddd9303c-9133-4a7d-9fc4-0b36a8564611",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "P1A-P1E, P2-P5, P6, P7: All text modifications",
        "status": "completed",
        "activeForm": "Text modifications complete"
      },
      {
        "content": "Verification grep and compile",
        "status": "in_progress",
        "activeForm": "Running verification greps"
      }
    ],
    "newTodos": [
      {
        "content": "P1A-P1E, P2-P5, P6, P7: All text modifications",
        "status": "completed",
        "activeForm": "Text modifications complete"
      },
      {
        "content": "Verification grep and compile",
        "status": "completed",
        "activeForm": "Verification complete"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 313_

All modifications complete. Summary:

**P1A (driven/drive/driver):** 9 replacements across abstract, introduction, discussion, sdgd_negative, supplementary, main. Zero residual (confirmed by grep; "schema-driven" and "does not drive" preserved).

**P1B (channel→dimension):** All instances replaced across abstract, introduction, discussion, results, checklist, main, supplementary. `\label{sec:multi_channel}` preserved. Zero residual.

**P1C (bounded interaction→bounded association):** All 9 instances replaced (abstract, intro×2, discussion, results×2, main×2, supplementary). Zero residual.

**P1D (mechanism):** 5 replacements (intro→"factors", related_work→"factors", discussion→removed "mechanistic", sdgd×2→"failure mode"). "Causal mechanism" in Limitations preserved.

**P1E:** Predictive framework statement inserted before "We ask three questions" in introduction.

**P2:** Contribution #2 reframed: "First controlled validation that embedding similarity predicts type confusion in zero-shot IE." Em-dash replaced with comma.

**P3:** Abstract TOST details removed ("TOST $p = 0.003$ at $\pm 3$\,pp"). Three core numbers retained: 2.2pp, -49pp, 22-53%.

**P4:** Contributions compressed: #1 removed TOST p-value and condensed to 2 sentences. #4 condensed from 4 sentences to 1.

**P5:** Contribution #3 title changed to "BCS generalizes across RE tasks and schema sizes" with qualifier about span-level tasks.

**P6 (em-dashes):** All 18+ prose em-dashes replaced with commas, parentheses, semicolons, or colons across all files including experimental_setup.tex. Zero residual (grep confirmed).

**P7:** Three placeholder sections in supplementary.tex deleted (Per-Count-Level Statistics, Count Curve Raw Data, BCS-Controlled Raw Data). No labels were referenced elsewhere.

**Compilation:** Both main.tex (21 pages, 8-page body) and supplementary.tex (8 pages) compile with zero LaTeX errors. No new undefined references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "uuid": "b40a1af1-2b63-47a8-a34c-33b1941d7df1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013u669iQ2id3VYf2oSSCiMv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 124622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 211
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

_source line 314_

All modifications complete. Summary:

**P1A (driven/drive/driver):** 9 replacements across abstract, introduction, discussion, sdgd_negative, supplementary, main. Zero residual (confirmed by grep; "schema-driven" and "does not drive" preserved).

**P1B (channel→dimension):** All instances replaced across abstract, introduction, discussion, results, checklist, main, supplementary. `\label{sec:multi_channel}` preserved. Zero residual.

**P1C (bounded interaction→bounded association):** All 9 instances replaced (abstract, intro×2, discussion, results×2, main×2, supplementary). Zero residual.

**P1D (mechanism):** 5 replacements (intro→"factors", related_work→"factors", discussion→removed "mechanistic", sdgd×2→"failure mode"). "Causal mechanism" in Limitations preserved.

**P1E:** Predictive framework statement inserted before "We ask three questions" in introduction.

**P2:** Contribution #2 reframed: "First controlled validation that embedding similarity predicts type confusion in zero-shot IE." Em-dash replaced with comma.

**P3:** Abstract TOST details removed ("TOST $p = 0.003$ at $\pm 3$\,pp"). Three core numbers retained: 2.2pp, -49pp, 22-53%.

**P4:** Contributions compressed: #1 removed TOST p-value and condensed to 2 sentences. #4 condensed from 4 sentences to 1.

**P5:** Contribution #3 title changed to "BCS generalizes across RE tasks and schema sizes" with qualifier about span-level tasks.

**P6 (em-dashes):** All 18+ prose em-dashes replaced with commas, parentheses, semicolons, or colons across all files including experimental_setup.tex. Zero residual (grep confirmed).

**P7:** Three placeholder sections in supplementary.tex deleted (Per-Count-Level Statistics, Count Curve Raw Data, BCS-Controlled Raw Data). No labels were referenced elsewhere.

**Compilation:** Both main.tex (21 pages, 8-page body) and supplementary.tex (8 pages) compile with zero LaTeX errors. No new undefined references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 878274,
  "duration_api_ms": 873168,
  "num_turns": 129,
  "stop_reason": "end_turn",
  "session_id": "90846268-bc36-4324-9009-c8751031cca1",
  "total_cost_usd": 7.9206805000000005,
  "usage": {
    "input_tokens": 124,
    "cache_creation_input_tokens": 112992,
    "cache_read_input_tokens": 12447075,
    "output_tokens": 39433,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 112992,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 539,
        "cache_read_input_tokens": 124622,
        "cache_creation_input_tokens": 211,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 211
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 4393,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.004498,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 124,
      "outputTokens": 39433,
      "cacheReadInputTokens": 12447075,
      "cacheCreationInputTokens": 112992,
      "webSearchRequests": 0,
      "costUSD": 7.916182499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b9f5518e-7c1b-44c1-9f27-cd5ce1707d95"
}
```

</details>

---
