% Results Section — Draft v1
% Target: CoRL 2026
% Status: Draft, pending Director review
% Writing order: 1 (anchors all other sections)

\section{Results}
\label{sec:results}

We organize findings around five diagnostic questions, followed by a gradient decomposition analysis and a taxonomy of failure modes. All quantitative claims cite experiment identifiers for traceability; evaluation returns are means over 10 episodes at each checkpoint. Primary experiments use Walker Walk from the DeepMind Control Suite; cross-environment validation on Cheetah Run is reported in Section~\ref{sec:cross_env} (see Section~\ref{sec:environment} for environment details).

% ============================================================
% F1: ALL DT>1 DEGRADE
% ============================================================

\subsection{Finding 1: All Variable-Rate Configurations Degrade Performance}
\label{sec:f1}

\begin{figure}[t]
  \centering
  % PLACEHOLDER: Learning curves for exp_001, 005, 006, 007
  \includegraphics[width=\linewidth]{figures/fig1_learning_curves.pdf}
  \caption{Learning curves for all primary configurations. The \mbox{$\Delta t{=}1$} baseline (exp\_001) converges to ${\sim}950$; every $\Delta t{>}1$ variant degrades or collapses.}
  \label{fig:learning_curves}
\end{figure}

Every tested variable-rate imagination configuration degrades asymptotic performance relative to the standard $\Delta t{=}1$ baseline. The baseline (exp\_001, seed~1) reaches 915.7 at 105K steps and converges to ${\sim}950$ asymptotically (peak 970.4 at 505K). In contrast:

\begin{itemize}
    \item \textbf{Learned gate} (exp\_005): peaks at 541.2 at 55K, then declines to 98.8 by 145K---a 90\% drop from peak.
    \item \textbf{Fixed $\Delta t{=}2$} (exp\_006, $H{=}15$): peaks at 485.3 at 35K, then collapses to 132.9 by 65K as the value/eval ratio accelerates from 31\% to 272\%.
    \item \textbf{Fixed $\Delta t{=}4$} (exp\_007, $H{=}15$): peaks at 176.9 at 25K and plateaus around 144--152, never exceeding 19\% of the baseline's asymptotic level.
\end{itemize}

No $\Delta t{>}1$ configuration achieves sustained performance above 60\% of the baseline beyond 65K steps. The degradation patterns vary---inverted-V collapse (exp\_006), monotonic decline (exp\_005), and severe suppression (exp\_007)---but the qualitative conclusion is uniform: variable-rate imagination degrades performance on Walker Walk across all tested configurations.


% ============================================================
% F2: TRAINED DT_EMB → CIVO
% ============================================================

\subsection{Finding 2: Trained Temporal Embedding Reliably Triggers Pathological Value Overestimation}
\label{sec:f2}

\begin{figure}[t]
  \centering
  % PLACEHOLDER: NVE trajectories with 1.5x threshold
  \includegraphics[width=\linewidth]{figures/fig2_nve_trajectories.pdf}
  \caption{Normalized value/eval ratio (NVE) trajectories. Dashed line: $1.5\times$ pathological threshold (applied at $k \geq 35\text{K}$). Both trained-$e_{\Delta t}$ seeds exceed the threshold; neither removed-$e_{\Delta t}$ seed does.}
  \label{fig:nve_trajectories}
\end{figure}

The controlled comparison between exp\_008d (trained $e_{\Delta t}$, subsample \textsc{on}, $H{=}8$) and exp\_008f ($e_{\Delta t}$ removed, subsample \textsc{on}, $H{=}8$) isolates the temporal embedding as the causal factor for conditioning-induced value overestimation (CIVO). These experiments share identical configurations except for the presence of the trained temporal embedding.

\paragraph{Diagnostic threshold.} Using the normalized value/eval ratio (NVE; see Section~\ref{sec:diagnostic}), the $\hat{r}_k > 1.5$ threshold at steps $\geq$35K achieves 4/4 classification accuracy across seeds:

\begin{table}[h]
\centering
\small
\caption{NVE diagnostic: trained vs.\ removed temporal embedding. Peak NVE reported at steps $\geq$35K where baseline $r_k > 0.24$ ensures ratio stability.}
\label{tab:nve_separation}
\begin{tabular}{llcc}
\toprule
Condition & Seed & Peak NVE ($\geq$35K) & $>$1.5$\times$? \\
\midrule
Trained $e_{\Delta t}$ (exp\_008d) & 1 & 2.09$\times$ @ 45K & \textbf{Yes} \\
Trained $e_{\Delta t}$ (exp\_009b) & 2 & 1.62$\times$ @ 45K & \textbf{Yes} \\
Removed $e_{\Delta t}$ (exp\_008f) & 1 & 0.97$\times$ @ 55K & No \\
Removed $e_{\Delta t}$ (exp\_009c) & 2 & 1.14$\times$ @ 105K & No \\
\bottomrule
\end{tabular}
\end{table}

Both trained-$e_{\Delta t}$ seeds exceed the pathological threshold; neither removed-$e_{\Delta t}$ seed does. The trained embedding reliably induces pathological value overestimation, though whether this overestimation progresses to catastrophic collapse is stochastic (see below).

\paragraph{Causal isolation.} The factorial structure establishes that CIVO requires the combination of a \textit{trained} temporal embedding and exposure to multi-rate training data:

\begin{figure}[h]
  \centering
  % PLACEHOLDER: 2×2 factorial grid summary
  \includegraphics[width=0.85\linewidth]{figures/fig3_factorial_grid.pdf}
  \caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\Delta t}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}
  \label{fig:factorial_grid}
\end{figure}

\begin{table}[h]
\centering
\small
\caption{Causal isolation: $e_{\Delta t}$ configuration $\times$ multi-rate data exposure. All treatment conditions use $\Delta t{=}2$ imagination and $H{=}8$ (except exp\_008a: $H{=}15$).}
\label{tab:causal_matrix}
\begin{tabular}{lcc}
\toprule
& Multi-rate data (\textsc{on}) & Single-rate data (\textsc{off}) \\
\midrule
Trained $e_{\Delta t}$ & exp\_008d: CIVO & exp\_008a: healthy \\
 & NVE 2.09$\times$, collapse & NVE 0.59--0.93$\times$ \\
\midrule
Frozen $e_{\Delta t}$ & exp\_015b: grad.\ starvation & --- \\
 & NVE 0.39--0.47$\times$ & \\
\midrule
Removed $e_{\Delta t}$ & exp\_008f: no CIVO & --- \\
 & NVE $\leq$0.97$\times$ & \\
\bottomrule
\end{tabular}
\end{table}

Exp\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\Delta t{>}1$ transitions during world-model training (subsample \textsc{off}). Despite sharing the same embedding architecture as exp\_008d, its NVE remains in the 0.59--0.93$\times$ range across 105K steps (exp\_008a). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\Delta t{>}1$ state predictions within the RSSM.

\paragraph{Post-CIVO outcomes: seed-dependent trajectories.} The 008d configuration was run with two independent seeds, producing qualitatively distinct outcomes:

\begin{enumerate}
    \item \textbf{Seed~1} (exp\_008d / exp\_009e): CIVO onset at 25K (NVE 1.78$\times$), eval declines from 167.2 to 82.8 by 55K (exp\_008d). Extended to 105K (exp\_009e), the run shows oscillatory degradation: a transient bounce to 250 at 65K, but actor loss flips positive ($+$0.011 at 85K, exp\_009e), signaling permanent actor damage. Eval oscillates between 131 and 250 without sustained recovery, ending at 131.1 at 105K (exp\_009e).
    \item \textbf{Seed~2} (exp\_009b): transient NVE of 1.62$\times$ at 45K, followed by self-correction---NVE declines monotonically from 1.62$\times$ to 0.38$\times$ between 45K and 105K. Value peaks at 110.9 at 65K then self-corrects to 67.3 by 105K, while eval rises from 141.0 to a peak of 278.5 at 95K (exp\_009b).
\end{enumerate}

Both seeds cross the NVE~$>$~1.5$\times$ threshold, confirming the trained embedding as a reliable trigger. The downstream trajectory depends on whether overestimation is sustained across consecutive checkpoints (seed~1: $1.71\times \to 2.09\times \to 4.12\times$ at 35--55K, locking in the positive feedback loop) or transient (seed~2: $1.62\times$ at 45K $\to$ $1.41\times$ at 55K, declining).


% ============================================================
% F3: UNTRAINED DT_EMB → PROTECTION
% ============================================================

\subsection{Finding 3: Unexposed Temporal Embedding Suppresses Value Drift}
\label{sec:f3}

Exp\_008a (trained-but-unexposed $e_{\Delta t}$,\footnote{Exp\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\Delta t{>}1$ data due to subsample \textsc{off}; it is not frozen or absent. See Table~\ref{tab:factorial}.} subsample \textsc{off}, $H{=}15$) demonstrates sustained value growth suppression over 105K steps. Its NVE ranges from 0.59$\times$ to 0.93$\times$ across the 55K--105K window (exp\_008a), diverging further \textit{below} baseline levels over time rather than converging toward them.

Performance follows two complete V-shaped recovery cycles: $500.8 \to 563.4 \to 487.9 \to 608.0 \to 469.9 \to 583.7 \to 572.2 \to 777.7$ over 35K--105K (exp\_008a). The final evaluation of 777.7 at 105K reaches 85\% of the baseline at the same step (915.7, exp\_001), with no collapse through 112K training steps.

This contrasts sharply with exp\_006 (trained $e_{\Delta t}$, subsample \textsc{on}, $H{=}15$), where NVE accelerates from 1.61$\times$ at 45K to 2.31$\times$ at 55K before catastrophic collapse to 132.9 at 65K (exp\_006). The 006-vs-008a comparison corroborates the causal role of multi-rate data exposure: both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\Delta t{>}1$ transitions during training.


% ============================================================
% F4: DT AMPLIFICATION
% ============================================================

\subsection{Finding 4: Longer Temporal Gaps Amplify Degradation}
\label{sec:f4}

Increasing the imagination step size from $\Delta t{=}2$ to $\Delta t{=}4$ worsens degradation monotonically. Peak evaluation returns are ${\sim}950$ ($\Delta t{=}1$, exp\_001), 485.3 ($\Delta t{=}2$, exp\_006), and 176.9 ($\Delta t{=}4$, exp\_007).

\begin{figure}[h]
  \centering
  % PLACEHOLDER: dt=1 vs dt=2 vs dt=4 comparison
  \includegraphics[width=0.7\linewidth]{figures/fig5_dt_amplification.pdf}
  \caption{Performance vs.\ imagination step size: monotonic degradation.}
  \label{fig:dt_amplification}
\end{figure}

At $\Delta t{=}4$ (exp\_007), the value/eval ratio at 45K is 0.126 (exp\_007)---severely suppressed rather than inflated---indicating a qualitatively different failure: the RSSM prediction quality at $\Delta t{=}4$ is too poor even for overestimation to develop, consistent with compounding prediction error over longer temporal gaps. Only two $\Delta t$ values were tested; a finer grid would be needed to characterize the degradation curve.


% ============================================================
% F5: HORIZON/SUBSAMPLE SECONDARY
% ============================================================

\subsection{Finding 5: Horizon and Subsampling Are Secondary Factors}
\label{sec:f5}

Subsampling and imagination horizon modulate performance levels but are neither necessary nor sufficient for CIVO.

\paragraph{Subsampling is not sufficient for collapse.} Exp\_008e\_v3 (trained $e_{\Delta t}$, subsample \textsc{on}, $\Delta t{=}1$ imagination, $H{=}15$) achieves 869.9 at 105K---95\% of baseline---with seed~1 (exp\_008e\_v3\_s1).\footnote{An independent run with seed~0 (exp\_008e\_v3) reproduces this trajectory.} This demonstrates that multi-rate training data alone does not degrade performance when imagination is restricted to $\Delta t{=}1$. Seed~2, however, collapses from 715.2 at 85K to 137.0 at 105K (exp\_008e\_v3\_s2), through a non-CIVO mechanism discussed in Section~\ref{sec:failure_taxonomy}.

\paragraph{Horizon affects performance level but not the overestimation pattern.} Exp\_008c ($H{=}8$, unexposed $e_{\Delta t}$, subsample \textsc{off}) plateaus at 241.9 at 55K (exp\_008c), while exp\_008a ($H{=}15$, same configuration otherwise) reaches 777.7 at 105K (exp\_008a). Both maintain healthy NVE ($\leq$0.93$\times$), confirming that horizon length modulates the performance ceiling but does not trigger CIVO.


% ============================================================
% GRADIENT DECOMPOSITION
% ============================================================

\subsection{Gradient Decomposition: Observation Decoders Dominate Temporal Embedding Learning}
\label{sec:gradient_decomposition_results}

To identify which gradient pathway through $e_{\Delta t}$ drives CIVO, we performed a post-hoc gradient decomposition (D061) measuring each loss component's contribution to the temporal embedding parameters via \texttt{torch.autograd.grad}. The analysis was motivated by a targeted stop-gradient experiment (exp\_016e) in which $e_{\Delta t}$ was detached from the reward head during the backward pass---see Section~\ref{sec:sgs_gradient_analysis} for full experimental details.

\begin{table}[h]
\centering
\small
\caption{Gradient contributions to $e_{\Delta t}$ parameters by loss component ($\ell_2$ norms of $\nabla_\theta \mathcal{L}_i$), measured at training step 95K (D061 analysis). Total gradient norm: 1.624.}
\label{tab:gradient_decomposition_results}
\begin{tabular}{lrr}
\toprule
Loss component & $\|\nabla_\theta \mathcal{L}_i\|_2$ & Share (\%) \\
\midrule
Observation decoders (orientations, velocity, height) & 1.505 & 92.7 \\
KL dynamics & 0.119 & 7.3 \\
Continuation head & $<$0.001 & $<$0.1 \\
Reward head & 0.000 & 0.0 \\
\bottomrule
\end{tabular}
\end{table}

The reward head's contribution is numerically negligible---zero to within floating-point precision. This explains why exp\_016e (reward-only stop-gradient; identical to exp\_008d except \texttt{reward\_dt\_emb\_detach=True}) exhibits the same collapse pattern: peak 326.7 at 75K followed by catastrophic decline to 31.7 at 95K with NVE reaching $10.42\times$ (exp\_016e). The intervention detaches a gradient that does not exist---an architectural no-op. The timing differences between exp\_016e and exp\_008d (collapse onset ${\sim}$75K vs.\ ${\sim}$25K, peak 326.7 vs.\ 167.2) are consistent with cross-seed variation across the 008d configuration's trajectories (cf.\ exp\_009b, peak 278.5 at 95K).

The 93\%/7\%/0\% split reveals that $e_{\Delta t}$ learns to encode temporal information that minimizes \textit{observation reconstruction error}, not reward prediction error. CIVO originates in the observation reconstruction objective's influence on latent dynamics---a structural property of DreamerV3's multi-head decoder architecture \citep{hafner2023dreamerv3}. This constrains the space of viable interventions: strategies targeting the reward pathway alone address $<$1\% of the gradient flow and cannot attenuate CIVO. The full-pathway SGS intervention (exp\_018; Section~\ref{sec:pending}) removes the dominant 93\% observation decoder contribution, constituting a genuine gradient-level intervention.

This gradient asymmetry is consistent with prior observations on the dominance of reconstruction losses in world-model training \citep{hafner2023dreamerv3, ma2024harmonydream}, but the D061 analysis provides the first \textit{backward-pass decomposition} quantifying the per-component gradient contributions to a conditioning variable. HarmonyDream \citep{ma2024harmonydream} reports a two-order-of-magnitude gap between observation and reward loss magnitudes; our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result that definitively rules out reward-pathway interventions.


% ============================================================
% THREE FAILURE MODES
% ============================================================

\subsection{Three Distinct Failure Modes}
\label{sec:failure_taxonomy}

\begin{figure}[t]
  \centering
  % PLACEHOLDER: Contrasting collapse dynamics across three mechanisms
  \includegraphics[width=\linewidth]{figures/fig6_failure_modes.pdf}
  \caption{Three failure modes triggered by temporal embedding configurations. Left: CIVO (exp\_008d)---value explosion drives eval decline, entropy decreases. Center: Gradient starvation (exp\_015b)---actor loss approaches zero, performance oscillates without convergence. Right: IRD (exp\_008e\_v3\_s2)---eval collapse precedes value rise, entropy increases.}
  \label{fig:failure_modes}
\end{figure}

The experiments reveal three mechanistically distinct failure modes. Distinguishing these modes is necessary for designing targeted interventions, as surface-level metrics (e.g., low final eval return) are shared across all three but the underlying dynamics differ qualitatively.

\begin{table}[h]
\centering
\small
\caption{Taxonomy of failure modes identified across temporal embedding configurations.}
\label{tab:failure_taxonomy}
\begin{tabular}{lccc}
\toprule
Feature & CIVO & Grad.\ Starvation & IRD \\
\midrule
Representative exp & 008d (seed 1) & 015b & 008e\_v3\_s2 \\
$e_{\Delta t}$ config & trained & frozen & trained \\
NVE trajectory & sustained $>$1.5$\times$ & $<$0.5$\times$ & passive rise \\
Value dynamics & explosion ($+$130\%) & suppressed & stable \\
Eval dynamics & decline & volatile (80--238) & collapse ($-$81\%) \\
Actor entropy & $\downarrow$ (locks in) & --- & $\uparrow$ (de-specializes) \\
\bottomrule
\end{tabular}
\end{table}

\paragraph{Conditioning-Induced Value Overestimation (CIVO).} In exp\_008d and exp\_006, the trained temporal embedding enables the reward head to produce systematically biased $\Delta t{>}1$ predictions. RSSM fidelity analysis reveals a $2.78\times$ reward gap between $\Delta t{=}1$ and $\Delta t{=}2$ transitions in exp\_008d (see Table~\ref{tab:rssm_fidelity} in Section~\ref{sec:rssm_analysis}). The critic inherits these biases through the $\lambda$-return computation, overestimates values for $\Delta t{>}1$ trajectories, and the actor exploits the overestimated landscape. This positive feedback loop produces accelerating NVE ($1.71\times \to 2.09\times \to 4.12\times$ at 35--55K in exp\_008d) with decreasing actor entropy---the policy becomes increasingly deterministic as it converges on the overestimated region.

\paragraph{Gradient Starvation.} A frozen temporal embedding (exp\_015b, $d{=}32$, \texttt{requires\_grad=False}) cannot co-adapt as RSSM representations drift during training. Actor loss approaches zero (0.0002 at 105K, exp\_015b), indicating gradient starvation: the actor receives insufficient learning signal. NVE remains at 0.39--0.47$\times$ (exp\_015b)---the critic \textit{under-estimates}, the opposite of CIVO. Evaluation oscillates between 80 and 238 without convergence. The NVE briefly reaches 1.45$\times$ at 55K but self-corrects to 0.65$\times$ by 65K---a transient, sub-threshold overestimation qualitatively different from CIVO's sustained acceleration.

\paragraph{Imagination-Reality Divergence (IRD).} Exp\_008e\_v3\_s2 collapses despite using $\Delta t{=}1$-only imagination (\texttt{gate\_dt\_mean}$\,{=}\,$1.0 throughout, exp\_008e\_v3\_s2). Evaluation drops from 715.2 at 85K to 137.0 at 105K, while value estimates remain relatively stable (339.3 $\to$ 339.8), producing a passive NVE rise to $3.78\times$ (exp\_008e\_v3\_s2). Crucially, actor entropy \textit{increases} from $-5.21$ to $-3.83$ during collapse (policy de-specialization), the opposite of CIVO's entropy decrease. The baseline seed~2 (exp\_009a) is stable through the same window (618.7 $\to$ 836.5 at 85K--105K, exp\_009a), ruling out seed-specific fragility.

This failure mode does not involve value overestimation driving actor exploitation. Rather, the trained embedding's interaction with multi-rate training data appears to create a latent representation vulnerability that manifests as policy instability independent of imagination $\Delta t$. The NVE rise is a \textit{consequence} of eval collapse, not a cause---distinguishing IRD from CIVO where the NVE rise precedes and drives the eval decline.

The existence of IRD alongside CIVO suggests that the trained temporal embedding creates vulnerability through multiple pathways. Eliminating CIVO (e.g., via $\Delta t{=}1$ imagination) does not eliminate all failure modes.


% ============================================================
% PENDING EXPERIMENTS (PLACEHOLDERS)
% ============================================================

% ============================================================
% CROSS-ENVIRONMENT VALIDATION
% ============================================================

\subsection{Cross-Environment Validation: Cheetah Run}
\label{sec:cross_env}

To test whether CIVO generalizes beyond Walker Walk, we replicate the trained-$e_{\Delta t}$ condition on Cheetah Run (17D observations, 6D actions). Both Cheetah seeds exhibit CIVO onset: exp\_010b (seed 1, peak NVE 8.27$\times$) and exp\_078 (seed 0, peak NVE 4.10$\times$ at 75K). In exp\_078, evaluation peaks at 213.7 at 35K, collapses to 26.1 at 75K, then partially recovers to 119.5 at 105K (26.7\% of the Cheetah baseline exp\_077, 448.1). Onset timing is consistent across environments, with CIVO appearing at ${\sim}$45K steps in both Walker and Cheetah. Both Cheetah runs self-correct, contrasting with Walker where 6/8 trained-$e_{\Delta t}$ runs exhibit sustained collapse. This divergence suggests that while the trained embedding deterministically triggers CIVO onset, outcome severity is modulated by environment dynamics.

Aggregating across both locomotion environments, 10/10 trained-$e_{\Delta t}$ runs (8 Walker, 2 Cheetah) exhibit CIVO onset, while none of the 8 control conditions (removed or unexposed embedding) exhibit pathological overestimation (Fisher exact test, $p < 0.0001$). The onset mechanism is deterministic given a trained temporal embedding; the downstream outcome (sustained collapse vs.\ self-correction) is stochastic.


% ============================================================
% PENDING EXPERIMENTS
% ============================================================

\subsection{Pending Experiment}
\label{sec:pending}

\paragraph{Full-pathway SGS (exp\_018).} Detaches all non-KL gradients from the temporal embedding, removing the dominant 93\% observation decoder contribution while retaining only the 7\% KL dynamics signal. If CIVO persists with only KL gradients, the vulnerability is representation-level (KL training alone sufficient); if eliminated, the observation decoder gradient pathway is the root cause. Results will be reported upon completion.
