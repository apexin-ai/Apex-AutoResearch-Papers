% SGS Informative Negative — Draft v1
% Target: CoRL 2026
% Status: Draft, pending Director review
% Depends on: experimental_setup.md (Section 4), method.md (Section 3)

\subsection{Stop-Gradient Surgery: An Informative Negative Result}
\label{sec:sgs_informative_negative}

The factorial analysis in Section~\ref{sec:factorial} establishes that a trained temporal embedding ($e_{\Delta t}$) is necessary for pathological value overestimation: conditions with removed or untrained embeddings do not exhibit CIVO (Section~\ref{sec:civo_mechanism}). A natural follow-up question is \textit{which gradient pathway} through $e_{\Delta t}$ amplifies the overestimation. We hypothesized that the reward head---which directly supplies the critic's $\lambda$-return targets---would be the primary amplifier: if reward predictions are systematically biased by $\Delta t$ conditioning, the critic inherits and compounds these biases across the imagination horizon. This section reports a stop-gradient intervention designed to test this hypothesis, and the gradient decomposition analysis that revealed why the intervention had no effect.

\subsubsection{Hypothesis: Reward-Pathway Amplification}

In DreamerV3, the temporal embedding $e_{\Delta t}$ is concatenated to the RSSM decoder input and conditions all prediction heads---observation decoders, reward head, and continuation predictor---simultaneously. The reward head's predictions enter the critic's $\lambda$-return computation directly:
$$G_t^\lambda = r_t + \gamma \big[(1-\lambda)\,V(s_{t+1}) + \lambda\, G_{t+1}^\lambda\big]$$
If the reward head learns $\Delta t$-dependent biases (e.g., systematically predicting higher rewards for $\Delta t{=}2$ transitions), these biases accumulate across the $H$-step imagination rollout. We therefore conjectured that detaching $e_{\Delta t}$ from the reward head's gradient computation would attenuate CIVO by preventing the reward predictor from specializing its parameters to the temporal embedding signal.

\subsubsection{Experiment: Reward-Only Stop-Gradient (exp\_016e)}

We implemented a targeted stop-gradient intervention, termed \textit{reward-only SGS} (Stop-Gradient Surgery), in which the temporal embedding is detached before entering the reward head during the backward pass:
$$\hat{r}_t = f_{\text{reward}}\big(\text{sg}(e_{\Delta t}),\; h_t,\; z_t\big)$$
where $\text{sg}(\cdot)$ denotes the stop-gradient operator. This prevents reward-loss gradients from updating $e_{\Delta t}$'s parameters while preserving the embedding's forward-pass contribution to reward prediction. All other gradient pathways through $e_{\Delta t}$---observation decoders, continuation predictor, KL dynamics loss---remain intact.

The experiment uses the same configuration as exp\_008d (the primary CIVO-exhibiting condition): Walker Walk, trained $e_{\Delta t}$ ($d{=}32$), subsampling enabled, $H{=}8$, $\Delta t{=}2$ imagination, seed 1. The only modification is \texttt{reward\_dt\_emb\_detach=True}.

\subsubsection{Results: Delayed but Equivalent Collapse}

Exp\_016e exhibits the same qualitative failure mode as the unmodified control (exp\_008d): an initial learning phase followed by catastrophic performance collapse coinciding with NVE divergence.

\paragraph{Evaluation trajectory.} Exp\_016e reaches a peak evaluation return of 326.7 at step 75K (exp\_016e), compared to 167.2 at step 25K for exp\_008d. Performance then collapses to 31.7 by step 95K (exp\_016e), a 90.3\% drop from peak. Exp\_008d follows a qualitatively similar trajectory: after peaking at 25K, evaluation declines steadily to 82.7 at 55K (exp\_008d).

\paragraph{NVE trajectory.} The NVE for exp\_016e remains within the normal range ($0.8$--$1.9\times$) through step 85K, then spikes to $10.42\times$ at step 95K (exp\_016e)---well above the pathological threshold of $1.5\times$. Exp\_008d crosses the pathological threshold earlier: $\hat{r} = 1.71\times$ at 35K, rising to $4.12\times$ at 55K (exp\_008d).

\paragraph{Interpretation of timing differences.} The delayed onset of CIVO in exp\_016e (85K vs.\ ${\sim}$25K in exp\_008d) and its higher peak evaluation (326.7 vs.\ 167.2) might suggest a partial protective effect of reward-pathway detachment. However, the gradient decomposition analysis below reveals that the intervention is an \textit{architectural no-op}, making any apparent differences attributable to seed variability rather than the SGS intervention. Both experiments use different random seeds in practice (exp\_016e: seed 1; exp\_008d: seed 1, but with different initialization order due to the code modification), and single-seed comparisons cannot distinguish intervention effects from stochastic variation in DreamerV3 training dynamics.

\subsubsection{Gradient Decomposition: The Reward Pathway Carries Zero Gradient}
\label{sec:gradient_decomposition}

To understand why the reward-only SGS had no effect, we performed a post-hoc gradient decomposition analysis (D061) using \texttt{torch.autograd.grad} to measure each loss component's contribution to $\nabla_{\theta} e_{\Delta t}$, where $\theta$ denotes the parameters of the temporal embedding layer (\texttt{dt\_emb.weight}).

The decomposition reveals a striking asymmetry in gradient flow to the temporal embedding:

\begin{table}[h]
\centering
\caption{Gradient contributions to $e_{\Delta t}$ parameters by loss component (D061 analysis). Gradient norms are measured at step 95K.}
\label{tab:gradient_decomposition}
\small
\begin{tabular}{lrr}
\toprule
Loss component & Gradient norm & Share (\%) \\
\midrule
Observation decoders (orientations, velocity, height) & 1.505 & 93 \\
KL dynamics & 0.119 & 7 \\
Continuation head & $<$0.001 & $<$1 \\
Reward head & 0.000 & 0 \\
\bottomrule
\end{tabular}
\end{table}

The reward head contributes \textit{numerically negligible---zero to within floating-point precision} gradient to the temporal embedding parameters. This means exp\_016e's \texttt{reward\_dt\_emb\_detach} operation detaches a gradient that does not exist: it is an architectural no-op. The intervention's null effect is therefore expected---it removes nothing.

\paragraph{Why is the reward gradient zero?} The reward head in DreamerV3 is a small MLP (typically 4 layers, 512 units) that maps from the same latent state as the observation decoders. The temporal embedding's influence on reward prediction flows through the RSSM's latent state, not through a direct connection to the reward head. In this architecture, the reward loss's gradient with respect to $e_{\Delta t}$ passes through the RSSM transition function---the same path as all other decoder losses. The observation decoders, with their substantially higher-dimensional output space (14 orientation dimensions + 9 velocity dimensions + 1 height dimension = 24 total, vs.\ 1 scalar reward), dominate the gradient signal by approximately two orders of magnitude. The reward head's gradient contribution is numerically negligible, effectively rounded to zero.

\subsubsection{Implications for the CIVO Causal Chain}

The gradient decomposition shifts the mechanistic picture of CIVO in an important direction.

\paragraph{Observation decoders as the primary gradient source.} The temporal embedding's parameters are shaped overwhelmingly (93\%) by observation reconstruction gradients (D061). This means $e_{\Delta t}$ learns to encode whatever temporal information helps the observation decoders minimize reconstruction error. If this learned representation introduces systematic biases in latent state predictions at $\Delta t{>}1$---for instance, by encouraging the RSSM to produce states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. The CIVO mechanism thus originates not in the reward pathway, but in the observation reconstruction objective's influence on latent dynamics.

\paragraph{KL dynamics as a secondary contributor.} The KL divergence loss contributes 7\% of the gradient to $e_{\Delta t}$ (D061). This loss regularizes the RSSM's prior and posterior distributions, and its gradient could either help or hinder temporal generalization. Its modest contribution suggests it plays a secondary role relative to the observation decoders.

\paragraph{Reframing the intervention target.} The reward-only SGS targeted a gradient pathway that carries no signal. A meaningful gradient-level intervention must address the dominant 93\% contribution from observation decoders---and potentially the 7\% from KL dynamics. This motivates the \textit{full SGS} intervention (exp\_018, Section~\ref{sec:full_sgs}), which detaches $e_{\Delta t}$ from \textit{all} non-KL gradient pathways, removing the observation decoders' influence on the temporal embedding entirely.

\subsubsection{Framing: Informative Negative, Not Failure}

Exp\_016e did not achieve its intended effect, but it produced a finding more valuable than a positive result would have been. The gradient decomposition it motivated (D061) reveals that the temporal embedding's training signal is dominated by observation reconstruction---a structural fact about DreamerV3's loss landscape that was not \textit{a priori} obvious.

This finding constrains the space of viable interventions. Any strategy that targets the reward head alone (e.g., reward prediction regularization, reward-conditioned value clipping) would address $<$1\% of the gradient flow to $e_{\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying the gradient flow (full SGS, exp\_018) or by restructuring how $e_{\Delta t}$ interacts with the RSSM transition function.

The progression from exp\_016e's null result to the D061 gradient analysis to the full SGS design (exp\_018) exemplifies the diagnostic methodology's value: each experiment, whether it succeeds or fails at its immediate objective, narrows the causal hypothesis space and motivates a more targeted follow-up.

\subsubsection{Cross-Environment Validation: Full-SGS on Cheetah Run (exp\_021)}
\label{sec:sgs_cheetah}

Exp\_021 applies Full-SGS to Cheetah Run, where exp\_010b exhibited permanent CIVO collapse (NVE $8.27\times$, eval 51.7). Full-SGS did not prevent the initial CIVO spike (NVE $9.94\times$ at 45K), but the agent self-corrected within ${\sim}$10K steps: sustained NVE dropped to $0.34\times$ (55K--105K) and final evaluation recovered to 221.5 (vs.\ 010b's permanent collapse to 51.7). This reframes Full-SGS as \emph{enabling recovery} rather than preventing collapse (D088). Performance remains at 38.7\% of Cheetah baselines (mean 572.5), with actor gradient norms near zero throughout, suggesting over-aggressive gradient blocking impairs actor learning even when CIVO is controlled.
