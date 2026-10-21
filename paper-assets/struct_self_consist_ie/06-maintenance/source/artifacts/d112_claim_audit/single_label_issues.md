# "Single" Label Issues

**Background**: Discovery that Table 2's "Single" row may actually be T=0 greedy decoding, mislabeled as "one T=1.0 draw."

---

## Evidence For/Against "Single = T=0 Greedy"

### Arguments supporting the mislabeling theory:
1. Provenance c013 lists `greedy=0.644` — very close to paper's `Single=0.645`
2. The provenance selection data (c011) has no explicit "single" field — only `greedy: 0.644, logprob: 0.650, sj: 0.645...`
3. Provenance c011 computes LP gain as "+0.6pp" — this is `0.650-0.644=+0.6pp`, treating the 0.644 value as the single-sample baseline

### Arguments against the mislabeling theory:
1. Table 2 shows `Single: 0.645 ± 0.001` — the ±0.001 variance implies stochasticity, inconsistent with deterministic T=0
2. Paper has BOTH `Greedy (T=0) = 0.663` and `Single = 0.645` as separate rows — if both are T=0, they should be identical
3. Method.tex L61 explicitly defines: "single-sample (one T=1.0 draw, not argmax decoding; labeled 'Single' in tables)"
4. Table 2 footnote: "‡Single: one T=1.0 draw (expected performance of a single sample)"

### Possible resolution:
The numbers suggest the pipeline has TWO different evaluation protocols both labeled as "greedy/T=0":
- `Greedy (T=0)` in Table 2 (F1=0.663): from one experiment/eval set
- `greedy` in provenance c013 (F1=0.644): from a different experiment (exp_016_rerun_1024_bootstrap)

The 1.9pp gap between them (0.663 vs 0.644) is too large to be noise. Likely explanations:
- Different instance filtering (full set vs gold-filtered)
- Different seed
- One is 2-seed averaged, the other single-seed

If "Single" (0.645) ≈ provenance "greedy" (0.644), the issue may be that the provenance experiment computed its "greedy" baseline differently from Table 2's "Greedy" row.

---

## Affected Claims (If Single IS T=0 Greedy)

### Category A: "Over single-sample" comparisons become "over greedy"

| Location | Claim | Current Interpretation | If Single=Greedy |
|----------|-------|----------------------|------------------|
| experiments.tex:L89 | "LP achieves 0.647 (Δ=+0.2pp)" | LP beats single T=1.0 draw | LP beats greedy by 0.2pp → greedy no longer best |
| experiments.tex:L89 | "oracle reveals 13.3pp headroom above single-sample" | Headroom above T=1.0 draw | Headroom above greedy |
| experiments.tex:L93 | "Greedy (T=0) surpasses all N=8 selection strategies" | Greedy > LP > Single | If Single=Greedy, contradiction: "Greedy"(0.663) ≠ "Single"(0.645) |
| introduction.tex:L35 | "Greedy decoding (F1=0.663) surpasses all N=8 selection strategies (best: 0.647) despite 13-18pp oracle headroom" | Clean claim | The "13-18pp" is now headroom over greedy, not over a stochastic sample |
| discussion.tex:L43 | "All three fail to improve over single-sample (best: +0.1pp)" | Combinations vs T=1.0 | Combinations vs greedy |

### Category B: The "correlation-selection gap" framing

The gap is defined as: "quality estimation works (ρ=0.38), but selection fails to beat single-sample."
- If single-sample IS greedy, then the gap is: "QE works, but selection fails to beat greedy."
- This actually STRENGTHENS the argument (it's even harder to beat greedy than a random T=1.0 draw).
- BUT: it removes the claim that "multi-sample is worse than the trivial single-sample baseline" because the baseline is no longer trivial (it's the best possible deterministic output).

### Category C: Definition contradictions

| Location | Text | Issue |
|----------|------|-------|
| method.tex:L61 | "single-sample (one T=1.0 draw, not argmax decoding; labeled 'Single' in tables)" | Definition explicitly says NOT argmax |
| experiments.tex:L60-61 | "‡Single: one T=1.0 draw (expected performance of a single sample)" | Footnote repeats the T=1.0 claim |
| experiments.tex:L78 | `Single‡ & 0.645 ± 0.001` | ±0.001 would be expected for T=1.0 across seeds |

### Category D: If there are TWO greedy values in the paper

| Row | F1 | Claimed Identity | Actual |
|-----|-----|-----------------|--------|
| Greedy (T=0)† | 0.663 | argmax decoding | ??? |
| Single‡ | 0.645±0.001 | one T=1.0 draw | ??? |

If both are T=0, they MUST give identical F1 (deterministic). The 1.8pp difference proves they cannot both be T=0 under the same evaluation protocol. Therefore EITHER:
1. Single IS T=1.0 (as stated) — no mislabeling, just confusing provenance
2. They use different eval sets (e.g., Greedy on n=551, Single on n=529 gold-filtered)
3. One is averaged over seeds differently

---

## Recommended Investigation

1. **Check the experiment code**: Verify the temperature parameter used when computing the "single" baseline in exp_016_signal_ensemble
2. **Check instance counts**: If Greedy uses n=551 (full) and Single uses n=529 (gold-filtered), the 1.8pp difference could be explained by the 22 excluded instances
3. **Reconcile provenance "greedy=0.644" with paper "Greedy=0.663"**: Identify which experiment/filtering produces each
4. **If Single is confirmed T=1.0**: Update provenance to stop conflating "single" with "greedy"
5. **If Single is confirmed T=0**: 
   - Correct method.tex definition
   - Correct table footnotes
   - Reframe all "vs single-sample" claims
   - Address why Greedy(0.663)≠Single(0.645) if both are T=0

---

## Impact Assessment

| Scenario | Impact on Paper Claims | Severity |
|----------|----------------------|----------|
| Single is actually T=1.0 (no bug) | No impact; provenance needs cleanup only | Low |
| Single is T=0 but from different eval set | Need to clarify eval protocol; minor text fixes | Medium |
| Single is truly mislabeled T=0 with same eval set | Major rewrite of framing; "Greedy=0.663" row becomes unexplained | **Critical** |

The ±0.001 variance in the Single row and the 1.8pp gap from Greedy argue strongly that **Single is genuinely T=1.0** and the confusion stems from provenance using a different experiment's "greedy" value (0.644) that happens to be close to Single (0.645). The real issue is the provenance-paper misalignment documented in the main audit report.
