# exp deberta verifier

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_deberta_verifier_20260518T055951_result.json`
- **Structured JSON:** [`c9d4131054dbdbcfae94.json`](../../sessions/c9/c9d4131054dbdbcfae94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here are the complete results.

---

## DeBERTa Representation Verifier Results

### Training Summary

| Dataset | Train Inst | Test Inst | Samples/Inst | Epochs | Final Train Loss | Final Val Loss |
|---------|-----------|-----------|-------------|--------|-----------------|---------------|
| SciERC | 423 | 106 | 8 | 3 | 0.0063 | 0.0257 |
| Few-NERD | 4,000 | 1,000 | 8 | 3 | 0.0165 | 0.0804 |

### SciERC In-Domain Selection

| Method | Entity F1 | Δ vs Greedy | Gap Closure |
|--------|----------|-------------|-------------|
| Greedy | 0.6620 | — | — |
| LP Selection | 0.6838 | +0.0218 | 17.8% |
| **DeBERTa Verifier** | **0.6061** | **-0.0559** | **-45.4%** |
| Oracle | 0.7849 | +0.1229 | 100.0% |

### Few-NERD In-Domain Selection

| Method | Entity F1 | Δ vs Greedy | Gap Closure |
|--------|----------|-------------|-------------|
| Greedy | 0.7558 | — | — |
| LP Selection | 0.7747 | +0.0189 | 16.3% |
| **DeBERTa Verifier** | **0.7599** | **+0.0041** | **3.5%** |
| Oracle | 0.8719 | +0.1161 | 100.0% |

### Cross-Dataset Transfer

| Train → Eval | Greedy F1 | LP Sel F1 (Gap%) | Verifier Sel F1 (Gap%) | Oracle F1 |
|-------------|----------|-----------------|----------------------|----------|
| SciERC → SciERC | 0.6620 | 0.6838 (17.8%) | 0.6061 (-45.4%) | 0.7849 |
| SciERC → Few-NERD | 0.7492 | 0.7633 (11.0%) | 0.6569 (-72.2%) | 0.8770 |
| Few-NERD → Few-NERD | 0.7558 | 0.7747 (16.3%) | 0.7599 (3.5%) | 0.8719 |
| Few-NERD → SciERC | 0.6620 | 0.6838 (17.8%) | 0.6278 (-27.8%) | 0.7849 |

### Comparison with MLP Verifier (exp-027, SciERC)

| Method | Selection F1 | Gap Closure |
|--------|-------------|-------------|
| Greedy | 0.6441 | — |
| LP Selection (unsup best) | 0.6470 | +1.6% |
| MLP_5feat (supervised) | 0.6386 | -3.1% |
| LR_5feat (supervised) | 0.6407 | -1.9% |
| **DeBERTa Verifier** | **0.6061** | **-45.4%** |
| Oracle | 0.8231 | 100.0% |

*Note: exp-027 uses 16 samples/instance and different train/test splits, so numbers are not directly comparable.*

---

### Key Findings

1. **DeBERTa verifier largely fails as a selection method.** On SciERC it achieves -45.4% gap closure (worse than greedy). On Few-NERD it achieves only +3.5% gap closure (barely above greedy).

2. **Cross-dataset transfer is even worse.** SciERC→Few-NERD gives -72.2% gap closure; Few-NERD→SciERC gives -27.8%.

3. **LP selection consistently outperforms DeBERTa verifier** across all settings (16-18% gap closure vs negative or near-zero).

4. **More training data helps marginally.** Few-NERD (4000 train instances) gets slightly positive gap closure (3.5%) vs SciERC (423 train instances) at -45.4%, but the improvement is small relative to the oracle gap.

5. **Serialized text representations lose structural information.** The DeBERTa verifier sees `"text (type); text2 (type2)"` strings, which discards entity boundary precision. The model learns to predict average quality but cannot reliably rank which specific sample is best for selection. The MLP verifier using handcrafted structural features (SJ, FK, EM, VC, LP) also fails at selection, confirming that the selection gap is fundamentally hard to close with current approaches.

Results saved to `artifacts/deberta_verifier_results.json`. Model checkpoints are on the server at `/root/autodl-tmp/struct_self_consist_ie/output/deberta_verifier/`.

---
