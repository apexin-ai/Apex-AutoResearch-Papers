# data sf4 sf2 m2m4m5 extract

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_sf4-sf2-m2m4m5-extract_20260518T051646_result.json`
- **Structured JSON:** [`9b37917ac341e74b82d0.json`](../../sessions/9b/9b37917ac341e74b82d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here are the 5 results:

---

### P1: SF4 — Random 300 MAE

Per-seed MAE (|IRT calibrated θ − clean baseline accuracy|):
- Seed 42: 0.0059, Seed 123: 0.0360, Seed 456: 0.0335, Seed 789: 0.0207, Seed 1024: 0.0234

**MAE = 0.024 ± 0.012** (5 seeds), alongside **τ = 0.554 ± 0.048**

Note: ground_truth in the JSON is clean baseline accuracy (not dosage level). The 16 models are 8×1.5B + 8×3B Qwen, vanilla 2PL, 300 random items.

---

### P2: SF2 — SFT Data Configuration

Contaminated items are appended to the base SFT corpus (augmentation, not replacement); d100 models receive **16,533** additional training examples beyond the base **50,000** examples.

Details from `data_meta.json` and `wc -l`:

| Dosage | Total examples | Base | Contaminated appended |
|--------|---------------|------|-----------------------|
| d000 | 50,000 | 50,000 | 0 |
| d005 | 50,826 | 50,000 | 826 (5% of 16,533) |
| d025 | 54,133 | 50,000 | 4,133 (25% of 16,533) |
| d100 | 66,533 | 50,000 | 16,533 (100% of 16,533) |

Contamination pool: MMLU 14,042 + GSM8K 1,319 + ARC 1,172 = 16,533. `mix_data()` does `list(base_data) + selected` then shuffles.

---

### P4-M2: S4 (Self-Critique) Prompt Template

**Prompt:**
```
Is the following answer correct? Answer: {answer}. Question: {question}. Explain briefly then conclude with YES or NO.
```

**Scoring:**
1. Model generates an answer to the benchmark question (greedy decode, max 64 tokens)
2. Critique prompt constructed with generated answer + original question (both truncated to 500 chars)
3. Extract logits at last position for YES/NO token variants (6 variants each: "YES"/"Yes"/"yes"/" YES"/" Yes"/" yes")
4. Normalize to binary P(YES), P(NO) via logsumexp
5. Compute binary entropy H = −p·log₂(p) − (1−p)·log₂(1−p)
6. **Score = −entropy** (more negative = higher uncertainty = less contaminated; near 0 = highly confident = more contaminated)

Source: `/root/contamcal-irt-calibration/exp002/signals/s4_selfcritique.py`

---

### P4-M4: SFT Training Final Loss (3B models)

Last logged training loss (within 5-9 steps of completion):

| Model | Dosage | Seed | Final Loss | Steps |
|-------|--------|------|------------|-------|
| d000_s42 | 0% | 42 | **1.075** | 3120/3125 |
| d000_s123 | 0% | 123 | **1.114** | 3120/3125 |
| d005_s42 | 5% | 42 | **1.082** | 3170/3177 |
| d005_s123 | 5% | 123 | **1.070** | 3170/3177 |
| d025_v3_s42 | 25% | 42 | **1.135** | 3380/3384 |
| d025_s123 | 25% | 123 | **1.140** | 3380/3384 |
| d100_a32_s42_v3 | 100% | 42 | **1.206** | 4150/4159 |
| d100_a32_s123 | 100% | 123 | **1.132** | 4150/4159 |

Loss increases with dosage (d000 ~1.07-1.11 → d100 ~1.13-1.21), consistent with contaminated items adding distribution shift.

---

### P4-M5: Within-Family GSM8K PPP

**N=24 pure Qwen (0.5B+1.5B+3B), 2PL+γ, 300 items:**
- **PPP = 0.541** (adequate fit)
- cal_MAE = 0.006, raw_MAE = 0.169
- γ = 0.064 ± 0.221 (CI includes zero → no significant contamination signal)
- Diagnostics: max R̂ = 1.008, min ESS = 1313, 0 divergences

Also available per-scale: 3B-only (N=7) PPP = 0.245 (poor fit, N too small for reliable IRT).

Source: `/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16_fixed/gsm8k/irt_results.json`

---
