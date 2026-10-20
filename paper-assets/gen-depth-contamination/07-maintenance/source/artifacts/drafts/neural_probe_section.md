# §4.x Neural Probe Analysis

> **Data source:** `artifacts/exp015_neural_probe_results.json` (Qwen-cont only).
> **Status:** Qwen-cont complete; Pythia and OLMo pending rerun.

---

## §4.x.1 Motivation

The preceding experiments establish $K^*_{\text{emp}} = 2$ using 15-dimensional hand-crafted statistical features.
A natural question arises: does this boundary reflect an intrinsic limit of the recursive generation process, or is it an artifact of information loss in the feature projection from high-dimensional text to a 15D summary?
The DPI analysis in Section~\ref{sec:formulation} guarantees the existence of a finite $K^*_{\text{theory}}$, and Section~\ref{sec:kstar_boundary} reports $K^*_{\text{emp}} \leq K^*_{\text{theory}}$ by construction---but it remains unknown how tight this bound is.

We address this gap with a \emph{neural probe} that bypasses hand-crafted feature engineering entirely.
By training a lightweight classifier on frozen LLM hidden states---which preserve a much richer representation of the input text than any fixed-dimensional statistical summary---we obtain a direct test of the "operational lower bound" hypothesis articulated in Section~\ref{sec:kstar_operational}: if $K^*_{\text{emp}} = 2$ is driven by feature projection loss rather than the data itself, a higher-capacity representation should push $K^*$ upward.

## §4.x.2 Method

We extract representations from a frozen Qwen2.5-1.5B-Instruct model.
Each document is tokenized and passed through the full transformer stack; we take the last hidden layer and apply average pooling across the sequence length to obtain a 1536-dimensional document embedding.
This representation preserves the model's full contextual understanding of the input, in contrast to the 15D features which project this information onto a small set of pre-specified statistical moments.

The probe is a three-layer MLP classifier ($1536 \to 512 \to 256 \to 6$) with ReLU activations and dropout, trained to predict depth class (generations 0--5).
We use the same 5-fold GroupKFold cross-validation protocol as the OBD-LightGBM experiments, grouping by seed document to prevent same-source leakage across folds.
Training uses early stopping on validation loss to prevent overfitting to the high-dimensional input.
Crucially, the neural probe operates on the same Qwen-continuation dataset and train/test splits as the corresponding LightGBM baseline, ensuring a fair comparison that isolates the effect of representation capacity.

## §4.x.3 Results

Table~\ref{tab:neural_probe} compares pairwise $\text{AUC}$ for adjacent depth pairs between the neural probe and OBD-LightGBM on the Qwen-continuation dataset.

### Table: Neural Probe vs. OBD-LightGBM Pairwise AUC (Qwen-cont)

```
\begin{table}[t]
\centering
\small
\caption{Pairwise $\auc$ for adjacent depth pairs on the Qwen-continuation dataset:
neural probe (frozen Qwen2.5-1.5B hidden states $\to$ MLP) vs.\ OBD-LightGBM (15D features).
Neural probe fold statistics report mean $\pm$ std over 5-fold GroupKFold CV.
The $\theta = 0.60$ threshold determines the $K^*$ boundary:
bold entries exceed $\theta$; the critical 2v3 pair flips from FAIL (LightGBM) to PASS (neural probe).
LightGBM values are re-evaluated on the same CV splits as the neural probe; the 1v2 value (0.6114) differs from the full-dataset estimate in Section~\ref{sec:kstar_boundary} (0.6112) by 0.0002 due to fold randomness.}
\label{tab:neural_probe}
\begin{tabular}{lccc}
\toprule
Depth pair & Neural probe & LightGBM & $\Delta$ \\
\midrule
0v1 & $\mathbf{0.9873}$ \scriptsize{$\pm 0.0021$} & $\mathbf{0.9972}$ & $-0.0099$ \\
1v2 & $\mathbf{0.6983}$ \scriptsize{$\pm 0.0073$} & $\mathbf{0.6114}$ & $+0.0869$ \\
2v3 & $\mathbf{0.6195}$ \scriptsize{$\pm 0.0094$} & $0.5609$ & $+0.0586$ \\
3v4 & $0.5930$ \scriptsize{$\pm 0.0051$} & $0.5408$ & $+0.0522$ \\
4v5 & $0.5747$ \scriptsize{$\pm 0.0072$} & $0.5139$ & $+0.0608$ \\
\midrule
$K^*$ ($\theta = 0.60$) & \textbf{3} & 2 & $+1$ \\
% TODO: 6-class accuracy row removed — neural probe 0.4335 is 5-fold CV,
% but LightGBM 0.3875 is from exp-013 (hold-out split, not matched).
% Re-add after exp-015 rerun computes matched LightGBM accuracy on same CV folds.
\bottomrule
\end{tabular}
\end{table}
```

The neural probe achieves higher $\text{AUC}$ than LightGBM at every depth pair except 0v1, with the advantage concentrated at the critical discrimination boundaries.
The 2v3 pair is the decisive flip: the neural probe yields $\text{AUC}_{2,3} = 0.6195 \pm 0.0094$, exceeding $\theta = 0.60$ across all five folds (fold range: 0.6052--0.6323), while LightGBM scores $0.5609$, well below the threshold.
This single boundary crossing shifts $K^*$ from 2 to 3.
At 3v4, the neural probe scores $0.5930 \pm 0.0051$---below $\theta$ but notably higher than LightGBM's $0.5408$---indicating that residual depth signal persists at generation~3 even if it falls short of the operational threshold.

The 1v2 improvement is also substantial ($+8.7$ percentage points), lifting the margin above $\theta$ from 0.0114 (LightGBM) to 0.0983 (neural probe).
This wider margin suggests that LightGBM's narrow pass at 1v2 (Section~\ref{sec:kstar_boundary}, CI lower bound = 0.6015) reflects genuine information loss in the 15D projection, not an intrinsic weakness of the depth signal.

[PLACEHOLDER: Pythia and OLMo results pending rerun]

```
% Placeholder rows for Pythia-1.4B and OLMo-1B neural probe results.
% \midrule
% \multicolumn{4}{l}{\textit{Pythia-1.4B (continuation)}} \\
% 0v1 & --- & $\mathbf{0.9932}$ & --- \\
% 1v2 & --- & $\mathbf{0.6539}$ & --- \\
% 2v3 & --- & $0.5514$ & --- \\
% $K^*$ & --- & 2 & --- \\
% \midrule
% \multicolumn{4}{l}{\textit{OLMo-1B (continuation)}} \\
% 0v1 & --- & $\mathbf{0.9970}$ & --- \\
% 1v2 & --- & $\mathbf{0.6145}$ & --- \\
% 2v3 & --- & $0.5496$ & --- \\
% $K^*$ & --- & 2 & --- \\
```

Results for Pythia-1.4B and OLMo-1B will be added upon completion of the full three-model rerun with bootstrap CI and permutation tests.

## §4.x.4 Interpretation

The neural probe result $K^*_{\text{neural}} = 3$ provides direct evidence for the "operational lower bound" characterization in Section~\ref{sec:kstar_operational}: the 1536-dimensional frozen representation retains sufficient signal to resolve one additional generational boundary that the 15D summary cannot.
This provides evidence that $K^*_{\text{emp}} = 2$ under 15D features reflects, at least in part, information loss in the feature projection rather than an intrinsic data limit, and establishes $K^*_{\text{theory}} \geq 3$. However, as the probe uses the same model that generated the text, this result must be validated with cross-model embeddings to disentangle representation capacity from self-familiarity.

However, the gain is modest: a shift from 15-dimensional statistical features to 1536-dimensional learned representations shifts $K^*$ by only one level.
The neural probe's 3v4 AUC ($0.5930$) falls short of $\theta = 0.60$ by only 0.007, and 4v5 ($0.5747$) decays further toward chance.
Even with access to the generator's own internal representations, the classifier cannot reliably distinguish generations beyond the third.
This is consistent with the lossy channel narrative established in Section~\ref{sec:formulation}: while the 15D features lose discriminative information prematurely, the underlying generative process itself destroys most depth-distinguishing structure within 2--3 recursive steps.
The gap between $K^*_{\text{neural}} = 3$ and $K^*_{\text{15D}} = 2$ quantifies the cost of hand-crafted feature engineering; the proximity of $K^*_{\text{neural}}$ to $K^*_{\text{15D}}$ quantifies the speed of information destruction in the recursive channel.

Two caveats qualify these findings.
First, the neural probe results are currently limited to a single model family (Qwen-continuation); cross-model generality awaits the Pythia and OLMo reruns.
Second, the probe uses the \emph{same} frozen model that generated the text, which may inflate discriminability via self-recognition artifacts.
A cross-model probe (e.g., using OLMo hidden states to classify Qwen-generated text) would disentangle intrinsic depth signal from generator self-familiarity, paralleling the cross-model transfer analysis in Section~\ref{sec:transfer}.

---

**Notation conventions** (consistent with `method.tex`):
- $K^*_{\text{emp}}$: `\Kempirical`
- $K^*_{\text{theory}}$: `\Ktheory`
- $K^*$: `\Kstar`
- AUC: `\auc`
- $\theta = 0.60$: operational threshold
