# Round 4 Track A-Main Changes

## Item 1: Table 1 — Add "Best Step" column, remove Dense/REINFORCE++ rows

### Before
```latex
\caption{1.7B results on ALFWorld (best checkpoint per seed, evaluated on held-out test sets). In-Dist: 32-task set; OOD: 134-task set. Cell~A reports best seed (2 seeds); Cell~B reports best checkpoint at step~5 (2 seeds). Cell~D reports mean of 2 seeds (In-Dist range: 28.1--40.6; OOD range: 10.4--23.9); Cell~D mean OOD (17.2\%) is consistent with the 11-seed evaluation (Table~\ref{tab:seed_variability}), which shows 36\% generalization rate. Dense reward and REINFORCE++: 1 seed each.}
\label{tab:main_results}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}llcc@{}}
\toprule
\textbf{Condition} & \textbf{Mechanisms} & \textbf{In-Dist (\%)} & \textbf{OOD (\%)} \\
\midrule
SFT baseline & --- & 12.50 & 6.72 \\
Cell A ($h{=}2$, step) & M1+M2 & 0 & 0 \\
Cell B ($h{=}2$, episode) & M1 only & 18.75 & 5.97 \\
Cell D (full, episode) & neither & \textbf{34.38} & \textbf{17.16} \\
\midrule
Dense reward & M1+M2 & 0 & 0 \\
REINFORCE++ & neither & 12.50 & --- \\
\bottomrule
\end{tabular}}
```

### After
```latex
\caption{1.7B results on ALFWorld. All cells report best checkpoint per seed, evaluated on held-out test sets. In-Dist: 32-task set; OOD: 134-task set. Cell~A reports best seed (2 seeds); Cell~B reports best checkpoint (2 seeds). Cell~D reports mean of 2 seeds (In-Dist range: 28.1--40.6; OOD range: 10.4--23.9); Cell~D mean OOD (17.2\%) is consistent with the 11-seed evaluation (Table~\ref{tab:seed_variability}), which shows 36\% generalization rate. See Appendix~\ref{app:additional} for additional baselines including REINFORCE++ and dense reward.}
\label{tab:main_results}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}llccc@{}}
\toprule
\textbf{Condition} & \textbf{Mechanisms} & \textbf{Best Step} & \textbf{In-Dist (\%)} & \textbf{OOD (\%)} \\
\midrule
SFT baseline & --- & --- & 12.50 & 6.72 \\
Cell A ($h{=}2$, step) & M1+M2 & 5 & 0 & 0 \\
Cell B ($h{=}2$, episode) & M1 only & 5 & 18.75 & 5.97 \\
Cell D (full, episode) & neither & 5 & \textbf{34.38} & \textbf{17.16} \\
\bottomrule
\end{tabular}}
```

## Item 2: Downgrade Factorial Claim (method.tex)

### Before
```latex
To separate the two mechanisms, we implement a $2 \times 2$ factorial varying observation scope and advantage granularity: \textbf{Cell~A} (truncated $h{=}2$ + step-level advantage; both mechanisms active), \textbf{Cell~B} (truncated $h{=}2$ + episode-level advantage; only M1 active), and \textbf{Cell~D} (full trajectory + episode-level advantage; neither active). The fourth cell, \textbf{Cell~C} (full trajectory + step-level advantage; only M2 active), would isolate sign misattribution without information loss. We attempted this configuration but encountered persistent training instability (Section~\ref{sec:factorial_experiments}; Appendix~\ref{app:cell_c}). Comparing A vs.\ B isolates sign misattribution; comparing B vs.\ D isolates information loss.
```

### After
```latex
To separate the two mechanisms, we design a $2 \times 2$ factorial varying observation scope and advantage granularity: \textbf{Cell~A} (truncated $h{=}2$ + step-level advantage; both mechanisms active), \textbf{Cell~B} (truncated $h{=}2$ + episode-level advantage; only M1 active), \textbf{Cell~D} (full trajectory + episode-level advantage; neither active), and \textbf{Cell~C} (full trajectory + step-level advantage; only M2 active). Cell~C encountered persistent numerical instability across six hyperparameter configurations (Appendix~\ref{app:cell_c}); we therefore evaluate a partial 3-of-4 factorial. Comparing A vs.\ B isolates sign misattribution; comparing B vs.\ D isolates information loss.
```

## Item 3: Non-Binary Reward Extension (theoretical_analysis.tex)

### Before
(No prior content — new paragraph added at end of Section 3)

### After
```latex
\paragraph{Extension to non-binary rewards.}
Propositions 1--2 assume binary reward ($r \in \{0, 1\}$). Our experimental setting uses a ternary scheme with a format penalty ($r \in \{-0.1, 0, 1\}$). The penalty introduces within-group reward variance even among failed episodes: a group may contain both $r = 0$ (task failure, correct format) and $r = -0.1$ (format violation) outcomes. This partial variance breaks the perfect correlation between advantage sign and episode outcome that drives the binary-case bound of $\leq$19.1\% (Proposition~2). Concretely, failed episodes with $r = 0$ can receive positive advantage when grouped with penalized episodes ($r = -0.1$), creating correct-sign updates that are absent in the binary case. The measured credit agreement of 52.07\% (Section~\ref{sec:sign_verification}) is thus consistent with theoretical expectations: substantially above the binary bound but far below the 100\% achievable with episode-level advantage. A detailed quantitative analysis appears in Appendix~\ref{app:sign_misattribution}.
```

## Item 4: Cohen's h Effect Size (experiments.tex)

### Before
```latex
only 52.07\% of windows with valid actions receive positive advantage, marginally above random chance ($p{=}0.025$ vs.\ 50\%; $+$2.07pp effect size).
```

### After
```latex
only 52.07\% of windows with valid actions receive positive advantage, marginally above random chance ($p{=}0.025$ vs.\ 50\%; Cohen's $h = 2\arcsin\sqrt{0.5207} - 2\arcsin\sqrt{0.5} \approx 0.041$, below the 0.2 small-effect threshold), confirming that credit agreement is effectively at chance, consistent with the theoretical prediction of near-random sign assignment.
```

## Item 7: Eq.6 Caveat Strengthened (theoretical_analysis.tex)

### Before
```latex
Empirical measurement from training logs confirms approximately comparable per-group advantage magnitudes ($|\hat{A}_{\text{correct}}|/|\hat{A}_{\text{wrong}}| \approx 1.32$; measured from a single training snapshot; validation across seeds and training stages would strengthen this estimate).
```

### After
```latex
Empirical measurement from training logs confirms approximately comparable per-group advantage magnitudes ($|\hat{A}_{\text{correct}}|/|\hat{A}_{\text{wrong}}| \approx 1.32$). This ratio is measured at a single training snapshot (step~5); we cannot rule out that it varies substantially across training stages. The cumulative divergence argument requires only that $|\hat{A}_{\text{correct}}|$ and $|\hat{A}_{\text{wrong}}|$ remain comparable in order of magnitude, which is consistent with gradient update mechanics but warrants broader empirical verification.
```

## M1: Definition 1 "Equivalently" Footnote (theoretical_analysis.tex)

### Before
```latex
Equivalently, window $k$ contains locally correct actions
```

### After
```latex
Equivalently,\footnote{This equivalence is approximate; it holds exactly when all trajectories within an episode are equally likely under the reference policy, and approximately under the mild assumption that policy drift remains small during early training.} window $k$ contains locally correct actions
```

## Q2: Cell B OOD Explanation (experiments.tex)

### Before
(No prior content — new paragraph added after Table 1)

### After
```latex
\paragraph{Cell~B OOD.} Cell~B's OOD performance (5.97\%) remains near the SFT baseline (6.72\%), confirming that removing M2 alone bounds learning without causing degradation.
```
