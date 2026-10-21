% Experimental Setup — Draft v1
% Target: CoRL 2026
% Status: Draft, pending Director review

\section{Experimental Setup}
\label{sec:experimental_setup}

We design a controlled factorial experiment to isolate the mechanisms by which variable-rate imagination degrades performance in world-model reinforcement learning. All experiments use DreamerV3 \citep{hafner2023dreamerv3} as the base architecture, with modifications limited to the imagination rollout mechanism and temporal conditioning.

\subsection{Base Architecture and Modifications}
\label{sec:base_arch}

Our base agent is DreamerV3 \citep{hafner2023dreamerv3} with its Recurrent State-Space Model (RSSM) world model. The RSSM learns latent dynamics from experience and generates imagined trajectories for actor-critic learning. In the standard configuration, each imagination step corresponds to a single environment transition ($\Delta t = 1$).

We study a \textit{variable-rate imagination} mechanism that modifies two components of the standard pipeline:

\paragraph{Temporal embedding.} We add a temporal step-size embedding $e_{\Delta t} \in \mathbb{R}^{d}$ that conditions the RSSM transition function on the imagination step size $\Delta t$. We study three configurations:
\begin{itemize}
    \item \textbf{Trained} ($d{=}32$, gradients enabled): the embedding is jointly optimized with the world model, allowing the RSSM to specialize its predictions for different $\Delta t$ values.
    \item \textbf{Untrained} ($d{=}32$, gradients disabled): the embedding is randomly initialized and frozen, providing a fixed but uninformative temporal signal.
    \item \textbf{Removed} ($d{=}0$): no temporal conditioning is provided to the RSSM.
\end{itemize}

\paragraph{Temporal subsampling.} When enabled (\textsc{subsample on}), the replay buffer stores both $\Delta t{=}1$ and $\Delta t{=}2$ transitions, exposing the world model to multi-rate dynamics during training. When disabled (\textsc{subsample off}), only standard $\Delta t{=}1$ transitions are stored, and $\Delta t{>}1$ is used only during imagination rollouts.

\paragraph{Imagination step size.} During imagination, the agent rolls out trajectories at a fixed step size: either $\Delta t{=}1$ (standard) or $\Delta t{=}2$ (skipping one intermediate step per imagination transition).

\paragraph{Imagination horizon.} The number of imagination steps per rollout: $H{=}8$ or $H{=}15$ (DreamerV3 default). With $\Delta t{=}2$ imagination, an $H$-step rollout covers $2H$ environment steps of lookahead.

All other DreamerV3 components---the actor, critic, reward head, and continuation predictor---remain unmodified.

\subsection{Environment}
\label{sec:environment}

We evaluate on continuous control tasks from the DeepMind Control Suite \citep{tassa2018deepmind}:

\paragraph{Primary environment.} \textbf{Walker Walk}: a planar bipedal locomotion task with 24-dimensional proprioceptive observations (14 orientations, 1 height, 9 velocities) and 6-dimensional continuous actions. This task requires sustained coordination and provides a challenging testbed for diagnosing value overestimation, as the reward signal is dense and performance differences are clearly distinguishable.

\paragraph{Cross-environment validation.} We include \textbf{Cheetah Run} (17D observations, 6D actions) to test whether the identified mechanisms generalize beyond Walker Walk. The Cheetah baseline (exp\_077) converges to 448.1; treatment conditions (exp\_010b, exp\_078) replicate the trained-$e_{\Delta t}$ configuration from Walker.

All environments use \texttt{action\_repeat=2} and \texttt{time\_limit=1000}, with proprioceptive (non-pixel) observations processed by MLP encoders and decoders.

\subsection{Factorial Experiment Design}
\label{sec:factorial}

The core of our diagnostic methodology is a factorial experiment that systematically varies three factors governing variable-rate imagination. Table~\ref{tab:factorial} summarizes the experimental conditions.

\paragraph{Factors.}
\begin{enumerate}
    \item \textbf{Temporal embedding type}: trained ($d{=}32$) vs.\ untrained ($d{=}32$, frozen) vs.\ removed ($d{=}0$).
    \item \textbf{Subsampling strategy}: \textsc{on} (replay buffer contains both $\Delta t{=}1$ and $\Delta t{=}2$ transitions) vs.\ \textsc{off} ($\Delta t{=}1$ only).
    \item \textbf{Imagination horizon}: $H{=}8$ vs.\ $H{=}15$.
\end{enumerate}

\begin{table}[t]
\centering
\caption{Experimental conditions. All treatment conditions use $\Delta t{=}2$ imagination unless noted. ``Imag.\ $\Delta t$'' denotes the step size used during imagination rollouts. The baseline uses standard DreamerV3 ($\Delta t{=}1$ throughout). Exp.~006 enables temporal subsampling relative to exp.~005 (learned gate); all other hyperparameters are shared between the two.}
\label{tab:factorial}
\small
\begin{tabular}{llccccl}
\toprule
ID & Name & dt\_emb & Subsample & $H$ & Imag.\ $\Delta t$ & Role \\
\midrule
001 & Baseline & --- & --- & 15 & 1 & Reference \\
\midrule
006 & Fixed-dt2 & trained & on & 15 & 2 & Initial dt$>$1 test \\
007 & Fixed-dt4 & trained & on & 15 & 4 & dt magnitude test \\
\midrule
008a & F-A & exp$^a$ & off & 15 & 2 & Unexposed embedding control \\
008c & F-C & exp$^a$ & off & 8 & 2 & Horizon control \\
008d & F-D & trained & on & 8 & 2 & Collapse condition \\
008e\_v3 & F-E & trained & on & 15 & 1 & $\Delta t{=}1$ imag.\ control \\
008f & F-F & removed & on & 8 & 2 & Causal ablation \\
\midrule
015b & Frozen-emb ctrl & frz$^b$ & on & 8 & 2 & Frozen embedding control \\
016e & Stop-grad & trained$^\dagger$ & on & 8 & 2 & Stop-gradient (reward-only) \\
018 & Full-SGS & trained$^\ddagger$ & on & 8 & 2 & Full stop-gradient$^{\text{p}}$ \\
\midrule
005 & Learned gate & adaptive & off & 15 & learned & Full adaptive \\
\bottomrule
\end{tabular}
\vspace{2pt}
{\footnotesize $^a$ Trained ($d{=}32$, gradients enabled) but never exposed to $\Delta t{>}1$ data during world-model training (subsample OFF $\Rightarrow$ only $\Delta t{=}1$ transitions in replay buffer); $\Delta t{=}2$ used only during imagination.\\
$^b$ Frozen random projection ($d{=}32$, \texttt{requires\_grad=False}): provides a fixed, uninformative temporal signal that cannot co-adapt with the RSSM dynamics.\\
$^\dagger$ \texttt{reward\_dt\_emb\_detach=True}: gradients from the reward head are stopped before the temporal embedding; all other gradients flow normally.\\
$^\ddagger$ All non-KL gradients to \texttt{dt\_emb} detached (observation decoders + reward head); only KL-dynamics gradients (7\%) remain. $^{\text{p}}$\,Pending at time of submission.}
\end{table}

\paragraph{Key controlled comparisons.} Rather than filling all cells of a complete factorial grid, we prioritize comparisons that isolate specific causal factors:

\begin{itemize}
    \item \textbf{008d vs.\ 008f} (trained dt\_emb vs.\ removed; all else equal): isolates the effect of temporal embedding conditioning on value overestimation. Both conditions use subsample \textsc{on} and $H{=}8$ with $\Delta t{=}2$ imagination.
    \item \textbf{008c vs.\ 008a} ($H{=}8$ vs.\ $H{=}15$; all else equal): isolates the effect of imagination horizon length. Both use trained-but-unexposed dt\_emb (subsample \textsc{off}), and $\Delta t{=}2$ imagination.
    \item \textbf{006 vs.\ 008a} (both trained dt\_emb, $H{=}15$; difference is subsample \textsc{on} vs.\ \textsc{off}): isolates data composition---whether the world model is exposed to $\Delta t{>}1$ transitions during training. Both conditions have identical trained embeddings ($d{=}32$, gradients enabled), so the divergence (006 collapses; 008a remains stable at 85\% baseline) demonstrates that embedding training alone is insufficient for CIVO; exposure to multi-rate data is additionally required.
    \item \textbf{008d vs.\ 008a} (subsample \textsc{on} vs.\ \textsc{off}; both trained dt\_emb, $\Delta t{=}2$ imagination; $H$ differs: 8 vs.\ 15): a supporting comparison that corroborates the 006 vs.\ 008a result. Despite 008a's longer horizon (which generally aids learning), it avoids CIVO while the shorter-horizon 008d collapses, reinforcing that data composition---not horizon length---is the operative variable.
    \item \textbf{008e\_v3} ($\Delta t{=}1$ imagination with multi-rate training data): tests whether restricting imagination to $\Delta t{=}1$ while training the world model on multi-rate data is sufficient to avoid CIVO.
\end{itemize}

\noindent\textbf{Key conclusion from the factorial structure.} Trained dt\_embedding triggers CIVO only when the world model is also exposed to $\Delta t{>}1$ training data: exp\_008a (trained, subsample OFF) remains healthy, while frozen dt\_embedding is safe even with full multi-rate exposure (exp\_015b, peak NVE 1.45$\times$ $\to$ self-corrects). The necessary trigger is the \textit{combination} of a trainable embedding and multi-rate data exposure.

\paragraph{Multi-seed replication.} All primary conditions are run with seed 1. To assess robustness, we replicate four key Walker conditions with seed 2: baseline (009a, complete, stable 957.87@505K), 008d (009b, complete, self-corrected, peak 278.5@95K), 008f (009c, complete, decline), and 008e\_v3 (008e\_v3\_s2, complete, collapsed via non-CIVO pathway). Cheetah Run adds two independent seeds under the trained-$e_{\Delta t}$ condition (exp\_010b seed 1, exp\_078 seed 0), both exhibiting CIVO onset. Per-seed trajectories are reported individually rather than averaged, to preserve visibility of seed-dependent behaviors such as the stochastic collapse observed in 008d.

\subsection{Diagnostic Framework: Normalized Value-Evaluation Ratio}
\label{sec:diagnostic}

A central challenge in diagnosing variable-rate imagination failures is distinguishing \textit{pathological} value overestimation (where the critic drives the actor toward incorrect behavior) from \textit{benign} value overshoot (a normal feature of temporal-difference learning). We introduce a normalized diagnostic metric that addresses this.

\paragraph{Value-evaluation ratio.} For a given experiment at training step $k$, we define the value-evaluation ratio:
\begin{equation}
    r_k = \frac{\bar{v}_k}{\bar{R}_k},
    \label{eq:ve_ratio}
\end{equation}
where $\bar{v}_k$ is the mean predicted value across imagined states and $\bar{R}_k$ is the mean evaluation return (averaged over 10 evaluation episodes). This ratio measures how closely the critic's value estimates track actual achievable returns.

\paragraph{Normalized value-evaluation ratio.} Since even the standard DreamerV3 baseline exhibits value overshoot (the critic's predictions exceed evaluation returns during early training), we normalize by the baseline's ratio at the same training step:
\begin{equation}
    \hat{r}_k = \frac{r_k^{\text{exp}}}{r_k^{\text{baseline}}}.
    \label{eq:nve}
\end{equation}

This normalization removes the baseline's own overshoot trend, isolating the \textit{excess} overestimation attributable to the experimental manipulation. In the current analysis, $r_k^{\text{baseline}}$ is computed from the mean of seeds 1 and 2 (009a, both 500K+ steps).

\paragraph{Diagnostic marker.} We calibrate a diagnostic threshold from our experimental conditions. We emphasize that this threshold serves as an empirical \textit{marker} for identifying pathological overestimation, not as a hypothesis test---it is derived from and evaluated on the same Walker experiments, with Cheetah Run providing independent cross-environment validation (see Section~\ref{sec:cross_env}):
\begin{itemize}
    \item $\hat{r}_k > 1.5$ (at $k \geq 35\text{K}$ steps, where baseline $r_k > 0.24$): \textbf{pathological} --- the critic overestimates returns far beyond baseline levels. This marker separates trained dt\_embedding conditions from untrained/removed conditions (4/4 classification accuracy across seeds 1 and 2). Catastrophic collapse is a stochastic downstream outcome of sustained pathological overestimation. At earlier steps ($k < 35\text{K}$), the baseline's small $r_k$ denominator amplifies noise, producing unreliable ratios.
    \item $0.8 \leq \hat{r}_k \leq 1.2$: \textbf{normal} --- value estimates are within the baseline's overshoot range.
    \item $\hat{r}_k < 0.7$: \textbf{value suppression} --- the critic underestimates returns relative to baseline, indicating overly conservative value estimates.
\end{itemize}

\paragraph{Classification accuracy.} Using the $\hat{r}_k > 1.5$ threshold at $k \geq 35\text{K}$ steps (task B2), the NVE diagnostic achieves AUROC\,=\,0.958 across 10 experiments, with 9/10 classification accuracy. The single false positive is 008e\_v3\_s2, which exhibits late collapse via a non-CIVO pathway identified through trajectory analysis. At the optimal B1 threshold $\hat{r}_k > 3.9$, the diagnostic achieves AUROC\,=\,1.0 with 10/10 accuracy. The 95\% Clopper--Pearson confidence interval for 9/10 accuracy is $[0.555,\, 0.997]$; for reference, 10/10 yields $[0.692,\, 1.0]$. Full per-condition NVE trajectories and threshold sensitivity analysis (\texttt{nve\_sensitivity\_table}) are reported in the supplementary material.

\paragraph{Supplementary diagnostic: late-training value-return ratio.} As a complementary signal, we examine the raw value-return ratio $v/R = \bar{v}_k / \bar{R}_k$ in late training ($k > 45\text{K}$ steps). In this regime, collapsed conditions exhibit $v/R > 1.5$ (the critic predicts returns exceeding what the agent actually achieves), while healthy conditions maintain $v/R < 1.0$. This provides a clean binary separation without requiring baseline normalization, though it is only reliable after sufficient training.

\subsection{Training Details}
\label{sec:training_details}

All experiments share the DreamerV3 \texttt{dmc\_proprio} default configuration: \texttt{train\_ratio=512}, 4 parallel environments, \texttt{batch\_size=16}, \texttt{batch\_length=64}, and MLP encoder/decoder networks for proprioceptive observations. We use the Adam optimizer with DreamerV3's default learning rates and gradient clipping.

\paragraph{Training duration.} The baseline is trained for 500K environment steps to establish convergence behavior. Treatment conditions are trained for 55K--112K steps, sufficient to observe the onset and progression of the identified failure modes. The $\Delta t{=}1$ imagination control (008e\_v3) is trained for 105K steps.

\paragraph{Evaluation protocol.} Every 10K training steps, the agent is evaluated over 10 episodes with the deterministic policy (action noise disabled). We report the mean evaluation return across these episodes. For multi-seed conditions, we report per-seed trajectories rather than averaged curves to preserve visibility of seed-dependent behaviors.

\paragraph{Reproducibility.} All primary conditions use seed 1; key conditions (baseline, 008d, 008f, 008e\_v3) include seed 2 replication (see \S\ref{sec:factorial}). All experiments use identical random seeds for environment initialization and network parameter initialization, differing only in the factorial treatment variables. Code is based on the official DreamerV3 implementation with modifications restricted to the imagination rollout and temporal embedding modules.
