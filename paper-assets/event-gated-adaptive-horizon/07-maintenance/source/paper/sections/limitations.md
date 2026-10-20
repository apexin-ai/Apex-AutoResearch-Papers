% Limitations — Draft v1
% Target: CoRL 2026
% Status: Draft, pending Director review

\section{Limitations}
\label{sec:limitations}

We scope our claims to the specific architecture and experimental conditions studied. Several limitations bear on the generalizability and completeness of our findings.

\paragraph{Two locomotion environments.}
Our diagnostic analysis centers on Walker Walk from the DeepMind Control Suite, with Cheetah Run providing cross-environment validation. Both are locomotion tasks with proprioceptive observations and dense rewards. While Cheetah Run confirms that CIVO onset generalizes (10/10 trained-$e_{\Delta t}$ runs across both environments), the environments share structural similarities. Whether the identified mechanisms transfer to qualitatively different domains (e.g., manipulation tasks with sparse rewards, or pixel-based observations) remains untested.

\paragraph{Limited seed count.}
Key experimental conditions are evaluated with two to four seeds per environment. CIVO onset is observed in 10/10 trained-$e_{\Delta t}$ runs across Walker and Cheetah (Fisher exact $p < 0.0001$ vs.\ 0/8 controls), providing strong evidence for onset reliability. However, stochastic collapse is inherently difficult to characterize with few seeds: Walker shows 6/8 sustained collapse while both Cheetah runs self-correct, but the true collapse probability per environment remains uncertain given our sample size. We report all seeds transparently rather than selecting favorable outcomes.

\paragraph{Replay sampling seed.}
In experiments prior to the final round, the replay buffer's episode sampling routine used a fixed seed rather than the per-run seed; model weight initialization and all other stochastic components received correct per-run seeds. Because the shared replay ordering is a common-mode factor affecting experimental and control conditions identically, between-group contrasts remain unbiased, though within-group variance may be slightly underestimated. The final seed (seed 3, exp\_008d) uses the corrected, fully independent implementation.

\paragraph{NVE threshold calibrated and evaluated on the same data.}
The $\text{nve}{>}1.5\text{x}$ diagnostic threshold was identified from the same experiments used to evaluate its separating power. No held-out validation set was used. The threshold achieves 4/4 separation for the trained-vs-removed $\Delta t$-embedding comparison, but the overall 9/10 classification accuracy across all 10 experiments yields a 95\% Clopper--Pearson confidence interval of $[55.5\%,\, 99.7\%]$; the supplementary $\hat{r}_k > 3.9$ threshold achieves 10/10 with CI $[69.2\%,\, 100\%]$. Cheetah Run provides partial independent validation (both trained-$e_{\Delta t}$ runs exceed the threshold), but a broader set of environments is needed to confirm the threshold's reliability as a general diagnostic.

\paragraph{Single base algorithm.}
All experiments use DreamerV3 with its RSSM world model. The identified causal chain---trained $\Delta t$-embedding $\to$ conditioning-induced value overestimation $\to$ collapse---is mechanistically tied to the RSSM's latent-dynamics architecture and the imagination-based actor-critic training loop. Whether analogous failure modes arise in other world-model architectures (e.g., transformer-based dynamics models or discrete latent spaces) remains untested. Notably, TAWM \citep{nhu2025tawm} demonstrates successful $\Delta t$-conditioning in a model-predictive control setting, suggesting the vulnerability may be specific to imagination-based training rather than $\Delta t$-conditioning per se.

\paragraph{No formal causal inference framework.}
Our analysis is interventional---we manipulate experimental factors and observe outcomes---but does not employ a formal causal inference framework (e.g., structural causal models or do-calculus). We use the term ``causal'' loosely to describe controlled ablations that isolate necessary conditions. A more rigorous treatment would strengthen the mechanistic claims.

\paragraph{Pathway B mechanism not fully characterized.}
Experiment 008e\_v3 seed 2 collapsed via a dynamically distinct pathway: eval-driven destabilization with increasing policy entropy, rather than the value-driven exploitation with decreasing entropy seen in classic CIVO (008d seed 1). While we observe this divergence and rule out seed-specific fragility (the matched baseline seed remains stable), the root cause of Pathway B remains an open question. Characterizing this second vulnerability pathway is necessary for developing robust mitigations.

\paragraph{Full stop-gradient results pending.}
Gradient decomposition reveals that 93\% of $\Delta t$-embedding gradients originate from observation decoders, with 0\% from the reward head. The full stop-gradient experiment (018), which blocks the dominant observation-decoder gradient pathway, had not completed at the time of writing. This leaves open whether gradient-level intervention at the correct source suffices to prevent CIVO, or whether the vulnerability persists through the remaining 7\% KL-dynamics pathway.
