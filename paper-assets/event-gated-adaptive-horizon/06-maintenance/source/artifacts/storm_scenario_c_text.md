# STORM Scenario C — Pre-written Paper Text

> Scenario C: STORM baseline NOT healthy (unstable training, low eval return).
> Minimal changes — CIVO isolation not possible, current hedged language preserved.
> This is the lowest-effort scenario: keep existing text, add transparency about the attempt.

---

## 1. Limitations (conclusion.tex) — Scenario C Update

**Current text:**
> All experiments use DreamerV3 as the sole world-model architecture; whether CIVO manifests in transformer-based world models \citep{micheli2023iris} remains untested...

**Scenario C replacement (minimal edit):**

```latex
All experiments use DreamerV3 as the sole world-model architecture. A cross-architecture attempt on STORM \citep{zhang2023storm} (transformer world model, adapted to DMC proprioceptive) did not achieve stable baselines (eval $[TBD]$ at 500K steps vs.\ DreamerV3's $787.7$), precluding CIVO isolation; whether CIVO manifests in transformer-based world models remains an open question (Appendix~\ref{sec:storm_attempt}).
```

---

## 2. analysis.tex ¶4 "Implications beyond DreamerV3" — No Change

Keep current hedged text verbatim:
> Whether the specific onset boundary (6 DoF locomotion) generalizes remains open; the structural constraint does.

No modification needed. The text already does not claim cross-architecture validation.

---

## 3. analysis.tex ¶5 末句 — No Change

Keep current text:
> For transformer-based world models \citep{micheli2023iris}, whether this boundary shifts remains open.

---

## 4. Abstract — No Change

No modification. Current abstract does not claim cross-architecture results.

---

## 5. Appendix — New Section "Transformer World Model Attempt"

```latex
\subsection{Transformer World Model Attempt}
\label{sec:storm_attempt}

\looseness=-1 To test whether CIVO generalizes beyond RSSM-based dynamics, we adapted STORM \citep{zhang2023storm}---a transformer world model with discrete categorical latents and imagination-based actor-critic training---to DMC Walker Walk with proprioceptive observations. The adaptation required replacing the CNN encoder/decoder with MLP networks (24-dim input), converting discrete Atari actions to continuous 6-dim control, and implementing a TanhGaussian policy. The resulting system trains a critic entirely on model-generated rollouts, matching the closed-loop imagination structure of DreamerV3.

However, the adapted STORM baseline ($\dt{=}1$, no temporal conditioning) achieved eval return $[TBD]$ at 500K steps ($[TBD]\%$ of DreamerV3's $787.7$), with [describe instability pattern: e.g., "high variance across seeds" / "failure to learn beyond random policy" / "training divergence after N steps"]. This parallels the Quadruped and Humanoid results (\S\ref{sec:discussion}), where intrinsic baseline instability precludes CIVO isolation: any value overestimation observed under $\dt$-conditioning cannot be attributed to CIVO rather than baseline pathology.

This negative result neither confirms nor refutes CIVO's architecture generality. The baseline instability may reflect (1)~insufficient hyperparameter tuning for the proprioceptive adaptation (original STORM was validated only on Atari image inputs), (2)~the discrete categorical latent space being less suited to continuous proprioceptive observations than DreamerV3's continuous--discrete hybrid, or (3)~fundamental limitations of the transformer dynamics model at the scale tested (2-layer, 512-dim). A purpose-built transformer world model for DMC, or visual DMC experiments using STORM's native CNN encoder, would provide a cleaner test.
```

---

## Checklist Before Slot-In

- [ ] Confirm STORM baseline eval return is genuinely unhealthy (< 400 or high variance)
- [ ] Describe the specific failure pattern in the appendix text
- [ ] Replace all `[TBD]` with actual numbers
- [ ] Add `\citep{zhang2023storm}` to references.bib
- [ ] Add `\subsection` to appendix.tex
- [ ] Recompile, verify ≤ 10 main pages (appendix grows by ~0.5 page)
