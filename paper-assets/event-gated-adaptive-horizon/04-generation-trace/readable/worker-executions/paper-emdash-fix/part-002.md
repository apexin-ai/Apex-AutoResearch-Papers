# paper emdash fix — Part 2 of 2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../paper-emdash-fix.md) · [Structured JSON](../../../sessions/11/11f66dc23e6695a038f7.json)

## Before a recorded user message

### Tool result

_source line 97 · 2026-05-17T17:02:16.201Z_

<details><summary>↩ Tool result · `toolu_012HM3hzbYXWoqUYNgmNtWky`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "bcffd4df-d8fe-4a0e-802f-bc1d75e636c4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "Hierarchical approaches---THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}---may",
    "newString": "Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may",
    "originalFile": "% --- APPENDIX ---\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eight factorial experiments. Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.84 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.13 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.13\\times$, exp~008d) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.13]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.933$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=2$, $n_{\\text{neg}}=6$, $n=8$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). Thresholds 1.2$\\times$/1.5$\\times$ and 1.7$\\times$/2.0$\\times$ yield identical operating points (no NVE values in those intervals). $^\\dagger$Optimal threshold in $(3.78, 4.13]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 2 & 3 & 0 & 3 & 62.5\\% \\; [24.5, 91.5] & 40.0\\% & 100\\% & 57.1\\% \\\\\n$\\geq 1.2\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.5\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 2 & 0 & 0 & 6 & 100\\% \\; [63.1, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=5$, $n=8$, $\\text{AUROC}=0.933$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 2 & 0 & 3 & 75.0\\% \\; [34.9, 96.8] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.2\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 1.7\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 3.9\\times$ & 2 & 0 & 1 & 5 & 87.5\\% \\; [47.3, 99.7] & 100\\% & 66.7\\% & 80.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all three CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 66.7\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 85.7\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 2$ the statistical power is severely limited (accuracy 95\\% CI: [63.1\\%, 100\\%]).\n\n\\paragraph{Limitations.} With $n = 8$ experiments, all Clopper-Pearson confidence intervals are wide (e.g., 87.5\\% accuracy has 95\\% CI [47.3\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training, confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.55\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.60 \\rightarrow 0.59 \\rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K---low, but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and triggers full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.55\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$, confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d)---the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced: the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 50\\% prevention rate (1/2 seeds) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe two post-CIVO outcomes (Table~\\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\\nve > 1.5\\times$ threshold, yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control---confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) prevents CIVO in 1 of 2 seeds but the other collapses via Pathway~B (\\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse mechanisms identified in \\S\\ref{sec:f6}, CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing), have distinct diagnostic signatures but a shared root cause: the trained $\\dt$-embedding's learned features affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B).  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse.\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches---THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}---may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.\n",
    "structuredPatch": [
      {
        "oldStart": 288,
        "oldLines": 4,
        "newStart": 288,
        "newLines": 4,
        "lines": [
          " \\subsection{Implications for Temporal Abstraction in World Models}",
          " \\label{sec:implications}",
          " ",
          "-CIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches---THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}---may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.",
          "+CIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously."
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

_source line 98_

Now let me verify with grep that all explanatory em-dashes are gone.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "945b301a-5aa4-462e-a0bb-00bcbe5a20ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vDgZuGsEHHH7fPZXCfM2m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 308,
      "cache_read_input_tokens": 48467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 308
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

_source line 99_

<details open><summary>🔧 Tool call — Grep · `toolu_01B2X1qMopvKHMjX5r45b3ro`</summary>

```json
{
  "pattern": "---",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
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
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "43b78280-b99e-4861-b182-bb47ca959c12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vDgZuGsEHHH7fPZXCfM2m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 308,
      "cache_read_input_tokens": 48467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 308
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

_source line 100 · 2026-05-17T17:02:19.754Z_

<details><summary>↩ Tool result · `toolu_01B2X1qMopvKHMjX5r45b3ro`</summary>

```text
docs/paper/sections/methodology.tex:44:001 & Reference baseline & --- & --- & 15 & 1 \\
docs/paper/sections/methodology.tex:52:008f & Causal ablation & --- & on & 8 & 2 \\
docs/paper/sections/methodology.tex:66:--- = removed ($d{=}0$).\\
docs/paper/sections/abstract.tex:2:[Omitted long matching line]
docs/paper/sections/appendix.tex:1:% --- APPENDIX ---
docs/paper/sections/appendix.tex:94:% --- APPENDIX B: Factorial Ablation Details ---
docs/paper/sections/appendix.tex:119:[Omitted long matching line]
docs/paper/sections/appendix.tex:137:Frozen $e_{\dt}$ & exp\_015b: grad.\ starvation & --- \\
docs/paper/sections/appendix.tex:140:Removed $e_{\dt}$ & exp\_008f: no CIVO & --- \\
docs/paper/sections/appendix.tex:167:% --- APPENDIX C: Full Analysis & Discussion ---
docs/paper/sections/appendix.tex:181:[Omitted long matching line]
docs/paper/sections/appendix.tex:213:Reward head & --- & 49.0 & --- & 38.1 \\
docs/paper/sections/appendix.tex:214:KL dynamics & --- & 34.7 & --- & 40.4 \\
docs/paper/sections/appendix.tex:215:Observation decoders & --- & 16.3 & --- & 21.5 \\
docs/paper/sections/appendix.tex:271:[Omitted long matching line]
docs/paper/sections/results.tex:20:001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
docs/paper/sections/results.tex:23:007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
docs/paper/sections/results.tex:24:005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
docs/paper/sections/results.tex:32:008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
docs/paper/sections/results.tex:39:018 s2 & Full-SGS & trn$^\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\
docs/paper/sections/results.tex:55:--- = removed ($d{=}0$).\\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "4eb47eed-4788-447d-955b-5faa7449cf76",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/methodology.tex:44:001 & Reference baseline & --- & --- & 15 & 1 \\\\\ndocs/paper/sections/methodology.tex:52:008f & Causal ablation & --- & on & 8 & 2 \\\\\ndocs/paper/sections/methodology.tex:66:--- = removed ($d{=}0$).\\\\\ndocs/paper/sections/abstract.tex:2:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:1:% --- APPENDIX ---\ndocs/paper/sections/appendix.tex:94:% --- APPENDIX B: Factorial Ablation Details ---\ndocs/paper/sections/appendix.tex:119:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:137:Frozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\ndocs/paper/sections/appendix.tex:140:Removed $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\ndocs/paper/sections/appendix.tex:167:% --- APPENDIX C: Full Analysis & Discussion ---\ndocs/paper/sections/appendix.tex:181:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:213:Reward head & --- & 49.0 & --- & 38.1 \\\\\ndocs/paper/sections/appendix.tex:214:KL dynamics & --- & 34.7 & --- & 40.4 \\\\\ndocs/paper/sections/appendix.tex:215:Observation decoders & --- & 16.3 & --- & 21.5 \\\\\ndocs/paper/sections/appendix.tex:271:[Omitted long matching line]\ndocs/paper/sections/results.tex:20:001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\ndocs/paper/sections/results.tex:23:007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\ndocs/paper/sections/results.tex:24:005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\ndocs/paper/sections/results.tex:32:008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\ndocs/paper/sections/results.tex:39:018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\ndocs/paper/sections/results.tex:55:--- = removed ($d{=}0$).\\\\",
    "numLines": 21
  }
}
```

</details>

---


### Assistant

_source line 101_

<details><summary>Logged reasoning block</summary>

```text
Let me check the remaining omitted lines to make sure they're not explanatory dashes:

1. abstract.tex:2 - I already edited this. Let me read the full line to check if there are any remaining.
2. appendix.tex:119 - I edited this line. Let me check.
3. appendix.tex:181 - Let me check.
4. appendix.tex:271 - I edited this line. Let me check.

Let me read these lines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "9d3bdf61-9711-4c03-88b3-fb3a91ccc40b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015b6HVxBa16u78J3eAcDC4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 48775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 887
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

_source line 102_

Let me check the omitted lines to confirm they're clean.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "976f2e79-7bc1-4a70-85df-302be08686a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015b6HVxBa16u78J3eAcDC4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 48775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 887
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

_source line 103_

<details open><summary>🔧 Tool call — Read · `toolu_01DbTiQY9RwxkQrSHfosLDL7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex",
  "offset": 1,
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
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "be011980-7acc-4f6f-9825-7bf2f00612d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015b6HVxBa16u78J3eAcDC4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 48775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 887
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

_source line 104 · 2026-05-17T17:02:25.554Z_

<details><summary>↩ Tool result · `toolu_01DbTiQY9RwxkQrSHfosLDL7`</summary>

```text
1	\begin{abstract}
2	Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance, despite the success of identical $\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify the combination of trained temporal embedding and multi-rate data exposure as the causal factor and characterize the resulting failure mode: \emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\Delta t{=}1$ and $\Delta t{=}2$, which the critic internalizes as optimistic values. Gradient decomposition shows that 93\% of embedding gradients flow through observation decoders (0\% from the reward head), establishing CIVO as observation-reconstruction-gradient-driven. Full-pathway gradient stopping (removing 93\% of embedding gradients from observation decoders) completely eliminates CIVO, confirming the vulnerability is gradient-level. A normalized value-to-eval threshold of $1.5\times$ (35K+ training window) achieves 11/12 classification ($n{=}12$, Walker Walk), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The same CIVO trigger produces stochastic downstream outcomes across seeds (full collapse, transient CIVO with self-correction, and oscillatory degradation) from identical configurations. Critically, restricting imagination to $\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "0a852b2d-cf42-49d8-aa2b-a25d07c8f1a0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTemporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance, despite the success of identical $\\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify the combination of trained temporal embedding and multi-rate data exposure as the causal factor and characterize the resulting failure mode: \\emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\Delta t{=}1$ and $\\Delta t{=}2$, which the critic internalizes as optimistic values. Gradient decomposition shows that 93\\% of embedding gradients flow through observation decoders (0\\% from the reward head), establishing CIVO as observation-reconstruction-gradient-driven. Full-pathway gradient stopping (removing 93\\% of embedding gradients from observation decoders) completely eliminates CIVO, confirming the vulnerability is gradient-level. A normalized value-to-eval threshold of $1.5\\times$ (35K+ training window) achieves 11/12 classification ($n{=}12$, Walker Walk), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The same CIVO trigger produces stochastic downstream outcomes across seeds (full collapse, transient CIVO with self-correction, and oscillatory degradation) from identical configurations. Critically, restricting imagination to $\\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---


### Tool call

_source line 105_

<details open><summary>🔧 Tool call — Read · `toolu_01XzssJXRyCcmChpj5BvoaNB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 118,
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
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "4ada8d22-ce73-4128-83a1-8382739e25ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015b6HVxBa16u78J3eAcDC4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 48775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 887
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

_source line 106 · 2026-05-17T17:02:26.471Z_

<details><summary>↩ Tool result · `toolu_01XzssJXRyCcmChpj5BvoaNB`</summary>

```text
118	\paragraph{Evidence B: trainability is necessary (exp\_015b).}
119	Exp\_015b uses a frozen random-projection embedding ($d{=}32$, \texttt{requires\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\_008d, but with a non-trainable temporal signal. Despite full exposure to $\dt{>}1$ transitions, the NVE peaks at $1.45\times$ at 55K but does not sustain escalation: it retreats to $0.65\times$ by 65K and settles at $0.55\times$ by 105K (trajectory: $0.81 \rightarrow 1.26 \rightarrow 1.45 \rightarrow 0.65 \rightarrow 1.05 \rightarrow 0.60 \rightarrow 0.59 \rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K---low, but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \S\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "f5922e6d-5222-4a71-a376-79ba682ec96a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.55\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.60 \\rightarrow 0.59 \\rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K---low, but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.",
      "numLines": 2,
      "startLine": 118,
      "totalLines": 292
    }
  }
}
```

</details>

---


### Tool call

_source line 107_

<details open><summary>🔧 Tool call — Read · `toolu_01ApMrtTH5z3D1YM3QWG4ED8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 180,
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
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "b7c9d5b7-0c97-43c1-b617-6a96bf75adfc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015b6HVxBa16u78J3eAcDC4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 48775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 887
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

_source line 108 · 2026-05-17T17:02:27.006Z_

<details><summary>↩ Tool result · `toolu_01ApMrtTH5z3D1YM3QWG4ED8`</summary>

```text
180	
181	A random-policy control experiment ($N{=}100$ rollouts, 95\% bootstrap CI) decomposes CIVO into two necessary stages.  \textbf{Stage~1 (dynamics bias):} even under a random policy, $\dt{=}2$ imagination produces $1.68\times$ higher mean reward than $\dt{=}1$ in the trained-embedding model (008d)---the RSSM prior already generates reward-favorable trajectories at $\dt > 1$, independent of actor behavior.  \textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\times$ and the trained-actor ratio is $0.98\times$.  The decomposition attributes $\approx 36\%$ of the total effect to dynamics bias and $\approx 64\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "f9e0a942-3a91-4926-9564-ce4e93436f22",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d)---the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.",
      "numLines": 2,
      "startLine": 180,
      "totalLines": 292
    }
  }
}
```

</details>

---


### Tool call

_source line 109_

<details open><summary>🔧 Tool call — Read · `toolu_01HJsouy9PDeeYZufDfpWDka`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 270,
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
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "8ba0e3e4-39a6-4651-8a65-a99cf4693e28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015b6HVxBa16u78J3eAcDC4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 48775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 887
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

_source line 110 · 2026-05-17T17:02:27.760Z_

<details><summary>↩ Tool result · `toolu_01HJsouy9PDeeYZufDfpWDka`</summary>

```text
270	
271	The two post-CIVO outcomes (Table~\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\nve > 1.5\times$ threshold, yet the downstream damage is stochastic.\footnote{Exp\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control---confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "c07b179f-372a-4f78-8ae9-91b3d5a67e1e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\nThe two post-CIVO outcomes (Table~\\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\\nve > 1.5\\times$ threshold, yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control---confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).",
      "numLines": 2,
      "startLine": 270,
      "totalLines": 292
    }
  }
}
```

</details>

---


### Assistant

_source line 111_

<details><summary>Logged reasoning block</summary>

```text
I found 3 more explanatory em-dashes that I missed:

1. **abstract.tex line 2**: `architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as` → need to fix
2. **appendix.tex line 119**: `at 105K---low, but` → need to fix
3. **appendix.tex line 181**: `(008d)---the RSSM prior` → need to fix
4. **appendix.tex line 271**: `control---confirming` → need to fix
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "337b6807-d9e7-4fb8-a69f-d554a69d1232",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vVRnRmkohBzW8pqurYw9F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2162,
      "cache_read_input_tokens": 49662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2162
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

_source line 112_

Found 4 more I missed. Fixing them now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "328235db-afc3-4159-a158-c1051b14cd7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vVRnRmkohBzW8pqurYw9F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2162,
      "cache_read_input_tokens": 49662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2162
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

_source line 113_

<details open><summary>🔧 Tool call — Edit · `toolu_01RfdNgKb7odzDPqXECsYBPu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex",
  "old_string": "architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as",
  "new_string": "architecture (imagination-based actor-critic bootstrapping versus MPC re-planning) as"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "65ad8a3c-ea3c-43d1-acd0-68404e8dc840",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vVRnRmkohBzW8pqurYw9F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2162,
      "cache_read_input_tokens": 49662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2162
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

_source line 114 · 2026-05-17T17:02:33.669Z_

<details><summary>↩ Tool result · `toolu_01RfdNgKb7odzDPqXECsYBPu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "3b5cb5a8-33ca-46c2-bd1a-5e043dc5287f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex",
    "oldString": "architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as",
    "newString": "architecture (imagination-based actor-critic bootstrapping versus MPC re-planning) as",
    "originalFile": "\\begin{abstract}\nTemporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance, despite the success of identical $\\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify the combination of trained temporal embedding and multi-rate data exposure as the causal factor and characterize the resulting failure mode: \\emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\Delta t{=}1$ and $\\Delta t{=}2$, which the critic internalizes as optimistic values. Gradient decomposition shows that 93\\% of embedding gradients flow through observation decoders (0\\% from the reward head), establishing CIVO as observation-reconstruction-gradient-driven. Full-pathway gradient stopping (removing 93\\% of embedding gradients from observation decoders) completely eliminates CIVO, confirming the vulnerability is gradient-level. A normalized value-to-eval threshold of $1.5\\times$ (35K+ training window) achieves 11/12 classification ($n{=}12$, Walker Walk), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The same CIVO trigger produces stochastic downstream outcomes across seeds (full collapse, transient CIVO with self-correction, and oscillatory degradation) from identical configurations. Critically, restricting imagination to $\\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\begin{abstract}",
          "-Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance, despite the success of identical $\\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify the combination of trained temporal embedding and multi-rate data exposure as the causal factor and characterize the resulting failure mode: \\emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\Delta t{=}1$ and $\\Delta t{=}2$, which the critic internalizes as optimistic values. Gradient decomposition shows that 93\\% of embedding gradients flow through observation decoders (0\\% from the reward head), establishing CIVO as observation-reconstruction-gradient-driven. Full-pathway gradient stopping (removing 93\\% of embedding gradients from observation decoders) completely eliminates CIVO, confirming the vulnerability is gradient-level. A normalized value-to-eval threshold of $1.5\\times$ (35K+ training window) achieves 11/12 classification ($n{=}12$, Walker Walk), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The same CIVO trigger produces stochastic downstream outcomes across seeds (full collapse, transient CIVO with self-correction, and oscillatory degradation) from identical configurations. Critically, restricting imagination to $\\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.",
          "+Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance, despite the success of identical $\\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify the combination of trained temporal embedding and multi-rate data exposure as the causal factor and characterize the resulting failure mode: \\emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\Delta t{=}1$ and $\\Delta t{=}2$, which the critic internalizes as optimistic values. Gradient decomposition shows that 93\\% of embedding gradients flow through observation decoders (0\\% from the reward head), establishing CIVO as observation-reconstruction-gradient-driven. Full-pathway gradient stopping (removing 93\\% of embedding gradients from observation decoders) completely eliminates CIVO, confirming the vulnerability is gradient-level. A normalized value-to-eval threshold of $1.5\\times$ (35K+ training window) achieves 11/12 classification ($n{=}12$, Walker Walk), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The same CIVO trigger produces stochastic downstream outcomes across seeds (full collapse, transient CIVO with self-correction, and oscillatory degradation) from identical configurations. Critically, restricting imagination to $\\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture (imagination-based actor-critic bootstrapping versus MPC re-planning) as the structural factor that transforms manageable model imprecision into pathological value dynamics.",
          " \\end{abstract}"
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

_source line 115_

<details open><summary>🔧 Tool call — Edit · `toolu_01HQ5Rp8CMyEBgMmPsTWcUe6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "at 105K---low, but",
  "new_string": "at 105K, low but"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "607c6891-0575-4e1d-b074-1054b19ad241",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5J8x8QF3Mmdz8rG5LhW1h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 397,
      "cache_read_input_tokens": 51824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 397
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

_source line 116 · 2026-05-17T17:02:37.017Z_

<details><summary>↩ Tool result · `toolu_01HQ5Rp8CMyEBgMmPsTWcUe6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "49c0d77d-597b-4777-80e5-866b6708c856",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "at 105K---low, but",
    "newString": "at 105K, low but",
    "originalFile": "% --- APPENDIX ---\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eight factorial experiments. Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.84 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.13 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.13\\times$, exp~008d) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.13]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.933$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=2$, $n_{\\text{neg}}=6$, $n=8$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). Thresholds 1.2$\\times$/1.5$\\times$ and 1.7$\\times$/2.0$\\times$ yield identical operating points (no NVE values in those intervals). $^\\dagger$Optimal threshold in $(3.78, 4.13]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 2 & 3 & 0 & 3 & 62.5\\% \\; [24.5, 91.5] & 40.0\\% & 100\\% & 57.1\\% \\\\\n$\\geq 1.2\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.5\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 2 & 0 & 0 & 6 & 100\\% \\; [63.1, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=5$, $n=8$, $\\text{AUROC}=0.933$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 2 & 0 & 3 & 75.0\\% \\; [34.9, 96.8] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.2\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 1.7\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 3.9\\times$ & 2 & 0 & 1 & 5 & 87.5\\% \\; [47.3, 99.7] & 100\\% & 66.7\\% & 80.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all three CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 66.7\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 85.7\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 2$ the statistical power is severely limited (accuracy 95\\% CI: [63.1\\%, 100\\%]).\n\n\\paragraph{Limitations.} With $n = 8$ experiments, all Clopper-Pearson confidence intervals are wide (e.g., 87.5\\% accuracy has 95\\% CI [47.3\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training, confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.55\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.60 \\rightarrow 0.59 \\rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K---low, but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and triggers full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.55\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$, confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d)---the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced: the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 50\\% prevention rate (1/2 seeds) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe two post-CIVO outcomes (Table~\\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\\nve > 1.5\\times$ threshold, yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control---confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) prevents CIVO in 1 of 2 seeds but the other collapses via Pathway~B (\\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse mechanisms identified in \\S\\ref{sec:f6}, CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing), have distinct diagnostic signatures but a shared root cause: the trained $\\dt$-embedding's learned features affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B).  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse.\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.\n",
    "structuredPatch": [
      {
        "oldStart": 116,
        "oldLines": 7,
        "newStart": 116,
        "newLines": 7,
        "lines": [
          " This contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training, confirming that multi-rate data exposure, not embedding architecture, is the operative variable.",
          " ",
          " \\paragraph{Evidence B: trainability is necessary (exp\\_015b).}",
          "-Exp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.55\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.60 \\rightarrow 0.59 \\rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K---low, but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.",
          "+Exp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.55\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.60 \\rightarrow 0.59 \\rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.",
          " ",
          " The contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and triggers full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.55\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.",
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

_source line 117_

<details open><summary>🔧 Tool call — Edit · `toolu_01Nv9dtEoiLpK1mCHN17AGzB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "(008d)---the RSSM prior",
  "new_string": "(008d): the RSSM prior"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "d13c3f4d-85dd-4a9c-aa1d-5667687389e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ccCdvuRV4HgmtSzBMvVKs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 222,
      "cache_read_input_tokens": 52221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 222
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

_source line 118 · 2026-05-17T17:02:40.361Z_

<details><summary>↩ Tool result · `toolu_01Nv9dtEoiLpK1mCHN17AGzB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "b7a3ca9e-d6e6-463b-86bb-b37835f352c8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "(008d)---the RSSM prior",
    "newString": "(008d): the RSSM prior",
    "originalFile": "% --- APPENDIX ---\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eight factorial experiments. Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.84 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.13 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.13\\times$, exp~008d) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.13]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.933$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=2$, $n_{\\text{neg}}=6$, $n=8$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). Thresholds 1.2$\\times$/1.5$\\times$ and 1.7$\\times$/2.0$\\times$ yield identical operating points (no NVE values in those intervals). $^\\dagger$Optimal threshold in $(3.78, 4.13]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 2 & 3 & 0 & 3 & 62.5\\% \\; [24.5, 91.5] & 40.0\\% & 100\\% & 57.1\\% \\\\\n$\\geq 1.2\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.5\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 2 & 0 & 0 & 6 & 100\\% \\; [63.1, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=5$, $n=8$, $\\text{AUROC}=0.933$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 2 & 0 & 3 & 75.0\\% \\; [34.9, 96.8] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.2\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 1.7\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 3.9\\times$ & 2 & 0 & 1 & 5 & 87.5\\% \\; [47.3, 99.7] & 100\\% & 66.7\\% & 80.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all three CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 66.7\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 85.7\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 2$ the statistical power is severely limited (accuracy 95\\% CI: [63.1\\%, 100\\%]).\n\n\\paragraph{Limitations.} With $n = 8$ experiments, all Clopper-Pearson confidence intervals are wide (e.g., 87.5\\% accuracy has 95\\% CI [47.3\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training, confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.55\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.60 \\rightarrow 0.59 \\rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and triggers full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.55\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$, confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d)---the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced: the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 50\\% prevention rate (1/2 seeds) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe two post-CIVO outcomes (Table~\\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\\nve > 1.5\\times$ threshold, yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control---confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) prevents CIVO in 1 of 2 seeds but the other collapses via Pathway~B (\\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse mechanisms identified in \\S\\ref{sec:f6}, CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing), have distinct diagnostic signatures but a shared root cause: the trained $\\dt$-embedding's learned features affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B).  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse.\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.\n",
    "structuredPatch": [
      {
        "oldStart": 178,
        "oldLines": 7,
        "newStart": 178,
        "newLines": 7,
        "lines": [
          " ",
          " This asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.",
          " ",
          "-A random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d)---the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.",
          "+A random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.",
          " ",
          " This mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced: the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.",
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

_source line 119_

<details open><summary>🔧 Tool call — Edit · `toolu_01L6h7MRnWjKakXjKdiRB3Dw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "control---confirming",
  "new_string": "control, confirming"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "79b85dfe-9b88-48ee-9d0e-ce2d12acfe26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWANEkRrHk9DUotcfpMy6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 52443,
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

_source line 120 · 2026-05-17T17:02:43.364Z_

<details><summary>↩ Tool result · `toolu_01L6h7MRnWjKakXjKdiRB3Dw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "29fd2b7d-75dd-4f4d-8bc7-d3624139a4d2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "control---confirming",
    "newString": "control, confirming",
    "originalFile": "% --- APPENDIX ---\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eight factorial experiments. Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.84 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.13 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.13\\times$, exp~008d) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.13]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.933$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=2$, $n_{\\text{neg}}=6$, $n=8$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). Thresholds 1.2$\\times$/1.5$\\times$ and 1.7$\\times$/2.0$\\times$ yield identical operating points (no NVE values in those intervals). $^\\dagger$Optimal threshold in $(3.78, 4.13]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 2 & 3 & 0 & 3 & 62.5\\% \\; [24.5, 91.5] & 40.0\\% & 100\\% & 57.1\\% \\\\\n$\\geq 1.2\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.5\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 2 & 0 & 0 & 6 & 100\\% \\; [63.1, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=5$, $n=8$, $\\text{AUROC}=0.933$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 2 & 0 & 3 & 75.0\\% \\; [34.9, 96.8] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.2\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 1.7\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 3.9\\times$ & 2 & 0 & 1 & 5 & 87.5\\% \\; [47.3, 99.7] & 100\\% & 66.7\\% & 80.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all three CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 66.7\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 85.7\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 2$ the statistical power is severely limited (accuracy 95\\% CI: [63.1\\%, 100\\%]).\n\n\\paragraph{Limitations.} With $n = 8$ experiments, all Clopper-Pearson confidence intervals are wide (e.g., 87.5\\% accuracy has 95\\% CI [47.3\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training, confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.55\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.60 \\rightarrow 0.59 \\rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and triggers full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.55\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$, confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced: the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 50\\% prevention rate (1/2 seeds) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe two post-CIVO outcomes (Table~\\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\\nve > 1.5\\times$ threshold, yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control---confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) prevents CIVO in 1 of 2 seeds but the other collapses via Pathway~B (\\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse mechanisms identified in \\S\\ref{sec:f6}, CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing), have distinct diagnostic signatures but a shared root cause: the trained $\\dt$-embedding's learned features affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B).  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse.\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.\n",
    "structuredPatch": [
      {
        "oldStart": 268,
        "oldLines": 7,
        "newStart": 268,
        "newLines": 7,
        "lines": [
          " \\end{tabular}",
          " \\end{table}",
          " ",
          "-The two post-CIVO outcomes (Table~\\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\\nve > 1.5\\times$ threshold, yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control---confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).",
          "+The two post-CIVO outcomes (Table~\\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\\nve > 1.5\\times$ threshold, yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control, confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).",
          " ",
          " \\subsection{Why MPC Is Immune}",
          " \\label{sec:mpc_immune}"
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

_source line 121_

Final verification:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "32f1c37e-1ace-48fb-bd60-a02a944be445",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2hc4yWTwD4qjbfoc7gYLE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 215,
      "cache_read_input_tokens": 52671,
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

_source line 122_

<details open><summary>🔧 Tool call — Grep · `toolu_01PexgmTqNBqdpErGyuCdkhV`</summary>

```json
{
  "pattern": "---",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
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
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "7a570024-6739-4445-b520-b15ae39e36a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2hc4yWTwD4qjbfoc7gYLE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 215,
      "cache_read_input_tokens": 52671,
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

_source line 123 · 2026-05-17T17:02:48.674Z_

<details><summary>↩ Tool result · `toolu_01PexgmTqNBqdpErGyuCdkhV`</summary>

```text
docs/paper/sections/methodology.tex:44:001 & Reference baseline & --- & --- & 15 & 1 \\
docs/paper/sections/methodology.tex:52:008f & Causal ablation & --- & on & 8 & 2 \\
docs/paper/sections/methodology.tex:66:--- = removed ($d{=}0$).\\
docs/paper/sections/appendix.tex:1:% --- APPENDIX ---
docs/paper/sections/appendix.tex:94:% --- APPENDIX B: Factorial Ablation Details ---
docs/paper/sections/appendix.tex:137:Frozen $e_{\dt}$ & exp\_015b: grad.\ starvation & --- \\
docs/paper/sections/appendix.tex:140:Removed $e_{\dt}$ & exp\_008f: no CIVO & --- \\
docs/paper/sections/appendix.tex:167:% --- APPENDIX C: Full Analysis & Discussion ---
docs/paper/sections/appendix.tex:213:Reward head & --- & 49.0 & --- & 38.1 \\
docs/paper/sections/appendix.tex:214:KL dynamics & --- & 34.7 & --- & 40.4 \\
docs/paper/sections/appendix.tex:215:Observation decoders & --- & 16.3 & --- & 21.5 \\
docs/paper/sections/results.tex:20:001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
docs/paper/sections/results.tex:23:007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
docs/paper/sections/results.tex:24:005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
docs/paper/sections/results.tex:32:008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
docs/paper/sections/results.tex:39:018 s2 & Full-SGS & trn$^\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\
docs/paper/sections/results.tex:55:--- = removed ($d{=}0$).\\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "cf1e51da-7f52-4f25-8dd0-b88e813690ca",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/methodology.tex:44:001 & Reference baseline & --- & --- & 15 & 1 \\\\\ndocs/paper/sections/methodology.tex:52:008f & Causal ablation & --- & on & 8 & 2 \\\\\ndocs/paper/sections/methodology.tex:66:--- = removed ($d{=}0$).\\\\\ndocs/paper/sections/appendix.tex:1:% --- APPENDIX ---\ndocs/paper/sections/appendix.tex:94:% --- APPENDIX B: Factorial Ablation Details ---\ndocs/paper/sections/appendix.tex:137:Frozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\ndocs/paper/sections/appendix.tex:140:Removed $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\ndocs/paper/sections/appendix.tex:167:% --- APPENDIX C: Full Analysis & Discussion ---\ndocs/paper/sections/appendix.tex:213:Reward head & --- & 49.0 & --- & 38.1 \\\\\ndocs/paper/sections/appendix.tex:214:KL dynamics & --- & 34.7 & --- & 40.4 \\\\\ndocs/paper/sections/appendix.tex:215:Observation decoders & --- & 16.3 & --- & 21.5 \\\\\ndocs/paper/sections/results.tex:20:001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\ndocs/paper/sections/results.tex:23:007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\ndocs/paper/sections/results.tex:24:005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\ndocs/paper/sections/results.tex:32:008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\ndocs/paper/sections/results.tex:39:018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\ndocs/paper/sections/results.tex:55:--- = removed ($d{=}0$).\\\\",
    "numLines": 17
  }
}
```

</details>

---


### Tool call

_source line 124_

<details open><summary>🔧 Tool call — Grep · `toolu_013BTg77cmuJh18Bi8YPykGz`</summary>

```json
{
  "pattern": " -- ",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
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
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "c1db16fc-f68c-4434-b13c-a3cffb1cbd60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2hc4yWTwD4qjbfoc7gYLE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 215,
      "cache_read_input_tokens": 52671,
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

_source line 125 · 2026-05-17T17:02:49.309Z_

<details><summary>↩ Tool result · `toolu_013BTg77cmuJh18Bi8YPykGz`</summary>

```text
docs/paper/sections/results.tex:218:008f s3 & no $\dt$-emb & TN & -- & -- & 594 & -- \\
docs/paper/sections/results.tex:219:009b s2 & trained $\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\
docs/paper/sections/results.tex:220:baseline s1 & vanilla & TN & -- & -- & 970 & -- \\
docs/paper/sections/results.tex:221:009d s0 & vanilla & TN & -- & -- & 951 & -- \\
docs/paper/sections/results.tex:222:009d s1 & vanilla & TN & -- & -- & 920 & -- \\
docs/paper/sections/results.tex:223:019b & trained $\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "1b792ca2-0a7d-476a-b55f-8a16ad441902",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/results.tex:218:008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\ndocs/paper/sections/results.tex:219:009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\ndocs/paper/sections/results.tex:220:baseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\ndocs/paper/sections/results.tex:221:009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\ndocs/paper/sections/results.tex:222:009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\ndocs/paper/sections/results.tex:223:019b & trained $\\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\\\",
    "numLines": 6
  }
}
```

</details>

---


### Assistant

_source line 126_

全部解释性 em-dash 已清除。剩余 `---` 均为以下合法用途（保留）：

**`---` 残留（全部为表格占位符或注释）：**
| 文件 | 行 | 用途 |
|---|---|---|
| methodology.tex | 44, 52 | 表格单元格（"removed"） |
| methodology.tex | 66 | 表格脚注定义 |
| appendix.tex | 1, 94, 167 | LaTeX 注释分隔符 |
| appendix.tex | 137, 140 | 表格单元格 |
| appendix.tex | 213–215 | 表格单元格 |
| results.tex | 20, 23, 24, 32, 39 | 表格单元格 |
| results.tex | 55 | 表格脚注定义 |

**`--` 残留（全部为表格占位符）：**
| 文件 | 行 | 用途 |
|---|---|---|
| results.tex | 218–223 | 表格单元格 |

**共修改 27 处解释性 em-dash**，分布于 6 个文件：
- abstract.tex: 3 处
- analysis.tex: 1 处
- related_work.tex: 2 处
- conclusion.tex: 3 处
- methodology.tex: 3 处
- appendix.tex: 15 处

替换策略：逗号（简单衔接）、括号（插入性列举）、冒号（引出解释）、句号（拆句）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "uuid": "ad17b4ea-166c-4352-949c-53577881f7be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8oZfqQcnK9b2acZ2hWWXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1203,
      "cache_read_input_tokens": 52886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1203
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

_source line 127_

全部解释性 em-dash 已清除。剩余 `---` 均为以下合法用途（保留）：

**`---` 残留（全部为表格占位符或注释）：**
| 文件 | 行 | 用途 |
|---|---|---|
| methodology.tex | 44, 52 | 表格单元格（"removed"） |
| methodology.tex | 66 | 表格脚注定义 |
| appendix.tex | 1, 94, 167 | LaTeX 注释分隔符 |
| appendix.tex | 137, 140 | 表格单元格 |
| appendix.tex | 213–215 | 表格单元格 |
| results.tex | 20, 23, 24, 32, 39 | 表格单元格 |
| results.tex | 55 | 表格脚注定义 |

**`--` 残留（全部为表格占位符）：**
| 文件 | 行 | 用途 |
|---|---|---|
| results.tex | 218–223 | 表格单元格 |

**共修改 27 处解释性 em-dash**，分布于 6 个文件：
- abstract.tex: 3 处
- analysis.tex: 1 处
- related_work.tex: 2 处
- conclusion.tex: 3 处
- methodology.tex: 3 处
- appendix.tex: 15 处

替换策略：逗号（简单衔接）、括号（插入性列举）、冒号（引出解释）、句号（拆句）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 254024,
  "duration_api_ms": 254751,
  "num_turns": 55,
  "stop_reason": "end_turn",
  "session_id": "250cd295-e71a-4a7b-b8cc-c5394debf85d",
  "total_cost_usd": 1.4765,
  "usage": {
    "input_tokens": 41,
    "cache_creation_input_tokens": 42642,
    "cache_read_input_tokens": 1717155,
    "output_tokens": 14005,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 42642,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 445,
        "cache_read_input_tokens": 52886,
        "cache_creation_input_tokens": 1203,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1203
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 990,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00108,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 41,
      "outputTokens": 14005,
      "cacheReadInputTokens": 1717155,
      "cacheCreationInputTokens": 42642,
      "webSearchRequests": 0,
      "costUSD": 1.47542,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "acc161f3-7f14-4e67-ba16-21b1cb14c497"
}
```

</details>

---
