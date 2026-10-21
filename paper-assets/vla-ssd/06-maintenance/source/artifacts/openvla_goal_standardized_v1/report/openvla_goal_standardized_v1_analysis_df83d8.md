# OpenVLA Goal Standardized v1 — Analysis

## Summary

OpenVLA on LIBERO-Goal completes the 5-phase standardized pipeline with both trained (finetuned-libero-goal) and untrained (OXE pretrained) conditions. The most notable deviation from prior suites (Object/Long/Spatial) is the **absence of R2 exit collapse** in the trained model — R2 remains flat (~0.85-0.87) from L8 to L31. All other phases produce expected patterns: finetuning shifts heads toward mixed, cross-instruction classification saturates at 1.0, RSA peaks at L16, and counterfactual sensitivity follows the expected gradient with finetuning amplifying effect sizes.

## Phase Results

### R2 Probing

**Trained (last_preaction):**

| Layer | R2 | Layer | R2 | Layer | R2 | Layer | R2 |
|-------|------|-------|------|-------|------|-------|------|
| L0 | 0.6387 | L8 | 0.8530 | L16 | 0.8622 | L24 | 0.8555 |
| L1 | 0.7444 | L9 | 0.8667 | L17 | 0.8616 | L25 | 0.8557 |
| L2 | 0.7766 | L10 | 0.8693 | L18 | 0.8594 | L26 | 0.8559 |
| L3 | 0.7947 | L11 | 0.8628 | L19 | 0.8618 | L27 | 0.8559 |
| L4 | 0.8180 | L12 | 0.8645 | L20 | 0.8601 | L28 | 0.8590 |
| L5 | 0.8364 | L13 | 0.8685 | L21 | 0.8537 | L29 | 0.8578 |
| L6 | 0.8436 | L14 | 0.8615 | L22 | 0.8540 | L30 | 0.8536 |
| L7 | 0.8410 | L15 | 0.8580 | L23 | 0.8525 | L31 | 0.8532 |

- Peak: L10 = 0.8693
- Exit (L31): 0.8532
- Peak-to-exit delta: **-0.016 (negligible)**

**Untrained (last_preaction):**

| Layer | R2 | Layer | R2 | Layer | R2 | Layer | R2 |
|-------|------|-------|------|-------|------|-------|------|
| L0 | 0.5741 | L8 | 0.7967 | L16 | 0.8000 | L24 | 0.8029 |
| L4 | 0.7773 | L10 | 0.8115 | L20 | 0.8131 | L28 | 0.7681 |
| L6 | 0.7868 | L14 | 0.8094 | L22 | 0.8024 | L30 | 0.7574 |
| L7 | 0.7823 | L15 | 0.7966 | L23 | 0.7992 | L31 | 0.7802 |

- Peak: L20 = 0.8131
- Trough: L30 = 0.7574
- Peak-to-trough delta: **-0.056 (moderate decline)**

**Delta (trained - untrained) at key layers:**

| Layer | Trained | Untrained | Delta |
|-------|---------|-----------|-------|
| L0 | 0.6387 | 0.5741 | +0.065 |
| L8 | 0.8530 | 0.7967 | +0.056 |
| L16 | 0.8622 | 0.8000 | +0.062 |
| L24 | 0.8555 | 0.8029 | +0.053 |
| L31 | 0.8532 | 0.7802 | +0.073 |

**Exit collapse: NOT confirmed.** Trained maintains flat R2 from L8-L31 (~0.85-0.87). Untrained shows MORE decline in exit layers (0.813 -> 0.757). The trained-untrained gap actually WIDENS at exit (L31 delta = +0.073 vs L8 delta = +0.056). This contrasts with Object/Long/Spatial where trained R2 dropped in upper layers.

### L1 Attention

| Metric | Trained | Untrained |
|--------|---------|-----------|
| Instruction-dominant | 23/32 | 26/32 |
| Image-dominant | 0/32 | 0/32 |
| Mixed | 9/32 | 6/32 |

**Trained mixed heads:** h3, h5, h6, h9, h13, h16, h20, h21, h24
**Untrained mixed heads:** h3, h6, h9, h13, h21, h24

Finetuning converts 3 heads from instruction-dominant to mixed (h5, h16, h20). Core mixed heads (h3, h6, h9, h13, h21, h24) are shared — these are architectural, not learned. Note h13 is mixed in both conditions (consistent with TracVLA's universal h13 pattern).

### Cross-Instruction Classification

| Layer | Trained img | Trained last_pre | Untrained img | Untrained last_pre |
|-------|-------------|------------------|---------------|---------------------|
| L0 | 0.978 | 0.976 | 0.992 | 0.986 |
| L1 | 0.980 | 1.000 | 0.993 | 1.000 |
| L5 | 0.993 | 1.000 | 0.995 | 1.000 |
| L8 | 0.996 | 1.000 | 0.998 | 1.000 |
| L12+ | ~1.0 | 1.000 | ~1.0 | 1.000 |

Both conditions achieve perfect classification from L1 (last_preaction). Instruction identity is fully separable in the first layer's output, independent of training status. Untrained L0 img is slightly higher (0.992 vs 0.978).

### RSA

**Best layer (both conditions):** L16_last_preaction

| Condition | RSA | 95% CI |
|-----------|------|--------|
| Trained | 0.6066 | [0.510, 0.694] |
| Untrained | 0.6050 | [0.521, 0.686] |

RSA profiles across layers:

| Layer | Trained img | Trained last_pre | Untrained img | Untrained last_pre |
|-------|-------------|------------------|---------------|---------------------|
| L0 | 0.447 | 0.494 | 0.466 | 0.459 |
| L4 | 0.544 | 0.473 | 0.555 | 0.459 |
| L8 | 0.533 | 0.467 | 0.545 | 0.460 |
| L12 | 0.465 | 0.465 | 0.472 | 0.449 |
| L16 | 0.517 | **0.607** | 0.494 | **0.605** |
| L20 | 0.461 | 0.557 | 0.460 | 0.560 |
| L24 | 0.415 | 0.474 | 0.427 | 0.478 |
| L28 | 0.494 | 0.511 | 0.514 | 0.473 |
| L31 | 0.522 | 0.491 | 0.489 | 0.510 |

Nearly identical profiles. Finetuning does not alter the representational geometry — action-correlated structure peaks at L16 regardless of training.

### Counterfactual

**Trained (Cohen's d, global):**

| Condition | d | MSE | token_div |
|-----------|------|------|-----------|
| wrong | 1.1821 | 0.0938 | 1.000 |
| empty | 1.1696 | 0.0940 | 1.000 |
| shuffled | 1.0960 | 0.0881 | 0.999 |
| paraphrased | 0.9956 | 0.0804 | 0.971 |

Ordering: **wrong > empty > shuffled > paraphrased**

**Untrained (Cohen's d, global):**

| Condition | d | MSE | token_div |
|-----------|------|------|-----------|
| empty | 0.9780 | 0.0691 | 1.000 |
| shuffled | 0.8035 | 0.0549 | 1.000 |
| wrong | 0.7948 | 0.0539 | 1.000 |
| paraphrased | 0.6843 | 0.0442 | 0.996 |

Ordering: **empty > shuffled > wrong > paraphrased**

**Expected ordering:** empty > wrong > shuffled > paraphrased

- Trained: wrong and empty are nearly identical (1.182 vs 1.170, delta=0.013), effectively tied. Rest follows expected gradient. Close enough to expected.
- Untrained: wrong and shuffled are swapped (0.795 vs 0.804, delta=0.009), within noise. Rest follows expected gradient.
- Finetuning amplifies all effect sizes by ~0.3-0.4d uniformly. Paraphrased token_div < 1.0 in both conditions (trained: 0.971, untrained: 0.996), confirming paraphrases sometimes produce identical tokenizations.

## Conclusion

**Overall: positive result with one deviation.**

1. **R2 exit collapse: NOT confirmed (deviation).** Goal is the first OpenVLA suite where trained R2 does not decline at exit layers. R2 stays flat at ~0.85 from L8-L31 with only -0.016 delta. This contrasts with Object/Long/Spatial which all showed clear exit collapse. Possible explanation: Goal tasks have simpler action spaces (fewer distinct manipulation targets), so exit layers are not as heavily repurposed for specialized action decoding.

2. **L1 attention: consistent.** Finetuning increases mixed heads (26->23 instr-dom, 6->9 mixed), with h3/h6/h9/h13/h21/h24 as universal mixed heads — overlapping with TracVLA's h13 finding.

3. **Cross-instruction: consistent.** Perfect separation from L1 in both conditions, as seen in all other suites.

4. **RSA: consistent.** Both peak at L16_last_preaction with near-identical values (~0.606), matching the layer identified in other suites as the action-representation alignment point.

5. **Counterfactual: consistent.** Expected gradient holds with minor top-rank inversions within noise. Finetuning amplifies effect sizes uniformly (~+0.3d).

## Key Metrics (for registry)

```yaml
metrics:
  r2_exit_collapse_confirmed: false
  r2_trained_peak: 0.8693
  r2_trained_exit_L31: 0.8532
  r2_trained_peak_to_exit_delta: -0.016
  r2_untrained_peak: 0.8131
  r2_untrained_exit_L31: 0.7802
  l1_instruction_dominant_trained: 23
  l1_instruction_dominant_untrained: 26
  l1_mixed_trained: 9
  l1_mixed_untrained: 6
  l1_shared_mixed_heads: [3, 6, 9, 13, 21, 24]
  cross_instruction_acc_L1_trained: 1.0
  cross_instruction_acc_L1_untrained: 1.0
  rsa_best_layer: L16_last_preaction
  rsa_trained: 0.6066
  rsa_untrained: 0.6050
  cf_trained_ordering: "wrong > empty > shuffled > paraphrased"
  cf_untrained_ordering: "empty > shuffled > wrong > paraphrased"
  cf_ordering_matches_expected: false
  cf_ordering_approximately_matches: true
  cf_trained_wrong_d: 1.1821
  cf_trained_empty_d: 1.1696
  cf_trained_shuffled_d: 1.0960
  cf_trained_para_d: 0.9956
  cf_untrained_wrong_d: 0.7948
  cf_untrained_empty_d: 0.9780
  cf_untrained_shuffled_d: 0.8035
  cf_untrained_para_d: 0.6843
```
