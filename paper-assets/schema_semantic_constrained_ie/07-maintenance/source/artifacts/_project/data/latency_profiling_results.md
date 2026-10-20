# Latency Profiling Results — OntoCoDec Constrained Decoding

## Setup
- Model: Qwen3-8B-LoRA-SciERC merged checkpoint
- GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (98GB)
- Dataset: SciERC test set, 100 samples
- Controlled benchmark: model loaded once, 5-sample warmup, all modes run sequentially in same process
- Timing: `torch.cuda.synchronize()` + `time.perf_counter()` for accurate measurement

## Results

| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |
|------|---|----------|---------|---------|---------|----------|-------|
| unconstrained | 100 | 2.594 | 2.359 | 5.985 | 8.194 | — | 57.7 |
| grammar_only | 100 | 2.637 | 2.397 | 6.099 | 8.346 | +1.7% | 56.7 |
| semantic_only | 100 | 2.625 | 2.379 | 6.080 | 8.335 | +1.2% | 57.0 |
| full_s1 | 100 | 2.655 | 2.416 | 6.162 | 8.449 | +2.3% | 56.4 |

## Statistical Significance (paired t-test)
- unconstrained vs grammar_only: +0.044s (+1.7%), t=-10.34, p<0.0001
- unconstrained vs semantic_only: +0.032s (+1.2%), t=-11.04, p<0.0001
- unconstrained vs full_s1: +0.061s (+2.3%), t=-12.84, p<0.0001

## Conclusion
Constrained decoding (full_s1 = grammar + semantic) adds **2.3% latency overhead** (61ms per sample on average). This is statistically significant but practically negligible. The grammar layer contributes most of the overhead (+1.7%), while the semantic layer adds only +1.2%. The combined overhead is sub-additive.