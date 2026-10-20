# κ Contingency Replacement Text

Pre-written replacement text for 3 critical positions × 3 scenarios.
When κ results arrive, pick the matching scenario and copy-paste.

---

## Position 1: Abstract (abstract.tex L2)

### Current
```
human $\kappa = 0.15$, collapsed $0.34$--$0.52$
```

### Scenario A (κ ≥ 0.40)
```
human $\kappa = [NEW]$ (improved guidelines; prior round $0.15$)
```

### Scenario B (κ = 0.25–0.39)
```
human $\kappa = [NEW]$, collapsed $[NEW_COLLAPSED]$
```

### Scenario C (κ < 0.25)
```
human $\kappa = [NEW]$, collapsed $[NEW_COLLAPSED]$
```
(Same format as B; claim downgrade handled in "provides initial evidence" → "provides suggestive evidence")

---

## Position 2: Abstract claim strength (abstract.tex L2)

### Current
```
provides initial evidence that the taxonomy functions as a diagnostic instrument
```

### Scenario A (κ ≥ 0.40)
```
provides evidence that the taxonomy functions as a diagnostic instrument
```

### Scenario B (κ = 0.25–0.39)
```
provides initial evidence that the taxonomy functions as a diagnostic instrument
```
(No change)

### Scenario C (κ < 0.25)
```
provides suggestive evidence that the taxonomy may function as a diagnostic instrument
```

---

## Position 3: Analysis §6 intro (analysis.tex L13)

### Current
```
Human mechanism coding yields $\kappa = 0.15$, rising to $0.34$--$0.52$ after collapsing the spurious-compliance/structural-misparse boundary (Appendix~\ref{app:human_validation}); we treat $V = 0.45$ as an upper bound.
```

### Scenario A (κ ≥ 0.40)
```
Human mechanism coding yields $\kappa = [NEW]$ (improved guidelines; prior round $0.15$ before resolving the spurious-compliance/structural-misparse boundary, Appendix~\ref{app:human_validation}); we treat $V = 0.45$ as an upper bound pending larger-sample human validation.
```

### Scenario B (κ = 0.25–0.39)
```
Human mechanism coding yields $\kappa = [NEW]$ (improved guidelines; prior round $0.15$), rising to $[NEW_COLLAPSED]$ after collapsing the spurious-compliance/structural-misparse boundary---both describe policy misinterpretation differing only in surface compliance (Appendix~\ref{app:human_validation}); we treat $V = 0.45$ as an upper bound.
```

### Scenario C (κ < 0.25)
```
Human mechanism coding yields $\kappa = [NEW]$ (improved guidelines; prior round $0.15$), rising to $[NEW_COLLAPSED]$ after collapsing the spurious-compliance/structural-misparse boundary (Appendix~\ref{app:human_validation}), confirming that fine-grained mechanism distinctions approach the limits of human discriminability for this task; we treat $V = 0.45$ as an upper bound.
```

---

## Position 4: Limitations (limitations.tex L4)

### Current
```
human $\kappa = 0.15$, rising to $0.34$--$0.52$ after collapsing the spurious-compliance/structural-misparse boundary
```

### Scenario A (κ ≥ 0.40)
```
human $\kappa = [NEW]$ (improved guidelines; prior round $0.15$)
```

### Scenario B (κ = 0.25–0.39)
```
human $\kappa = [NEW]$ (improved from $0.15$), rising to $[NEW_COLLAPSED]$ after collapsing the spurious-compliance/structural-misparse boundary
```

### Scenario C (κ < 0.25)
```
human $\kappa = [NEW]$ (improved from $0.15$; improved guidelines raised agreement but fine-grained mechanism distinctions remain difficult for human annotators), rising to $[NEW_COLLAPSED]$ after collapsing the spurious-compliance/structural-misparse boundary
```

---

## Remaining 4 positions (mechanical number replacement)

These require only swapping `0.15` → `[NEW]` and `0.34--0.52` → `[NEW_COLLAPSED]`:

5. **Intro** (intro.tex): Find `\kappa = 0.34--0.52` or `\kappa = 0.15` and replace
6. **Figure caption** (analysis.tex L7): `human collapsed $\kappa = 0.34$--$0.52$` → scenario-dependent
7. **Appendix human_validation** (appendix.tex ~L773): Update raw numbers + add new-round comparison paragraph
8. **Appendix human_validation table**: Add new annotation round data row

---

## Decision matrix

| κ result | Claim strength | "upper bound" rationale | Collapsed-κ role | Action time |
|----------|---------------|------------------------|-----------------|-------------|
| ≥ 0.40   | "evidence"     | sample size            | supplementary   | ~15 min     |
| 0.25–0.39| "initial evidence" | low κ (unchanged)   | primary defense | ~10 min     |
| < 0.25   | "suggestive evidence...may" | low κ (unchanged) | last defense | ~20 min     |
