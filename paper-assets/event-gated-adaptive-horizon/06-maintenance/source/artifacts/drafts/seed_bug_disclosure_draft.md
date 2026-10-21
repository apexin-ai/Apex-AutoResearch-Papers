# Seed Bug Disclosure — Draft for Limitations Section

**Placement**: `paper/sections/limitations.md`, as a new `\paragraph{}` after "Limited seed count."

---

## Draft (LaTeX)

```latex
\paragraph{Replay sampling seed.}
In experiments prior to the final round, the replay buffer's episode sampling routine used a fixed seed (0) rather than the per-run random seed. Model weight initialization, environment stochasticity, and all other randomized components correctly received the per-run seed. Because the shared replay ordering affects both experimental and control conditions identically, between-group effect size estimates remain unbiased. However, within-group variance across seeds may be slightly underestimated relative to fully independent sampling, as one source of run-to-run stochasticity was inadvertently removed. The final seed (seed 3, exp\_008d) uses the corrected implementation with a fully independent replay sampling sequence.
```

---

## Notes

- 5 sentences, ~100 words
- Honest disclosure without excessive self-flagellation
- Key logic: shared nuisance → between-group contrast unbiased; within-group variance potentially deflated
- Positioned after "Limited seed count" because it qualifies the same concern (seed-level independence)
- No dashes used
