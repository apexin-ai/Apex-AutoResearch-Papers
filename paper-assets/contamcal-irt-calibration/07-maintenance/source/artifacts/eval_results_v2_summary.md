# Eval Results v2 Summary (Post-D148 Logprob Fix)

**Date**: 2026-05-19
**Server**: westd-29999
**Source**: `/root/autodl-tmp/exp001/eval_results_v2/`
**Eval method**: Logprob-based MCQ scoring (aligned format), 5-shot MMLU, 25-shot ARC Challenge

## Full Results Table

| Model | Dosage | MMLU (acc) | ARC-C (acc) |
|-------|--------|------------|-------------|
| Qwen2.5-7B | d000 | 0.6611 | 0.8788 |
| Qwen2.5-7B | d005 | 0.6474 | 0.8609 |
| Qwen2.5-7B | d025 | 0.6298 | 0.8404 |
| Qwen2.5-7B | d050 | 0.6307 | 0.8456 |
| Qwen2.5-7B | d100 | 0.6433 | 0.8498 |
| Qwen2.5-14B | d000 | 0.6944 | 0.9104 |
| Qwen2.5-14B | d005 | 0.6901 | 0.9036 |
| Qwen2.5-14B | d025 | 0.6204 | 0.8891 |
| Qwen2.5-14B | d050 | 0.5941 | 0.8763 |
| Qwen2.5-14B | d100 | 0.6007 | 0.8848 |
| Phi-4 | d000 | 0.7644 | 0.9206 |
| Phi-4 | d005 | 0.7636 | 0.9181 |
| Phi-4 | d025 | 0.7698 | 0.9232 |
| Phi-4 | d050 | 0.7675 | 0.9241 |
| Phi-4 | d100 | 0.7627 | 0.9266 |
| Gemma-2-9B | d000 | 0.6186 | 0.8601 |
| Gemma-2-9B | d005 | 0.6342 | 0.7782 |
| Gemma-2-9B | d025 | 0.6456 | 0.8737 |
| Gemma-2-9B | d050 | 0.6401 | 0.7108 |
| Gemma-2-9B | d100 | 0.6562 | 0.8481 |
| OLMo-2-7B | d000 | 0.5379 | 0.7611 |
| OLMo-2-7B | d005 | 0.5614 | 0.7662 |
| OLMo-2-7B | d025 | 0.5617 | 0.7816 |
| OLMo-2-7B | d050 | 0.5725 | 0.7961 |
| OLMo-2-7B | d100 | 0.5700 | 0.8003 |

## By Model (Dose-Response Trends)

### Qwen2.5-7B
- MMLU: 0.661 → 0.643 (d000→d100, -1.8pp), non-monotonic dip at d025/d050
- ARC-C: 0.879 → 0.850 (d000→d100, -2.9pp), monotonic decline then partial recovery

### Qwen2.5-14B
- MMLU: 0.694 → 0.601 (d000→d100, **-9.4pp**), largest degradation across all models
- ARC-C: 0.910 → 0.885 (d000→d100, -2.6pp), gradual decline

### Phi-4
- MMLU: 0.764 → 0.763 (d000→d100, -0.2pp), **virtually no effect**
- ARC-C: 0.921 → 0.927 (d000→d100, +0.6pp), slight increase — contamination-robust

### Gemma-2-9B
- MMLU: 0.619 → 0.656 (d000→d100, +3.8pp), slight upward trend
- ARC-C: **highly erratic** — 0.860, 0.778, 0.874, 0.711, 0.848 — non-monotonic, suggests instability

### OLMo-2-7B
- MMLU: 0.538 → 0.570 (d000→d100, +3.2pp), consistent upward trend
- ARC-C: 0.761 → 0.800 (d000→d100, +3.9pp), monotonic increase — contamination inflates scores

## Cross-Model Summary

| Model | MMLU d000 | MMLU d100 | Δ MMLU | ARC d000 | ARC d100 | Δ ARC |
|-------|-----------|-----------|--------|----------|----------|-------|
| Qwen2.5-7B | 0.661 | 0.643 | -1.8pp | 0.879 | 0.850 | -2.9pp |
| Qwen2.5-14B | 0.694 | 0.601 | **-9.4pp** | 0.910 | 0.885 | -2.6pp |
| Phi-4 | 0.764 | 0.763 | -0.2pp | 0.921 | 0.927 | +0.6pp |
| Gemma-2-9B | 0.619 | 0.656 | +3.8pp | 0.860 | 0.848 | -1.2pp |
| OLMo-2-7B | 0.538 | 0.570 | +3.2pp | 0.761 | 0.800 | +3.9pp |
