# pipeline cell4 s2 eval anova compile v2 — Part 4 of 5

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

[← Part 3](part-003.md) · [Transcript overview](../pipeline-cell4-s2-eval-anova-compile-v2.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/c2/c2679ffe68fc4e6a1e61.json)

## Round 1

### Tool result

_source line 1140 · 2026-05-28T10:00:50.668Z_

<details><summary>↩ Tool result · `toolu_01YL8uoQKtoggHtQb1wRDa8n`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "c2bb5a88-08c1-4ba8-835e-c33fa3c51afa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "under v2 ($n{=}3$), Detach+LN achieves $0.802 \\pm 0.024$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.7$\\,pp vs.\\ Vanilla, $d{=}+2.36$)",
    "newString": "under v2 ($n{=}4$), Detach+LN achieves $0.798 \\pm 0.022$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.2$\\,pp vs.\\ Vanilla, $d{=}+2.31$)",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\\approx}$46\\%). (d)~Gradient norm ratio per layer.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}3$), Detach+LN achieves $0.802 \\pm 0.024$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.7$\\,pp vs.\\ Vanilla, $d{=}+2.36$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (14 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect does not reach significance ($p{=}0.104$) but shows a medium-to-large effect size ($\\eta^2{=}0.180$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.005$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.180$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.060$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\\nInteraction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.60 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.12 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.47 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
    "structuredPatch": [
      {
        "oldStart": 82,
        "oldLines": 7,
        "newStart": 82,
        "newLines": 7,
        "lines": [
          " \\label{fig:gradient_analysis}",
          " \\end{figure}",
          " ",
          "-The Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}3$), Detach+LN achieves $0.802 \\pm 0.024$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.7$\\,pp vs.\\ Vanilla, $d{=}+2.36$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.",
          "+The Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}4$), Detach+LN achieves $0.798 \\pm 0.022$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.2$\\,pp vs.\\ Vanilla, $d{=}+2.31$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.",
          " ",
          " \\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.",
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

_source line 1141_

Now the ANOVA table and surrounding text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "fa9aef47-5127-4d95-901e-601d1cde7c37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNhgnp4JRyiyu7ya8Zbetr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 355,
      "cache_read_input_tokens": 155199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 355
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

_source line 1142_

<details open><summary>🔧 Tool call — Read · `toolu_01AeEN1ABGGivMrrUjzqbU89`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "offset": 132,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "fd582cd3-1825-421c-8c61-e413779b9242",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNhgnp4JRyiyu7ya8Zbetr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 355,
      "cache_read_input_tokens": 155199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 355
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

_source line 1143 · 2026-05-28T10:00:54.191Z_

<details><summary>↩ Tool result · `toolu_01AeEN1ABGGivMrrUjzqbU89`</summary>

```text
132	The $2{\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (14 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.060$, $\eta^2{=}0.253$); the gradient flow main effect does not reach significance ($p{=}0.104$) but shows a medium-to-large effect size ($\eta^2{=}0.180$). We report effect sizes as the primary inferential quantity.
133	
134	The study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\eta^2{=}0.005$) confirms these effects are additive.
135	
136	\textbf{Formal $2{\times}2$ ANOVA.} Table~\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\eta^2{=}0.180$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.
137	
138	\begin{table}[h]
139	\centering
140	\caption{$2{\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.060$).}
141	\label{tab:anova}
142	\begin{tabular}{lcccc}
143	\toprule
144	Source & $F$ & df & $p$ & $\eta^2$ \\
145	\midrule
146	Gradient flow (ON vs.\ OFF) & 3.20 & 1,\,10 & 0.104 & 0.180 \\
147	Normalization (BN vs.\ LN) & 4.49 & 1,\,10 & 0.060 & 0.253 \\
148	Interaction & 0.10 & 1,\,10 & 0.763 & 0.005 \\
149	\bottomrule
150	\end{tabular}
151	\end{table}
152	
153	\textbf{Pairwise effect sizes.} Table~\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).
154	
155	\begin{table}[h]
156	\centering
157	\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}
158	\label{tab:pairwise}
159	\small
160	\begin{tabular}{lc}
161	\toprule
162	Comparison & Cohen's $d$ \\
163	\midrule
164	Cell~1 (Full OCC BN) vs.\ Cell~2 (Full OCC+LN) & $-$1.05 \\
165	Cell~1 vs.\ Cell~3 (Detach OCC) & $-$0.93 \\
166	Cell~1 vs.\ Cell~4 (Detach+LN) & $-$1.60 \\
167	Cell~2 vs.\ Cell~3 & $+$0.25 \\
168	Cell~2 vs.\ Cell~4 & $-$1.12 \\
169	Cell~3 vs.\ Cell~4 & $-$1.47 \\
170	\addlinespace
171	Cell~1 vs.\ Vanilla & $-$0.42 \\
172	Cell~2 vs.\ Vanilla & $+$1.07 \\
173	Cell~3 vs.\ Vanilla & $+$0.88 \\
174	Cell~4 vs.\ Vanilla & $+$2.36 \\
175	\bottomrule
176	\end{tabular}
177	\end{table}
178	
179	\section{Per-Task Factorial Analysis}
180	\label{app:per_task_factorial}
181	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "a430cef9-6723-440b-ae00-a21a629b6c6d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
      "content": "The $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (14 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect does not reach significance ($p{=}0.104$) but shows a medium-to-large effect size ($\\eta^2{=}0.180$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.005$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.180$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.060$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\\nInteraction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.60 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.12 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.47 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n",
      "numLines": 50,
      "startLine": 132,
      "totalLines": 194
    }
  }
}
```

</details>

---


### Tool call

_source line 1144_

<details open><summary>🔧 Tool call — Edit · `toolu_012HhhPs1j3FZdDYt3yP9V94`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "With $n{=}3$--$4$ per cell (14 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect does not reach significance ($p{=}0.104$) but shows a medium-to-large effect size ($\\eta^2{=}0.180$).",
  "new_string": "With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "458d6a18-1783-4d4a-b307-1ff0fff471ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012D1Yk4przVCtyJqG4tdA4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1353,
      "cache_read_input_tokens": 155554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1353
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

_source line 1145 · 2026-05-28T10:01:00.005Z_

<details><summary>↩ Tool result · `toolu_012HhhPs1j3FZdDYt3yP9V94`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "0116dcfb-8147-4f94-a4df-3a9d7c1fd904",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "With $n{=}3$--$4$ per cell (14 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect does not reach significance ($p{=}0.104$) but shows a medium-to-large effect size ($\\eta^2{=}0.180$).",
    "newString": "With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$).",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\\approx}$46\\%). (d)~Gradient norm ratio per layer.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}4$), Detach+LN achieves $0.798 \\pm 0.022$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.2$\\,pp vs.\\ Vanilla, $d{=}+2.31$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (14 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect does not reach significance ($p{=}0.104$) but shows a medium-to-large effect size ($\\eta^2{=}0.180$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.005$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.180$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.060$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\\nInteraction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.60 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.12 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.47 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
    "structuredPatch": [
      {
        "oldStart": 129,
        "oldLines": 7,
        "newStart": 129,
        "newLines": 7,
        "lines": [
          " \\section{Statistical Power Analysis}",
          " \\label{app:stat_power}",
          " ",
          "-The $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (14 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect does not reach significance ($p{=}0.104$) but shows a medium-to-large effect size ($\\eta^2{=}0.180$). We report effect sizes as the primary inferential quantity.",
          "+The $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$). We report effect sizes as the primary inferential quantity.",
          " ",
          " The study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.005$) confirms these effects are additive.",
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

_source line 1146_

<details open><summary>🔧 Tool call — Edit · `toolu_012PcKQoyLsdNXd3MzdHcaCN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "The negligible interaction ($\\eta^2{=}0.005$) confirms",
  "new_string": "The negligible interaction ($\\eta^2{=}0.019$) confirms"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "caabac08-259b-4c98-a43a-2a6a9e1b387e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHPv2wRKdmXZfCQw8asoJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 156907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 1147 · 2026-05-28T10:01:03.941Z_

<details><summary>↩ Tool result · `toolu_012PcKQoyLsdNXd3MzdHcaCN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "65fc763b-c3ad-4f8a-9a88-812d2f283c92",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "The negligible interaction ($\\eta^2{=}0.005$) confirms",
    "newString": "The negligible interaction ($\\eta^2{=}0.019$) confirms",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\\approx}$46\\%). (d)~Gradient norm ratio per layer.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}4$), Detach+LN achieves $0.798 \\pm 0.022$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.2$\\,pp vs.\\ Vanilla, $d{=}+2.31$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.005$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.180$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.060$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\\nInteraction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.60 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.12 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.47 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
    "structuredPatch": [
      {
        "oldStart": 131,
        "oldLines": 7,
        "newStart": 131,
        "newLines": 7,
        "lines": [
          " ",
          " The $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$). We report effect sizes as the primary inferential quantity.",
          " ",
          "-The study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.005$) confirms these effects are additive.",
          "+The study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.019$) confirms these effects are additive.",
          " ",
          " \\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.180$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.",
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

_source line 1148_

<details open><summary>🔧 Tool call — Edit · `toolu_01QgJcKF9BRS8J8C6NqE26y5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "$n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.180$).",
  "new_string": "$n{=}3$--$4$ per cell, 15 total observations). The interaction is negligible ($F(1,11){=}0.21$, $p{=}0.656$, $\\eta^2{=}0.019$), confirming additive main effects. The normalization main effect approaches significance ($F(1,11){=}4.68$, $p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect is medium-sized but non-significant ($F(1,11){=}3.26$, $p{=}0.098$, $\\eta^2{=}0.229$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "d46d600b-69e3-4a4b-bec4-7852a5939b00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TjuhsFtBCx6RdQUhrTEDW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 157308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 231
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

_source line 1149 · 2026-05-28T10:01:10.789Z_

<details><summary>↩ Tool result · `toolu_01QgJcKF9BRS8J8C6NqE26y5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "c5323f86-c8f4-49db-9c5e-b5b3d88e7f9c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "$n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.180$).",
    "newString": "$n{=}3$--$4$ per cell, 15 total observations). The interaction is negligible ($F(1,11){=}0.21$, $p{=}0.656$, $\\eta^2{=}0.019$), confirming additive main effects. The normalization main effect approaches significance ($F(1,11){=}4.68$, $p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect is medium-sized but non-significant ($F(1,11){=}3.26$, $p{=}0.098$, $\\eta^2{=}0.229$).",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\\approx}$46\\%). (d)~Gradient norm ratio per layer.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}4$), Detach+LN achieves $0.798 \\pm 0.022$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.2$\\,pp vs.\\ Vanilla, $d{=}+2.31$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.019$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.180$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.060$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\\nInteraction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.60 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.12 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.47 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
    "structuredPatch": [
      {
        "oldStart": 133,
        "oldLines": 7,
        "newStart": 133,
        "newLines": 7,
        "lines": [
          " ",
          " The study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.019$) confirms these effects are additive.",
          " ",
          "-\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.180$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.",
          "+\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 15 total observations). The interaction is negligible ($F(1,11){=}0.21$, $p{=}0.656$, $\\eta^2{=}0.019$), confirming additive main effects. The normalization main effect approaches significance ($F(1,11){=}4.68$, $p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect is medium-sized but non-significant ($F(1,11){=}3.26$, $p{=}0.098$, $\\eta^2{=}0.229$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.",
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


### Tool call

_source line 1150_

<details open><summary>🔧 Tool call — Edit · `toolu_01BrN9XSf4aY5tvY8uKNtmLS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "the normalization main effect approaches significance ($p{=}0.060$).}",
  "new_string": "the normalization main effect approaches significance ($p{=}0.053$).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "0aa0549f-48f4-4616-b635-6b0648d56252",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JB6LMmdCQ4xXo9FQpmAjbw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 521,
      "cache_read_input_tokens": 157539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 521
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

_source line 1151 · 2026-05-28T10:01:14.827Z_

<details><summary>↩ Tool result · `toolu_01BrN9XSf4aY5tvY8uKNtmLS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "9644c18c-c702-4006-94f2-df7553c6dc47",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "the normalization main effect approaches significance ($p{=}0.060$).}",
    "newString": "the normalization main effect approaches significance ($p{=}0.053$).}",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\\approx}$46\\%). (d)~Gradient norm ratio per layer.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}4$), Detach+LN achieves $0.798 \\pm 0.022$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.2$\\,pp vs.\\ Vanilla, $d{=}+2.31$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.019$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 15 total observations). The interaction is negligible ($F(1,11){=}0.21$, $p{=}0.656$, $\\eta^2{=}0.019$), confirming additive main effects. The normalization main effect approaches significance ($F(1,11){=}4.68$, $p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect is medium-sized but non-significant ($F(1,11){=}3.26$, $p{=}0.098$, $\\eta^2{=}0.229$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.060$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\\nInteraction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.60 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.12 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.47 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
    "structuredPatch": [
      {
        "oldStart": 137,
        "oldLines": 7,
        "newStart": 137,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{table}[h]",
          " \\centering",
          "-\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.060$).}",
          "+\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.053$).}",
          " \\label{tab:anova}",
          " \\begin{tabular}{lcccc}",
          " \\toprule"
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

_source line 1152_

Now the ANOVA table rows.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "5685166c-4168-4792-838a-7fc744b2659d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGNoHwL6YGEb4nct9W7tLH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 158060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 444
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

_source line 1153_

<details open><summary>🔧 Tool call — Edit · `toolu_01L5Rz7MZHXqXqn4a1jc1WEW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "Gradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\\nInteraction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\",
  "new_string": "Gradient flow (ON vs.\\ OFF) & 3.26 & 1,\\,11 & 0.098 & 0.229 \\\\\nNormalization (BN vs.\\ LN) & 4.68 & 1,\\,11 & 0.053 & 0.298 \\\\\nInteraction & 0.21 & 1,\\,11 & 0.656 & 0.019 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "e9cc0c5c-baba-472c-be59-8513a1756fc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGNoHwL6YGEb4nct9W7tLH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 158060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 444
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

_source line 1154 · 2026-05-28T10:01:20.375Z_

<details><summary>↩ Tool result · `toolu_01L5Rz7MZHXqXqn4a1jc1WEW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "329195a8-da12-4d39-9322-c28d984b4dc2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "Gradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\\nInteraction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\",
    "newString": "Gradient flow (ON vs.\\ OFF) & 3.26 & 1,\\,11 & 0.098 & 0.229 \\\\\nNormalization (BN vs.\\ LN) & 4.68 & 1,\\,11 & 0.053 & 0.298 \\\\\nInteraction & 0.21 & 1,\\,11 & 0.656 & 0.019 \\\\",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\\approx}$46\\%). (d)~Gradient norm ratio per layer.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}4$), Detach+LN achieves $0.798 \\pm 0.022$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.2$\\,pp vs.\\ Vanilla, $d{=}+2.31$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.019$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 15 total observations). The interaction is negligible ($F(1,11){=}0.21$, $p{=}0.656$, $\\eta^2{=}0.019$), confirming additive main effects. The normalization main effect approaches significance ($F(1,11){=}4.68$, $p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect is medium-sized but non-significant ($F(1,11){=}3.26$, $p{=}0.098$, $\\eta^2{=}0.229$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.053$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\\nInteraction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.60 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.12 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.47 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
    "structuredPatch": [
      {
        "oldStart": 143,
        "oldLines": 9,
        "newStart": 143,
        "newLines": 9,
        "lines": [
          " \\toprule",
          " Source & $F$ & df & $p$ & $\\eta^2$ \\\\",
          " \\midrule",
          "-Gradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\",
          "-Normalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\",
          "-Interaction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\",
          "+Gradient flow (ON vs.\\ OFF) & 3.26 & 1,\\,11 & 0.098 & 0.229 \\\\",
          "+Normalization (BN vs.\\ LN) & 4.68 & 1,\\,11 & 0.053 & 0.298 \\\\",
          "+Interaction & 0.21 & 1,\\,11 & 0.656 & 0.019 \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}"
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

_source line 1155_

Now the pairwise d table — only Cell 4 rows change.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "ffc0f2bd-82b5-4f37-a0b7-e886f30c656a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USmgos6um3exK3r6o6iUZE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 424,
      "cache_read_input_tokens": 158504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 424
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

_source line 1156_

<details open><summary>🔧 Tool call — Edit · `toolu_01DYPUKWssv9AkVzPNP8xP5G`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "Cell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.60 \\\\",
  "new_string": "Cell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.66 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "0823497c-5040-4412-84ec-e8a10021d820",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USmgos6um3exK3r6o6iUZE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 424,
      "cache_read_input_tokens": 158504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 424
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

_source line 1157 · 2026-05-28T10:01:26.023Z_

<details><summary>↩ Tool result · `toolu_01DYPUKWssv9AkVzPNP8xP5G`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "b9ae60c3-742e-4783-a3b7-8a2540d48af8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "Cell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.60 \\\\",
    "newString": "Cell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.66 \\\\",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\\approx}$46\\%). (d)~Gradient norm ratio per layer.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}4$), Detach+LN achieves $0.798 \\pm 0.022$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.2$\\,pp vs.\\ Vanilla, $d{=}+2.31$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.019$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 15 total observations). The interaction is negligible ($F(1,11){=}0.21$, $p{=}0.656$, $\\eta^2{=}0.019$), confirming additive main effects. The normalization main effect approaches significance ($F(1,11){=}4.68$, $p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect is medium-sized but non-significant ($F(1,11){=}3.26$, $p{=}0.098$, $\\eta^2{=}0.229$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.053$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.26 & 1,\\,11 & 0.098 & 0.229 \\\\\nNormalization (BN vs.\\ LN) & 4.68 & 1,\\,11 & 0.053 & 0.298 \\\\\nInteraction & 0.21 & 1,\\,11 & 0.656 & 0.019 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.60 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.12 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.47 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
    "structuredPatch": [
      {
        "oldStart": 163,
        "oldLines": 7,
        "newStart": 163,
        "newLines": 7,
        "lines": [
          " \\midrule",
          " Cell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\",
          " Cell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\",
          "-Cell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.60 \\\\",
          "+Cell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.66 \\\\",
          " Cell~2 vs.\\ Cell~3 & $+$0.25 \\\\",
          " Cell~2 vs.\\ Cell~4 & $-$1.12 \\\\",
          " Cell~3 vs.\\ Cell~4 & $-$1.47 \\\\"
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

_source line 1158_

<details open><summary>🔧 Tool call — Edit · `toolu_01Aa8Wdog2vFKfEGeqoiPsYA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "Cell~2 vs.\\ Cell~4 & $-$1.12 \\\\",
  "new_string": "Cell~2 vs.\\ Cell~4 & $-$1.00 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "1472f51c-4c18-445c-a619-d246af2141fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gf9KpJREfU9DoDQ71Kok9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 158928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 270
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

_source line 1159 · 2026-05-28T10:01:30.543Z_

<details><summary>↩ Tool result · `toolu_01Aa8Wdog2vFKfEGeqoiPsYA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "75c5a9a6-67a4-4301-a8ec-8780e07e7990",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "Cell~2 vs.\\ Cell~4 & $-$1.12 \\\\",
    "newString": "Cell~2 vs.\\ Cell~4 & $-$1.00 \\\\",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\\approx}$46\\%). (d)~Gradient norm ratio per layer.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}4$), Detach+LN achieves $0.798 \\pm 0.022$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.2$\\,pp vs.\\ Vanilla, $d{=}+2.31$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.019$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 15 total observations). The interaction is negligible ($F(1,11){=}0.21$, $p{=}0.656$, $\\eta^2{=}0.019$), confirming additive main effects. The normalization main effect approaches significance ($F(1,11){=}4.68$, $p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect is medium-sized but non-significant ($F(1,11){=}3.26$, $p{=}0.098$, $\\eta^2{=}0.229$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.053$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.26 & 1,\\,11 & 0.098 & 0.229 \\\\\nNormalization (BN vs.\\ LN) & 4.68 & 1,\\,11 & 0.053 & 0.298 \\\\\nInteraction & 0.21 & 1,\\,11 & 0.656 & 0.019 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.66 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.12 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.47 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
    "structuredPatch": [
      {
        "oldStart": 165,
        "oldLines": 7,
        "newStart": 165,
        "newLines": 7,
        "lines": [
          " Cell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\",
          " Cell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.66 \\\\",
          " Cell~2 vs.\\ Cell~3 & $+$0.25 \\\\",
          "-Cell~2 vs.\\ Cell~4 & $-$1.12 \\\\",
          "+Cell~2 vs.\\ Cell~4 & $-$1.00 \\\\",
          " Cell~3 vs.\\ Cell~4 & $-$1.47 \\\\",
          " \\addlinespace",
          " Cell~1 vs.\\ Vanilla & $-$0.42 \\\\"
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

_source line 1160_

<details open><summary>🔧 Tool call — Edit · `toolu_01Ybbqp2MDnxpBXGm6wxvW5E`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "Cell~3 vs.\\ Cell~4 & $-$1.47 \\\\",
  "new_string": "Cell~3 vs.\\ Cell~4 & $-$1.35 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "5b7c8437-7102-43ac-a7f9-69f340eaa04c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CL877CNCGBpMF3ktMD8nKh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 159198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
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

_source line 1161 · 2026-05-28T10:01:33.850Z_

<details><summary>↩ Tool result · `toolu_01Ybbqp2MDnxpBXGm6wxvW5E`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "ad056dd6-6f51-42e3-9164-e989ead4f47c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "Cell~3 vs.\\ Cell~4 & $-$1.47 \\\\",
    "newString": "Cell~3 vs.\\ Cell~4 & $-$1.35 \\\\",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\\approx}$46\\%). (d)~Gradient norm ratio per layer.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}4$), Detach+LN achieves $0.798 \\pm 0.022$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.2$\\,pp vs.\\ Vanilla, $d{=}+2.31$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.019$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 15 total observations). The interaction is negligible ($F(1,11){=}0.21$, $p{=}0.656$, $\\eta^2{=}0.019$), confirming additive main effects. The normalization main effect approaches significance ($F(1,11){=}4.68$, $p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect is medium-sized but non-significant ($F(1,11){=}3.26$, $p{=}0.098$, $\\eta^2{=}0.229$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.053$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.26 & 1,\\,11 & 0.098 & 0.229 \\\\\nNormalization (BN vs.\\ LN) & 4.68 & 1,\\,11 & 0.053 & 0.298 \\\\\nInteraction & 0.21 & 1,\\,11 & 0.656 & 0.019 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.66 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.00 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.47 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
    "structuredPatch": [
      {
        "oldStart": 166,
        "oldLines": 7,
        "newStart": 166,
        "newLines": 7,
        "lines": [
          " Cell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.66 \\\\",
          " Cell~2 vs.\\ Cell~3 & $+$0.25 \\\\",
          " Cell~2 vs.\\ Cell~4 & $-$1.00 \\\\",
          "-Cell~3 vs.\\ Cell~4 & $-$1.47 \\\\",
          "+Cell~3 vs.\\ Cell~4 & $-$1.35 \\\\",
          " \\addlinespace",
          " Cell~1 vs.\\ Vanilla & $-$0.42 \\\\",
          " Cell~2 vs.\\ Vanilla & $+$1.07 \\\\"
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

_source line 1162_

<details open><summary>🔧 Tool call — Edit · `toolu_019PfUNYM29mDEpFDTAvJ9Eg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "Cell~4 vs.\\ Vanilla & $+$2.36 \\\\",
  "new_string": "Cell~4 vs.\\ Vanilla & $+$2.31 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "b1d3c226-a8c1-4008-8f1d-1dfff99fc834",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018uapeHVp85tfLMhxCGq25y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 159435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
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

_source line 1163 · 2026-05-28T10:01:37.615Z_

<details><summary>↩ Tool result · `toolu_019PfUNYM29mDEpFDTAvJ9Eg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "72adb82b-9070-4150-895e-8d495e7ce799",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "Cell~4 vs.\\ Vanilla & $+$2.36 \\\\",
    "newString": "Cell~4 vs.\\ Vanilla & $+$2.31 \\\\",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\\approx}$46\\%). (d)~Gradient norm ratio per layer.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}4$), Detach+LN achieves $0.798 \\pm 0.022$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.2$\\,pp vs.\\ Vanilla, $d{=}+2.31$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.019$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 15 total observations). The interaction is negligible ($F(1,11){=}0.21$, $p{=}0.656$, $\\eta^2{=}0.019$), confirming additive main effects. The normalization main effect approaches significance ($F(1,11){=}4.68$, $p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect is medium-sized but non-significant ($F(1,11){=}3.26$, $p{=}0.098$, $\\eta^2{=}0.229$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.053$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.26 & 1,\\,11 & 0.098 & 0.229 \\\\\nNormalization (BN vs.\\ LN) & 4.68 & 1,\\,11 & 0.053 & 0.298 \\\\\nInteraction & 0.21 & 1,\\,11 & 0.656 & 0.019 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.66 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.00 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.35 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
    "structuredPatch": [
      {
        "oldStart": 171,
        "oldLines": 7,
        "newStart": 171,
        "newLines": 7,
        "lines": [
          " Cell~1 vs.\\ Vanilla & $-$0.42 \\\\",
          " Cell~2 vs.\\ Vanilla & $+$1.07 \\\\",
          " Cell~3 vs.\\ Vanilla & $+$0.88 \\\\",
          "-Cell~4 vs.\\ Vanilla & $+$2.36 \\\\",
          "+Cell~4 vs.\\ Vanilla & $+$2.31 \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}"
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

_source line 1164_

Now update the Limitations section "14 total observations" reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "4bb8f34c-9d20-42d3-a7b7-d72878744d84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181bx7ProbxQaVe7ipWu9iT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 159672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
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

_source line 1165_

<details open><summary>🔧 Tool call — Read · `toolu_019wSfGY4FYK7VQ2KMzJA6su`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "offset": 192,
  "limit": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "9a396b8b-52ae-4da9-86dd-6792d9bc70a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181bx7ProbxQaVe7ipWu9iT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 159672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
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

_source line 1166 · 2026-05-28T10:01:41.260Z_

<details><summary>↩ Tool result · `toolu_019wSfGY4FYK7VQ2KMzJA6su`</summary>

```text
192	
193	Our study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.
194	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "9e2b1833-8614-4034-9d05-158adaab6ae9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
      "content": "\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
      "numLines": 3,
      "startLine": 192,
      "totalLines": 194
    }
  }
}
```

</details>

---


### Tool call

_source line 1167_

<details open><summary>🔧 Tool call — Edit · `toolu_011sUfBdcDCfBTynK3Zxkh5v`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "$n{=}3$--$4$ seeds per cell (14 total observations)",
  "new_string": "$n{=}3$--$4$ seeds per cell (15 total observations)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "5c3fb3fc-52f4-4805-a6af-574ae1baa8b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156ZskdUEMiFz1rdTTExfrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 558,
      "cache_read_input_tokens": 159905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 558
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

_source line 1168 · 2026-05-28T10:01:44.918Z_

<details><summary>↩ Tool result · `toolu_011sUfBdcDCfBTynK3Zxkh5v`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "34ace7e4-3611-4915-99e0-eb02fc8362fa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "$n{=}3$--$4$ seeds per cell (14 total observations)",
    "newString": "$n{=}3$--$4$ seeds per cell (15 total observations)",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\\approx}$46\\%). (d)~Gradient norm ratio per layer.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}4$), Detach+LN achieves $0.798 \\pm 0.022$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.2$\\,pp vs.\\ Vanilla, $d{=}+2.31$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (15 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect does not reach significance ($p{=}0.098$) but shows a medium-to-large effect size ($\\eta^2{=}0.229$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.019$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 15 total observations). The interaction is negligible ($F(1,11){=}0.21$, $p{=}0.656$, $\\eta^2{=}0.019$), confirming additive main effects. The normalization main effect approaches significance ($F(1,11){=}4.68$, $p{=}0.053$, $\\eta^2{=}0.298$); the gradient flow main effect is medium-sized but non-significant ($F(1,11){=}3.26$, $p{=}0.098$, $\\eta^2{=}0.229$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.053$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.26 & 1,\\,11 & 0.098 & 0.229 \\\\\nNormalization (BN vs.\\ LN) & 4.68 & 1,\\,11 & 0.053 & 0.298 \\\\\nInteraction & 0.21 & 1,\\,11 & 0.656 & 0.019 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.66 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.00 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.35 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
    "structuredPatch": [
      {
        "oldStart": 190,
        "oldLines": 4,
        "newStart": 190,
        "newLines": 4,
        "lines": [
          " \\section{Limitations}",
          " \\label{app:limitations}",
          " ",
          "-Our study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.",
          "+Our study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (15 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules."
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

_source line 1169_

All paper tex files updated. Now update paper_framing.md.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "4a26043c-22bc-465f-8ce0-5ac6b1f66685",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rnk72uR1J8horNuVfF2zUu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 448,
      "cache_read_input_tokens": 160463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 448
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

_source line 1170_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01CvEygfhdKg4pVejUHEcitg`</summary>

```json
{
  "todos": [
    {
      "content": "Wait for eval completion (T7-T9 remaining)",
      "status": "completed",
      "activeForm": "Waiting for eval completion on westd-34685"
    },
    {
      "content": "Extract results JSON and update registry",
      "status": "completed",
      "activeForm": "Extracting results and updating registry"
    },
    {
      "content": "Add 4th seed to ANOVA script and rerun",
      "status": "completed",
      "activeForm": "Updating ANOVA script with new Cell 4 seed"
    },
    {
      "content": "Update all paper files with n=4 numbers",
      "status": "completed",
      "activeForm": "Updating paper files with new statistics"
    },
    {
      "content": "Update paper_framing.md",
      "status": "in_progress",
      "activeForm": "Updating paper_framing.md"
    },
    {
      "content": "Compile LaTeX PDF and verify 0 errors",
      "status": "pending",
      "activeForm": "Compiling LaTeX PDF"
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
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "0b056a62-20f3-42f7-96b2-c2eb84c9f579",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rnk72uR1J8horNuVfF2zUu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 448,
      "cache_read_input_tokens": 160463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 448
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

_source line 1171 · 2026-05-28T10:01:50.130Z_

<details><summary>↩ Tool result · `toolu_01CvEygfhdKg4pVejUHEcitg`</summary>

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
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "0f9f5bd2-9f34-46bc-8962-405858b667dd",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Wait for eval completion (T7-T9 remaining)",
        "status": "completed",
        "activeForm": "Waiting for eval completion on westd-34685"
      },
      {
        "content": "Extract results JSON and update registry",
        "status": "completed",
        "activeForm": "Extracting results and updating registry"
      },
      {
        "content": "Add 4th seed to ANOVA script and rerun",
        "status": "completed",
        "activeForm": "Updating ANOVA script with new Cell 4 seed"
      },
      {
        "content": "Update all paper files with n=4 numbers",
        "status": "in_progress",
        "activeForm": "Updating paper files with new statistics"
      },
      {
        "content": "Update paper_framing.md",
        "status": "pending",
        "activeForm": "Updating paper_framing.md"
      },
      {
        "content": "Compile LaTeX PDF and verify 0 errors",
        "status": "pending",
        "activeForm": "Compiling LaTeX PDF"
      }
    ],
    "newTodos": [
      {
        "content": "Wait for eval completion (T7-T9 remaining)",
        "status": "completed",
        "activeForm": "Waiting for eval completion on westd-34685"
      },
      {
        "content": "Extract results JSON and update registry",
        "status": "completed",
        "activeForm": "Extracting results and updating registry"
      },
      {
        "content": "Add 4th seed to ANOVA script and rerun",
        "status": "completed",
        "activeForm": "Updating ANOVA script with new Cell 4 seed"
      },
      {
        "content": "Update all paper files with n=4 numbers",
        "status": "completed",
        "activeForm": "Updating paper files with new statistics"
      },
      {
        "content": "Update paper_framing.md",
        "status": "in_progress",
        "activeForm": "Updating paper_framing.md"
      },
      {
        "content": "Compile LaTeX PDF and verify 0 errors",
        "status": "pending",
        "activeForm": "Compiling LaTeX PDF"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Tool call

_source line 1172_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Lrmgb9A5aWSaAsxsDj1STi`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "ffbece37-ed09-4e28-b548-905b52a7fc54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UMFW9oQBMkfKpYcma8pwo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 160911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 331
      },
      "output_tokens": 46,
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

_source line 1173 · 2026-05-28T10:01:55.812Z_

<details><summary>↩ Tool result · `toolu_01Lrmgb9A5aWSaAsxsDj1STi`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "30ba8250-d1c8-4f30-b1d0-78a39d1009dc",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 29
  }
}
```

</details>

---


### Assistant

_source line 1174_

<details><summary>Logged reasoning block</summary>

```text
I need to update the paper_framing.md with the new Cell 4 data. Let me prepare the updated content. I'll need to update:

1. The D074 factorial table (Cell 4 row)
2. The ANOVA stats
3. The Cell 4 vs Vanilla stats
4. The v2 Factorial Evidence table
5. The C3 contribution text
6. Various other references

Let me read the current content and make the targeted changes. Since save_project_file requires the full file content, I need to construct the full updated file.

Actually, the paper_framing.md is quite long (14587 chars). 

Now I'm pulling the full content from what I already have and systematically updating all the Cell 4 references. I need to change the sample size from n=3 to n=4, update the mean and standard error values in the D074 table, recalculate the performance gap from +3.5pp to +3.1pp, and adjust all the ANOVA F-statistics and p-values accordingly. I need to track down the actual file and make these updates systematically. Let me pull up the paper framing document and work through all the changes I've identified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "4704a11e-107e-408c-95eb-1eabcfc710d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014coH2177uCkvb5h95jm9de",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 161242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
      },
      "output_tokens": 35,
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

_source line 1175_

Let me read the paper_framing.md locally to edit it precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "dfbf1b1e-b6ab-4972-9e6f-d40f14be194c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014coH2177uCkvb5h95jm9de",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 161242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
      },
      "output_tokens": 35,
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

_source line 1176_

<details open><summary>🔧 Tool call — Read · `toolu_01948DswPFFMoYftvyPqdU9x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "c5d9ed67-ed17-4113-9a18-99b0853b292c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014coH2177uCkvb5h95jm9de",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 161242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
      },
      "output_tokens": 35,
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

_source line 1177 · 2026-05-28T10:02:11.774Z_

<details><summary>↩ Tool result · `toolu_01948DswPFFMoYftvyPqdU9x`</summary>

```text
1	# OccSafe-VLA — Paper Framing
2	
3	> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=3。CoRL 2026 target (Paper May 29)
4	>
5	> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。"ordinal interaction" framing 改为 "dual main effects + practical threshold crossing"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。
6	
7	## Architecture Facts (from code, verified)
8	- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）
9	- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。
10	- **FocalLoss**: α=0.25, γ=2.0
11	- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)
12	- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）
13	- **LoRA**: rank=32, alpha=16, dropout=0.0
14	- **GPU**: 4× RTX PRO 6000 98GB per server
15	- **训练时间**: ~12.9h/run @ 1.08 it/s
16	
17	### 叙事含义
18	- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。
19	  比"仅改善 DINOv2"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。
20	- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 "lightweight auxiliary" 叙事
21	- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐"放手"让 action loss 主导，
22	  可论证为"先学空间结构，再精化动作"的课程学习效果
23	- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守
24	
25	### DepthHead (新增, 2026-05-22)
26	- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）
27	- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）
28	- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64
29	- **参数量**: ~1.2M（与 OccHead 同量级）
30	
31	## Core Insight (D043 Plan B, 2026-05-26)
32	
33	**假设演变**：
34	- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence
35	- D017-D019：梯度流是防止损害的条件，非提供收益的条件
36	- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**
37	- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**
38	
39	### D074 v2 Factorial — Dual Main Effects（当前权威数据）
40	
41	| | BN | LN | Δ(LN-BN) |
42	|--|----|----|-----------|
43	| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |
44	| **Gradient OFF** | 0.767±0.024 (n=4) | **0.802±0.024** (n=3) | **+3.5pp** |
45	| Δ(ON-OFF) | **-4.2pp** | **-2.9pp** | — |
46	| **主效应** | BN pooled: 0.746 | LN pooled: 0.788 | **+4.2pp (d≈1.03)** |
47	| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |
48	
49	**ANOVA 交互项**: F=0.10, p=0.763, η²=0.005。两行斜率几乎相同 (BN: -4.2pp, LN: -2.9pp)，纯可加模型。
50	
51	**关键发现（D074 更新）**：
52	- **Gradient flow 主效应**: ON pooled (0.749) < OFF pooled (0.785), Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全
53	- **Normalization 主效应**: LN pooled (0.788) > BN pooled (0.746), Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致优于 BN
54	- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla
55	- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分
56	- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding
57	- ✅ Cell 4 n=3 完成: [0.826, 0.802, 0.778], mean=0.802±0.024
58	- Cell 4 vs Vanilla: Cohen's d=2.36, p=0.045
59	
60	### v1 → v2 数据不一致 [v1-SUPERSEDED]
61	
62	v1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。
63	**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。
64	
65	### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）
66	
67	### 机制证据状态（D056 v2 验证完成）
68	
69	**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：
70	- v1 结果：Detach gradient norms = 1-13% of Vanilla — "灾难性崩塌"（逐层分析, 200 真实样本）
71	- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）
72	- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**
73	- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做
74	- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证
75	
76	**v2 Gradient Analysis (D056/D057) — 部分有效**：
77	- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认
78	- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足
79	- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)
80	- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**
81	
82	**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：
83	- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除
84	- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常
85	- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移
86	- BN forward-pass 并未导致表征退化 — "BN interference" 假设不成立
87	
88	**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：
89	所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。
90	v2 存活的机制信号：
91	- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突
92	- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)
93	- ❌ "capacity competition" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据
94	- ❌ "BN forward-pass interference" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好
95	- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim
96	
97	### Core Insight（D074 修正）
98	
99	VLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：
100	
101	1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害
102	2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件
103	3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）
104	
105	**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。
106	
107	**机制层面（D057 修正）**：
108	- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突
109	- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）
110	- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证
111	- 空间内容仍然次要
112	
113	**论文策略选项**（Reviewer 建议）：
114	- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h
115	- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响
116	- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary
117	
118	### 措辞约束（D057 更新）
119	- **禁止** "crossover interaction" — v2 是 ordinal
120	- **禁止** "statistically significant interaction" / "significant interaction effect" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)
121	- **谨慎** "interaction" 单独使用 — 改用 "normalization-dependent gradient flow effect" 或 "dual main effects"
122	- **禁止** "BN-mediated gradient calibration" / "existence regularization" — v1 不可复现
123	- **禁止** 引用 v1/v2 梯度数值的跨方法论比较
124	- **谨慎** "gradient collapse" / "no gradient collapse" — 待同方法论验证，暂不 claim
125	- **可用** "gradient orthogonality"（v2 确认）— 排除直接梯度冲突
126	- **可用** "capacity competition" / "BN forward-pass interference"（需标注为假设，待 CKA 验证）
127	- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著
128	- Cell 1 高方差本身可作为 finding：用 "BN+gradient flow leads to unstable training"
129	- Gradient flow 主效应用 "detrimental" / "harmful"，不用 "collapse"（collapse 特指 detach 极端情况）
130	
131	**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。
132	
133	## Framing Strategy (D019 修正)
134	
135	**确定路线: Option B 分析论文**（Reviewer 审查通过）
136	
137	**核心叙事转变 (D026)**：从"梯度流是必要条件"→"梯度流防止 encoder gradient collapse"（具体机制，非抽象论断）
138	
139	**Title（暂定）**: "Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis"
140	
141	**3-Contribution 结构（D043 Plan B 修正）**：
142	- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：
143	  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全
144	  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势
145	  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**
146	  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)
147	  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定
148	  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla
149	  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变
150	  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证
151	- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）
152	- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)
153	- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla
154	
155	## Core Contribution Evidence
156	
157	### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)
158	v1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。
159	v2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。
160	
161	### v2 Factorial Evidence (D043, 权威数据)
162	
163	| Cell | Condition | n | CAR values | mean±std | 代码版本 |
164	|------|-----------|---|-----------|----------|---------|
165	| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |
166	| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |
167	| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |
168	| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |
169	| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |
170	
171	✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。
172	✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。
173	
174	### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]
175	
176	**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**
177	
178	**CKA Evidence [v1-SUPERSEDED]**：
179	- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）
180	- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化
181	- **"BN = 100% 表征漂移原因" 不再成立** — v2 中 BN 不导致 CKA 退化
182	
183	**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：
184	v1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。
185	
186	**两种失败模式（D031, 仍有效）**：
187	- Detach = 均匀退化 (per-task CAR std=0.002)
188	- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)
189	
190	**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。
191	
192	### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]
193	- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，"BN interference" 假设不成立
194	- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）
195	- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证
196	- ⚠️ v1 的 "existence regularization" / "BN-mediated calibration" 不再成立
197	- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突
198	
199	### Claim 3: Spatial Content Secondary
200	v1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。
201	Depth = Vanilla exactly (4 seeds, D022)。空间内容次要。
202	⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。
203	
204	### Claim 4 (Depth): ✅ Confirmed (D022)
205	Depth CAR = 0.780 = Vanilla exactly (4 seeds)。
206	
207	## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）
208	
209	**【Pass（必须同时满足）】**
210	1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）
211	2. Depth 4-seed mean TSR ≥ 0.870
212	
213	**【Fail（满足任一）】**
214	1. Depth 4-seed mean CAR < 0.780
215	2. Depth 4-seed mean TSR < 0.870
216	
217	## Anticipated Reviewer Concerns
218	
219	### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED
220	### RC2 [HIGH]: "Why Not Just Use CBF?" — Defense: zero inference cost + complementarity
221	### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)
222	### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations
223	### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations
224	### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI
225	
226	## 待定关键实验
227	
228	### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)
229	替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。
230	- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)
231	- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)
232	- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠
233	- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移
234	
235	### Cutoff Temporal Dynamics (D029/D030/D041)
236	
237	**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。
238	
239	**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**
240	cutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。
241	
242	| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |
243	|------|--------|--------|--------|------|-----------|
244	| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |
245	| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |
246	| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |
247	| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |
248	| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |
249	| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |
250	
251	**安全 claim（D041 限缩后）**：
252	1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本
253	2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）
254	3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）
255	4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim
256	
257	**不安全 claim**：任何特定 cutoff 点优于另一个、非单调"sweet spot"。
258	
259	**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。
260	
261	### Same-Seed 梯度重分析 — 条件式 (D028)
262	当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：
263	- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓
264	- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异
265	- **Scenario C**: 需两版分析（BN 和 LN）
266	Fig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 "旧 round"。
267	
268	## Framing Risk Ranking (D043 Plan B 更新)
269	
270	| 排名 | 风险 | 状态 | 应对 |
271	|------|------|------|------|
272	| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |
273	| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |
274	| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 "无害" 但非 "有益" | ✅ 已定性 | 论文用 "statistically indistinguishable"，不 claim positive |
275	| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |
276	| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |
277	| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |
278	
279	## 目标会议
280	**CoRL 2026**: Abstract May 26, Paper May 29
281	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "50a6f0df-b814-47aa-96f3-fc2ebeb381b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
      "content": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=3。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.802±0.024** (n=3) | **+3.5pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.9pp** | — |\n| **主效应** | BN pooled: 0.746 | LN pooled: 0.788 | **+4.2pp (d≈1.03)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.10, p=0.763, η²=0.005。两行斜率几乎相同 (BN: -4.2pp, LN: -2.9pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.749) < OFF pooled (0.785), Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.788) > BN pooled (0.746), Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=3 完成: [0.826, 0.802, 0.778], mean=0.802±0.024\n- Cell 4 vs Vanilla: Cohen's d=2.36, p=0.045\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
      "numLines": 281,
      "startLine": 1,
      "totalLines": 281
    }
  }
}
```

</details>

---


### Assistant

_source line 1178_

<details><summary>Logged reasoning block</summary>

```text
Now I need to update the paper_framing.md with all the new Cell 4 n=4 data. Let me make the key changes:

1. Line 3: header status — Cell 4 n=3 → n=4, d≈1.03 → d≈1.05, F=0.10, p=0.763 → F=0.21, p=0.656
2. Line 5: d≈1.03 → d≈1.05
3. Line 44: Cell 4 row in D074 table: 0.802±0.024 (n=3) → 0.798±0.022 (n=4), +3.5pp → +3.1pp


4. Line 45: -2.9pp → -2.5pp
5. Line 46: LN pooled update, d≈1.03 → d≈1.05
6. Line 49: ANOVA stats update
7. Line 52: F=3.20→3.26, p=0.104→0.098, η²=0.180→0.229
8. Line 53: F=4.49→4.68, p=0.060→0.053, η²=0.253→0.298
9. Line 57: Cell 4 data update
10. Line 58: d=2

.36→2.31, p=0.045→0.040
11. Line 101-102: ANOVA stats
12. Line 143-144: C1 ANOVA stats
13. Line 150: 14 seeds → 15 seeds
14. Line 152: C3 Cell 4 stats
15. Line 168: v2 Evidence table Cell 4 row
16. Line 171: N=14 → N=15, Cell 4 n=3 → n=4
17. Line 172: ANOVA stats
18. Line 190: Cell 4 n=3 → n=4
19. Line 273: N=14 → N=15, p=0.045 → p=0.040

There are quite a few updates scattered throughout the document—effect sizes, p-values, sample sizes, and ANOVA statistics across multiple sections. Since I need to save the full file, I'm going to reconstruct the entire content with all these edits applied.

The file is already on disk at `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md`, so I'll apply the changes directly to the local copy and then push it through the MCP tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "c0720d42-5dee-4177-8afa-c9c4fd7509ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkowZWpWguxyFXMGa5xQeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9995,
      "cache_read_input_tokens": 161605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9995
      },
      "output_tokens": 21,
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

_source line 1179_

I'll make all the necessary edits to paper_framing.md. Let me do them systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "64324bf1-7f70-4c8e-a9e7-2d56fc14621a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkowZWpWguxyFXMGa5xQeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9995,
      "cache_read_input_tokens": 161605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9995
      },
      "output_tokens": 21,
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

_source line 1180_

<details open><summary>🔧 Tool call — Edit · `toolu_01JPARw7iHVTtqnY8zivWP5B`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=3。CoRL 2026 target (Paper May 29)",
  "new_string": "Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "039ec213-e0eb-4bc3-a344-5a5471456ac6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkowZWpWguxyFXMGa5xQeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9995,
      "cache_read_input_tokens": 161605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9995
      },
      "output_tokens": 21,
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

_source line 1181 · 2026-05-28T10:02:32.076Z_

<details><summary>↩ Tool result · `toolu_01JPARw7iHVTtqnY8zivWP5B`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "d28ad41a-99d1-40ad-b079-d34dc879b6fa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=3。CoRL 2026 target (Paper May 29)",
    "newString": "Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=3。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.802±0.024** (n=3) | **+3.5pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.9pp** | — |\n| **主效应** | BN pooled: 0.746 | LN pooled: 0.788 | **+4.2pp (d≈1.03)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.10, p=0.763, η²=0.005。两行斜率几乎相同 (BN: -4.2pp, LN: -2.9pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.749) < OFF pooled (0.785), Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.788) > BN pooled (0.746), Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=3 完成: [0.826, 0.802, 0.778], mean=0.802±0.024\n- Cell 4 vs Vanilla: Cohen's d=2.36, p=0.045\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " # OccSafe-VLA — Paper Framing",
          " ",
          "-> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=3。CoRL 2026 target (Paper May 29)",
          "+> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)",
          " >",
          " > ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。",
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


### System

_source line 1182_

```json
{
  "type": "system",
  "subtype": "status",
  "status": "compacting",
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "3c60f29c-a84b-4eb7-a91c-84fa24fd9600"
}
```

---


### System

_source line 1183_

```json
{
  "type": "system",
  "subtype": "status",
  "status": null,
  "compact_result": "success",
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "c2e971f2-12d2-49fd-8444-f63cadc1d2b9"
}
```

---


### System

_source line 1184_

```json
{
  "type": "system",
  "subtype": "compact_boundary",
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "402fe14c-6619-428e-a8cb-7ba75cf18627",
  "compact_metadata": {
    "trigger": "auto",
    "pre_tokens": 172628,
    "post_tokens": 5669,
    "duration_ms": 111517
  }
}
```

---


## Round 2

## Round 2

78 recorded events


### User

_source line 1185 · 2026-05-28T10:04:23.687Z_

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. Primary Request and Intent:
   The user assigned a time-critical 5-phase task (DDL May 28 12:00 UTC) for project `occsafe_vla` targeting CoRL 2026:
   - **Phase 1**: Monitor running `detach_ln_v2_s2` eval (50-rollout SafeLIBERO, 10 tasks) on westd-34685 until all 10 tasks complete
   - **Phase 2**: Extract results JSON, update experiment registry via `update_registry`
   - **Phase 3**: Add new CAR value as 4th seed to Cell 4 in the ANOVA script, rerun it
   - **Phase 4**: Update ALL paper files (results.tex, main.tex, introduction.tex, discussion.tex, appendix.tex, conclusion.tex, paper_framing.md) with new n=4 numbers, ANOVA stats, Cohen's d, etc.
   - **Phase 5**: Compile LaTeX PDF and verify 0 errors
   Key constraint: "所有数字更新必须保持一致性" (all number updates must be consistent)

2. Key Technical Concepts:
   - 2×2 factorial ANOVA (gradient flow × normalization type) on Collision Avoidance Rate (CAR)
   - SafeLIBERO Level I benchmark: 10 tasks, 50 rollouts/seed, 500 episodes per seed
   - Cell 4 = Detach+LN (gradient OFF + LayerNorm) — best factorial cell
   - Vanilla baseline: n=3, [0.768, 0.748, 0.720], mean=0.745±0.024
   - OpenVLA-7B with OFT recipe, LoRA rank=32, auxiliary spatial head
   - Cohen's d effect sizes, Welch's t-tests, Type III SS ANOVA
   - MCP tools for remote SSH (ssh_read_only, ssh_execute) and registry management
   - Server westd-34685 uses conda environment (not system python): `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`

3. Files and Code Sections:

   - **`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/anova_v2_final_gen.py`**
     - ANOVA script computing 2×2 factorial ANOVA, pairwise t-tests, Cohen's d, simple effects
     - Edit: Line 17 changed from `'grad_off_ln': [0.802, 0.826, 0.778],  # Cell 4: Detach LN, n=3` to `'grad_off_ln': [0.802, 0.826, 0.778, 0.784],  # Cell 4: Detach LN, n=4`
     - Script was rerun successfully, producing new ANOVA output saved to `anova_v2_final.txt`

   - **`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex`**
     - Main results section with Table 1 (tab:main_results), Table 2 (tab:factorial), inline ANOVA stats
     - 9 edits made:
       - Table 1 Cell 4 row: `OFF & LN & 3 & $0.802 \pm 0.024$ & $0.911 \pm 0.018$ & $+$5.7` → `OFF & LN & 4 & $0.798 \pm 0.022$ & $0.909 \pm 0.015$ & $+$5.2`
       - Inline Cell 4: `$0.798 \pm 0.022$, $n{=}4$, $\Delta{=}+5.2$\,pp, $d{=}+2.31

       - ANOVA inline: `gradient flow $F(1,11){=}3.26$, $p{=}0.098$, $\eta^2{=}0.23$; normalization $F(1,11){=}4.68$, $p{=}0.053$, $\eta^2{=}0.30$; interaction $F{=}0.21$, $p{=}0.66

       - LN advantage: `$+$3.1\,pp without ($d{=}1.35$, very large)`, η²=0.019
       - p=0.053 for normalization effect
       - Table 2 caption: `normalization effect $d{=}1.05$--$1.35

, `ANOVA interaction $F{=}0.21$, $p{=}0.66

       - Table 2 body: `Detach+LN (0.798)`, `$-$2.5`, `$-$3.1 ($d{=}{-}1.35$)`
       - Figure caption: `LN row: 2.5\,pp ($d{=}1.00$)`

   - **`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex`**
     - Contains fig1 caption with Cell 4 stats, central finding paragraph, contribution list
     - 2 edits:
       - Fig caption: `$0.798{\pm}0.022$, $n{=}4

       - All occurrences: `3.5--4.8\,pp` → `3.1--4.8\,pp` (replace_all, hit lines 16 and 20)

   - **`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex`**
     - Discussion of BN/LN effects, additive protection model, ANOVA interaction
     - 3 edits:
       - `$-$2.9\,pp for LN)` → `$-$2.5\,pp for LN)`
       - `$+$3.5\,pp without)` → `$+$3.1\,pp without)`
       - ANOVA: `$F{=}0.21$, $p{=}0.656$, $\eta^2{=}0.019

; Cell 4: `$0.798{\pm}0.022$ ($n{=}4$)`

   - **`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex`**
     - Abstract with overall study claims
     - 1 edit: `3.1--4.8\,pp`, `$d{\approx}1.05$--$1.35

, `$\eta^2{<}0.02

   - **`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex`**
     - 1 edit: `3.5--4.8\,pp` → `3.1--4.8\,pp`

   - **`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex`**
     - ANOVA table (tab:anova), pairwise d table (tab:pairwise), statistical power analysis text, limitations
     - 8 edits:
       - Cell 4 inline: `($n{=}4$), Detach+LN achieves $0.798 \pm 0.022

, `$\Delta{=}+5.2$\,pp`, `$d{=}+2.31

       - Power analysis: `15 total observations`, updated p and η² values
       - η²=0.005→0.019 for interaction
       - Full ANOVA inline text: all F, p, η² updated with df 1,11
       - Table caption: p=0.053
       - ANOVA table rows: `3.26 & 1,\,11 & 0.098 & 0.229`, `4.68 & 1,\,11 & 0.053 & 0.298`, `0.21 & 1,\,11 & 0.656 & 0.019`
       - Pairwise d: Cell 1 vs 4: -1.66, Cell 2 vs 4: -1.00, Cell 3 vs 4: -1.35, Cell 4 vs Vanilla: +2.31
       - Limitations: 15 total observations

   - **`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md`**
     - Project framing document with authoritative data tables, ANOVA stats, contribution text
     - Only 1 edit completed so far: header line Cell 4 n=3→n=4
     - Many more edits still needed (D074 table, ANOVA stats, v2 Evidence table, C3 text, etc.)

4. Errors and fixes:
   - **`python3: command not found` on westd-34685**: System python wasn't in PATH. Fixed by using conda: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c "..."`
   - **`ssh_read_only` blocked shell metacharacters**: `python3 -c` with `;` was blocked. Switched to `ssh_execute` tool.
   - **Registry DONE transition failed**: "Cannot transition to DONE without a 'conclusion' field." Fixed by setting conclusion='success' first, then status='DONE'.
   - **Registry conclusion validation**: Tried to pass a descriptive string, but only enum values accepted ('failed', 'killed', 'negative', 'success'). Fixed by using 'success'.
   - **`File has been modified since read` errors**: Occurred when trying to edit files that had been modified externally since last read. Fixed by re-reading the file before editing.

5. Problem Solving:
   - Successfully monitored eval from 7/10 to 10/10 tasks via repeated SSH polling
   - Extracted results from 236KB JSON file using remote Python execution
   - Computed all derived statistics (new ANOVA, pairwise Cohen's d, TSR approximation) using local Python
   - Systematically identified all paper locations needing updates by pre-reading files during eval wait time
   - Cell 4 vs Vanilla now reaches p=0.040 (< 0.05), a notable improvement from p=0.045

6. All user messages:
   - "Tool loaded." (after ToolSearch for ssh_read_only)
   - "Tool loaded." (after ToolSearch for TodoWrite)
   - "Tool loaded." (after ToolSearch for update_registry)
   - "Tool loaded." (after ToolSearch for ssh_execute)
   - "Tool loaded." (after ToolSearch for read_project_file)
   - "Tool loaded." (after ToolSearch for save_project_file)
   - "CRITICAL: Respond with TEXT ONLY. Do NOT call any tools..." (current summary request)

7. Pending Tasks:
   - **Complete paper_framing.md updates**: Only 1 of ~15+ needed edits done. Remaining changes include:
     - D074 factorial table (Cell 4 row: 0.802±0.024 n=3 → 0.798±0.022 n=4, +3.5pp→+3.1pp, -2.9pp→-2.5pp)
     - ANOVA stats throughout (F=0.10→0.21, p=0.763→0.656, η²=0.005→0.019; and gradient/norm main effects)
     - LN pooled mean and d≈1.03→d≈1.05
     - Cell 4 line: [0.826, 0.802, 0.778] → [0.826, 0.802, 0.778, 0.784], mean/std update
     - Cell 4 vs Vanilla: d=2.36→2.31, p=0.045→0.040
     - v2 Evidence table Cell 4 row (n=3→4, add 0.784)
     - Total N=14→15
     - C1 and C3 contribution text stats
     - Risk ranking table (N=14→15, p=0.045→0.040)
     - Core Insight section ANOVA stats
     - Status lines (Cell 4 n=3→n=4)
   - **Phase 5: Compile LaTeX PDF and verify 0 errors**: Run `pdflatex + bibtex + pdflatex + pdflatex` in the paper directory

8. Current Work:
   I was in the middle of updating paper_framing.md (Phase 4 continuation). I had just made the first edit (header status line: Cell 4 n=3→n=4) when the summary request interrupted. The file needs approximately 15 more targeted edits covering the D074 table, ANOVA stats, v2 Evidence table, contribution text, and various inline references throughout the document. After paper_framing.md is complete, the final task is Phase 5: LaTeX compilation.

   The todo list state at interruption:
   - [completed] Wait for eval completion
   - [completed] Extract results JSON and update registry
   - [completed] Add 4th seed to ANOVA script and rerun
   - [in_progress → effectively completed for tex files] Update all paper files with n=4 numbers
   - [in_progress] Update paper_framing.md (1 of ~15 edits done)
   - [pending] Compile LaTeX PDF and verify 0 errors

9. Optional Next Step:
   Continue updating paper_framing.md with all remaining Cell 4 n=4 statistics. The file is at `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md` and needs extensive updates. Since `save_project_file` requires full file content, the most efficient approach is to complete all remaining Edit tool calls on the local file, then save via the MCP tool. Key remaining changes:

   - D074 table line 44: `**0.802±0.024** (n=3)` → `**0.798±0.022** (n=4)`, `+3.5pp` → `+3.1pp`
   - Line 45: `-2.9pp` → `-2.5pp`
   - Line 46: `d≈1.03` → `d≈1.05`, pooled means update
   - Line 49: ANOVA interaction F/p/η²
   - Lines 52-53: Main effect F/p/η² stats
   - Line 57-58: Cell 4 data and vs-Vanilla stats
   - Lines 101-102: Core Insight ANOVA stats
   - Lines 143-144: C1 contribution stats
   - Line 150: 14→15 seeds
   - Line 152: C3 contribution Cell 4 stats
   - Line 168: v2 Evidence table Cell 4 row
   - Lines 171-172: Completion status and ANOVA summary
   - Line 190: Status line
   - Line 273: Risk ranking
   
   After paper_framing.md, proceed to Phase 5: compile PDF with `pdflatex + bibtex + pdflatex + pdflatex` on server westd-10894 (project code root) and verify 0 errors.

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/f5f30872-6952-4d1d-bd6a-41a4de679647.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "e6f55f7b-2fa5-4803-880d-b3db58e97b25",
  "isSynthetic": true
}
```

</details>

---


### Assistant

_source line 1186_

<details><summary>Logged reasoning block</summary>

```text
I need to continue updating paper_framing.md with all remaining Cell 4 n=4 statistics, then compile the LaTeX PDF. Let me first read the current state of paper_framing.md to see what edits are still needed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "f99bafbd-32e7-45e2-aae8-b505e19291b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012v3pWQ8g2kBugxaDyDWUPL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16911,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16911
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


### Tool call

_source line 1187_

<details open><summary>🔧 Tool call — Read · `toolu_014xk4J14qFCpYeUbLaa23he`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "903effaa-1177-4da7-8984-3ba6adb79281",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012v3pWQ8g2kBugxaDyDWUPL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16911,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16911
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

_source line 1188 · 2026-05-28T10:04:27.494Z_

<details><summary>↩ Tool result · `toolu_014xk4J14qFCpYeUbLaa23he`</summary>

```text
1	# OccSafe-VLA — Paper Framing
2	
3	> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)
4	>
5	> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。"ordinal interaction" framing 改为 "dual main effects + practical threshold crossing"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。
6	
7	## Architecture Facts (from code, verified)
8	- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）
9	- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。
10	- **FocalLoss**: α=0.25, γ=2.0
11	- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)
12	- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）
13	- **LoRA**: rank=32, alpha=16, dropout=0.0
14	- **GPU**: 4× RTX PRO 6000 98GB per server
15	- **训练时间**: ~12.9h/run @ 1.08 it/s
16	
17	### 叙事含义
18	- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。
19	  比"仅改善 DINOv2"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。
20	- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 "lightweight auxiliary" 叙事
21	- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐"放手"让 action loss 主导，
22	  可论证为"先学空间结构，再精化动作"的课程学习效果
23	- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守
24	
25	### DepthHead (新增, 2026-05-22)
26	- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）
27	- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）
28	- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64
29	- **参数量**: ~1.2M（与 OccHead 同量级）
30	
31	## Core Insight (D043 Plan B, 2026-05-26)
32	
33	**假设演变**：
34	- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence
35	- D017-D019：梯度流是防止损害的条件，非提供收益的条件
36	- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**
37	- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**
38	
39	### D074 v2 Factorial — Dual Main Effects（当前权威数据）
40	
41	| | BN | LN | Δ(LN-BN) |
42	|--|----|----|-----------|
43	| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |
44	| **Gradient OFF** | 0.767±0.024 (n=4) | **0.802±0.024** (n=3) | **+3.5pp** |
45	| Δ(ON-OFF) | **-4.2pp** | **-2.9pp** | — |
46	| **主效应** | BN pooled: 0.746 | LN pooled: 0.788 | **+4.2pp (d≈1.03)** |
47	| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |
48	
49	**ANOVA 交互项**: F=0.10, p=0.763, η²=0.005。两行斜率几乎相同 (BN: -4.2pp, LN: -2.9pp)，纯可加模型。
50	
51	**关键发现（D074 更新）**：
52	- **Gradient flow 主效应**: ON pooled (0.749) < OFF pooled (0.785), Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全
53	- **Normalization 主效应**: LN pooled (0.788) > BN pooled (0.746), Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致优于 BN
54	- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla
55	- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分
56	- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding
57	- ✅ Cell 4 n=3 完成: [0.826, 0.802, 0.778], mean=0.802±0.024
58	- Cell 4 vs Vanilla: Cohen's d=2.36, p=0.045
59	
60	### v1 → v2 数据不一致 [v1-SUPERSEDED]
61	
62	v1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。
63	**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。
64	
65	### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）
66	
67	### 机制证据状态（D056 v2 验证完成）
68	
69	**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：
70	- v1 结果：Detach gradient norms = 1-13% of Vanilla — "灾难性崩塌"（逐层分析, 200 真实样本）
71	- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）
72	- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**
73	- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做
74	- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证
75	
76	**v2 Gradient Analysis (D056/D057) — 部分有效**：
77	- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认
78	- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足
79	- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)
80	- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**
81	
82	**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：
83	- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除
84	- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常
85	- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移
86	- BN forward-pass 并未导致表征退化 — "BN interference" 假设不成立
87	
88	**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：
89	所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。
90	v2 存活的机制信号：
91	- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突
92	- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)
93	- ❌ "capacity competition" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据
94	- ❌ "BN forward-pass interference" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好
95	- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim
96	
97	### Core Insight（D074 修正）
98	
99	VLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：
100	
101	1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害
102	2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件
103	3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）
104	
105	**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。
106	
107	**机制层面（D057 修正）**：
108	- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突
109	- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）
110	- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证
111	- 空间内容仍然次要
112	
113	**论文策略选项**（Reviewer 建议）：
114	- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h
115	- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响
116	- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary
117	
118	### 措辞约束（D057 更新）
119	- **禁止** "crossover interaction" — v2 是 ordinal
120	- **禁止** "statistically significant interaction" / "significant interaction effect" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)
121	- **谨慎** "interaction" 单独使用 — 改用 "normalization-dependent gradient flow effect" 或 "dual main effects"
122	- **禁止** "BN-mediated gradient calibration" / "existence regularization" — v1 不可复现
123	- **禁止** 引用 v1/v2 梯度数值的跨方法论比较
124	- **谨慎** "gradient collapse" / "no gradient collapse" — 待同方法论验证，暂不 claim
125	- **可用** "gradient orthogonality"（v2 确认）— 排除直接梯度冲突
126	- **可用** "capacity competition" / "BN forward-pass interference"（需标注为假设，待 CKA 验证）
127	- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著
128	- Cell 1 高方差本身可作为 finding：用 "BN+gradient flow leads to unstable training"
129	- Gradient flow 主效应用 "detrimental" / "harmful"，不用 "collapse"（collapse 特指 detach 极端情况）
130	
131	**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。
132	
133	## Framing Strategy (D019 修正)
134	
135	**确定路线: Option B 分析论文**（Reviewer 审查通过）
136	
137	**核心叙事转变 (D026)**：从"梯度流是必要条件"→"梯度流防止 encoder gradient collapse"（具体机制，非抽象论断）
138	
139	**Title（暂定）**: "Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis"
140	
141	**3-Contribution 结构（D043 Plan B 修正）**：
142	- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：
143	  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全
144	  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势
145	  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**
146	  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)
147	  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定
148	  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla
149	  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变
150	  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证
151	- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）
152	- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)
153	- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla
154	
155	## Core Contribution Evidence
156	
157	### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)
158	v1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。
159	v2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。
160	
161	### v2 Factorial Evidence (D043, 权威数据)
162	
163	| Cell | Condition | n | CAR values | mean±std | 代码版本 |
164	|------|-----------|---|-----------|----------|---------|
165	| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |
166	| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |
167	| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |
168	| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |
169	| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |
170	
171	✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。
172	✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。
173	
174	### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]
175	
176	**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**
177	
178	**CKA Evidence [v1-SUPERSEDED]**：
179	- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）
180	- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化
181	- **"BN = 100% 表征漂移原因" 不再成立** — v2 中 BN 不导致 CKA 退化
182	
183	**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：
184	v1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。
185	
186	**两种失败模式（D031, 仍有效）**：
187	- Detach = 均匀退化 (per-task CAR std=0.002)
188	- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)
189	
190	**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。
191	
192	### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]
193	- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，"BN interference" 假设不成立
194	- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）
195	- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证
196	- ⚠️ v1 的 "existence regularization" / "BN-mediated calibration" 不再成立
197	- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突
198	
199	### Claim 3: Spatial Content Secondary
200	v1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。
201	Depth = Vanilla exactly (4 seeds, D022)。空间内容次要。
202	⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。
203	
204	### Claim 4 (Depth): ✅ Confirmed (D022)
205	Depth CAR = 0.780 = Vanilla exactly (4 seeds)。
206	
207	## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）
208	
209	**【Pass（必须同时满足）】**
210	1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）
211	2. Depth 4-seed mean TSR ≥ 0.870
212	
213	**【Fail（满足任一）】**
214	1. Depth 4-seed mean CAR < 0.780
215	2. Depth 4-seed mean TSR < 0.870
216	
217	## Anticipated Reviewer Concerns
218	
219	### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED
220	### RC2 [HIGH]: "Why Not Just Use CBF?" — Defense: zero inference cost + complementarity
221	### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)
222	### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations
223	### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations
224	### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI
225	
226	## 待定关键实验
227	
228	### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)
229	替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。
230	- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)
231	- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)
232	- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠
233	- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移
234	
235	### Cutoff Temporal Dynamics (D029/D030/D041)
236	
237	**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。
238	
239	**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**
240	cutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。
241	
242	| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |
243	|------|--------|--------|--------|------|-----------|
244	| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |
245	| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |
246	| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |
247	| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |
248	| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |
249	| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |
250	
251	**安全 claim（D041 限缩后）**：
252	1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本
253	2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）
254	3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）
255	4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim
256	
257	**不安全 claim**：任何特定 cutoff 点优于另一个、非单调"sweet spot"。
258	
259	**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。
260	
261	### Same-Seed 梯度重分析 — 条件式 (D028)
262	当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：
263	- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓
264	- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异
265	- **Scenario C**: 需两版分析（BN 和 LN）
266	Fig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 "旧 round"。
267	
268	## Framing Risk Ranking (D043 Plan B 更新)
269	
270	| 排名 | 风险 | 状态 | 应对 |
271	|------|------|------|------|
272	| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |
273	| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |
274	| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 "无害" 但非 "有益" | ✅ 已定性 | 论文用 "statistically indistinguishable"，不 claim positive |
275	| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |
276	| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |
277	| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |
278	
279	## 目标会议
280	**CoRL 2026**: Abstract May 26, Paper May 29
281	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "4b3c23fe-0064-4ee3-b603-7ec2c503def8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
      "content": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.802±0.024** (n=3) | **+3.5pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.9pp** | — |\n| **主效应** | BN pooled: 0.746 | LN pooled: 0.788 | **+4.2pp (d≈1.03)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.10, p=0.763, η²=0.005。两行斜率几乎相同 (BN: -4.2pp, LN: -2.9pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.749) < OFF pooled (0.785), Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.788) > BN pooled (0.746), Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=3 完成: [0.826, 0.802, 0.778], mean=0.802±0.024\n- Cell 4 vs Vanilla: Cohen's d=2.36, p=0.045\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
      "numLines": 281,
      "startLine": 1,
      "totalLines": 281
    }
  }
}
```

</details>

---


### Assistant

_source line 1189_

Now I have the full file. Let me make all the remaining edits to paper_framing.md.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "017f51a2-9a2e-403c-82a2-a567a0506888",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rsQ87xpAegwtuhY9ANETX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9374,
      "cache_read_input_tokens": 28756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9374
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

_source line 1190_

<details open><summary>🔧 Tool call — Read · `toolu_01P6w1hmVJjqnpqwTT9jipW2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/anova_v2_final.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "89e5a01f-1490-4ee5-8c16-38777c0bd5da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rsQ87xpAegwtuhY9ANETX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9374,
      "cache_read_input_tokens": 28756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9374
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

_source line 1191 · 2026-05-28T10:04:32.301Z_

<details><summary>↩ Tool result · `toolu_01P6w1hmVJjqnpqwTT9jipW2`</summary>

```text
1	======================================================================
2	2x2 FACTORIAL ANOVA: gradient_flow x norm_type on CAR (v2 data)
3	Date: 2026-05-28
4	======================================================================
5	
6	--- Cell Descriptives ---
7	  Cell 1 (Full OCC BN, grad ON + BN): n=3, mean=0.7253, SD=0.0636, range=[0.654, 0.776]
8	  Cell 2 (Full OCC LN, grad ON + LN): n=4, mean=0.7730, SD=0.0271, range=[0.740, 0.798]
9	  Cell 3 (Detach BN, grad OFF + BN): n=4, mean=0.7665, SD=0.0242, range=[0.736, 0.794]
10	  Cell 4 (Detach LN, grad OFF + LN): n=4, mean=0.7975, SD=0.0216, range=[0.778, 0.826]
11	  Vanilla baseline:                    n=3, mean=0.7453, SD=0.0241, range=[0.720, 0.768]
12	
13	--- Marginal Means ---
14	  Gradient ON:  mean=0.7526 (n=7)
15	  Gradient OFF: mean=0.7820 (n=8)
16	  BN:           mean=0.7489 (n=7)
17	  LN:           mean=0.7853 (n=8)
18	
19	======================================================================
20	2x2 FACTORIAL ANOVA (Type III Sum of Squares)
21	======================================================================
22	
23	Source                                                     SS    df          F          p       η²_p
24	-------------------------------------------------------------------------------------
25	  C(gradient_flow)                                   0.003980     1      3.259     0.0985     0.2285
26	  C(norm_type)                                       0.005712     1      4.676     0.0535     0.2983
27	  C(gradient_flow)                                   0.000256     1      0.210     0.6558     0.0187
28	  Residual                                           0.013437    11
29	-------------------------------------------------------------------------------------
30	Significance: *** p<.001, ** p<.01, * p<.05, † p<.10
31	
32	======================================================================
33	WELCH'S T-TESTS: Each Cell vs Vanilla
34	======================================================================
35	
36	Vanilla: mean=0.7453, SD=0.0241, n=3
37	
38	Cell                                                   mean        t  p(2-tail)    Cohen d
39	------------------------------------------------------------------------------------------
40	  Cell 1 (Full OCC BN, grad ON + BN)                 0.7253   -0.510     0.6510     -0.416
41	  Cell 2 (Full OCC LN, grad ON + LN)                 0.7730    1.425     0.2164      1.067
42	  Cell 3 (Detach BN, grad OFF + BN)                  0.7665    1.147     0.3091      0.875
43	  Cell 4 (Detach LN, grad OFF + LN)                  0.7975    2.963     0.0398      2.307
44	
45	======================================================================
46	SIMPLE EFFECTS: LN-BN within each gradient condition
47	======================================================================
48	
49	  Under gradient ON:  LN-BN = 0.7730 - 0.7253 = +0.0477 (+4.8pp)
50	  Under gradient OFF: LN-BN = 0.7975 - 0.7665 = +0.0310 (+3.1pp)
51	
52	  Cell 4 vs Vanilla: Cohen's d=2.31, t=2.963, p=0.040
53	  Cell 2 vs Vanilla: Cohen's d=+1.07
54	
55	======================================================================
56	SUMMARY
57	======================================================================
58	  Gradient flow: F=3.26, p=0.098, η²=0.229
59	  Norm type:     F=4.68, p=0.053, η²=0.298
60	  Interaction:   F=0.21, p=0.656, η²=0.019
61	
62	  Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040
63	  Cell 2 vs Vanilla: d=+1.07
64	  LN-BN under gradient ON:  +4.8pp
65	  LN-BN under gradient OFF: +3.1pp
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "39a50274-be03-4715-a1f2-e78098522e28",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/anova_v2_final.txt",
      "content": "======================================================================\n2x2 FACTORIAL ANOVA: gradient_flow x norm_type on CAR (v2 data)\nDate: 2026-05-28\n======================================================================\n\n--- Cell Descriptives ---\n  Cell 1 (Full OCC BN, grad ON + BN): n=3, mean=0.7253, SD=0.0636, range=[0.654, 0.776]\n  Cell 2 (Full OCC LN, grad ON + LN): n=4, mean=0.7730, SD=0.0271, range=[0.740, 0.798]\n  Cell 3 (Detach BN, grad OFF + BN): n=4, mean=0.7665, SD=0.0242, range=[0.736, 0.794]\n  Cell 4 (Detach LN, grad OFF + LN): n=4, mean=0.7975, SD=0.0216, range=[0.778, 0.826]\n  Vanilla baseline:                    n=3, mean=0.7453, SD=0.0241, range=[0.720, 0.768]\n\n--- Marginal Means ---\n  Gradient ON:  mean=0.7526 (n=7)\n  Gradient OFF: mean=0.7820 (n=8)\n  BN:           mean=0.7489 (n=7)\n  LN:           mean=0.7853 (n=8)\n\n======================================================================\n2x2 FACTORIAL ANOVA (Type III Sum of Squares)\n======================================================================\n\nSource                                                     SS    df          F          p       η²_p\n-------------------------------------------------------------------------------------\n  C(gradient_flow)                                   0.003980     1      3.259     0.0985     0.2285\n  C(norm_type)                                       0.005712     1      4.676     0.0535     0.2983\n  C(gradient_flow)                                   0.000256     1      0.210     0.6558     0.0187\n  Residual                                           0.013437    11\n-------------------------------------------------------------------------------------\nSignificance: *** p<.001, ** p<.01, * p<.05, † p<.10\n\n======================================================================\nWELCH'S T-TESTS: Each Cell vs Vanilla\n======================================================================\n\nVanilla: mean=0.7453, SD=0.0241, n=3\n\nCell                                                   mean        t  p(2-tail)    Cohen d\n------------------------------------------------------------------------------------------\n  Cell 1 (Full OCC BN, grad ON + BN)                 0.7253   -0.510     0.6510     -0.416\n  Cell 2 (Full OCC LN, grad ON + LN)                 0.7730    1.425     0.2164      1.067\n  Cell 3 (Detach BN, grad OFF + BN)                  0.7665    1.147     0.3091      0.875\n  Cell 4 (Detach LN, grad OFF + LN)                  0.7975    2.963     0.0398      2.307\n\n======================================================================\nSIMPLE EFFECTS: LN-BN within each gradient condition\n======================================================================\n\n  Under gradient ON:  LN-BN = 0.7730 - 0.7253 = +0.0477 (+4.8pp)\n  Under gradient OFF: LN-BN = 0.7975 - 0.7665 = +0.0310 (+3.1pp)\n\n  Cell 4 vs Vanilla: Cohen's d=2.31, t=2.963, p=0.040\n  Cell 2 vs Vanilla: Cohen's d=+1.07\n\n======================================================================\nSUMMARY\n======================================================================\n  Gradient flow: F=3.26, p=0.098, η²=0.229\n  Norm type:     F=4.68, p=0.053, η²=0.298\n  Interaction:   F=0.21, p=0.656, η²=0.019\n\n  Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040\n  Cell 2 vs Vanilla: d=+1.07\n  LN-BN under gradient ON:  +4.8pp\n  LN-BN under gradient OFF: +3.1pp",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---


### Assistant

_source line 1192_

Good, I have the authoritative ANOVA output. Now I'll apply all remaining edits to paper_framing.md systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "562f45f5-2016-4c6f-b444-3c5542bf5644",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UCxsgaD1xpNiVwuiJMvsJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1331,
      "cache_read_input_tokens": 38130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1331
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

_source line 1193_

<details open><summary>🔧 Tool call — Edit · `toolu_01BLKfZjhkRfScb3y9XcM3v9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "| **Gradient OFF** | 0.767±0.024 (n=4) | **0.802±0.024** (n=3) | **+3.5pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.9pp** | — |\n| **主效应** | BN pooled: 0.746 | LN pooled: 0.788 | **+4.2pp (d≈1.03)** |",
  "new_string": "| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "8248cc01-9da1-4ca0-ae63-c75eab385888",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UCxsgaD1xpNiVwuiJMvsJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1331,
      "cache_read_input_tokens": 38130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1331
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

_source line 1194 · 2026-05-28T10:04:40.758Z_

<details><summary>↩ Tool result · `toolu_01BLKfZjhkRfScb3y9XcM3v9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "8f85213d-353b-41ba-b40a-4e7cd29040c2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "| **Gradient OFF** | 0.767±0.024 (n=4) | **0.802±0.024** (n=3) | **+3.5pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.9pp** | — |\n| **主效应** | BN pooled: 0.746 | LN pooled: 0.788 | **+4.2pp (d≈1.03)** |",
    "newString": "| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.802±0.024** (n=3) | **+3.5pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.9pp** | — |\n| **主效应** | BN pooled: 0.746 | LN pooled: 0.788 | **+4.2pp (d≈1.03)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.10, p=0.763, η²=0.005。两行斜率几乎相同 (BN: -4.2pp, LN: -2.9pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.749) < OFF pooled (0.785), Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.788) > BN pooled (0.746), Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=3 完成: [0.826, 0.802, 0.778], mean=0.802±0.024\n- Cell 4 vs Vanilla: Cohen's d=2.36, p=0.045\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 41,
        "oldLines": 9,
        "newStart": 41,
        "newLines": 9,
        "lines": [
          " | | BN | LN | Δ(LN-BN) |",
          " |--|----|----|-----------|",
          " | **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |",
          "-| **Gradient OFF** | 0.767±0.024 (n=4) | **0.802±0.024** (n=3) | **+3.5pp** |",
          "-| Δ(ON-OFF) | **-4.2pp** | **-2.9pp** | — |",
          "-| **主效应** | BN pooled: 0.746 | LN pooled: 0.788 | **+4.2pp (d≈1.03)** |",
          "+| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |",
          "+| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |",
          "+| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |",
          " | Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |",
          " ",
          " **ANOVA 交互项**: F=0.10, p=0.763, η²=0.005。两行斜率几乎相同 (BN: -4.2pp, LN: -2.9pp)，纯可加模型。"
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

_source line 1195_

<details open><summary>🔧 Tool call — Edit · `toolu_0196sgs9zaQpvqe4uhu6Gq5g`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "**ANOVA 交互项**: F=0.10, p=0.763, η²=0.005。两行斜率几乎相同 (BN: -4.2pp, LN: -2.9pp)，纯可加模型。",
  "new_string": "**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "955d84da-1ec8-4668-96e3-485cbb8f6428",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvwtwvX9r8pqxK7k4riJaK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 462,
      "cache_read_input_tokens": 39461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 462
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

_source line 1196 · 2026-05-28T10:04:46.062Z_

<details><summary>↩ Tool result · `toolu_0196sgs9zaQpvqe4uhu6Gq5g`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "a7e0c358-7d4d-4c73-88dd-316759b73056",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "**ANOVA 交互项**: F=0.10, p=0.763, η²=0.005。两行斜率几乎相同 (BN: -4.2pp, LN: -2.9pp)，纯可加模型。",
    "newString": "**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.10, p=0.763, η²=0.005。两行斜率几乎相同 (BN: -4.2pp, LN: -2.9pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.749) < OFF pooled (0.785), Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.788) > BN pooled (0.746), Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=3 完成: [0.826, 0.802, 0.778], mean=0.802±0.024\n- Cell 4 vs Vanilla: Cohen's d=2.36, p=0.045\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 46,
        "oldLines": 7,
        "newStart": 46,
        "newLines": 7,
        "lines": [
          " | **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |",
          " | Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |",
          " ",
          "-**ANOVA 交互项**: F=0.10, p=0.763, η²=0.005。两行斜率几乎相同 (BN: -4.2pp, LN: -2.9pp)，纯可加模型。",
          "+**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。",
          " ",
          " **关键发现（D074 更新）**：",
          " - **Gradient flow 主效应**: ON pooled (0.749) < OFF pooled (0.785), Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全"
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

_source line 1197_

<details open><summary>🔧 Tool call — Edit · `toolu_019hEr9XYLXjc3PXW27JE6Wp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "- **Gradient flow 主效应**: ON pooled (0.749) < OFF pooled (0.785), Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.788) > BN pooled (0.746), Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致优于 BN",
  "new_string": "- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "a7f64a16-f654-4207-beae-853e7d1f4ba8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQ736gF9nSAXhzip3gFBK8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 323,
      "cache_read_input_tokens": 39923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 323
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

_source line 1198 · 2026-05-28T10:04:52.862Z_

<details><summary>↩ Tool result · `toolu_019hEr9XYLXjc3PXW27JE6Wp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "f7f5ca44-3d42-4f39-928f-56dc3319c837",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "- **Gradient flow 主效应**: ON pooled (0.749) < OFF pooled (0.785), Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.788) > BN pooled (0.746), Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致优于 BN",
    "newString": "- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.749) < OFF pooled (0.785), Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.788) > BN pooled (0.746), Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=3 完成: [0.826, 0.802, 0.778], mean=0.802±0.024\n- Cell 4 vs Vanilla: Cohen's d=2.36, p=0.045\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 49,
        "oldLines": 8,
        "newStart": 49,
        "newLines": 8,
        "lines": [
          " **ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。",
          " ",
          " **关键发现（D074 更新）**：",
          "-- **Gradient flow 主效应**: ON pooled (0.749) < OFF pooled (0.785), Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全",
          "-- **Normalization 主效应**: LN pooled (0.788) > BN pooled (0.746), Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致优于 BN",
          "+- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全",
          "+- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN",
          " - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla",
          " - **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分",
          " - **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding"
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

_source line 1199_

<details open><summary>🔧 Tool call — Edit · `toolu_018J3ihePrurv8Ro43zMk59C`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "- ✅ Cell 4 n=3 完成: [0.826, 0.802, 0.778], mean=0.802±0.024\n- Cell 4 vs Vanilla: Cohen's d=2.36, p=0.045",
  "new_string": "- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "ddf8c975-2d66-48dc-935d-f4a0bc7b54d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127uuUjtwhFctcQgNLn8dvW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 461,
      "cache_read_input_tokens": 40246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 461
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

_source line 1200 · 2026-05-28T10:04:57.766Z_

<details><summary>↩ Tool result · `toolu_018J3ihePrurv8Ro43zMk59C`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "985825df-6108-49c3-8cfe-3d3c3909869e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "- ✅ Cell 4 n=3 完成: [0.826, 0.802, 0.778], mean=0.802±0.024\n- Cell 4 vs Vanilla: Cohen's d=2.36, p=0.045",
    "newString": "- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=3 完成: [0.826, 0.802, 0.778], mean=0.802±0.024\n- Cell 4 vs Vanilla: Cohen's d=2.36, p=0.045\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 54,
        "oldLines": 8,
        "newStart": 54,
        "newLines": 8,
        "lines": [
          " - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla",
          " - **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分",
          " - **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding",
          "-- ✅ Cell 4 n=3 完成: [0.826, 0.802, 0.778], mean=0.802±0.024",
          "-- Cell 4 vs Vanilla: Cohen's d=2.36, p=0.045",
          "+- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022",
          "+- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040",
          " ",
          " ### v1 → v2 数据不一致 [v1-SUPERSEDED]",
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

_source line 1201_

<details open><summary>🔧 Tool call — Edit · `toolu_019WdRULEGC1DenNYXwfUnd6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件",
  "new_string": "1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "38c76d22-428e-4b2c-adf3-3a254ef03e02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GohgNgUvBGFyNU2rvTt8Dm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 322,
      "cache_read_input_tokens": 40707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 322
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

_source line 1202 · 2026-05-28T10:05:03.911Z_

<details><summary>↩ Tool result · `toolu_019WdRULEGC1DenNYXwfUnd6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "19b5c0f7-3e01-4df9-b500-cbaedd90e4f8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件",
    "newString": "1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 98,
        "oldLines": 8,
        "newStart": 98,
        "newLines": 8,
        "lines": [
          " ",
          " VLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：",
          " ",
          "-1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.6pp, F=3.20, p=0.104），Detach 消除损害",
          "-2. **Normalization 主效应**: LN 一致优于 BN（Δ=+4.2pp, F=4.49, p=0.060, d≈1.03），独立于 gradient flow 条件",
          "+1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害",
          "+2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件",
          " 3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）",
          " ",
          " **行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。"
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

_source line 1203_

<details open><summary>🔧 Tool call — Edit · `toolu_01MQwD36ptZtcC21hdHNCEKY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势",
  "new_string": "  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致提供安全优势"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "a5c229ea-95eb-47a7-9127-0bcf6e468ee4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GS7uBJCvxHEMgcJ4vqjUv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 41029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 421
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

_source line 1204 · 2026-05-28T10:05:10.438Z_

<details><summary>↩ Tool result · `toolu_01MQwD36ptZtcC21hdHNCEKY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "68ec267e-045a-4676-a36e-32942c00c627",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势",
    "newString": "  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致提供安全优势",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 140,
        "oldLines": 8,
        "newStart": 140,
        "newLines": 8,
        "lines": [
          " ",
          " **3-Contribution 结构（D043 Plan B 修正）**：",
          " - **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：",
          "-  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.6pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全",
          "-  - **Normalization 主效应 (d≈1.03)**: LN > BN, Δ=+4.2pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势",
          "+  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全",
          "+  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致提供安全优势",
          "   - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**",
          "   - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)",
          "   - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定"
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

_source line 1205_

<details open><summary>🔧 Tool call — Edit · `toolu_01MVgJSdDnvvSaqN1i5ctfHX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证",
  "new_string": "  - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "58f71200-344a-43c0-9e66-33b6619f7f6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yWZVCp884EZioE4QQu8pH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 41450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 656
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

_source line 1206 · 2026-05-28T10:05:14.137Z_

<details><summary>↩ Tool result · `toolu_01MVgJSdDnvvSaqN1i5ctfHX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "49749995-5de6-46f3-aa7c-df42fa4b44ee",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证",
    "newString": "  - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 147,
        "oldLines": 7,
        "newStart": 147,
        "newLines": 7,
        "lines": [
          "   - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定",
          "   - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla",
          "   - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变",
          "-  - ✅ 全部 14 seeds 完成, ANOVA v2 final 已验证",
          "+  - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证",
          " - **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）",
          " - **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)",
          " - **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla"
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

_source line 1207_

<details open><summary>🔧 Tool call — Edit · `toolu_018rnzKoibw44u76BULuMNyG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)",
  "new_string": "最优：Detach + LN (0.798±0.022, n=4, d=2.31 vs Vanilla, p=0.040)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "b965d75c-0d1e-4079-b920-33e267ff3560",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0124xgBsnh7epxS5o9RiRnL2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 42106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 247
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

_source line 1208 · 2026-05-28T10:05:18.257Z_

<details><summary>↩ Tool result · `toolu_018rnzKoibw44u76BULuMNyG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "d3604506-35e6-41fc-9456-1ff40db5fc04",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)",
    "newString": "最优：Detach + LN (0.798±0.022, n=4, d=2.31 vs Vanilla, p=0.040)",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 149,
        "oldLines": 7,
        "newStart": 149,
        "newLines": 7,
        "lines": [
          "   - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变",
          "   - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证",
          " - **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）",
          "-- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, d=2.36 vs Vanilla, p=0.045)",
          "+- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.798±0.022, n=4, d=2.31 vs Vanilla, p=0.040)",
          " - **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla",
          " ",
          " ## Core Contribution Evidence"
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

_source line 1209_

Now update the v2 Evidence table (Cell 4 row):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "1aefba8b-928d-4d68-81a7-b28f7fd54436",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LntZ1bL8bMvdGG39xcY9za",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 42353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 1210_

<details open><summary>🔧 Tool call — Edit · `toolu_01TQptUfdRtik5cWAecxic6f`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |",
  "new_string": "| 4 | Detach LN (Grad OFF + LN) | 4 | 0.826, 0.802, 0.778, 0.784 | 0.798±0.022 | **v2** ✅ |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "cce251bb-02d9-4b82-b3a4-0758fc5f2aa6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LntZ1bL8bMvdGG39xcY9za",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 42353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 1211 · 2026-05-28T10:05:23.170Z_

<details><summary>↩ Tool result · `toolu_01TQptUfdRtik5cWAecxic6f`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "f31f143f-7f17-4ab6-857c-672513d744e9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |",
    "newString": "| 4 | Detach LN (Grad OFF + LN) | 4 | 0.826, 0.802, 0.778, 0.784 | 0.798±0.022 | **v2** ✅ |",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.798±0.022, n=4, d=2.31 vs Vanilla, p=0.040)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 165,
        "oldLines": 7,
        "newStart": 165,
        "newLines": 7,
        "lines": [
          " | 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |",
          " | 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |",
          " | 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |",
          "-| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ |",
          "+| 4 | Detach LN (Grad OFF + LN) | 4 | 0.826, 0.802, 0.778, 0.784 | 0.798±0.022 | **v2** ✅ |",
          " | — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |",
          " ",
          " ✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。"
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

_source line 1212_

<details open><summary>🔧 Tool call — Edit · `toolu_0134JBDBwUgd56mWfnGGt32r`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。",
  "new_string": "✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=4 ✅; Vanilla n=3 ✅。共 N=15+3=18。\n✅ **ANOVA v2 final**: F(gradient)=3.26, p=0.098; F(norm)=4.68, p=0.053; F(interaction)=0.21, p=0.656。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "00909f18-0fdd-44a9-830d-929423449260",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WAFyY1SDbHcEky8tEosDs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 42618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 328
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

_source line 1213 · 2026-05-28T10:05:29.328Z_

<details><summary>↩ Tool result · `toolu_0134JBDBwUgd56mWfnGGt32r`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "ef2f2bc7-32a2-4e7f-be67-0f2ac8f6d97c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。",
    "newString": "✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=4 ✅; Vanilla n=3 ✅。共 N=15+3=18。\n✅ **ANOVA v2 final**: F(gradient)=3.26, p=0.098; F(norm)=4.68, p=0.053; F(interaction)=0.21, p=0.656。",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.798±0.022, n=4, d=2.31 vs Vanilla, p=0.040)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 4 | 0.826, 0.802, 0.778, 0.784 | 0.798±0.022 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。\n✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 168,
        "oldLines": 8,
        "newStart": 168,
        "newLines": 8,
        "lines": [
          " | 4 | Detach LN (Grad OFF + LN) | 4 | 0.826, 0.802, 0.778, 0.784 | 0.798±0.022 | **v2** ✅ |",
          " | — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |",
          " ",
          "-✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅; Vanilla n=3 ✅。共 N=14+3=17。",
          "-✅ **ANOVA v2 final**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。",
          "+✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=4 ✅; Vanilla n=3 ✅。共 N=15+3=18。",
          "+✅ **ANOVA v2 final**: F(gradient)=3.26, p=0.098; F(norm)=4.68, p=0.053; F(interaction)=0.21, p=0.656。",
          " ",
          " ### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]",
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

_source line 1214_

<details open><summary>🔧 Tool call — Edit · `toolu_019bt7mSFjcpKhCCYbP3w5Qf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。",
  "new_string": "**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=4 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "ef1b8e62-6b31-4565-b723-b27e07adfa53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zuJSw9HgKenntwYbrKwfL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 42946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 1215 · 2026-05-28T10:05:34.254Z_

<details><summary>↩ Tool result · `toolu_019bt7mSFjcpKhCCYbP3w5Qf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "55c66ef4-4bd4-4840-81d5-b19fc22a55dd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。",
    "newString": "**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=4 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.798±0.022, n=4, d=2.31 vs Vanilla, p=0.040)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 4 | 0.826, 0.802, 0.778, 0.784 | 0.798±0.022 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=4 ✅; Vanilla n=3 ✅。共 N=15+3=18。\n✅ **ANOVA v2 final**: F(gradient)=3.26, p=0.098; F(norm)=4.68, p=0.053; F(interaction)=0.21, p=0.656。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 187,
        "oldLines": 7,
        "newStart": 187,
        "newLines": 7,
        "lines": [
          " - Detach = 均匀退化 (per-task CAR std=0.002)",
          " - Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)",
          " ",
          "-**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。",
          "+**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=4 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。",
          " ",
          " ### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]",
          " - ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立"
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

_source line 1216_

<details open><summary>🔧 Tool call — Edit · `toolu_01WrW5J6cFm6pu7ww6Exa6ZH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |",
  "new_string": "| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=15, F/p/η² 已验证。Cell 4 vs Vanilla p=0.040 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "c4ee8e29-964d-4522-87ab-862f09d4e6df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYXM3VnySaLwqvBUh7SaC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 43409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 371
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

_source line 1217 · 2026-05-28T10:05:38.860Z_

<details><summary>↩ Tool result · `toolu_01WrW5J6cFm6pu7ww6Exa6ZH`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "2434c6d2-2234-4b87-8c7e-6534367bc972",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |",
    "newString": "| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=15, F/p/η² 已验证。Cell 4 vs Vanilla p=0.040 |",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.798±0.022, n=4, d=2.31 vs Vanilla, p=0.040)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 4 | 0.826, 0.802, 0.778, 0.784 | 0.798±0.022 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=4 ✅; Vanilla n=3 ✅。共 N=15+3=18。\n✅ **ANOVA v2 final**: F(gradient)=3.26, p=0.098; F(norm)=4.68, p=0.053; F(interaction)=0.21, p=0.656。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=4 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 270,
        "oldLines": 7,
        "newStart": 270,
        "newLines": 7,
        "lines": [
          " | 排名 | 风险 | 状态 | 应对 |",
          " |------|------|------|------|",
          " | **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |",
          "-| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla p=0.045 |",
          "+| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=15, F/p/η² 已验证。Cell 4 vs Vanilla p=0.040 |",
          " | **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |",
          " | **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |",
          " | **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |"
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

_source line 1218_

Now update the header status line (d≈1.03 → d≈1.05, F/p stats):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "412a9f28-8a2f-4b92-a2a8-633d471e016d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UNw84s2MuQZztDPBMAy96B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 307,
      "cache_read_input_tokens": 43780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 307
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

_source line 1219_

<details open><summary>🔧 Tool call — Edit · `toolu_01GaeiATCAZbwbeJYHJfXVt8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763)",
  "new_string": "v2 factorial: gradient flow 主效应 (Δ=-2.9pp) + normalization 主效应 (LN>BN, Δ=+3.6pp, d≈1.05); ANOVA interaction ≈ 0 (F=0.21, p=0.656)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "4f448395-5799-40d6-997f-65fc9955936c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UNw84s2MuQZztDPBMAy96B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 307,
      "cache_read_input_tokens": 43780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 307
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

_source line 1220 · 2026-05-28T10:05:44.163Z_

<details><summary>↩ Tool result · `toolu_01GaeiATCAZbwbeJYHJfXVt8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "513b5161-64e2-4089-bde8-6c887f3b0af0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763)",
    "newString": "v2 factorial: gradient flow 主效应 (Δ=-2.9pp) + normalization 主效应 (LN>BN, Δ=+3.6pp, d≈1.05); ANOVA interaction ≈ 0 (F=0.21, p=0.656)",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.798±0.022, n=4, d=2.31 vs Vanilla, p=0.040)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 4 | 0.826, 0.802, 0.778, 0.784 | 0.798±0.022 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=4 ✅; Vanilla n=3 ✅。共 N=15+3=18。\n✅ **ANOVA v2 final**: F(gradient)=3.26, p=0.098; F(norm)=4.68, p=0.053; F(interaction)=0.21, p=0.656。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=4 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=15, F/p/η² 已验证。Cell 4 vs Vanilla p=0.040 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " # OccSafe-VLA — Paper Framing",
          " ",
          "-> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-3.6pp) + normalization 主效应 (LN>BN, Δ=+4.2pp, d≈1.03); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)",
          "+> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-2.9pp) + normalization 主效应 (LN>BN, Δ=+3.6pp, d≈1.05); ANOVA interaction ≈ 0 (F=0.21, p=0.656); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)",
          " >",
          " > ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。",
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

_source line 1221_

Now update the "additive protection" section text referencing LN pooled mean and d≈1.03:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "16051e4b-0cd6-4889-a452-6f3bbb70ec4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JT3g9BYgTWsuKJS9MbeX5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 44087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 373
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

_source line 1222_

<details open><summary>🔧 Tool call — Edit · `toolu_01S23iZSURxm3CYj82xmfja4`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "d≈1.03",
  "new_string": "d≈1.05"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "0bad63ab-c5e2-496e-bfd7-9fb136b7b8b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JT3g9BYgTWsuKJS9MbeX5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 44087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 373
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

_source line 1223 · 2026-05-28T10:05:47.651Z_

<details><summary>↩ Tool result · `toolu_01S23iZSURxm3CYj82xmfja4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "49af3585-925f-4532-8b20-a4be1b30e1a8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "d≈1.03",
    "newString": "d≈1.05",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-2.9pp) + normalization 主效应 (LN>BN, Δ=+3.6pp, d≈1.05); ANOVA interaction ≈ 0 (F=0.21, p=0.656); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.798±0.022, n=4, d=2.31 vs Vanilla, p=0.040)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 4 | 0.826, 0.802, 0.778, 0.784 | 0.798±0.022 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=4 ✅; Vanilla n=3 ✅。共 N=15+3=18。\n✅ **ANOVA v2 final**: F(gradient)=3.26, p=0.098; F(norm)=4.68, p=0.053; F(interaction)=0.21, p=0.656。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=4 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=15, F/p/η² 已验证。Cell 4 vs Vanilla p=0.040 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " ",
          " > 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-2.9pp) + normalization 主效应 (LN>BN, Δ=+3.6pp, d≈1.05); ANOVA interaction ≈ 0 (F=0.21, p=0.656); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)",
          " >",
          "-> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。",
          "+> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.05) 作为 secondary claim。详见 D074。",
          " ",
          " ## Architecture Facts (from code, verified)",
          " - **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  }
}
```

</details>

---


### Assistant

_source line 1224_

Now update the C3 contribution LN advantage text (Δ=+4.2pp → +3.6pp):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "383f422d-e41c-4b2e-9885-7e1c7913bb7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTkWi6QFf1hQe3fqD3G7wP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 44460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 451
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

_source line 1225_

<details open><summary>🔧 Tool call — Edit · `toolu_01UDhMoFkkm6387jGc2k93cb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
  "old_string": "**用 LN 替代 BN** — LN 一致 +4.2pp 安全优势",
  "new_string": "**用 LN 替代 BN** — LN 一致 +3.6pp 安全优势"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "d00afe2e-09c3-4556-b192-50c73a20dec8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTkWi6QFf1hQe3fqD3G7wP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 44460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 451
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

_source line 1226 · 2026-05-28T10:05:54.202Z_

<details><summary>↩ Tool result · `toolu_01UDhMoFkkm6387jGc2k93cb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "5db52d59-599b-4a52-8b8d-40cda93f7c09",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
    "oldString": "**用 LN 替代 BN** — LN 一致 +4.2pp 安全优势",
    "newString": "**用 LN 替代 BN** — LN 一致 +3.6pp 安全优势",
    "originalFile": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-2.9pp) + normalization 主效应 (LN>BN, Δ=+3.6pp, d≈1.05); ANOVA interaction ≈ 0 (F=0.21, p=0.656); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=4。CoRL 2026 target (Paper May 29)\n>\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\"ordinal interaction\" framing 改为 \"dual main effects + practical threshold crossing\"。新增 normalization 主效应 (d≈1.05) 作为 secondary claim。详见 D074。\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D043 Plan B, 2026-05-26)\n\n**假设演变**：\n- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence\n- D017-D019：梯度流是防止损害的条件，非提供收益的条件\n- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**\n- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**\n\n### D074 v2 Factorial — Dual Main Effects（当前权威数据）\n\n| | BN | LN | Δ(LN-BN) |\n|--|----|----|-----------|\n| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |\n| **Gradient OFF** | 0.767±0.024 (n=4) | **0.798±0.022** (n=4) | **+3.1pp** |\n| Δ(ON-OFF) | **-4.2pp** | **-2.5pp** | — |\n| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |\n| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |\n\n**ANOVA 交互项**: F=0.21, p=0.656, η²=0.019。两行斜率几乎相同 (BN: -4.2pp, LN: -2.5pp)，纯可加模型。\n\n**关键发现（D074 更新）**：\n- **Gradient flow 主效应**: ON pooled (0.753) < OFF pooled (0.782), Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致优于 BN\n- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla\n- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分\n- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding\n- ✅ Cell 4 n=4 完成: [0.826, 0.802, 0.778, 0.784], mean=0.798±0.022\n- Cell 4 vs Vanilla: Cohen's d=2.31, p=0.040\n\n### v1 → v2 数据不一致 [v1-SUPERSEDED]\n\nv1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。\n**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。\n\n### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）\n\n### 机制证据状态（D056 v2 验证完成）\n\n**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：\n- v1 结果：Detach gradient norms = 1-13% of Vanilla — \"灾难性崩塌\"（逐层分析, 200 真实样本）\n- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）\n- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**\n- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做\n- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证\n\n**v2 Gradient Analysis (D056/D057) — 部分有效**：\n- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认\n- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足\n- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)\n- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**\n\n**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：\n- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除\n- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常\n- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移\n- BN forward-pass 并未导致表征退化 — \"BN interference\" 假设不成立\n\n**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：\n所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。\nv2 存活的机制信号：\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突\n- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)\n- ❌ \"capacity competition\" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据\n- ❌ \"BN forward-pass interference\" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好\n- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim\n\n### Core Insight（D074 修正）\n\nVLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：\n\n1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-2.9pp, F=3.26, p=0.098），Detach 消除损害\n2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.68, p=0.053, d≈1.05），独立于 gradient flow 条件\n3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）\n\n**行为层面**：两个主效应近似可加（ANOVA 交互项 ≈ 0），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。\n\n**机制层面（D057 修正）**：\n- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突\n- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）\n- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证\n- 空间内容仍然次要\n\n**论文策略选项**（Reviewer 建议）：\n- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h\n- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响\n- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary\n\n### 措辞约束（D057 更新）\n- **禁止** \"crossover interaction\" — v2 是 ordinal\n- **禁止** \"statistically significant interaction\" / \"significant interaction effect\" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)\n- **谨慎** \"interaction\" 单独使用 — 改用 \"normalization-dependent gradient flow effect\" 或 \"dual main effects\"\n- **禁止** \"BN-mediated gradient calibration\" / \"existence regularization\" — v1 不可复现\n- **禁止** 引用 v1/v2 梯度数值的跨方法论比较\n- **谨慎** \"gradient collapse\" / \"no gradient collapse\" — 待同方法论验证，暂不 claim\n- **可用** \"gradient orthogonality\"（v2 确认）— 排除直接梯度冲突\n- **可用** \"capacity competition\" / \"BN forward-pass interference\"（需标注为假设，待 CKA 验证）\n- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著\n- Cell 1 高方差本身可作为 finding：用 \"BN+gradient flow leads to unstable training\"\n- Gradient flow 主效应用 \"detrimental\" / \"harmful\"，不用 \"collapse\"（collapse 特指 detach 极端情况）\n\n**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。\n\n## Framing Strategy (D019 修正)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**核心叙事转变 (D026)**：从\"梯度流是必要条件\"→\"梯度流防止 encoder gradient collapse\"（具体机制，非抽象论断）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n\n**3-Contribution 结构（D043 Plan B 修正）**：\n- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：\n  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-2.9pp, F=3.26, p=0.098, η²=0.229 — 梯度流损害安全\n  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.68, p=0.053, η²=0.298 — LN 一致提供安全优势\n  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**\n  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)\n  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定\n  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla\n  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变\n  - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证\n- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）\n- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.798±0.022, n=4, d=2.31 vs Vanilla, p=0.040)\n- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla\n\n## Core Contribution Evidence\n\n### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)\nv1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。\nv2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。\n\n### v2 Factorial Evidence (D043, 权威数据)\n\n| Cell | Condition | n | CAR values | mean±std | 代码版本 |\n|------|-----------|---|-----------|----------|---------|\n| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |\n| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |\n| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |\n| 4 | Detach LN (Grad OFF + LN) | 4 | 0.826, 0.802, 0.778, 0.784 | 0.798±0.022 | **v2** ✅ |\n| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |\n\n✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=4 ✅; Vanilla n=3 ✅。共 N=15+3=18。\n✅ **ANOVA v2 final**: F(gradient)=3.26, p=0.098; F(norm)=4.68, p=0.053; F(interaction)=0.21, p=0.656。\n\n### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]\n\n**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**\n\n**CKA Evidence [v1-SUPERSEDED]**：\n- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）\n- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化\n- **\"BN = 100% 表征漂移原因\" 不再成立** — v2 中 BN 不导致 CKA 退化\n\n**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：\nv1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。\n\n**两种失败模式（D031, 仍有效）**：\n- Detach = 均匀退化 (per-task CAR std=0.002)\n- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)\n\n**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=4 ✅, Vanilla n=3 ✅。Depth 4-seed ✅。ANOVA v2 final verified。\n\n### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]\n- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，\"BN interference\" 假设不成立\n- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）\n- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证\n- ⚠️ v1 的 \"existence regularization\" / \"BN-mediated calibration\" 不再成立\n- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突\n\n### Claim 3: Spatial Content Secondary\nv1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。\nDepth = Vanilla exactly (4 seeds, D022)。空间内容次要。\n⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。\n\n### Claim 4 (Depth): ✅ Confirmed (D022)\nDepth CAR = 0.780 = Vanilla exactly (4 seeds)。\n\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\n### RC2 [HIGH]: \"Why Not Just Use CBF?\" — Defense: zero inference cost + complementarity\n### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\n\n## 待定关键实验\n\n### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)\n替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。\n- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)\n- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)\n- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠\n- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移\n\n### Cutoff Temporal Dynamics (D029/D030/D041)\n\n**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。\n\n**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**\ncutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。\n\n| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |\n|------|--------|--------|--------|------|-----------|\n| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |\n| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |\n| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |\n| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |\n| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |\n| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |\n\n**安全 claim（D041 限缩后）**：\n1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本\n2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）\n3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）\n4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim\n\n**不安全 claim**：任何特定 cutoff 点优于另一个、非单调\"sweet spot\"。\n\n**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。\n\n### Same-Seed 梯度重分析 — 条件式 (D028)\n当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：\n- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓\n- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异\n- **Scenario C**: 需两版分析（BN 和 LN）\nFig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 \"旧 round\"。\n\n## Framing Risk Ranking (D043 Plan B 更新)\n\n| 排名 | 风险 | 状态 | 应对 |\n|------|------|------|------|\n| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |\n| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=15, F/p/η² 已验证。Cell 4 vs Vanilla p=0.040 |\n| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 \"无害\" 但非 \"有益\" | ✅ 已定性 | 论文用 \"statistically indistinguishable\"，不 claim positive |\n| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |\n| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |\n| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |\n\n## 目标会议\n**CoRL 2026**: Abstract May 26, Paper May 29\n",
    "structuredPatch": [
      {
        "oldStart": 149,
        "oldLines": 7,
        "newStart": 149,
        "newLines": 7,
        "lines": [
          "   - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变",
          "   - ✅ 全部 15 seeds 完成, ANOVA v2 final 已验证",
          " - **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）",
          "-- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +4.2pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.798±0.022, n=4, d=2.31 vs Vanilla, p=0.040)",
          "+- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +3.6pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.798±0.022, n=4, d=2.31 vs Vanilla, p=0.040)",
          " - **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla",
          " ",
          " ## Core Contribution Evidence"
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

_source line 1227_

Now update the D074 transition note (F=0.10, p=0.763 → F=0.21, p=0.656):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5f30872-6952-4d1d-bd6a-41a4de679647",
  "uuid": "4e01c5b0-1137-4ea9-a5fc-2abe867153aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YAGCZr8cmDooAap4y9HQo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 278,
      "cache_read_input_tokens": 44911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 278
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
