# Exp\_018 Full-SGS Pre-Written Paragraphs (Two Versions)

**Status:** Pre-written before results. Pick Version A or B based on actual 018 outcome.

**Decision criteria:**
- eval ≥ 500, NVE < 1.5× in 35K+ window → **Version A** (CIVO eliminated)
- eval < 300, NVE > 1.5× → **Version B** (CIVO persists)
- eval 300–500 or NVE 1.3–1.7× → **Version C** (partial effect, ambiguous zone)

---

## Version A: CIVO Disappears (Gradient-Level Vulnerability)

### analysis.tex §5.3.5 — Full-Pathway Gradient Stopping Eliminates CIVO

```latex
\paragraph{Full-pathway SGS eliminates CIVO.}
The gradient decomposition in Table~\ref{tab:gradient_decomposition} reveals that
observation decoders contribute 92.7\% of all gradients flowing into the temporal
embedding $e_{\Delta t}$, with KL dynamics accounting for 7.3\% and the reward head
contributing exactly zero. Exp\_016e (reward-only SGS) confirmed this decomposition
empirically: detaching the reward pathway---a \emph{null intervention} given the zero
gradient share---left CIVO entirely intact (NVE $10.42\times$;
\S\ref{sec:016e_reinterp}). The critical test is whether removing the dominant 92.7\%
observation decoder pathway suffices.

Exp\_018 applies full-pathway SGS, detaching all non-KL gradients from $e_{\Delta t}$
so that only the 7.3\% KL dynamics signal remains. Under the same configuration that
produces catastrophic CIVO in exp\_008d (trained $e_{\Delta t}$, $d{=}32$, subsample ON,
$H{=}8$), exp\_018 reaches evaluation [EVAL] at 105K steps with peak NVE [NVE]$\times$
in the 35K+ diagnostic window---well below the $1.5\times$ CIVO threshold. This
directly contrasts with exp\_008d's collapse to evaluation 82.8 and NVE $4.12\times$.

The residual 7.3\% KL gradient does not trigger CIVO within the 105K training horizon
tested. The KL loss $D_\mathrm{KL}(q_\phi \| p_\theta)$ constrains only the consistency
between posterior and prior distributions---it enforces that the transition model's
predictions align with encoder observations, but does not directly encode
observation-level temporal patterns that enable scale-dependent reward prediction bias. In contrast, observation
decoder gradients back-propagate reconstruction objectives across the full
24-dimensional proprioceptive signal, providing a rich channel through which
$e_{\Delta t}$ can learn $\Delta t$-specific state features that the reward head
subsequently exploits.

The progression across interventions establishes a clear causal chain:
exp\_016e removes 0\% of $e_{\Delta t}$ gradients (no-op) $\rightarrow$ full CIVO
($10.42\times$); exp\_018 removes 92.7\% $\rightarrow$ no CIVO ([NVE]$\times$);
exp\_008f removes 100\% (no embedding) $\rightarrow$ no CIVO ($0.97\times$). The
observation decoder gradient pathway is necessary for CIVO
induction---the dominant causal factor. The complete causal mechanism is: observation decoder gradients train
$e_{\Delta t}$ to encode $\Delta t$-specific temporal features $\rightarrow$ the RSSM
develops scale-dependent state representations $\rightarrow$ the reward head produces
biased predictions at $\dt{>}1$ $\rightarrow$ the critic overestimates imagined returns
$\rightarrow$ policy exploitation triggers CIVO collapse.
```

### results.tex Table 1 Row (Version A)

```latex
\rowcolor{white}
018 & Full-SGS & trn$^\ddagger$ & ON & 8 & [EVAL]@105K & [NVE]$\times$ & Healthy \\
```

> $^\ddagger$: trained $e_{\Delta t}$ ($d{=}32$) with full-pathway stop-gradient (only KL dynamics gradients retained).

---

## Version B: CIVO Persists (Representation-Level Vulnerability)

### analysis.tex §5.3.5 — Full-Pathway Gradient Stopping Fails to Eliminate CIVO

```latex
\paragraph{Full-pathway SGS is insufficient: CIVO operates at the representation level.}
Exp\_018 applies full-pathway SGS to the temporal embedding $e_{\Delta t}$, detaching
all gradients except the 7.3\% KL dynamics contribution
(Table~\ref{tab:gradient_decomposition}). This removes the dominant observation decoder
pathway (92.7\%) that we hypothesized as CIVO's primary transmission channel. Yet under
the same configuration that produces CIVO in exp\_008d (trained $e_{\Delta t}$,
$d{=}32$, subsample ON, $H{=}8$), exp\_018 still collapses: evaluation degrades to
[EVAL] at [STEP]K steps with peak NVE [NVE]$\times$ in the 35K+ window, confirming
sustained value overestimation above the $1.5\times$ diagnostic threshold.

This result decisively shifts the mechanistic interpretation. The 7.3\% KL dynamics
gradient, though small in magnitude, is sufficient to encode harmful temporal
information into the RSSM state representation. The KL loss
$D_\mathrm{KL}(q_\phi \| p_\theta)$ constrains the transition model to predict
accurate state distributions conditioned on $e_{\Delta t}$---but this is precisely the
channel through which $\Delta t$-dependent prediction bias enters. The transition model
\emph{must} learn different dynamics for different temporal scales to minimize the KL
objective; this scale-dependent state structure then propagates to all downstream heads,
including reward prediction, regardless of whether observation decoder gradients flow
back to $e_{\Delta t}$.

The contrast with exp\_008f is instructive: removing $e_{\Delta t}$ entirely eliminates
CIVO (NVE $0.97\times$, evaluation 503.0), while retaining it with only 7.3\% of
gradients still triggers collapse ([NVE]$\times$). The vulnerability is not proportional
to gradient magnitude---it is binary in the \emph{architectural capacity} to represent
temporal information. As long as $e_{\Delta t}$ exists and receives \emph{any} learning
signal, the transition model can develop $\Delta t$-conditioned dynamics that produce
scale-dependent reward prediction bias.

This has direct implications for hierarchical world-model methods such as
THICK~\citep{gumbsch2024thick} and Hieros~\citep{mattes2024hieros} that inherently operate across
temporal scales. If CIVO is a representation-level phenomenon rather than a
gradient-pathway artifact, flat gradient stopping is fundamentally insufficient.
Mitigation requires architectural interventions that enforce temporal separation in the
state space---e.g., orthogonality constraints between temporal-scale representations,
information bottlenecks that prevent $\Delta t$ from influencing reward-relevant state
dimensions, or explicit factorization of temporal and reward-relevant features.
```

### results.tex Table 1 Row (Version B)

```latex
\rowcolor{gray!15}
018 & Full-SGS & trn$^\ddagger$ & ON & 8 & [EVAL]@[STEP]K & [NVE]$\times$ & CIVO collapse \\
```

> $^\ddagger$: trained $e_{\Delta t}$ ($d{=}32$) with full-pathway stop-gradient (only KL dynamics gradients retained).

---

## Placeholder Substitution Guide

When 018 results arrive, replace:

| Placeholder | Source |
|-------------|--------|
| `[EVAL]` | Final or peak evaluation score |
| `[NVE]` | Peak NVE in 35K+ window |
| `[STEP]` | Step at which eval is reported (Version B only) |

## Quick Reference: Control Experiments

| Exp | Intervention | Gradient removed | NVE | Eval | Outcome |
|-----|-------------|-----------------|-----|------|---------|
| 008d | None (full trained dt_emb) | 0% | 4.12× | 82.8 | CIVO collapse |
| 008f | Remove dt_emb entirely | 100% | 0.97× | 503.0 | Healthy |
| 016e | Reward-only SGS | 0% (reward=0, no-op) | 10.42× | 31.7 | CIVO collapse |
| 018 | Full-SGS (obs decoder detach) | 92.7% | **TBD** | **TBD** | **TBD** |

---

## Version C: Partial Effect (Ambiguous Zone)

**Applies when:** eval 300–500 or NVE 1.3–1.7× (neither clearly eliminated nor clearly persisting).

### analysis.tex §5.3.5 — Full-Pathway Gradient Stopping Attenuates but Does Not Eliminate CIVO

```latex
\paragraph{Full-pathway SGS attenuates CIVO: observation decoder gradients are the primary but not sole pathway.}
Exp\_018 applies full-pathway SGS, detaching all non-KL gradients from $e_{\Delta t}$
so that only the 7.3\% KL dynamics signal remains. Under the same configuration that
produces catastrophic CIVO in exp\_008d (trained $e_{\Delta t}$, $d{=}32$, subsample ON,
$H{=}8$), exp\_018 reaches evaluation [EVAL] at 105K steps with peak NVE [NVE]$\times$
in the 35K+ diagnostic window. This represents a substantial attenuation relative to
exp\_008d (NVE $4.12\times$, eval 82.8) but does not achieve the full protection
observed in exp\_008f (NVE $0.97\times$, eval 503.0).

The partial protection indicates that the observation decoder gradient pathway is the
\emph{primary} contributor to CIVO---removing it reduces NVE from $4.12\times$ to
[NVE]$\times$---but the residual 7.3\% KL dynamics gradient retains sufficient capacity
to induce sub-threshold overestimation within the 105K training horizon. The KL loss
$D_\mathrm{KL}(q_\phi \| p_\theta)$ provides a weaker but non-negligible channel:
the transition model must still condition on $e_{\Delta t}$ to satisfy the KL objective,
encoding some degree of $\Delta t$-dependent state structure that downstream heads can
exploit.

This positions the vulnerability as \emph{primarily gradient-level} (93\% contribution
from observation decoders) with a \emph{secondary representation-level} component (7\%
KL pathway). The intervention hierarchy is: reward-only SGS (0\% removed, no-op,
$10.42\times$) $\rightarrow$ full-pathway SGS (92.7\% removed, attenuated,
[NVE]$\times$) $\rightarrow$ full removal (100\%, eliminated, $0.97\times$). Complete
mitigation likely requires either extending the gradient barrier to include KL dynamics
(removing all learning signal from $e_{\Delta t}$, functionally equivalent to removal)
or architectural separation of temporal and reward-relevant representations.
```

### results.tex Table 1 Row (Version C)

```latex
\rowcolor{white}
018 & Full-SGS & trn$^\ddagger$ & ON & 8 & [EVAL]@105K & [NVE]$\times$ & Attenuated \\
```
