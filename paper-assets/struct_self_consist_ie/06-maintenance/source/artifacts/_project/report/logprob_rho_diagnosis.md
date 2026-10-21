See full JSON at server: /root/autodl-tmp/struct_self_consist_ie/output/logprob_diagnosis/diagnosis.json

SUMMARY:
Total NER logprob rho gap: 0.314 - 0.140 = 0.174

Factor decomposition:
(a) Instance subset (200 vs 529): +0.039 (22% of gap) — MINOR
(b) Temperature (T=0.7 vs T=1.0): ~+0.129 (74% of gap) — DOMINANT ROOT CAUSE
(c) N samples (16 vs 8):          +0.007 (4% of gap)  — NEGLIGIBLE
(d) Normalization:                 IDENTICAL (both per-token mean) — RULED OUT

Key evidence:
- Same 200 instances, exp-001 (N=16,T=0.7) rho=0.314 vs exp-012 (N=8,T=1.0) rho=0.179. Delta=+0.135
- N=16 vs N=8 (subsampled within exp-001 at T=0.7): delta=+0.007 only
- Therefore T effect ≈ 0.135 - 0.007 = 0.129
- T=1.0 widens logprob spread (range 0.151 vs 0.098 at T=0.7), adding noise that dilutes F1 correlation

Greedy output mismatch: 12.5% of instances have different greedy entities due to guided decoding in exp-012.
This is a secondary confound but does NOT explain the bulk of the gap.