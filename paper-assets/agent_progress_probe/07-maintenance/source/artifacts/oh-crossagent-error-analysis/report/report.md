# OH Cross-Agent Probe Zero-Shot Error Analysis

## Summary

SWE-agent-trained GRU probe evaluated zero-shot on OpenHands conf>=2 data (43,366 windows, 19.9% stag). The probe achieves macro_f1=0.581 (f1_stag=0.278, f1_prog=0.884), with errors heavily skewed toward FP (stag mispredicted as prog). Structural GB baseline achieves macro_f1=0.998 on the same data with near-zero error overlap with the probe.

---

## 1. Probe Zero-Shot Error Distribution

| Metric | Value |
|--------|-------|
| Total windows | 43,366 |
| Total errors | 8,643 (19.9%) |
| FP (stag->prog) | 6,955 (80.5% of errors) |
| FN (prog->stag) | 1,688 (19.5% of errors) |
| macro_f1 | 0.581 |
| f1_stag | 0.278 |
| f1_prog | 0.884 |

**Key finding:** The probe has a massive progress bias on OH data -- it predicts prog for ~92% of all windows, missing most stagnation.

### 1.1 Error by LF Confidence

| Conf | n | Errors | Error Rate | FP | FN | macro_f1 |
|------|---|--------|------------|----|----|----------|
| 2 | 42,364 | 7,936 | 18.7% | 6,251 | 1,685 | 0.581 |
| 3 | 1,002 | 707 | **70.6%** | 704 | 3 | 0.288 |

**Critical:** conf=3 windows (all 3 LFs agree) have 70.6% error rate. Nearly all conf=3 errors are FP (704/707), meaning the probe confidently predicts progress for windows where all LFs unanimously indicate stagnation. This is the strongest evidence of embedding distribution shift.

### 1.2 Error by Trajectory Position

| Position | n | Errors | Error Rate | FP | FN |
|----------|---|--------|------------|----|----|
| Early (0-25%) | 11,061 | 2,198 | 19.9% | 1,789 | 409 |
| Mid (25-75%) | 21,031 | 4,138 | 19.7% | 3,320 | 818 |
| Late (75-100%) | 11,274 | 2,307 | 20.5% | 1,846 | 461 |

Error rate is roughly uniform across trajectory positions (~20%), unlike in-domain errors which concentrate in late positions. This suggests the cross-agent error is a global distribution shift, not position-dependent.

### 1.3 Model Confidence

| Category | Mean Prob | Mean Confidence (|p-0.5|) |
|----------|-----------|---------------------------|
| Correct samples | 0.924 | 0.454 |
| All errors | 0.791 | 0.380 |
| FP (stag->prog) | **0.917** | 0.417 |
| FN (prog->stag) | 0.273 | 0.228 |

- **62% of all errors are high-confidence** (prob>0.9 for FP or <0.1 for FN)
  - FP with prob>0.9: **5,068** (72.9% of all FP)
  - FN with prob<0.1: 287 (17.0% of all FN)
- FP errors are particularly dangerous: probe is very confident (mean prob=0.917) when wrongly predicting progress for stagnating windows

### 1.4 Probability Histogram

| Prob Range | n | Errors | Error Rate |
|------------|---|--------|------------|
| 0.0-0.1 | 975 | 287 | 29.4% |
| 0.1-0.2 | 534 | 255 | 47.8% |
| 0.2-0.3 | 583 | 351 | 60.2% |
| 0.3-0.4 | 629 | 391 | 62.2% |
| 0.4-0.5 | 628 | 404 | 64.3% |
| 0.5-0.6 | 798 | 280 | 35.1% |
| 0.6-0.7 | 1,061 | 361 | 34.0% |
| 0.7-0.8 | 1,419 | 436 | 30.7% |
| 0.8-0.9 | 2,614 | 810 | 31.0% |
| 0.9-1.0 | 34,125 | 5,068 | 14.9% |

78.7% of all windows fall in the 0.9-1.0 bin (probe overwhelmingly predicts high-confidence progress). The mid-range bins (0.2-0.5) have the highest error rates (60-64%), but contain few samples.

### 1.5 Error by Trajectory Length

| Length | n | Errors | Error Rate | macro_f1 |
|--------|---|--------|------------|----------|
| 10-20 | 2,085 | 430 | 20.6% | 0.551 |
| 20-50 | 41,281 | 8,213 | 19.9% | 0.583 |

Most OH trajectories are long (20-50 windows), so trajectory length has minimal effect on error rate.

---

## 2. LF Firing Patterns in Errors

### Per-LF Analysis

| LF | FP: LF says stag | FP: total | FP% | FN: LF says prog | FN: total | FN% |
|----|-------------------|-----------|-----|-------------------|-----------|-----|
| file_diff_delta | 1,255 | 6,955 | 18.0% | 429 | 1,688 | 25.4% |
| command_repetition | 358 | 6,955 | **5.1%** | 1,488 | 1,688 | **88.2%** |
| outcome_backpropagation | 1,256 | 6,955 | 18.1% | 69 | 1,688 | 4.1% |

**FP errors (stag predicted as prog):**
- Only 5.1% have cmd_rep=stag. Most FP windows have cmd_rep=prog or abstain.
- file_diff_delta and outcome_bp contribute to the stag label in ~18% of FP errors.
- Dominant FP pattern: windows where only file_diff or outcome_bp signals stag but embedding looks "progressive"

**FN errors (prog predicted as stag):**
- 88.2% have cmd_rep=prog -- the probe misreads OH progress embeddings as SWE-agent stagnation patterns
- outcome_bp rarely signals prog in FN errors (4.1%)

### Top FP Patterns (stag windows mispredicted as prog)

| Pattern (file_diff, cmd_rep, outcome_bp) | Count | Interpretation |
|------------------------------------------|-------|----------------|
| (abstain, prog, abstain) | 2,894 | Only cmd_rep votes, but overall label is stag |
| (prog, prog, abstain) | 1,152 | file_diff+cmd_rep say prog, outcome_bp abstains |
| (abstain, prog, stag) | 733 | outcome_bp dissents but probe follows prog pattern |
| (stag, prog, abstain) | 882 | file_diff says stag, cmd_rep says prog |

---

## 3. Structural GB Comparison

### Performance

| Model | macro_f1 | f1_stag | f1_prog | Errors |
|-------|----------|---------|---------|--------|
| GRU Probe (zero-shot) | 0.581 | 0.278 | 0.884 | 8,643 |
| Structural GB (cross-agent) | **0.998** | 0.997 | 0.999 | **57** |

Structural GB makes only 57 errors (32 FP + 25 FN) vs probe's 8,643 errors.

### Error Overlap

Analysis on 12,328 common windows (matched by trajectory_id + window_idx):

| Category | Count |
|----------|-------|
| Probe errors | 2,460 |
| Struct errors | 13 |
| Both wrong | **2** |
| Probe-only errors | 2,458 |
| Struct-only errors | 11 |
| Overlap rate (probe) | **0.08%** |

**Near-zero error overlap.** The two models fail on completely different windows. The probe's errors are embedding-distribution-shift errors that structural features are immune to. The structural model's rare errors are isolated edge cases.

### Probe-Only Error Characteristics

**FP (1,968 probe-only FPs):**
- Mean position: 0.587 (mid-late trajectory)
- 87.5% have cmd_rep=prog, 70.1% have file_diff=prog
- These are windows where structural features correctly identify the pattern but embedding-based probe fails due to OH embedding shift

**FN (490 probe-only FNs):**
- Mean position: 0.597
- 89.0% have cmd_rep=prog -- these are truly progressing windows that the probe's shifted embeddings classify as stagnating

---

## 4. Error Concentration

- 2,928 / 4,969 trajectories (58.9%) have at least one probe error
- Top error-prone trajectories:
  - zarr-developers__zarr-python-2755: 25/37 errors (68%)
  - onicagroup__runway-1245: 25/32 errors (78%)
  - iterative__dvc-2462: 23/32 errors (72%)
- Error-heavy trajectories are dominated by FP errors (stag windows in failed/stagnating trajectories mispredicted as prog)

---

## 5. Key Takeaways

1. **Progress bias is the dominant failure mode.** 80.5% of errors are FP (stag->prog). The probe has learned SWE-agent-specific embedding patterns for stagnation that don't transfer to OpenHands.

2. **High-confidence errors are the norm.** 62% of errors have prob>0.9 or <0.1. The probe isn't uncertain when it's wrong -- it's confidently wrong. This means calibration/threshold tuning cannot fix the problem.

3. **conf=3 windows are worst.** 70.6% error rate on the most reliable labels. The probe fails hardest where the LFs are most unanimous.

4. **Zero overlap with structural errors.** Only 2/12,328 windows are wrong in both models. The structural baseline (macro_f1=0.998) succeeds by capturing the same heuristic patterns as the LFs directly, making it distribution-shift immune. The probe's embedding-based approach is uniquely vulnerable to framework-level distribution shift.

5. **Position-independent errors.** Unlike in-domain errors (which concentrate late), cross-agent errors are uniformly distributed across trajectory positions, confirming this is a global embedding shift rather than a position-specific phenomenon.

6. **cmd_rep is the biggest source of confusion.** The probe sees OH embeddings with cmd_rep=prog patterns and predicts progress, but the window's true label is stag (overruled by file_diff or outcome_bp). The SWE-trained probe has learned to weight cmd_rep-like embedding patterns too heavily relative to the OH distribution.
