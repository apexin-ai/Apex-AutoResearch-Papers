# W2 Distribution Matching Validation

## Hypothesis
If adaptive weighting's FineWeb PPL improvement is genuine quality gain, it should also show lower PPL on non-FineWeb eval sets.

## Results

| Eval Set | Adaptive PPL | Uniform PPL | Δ (A-U) | Eval Tokens |
|---|---|---|---|---|
| FineWeb holdout | **17.65** | 17.69 | -0.04 | 4,077,068 |
| OpenWebText | 18.42 | **18.37** | +0.06 | 6,767,242 |
| Wikipedia | 15.47 | **15.34** | +0.14 | 27,000,339 |

## Detailed Numbers

### FineWeb holdout (original eval)
- Adaptive: loss=2.8709, PPL=17.65, tokens=4,077,068, time=123.5s
- Uniform: loss=2.8733, PPL=17.69, tokens=4,077,068, time=134.0s

### OpenWebText (web crawl, non-FineWeb)
- Adaptive: loss=2.9136, PPL=18.42, tokens=6,767,242, time=148.1s
- Uniform: loss=2.9105, PPL=18.37, tokens=6,767,242, time=146.9s

### Wikipedia (encyclopedic text)
- Adaptive: loss=2.7391, PPL=15.47, tokens=27,000,339, time=390.1s
- Uniform: loss=2.7302, PPL=15.34, tokens=27,000,339, time=385.2s

## Conclusion
NEGATIVE: Adaptive weighting advantage is FineWeb-specific. On independent eval sets (OpenWebText, Wikipedia), uniform weighting performs equal or better. This is consistent with the reviewer's concern about tautological distribution matching.

## Setup
- Models: Qwen 0.6B, adaptive_fix_seed42 vs qwen06b_uniform_seed42_v2
- Server: westd-41312
- Eval params: max_docs=5000, max_length=2048
- Data sources: FineWeb eval holdout, Skylion007/openwebtext, wikimedia/wikipedia 20231101.en
