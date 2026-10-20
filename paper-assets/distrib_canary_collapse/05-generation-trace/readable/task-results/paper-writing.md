# paper writing

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_20260515T201359_result.json`
- **Structured JSON:** [`2aeb09c47bb26786ba2a.json`](../../sessions/2a/2aeb09c47bb26786ba2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```latex
\section{Discussion}\label{sec:discussion}

\paragraph{Granger precedence is not causation.}
Granger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\cite{granger1969investigating,shojaie2022granger}.
Bivariate Granger tests cannot exclude confounders: an unobserved process---such as a latent distributional shift in the training data---could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.
Our multi-method consensus framework inherits this limitation in full.
Throughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.
This distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \emph{causes} diversity collapse.

\paragraph{Calibration scope and generalization.}
All FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\alpha \in \{0.0, 0.25, 0.50, 0.75, 1.0\}$).
Generalization to other model architectures, datasets, or training protocols requires independent validation.
The consensus framework's structure---multi-method agreement combined with multi-seed replication---is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.
For instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.
Our ongoing GPT-2-medium experiments represent a first step toward cross-architecture validation, though results are not yet available.

\paragraph{FPR/FNR calibration asymmetry.}
The FPR and FNR estimates in our calibration analysis differ in their coverage of the seed dimension.
FPR is validated on the method dimension only, using a single seed at the null-control condition ($\alpha{=}0.0$).
FNR is validated on the joint method${\times}$seed dimension, aggregating across four seeds at full contamination ($\alpha{=}1.0$).
This asymmetry means our FPR estimate of 0\% may be optimistic: if seed-level variance in false positive rates is non-negligible, the true FPR under the consensus rule could exceed zero.
Full joint calibration---requiring multi-seed null-control experiments at $\alpha{=}0.0$---remains an open direction for future work.

\paragraph{Short time-series constraint.}
With $T{=}10$ generation cycles (11 data points per series), our time-series analyses operate near the lower bound of what standard methods require.
This series length is typical for iterative training studies, where each generation involves a complete training run, but it severely limits statistical power.
The Toda-Yamamoto procedure's elevated FNR (33.3\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.
This finding aligns with \citet{boettiger2012limits}, who demonstrated that early-warning signals have limited detection power in short time series.
Longer generation chains would improve power for all methods but impose substantial computational cost; this trade-off between statistical power and compute budget is inherent to iterative training research and cannot be resolved by methodological improvements alone.

\paragraph{Limitations.}
Several limitations constrain the generalizability of our findings.
First, we evaluate a single architecture family (Pythia-410M); canary dynamics may differ across architectures with different tokenization strategies, attention patterns, or model scales.
Second, training data is drawn from a single domain (a WikiText-103 subset), and domain-specific distributional properties may influence the coupling between canary and downstream metrics.
Third, we lack an intervention experiment: we observe that token entropy Granger-precedes diversity collapse at $\alpha{\geq}0.75$ but do not test whether acting on canary signals can prevent or delay collapse onset.
Fourth, our experiments use replace-only data accumulation; accumulate-mode training~\cite{dey2024breaking,kazdan2025collapse} may exhibit qualitatively different canary dynamics.
Finally, our canary claims are scoped to distinct-$n$ diversity metrics~\cite{li2016diversity}---not to model collapse broadly---as the perplexity channel proved spurious ($F{\approx}0$, $p{=}0.99$ after differencing)~\cite{schaeffer2025position}.

\paragraph{Future work.}
Several directions extend this work.
Multivariate VAR models would enable testing for confounders and multi-directional Granger relationships beyond our current bivariate framework.
Cross-architecture validation is needed: our GPT-2-medium experiments are in progress, and evaluation on larger-scale models would further test generalizability.
Online monitoring---integrating canary metrics into training pipelines for real-time collapse detection---is a natural applied extension.
Accumulate-mode experiments~\cite{dey2024breaking} would test whether canary dynamics differ from the replace-mode setting studied here.
Finally, connecting the empirically observed detectability boundary at $\alpha{\approx}0.50$--$0.75$ to theoretical phase transition analysis~\cite{truong2025entropy} could yield a principled explanation for why canary signals emerge at this contamination regime rather than at lower contamination levels.
```

~710 words. Constraint compliance summary:

- **PC11**: Paragraph 1 explicitly states Granger precedence ≠ true causality
- **PC05**: Paragraph 2 declares calibration specific to current setup
- **PC04**: Paragraph 3 flags FPR/FNR dimension asymmetry
- **PC07**: Paragraph 5 scopes claims to diversity collapse (distinct-n), not model collapse broadly
- **PC14**: No "consistently outperforms", "state-of-the-art", or unqualified "significantly"
- **C001**: No reference to Phase 2 single-seed TY cross-α trends

---
