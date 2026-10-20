# 1.4B Scale Verification — Discussion/Results Paragraph Templates

Pre-drafted LaTeX templates for 1.4B phase-diagram results. `[X/8]` marks placeholders to fill when data arrives.

---

## Template A — Positive (above-boundary cells ≥6/8)

**Placement**: §5.4 (Cross-Architecture Validation), after Table 2 discussion.

```latex
Pythia-1.4B phase-diagram replication ([X] above-boundary cells at ${\geq}6/8$) confirms that the detection boundary $\alpha_c(T) \propto T^{-1/(2\beta)}$ (Proposition~\ref{prop:phase-boundary}) generalizes beyond 410M, with $\alpha_c$ position [consistent with / shifted by $+$[Y] relative to] the 410M fit.
```

---

## Template B — Sync-dip reproduces at 1.4B (α=0.60 = 0/8)

**Placement**: Discussion, "Non-confirming cells" paragraph, after the sync-dip dissolution sentence.

```latex
The sync-dip reproduces at 1.4B ($\alpha{=}0.60$: [X/8] at $T{=}[Z]$), consistent with the replacement-ratio synchronization mechanism being scale-invariant.
```

---

## Template C — Onset high variance (α=0.50 seed-split)

**Placement**: Discussion, after "Non-confirming cells" or in §5.4.

```latex
At 1.4B, onset-boundary variance persists ($\alpha{=}0.50$: [X/8] vs [Y/8] across seeds), consistent with the 410M cross-seed range $[0, 6]/8$ at ($T{=}10$, $\alpha{=}0.50$).
```

---

## Template D — α_c scale-shift (T=15 α=0.45 fails at 1.4B)

**Placement**: Discussion, new sentence in "Non-confirming cells" or §5.4.

```latex
The detection boundary at 1.4B shifts upward ($T{=}15$, $\alpha{=}0.45$: [X/8] vs 410M 6/8), indicating that $\alpha_c$ is scale-dependent.
This is consistent with $\beta$ requiring architecture-specific calibration (Proposition~\ref{prop:phase-boundary}); a single fitted $\beta$ does not transfer across model scales without re-estimation.
```

---

## Usage Notes

- Templates are LaTeX-ready; paste directly into `.tex` files after filling `[X/8]`, `[Y]`, `[Z]` placeholders.
- Multiple templates may apply simultaneously (e.g., A+B if boundary holds but sync-dip reproduces).
- If mixed results (Director's 55% scenario), combine relevant templates; prioritize A or D for Results, B+C for Discussion.
