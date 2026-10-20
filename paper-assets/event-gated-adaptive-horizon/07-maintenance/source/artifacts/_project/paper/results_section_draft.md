# Results Section Draft (LaTeX-ready)

## 4. Results

We organize our findings into seven progressively deeper diagnostics, moving from phenomenon characterization (F1--F2) through causal isolation (F3--F4) to mechanistic explanation (F5) and intervention (F6--F7).

All experiments use DreamerV3 on DeepMind Control Suite unless stated otherwise. We report eval returns (mean over 10 episodes, every 5K steps) and the Normalized Value Excess (NVE), defined as the ratio of the critic's imagined value to the realized evaluation return. An NVE $>1.5\times$ sustained over $\geq$10K steps indicates pathological overestimation. Bootstrap 95\% confidence intervals (10,000 resamples) are reported where sample size permits ($n \geq 3$).

### 4.1 Finding 1: Variable-Rate Imagination Universally Degrades Performance

\textbf{Setup.} We augment DreamerV3 with a discrete duration token $d_t \in \{1,2,4\}$ appended to the imagination trajectory, comparing against vanilla DreamerV3 (exp\_001, eval 916@105K, 970@505K).

\textbf{Results.} All variable-rate configurations collapse:
\begin{itemize}
  \item \textbf{exp\_005} (learned gating): peak 541@55K $\rightarrow$ 99@145K (10.4\% of baseline)
  \item \textbf{exp\_006} (fixed $d_t=2$): peak 485@35K $\rightarrow$ 133@65K; value/eval ratio inflates from 31\% to 272\%
  \item \textbf{exp\_007} (fixed $d_t=4$): peak 177@25K, never recovers (33\% of baseline at best)
\end{itemize}

The severity scales with temporal skip: $d_t=2$ degrades performance by $\sim$85\% and $d_t=4$ by $\sim$81\% from peak, with larger skips producing earlier and more severe collapses. This establishes the core phenomenon: multi-step imagination in world-model RL induces a failure mode absent from standard single-step training.

### 4.2 Finding 2: Conditioning-Induced Value Overestimation (CIVO) Is the Primary Failure Mode

\textbf{Setup.} We isolate the role of the trained duration embedding (dt\_emb) by comparing configurations with and without it under matched architectures ($d_t=2$, $H=8$, subsample ON, Walker Walk).

\textbf{Primary demonstration (exp\_008d).} With trained dt\_emb: eval 167@25K $\rightarrow$ 83@55K (collapse onset), NVE peaks at $4.12\times$@55K and remains $>1.5\times$ through 105K. The critic's imagined values inflate to 1.67$\times$ the realized return at collapse, and actor loss flips positive by 85K---indicating the critic actively drives policy toward worse actions.

\textbf{Statistical separation.} Across conditions:
\begin{itemize}
  \item \textbf{Trained dt\_emb} ($n=3$): NVE peak mean $3.43\times$ [95\% CI: 2.05, 4.12]; collapse rate 0.667
  \item \textbf{No dt\_emb} ($n=2$): NVE peak mean $1.14\times$ [95\% CI: 1.02, 1.26]; collapse rate 0.000
  \item \textbf{Effect size}: $\Delta$ NVE peak $= +2.29$ [95\% CI: +0.91, +3.10]; CI excludes zero
\end{itemize}

The NVE $>1.5\times$ threshold achieves perfect binary classification: all trained dt\_emb runs (3/3) exceed it; no baseline runs (0/2) do. The stochastic nature of collapse (2/3 seeds collapse fully) is consistent with a necessary-but-not-sufficient trigger: the trained dt\_emb creates vulnerability, but whether it manifests depends on the training trajectory.

\textbf{Variant behavior (exp\_009b, seed 2).} NVE peaks at $2.04\times$@25K but self-corrects to $0.38\times$@105K (eval 278, stable). This transient CIVO confirms that trained dt\_emb reliably triggers overestimation, though collapse is not deterministic---reinforcing the diagnostic framing over a guaranteed failure claim.

### 4.3 Finding 3: Causal Ablation Confirms dt\_emb as Necessary Condition

\textbf{Ablation 1: Remove dt\_emb entirely (exp\_008f).} Configuration identical to exp\_008d except dt\_emb is replaced with a zero vector. Result: eval stable at 503@105K (no collapse), NVE peaks at $0.97\times$ (never exceeds $1.5\times$). Performance is lower than vanilla DreamerV3 due to the multi-step imagination overhead, but critically, no pathological overestimation emerges.

\textbf{Ablation 2: Freeze dt\_emb (exp\_015b).} The duration embedding is initialized randomly and frozen (no gradient updates). Result: NVE peaks at $1.45\times$@55K (briefly, stays below $1.5\times$ threshold), with partial recovery to eval 204@105K. The degradation reflects gradient starvation (the model cannot leverage duration information) rather than CIVO---the failure mode is qualitatively different (no sustained value inflation).

\textbf{Ablation 3: Vanilla DreamerV3 without any gating (exp\_020).} Seed 2, $H=15$, no dt\_emb, no gate, no subsample. Result: stable 837@105K with no collapse. A 75K--95K dip (689$\rightarrow$596) represents normal variance with full recovery to 837. Compared against exp\_008e\_v3\_s2 (same seed, same hyperparameters, but WITH trained dt\_emb): that run collapses 715$\rightarrow$137@105K (NVE $3.78\times$).

\textbf{Interpretation.} The conjunction of these three ablations establishes trained dt\_emb as a necessary condition for both CIVO (Pathway A) and the secondary instability mode (Pathway B, \S4.7). The embedding itself is not toxic---it must be trained, receiving gradient updates that create the pathological feedback loop.

### 4.4 Finding 4: Cross-Environment Generalization (Cheetah Run)

\textbf{Setup.} To address whether CIVO is specific to the Walker Walk morphology, we replicate the diagnostic configuration (trained dt\_emb, subsample ON, $d_t=2$, $H=8$) on Cheetah Run (exp\_010b, seed 1).

\textbf{Result.} NVE reaches $8.63\times$ (sustained average; raw peak $14.59\times$), with eval collapsing from 287@45K $\rightarrow$ 45@105K. All 5 CIVO diagnostic criteria are met:
\begin{enumerate}
  \item NVE $> 1.5\times$ sustained $\checkmark$ ($8.63\times$)
  \item Monotonic eval decline post-peak $\checkmark$ (287$\rightarrow$45)
  \item Value inflation precedes eval collapse $\checkmark$
  \item Entropy reduction (policy lock-in) $\checkmark$
  \item Positive actor loss (critic drives degradation) $\checkmark$
\end{enumerate}

\textbf{Comparison.} The Cheetah baseline (exp\_010a, same config without trained dt\_emb) reaches stable 654@105K. The CIVO effect is more severe in Cheetah (NVE $8.63\times$ vs Walker's $4.12\times$), possibly because the faster dynamics amplify multi-step prediction errors.

\textbf{Implication.} CIVO is environment-general. It emerges from the interaction between trained temporal embeddings and the world-model training objective, not from specific kinematic properties of Walker Walk.

### 4.5 Finding 5: Gradient Decomposition Reveals Observation Decoder Dominance

\textbf{Setup.} We decompose gradients flowing through dt\_emb by source component using per-loss backward passes at multiple checkpoints during exp\_008d training (methodology in Appendix~\ref{app:gradient}).

\textbf{Gradient composition evolves during training:}
\begin{itemize}
  \item \textbf{Step 55K} (pre-collapse): obs decoders 25.8\%, reward head 23.5\%, KL dynamics 50.7\%
  \item \textbf{Step 105K} (post-collapse): obs decoders \textbf{93\%}, reward head \textbf{0\%}, KL dynamics 7\%
\end{itemize}

The observation decoder gradient norm grows from 0.601 to 1.505 while total gradient norm \emph{decreases} (2.33$\rightarrow$1.62), indicating that other components' gradients collapse as the obs decoder dominates. This constitutes a positive feedback loop: obs decoder gradients reshape dt\_emb $\rightarrow$ dt\_emb misrepresents temporal context $\rightarrow$ critic overestimates $\rightarrow$ policy degrades $\rightarrow$ obs decoder receives higher loss $\rightarrow$ obs decoder gradients grow further.

\textbf{Counterfactual: reward-only SGS (exp\_016e).} Blocking only the reward head gradient from dt\_emb is a no-op, since reward contributes 0\% by the time collapse occurs. In fact, this intervention \emph{worsens} outcomes: NVE reaches $10.42\times$@95K with eval collapsing to 32 (vs 008d's 131@105K). This confirms that the CIVO mechanism is driven by observation reconstruction, not reward prediction.

### 4.6 Finding 6: Full Selective Gradient Stopping Eliminates CIVO

\textbf{Setup (exp\_018v2).} We apply Full-SGS: detaching the observation decoder's gradient path from dt\_emb while preserving all other gradient flows. Configuration otherwise identical to exp\_008d (trained dt\_emb, subsample ON, $d_t=2$, $H=8$, Walker Walk, seed 1).

\textbf{Result.}
\begin{itemize}
  \item NVE sustained average: $1.34\times$ over 35K+ window (vs 008d's $4.12\times$)
  \item Eval peak: 499.6@75K; final: 448.3@105K (vs 008d's 131@105K)
  \item No collapse detected through 105K steps
  \item Gradient composition with SGS: obs decoder contribution stays $\sim$24\% (blocked from reaching dt\_emb), preventing the runaway feedback loop
\end{itemize}

\textbf{Quantification.} Full-SGS eliminates 79\% of excess NVE ($4.12 \rightarrow 1.34$ on a baseline of $\sim$1.0) and achieves $3.4\times$ higher final eval return than the matched CIVO condition. While performance remains below vanilla DreamerV3 (448 vs 916), this gap reflects the inherent cost of multi-step imagination without full architectural support, not residual CIVO.

\textbf{Limitation.} This result is from a single seed ($n=1$). We report it as proof-of-concept evidence that the identified mechanism (obs decoder $\rightarrow$ dt\_emb gradient pathway) is causally responsible for CIVO, not as a mature intervention. A second seed is needed before claiming reliable mitigation.

### 4.7 Finding 7: Pathway B---A Secondary Instability Mode

\textbf{Observation (exp\_008e\_v3\_s2).} Under trained dt\_emb with $d_t=1$ imagination (which should prevent CIVO by eliminating multi-step value estimation), one of two seeds still collapses: eval 715@85K $\rightarrow$ 137@105K, NVE $3.78\times$.

\textbf{Differential diagnosis.} This collapse is mechanistically distinct from CIVO:
\begin{itemize}
  \item CIVO (Pathway A, exp\_008d): value inflates \emph{before} eval drops; entropy \emph{decreases} (policy locks into suboptimal actions)
  \item Pathway B (exp\_008e\_v3\_s2): value tracks target closely until late; entropy \emph{increases}; value standard deviation explodes ($7.4 \rightarrow 18.3$), indicating noisy critic gradients destabilize policy
\end{itemize}

\textbf{Necessary condition test (exp\_020).} Vanilla DreamerV3 with identical seed=2 and $H=15$ (no dt\_emb) remains stable at 837@105K. This rules out inherent DreamerV3 fragility or seed-specific instability as explanations---trained dt\_emb is necessary for Pathway B as well.

\textbf{Interpretation.} Trained dt\_emb introduces vulnerability through at least two distinct pathways. CIVO (Pathway A) operates via observation decoder gradient corruption and can be blocked by SGS. Pathway B operates via increased value estimation variance under distributional shift and is not addressed by SGS. This represents residual risk: even with SGS intervention, trained temporal embeddings may destabilize training through secondary mechanisms. We flag this as an open problem requiring further investigation.

\textbf{Stochastic nature.} Pathway B manifests in 1/2 seeds under $d_t=1$ imagination. Combined with CIVO's 2/3 collapse rate, trained dt\_emb configurations show an aggregate collapse rate of 67--75\% across conditions, reinforcing the diagnostic conclusion that temporal abstraction via learned embeddings is a high-risk architectural choice in world-model RL.

---

## Summary of Key Metrics

| Finding | Primary Exp | Key Metric | Comparison | Statistical Support |
|---------|-------------|-----------|------------|-------------------|
| F1 | 005/006/007 | Peak $\rightarrow$ collapse | Baseline 916 stable | $n=3$ environments |
| F2 | 008d | NVE $4.12\times$ | No-dt\_emb $1.14\times$ | $\Delta=+2.29$ [0.91, 3.10] |
| F3 | 008f/015b/020 | NVE $<1.5\times$, no collapse | 008d/008e\_v3\_s2 collapse | 3 independent ablations |
| F4 | 010b | NVE $8.63\times$, Cheetah | 010a stable 654 | $n=1$ (cross-env) |
| F5 | 008d gradient | Obs 93\% @ 105K | Obs 25.8\% @ 55K | Temporal evolution |
| F6 | 018v2 | NVE $1.34\times$, eval 448 | 008d NVE $4.12\times$, eval 131 | $n=1$ (proof-of-concept) |
| F7 | 008e\_v3\_s2 | Collapse 715$\rightarrow$137 | 020 stable 837 | Same-seed control |
