# Research conversation: [HANDOFF] 你是 Research Reviewer，这是 Loop #13。 ## 上一轮交接 (task_context) ### 1. 🔴 硬约束 / 红线 - 本项目 GPU 白名单未在 constraints.yaml 中 — Part 2 of 2

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-handoff-research-reviewer-loop-13-task-context-1-gpu-constraints-yaml-copy-2.md) · [Structured JSON](../../../sessions/2a/2ab8d40058700f2cb620.json)

## Round 7

### Tool result

_source line 223 · 2026-05-16T03:30:42.963Z_

<details><summary>↩ Tool result · `toolu_016iHDxs61jPThTpKcTBZToM`</summary>

```text
diff --git a/docs/paper/experiments.tex b/docs/paper/experiments.tex
index f27725f..71d8b12 100644
--- a/docs/paper/experiments.tex
+++ b/docs/paper/experiments.tex
@@ -5,14 +5,17 @@
 \label{sec:setup}
 
 \paragraph{Models.}
-We evaluate seven models spanning five architecture families and diverse attention configurations:
+We evaluate nine models spanning seven architecture families and diverse attention configurations:
 \textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\times$ 4 KV heads = 112),
 \textbf{Qwen2.5-14B} (GQA 5:1, 48 $\times$ 8 = 384),
 \textbf{Yi-1.5-9B} (GQA 8:1, 48 $\times$ 4 = 192),
 \textbf{Llama-3.1-8B} (GQA 4:1, 32 $\times$ 8 = 256),
+\textbf{CodeLlama-7B} (MHA 1:1, 32 $\times$ 32 = 1024; profiling only),
 \textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\times$ 8 = 256, sliding window attention),
 \textbf{Gemma-2-9B} (GQA 2:1, 42 $\times$ 8 = 336, \texttt{head\_dim}=256, attention logit softcapping),
+\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\times$ 10 = 400),
 and \textbf{Pythia-1.4B} (MHA 1:1, 24 $\times$ 16 = 384).
+Eight models undergo full constrained evaluation; CodeLlama-7B is characterized by profiling and heterogeneity classification only.
 This selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.
 
 \paragraph{Evaluation.}
@@ -25,7 +28,7 @@ All results use high-resolution profiling (64 sequences $\times$ 2048 tokens fro
 
 \paragraph{Compression and constraint.}
 The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
-The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2 and Pythia).
+The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).
 
 \paragraph{Baselines.}
 We compare against:
@@ -41,7 +44,7 @@ and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ d
 \begin{table}[t]
 \centering
 \small
-\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\times$ bf16), severe on Pythia ($1.9\times$), moderate on Gemma-2 ($1.5\times$), mild on remaining incl.\ Qwen-14B (${\sim}1.1\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \textbf{bold}. $^*$BOS-corrected.}
+\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\times$ bf16), severe on Pythia ($1.9\times$), moderate on Gemma-2 ($1.5\times$), mild on remaining incl.\ Qwen-14B (${\sim}1.1\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \textbf{bold}. $^*$BOS-corrected.}
 \label{tab:main_results}
 \begin{tabular}{lccccc}
 \toprule
@@ -55,6 +58,7 @@ Yi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\
 Llama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \textbf{8.45} \\
 Mistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\
 Gemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\
+Phi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\
 Pythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\
 \bottomrule
 \end{tabular}
@@ -67,12 +71,14 @@ Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 with
 On Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47, $\Delta < 0.02$ PPL).
 Hires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.
 
-On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.
+On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite high concentration (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.
 On Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.
 
 On Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\ uniform 6.17 ($+$0.4\%).
 Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\times$ bf16) from 31.5\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.
 
+On Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\times$ bf16). %exp_id=phi3_medium_constrained_mckp
+
 Unconstrained failure severity tracks heterogeneity shape: \emph{catastrophic} on Qwen-7B ($3.3\times$ bf16, 60\% heads at 2-bit), \emph{severe} on Pythia ($1.9\times$), \emph{moderate} on Gemma-2 ($1.47\times$), and \emph{mild} on remaining models (${\sim}1.07$--$1.12\times$) including Qwen-14B ($1.12\times$, 20\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\ flat).
 See Appendix~\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\ref{sec:budget_sweep} (budget sweep) for additional detail.
 
@@ -86,28 +92,51 @@ The two approaches are orthogonal and composable: KIVI selects the per-channel s
 However, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.
 Per-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.
 
+\subsection{Cross-Architecture Compounding}
+\label{sec:compounding_cross}
+
+\begin{figure}[t]
+\centering
+\includegraphics[width=\columnwidth]{figures/fig_compounding_curves.pdf}
+\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\times$). All three stay near-baseline for $k{\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\approx}96$ due to its 112 KV heads (maximum ${\sim}96$ eligible for 2-bit assignment).}
+\label{fig:compounding_cross}
+\end{figure}
+
+Figure~\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.
+At small $k$ (${\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\leq}2.5\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.
+
+Beyond $k{=}8$, divergence is stark.
+Llama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.
+Qwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\times$) and $98.75$ at $k{=}256$ ($10.1\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.
+Mistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.
+
+These curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\times$ baseline) is ${\sim}32$ for Qwen, ${\sim}64$ for Llama, and ${\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.
+
 \subsection{Downstream Evaluation}
 \label{sec:downstream}
 
 \begin{table}[t]
 \centering
 \small
-\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\times$ compression. Qwen shows large gains; the remaining models show small degradations or neutrality, tracking PPL results.}
+\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\times$ compression. Qwen values are mean over 3 calibration seeds ($\pm$1$\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}
 \label{tab:downstream}
 \begin{tabular}{lccccc}
 \toprule
 Model & ARC-C & HS & PIQA & WG & Avg \\
 \midrule
-Qwen2.5-7B        & $+$3.2 & $+$4.0 & $+$1.3 & $+$2.0 & $+$2.6 \\
-Yi-1.5-9B        & $-$3.2 & $-$0.6 & $-$0.3 & $+$1.3 & $-$0.8 \\
-Llama-3.1-8B     & $-$2.7 & $-$0.1 & $-$0.7 & $-$0.2 & $-$1.0 \\
-Mistral-7B       & $-$1.2 & $-$0.2 & $+$0.4 & $-$1.0 & $-$0.5 \\
-Gemma-2-9B       & $-$0.2 & $+$0.3 & $-$0.1 & $+$0.8 & $+$0.1 \\
+Qwen2.5-7B        & $+$0.0{\scriptsize$\pm$0.4} & $+$4.1{\scriptsize$\pm$0.2} & $+$2.0{\scriptsize$\pm$0.2} & $+$1.6{\scriptsize$\pm$1.2} & $+$1.9 \\
+Yi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\
+Llama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\
+Mistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\
+Gemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\
 \bottomrule
 \end{tabular}
 \end{table}
 
-On Qwen, constrained MCKP improves average 0-shot accuracy by 2.6 pts over uniform (0.686 vs.\ 0.660), recovering $\sim$73\% of the accuracy lost to quantization.
-The four non-spread models show minor average degradation (Yi $-$0.8, Llama $-$1.0, Mistral $-$0.5, Gemma-2 $+$0.1 pts); Llama is the most systematic, with 0 of 5 tasks showing positive change.
-ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$3.2, Llama $-$2.7, Mistral $-$1.2, Gemma-2 $-$0.2 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.
-Cross-dataset (Appendix~\ref{sec:cross_dataset}, ${>}96\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\ref{sec:long_context}, Qwen uniform $11.15\times$ bf16 at 8K vs.\ MCKP $1.23\times$) analyses confirm allocation robustness.
\ No newline at end of file
+On Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\pm$1$\sigma$ in Table~\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).
+The four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.
+ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.
+Cross-dataset evaluation (Appendix~\ref{sec:cross_dataset}, ${>}96\%$ bit-assignment agreement across WikiText-2/C4) confirms calibration robustness.
+Long-context evaluation (Appendix~\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\times$ bf16 at 2K to $11.15\times$ at 8K, while constrained MCKP remains stable ($1.11\times$ to $1.23\times$).
+In contrast, Llama-3.1-8B (spike, $t_1/t_5{=}0.85$) shows negligible difference between uniform ($1.08\times$ bf16) and constrained MCKP ($1.08\times$) at 8K, consistent with its 2K behavior.
+The uniform-to-constrained PPL ratio on Qwen thus widens from $1.4\times$ at 2K to $9.1\times$ at 8K, while Llama remains flat---long-context stress amplifies the spread-specific benefit of per-head allocation.
\ No newline at end of file
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ad16e44-ad4d-407a-b7ba-d8a56392b10a",
  "isSidechain": false,
  "promptId": "d1a8ba68-f6bd-4e5c-b2e2-e61a399781d5",
  "type": "user",
  "uuid": "f8569fa7-35d3-4f59-9070-0ffd0ddbab6d",
  "toolUseResult": {
    "stdout": "diff --git a/docs/paper/experiments.tex b/docs/paper/experiments.tex\nindex f27725f..71d8b12 100644\n--- a/docs/paper/experiments.tex\n+++ b/docs/paper/experiments.tex\n@@ -5,14 +5,17 @@\n \\label{sec:setup}\n \n \\paragraph{Models.}\n-We evaluate seven models spanning five architecture families and diverse attention configurations:\n+We evaluate nine models spanning seven architecture families and diverse attention configurations:\n \\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n \\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n \\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n \\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n+\\textbf{CodeLlama-7B} (MHA 1:1, 32 $\\times$ 32 = 1024; profiling only),\n \\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n \\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\n+\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),\n and \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\n+Eight models undergo full constrained evaluation; CodeLlama-7B is characterized by profiling and heterogeneity classification only.\n This selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n \n \\paragraph{Evaluation.}\n@@ -25,7 +28,7 @@ All results use high-resolution profiling (64 sequences $\\times$ 2048 tokens fro\n \n \\paragraph{Compression and constraint.}\n The default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\n-The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2 and Pythia).\n+The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).\n \n \\paragraph{Baselines.}\n We compare against:\n@@ -41,7 +44,7 @@ and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ d\n \\begin{table}[t]\n \\centering\n \\small\n-\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n+\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n \\label{tab:main_results}\n \\begin{tabular}{lccccc}\n \\toprule\n@@ -55,6 +58,7 @@ Yi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\n Llama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\n Mistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\n Gemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\n+Phi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\\\\n Pythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n \\bottomrule\n \\end{tabular}\n@@ -67,12 +71,14 @@ Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with\n On Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\n Hires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n \n-On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\n+On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite high concentration (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\n On Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n \n On Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\n Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n \n+On Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\\times$ bf16). %exp_id=phi3_medium_constrained_mckp\n+\n Unconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\n See Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n \n@@ -86,28 +92,51 @@ The two approaches are orthogonal and composable: KIVI selects the per-channel s\n However, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.\n Per-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.\n \n+\\subsection{Cross-Architecture Compounding}\n+\\label{sec:compounding_cross}\n+\n+\\begin{figure}[t]\n+\\centering\n+\\includegraphics[width=\\columnwidth]{figures/fig_compounding_curves.pdf}\n+\\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\\times$). All three stay near-baseline for $k{\\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\\approx}96$ due to its 112 KV heads (maximum ${\\sim}96$ eligible for 2-bit assignment).}\n+\\label{fig:compounding_cross}\n+\\end{figure}\n+\n+Figure~\\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.\n+At small $k$ (${\\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\\leq}2.5\\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.\n+\n+Beyond $k{=}8$, divergence is stark.\n+Llama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.\n+Qwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\\times$) and $98.75$ at $k{=}256$ ($10.1\\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.\n+Mistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.\n+\n+These curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\\times$ baseline) is ${\\sim}32$ for Qwen, ${\\sim}64$ for Llama, and ${\\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.\n+\n \\subsection{Downstream Evaluation}\n \\label{sec:downstream}\n \n \\begin{table}[t]\n \\centering\n \\small\n-\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen shows large gains; the remaining models show small degradations or neutrality, tracking PPL results.}\n+\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen values are mean over 3 calibration seeds ($\\pm$1$\\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}\n \\label{tab:downstream}\n \\begin{tabular}{lccccc}\n \\toprule\n Model & ARC-C & HS & PIQA & WG & Avg \\\\\n \\midrule\n-Qwen2.5-7B        & $+$3.2 & $+$4.0 & $+$1.3 & $+$2.0 & $+$2.6 \\\\\n-Yi-1.5-9B        & $-$3.2 & $-$0.6 & $-$0.3 & $+$1.3 & $-$0.8 \\\\\n-Llama-3.1-8B     & $-$2.7 & $-$0.1 & $-$0.7 & $-$0.2 & $-$1.0 \\\\\n-Mistral-7B       & $-$1.2 & $-$0.2 & $+$0.4 & $-$1.0 & $-$0.5 \\\\\n-Gemma-2-9B       & $-$0.2 & $+$0.3 & $-$0.1 & $+$0.8 & $+$0.1 \\\\\n+Qwen2.5-7B        & $+$0.0{\\scriptsize$\\pm$0.4} & $+$4.1{\\scriptsize$\\pm$0.2} & $+$2.0{\\scriptsize$\\pm$0.2} & $+$1.6{\\scriptsize$\\pm$1.2} & $+$1.9 \\\\\n+Yi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\\\\n+Llama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\\\\n+Mistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\\\\n+Gemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\\\\n \\bottomrule\n \\end{tabular}\n \\end{table}\n \n-On Qwen, constrained MCKP improves average 0-shot accuracy by 2.6 pts over uniform (0.686 vs.\\ 0.660), recovering $\\sim$73\\% of the accuracy lost to quantization.\n-The four non-spread models show minor average degradation (Yi $-$0.8, Llama $-$1.0, Mistral $-$0.5, Gemma-2 $+$0.1 pts); Llama is the most systematic, with 0 of 5 tasks showing positive change.\n-ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$3.2, Llama $-$2.7, Mistral $-$1.2, Gemma-2 $-$0.2 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\n-Cross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.\n\\ No newline at end of file\n+On Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\n+The four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\n+ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\n+Cross-dataset evaluation (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) confirms calibration robustness.\n+Long-context evaluation (Appendix~\\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\\times$ bf16 at 2K to $11.15\\times$ at 8K, while constrained MCKP remains stable ($1.11\\times$ to $1.23\\times$).\n+In contrast, Llama-3.1-8B (spike, $t_1/t_5{=}0.85$) shows negligible difference between uniform ($1.08\\times$ bf16) and constrained MCKP ($1.08\\times$) at 8K, consistent with its 2K behavior.\n+The uniform-to-constrained PPL ratio on Qwen thus widens from $1.4\\times$ at 2K to $9.1\\times$ at 8K, while Llama remains flat---long-context stress amplifies the spread-specific benefit of per-head allocation.\n\\ No newline at end of file",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4ad16e44-ad4d-407a-b7ba-d8a56392b10a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bcb5bab1-191d-4a2c-8012-6ab3535c025f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-16T03:30:43.404Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0181rk264KYuiYZAZdY5GMPy`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv && git diff HEAD docs/paper/introduction.tex",
  "description": "Review introduction changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8569fa7-35d3-4f59-9070-0ffd0ddbab6d",
  "isSidechain": false,
  "requestId": "req_011Cb5YKRUHCXftSamqAG3Gb",
  "type": "assistant",
  "uuid": "523a7530-a0ae-4388-823c-37b5ceaa3bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bcb5bab1-191d-4a2c-8012-6ab3535c025f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MV3ryD9mBRdgA8aQf6RSgg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4725,
      "cache_read_input_tokens": 96609,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4725,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 96609,
          "cache_creation_input_tokens": 4725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4725
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

_source line 225 · 2026-05-16T03:30:43.452Z_

<details><summary>↩ Tool result · `toolu_0181rk264KYuiYZAZdY5GMPy`</summary>

```text
diff --git a/docs/paper/introduction.tex b/docs/paper/introduction.tex
index daf4de4..d4efce9 100644
--- a/docs/paper/introduction.tex
+++ b/docs/paper/introduction.tex
@@ -28,18 +28,18 @@ Constrained greedy and MCKP produce identical allocations across all tested arch
 A per-layer brute-force oracle confirms near-optimality: the maximum gap is 0.02 PPL, 0.4\% of the total improvement (\S\ref{sec:solver_equiv}).
 
 However, non-uniform allocation does not help universally.
-On the remaining six models---including Qwen2.5-14B, where the $3.4\times$ increase in head count dilutes spread into flat---constrained MCKP provides no meaningful improvement.
-The difference traces to the \emph{distribution shape} of head sensitivity, not GQA ratio or model scale alone: Qwen-7B's Layer-0 heads form a cluster of high sensitivity across multiple bitwidths (``spread''); Yi-1.5 and Llama have dominant outliers (``spike''); Gemma-2, Mistral, Qwen-14B, and Pythia show near-uniform or diluted sensitivity (``flat'').
+On the remaining eight models---including Qwen2.5-14B, where the $3.4\times$ increase in head count dilutes spread into flat---constrained MCKP provides no meaningful improvement.
+The difference traces to the \emph{distribution shape} of head sensitivity, not GQA ratio or model scale alone: Qwen-7B's Layer-0 heads form a cluster of high sensitivity across multiple bitwidths (``spread''); Yi-1.5, CodeLlama, and Llama have dominant outliers (``spike''); Gemma-2, Mistral, Phi-3-medium, Qwen-14B, and Pythia show near-uniform or diluted sensitivity (``flat'').
 
 This motivates a question prior work does not address: \emph{when} should a practitioner use per-head mixed-precision quantization?
-We propose a joint empirical decision rule based on concentration and distribution shape (\S\ref{sec:heterogeneity}) that correctly classifies all seven evaluated models (7/7), including a within-family scale contrast.
+We propose a joint empirical decision rule based on concentration and distribution shape (\S\ref{sec:heterogeneity}) that correctly classifies all eight fully evaluated models (8/8; CodeLlama's spike predicted by profiling alone), including a within-family scale contrast.
 Yi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen-7B's, but its single-outlier spike has no cross-bitwidth gradient, so MCKP cannot redistribute budget.
 
 Our contributions are:
 \begin{enumerate}[nosep]
 \item We identify 2-bit distortion compounding as a major contributing factor in the degradation observed under unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a single cardinality constraint on 2-bit assignments suffices to prevent it, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 10.91 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
 
-\item RateQuant~\cite{zuo2026ratequant} formalized per-head MCKP and proved greedy optimality for consecutive integer bit-widths. Our algorithmic contribution is a single cardinality constraint (Eq.~\ref{eq:constraint}); the scientific contribution is the systematic finding that this constraint suffices to prevent compounding, yet six of seven tested models do not benefit from non-uniform allocation---the constraint renders solver choice irrelevant, with constrained greedy and MCKP producing equivalent allocations across all tested architectures (\S\ref{sec:solver_equiv}).
+\item RateQuant~\cite{zuo2026ratequant} formalized per-head MCKP and proved greedy optimality for consecutive integer bit-widths. Our algorithmic contribution is a single cardinality constraint (Eq.~\ref{eq:constraint}); the scientific contribution is the systematic finding that this constraint suffices to prevent compounding, yet eight of nine tested models do not benefit from non-uniform allocation---the constraint renders solver choice irrelevant, with constrained greedy and MCKP producing equivalent allocations across all tested architectures (\S\ref{sec:solver_equiv}).
 
-\item We provide an empirical characterization of head sensitivity heterogeneity across seven models, revealing three distribution shapes (spread, spike, flat) that predict allocation benefit. Concentration and $t_1/t_5$ ratio correctly classify all seven models (7/7), though the spread pattern is observed in only one model ($N{=}1$, Qwen2.5-7B); the suggested thresholds should be treated as preliminary (\S\ref{sec:heterogeneity}).
+\item We provide an empirical characterization of head sensitivity heterogeneity across nine models, revealing three distribution shapes (spread, spike, flat) that predict allocation benefit. Concentration and $t_1/t_5$ ratio correctly classify all eight fully evaluated models (8/8; CodeLlama predicted by profiling), though the spread pattern is observed in only one model ($N{=}1$, Qwen2.5-7B); the suggested thresholds should be treated as preliminary (\S\ref{sec:heterogeneity}).
 \end{enumerate}
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "523a7530-a0ae-4388-823c-37b5ceaa3bba",
  "isSidechain": false,
  "promptId": "d1a8ba68-f6bd-4e5c-b2e2-e61a399781d5",
  "type": "user",
  "uuid": "044c976e-2e22-4eeb-b9ae-bbeffa85b3bd",
  "toolUseResult": {
    "stdout": "diff --git a/docs/paper/introduction.tex b/docs/paper/introduction.tex\nindex daf4de4..d4efce9 100644\n--- a/docs/paper/introduction.tex\n+++ b/docs/paper/introduction.tex\n@@ -28,18 +28,18 @@ Constrained greedy and MCKP produce identical allocations across all tested arch\n A per-layer brute-force oracle confirms near-optimality: the maximum gap is 0.02 PPL, 0.4\\% of the total improvement (\\S\\ref{sec:solver_equiv}).\n \n However, non-uniform allocation does not help universally.\n-On the remaining six models---including Qwen2.5-14B, where the $3.4\\times$ increase in head count dilutes spread into flat---constrained MCKP provides no meaningful improvement.\n-The difference traces to the \\emph{distribution shape} of head sensitivity, not GQA ratio or model scale alone: Qwen-7B's Layer-0 heads form a cluster of high sensitivity across multiple bitwidths (``spread''); Yi-1.5 and Llama have dominant outliers (``spike''); Gemma-2, Mistral, Qwen-14B, and Pythia show near-uniform or diluted sensitivity (``flat'').\n+On the remaining eight models---including Qwen2.5-14B, where the $3.4\\times$ increase in head count dilutes spread into flat---constrained MCKP provides no meaningful improvement.\n+The difference traces to the \\emph{distribution shape} of head sensitivity, not GQA ratio or model scale alone: Qwen-7B's Layer-0 heads form a cluster of high sensitivity across multiple bitwidths (``spread''); Yi-1.5, CodeLlama, and Llama have dominant outliers (``spike''); Gemma-2, Mistral, Phi-3-medium, Qwen-14B, and Pythia show near-uniform or diluted sensitivity (``flat'').\n \n This motivates a question prior work does not address: \\emph{when} should a practitioner use per-head mixed-precision quantization?\n-We propose a joint empirical decision rule based on concentration and distribution shape (\\S\\ref{sec:heterogeneity}) that correctly classifies all seven evaluated models (7/7), including a within-family scale contrast.\n+We propose a joint empirical decision rule based on concentration and distribution shape (\\S\\ref{sec:heterogeneity}) that correctly classifies all eight fully evaluated models (8/8; CodeLlama's spike predicted by profiling alone), including a within-family scale contrast.\n Yi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen-7B's, but its single-outlier spike has no cross-bitwidth gradient, so MCKP cannot redistribute budget.\n \n Our contributions are:\n \\begin{enumerate}[nosep]\n \\item We identify 2-bit distortion compounding as a major contributing factor in the degradation observed under unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a single cardinality constraint on 2-bit assignments suffices to prevent it, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 10.91 (constrained) at $4\\times$ compression (\\S\\ref{sec:compounding}, \\S\\ref{sec:experiments}).\n \n-\\item RateQuant~\\cite{zuo2026ratequant} formalized per-head MCKP and proved greedy optimality for consecutive integer bit-widths. Our algorithmic contribution is a single cardinality constraint (Eq.~\\ref{eq:constraint}); the scientific contribution is the systematic finding that this constraint suffices to prevent compounding, yet six of seven tested models do not benefit from non-uniform allocation---the constraint renders solver choice irrelevant, with constrained greedy and MCKP producing equivalent allocations across all tested architectures (\\S\\ref{sec:solver_equiv}).\n+\\item RateQuant~\\cite{zuo2026ratequant} formalized per-head MCKP and proved greedy optimality for consecutive integer bit-widths. Our algorithmic contribution is a single cardinality constraint (Eq.~\\ref{eq:constraint}); the scientific contribution is the systematic finding that this constraint suffices to prevent compounding, yet eight of nine tested models do not benefit from non-uniform allocation---the constraint renders solver choice irrelevant, with constrained greedy and MCKP producing equivalent allocations across all tested architectures (\\S\\ref{sec:solver_equiv}).\n \n-\\item We provide an empirical characterization of head sensitivity heterogeneity across seven models, revealing three distribution shapes (spread, spike, flat) that predict allocation benefit. Concentration and $t_1/t_5$ ratio correctly classify all seven models (7/7), though the spread pattern is observed in only one model ($N{=}1$, Qwen2.5-7B); the suggested thresholds should be treated as preliminary (\\S\\ref{sec:heterogeneity}).\n+\\item We provide an empirical characterization of head sensitivity heterogeneity across nine models, revealing three distribution shapes (spread, spike, flat) that predict allocation benefit. Concentration and $t_1/t_5$ ratio correctly classify all eight fully evaluated models (8/8; CodeLlama predicted by profiling), though the spread pattern is observed in only one model ($N{=}1$, Qwen2.5-7B); the suggested thresholds should be treated as preliminary (\\S\\ref{sec:heterogeneity}).\n \\end{enumerate}",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "523a7530-a0ae-4388-823c-37b5ceaa3bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bcb5bab1-191d-4a2c-8012-6ab3535c025f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 226_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_paper_reviewer_fixes_batch2_20260516T031211]: Worker worker_paper_reviewer_fixes_batch2_20260516T031211 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "044c976e-2e22-4eeb-b9ae-bbeffa85b3bd",
  "sessionId": "bcb5bab1-191d-4a2c-8012-6ab3535c025f"
}
```

---


### Runtime record

_source line 227_

```json
{
  "type": "ai-title",
  "aiTitle": "Review loop 13: constrained MCKP results and paper consistency",
  "sessionId": "bcb5bab1-191d-4a2c-8012-6ab3535c025f"
}
```

---


### Tool call

_source line 228 · 2026-05-16T03:30:47.500Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FMirNqtXaqGfZeQWi9ez16`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv && git diff HEAD docs/paper/conclusion.tex",
  "description": "Review conclusion changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "044c976e-2e22-4eeb-b9ae-bbeffa85b3bd",
  "isSidechain": false,
  "requestId": "req_011Cb5YKmrsQ58Nwqv4SufVr",
  "type": "assistant",
  "uuid": "ee8b2e49-5df1-490b-8d25-96f6fbf4882b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bcb5bab1-191d-4a2c-8012-6ab3535c025f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYbiMZY5joGbbVgmDPGY1D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6908,
      "cache_read_input_tokens": 101334,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6908,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 101334,
          "cache_creation_input_tokens": 6908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6908
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

_source line 229 · 2026-05-16T03:30:47.572Z_

<details><summary>↩ Tool result · `toolu_01FMirNqtXaqGfZeQWi9ez16`</summary>

```text
diff --git a/docs/paper/conclusion.tex b/docs/paper/conclusion.tex
index ce55381..31565ec 100644
--- a/docs/paper/conclusion.tex
+++ b/docs/paper/conclusion.tex
@@ -2,23 +2,23 @@
 
 Per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.
 On Qwen2.5-7B, limiting 2-bit heads to $k{\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\%) at $4\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.
-Whether non-uniform allocation helps depends on the \emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2, Qwen-14B, Pythia) patterns show no benefit.
-An empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all seven evaluated models (7/7), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.
+Whether non-uniform allocation helps depends on the \emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, CodeLlama, Llama) and flat (Mistral, Gemma-2, Phi-3-medium, Qwen-14B, Pythia) patterns show no benefit.
+An empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all eight fully evaluated models (8/8; CodeLlama's spike predicted by profiling alone), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.
 Extending to 70B+ models, production inference engines, and per-side K/V cardinality constraints (Appendix~\ref{sec:kv_separation}) are natural next steps.
 
 \section*{Limitations}
 
 \paragraph{$N{=}1$ spread.}
-The spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\geq 0.50$, $t_1/t_5 \leq 0.70$) are calibrated on seven models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.
+The spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\geq 0.50$, $t_1/t_5 \leq 0.70$) are calibrated on nine models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.
 
 \paragraph{Model scale.}
-The largest model evaluated is 14B parameters (384 heads). The Qwen-7B/14B contrast suggests that concentration dilutes with increasing head count, which may make spread less likely at larger scales; this trend is a hypothesis, not a confirmed finding.
+The largest model evaluated is 14B parameters (up to 400 heads). The Qwen-7B/14B contrast suggests that concentration dilutes with increasing head count, which may make spread less likely at larger scales; this trend is a hypothesis, not a confirmed finding.
 
 \paragraph{Runtime.}
 All latency measurements use PyTorch-level per-head \texttt{quantize}/\texttt{dequantize} dispatch and do not represent optimized CUDA kernel performance. The overhead reported in Appendix~\ref{sec:runtime} is an upper bound on the mixed-precision penalty; production inference engines with fused attention kernels would likely narrow this gap. No real-kernel latency benchmarks are reported.
 
 \paragraph{Downstream scope.}
-Downstream evaluation covers four 0-shot classification tasks (ARC-C, HellaSwag, PIQA, WinoGrande). Generation tasks (summarization, translation, long-form QA) are not evaluated, and no confidence intervals are reported for the current single-seed results.
+Downstream evaluation covers four 0-shot classification tasks (ARC-C, HellaSwag, PIQA, WinoGrande). For HellaSwag, we report raw accuracy (\texttt{acc}) rather than length-normalized accuracy (\texttt{acc\_norm}). Generation tasks (summarization, translation, long-form QA) are not evaluated, and no confidence intervals are reported for the current single-seed results.
 
 \paragraph{Calibration domain.}
 Cross-dataset stability is verified only between WikiText-2 and C4 (96--97\% bit-assignment agreement); other domains (code, dialogue, multilingual) are untested.
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee8b2e49-5df1-490b-8d25-96f6fbf4882b",
  "isSidechain": false,
  "promptId": "d1a8ba68-f6bd-4e5c-b2e2-e61a399781d5",
  "type": "user",
  "uuid": "29bdcaf9-6074-4184-9d97-765c4f315b20",
  "toolUseResult": {
    "stdout": "diff --git a/docs/paper/conclusion.tex b/docs/paper/conclusion.tex\nindex ce55381..31565ec 100644\n--- a/docs/paper/conclusion.tex\n+++ b/docs/paper/conclusion.tex\n@@ -2,23 +2,23 @@\n \n Per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \\{2, 4, 8, 16\\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.\n On Qwen2.5-7B, limiting 2-bit heads to $k{\\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\\%) at $4\\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.\n-Whether non-uniform allocation helps depends on the \\emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2, Qwen-14B, Pythia) patterns show no benefit.\n-An empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all seven evaluated models (7/7), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.\n+Whether non-uniform allocation helps depends on the \\emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, CodeLlama, Llama) and flat (Mistral, Gemma-2, Phi-3-medium, Qwen-14B, Pythia) patterns show no benefit.\n+An empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all eight fully evaluated models (8/8; CodeLlama's spike predicted by profiling alone), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.\n Extending to 70B+ models, production inference engines, and per-side K/V cardinality constraints (Appendix~\\ref{sec:kv_separation}) are natural next steps.\n \n \\section*{Limitations}\n \n \\paragraph{$N{=}1$ spread.}\n-The spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\\geq 0.50$, $t_1/t_5 \\leq 0.70$) are calibrated on seven models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.\n+The spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\\geq 0.50$, $t_1/t_5 \\leq 0.70$) are calibrated on nine models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.\n \n \\paragraph{Model scale.}\n-The largest model evaluated is 14B parameters (384 heads). The Qwen-7B/14B contrast suggests that concentration dilutes with increasing head count, which may make spread less likely at larger scales; this trend is a hypothesis, not a confirmed finding.\n+The largest model evaluated is 14B parameters (up to 400 heads). The Qwen-7B/14B contrast suggests that concentration dilutes with increasing head count, which may make spread less likely at larger scales; this trend is a hypothesis, not a confirmed finding.\n \n \\paragraph{Runtime.}\n All latency measurements use PyTorch-level per-head \\texttt{quantize}/\\texttt{dequantize} dispatch and do not represent optimized CUDA kernel performance. The overhead reported in Appendix~\\ref{sec:runtime} is an upper bound on the mixed-precision penalty; production inference engines with fused attention kernels would likely narrow this gap. No real-kernel latency benchmarks are reported.\n \n \\paragraph{Downstream scope.}\n-Downstream evaluation covers four 0-shot classification tasks (ARC-C, HellaSwag, PIQA, WinoGrande). Generation tasks (summarization, translation, long-form QA) are not evaluated, and no confidence intervals are reported for the current single-seed results.\n+Downstream evaluation covers four 0-shot classification tasks (ARC-C, HellaSwag, PIQA, WinoGrande). For HellaSwag, we report raw accuracy (\\texttt{acc}) rather than length-normalized accuracy (\\texttt{acc\\_norm}). Generation tasks (summarization, translation, long-form QA) are not evaluated, and no confidence intervals are reported for the current single-seed results.\n \n \\paragraph{Calibration domain.}\n Cross-dataset stability is verified only between WikiText-2 and C4 (96--97\\% bit-assignment agreement); other domains (code, dialogue, multilingual) are untested.",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ee8b2e49-5df1-490b-8d25-96f6fbf4882b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bcb5bab1-191d-4a2c-8012-6ab3535c025f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-16T03:30:47.965Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0167gjADNQzeZoTLitnq9e57`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv && git diff HEAD docs/paper/method.tex",
  "description": "Review method changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29bdcaf9-6074-4184-9d97-765c4f315b20",
  "isSidechain": false,
  "requestId": "req_011Cb5YKmrsQ58Nwqv4SufVr",
  "type": "assistant",
  "uuid": "f3b77e7c-db1b-4af6-8061-172864139a79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bcb5bab1-191d-4a2c-8012-6ab3535c025f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYbiMZY5joGbbVgmDPGY1D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6908,
      "cache_read_input_tokens": 101334,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6908,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 101334,
          "cache_creation_input_tokens": 6908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6908
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

_source line 231 · 2026-05-16T03:30:48.014Z_

<details><summary>↩ Tool result · `toolu_0167gjADNQzeZoTLitnq9e57`</summary>

```text
diff --git a/docs/paper/method.tex b/docs/paper/method.tex
index e337183..b425423 100644
--- a/docs/paper/method.tex
+++ b/docs/paper/method.tex
@@ -21,7 +21,8 @@ Moreover, as we show in \S\ref{sec:compounding}, the objective itself is not wel
 \subsection{PPL-based Per-Head Profiling}
 \label{sec:profiling}
 
-We profile each KV head independently by quantizing it to each $b \in \mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\times$ 2048 tokens from WikiText-2 train.
+We use symmetric per-channel quantization with per-head granularity: each KV head is independently quantized to one of the candidate bit-widths $\mathcal{B} = \{2, 4, 8, 16\}$, without per-token scaling.
+We profile each head by quantizing it to each $b \in \mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\times$ 2048 tokens from WikiText-2 train.
 This yields a distortion table of $H \times |\mathcal{B}|$ entries that serves as input to the solver.
 
 The optimization in Eq.~\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\sum_h d_h(b_h)$.
@@ -31,29 +32,19 @@ At 2-bit, however, individual distortions are orders of magnitude larger, and th
 \subsection{Compounding Effect}
 \label{sec:compounding}
 
-When many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively.
-The mechanism is straightforward: each head's quantized output feeds into the residual stream, and truncation errors from multiple 2-bit heads accumulate through subsequent layers.
-When the number of 2-bit heads is small, these errors are absorbed by the remaining high-precision heads.
-As the count grows, cumulative errors exceed the capacity of the residual stream to compensate, and PPL degrades super-linearly.
-
-\begin{figure}[t]
-\centering
-\includegraphics[width=\columnwidth]{figures/fig2_compounding_curve.pdf}
-\caption{PPL on Qwen2.5-7B ($4\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}
-\label{fig:compounding}
-\end{figure}
+When many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively: truncation errors from multiple 2-bit heads accumulate through the residual stream, and once their count exceeds the network's capacity to compensate, PPL degrades super-linearly.
 
 Unconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.
 On Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).
 Standard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \approx 0$, so most 2-bit assignments appear free to the additive objective.
 The resulting additive prediction is $\sum_h d_h(b_h) + \text{baseline} \approx 11$ PPL---$3\text{--}4\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.
 
-This compounding is specific to 2-bit quantization.
+This compounding is specific to 2-bit quantization and is \emph{super-additive}: quantizing the top-$k$ most sensitive heads to 2-bit simultaneously produces PPL $1.56\times$ the sum of their individual distortions at $k{=}8$, growing to $4.89\times$ at $k{=}64$.
+A random-$k$ control confirms that sensitivity ordering matters: at $k{=}64$, random selection yields 55.94 PPL vs.\ 22.95 for top-$k$, because random draws are more likely to include high-distortion heads that amplify compounding.
 At 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).
 The qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.
 
-Figure~\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\times$ compression.
-The curve is U-shaped: at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond this point, compounding drives PPL upward, reaching 35.35 at $k{=}75$.
+The relationship between $k$ and PPL is U-shaped (Figure~\ref{fig:compounding}, Appendix~\ref{sec:compounding_appendix}): at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 10.89 at $k{=}8$; beyond $k{=}8$, compounding drives PPL upward.
 
 \subsection{Cardinality Constraint}
 \label{sec:cardinality}
@@ -69,18 +60,15 @@ For Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\sim$7\% of heads).
 
 The constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.
 
-A natural question is whether Layer-0 heads require explicit protection, since attention heads in the first layer are known to carry disproportionate importance.
-On Qwen2.5-7B, the profiler assigns very high distortion to Layer-0 heads at 2-bit: L0H0 increases PPL by 31.9\% relative to the bf16 baseline (9.81 $\to$ 12.94), L0H2 by 23.2\% (9.81 $\to$ 12.09), L0H3 by 11.7\% (9.81 $\to$ 10.96).
-These values are large enough that no solver would assign 2-bit to Layer-0 under any reasonable budget.
-We verify this empirically: running the solver with and without manual Layer-0 exclusion produces identical allocations across all 112 heads.
-No manual exclusion rule is needed; the profiler signal is sufficient.
+One might expect Layer-0 heads to require explicit protection.
+On Qwen2.5-7B, however, the profiler assigns very high 2-bit distortion to Layer-0 heads (L0H0: $+$31.9\%, L0H2: $+$23.2\%, L0H3: $+$11.7\% relative to bf16), so no solver would assign them 2-bit under any reasonable budget.
+Running the solver with and without manual Layer-0 exclusion produces identical allocations; no manual rule is needed.
 
 \paragraph{Restoring additivity.}
-The cardinality constraint resolves a tension between the profiling methodology (\S\ref{sec:profiling}) and the compounding effect (\S\ref{sec:compounding}): the additive objective in Eq.~\eqref{eq:objective} treats per-head distortions as independent, but 2-bit compounding violates this assumption once many 2-bit heads coexist.
-Restricting the number of 2-bit heads to $k \ll H$ pushes the allocation back into a near-additive regime, where interactions between simultaneously quantized 2-bit heads are small enough that the profiler's additive prediction agrees with measured PPL.
-For Qwen2.5-7B, $k{=}8$ corresponds to $\sim$7\% of the 112 heads---few enough that compounding contributes negligibly.
-This is consistent with the U-shaped curve in Figure~\ref{fig:compounding}: the minimum at $k{=}8$ lies in the interval where the additive assumption is still a reasonable approximation, before compounding inflates true PPL above the additive prediction.
-It also explains the gap between constrained and unconstrained solvers in Table~\ref{tab:solver_equiv}: constrained greedy operates inside the additive regime and attains 11.23 PPL, matching the additive estimate $\sum_h d_h(b_h) + \text{baseline} \approx 11$; unconstrained solvers extrapolate the same additive model outside its valid range and miss true PPL by $3\text{--}4\times$ (32.45 for greedy and 36.92 for MCKP, against the $\approx$11 they would predict).
+The additive objective treats per-head distortions as independent, but 2-bit compounding violates this once many 2-bit heads coexist.
+Restricting 2-bit heads to $k \ll H$ pushes the allocation back into a near-additive regime where the profiler's prediction agrees with measured PPL.
+For Qwen2.5-7B, $k{=}8$ ($\sim$7\% of heads) is few enough that compounding contributes negligibly, consistent with the U-shaped curve minimum (Figure~\ref{fig:compounding}).
+This explains the constrained--unconstrained gap in Table~\ref{tab:solver_equiv}: constrained greedy operates inside the additive regime (10.91 PPL, matching the ${\approx}11$ additive estimate), while unconstrained solvers extrapolate outside it and miss true PPL by $3\text{--}4\times$.
 
 \subsection{Solver Equivalence}
 \label{sec:solver_equiv}
@@ -97,36 +85,21 @@ Solver & Constraint & PPL & \multicolumn{3}{c}{Bit distribution} \\
 \midrule
 Greedy & None & 32.45 & 68 & 30 & 14 \\
 MCKP & None & 36.92 & 75 & 33 & 4 \\
-Greedy & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
-MCKP & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
+Greedy & $k{\leq}8$ & 10.91 & 8 & 100 & 4 \\
+MCKP & $k{\leq}8$ & 10.91 & 8 & 100 & 4 \\
 Uniform & --- & 15.45 & 0 & 112 & 0 \\
 \bottomrule
 \end{tabular}
 \end{table}
-\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\times$ 2048 tok) achieves 10.91 (Appendix~\ref{sec:profiling_resolution}).}
+\footnotetext{Constrained results use high-resolution profiling; unconstrained rows use standard-resolution profiling to illustrate the failure mode (the exact PPL is irrelevant---any unconstrained allocation fails catastrophically).}
 
-With the cardinality constraint in place, greedy and MCKP produce identical results---not approximately, but exactly.
-Table~\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.
+With the cardinality constraint, greedy and MCKP produce identical results (Table~\ref{tab:solver_equiv}): same PPL (10.91), same bit distribution on Qwen2.5-7B.
 
 \paragraph{Empirical observation.}
-When the cardinality budget satisfies $k \ll H$ and the top-$k$ heads ranked by marginal benefit $d_h(4) - d_h(2)$ contain no ties, constrained greedy and constrained MCKP produce identical per-head allocations.
-We verify this across three architectures (Qwen2.5-7B: 112/112, Llama-3.1-8B: 256/256, Mistral-7B-v0.3: 255/256 heads identical; see per-head verification below).
-Intuitively, the constraint restricts the feasible set to a small combinatorial space in which the only decision is which $k$ heads to assign 2-bit; the marginal-benefit ordering determines this set uniquely up to ties, so greedy's local choice coincides with the MCKP global optimum.
-
-We verify this at the per-head level across three models:
-
-\begin{itemize}[nosep]
-\item \textbf{Qwen2.5-7B:} 112/112 heads receive identical bit-widths.
-\item \textbf{Llama-3.1-8B:} 256/256 heads identical.
-\item \textbf{Mistral-7B-v0.3:} 255/256 heads identical. The single difference is a zero-distortion tie between two heads at 4-bit and 8-bit, with no PPL impact.
-\end{itemize}
-
-The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal.
-Without it, greedy cascades into excessive 2-bit allocation: each additional 2-bit head looks locally beneficial (freeing budget) but contributes to the compounding effect that degrades global PPL.
-The cardinality constraint breaks this cascade by capping the number of 2-bit heads, aligning local and global optima.
-
-The practical implication is that practitioners can use the simpler $O(H \log H)$ greedy algorithm instead of MCKP without sacrificing optimality.
+When $k \ll H$ and the top-$k$ heads ranked by marginal benefit $d_h(4) - d_h(2)$ contain no ties, constrained greedy and MCKP produce identical per-head allocations.
+The constraint restricts the feasible set so that the only decision is which $k$ heads to assign 2-bit; the marginal-benefit ordering determines this uniquely, so greedy's local choice coincides with the global optimum.
+We verify this across three architectures: Qwen2.5-7B (112/112 heads identical), Llama-3.1-8B (256/256), Mistral-7B-v0.3 (255/256; the single difference is a zero-distortion tie with no PPL impact).
+Without the constraint, greedy cascades into excessive 2-bit allocation, as each additional 2-bit head looks locally beneficial but contributes to compounding.
+Practitioners can therefore use the simpler $O(H \log H)$ greedy algorithm without sacrificing optimality.
 
-To verify that constrained MCKP is near-optimal, we perform a per-layer brute-force oracle on Qwen2.5-7B: for each of the 28 layers, we enumerate all $4^4{=}256$ bit-width assignments to the 4 KV heads and select the allocation minimizing per-layer PPL.
-Of the 8 layers with non-trivial (non-all-4-bit) allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.018 PPL---0.4\% of the constrained-vs-uniform improvement (4.53 PPL)---due to within-layer 2-bit head position swaps with no change to the per-layer bit budget.
-Combined with the greedy--MCKP equivalence above, this closes the optimality chain: a simple $O(H \log H)$ greedy algorithm (runtime 0.005s) produces allocations within 0.02 PPL of the brute-force optimum.
\ No newline at end of file
+A per-layer brute-force oracle on Qwen2.5-7B confirms near-optimality: of 8 layers with non-trivial allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.018 PPL (0.4\% of the total improvement), closing the optimality chain from greedy through MCKP to brute-force.
\ No newline at end of file
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3b77e7c-db1b-4af6-8061-172864139a79",
  "isSidechain": false,
  "promptId": "d1a8ba68-f6bd-4e5c-b2e2-e61a399781d5",
  "type": "user",
  "uuid": "ea999d32-7fa9-4850-af41-e77e6937a532",
  "toolUseResult": {
    "stdout": "diff --git a/docs/paper/method.tex b/docs/paper/method.tex\nindex e337183..b425423 100644\n--- a/docs/paper/method.tex\n+++ b/docs/paper/method.tex\n@@ -21,7 +21,8 @@ Moreover, as we show in \\S\\ref{sec:compounding}, the objective itself is not wel\n \\subsection{PPL-based Per-Head Profiling}\n \\label{sec:profiling}\n \n-We profile each KV head independently by quantizing it to each $b \\in \\mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\\times$ 2048 tokens from WikiText-2 train.\n+We use symmetric per-channel quantization with per-head granularity: each KV head is independently quantized to one of the candidate bit-widths $\\mathcal{B} = \\{2, 4, 8, 16\\}$, without per-token scaling.\n+We profile each head by quantizing it to each $b \\in \\mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\\times$ 2048 tokens from WikiText-2 train.\n This yields a distortion table of $H \\times |\\mathcal{B}|$ entries that serves as input to the solver.\n \n The optimization in Eq.~\\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\\sum_h d_h(b_h)$.\n@@ -31,29 +32,19 @@ At 2-bit, however, individual distortions are orders of magnitude larger, and th\n \\subsection{Compounding Effect}\n \\label{sec:compounding}\n \n-When many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively.\n-The mechanism is straightforward: each head's quantized output feeds into the residual stream, and truncation errors from multiple 2-bit heads accumulate through subsequent layers.\n-When the number of 2-bit heads is small, these errors are absorbed by the remaining high-precision heads.\n-As the count grows, cumulative errors exceed the capacity of the residual stream to compensate, and PPL degrades super-linearly.\n-\n-\\begin{figure}[t]\n-\\centering\n-\\includegraphics[width=\\columnwidth]{figures/fig2_compounding_curve.pdf}\n-\\caption{PPL on Qwen2.5-7B ($4\\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}\n-\\label{fig:compounding}\n-\\end{figure}\n+When many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively: truncation errors from multiple 2-bit heads accumulate through the residual stream, and once their count exceeds the network's capacity to compensate, PPL degrades super-linearly.\n \n Unconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.\n On Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).\n Standard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \\approx 0$, so most 2-bit assignments appear free to the additive objective.\n The resulting additive prediction is $\\sum_h d_h(b_h) + \\text{baseline} \\approx 11$ PPL---$3\\text{--}4\\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.\n \n-This compounding is specific to 2-bit quantization.\n+This compounding is specific to 2-bit quantization and is \\emph{super-additive}: quantizing the top-$k$ most sensitive heads to 2-bit simultaneously produces PPL $1.56\\times$ the sum of their individual distortions at $k{=}8$, growing to $4.89\\times$ at $k{=}64$.\n+A random-$k$ control confirms that sensitivity ordering matters: at $k{=}64$, random selection yields 55.94 PPL vs.\\ 22.95 for top-$k$, because random draws are more likely to include high-distortion heads that amplify compounding.\n At 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).\n The qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.\n \n-Figure~\\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\\times$ compression.\n-The curve is U-shaped: at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond this point, compounding drives PPL upward, reaching 35.35 at $k{=}75$.\n+The relationship between $k$ and PPL is U-shaped (Figure~\\ref{fig:compounding}, Appendix~\\ref{sec:compounding_appendix}): at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 10.89 at $k{=}8$; beyond $k{=}8$, compounding drives PPL upward.\n \n \\subsection{Cardinality Constraint}\n \\label{sec:cardinality}\n@@ -69,18 +60,15 @@ For Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\\sim$7\\% of heads).\n \n The constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.\n \n-A natural question is whether Layer-0 heads require explicit protection, since attention heads in the first layer are known to carry disproportionate importance.\n-On Qwen2.5-7B, the profiler assigns very high distortion to Layer-0 heads at 2-bit: L0H0 increases PPL by 31.9\\% relative to the bf16 baseline (9.81 $\\to$ 12.94), L0H2 by 23.2\\% (9.81 $\\to$ 12.09), L0H3 by 11.7\\% (9.81 $\\to$ 10.96).\n-These values are large enough that no solver would assign 2-bit to Layer-0 under any reasonable budget.\n-We verify this empirically: running the solver with and without manual Layer-0 exclusion produces identical allocations across all 112 heads.\n-No manual exclusion rule is needed; the profiler signal is sufficient.\n+One might expect Layer-0 heads to require explicit protection.\n+On Qwen2.5-7B, however, the profiler assigns very high 2-bit distortion to Layer-0 heads (L0H0: $+$31.9\\%, L0H2: $+$23.2\\%, L0H3: $+$11.7\\% relative to bf16), so no solver would assign them 2-bit under any reasonable budget.\n+Running the solver with and without manual Layer-0 exclusion produces identical allocations; no manual rule is needed.\n \n \\paragraph{Restoring additivity.}\n-The cardinality constraint resolves a tension between the profiling methodology (\\S\\ref{sec:profiling}) and the compounding effect (\\S\\ref{sec:compounding}): the additive objective in Eq.~\\eqref{eq:objective} treats per-head distortions as independent, but 2-bit compounding violates this assumption once many 2-bit heads coexist.\n-Restricting the number of 2-bit heads to $k \\ll H$ pushes the allocation back into a near-additive regime, where interactions between simultaneously quantized 2-bit heads are small enough that the profiler's additive prediction agrees with measured PPL.\n-For Qwen2.5-7B, $k{=}8$ corresponds to $\\sim$7\\% of the 112 heads---few enough that compounding contributes negligibly.\n-This is consistent with the U-shaped curve in Figure~\\ref{fig:compounding}: the minimum at $k{=}8$ lies in the interval where the additive assumption is still a reasonable approximation, before compounding inflates true PPL above the additive prediction.\n-It also explains the gap between constrained and unconstrained solvers in Table~\\ref{tab:solver_equiv}: constrained greedy operates inside the additive regime and attains 11.23 PPL, matching the additive estimate $\\sum_h d_h(b_h) + \\text{baseline} \\approx 11$; unconstrained solvers extrapolate the same additive model outside its valid range and miss true PPL by $3\\text{--}4\\times$ (32.45 for greedy and 36.92 for MCKP, against the $\\approx$11 they would predict).\n+The additive objective treats per-head distortions as independent, but 2-bit compounding violates this once many 2-bit heads coexist.\n+Restricting 2-bit heads to $k \\ll H$ pushes the allocation back into a near-additive regime where the profiler's prediction agrees with measured PPL.\n+For Qwen2.5-7B, $k{=}8$ ($\\sim$7\\% of heads) is few enough that compounding contributes negligibly, consistent with the U-shaped curve minimum (Figure~\\ref{fig:compounding}).\n+This explains the constrained--unconstrained gap in Table~\\ref{tab:solver_equiv}: constrained greedy operates inside the additive regime (10.91 PPL, matching the ${\\approx}11$ additive estimate), while unconstrained solvers extrapolate outside it and miss true PPL by $3\\text{--}4\\times$.\n \n \\subsection{Solver Equivalence}\n \\label{sec:solver_equiv}\n@@ -97,36 +85,21 @@ Solver & Constraint & PPL & \\multicolumn{3}{c}{Bit distribution} \\\\\n \\midrule\n Greedy & None & 32.45 & 68 & 30 & 14 \\\\\n MCKP & None & 36.92 & 75 & 33 & 4 \\\\\n-Greedy & $k{\\leq}8$ & 11.23 & 8 & 100 & 4 \\\\\n-MCKP & $k{\\leq}8$ & 11.23 & 8 & 100 & 4 \\\\\n+Greedy & $k{\\leq}8$ & 10.91 & 8 & 100 & 4 \\\\\n+MCKP & $k{\\leq}8$ & 10.91 & 8 & 100 & 4 \\\\\n Uniform & --- & 15.45 & 0 & 112 & 0 \\\\\n \\bottomrule\n \\end{tabular}\n \\end{table}\n-\\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\\times$ 2048 tok) achieves 10.91 (Appendix~\\ref{sec:profiling_resolution}).}\n+\\footnotetext{Constrained results use high-resolution profiling; unconstrained rows use standard-resolution profiling to illustrate the failure mode (the exact PPL is irrelevant---any unconstrained allocation fails catastrophically).}\n \n-With the cardinality constraint in place, greedy and MCKP produce identical results---not approximately, but exactly.\n-Table~\\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.\n+With the cardinality constraint, greedy and MCKP produce identical results (Table~\\ref{tab:solver_equiv}): same PPL (10.91), same bit distribution on Qwen2.5-7B.\n \n \\paragraph{Empirical observation.}\n-When the cardinality budget satisfies $k \\ll H$ and the top-$k$ heads ranked by marginal benefit $d_h(4) - d_h(2)$ contain no ties, constrained greedy and constrained MCKP produce identical per-head allocations.\n-We verify this across three architectures (Qwen2.5-7B: 112/112, Llama-3.1-8B: 256/256, Mistral-7B-v0.3: 255/256 heads identical; see per-head verification below).\n-Intuitively, the constraint restricts the feasible set to a small combinatorial space in which the only decision is which $k$ heads to assign 2-bit; the marginal-benefit ordering determines this set uniquely up to ties, so greedy's local choice coincides with the MCKP global optimum.\n-\n-We verify this at the per-head level across three models:\n-\n-\\begin{itemize}[nosep]\n-\\item \\textbf{Qwen2.5-7B:} 112/112 heads receive identical bit-widths.\n-\\item \\textbf{Llama-3.1-8B:} 256/256 heads identical.\n-\\item \\textbf{Mistral-7B-v0.3:} 255/256 heads identical. The single difference is a zero-distortion tie between two heads at 4-bit and 8-bit, with no PPL impact.\n-\\end{itemize}\n-\n-The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal.\n-Without it, greedy cascades into excessive 2-bit allocation: each additional 2-bit head looks locally beneficial (freeing budget) but contributes to the compounding effect that degrades global PPL.\n-The cardinality constraint breaks this cascade by capping the number of 2-bit heads, aligning local and global optima.\n-\n-The practical implication is that practitioners can use the simpler $O(H \\log H)$ greedy algorithm instead of MCKP without sacrificing optimality.\n+When $k \\ll H$ and the top-$k$ heads ranked by marginal benefit $d_h(4) - d_h(2)$ contain no ties, constrained greedy and MCKP produce identical per-head allocations.\n+The constraint restricts the feasible set so that the only decision is which $k$ heads to assign 2-bit; the marginal-benefit ordering determines this uniquely, so greedy's local choice coincides with the global optimum.\n+We verify this across three architectures: Qwen2.5-7B (112/112 heads identical), Llama-3.1-8B (256/256), Mistral-7B-v0.3 (255/256; the single difference is a zero-distortion tie with no PPL impact).\n+Without the constraint, greedy cascades into excessive 2-bit allocation, as each additional 2-bit head looks locally beneficial but contributes to compounding.\n+Practitioners can therefore use the simpler $O(H \\log H)$ greedy algorithm without sacrificing optimality.\n \n-To verify that constrained MCKP is near-optimal, we perform a per-layer brute-force oracle on Qwen2.5-7B: for each of the 28 layers, we enumerate all $4^4{=}256$ bit-width assignments to the 4 KV heads and select the allocation minimizing per-layer PPL.\n-Of the 8 layers with non-trivial (non-all-4-bit) allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.018 PPL---0.4\\% of the constrained-vs-uniform improvement (4.53 PPL)---due to within-layer 2-bit head position swaps with no change to the per-layer bit budget.\n-Combined with the greedy--MCKP equivalence above, this closes the optimality chain: a simple $O(H \\log H)$ greedy algorithm (runtime 0.005s) produces allocations within 0.02 PPL of the brute-force optimum.\n\\ No newline at end of file\n+A per-layer brute-force oracle on Qwen2.5-7B confirms near-optimality: of 8 layers with non-trivial allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.018 PPL (0.4\\% of the total improvement), closing the optimality chain from greedy through MCKP to brute-force.\n\\ No newline at end of file",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f3b77e7c-db1b-4af6-8061-172864139a79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bcb5bab1-191d-4a2c-8012-6ab3535c025f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 232_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_paper_reviewer_fixes_batch2_20260516T031211]: Worker worker_paper_reviewer_fixes_batch2_20260516T031211 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "ea999d32-7fa9-4850-af41-e77e6937a532",
  "sessionId": "bcb5bab1-191d-4a2c-8012-6ab3535c025f"
}
```

---


### Runtime record

_source line 233_

```json
{
  "type": "ai-title",
  "aiTitle": "Review loop 13: constrained MCKP results and paper consistency",
  "sessionId": "bcb5bab1-191d-4a2c-8012-6ab3535c025f"
}
```

---
