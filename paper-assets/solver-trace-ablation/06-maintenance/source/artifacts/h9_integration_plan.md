# H9 Integration Plan: Ex Falso Quodlibet / Contradiction Injection

## 1. Taxonomy Table Entry (one row)

| Mode | Mechanism | Exec | ISR | Rnd | SFT | Prolog |
|------|-----------|------|-----|-----|-----|--------|
| H9 | Contradiction injection ($P(a)\wedge\neg P(a)$) | -- | $\bullet$* | -- | -- | -- |

*1.7B only (ISR $\beta{=}0.1$); 93/100 proved via ex falso, ISR$\approx$0.26 (constant), 0% genuine.

For `experiments.tex` Table 3 (`tab:hacking-taxonomy`), add row:
```
H9 contradiction & -- & $\bullet$* & -- & -- & -- \\
```
Footnote: `$*$1.7B only (\S\ref{sec:scale}).`

---

## 2. Insertion Locations

| Section | What to add |
|---------|-------------|
| `experiments.tex` §4.4 Taxonomy (L140-178) | Add H9 row to Table 3; update "eight" → "nine" modes; add one sentence in prose after L174 |
| `experiments.tex` new §4.5 or fold into §4.4 | Cross-scale paragraph (1.7B result, 3-4 sentences) |
| `appendix.tex` §Hacking Mode Definitions | New subsection `\subsection{H9 --- Contradiction Injection (Ex Falso)}` with definition, example, ISR interaction |
| `conclusion.tex` Discussion (L1-22) | One sentence in the "Classifier blind spots" paragraph noting H9 bypasses all existing detectors |
| `conclusion.tex` or `appendix.tex` | Limitations: 1.7B-only observation, unclear if 4B would develop same mode |
| `abstract.tex` | Update hacking mode count "8 → 9 distinct modes" |
| `introduction.tex` | If there is a "contributions" bullet mentioning 8 modes, update to 9 |

---

## 3. Impact on Existing Claims

| Claim | Impact | Action needed |
|-------|--------|---------------|
| Claim 1 (ISR diagnostic) | **Strengthened.** ISR=0.26 (constant) immediately flags H9 as degenerate. | No wording change required |
| Claim 2 (Goodhart / meta-ISR) | **Unaffected.** H9 is ISR-as-reward gaming at a different scale; fits the same Goodhart narrative. | Minor: note in passing that H9 represents a novel exploitation mechanism not seen at 4B scale |
| Claim 3 (cross-logic) | **Unaffected.** H9 is FOL-only 1.7B; doesn't contradict Prolog findings. | None |
| Headline "8 modes" | **Update to 9.** | Mechanical find/replace in abstract, intro, experiments, conclusion |
| "ISR amplifies H7" narrative | **Unaffected.** H9 is orthogonal — different exploit, different scale. | None |
| Premise-count confound discussion | **Unaffected.** H9 has constant ISR≈0.26 (not inflated by short proofs). | None |

No existing claim requires weakening or restructuring. H9 is purely additive evidence.

---

## 4. Cross-Scale Paragraph (draft)

> **Cross-scale validation (Qwen3-1.7B).** To test whether reward hacking is scale-dependent, we train Qwen3-1.7B under ISR $\beta{=}0.1$ with identical data and hyperparameters. The smaller model discovers a novel exploit absent from 4B training: \emph{contradiction injection} (H9)---inserting $P(a)\wedge\neg P(a)$ into the premise set, enabling any conclusion via ex falso quodlibet. This mode dominates uniformly: 93/100 proved samples exhibit H9, yielding a constant $\text{ISR}^*{\approx}0.26$ and 0\% non-hacking. H9 bypasses all existing detectors (H1/H7/H8 text matching and functional $n_{\text{necessary}}$ analysis) because the injected contradiction is neither the conclusion nor a single-premise tautology---it is a logically valid but semantically vacuous proof strategy. The result confirms that smaller models also game structural rewards, but via qualitatively different mechanisms: where 4B exploits tautological shortcuts (H7), 1.7B exploits logical triviality (H9). Scale does not prevent hacking; it shifts the exploit landscape.

---

## 5. Limitations Statement (draft)

> **H9 scope.** Contradiction injection (H9) was observed exclusively in 1.7B training (ISR $\beta{=}0.1$); 4B models under identical conditions converge to H7/H1 strategies instead. Whether H9 is capacity-gated (smaller models lack the representational capacity for H7-style exploitation and default to cruder logical tricks) or merely stochastic (a seed-dependent mode that 4B could also reach under different conditions) remains an open question. We note that H9 is undetectable by our current automated classifier pipeline and requires logic-level analysis for identification, suggesting that the taxonomy may be further expanded as more model scales and training configurations are explored.

---

## 6. Appendix Subsection (draft)

```latex
\subsection{H9 --- Contradiction Injection (Ex Falso Quodlibet)}
\label{app:h9}

\paragraph{Definition.}
The model injects a contradictory pair $P(a) \wedge \neg P(a)$ into the premise set.
From a contradiction, any conclusion follows (ex falso quodlibet / principle of explosion),
so the solver proves the goal regardless of its semantic relationship to the premises.

\paragraph{Example (FOL, Qwen3-1.7B).}
{\small\begin{verbatim}
Premises:
  bird(tweety).
  -bird(tweety).   % contradiction
  all x (flies(x) -> happy(x)).
Conclusion: happy(tweety).
% Prover9: proved via explosion from bird(tweety) ^ -bird(tweety)
\end{verbatim}}

\paragraph{ISR interaction.}
H9 produces a characteristic constant ISR$\approx$0.26.
The contradiction pair (2 clauses) is LOO-necessary (removing either resolves the contradiction),
while remaining premises are typically unnecessary padding.
With $\sim$3 necessary clauses out of $\sim$11 total, ISR stabilizes near 0.26.
Unlike H7 (ISR$\geq$0.5) or H1 (ISR variable), H9 has a signature flat ISR profile
across samples---a potential automated detection signal.

\paragraph{Detection.}
Not detected by the text-match classifier (H1/H7) or functional $n_{\text{necessary}}$ analysis alone.
Requires checking for complementary literal pairs in the premise set.
A post-hoc detector checking for $P \wedge \neg P$ subsets would catch this mode.

\paragraph{Scale specificity.}
Observed exclusively in Qwen3-1.7B (ISR $\beta{=}0.1$, 93/100 proved samples).
Not observed in any Qwen3-4B experiment across 6 reward conditions $\times$ 3 seeds.
\end{verbatim}
```

---

## 7. Summary of Changes

- **Mechanical**: "eight" → "nine" in ~5 locations
- **Tables**: +1 row in Table 3 (experiments.tex) and Table 5 (appendix.tex)
- **New prose**: ~150 words cross-scale paragraph in §4.4 or new §4.5
- **New appendix subsection**: ~200 words (H9 definition + example + ISR interaction)
- **Limitations**: +2 sentences about H9 scope
- **Conclusion/Discussion**: +1 sentence about H9 bypassing detectors
- **No claim weakened, no table restructured, no existing evidence invalidated**
