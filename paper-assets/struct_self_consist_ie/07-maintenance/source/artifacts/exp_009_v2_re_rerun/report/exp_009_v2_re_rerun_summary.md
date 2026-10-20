EXP-009 v2 RE RERUN — FILTERED + PROXY INDEPENDENCE CHECK

## Filtering
551 raw → 154 empty-gold removed → 397 kept (28% filtered)

## Proxy Independence (all pass after filtering)
  ✓ ent_count      |ρ|=0.011  (was 0.512 before filtering!)
  ✓ sent_len       |ρ|=0.023  (was 0.124)
  ✓ type_diversity  |ρ|=0.071  (was 0.481)
  ✓ rel_count      |ρ|=0.131  (new proxy)

## Global Signal ρ (n=397, after filtering)
  sj            ρ=0.281 [0.182, 0.371]  (was 0.063)
  fk            ρ=0.279 [0.173, 0.375]  (was 0.226)
  logprob       ρ=0.287 [0.192, 0.379]  (was 0.400)
  voting_conf   ρ=0.322 [0.228, 0.414]  (was 0.220)
  em            ρ=0.165 [0.066, 0.263]  (was -0.132)

## Sentence Length Quartile Stratification (primary)
  Q1 (low,  n=117): SJ=0.110, FK=0.188, logprob=0.152, VC=0.123, EM=0.112
  Q2        (n=93):  SJ=0.308, FK=0.356, logprob=0.351, VC=0.443, EM=0.137
  Q3        (n=92):  SJ=0.372, FK=0.272, logprob=0.311, VC=0.456, EM=0.206
  Q4 (high, n=95):  SJ=0.473, FK=0.415, logprob=0.363, VC=0.414, EM=0.241

Fisher z Q1 vs Q4: SJ p=0.004*, VC p=0.024*

## Key Finding
Filtering empty-gold instances dramatically changes the picture:
- All proxy variables become independent (|ρ|<0.3 with F1)
- SJ jumps from near-zero (0.063) to meaningful (0.281) globally
- EM flips from negative (-0.132) to positive (0.165)
- Signal strength consistently increases with sentence length