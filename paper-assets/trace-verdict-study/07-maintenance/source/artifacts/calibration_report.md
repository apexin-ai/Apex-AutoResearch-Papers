# Cross-Model & Cross-Condition Calibration Report

**Date**: 2026-05-20  
**Dataset**: 1,190 test samples (exception_only condition)  
**Source**: `/root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration/`

---

## 1. Four-Model Exception-Only Calibration Comparison

| Model | ECE ↓ | Brier ↓ | MCE ↓ | Accuracy |
|-------|-------|---------|-------|----------|
| Qwen-1.5B | **0.0020** | **0.0013** | 0.7549 | 99.83% |
| CodeLlama-13B | 0.0020 | 0.0013 | **0.0411** | 99.83% |
| Qwen-7B | 0.0027 | 0.0013 | 0.8355 | 99.83% |
| DeepSeek-6.7B | 0.0064 | 0.0061 | 0.7756 | 99.33% |

### Per-Class Breakdown

| Model | Pass ECE | Pass Brier | Fail ECE | Fail Brier |
|-------|----------|------------|----------|------------|
| Qwen-1.5B | 0.0027 | 0.0018 | 0.0003 | 0.000001 |
| CodeLlama-13B | 0.0016 | 0.0018 | 0.0033 | 0.000015 |
| Qwen-7B | 0.0037 | 0.0018 | 0.0003 | 0.000001 |
| DeepSeek-6.7B | 0.0069 | 0.0081 | 0.0079 | 0.0012 |

---

## 2. Cross-Condition Calibration (Qwen-7B)

| Condition | ECE ↓ | Brier ↓ | MCE ↓ | Accuracy |
|-----------|-------|---------|-------|----------|
| ae_only | **0.0004** | **0.0008** | **0.0004** | 99.92% |
| exception_only | 0.0027 | 0.0013 | 0.8355 | 99.83% |
| vota | 0.0054 | 0.0052 | 0.6225 | 99.41% |
| loop_only | 0.0831 | 0.1184 | 0.1834 | 85.63% |
| full_trace | 0.0958 | 0.1439 | 0.2491 | 81.76% |
| label_only | 0.1107 | 0.1201 | 0.4171 | 86.22% |
| no_trace | 0.1715 | 0.1972 | 0.4756 | 75.13% |

---

## 3. Key Findings

### Cross-Model (exception_only)

1. **All 4 models are well-calibrated** with ECE < 0.007. The exception_only trace condition produces highly confident, well-calibrated predictions regardless of model architecture or scale.

2. **Qwen-1.5B and CodeLlama-13B tie for best ECE** (0.0020). Model scale does not improve calibration — the 1.5B model matches or beats the 7B and 13B models.

3. **CodeLlama-13B has dramatically better MCE** (0.041 vs. 0.75–0.84 for others). The other three models all have a single low-count bin (typically 1 sample in the 0.80–0.85 range) where the model is confident but wrong, inflating MCE. CodeLlama-13B avoids this by distributing uncertain predictions into the 0.70–0.75 bin where accuracy roughly matches confidence.

4. **DeepSeek-6.7B is the outlier**: 3× higher ECE, 5× higher Brier, and 0.5% lower accuracy. It also has the most spread confidence distribution (samples across 6 bins vs. 3 bins for others), suggesting less decisive predictions.

5. **Brier scores are near-identical** for Qwen-7B, Qwen-1.5B, and CodeLlama-13B (all ~0.0013), confirming that calibration quality is dominated by the trace signal, not model capacity.

### Cross-Condition (Qwen-7B)

6. **Calibration tracks accuracy almost perfectly**: the three high-accuracy conditions (ae_only, exception_only, vota) all have ECE < 0.006, while the lower-accuracy conditions (loop_only, full_trace, label_only, no_trace) have ECE 0.08–0.17.

7. **ae_only achieves near-perfect calibration** (ECE=0.0004, MCE=0.0004) — 99.92% of predictions fall in the 0.95–1.0 confidence bin. This is the most "trivially separable" condition.

8. **ECE vs. MCE divergence reveals a calibration pathology**: exception_only has low ECE (0.0027) but extremely high MCE (0.8355), meaning the average calibration is excellent but a single bin has a catastrophic gap. In practice, this is a single misclassified sample with ~83.5% confidence. MCE is sensitive to bin count noise; ECE and Brier are more reliable metrics here.

9. **Non-trace conditions are systematically overconfident**: no_trace (ECE=0.17) and label_only (ECE=0.11) show the model assigns high confidence to incorrect predictions — a calibration failure that would matter in deployment.

---

## 4. Confidence Distribution Summary

| Model (exception_only) | Samples in [0.95, 1.0] | Samples in other bins |
|------------------------|------------------------|-----------------------|
| Qwen-7B | 1182 (99.3%) | 8 |
| Qwen-1.5B | 1182 (99.3%) | 8 |
| CodeLlama-13B | 1182 (99.3%) | 8 |
| DeepSeek-6.7B | 1171 (98.4%) | 19 |

All models concentrate predictions in the highest confidence bin. DeepSeek has ~2× more uncertain predictions.

---

## 5. Reliability Diagram Highlights

**CodeLlama-13B** (best MCE): 8 samples in [0.70, 0.75] bin with acc=75%, conf=70.9% → gap=4.1%. No samples in the problematic 0.80–0.85 bin.

**Qwen-7B** (worst MCE): 1 sample in [0.80, 0.85] bin with acc=0%, conf=83.5% → gap=83.5%. This single misclassified sample drives the entire MCE.

**DeepSeek-6.7B** (worst ECE): 7 samples in [0.90, 0.95] bin with acc=14.3%, conf=91.8% → gap=77.6%. Multiple samples are confidently wrong, not just one.
