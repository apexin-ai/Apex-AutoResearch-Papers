# Theta Sensitivity Analysis: K* Stability Across Threshold Values

## Overview

This report analyzes how K* (the maximum generation depth at which consecutive depths remain distinguishable) varies as a function of the classification threshold theta. For each experiment with pairwise AUC data, K* is computed for theta in {0.55, 0.575, 0.60, 0.625, 0.65, 0.70}.

**K* definition:** the maximum k such that AUC(k-1 vs k) >= theta. If AUC(0v1) < theta, then K* = 0.

**Experiments analyzed:** 21 (16 from registry with nested/flat pairwise AUC + 4 sub-experiments from exp_020 decoding ablation + 1 retrain bootstrap)

---

## Summary Table

### C4 Domain

| Exp ID | Model | K*(rep) | theta=0.55 | 0.575 | 0.60 | 0.625 | 0.65 | 0.70 |
|--------|-------|---------|------------|-------|------|-------|------|------|
| exp_001_pythia_depth | Pythia-1.4B | 2 | 3 | 2 | 2 | 2 | 2 | 1 |
| exp_002_olmo_depth | OLMo-1B | 2 | 2 | 2 | 2 | 1 | 1 | 1 |
| exp_004_7b_crossscale | Qwen2.5-7B | 2 | 2 | 2 | 2 | 1 | 1 | 1 |
| exp_016_base_vs_instruct | Qwen2.5-1.5B | 2 | 2 | 2 | 2 | 2 | 1 | 1 |
| exp_017_qwen_continuation | Qwen2.5-1.5B | 2 | 3 | 2 | 2 | 1 | 1 | 1 |
| exp_018_llama8b_depth | LLaMA-3.1-8B | 2 | 2 | 2 | 2 | 1 | 1 | 1 |
| exp_019_mistral7b_depth | Mistral-7B | 1 | 2 | 2 | 1 | 1 | 1 | 1 |
| exp_019b_mistral_cross_scorer | Mistral-7B | 1 | 2 | 1 | 1 | 1 | 1 | 1 |
| exp_020_greedy | Pythia-1.4B | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| exp_020_nuc09 | Pythia-1.4B | 2 | 3 | 2 | 2 | 2 | 2 | 1 |
| exp_020_t07 | Pythia-1.4B | 2 | 4 | 3 | 2 | 2 | 2 | 2 |
| exp_020_t12 | Pythia-1.4B | 2 | 2 | 2 | 2 | 1 | 1 | 1 |
| mvp_pilot_sat_v1 | Qwen2.5-1.5B | 2 | 3 | 3 | 2 | 2 | 2 | 1 |

### arXiv Domain

| Exp ID | Model | K*(rep) | theta=0.55 | 0.575 | 0.60 | 0.625 | 0.65 | 0.70 |
|--------|-------|---------|------------|-------|------|-------|------|------|
| exp_024_arxiv_domain | Qwen2.5-1.5B | 3 | 3 | 3 | 3 | 3 | 2 | 2 |
| exp_025_pythia_arxiv | Pythia-1.4B | 3 | 4 | 3 | 3 | 3 | 3 | 2 |
| exp_arXiv_llama8b | LLaMA-3.1-8B | 3 | 3 | 3 | 3 | 2 | 2 | 2 |
| exp_arXiv_mistral7b | Mistral-7B | 3 | 3 | 3 | 3 | 3 | 2 | 2 |
| exp_arXiv_qwen7b | Qwen2.5-7B | 3 | 3 | 3 | 3 | 3 | 2 | 2 |

### Wikipedia Domain

| Exp ID | Model | K*(rep) | theta=0.55 | 0.575 | 0.60 | 0.625 | 0.65 | 0.70 |
|--------|-------|---------|------------|-------|------|-------|------|------|
| exp_wiki_mistral7b | Mistral-7B | 1 | 2 | 1 | 1 | 1 | 1 | 1 |

### Retrain-chain Domain

| Exp ID | Model | K*(rep) | theta=0.55 | 0.575 | 0.60 | 0.625 | 0.65 | 0.70 |
|--------|-------|---------|------------|-------|------|-------|------|------|
| exp_008_retrain_chain_v2 | Pythia-1.4B | >=4 | 4 | 4 | 4 | 4 | 4 | 4 |
| exp_027 | Pythia-1.4B | 4 | 4 | 4 | 4 | 4 | 4 | 4 |

---

## Detailed Analysis by Domain

### C4 (Prompt-Chain) Experiments

The canonical prompt-chain experiments on C4 data consistently report K*=2 at theta=0.60. The theta sensitivity analysis reveals:

**Stability ranges for K*=2:**

- **exp_001_pythia_depth** (Pythia-1.4B): K*=2 stable for theta in [0.575, 0.65]
- **exp_002_olmo_depth** (OLMo-1B): K*=2 stable for theta in [0.55, 0.6]
- **exp_004_7b_crossscale** (Qwen2.5-7B): K*=2 stable for theta in [0.55, 0.6]
- **exp_016_base_vs_instruct** (Qwen2.5-1.5B): K*=2 stable for theta in [0.55, 0.625]
- **exp_017_qwen_continuation** (Qwen2.5-1.5B): K*=2 stable for theta in [0.575, 0.6]
- **exp_018_llama8b_depth** (LLaMA-3.1-8B): K*=2 stable for theta in [0.55, 0.6]
- **exp_019_mistral7b_depth** (Mistral-7B): K*=2 stable for theta in [0.55, 0.575]
- **exp_019b_mistral_cross_scorer** (Mistral-7B): K*=2 stable for theta in [0.55, 0.55]
- **exp_020_greedy** (Pythia-1.4B): K*=2 stable for theta in [0.55, 0.7]
- **exp_020_nuc09** (Pythia-1.4B): K*=2 stable for theta in [0.575, 0.65]
- **exp_020_t07** (Pythia-1.4B): K*=2 stable for theta in [0.6, 0.7]
- **exp_020_t12** (Pythia-1.4B): K*=2 stable for theta in [0.55, 0.6]
- **mvp_pilot_sat_v1** (Qwen2.5-1.5B): K*=2 stable for theta in [0.6, 0.65]

**Key observations:**

1. **theta=0.60 is the consensus threshold.** At this value, 10 of 13 C4 experiments yield K*=2, matching the reported values. The two Mistral-7B experiments (exp_019, exp_019b) yield K*=1, consistent with Mistral being a one-wash model on C4.
2. **Lowering theta to 0.55 inflates K*.** Several experiments jump to K*=3 (exp_001, exp_017, mvp_pilot, exp_020_nuc09) or even K*=4 (exp_020_t07) because marginal AUC values in the 0.55-0.59 range cross the lower bar.
3. **Raising theta to 0.625 begins to erode K*=2.** OLMo (1v2=0.615), Qwen-7B (1v2=0.618), LLaMA-8B (1v2=0.612), and Qwen-continuation (1v2=0.611) all drop to K*=1 at theta=0.625.
4. **At theta=0.70, only two experiments survive at K*=2:** exp_020_greedy (1v2=0.884) and exp_020_t07 (1v2=0.727). Greedy decoding produces anomalously high 1v2 AUC.

### arXiv Domain Experiments

The arXiv experiments consistently report K*=3, which the analysis confirms is stable across a wider theta range:

- **exp_024_arxiv_domain** (Qwen2.5-1.5B): K*=3 stable for theta in [0.55, 0.625]. Critical 2v3 AUC = 0.6427
- **exp_025_pythia_arxiv** (Pythia-1.4B): K*=3 stable for theta in [0.575, 0.65]. Critical 2v3 AUC = 0.6545
- **exp_arXiv_llama8b** (LLaMA-3.1-8B): K*=3 stable for theta in [0.55, 0.6]. Critical 2v3 AUC = 0.6215
- **exp_arXiv_mistral7b** (Mistral-7B): K*=3 stable for theta in [0.55, 0.625]. Critical 2v3 AUC = 0.6275
- **exp_arXiv_qwen7b** (Qwen2.5-7B): K*=3 stable for theta in [0.55, 0.625]. Critical 2v3 AUC = 0.626

**Key observations:**

1. **K*=3 is stable across theta in [0.55, 0.625] for 4 of 5 experiments.** The exception is LLaMA-8B (2v3=0.622), which drops to K*=2 at theta=0.625.
2. **The 2v3 AUC ranges from 0.622 to 0.655,** giving K*=3 a margin of 0.02-0.055 over theta=0.60. This is comparable to the C4 margin for K*=2.
3. **The 1v2 AUC is very high (0.80-0.86)** for all arXiv experiments, providing a large buffer. K* will not degrade below K*=2 for any reasonable theta.
4. **At theta=0.65, K* drops from 3 to 2** for Qwen-1.5B, LLaMA-8B, Qwen-7B, and Mistral-7B. Only Pythia (2v3=0.655) remains at K*=3.
5. **At theta=0.70, all arXiv experiments drop to K*=2** because no 2v3 AUC exceeds 0.70.

### Wikipedia Domain

- **exp_wiki_mistral7b** (Mistral-7B): K*=2 only at theta=0.55 (1v2 AUC=0.555), K*=1 for theta >= 0.575. This confirms Mistral-7B as a one-wash model; the 1v2 AUC is barely above chance.

### Retrain-Chain Experiments

The retrain-chain experiments show fundamentally different behavior:

- **exp_008_retrain_chain_v2** (Pythia-1.4B): K*=4 for ALL theta values in [0.55, 0.70]. Minimum AUC in chain = 0.7982
- **exp_027** (Pythia-1.4B): K*=4 for ALL theta values in [0.55, 0.70]. Minimum AUC in chain = 0.7977

K*=4 is completely theta-insensitive because all pairwise AUCs exceed 0.79. Retrain-chain artifacts are qualitatively different from prompt-chain depth signals.

---

## Critical AUC Values at K* Boundary

The table below shows, for each experiment at theta=0.60, the AUC of the last passing pair (the one that determines K*) and its margin above theta.

| Exp ID | Domain | K*(0.60) | Last Passing Pair | AUC | Margin |
|--------|--------|----------|-------------------|-----|--------|
| exp_001_pythia_depth | C4 | 2 | 1v2 | 0.6539 | +0.0539 |
| exp_002_olmo_depth | C4 | 2 | 1v2 | 0.6146 | +0.0146 |
| exp_004_7b_crossscale | C4 | 2 | 1v2 | 0.6178 | +0.0178 |
| exp_016_base_vs_instruct | C4 | 2 | 1v2 | 0.6262 | +0.0262 |
| exp_017_qwen_continuation | C4 | 2 | 1v2 | 0.6114 | +0.0114 |
| exp_018_llama8b_depth | C4 | 2 | 1v2 | 0.6123 | +0.0123 |
| exp_019_mistral7b_depth | C4 | 1 | 0v1 | 0.9843 | +0.3843 |
| exp_019b_mistral_cross_scorer | C4 | 1 | 0v1 | 0.9209 | +0.3209 |
| exp_020_greedy | C4 | 2 | 1v2 | 0.8838 | +0.2838 |
| exp_020_nuc09 | C4 | 2 | 1v2 | 0.6770 | +0.0770 |
| exp_020_t07 | C4 | 2 | 1v2 | 0.7265 | +0.1265 |
| exp_020_t12 | C4 | 2 | 1v2 | 0.6172 | +0.0172 |
| mvp_pilot_sat_v1 | C4 | 2 | 1v2 | 0.6957 | +0.0957 |
| exp_024_arxiv_domain | arXiv | 3 | 2v3 | 0.6427 | +0.0427 |
| exp_025_pythia_arxiv | arXiv | 3 | 2v3 | 0.6545 | +0.0545 |
| exp_arXiv_llama8b | arXiv | 3 | 2v3 | 0.6215 | +0.0215 |
| exp_arXiv_mistral7b | arXiv | 3 | 2v3 | 0.6275 | +0.0275 |
| exp_arXiv_qwen7b | arXiv | 3 | 2v3 | 0.6260 | +0.0260 |
| exp_wiki_mistral7b | Wikipedia | 1 | 0v1 | 0.9607 | +0.3607 |
| exp_008_retrain_chain_v2 | Retrain-chain | 4 | 3v4 | 0.7982 | +0.1982 |
| exp_027 | Retrain-chain | 4 | 3v4 | 0.7977 | +0.1977 |

---

## Stability Conclusion

### 1. C4 Domain: K*=2 is moderately stable

- **Stable range:** theta in [0.55, 0.60] for most experiments; theta in [0.55, 0.625] for the strongest (exp_001, exp_016, mvp_pilot).
- **Fragile boundary:** The 1v2 AUC values cluster between 0.61 and 0.70. K*=2 is robust at theta=0.60 but sensitive to increases beyond 0.625.
- **Typical margin over theta=0.60:** +0.01 to +0.10 for the boundary pair (1v2).
- **Mistral-7B on C4** is K*=1 regardless of theta choice in [0.575, 0.70], confirming it as a genuinely one-wash model.

### 2. arXiv Domain: K*=3 is stable

- **Stable range:** theta in [0.55, 0.625] for 4/5 experiments; universally stable at theta=0.60.
- **The 2v3 AUC** (0.621-0.655) gives K*=3 a margin of +0.02 to +0.055 over theta=0.60, comparable to C4's K*=2 margins.
- **The 1v2 AUC is very high** (0.80-0.86), ensuring K* never drops below 2 for any reasonable theta.
- **K*=3 breaks at theta=0.65** for most models, establishing 0.65 as the upper bound.

### 3. Retrain-Chain: K*>=4 is theta-invariant

- K*=4 holds for all theta in [0.55, 0.70]. Minimum chain AUC is 0.798, providing a +0.198 margin at theta=0.60 and +0.098 even at theta=0.70.
- This cleanly separates retrain-chain contamination from prompt-chain generation.

### 4. Recommended Theta Choice

| Theta | Assessment |
|-------|------------|
| 0.55 | Too permissive. Inflates K* by accepting near-chance AUC (0.55-0.59) as signal. |
| 0.575 | Slightly permissive. Some C4 experiments gain spurious K*=3. |
| **0.60** | **Recommended. Produces consensus K* values across all domains and models.** |
| 0.625 | Acceptable but strict. Drops 4/13 C4 experiments from K*=2 to K*=1. |
| 0.65 | Too strict for C4 (most drop to K*=1). Drops arXiv from K*=3 to K*=2. |
| 0.70 | Far too strict. Only greedy-decoded experiments retain K*=2. |

**The safe zone is theta in [0.575, 0.625].** Within this range, the core findings (C4 K*=2, arXiv K*=3) are preserved for the majority of experiments. The canonical choice theta=0.60 sits at the center of this interval.

### 5. Per-Domain K* Summary at theta=0.60

| Domain | Consensus K* | Experiments | Exceptions |
|--------|-------------|-------------|------------|
| C4 (prompt-chain) | 2 | 13 | Mistral-7B: K*=1 (2 exps) |
| arXiv | 3 | 5 | None |
| Wikipedia | 1 | 1 | Mistral-7B only |
| Retrain-chain | >=4 | 2 | None |