# LP × VC Combination Selection Analysis (D108)

## Key Results

### SciERC NER (N=551, 8 samples)
- LP-only: 0.6602, Greedy: 0.6633, Oracle: 0.7775
- Best combo (Strategy 2, α=2.0): **0.6669** (+0.0067 vs LP, +0.0036 vs greedy)
- Strategy 3 (ε=0.1, LP+VC tied handling): **0.6675** (+0.0073 vs LP)

### CoNLL NER (N=3453, 16 samples)
- LP-only: 0.8904, Greedy: 0.9067, Oracle: 0.9544
- Best combo (Strategy 2, α=2.0): **0.9063** (+0.0159 vs LP, -0.0004 vs greedy)
- Strategy 3 (ε=0.1, LP+VC): 0.8986 (+0.0082 vs LP)

## Takeaways
1. VC-gated LP (Strategy 1) hurts — replacing LP with random on low-VC instances loses more than it gains
2. Per-sample VC-weighted LP (Strategy 2) consistently helps, especially on CoNLL where α=2.0 nearly matches greedy
3. Tied handling (Strategy 3) shows VC helps resolve LP ties, but 60-84% of instances are "tied" at ε=0.05-0.1, confirming LP's discrimination weakness
4. Oracle gap remains huge (0.7775 / 0.9544), indicating room for better signals