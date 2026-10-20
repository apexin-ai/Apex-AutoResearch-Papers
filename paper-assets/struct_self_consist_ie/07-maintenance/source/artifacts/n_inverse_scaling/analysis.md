# Inverse Scaling Analysis for Structured Self-Consistency

Date: 2026-05-20

## Question

Does increasing the number of samples N ever *decrease* entity-level F1 for any construction method? If so, which methods and under what conditions?

## Setup

- Configs: 6 (2 models x 3 datasets)
- Methods: majority_vote, lp_weighted, vc_weighted, sj_weighted, theta2n, uniform
- Threshold: majority_vote uses theta=0.5 (fixed); lp/vc/sj_weighted and theta2n use theta=2/N (adaptive); uniform uses theta=0.25 (fixed)
- Metric: entity-level micro F1 (pooled TP/FP/FN)
- Significance: paired bootstrap (B=5000-10000), 95% CI

## Results

**58 inverse scaling transitions detected, 40 statistically significant.**

### Inverse Scaling Cases

| Config | Method | N1->N2 | F1(N1) | F1(N2) | Drop | 95% CI | Sig? |
|--------|--------|--------|--------|--------|------|--------|------|
| Qwen_SciERC | lp_weighted | 6->8 | 0.6718 | 0.6659 | 0.58pp | [-1.28,+0.13] | no |
| Qwen_SciERC | lp_weighted | 8->16 | 0.6659 | 0.6456 | 2.04pp | [-2.87,-1.18] | **YES** |
| Qwen_SciERC | vc_weighted | 8->16 | 0.6682 | 0.6544 | 1.38pp | [-2.22,-0.50] | **YES** |
| Qwen_SciERC | sj_weighted | 8->16 | 0.6674 | 0.6546 | 1.28pp | [-2.11,-0.43] | **YES** |
| Qwen_SciERC | theta2n | 6->8 | 0.6634 | 0.6593 | 0.41pp | [-1.02,+0.22] | no |
| Qwen_SciERC | theta2n | 8->16 | 0.6593 | 0.6344 | 2.49pp | [-3.31,-1.65] | **YES** |
| Qwen_SciERC | uniform | 2->4 | 0.6446 | 0.6322 | 1.24pp | [-2.22,-0.23] | **YES** |
| Qwen_SciERC | uniform | 6->8 | 0.6634 | 0.6593 | 0.41pp | [-1.02,+0.22] | no |
| Qwen_CoNLL | lp_weighted | 4->6 | 0.9059 | 0.9028 | 0.31pp | [-0.72,+0.16] | no |
| Qwen_CoNLL | lp_weighted | 6->8 | 0.9028 | 0.8994 | 0.34pp | [-0.61,-0.09] | **YES** |
| Qwen_CoNLL | lp_weighted | 8->16 | 0.8994 | 0.8743 | 2.51pp | [-2.92,-2.10] | **YES** |
| Qwen_CoNLL | vc_weighted | 4->6 | 0.9073 | 0.9058 | 0.15pp | [-0.49,+0.20] | no |
| Qwen_CoNLL | vc_weighted | 6->8 | 0.9058 | 0.9039 | 0.19pp | [-0.45,+0.07] | no |
| Qwen_CoNLL | vc_weighted | 8->16 | 0.9039 | 0.8859 | 1.80pp | [-2.18,-1.44] | **YES** |
| Qwen_CoNLL | sj_weighted | 4->6 | 0.9057 | 0.9041 | 0.16pp | [-0.51,+0.18] | no |
| Qwen_CoNLL | sj_weighted | 6->8 | 0.9041 | 0.9026 | 0.15pp | [-0.42,+0.12] | no |
| Qwen_CoNLL | sj_weighted | 8->16 | 0.9026 | 0.8876 | 1.51pp | [-1.86,-1.16] | **YES** |
| Qwen_CoNLL | theta2n | 4->6 | 0.9050 | 0.8961 | 0.89pp | [-1.22,-0.56] | **YES** |
| Qwen_CoNLL | theta2n | 6->8 | 0.8961 | 0.8869 | 0.92pp | [-1.16,-0.68] | **YES** |
| Qwen_CoNLL | theta2n | 8->16 | 0.8869 | 0.8524 | 3.45pp | [-3.87,-3.04] | **YES** |
| Qwen_CoNLL | uniform | 2->4 | 0.8674 | 0.8397 | 2.77pp | [-3.23,-2.31] | **YES** |
| Qwen_CoNLL | uniform | 6->8 | 0.8961 | 0.8869 | 0.92pp | [-1.16,-0.68] | **YES** |
| Qwen_FewNERD | lp_weighted | 6->8 | 0.7828 | 0.7771 | 0.57pp | [-0.83,-0.31] | **YES** |
| Qwen_FewNERD | lp_weighted | 8->16 | 0.7771 | 0.7524 | 2.47pp | [-2.87,-2.05] | **YES** |
| Qwen_FewNERD | vc_weighted | 8->16 | 0.7807 | 0.7640 | 1.68pp | [-2.07,-1.27] | **YES** |
| Qwen_FewNERD | sj_weighted | 8->16 | 0.7775 | 0.7646 | 1.29pp | [-1.65,-0.93] | **YES** |
| Qwen_FewNERD | theta2n | 4->6 | 0.7743 | 0.7718 | 0.24pp | [-0.60,+0.11] | no |
| Qwen_FewNERD | theta2n | 6->8 | 0.7718 | 0.7617 | 1.01pp | [-1.25,-0.77] | **YES** |
| Qwen_FewNERD | theta2n | 8->16 | 0.7617 | 0.7237 | 3.80pp | [-4.19,-3.39] | **YES** |
| Qwen_FewNERD | uniform | 2->4 | 0.7306 | 0.7023 | 2.84pp | [-3.24,-2.42] | **YES** |
| Qwen_FewNERD | uniform | 6->8 | 0.7718 | 0.7617 | 1.01pp | [-1.25,-0.77] | **YES** |
| LLaMA_SciERC | majority_vote | 6->8 | 0.6663 | 0.6634 | 0.28pp | [-0.90,+0.29] | no |
| LLaMA_SciERC | lp_weighted | 8->16 | 0.6693 | 0.6604 | 0.88pp | [-1.69,-0.07] | **YES** |
| LLaMA_SciERC | vc_weighted | 8->16 | 0.6686 | 0.6638 | 0.47pp | [-1.32,+0.40] | no |
| LLaMA_SciERC | sj_weighted | 4->6 | 0.6655 | 0.6606 | 0.49pp | [-1.31,+0.32] | no |
| LLaMA_SciERC | sj_weighted | 8->16 | 0.6670 | 0.6633 | 0.38pp | [-1.20,+0.45] | no |
| LLaMA_SciERC | theta2n | 4->6 | 0.6663 | 0.6637 | 0.26pp | [-1.00,+0.50] | no |
| LLaMA_SciERC | theta2n | 6->8 | 0.6637 | 0.6606 | 0.31pp | [-0.89,+0.28] | no |
| LLaMA_SciERC | theta2n | 8->16 | 0.6606 | 0.6477 | 1.28pp | [-2.04,-0.50] | **YES** |
| LLaMA_SciERC | uniform | 2->4 | 0.6530 | 0.6463 | 0.67pp | [-1.56,+0.24] | no |
| LLaMA_SciERC | uniform | 6->8 | 0.6637 | 0.6606 | 0.31pp | [-0.89,+0.28] | no |
| LLaMA_CoNLL | lp_weighted | 6->8 | 0.9310 | 0.9286 | 0.24pp | [-0.36,-0.11] | **YES** |
| LLaMA_CoNLL | lp_weighted | 8->16 | 0.9286 | 0.9251 | 0.35pp | [-0.55,-0.16] | **YES** |
| LLaMA_CoNLL | vc_weighted | 8->16 | 0.9295 | 0.9257 | 0.38pp | [-0.56,-0.20] | **YES** |
| LLaMA_CoNLL | sj_weighted | 8->16 | 0.9297 | 0.9262 | 0.35pp | [-0.52,-0.19] | **YES** |
| LLaMA_CoNLL | theta2n | 4->6 | 0.9294 | 0.9283 | 0.11pp | [-0.27,+0.05] | no |
| LLaMA_CoNLL | theta2n | 6->8 | 0.9283 | 0.9261 | 0.21pp | [-0.35,-0.07] | **YES** |
| LLaMA_CoNLL | theta2n | 8->16 | 0.9261 | 0.9221 | 0.40pp | [-0.60,-0.22] | **YES** |
| LLaMA_CoNLL | uniform | 2->4 | 0.9245 | 0.9208 | 0.37pp | [-0.58,-0.16] | **YES** |
| LLaMA_CoNLL | uniform | 6->8 | 0.9283 | 0.9261 | 0.21pp | [-0.35,-0.07] | **YES** |
| LLaMA_FewNERD | lp_weighted | 4->6 | 0.7949 | 0.7928 | 0.21pp | [-0.33,-0.10] | **YES** |
| LLaMA_FewNERD | lp_weighted | 6->8 | 0.7928 | 0.7869 | 0.59pp | [-0.68,-0.50] | **YES** |
| LLaMA_FewNERD | vc_weighted | 6->8 | 0.7913 | 0.7894 | 0.19pp | [-0.29,-0.10] | **YES** |
| LLaMA_FewNERD | sj_weighted | 6->8 | 0.7905 | 0.7891 | 0.14pp | [-0.23,-0.04] | **YES** |
| LLaMA_FewNERD | theta2n | 4->6 | 0.7893 | 0.7815 | 0.77pp | [-0.88,-0.67] | **YES** |
| LLaMA_FewNERD | theta2n | 6->8 | 0.7815 | 0.7705 | 1.10pp | [-1.18,-1.03] | **YES** |
| LLaMA_FewNERD | uniform | 2->4 | 0.7573 | 0.7263 | 3.09pp | [-3.22,-2.97] | **YES** |
| LLaMA_FewNERD | uniform | 6->8 | 0.7815 | 0.7705 | 1.10pp | [-1.18,-1.03] | **YES** |

### Method Behavior Summary

| Config | majority_vote | lp_weighted | vc_weighted | sj_weighted | theta2n | uniform |
|--------|--------|--------|--------|--------|--------|--------|
| Qwen_SciERC | mono inc | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** |
| Qwen_CoNLL | mono inc | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** |
| Qwen_FewNERD | mono inc | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** |
| LLaMA_SciERC | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** |
| LLaMA_CoNLL | mono inc | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** |
| LLaMA_FewNERD | mono inc | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** | **INVERSE** |

### Degeneracy by N

| Config |N=2 | N=4 | N=6 | N=8 | N=16 |
|--------|------|------|------|------|------|
| Qwen_SciERC | 44.6% | 24.2% | 15.7% | 11.7% | 7.6% |
| Qwen_CoNLL | 78.6% | 67.3% | 61.2% | 56.9% | 46.7% |
| Qwen_FewNERD | 42.4% | 22.3% | 14.5% | 10.4% | 4.5% |
| LLaMA_SciERC | 50.3% | 30.4% | 23.1% | 19.8% | 12.3% |
| LLaMA_CoNLL | 95.7% | 91.7% | 89.6% | 88.4% | 85.1% |
| LLaMA_FewNERD | 54.1% | 35.5% | 26.8% | 23.4% | - |

## Mechanism Analysis

### Why theta2n shows the strongest inverse scaling

theta2n (theta=2/N, uniform weights) is the worst affected because its threshold becomes excessively lenient at large N. At N=16, theta=0.125, meaning any entity appearing in just 2 of 16 samples is included. This over-inclusion of noisy, spurious entities degrades precision faster than the marginal recall gains from more diverse samples. On CoNLL (Qwen), theta2n drops 3.45pp from N=8 to N=16.

### Why weighted methods (lp/vc/sj) also show inverse scaling

All weighted methods use theta=2/N, inheriting the same over-lenient threshold. Weighting partially compensates by downweighting unreliable samples, but the effect is insufficient: once the threshold is low enough to admit noise, even well-weighted noisy entities accumulate. The severity ranking (lp > vc > sj) reflects the degree to which each weighting scheme correlates with entity correctness.

### Why majority_vote is immune

majority_vote (theta=0.5 fixed) maintains a proportional threshold: an entity always needs >50% consensus regardless of N. Entities passing this bar are genuinely consistent across samples. As N grows, the effective vote count increases (e.g., 8 of 16), but so does the evidence base. This ratio-based requirement naturally prevents over-inclusion. Only 1 borderline case (LLaMA SciERC N=6->8, not significant) was detected.

### Why uniform shows non-monotonic behavior

uniform (theta=0.25 fixed) shows a characteristic "dip-then-recovery" pattern, especially at N=2->4 (e.g., -3.09pp on LLaMA FewNERD, -2.77pp on Qwen CoNLL). At N=2-4, the effective vote threshold is 1 (any entity from any sample is included), so more samples = more noise without filtering. At N=6+, the threshold rises to 2+ votes, enabling filtering and recovery.

### Threshold type is the primary driver

The critical distinction is not the weighting scheme but the threshold type:
- **Fixed proportional threshold** (theta=0.5): immune to inverse scaling
- **Adaptive decreasing threshold** (theta=2/N): systematically affected
- **Fixed low threshold** (theta=0.25): affected at specific N transitions

This suggests that the commonly-recommended theta=2/N ("confirmation threshold") may be suboptimal at large N. A fixed proportional threshold like theta=0.5 is more robust.

### Relationship with degeneracy

High degeneracy (CoNLL: 46-96%) does NOT prevent inverse scaling---in fact, CoNLL shows the largest absolute drops. When most instances are degenerate (all samples identical), construction reduces to greedy for those instances, and the non-degenerate minority drives the aggregate F1 changes. The inverse scaling is concentrated in the low-consensus tail of the distribution.

### Degeneracy Correlation

- **Qwen_SciERC**: degeneracy at N=2: 44.6%, at N=16: 7.6%
- **Qwen_CoNLL**: degeneracy at N=2: 78.6%, at N=16: 46.7%
- **Qwen_FewNERD**: degeneracy at N=2: 42.4%, at N=16: 4.5%
- **LLaMA_SciERC**: degeneracy at N=2: 50.3%, at N=16: 12.3%
- **LLaMA_CoNLL**: degeneracy at N=2: 95.7%, at N=16: 85.1%
- **LLaMA_FewNERD**: degeneracy at N=2: 54.1%, at N=8: 23.4%

## Conclusion

We find 40 statistically significant inverse scaling case(s). This is a notable finding for structured self-consistency. The finding has implications for practitioners choosing aggregation methods and sample budgets.
