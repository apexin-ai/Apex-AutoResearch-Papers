# exp_008_base_pretrained_15B_eval — Analysis

## Experiment Summary
- **Model**: Qwen2.5-1.5B (base pretrained, no SFT/instruction-tuning)
- **Server**: cqa1-21977, cuda:4, PID 530975
- **Status**: Completed successfully (EXIT_CODE=0, .done sentinel present)
- **Output**: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained/`
- **Log**: `~/runs/exp_008_base_pretrained_15B_eval.log`
- **MC format**: Default (NOT aligned) — caveat for comparison with aligned-format SFT evals

## Benchmark Results

| Benchmark | Accuracy | Correct/Total | Notes |
|-----------|----------|---------------|-------|
| MMLU | 0.2303 | 3234/14042 | Near random (25% for 4-choice) |
| GSM8K | 0.0053 | 7/1319 | Essentially zero |
| ARC-Challenge | 0.2304 | 270/1172 | Near random (25% for 4-choice) |
| HumanEval pass@1 | 0.2317 | 38/164 | Decent for base model |

## Contamination Signals
**Not computed in this run.** Only benchmark accuracy was evaluated. The 4 contamination signals (S1-S4) were not part of the evaluation pipeline for this experiment.

## SFT Tax Quantification: Base vs d000 SFT (1.5B)

Comparison with `exp_001_eval_15B_d000_s123_aligned` (Qwen2.5-1.5B, 0% contamination SFT, aligned MC format):

| Benchmark | Base (this) | d000 SFT | Δ Absolute | Δ Relative |
|-----------|-------------|----------|------------|------------|
| MMLU | 0.2303 | 0.5855 | **+0.3552** | +154% |
| GSM8K | 0.0053 | 0.6535 | **+0.6482** | +12,230% |
| ARC-Challenge | 0.2304 | 0.7577 | **+0.5273** | +229% |
| HumanEval | 0.2317 | 0.1707 | **-0.0610** | -26% |

## 3-Regime Comparison (1.5B scale): Base → SFT → Contaminated

| Benchmark | Base | d000 SFT | d100 (100% contam) | SFT effect | Contam effect |
|-----------|------|----------|---------------------|------------|---------------|
| MMLU | 0.2303 | 0.5855 | 0.5956 | +0.3552 | +0.0101 |
| GSM8K | 0.0053 | 0.6535 | 0.6444 | +0.6482 | -0.0091 |
| ARC-Challenge | 0.2304 | 0.7577 | 0.7816 | +0.5273 | +0.0239 |
| HumanEval | 0.2317 | 0.1707 | 0.2805 | -0.0610 | +0.1098 |

## Key Findings

### 1. Base model at random chance on MC benchmarks
All MMLU predictions are "A" — the base model does not understand the multiple-choice format. The ~23% accuracy reflects the prior distribution of "A" being the correct answer across MMLU items.

### 2. SFT is the dominant capability driver
SFT accounts for the overwhelming majority of performance gains: +35.5pp on MMLU, +64.8pp on GSM8K, +52.7pp on ARC. Contamination effects are tiny in comparison (< 2.5pp on most benchmarks).

### 3. HumanEval anomaly: SFT hurts code generation
Base model outperforms clean SFT (23.2% vs 17.1%). Likely explanation: SFT on non-code instruction data shifts the model's generation distribution away from code completion. Contamination with HumanEval items restores performance (28.1%).

### 4. Contamination signal is dwarfed by SFT signal
The 3-regime comparison shows that for 1.5B scale, the "contamination effect" (d000→d100) is 1-2 orders of magnitude smaller than the "SFT effect" (base→d000) on MMLU/GSM8K/ARC. Only HumanEval shows a meaningful contamination effect (+11pp), largely because SFT itself was detrimental.

## Caveats
1. **MC format mismatch**: This base eval used default format; d000/d100 used `--mc-format aligned`. For a base model that always predicts "A", this likely doesn't affect MC scores, but GSM8K/HumanEval generation could differ.
2. **No contamination signals**: S1-S4 were not computed. A separate contamination signal extraction run would be needed.
3. **Single seed**: Base model eval has no seed variation (pretrained weights are fixed); SFT comparisons use s123.
