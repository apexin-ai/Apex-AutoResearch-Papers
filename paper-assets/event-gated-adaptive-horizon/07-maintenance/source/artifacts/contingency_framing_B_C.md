# Contingency Framing: Scenarios B and C

Prepared 2026-05-20. For use after 5/22 go/no-go based on TCN/RAVE results.
Scene A (current framing, pure diagnostic) remains unchanged in .tex files.

---

## Scenario B: TCN σ=0.2 multi-seed success, Cheetah fails (~35% probability)

**Pitch**: Systematic diagnosis → partial solution, environment-constrained.
C1-C7 as primary contributions; C8 as "promising but limited."

### Abstract (Scenario B)

Temporal abstraction via variable-rate imagination promises to extend the planning horizon of world-model reinforcement learning, yet transferring $\Delta t$-conditioning from model-predictive control to imagination-based actor-critic training remains unsolved. Through factorial diagnostics on two continuous-control environments, we identify a previously unreported failure mode---\emph{conditioning-induced value overestimation} (CIVO)---triggered by the combination of trained temporal embedding and multi-rate data exposure, and universally degrading performance across all tested seeds ($n{=}6$, two environments). We trace CIVO's mechanism to a $2.78\times$ reward prediction gap that the critic internalizes, and show that gradient-level interventions fail across all three tested variants (reward-only 0/2, full-pathway 0/3, obs-decoder 1/6), establishing that the vulnerability resides in forward-pass representations rather than backward-pass gradients. Guided by this analysis, we propose Temporal Conditioning Noise (TCN), which injects calibrated noise into the temporal embedding during imagination. TCN eliminates CIVO on Walker Walk (NVE~$<1.5\times$ in TBD/TBD seeds) but fails to generalize to Cheetah Run, where CIVO severity is 10--25$\times$ higher. The environment-dependent outcome reveals that CIVO's forward-pass mechanism scales with reward-prediction sensitivity, requiring environment-aware calibration that fixed-noise approaches cannot provide. A lightweight online detector (100\% sensitivity, 5/5) enables monitoring in both protected and unprotected regimes.

### Intro paragraph 1 (Scenario B)

TAWM shows that $\Delta t$-conditioning yields consistent gains within TD-MPC2's MPC framework. Can the same conditioning bring temporal abstraction to imagination-based actor-critic methods? We find that it introduces a pathological failure mode---conditioning-induced value overestimation (CIVO)---that no gradient-level intervention eliminates. Guided by this diagnosis, we propose a forward-pass intervention (Temporal Conditioning Noise) that succeeds on Walker Walk but fails on Cheetah Run, where CIVO severity is an order of magnitude higher. The partial success delineates a boundary condition: CIVO mitigation requires environment-aware calibration that scales with the reward prediction sensitivity gap between temporal scales.

### Key narrative adjustments for B
- C1-C7 remain primary (~60% of paper); C8 contributes ~20%
- New insight: cross-environment severity gap (Walker 2-6× vs Cheetah 8-108×) as structural explanation for TCN's partial success
- Intervention hierarchy table: gradient-level (all fail) → output-level (RAVE TBD) → representation-level (TCN partial)
- σ dose-response curve as evidence that noise magnitude matters
- Limitations: single-environment success, calibration not automated

---

## Scenario C: TCN σ=0.2 only 1/3 seeds succeed (~25% probability)

**Pitch**: Thorough problem characterization + intervention impossibility landscape.
From "problem + solution" to "why it's fundamentally hard to fix."

### Abstract (Scenario C)

Temporal abstraction via variable-rate imagination promises to extend planning horizons in world-model reinforcement learning, but $\Delta t$-conditioning that succeeds under model-predictive control fails catastrophically under imagination-based actor-critic training. We present a systematic investigation of this failure through factorial diagnostics on two continuous-control environments, identifying \emph{conditioning-induced value overestimation} (CIVO) as the underlying pathology: trained temporal embedding combined with multi-rate data exposure enables a reward prediction gap that the critic exploits, universally degrading performance ($n{=}6$ seeds, two environments). We then construct an \emph{intervention impossibility landscape} across three levels: gradient-level stopping (reward-only 0/2, full-pathway 0/3, obs-decoder 1/6) fails because gradient magnitude is decoupled from causal importance; representation-level noise (TCN, TBD/TBD seeds) fails because forward-pass damage operates below the noise threshold; output-level clamping (RAVE, TBD/TBD) fails because value truncation does not address the upstream bias. The systematic failure across all intervention levels establishes that CIVO is not an incidental bug but an architectural incompatibility: imagination-based bootstrapping amplifies any temporal-scale prediction asymmetry into a self-reinforcing value bias. A lightweight detector (100\% sensitivity) provides the practical path forward---monitoring rather than preventing.

### Intro paragraph 1 (Scenario C)

TAWM shows that $\Delta t$-conditioning yields consistent gains in MPC-based world-model RL. Can the same conditioning benefit imagination-based actor-critic methods? We find that it introduces conditioning-induced value overestimation (CIVO), a self-reinforcing pathology that resists intervention at every level we test. Gradient stopping fails because gradient magnitude is decoupled from causal importance; representation-level noise fails because the forward-pass vulnerability operates below perturbation thresholds; output-level value clamping fails because it addresses symptoms rather than causes. The systematic failure across three intervention levels establishes CIVO as an architectural incompatibility between temporal conditioning and imagination-based bootstrapping, not a fixable implementation detail. We provide the first comprehensive characterization of this failure mode and a practical detector for deployment monitoring.

### Key narrative adjustments for C
- C1-C7 are the entire contribution; C8 reframed as "intervention impossibility evidence"
- Three-level intervention hierarchy as a structuring device (gradient / representation / output)
- Each level fails for a different reason → deeper mechanistic understanding
- Positioned as "negative results that save the community years of dead-end work"
- Practical contribution shifts to detector + design guidelines (avoid flat dt-conditioning in imagination-based AC)
- Limitations: cannot prove fundamental impossibility, only exhaustive empirical failure
