# Related Work — Draft

## \section{Related Work}

\paragraph{Synthetic Contamination and Model Collapse.}
Training on recursively generated data leads to irreversible quality degradation---\emph{model collapse}~\citep{shumailov_2024_model_collapse}.
\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
More critically, \citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, and that larger models can \emph{amplify} rather than mitigate the effect---ruling out data scaling as a remedy.
\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
These results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.

\paragraph{Detection-Based Reweighting and Filtering.}
Given the severity of contamination, a natural response is to detect and remove synthetic content.
DetectGPT~\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\% Prob~\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\% tokens as a reference-free membership signal.
Both produce continuous confidence scores suitable as input to downstream weighting schemes, including ours.
On the mitigation side, \citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards potentially useful borderline samples.
\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.
Hard filtering requires a precision--recall threshold and loses information; soft reweighting avoids this trade-off by assigning continuous weights.

Most directly related to our work, \citet{drayson_2025_detection_collapse} propose the detect-and-reweight formula $w_j = (1{-}q_j)^b$ for collapse prevention, where $q_j$ is the detector's synthetic probability.
We adopt the same weighting formula but differ in several fundamental ways.
\textbf{(i)}~Drayson et al.\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B), making the choice \emph{per-model} and expensive.
Our $b^*$ is derived per-batch from dual constraints ($\alpha_{\mathrm{eff}} \geq \tau$, $\mathrm{ESS} \geq n_{\min}$) at zero validation cost.
\textbf{(ii)}~Their SIR resampling discretizes the weight distribution into a resampled subset; we apply direct loss reweighting with continuous gradients, preserving the full batch.
\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\,=\,0.986) on WikiText-2 (${\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\,=\,0.939) suffices at FineWeb scale (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.

\paragraph{Data Mixing and Instance-Level Reweighting.}
A parallel line of work optimizes data composition without targeting synthetic contamination.
At the \emph{domain} level, DoReMi~\citep{xie_2023_doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\citep{xie_2023_dsir} performs importance resampling with $n$-gram features, and \citet{ye_2025_data_mixing_laws} discover predictable functional forms relating mixing ratios to performance.
AIOLI~\citep{chen_2025_aioli} unifies these into an online adaptive framework.
These methods operate at the domain level and do not address instance-level contamination within a domain.
At the \emph{instance} level, SoftDedup~\citep{he_2024_softdedup} downweights high-frequency samples via $n$-gram commonness, and \citet{sow_2025_dynamic_reweighting} derive sample weights from per-sample loss with convergence guarantees.
Our reweighting differs from all of these in being driven by \emph{provenance}---detector scores estimating human vs.\ synthetic origin---rather than loss, frequency, or domain membership.

\paragraph{Theoretical Foundations.}
\citet{he_2025_golden_ratio} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal ($w^* \approx 0.62$) optimal when both sources are equally sized.
Their result requires the contamination ratio $k$, which is unavailable in web-scale settings; we use it as an oracle baseline.
\citet{wang_2026_survive_contamination} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\alpha_{\mathrm{eff}}(b) \geq \tau$ guarantees a convergence-rate lower bound.
We operationalize this insight without the known-proportion assumption by estimating $\alpha_{\mathrm{eff}}$ from batch-level detector statistics online.
For the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling diagnostics of \citet{vehtari_2024_psis}.
\citet{kimura_2024_iw_survey} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as covariate-shift correction where the covariate is synthetic-origin probability.
To our knowledge, no existing method provides principled, per-batch exponent selection for contamination-aware reweighting without relying on a held-out validation set or known contamination proportions.
