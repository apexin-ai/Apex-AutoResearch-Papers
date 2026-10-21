# Cheetah Integration Template (024 completion)

## 1. Table 1 Appendix Row (after 021 row)

```latex
024 & Cheetah Run & --- & ON & 8 & [EVAL] @105K & [NVE]$\times$ & [OUTCOME] \\
```

- dt_emb = `---` (removed, $d{=}0$)
- Fill `[EVAL]` with final eval return, `[NVE]` with peak NVE ratio
- Expected outcome: Healthy (if no collapse confirms dt_emb is necessary for CIVO)
- Row should NOT have `\rowcolor{gray!15}` (follows 019b which now has gray)

## 2. F7 Paragraph: Cheetah Causal Triangle Summary

Insert after the existing Cheetah cross-env paragraph in Appendix F7 (or equivalent causal analysis section):

```
The Cheetah Run experiments complete a causal triangle isolating dt_emb as the
necessary trigger for CIVO. Baseline runs (023a/023b) with standard dt_emb
achieve healthy returns (624.7/520.3), confirming the environment supports
stable learning. Run 010b, which uses the same trained dt_emb but triggers
CIVO conditions, collapses to 51.7 with NVE peaking at 8.27x. Run 024
removes dt_emb entirely (d=0) while keeping all other hyperparameters
identical to 010b; if 024 remains healthy, it establishes that trained dt_emb
is necessary for CIVO onset in Cheetah Run. Run 021 further shows that
Full-SGS can recover performance (221.5) even with trained dt_emb present,
confirming SGS as an effective mitigation that does not require removing the
embedding.
```

## 3. F2 Paragraph: Cross-Environment Evidence

Candidate sentence to add to the cross-environment validation discussion:

```
Cheetah Run provides the strongest causal evidence: three matched
configurations (baseline healthy, dt_emb-triggered collapse, no-dt_emb
control) confirm that CIVO generalizes beyond Walker Walk and that the
dt_emb pathway is the consistent necessary condition across environments.
```

## Notes

- All text above avoids em-dashes per style guidelines
- Update NVE values from actual 024 W&B metrics before inserting
- If 024 unexpectedly collapses, the causal narrative needs revision;
  consult the CIVO trigger conditions analysis before writing
