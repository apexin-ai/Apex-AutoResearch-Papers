# tail_decay Fix Report (2026-05-20)

## Problem
Original 6 generators used log-prob slope for tail_decay; 3 new generators (Llama-3.2-3B, Mistral-7B, Gemma-2-2B) used NLL proportion.

## Two Implementations Compared

### Original (extract_features.py) — Log-prob Slope
```python
avg_log_probs = log_probs.float().mean(dim=0)  # per-vocab average
sorted_lp, _ = torch.sort(avg_log_probs, descending=True)
x = np.arange(100, 1000)  # ranks 100-1000
y = sorted_lp_np[100:1000]
coeffs = np.polyfit(x, y, 1)
tail_decay = coeffs[0]  # slope of linear fit
```
- Output: negative float ~-0.002
- Measures: how quickly vocab probability distribution decays in tail

### New (llama/mistral_filter_and_extract.py) — NLL Proportion
```python
threshold_90 = np.percentile(depth0_nll_values, 90)
tail_decay = np.mean(nll_arr > threshold_90)  # proportion above threshold
```
- Output: float in [0, 1], typically ~0.1
- Measures: fraction of tokens with high NLL

## Fix Status
| Generator | Fix Method | File Modified |
|-----------|-----------|--------------|
| llama-3.2-3b | fix_tail_decay_and_eval.py | 2026-05-16 |
| mistral-7b-v0.3 | fix_tail_decay_and_eval.py | 2026-05-16 |
| gemma-2-2b | Re-extracted with slope formula | 2026-05-20 |

## Verification: All 9 generators now consistent

| Generator | mean | std | range |
|-----------|------|-----|-------|
| olmo-2-1b | -0.002335 | 0.000223 | [-0.003682, 0.000] |
| pythia-1b | -0.002236 | 0.000242 | [-0.004007, 0.000] |
| pythia-2.8b | -0.002249 | 0.000241 | [-0.003369, 0.000] |
| qwen3-0.6b | -0.002329 | 0.000211 | [-0.003647, 0.000] |
| qwen3-1.7b | -0.002321 | 0.000232 | [-0.006501, 0.000] |
| qwen3-8b | -0.002318 | 0.000222 | [-0.006554, 0.000] |
| llama-3.2-3b | -0.002303 | 0.000214 | [-0.004643, -0.001723] |
| mistral-7b-v0.3 | -0.002293 | 0.000195 | [-0.003581, -0.001661] |
| gemma-2-2b | -0.002308 | 0.000219 | [-0.004049, -0.001271] |

## Gemma Before/After
- Before (NLL proportion): mean=0.1027, range=[0, 1]
- After (log-prob slope): mean=-0.0023, range=[-0.004, -0.001]

## 9gen LOGO Results (unchanged — data was already corrected)
- 3-class macro F1: 0.751
- Binary macro F1: 0.666

## Updated Files
- data/features_9gen.csv — combined 9-gen features (42,015 rows)
- eval_9gen_logo.py — stale note on line 212 corrected
- results/9gen_logo_results.json — notes updated
