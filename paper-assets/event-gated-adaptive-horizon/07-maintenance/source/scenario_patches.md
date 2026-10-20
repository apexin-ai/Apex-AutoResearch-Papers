# Scenario Patches for exp_041 / exp_042 (Data Lockdown 5/25)

## Decision Matrix

|  | exp_042 ✅ (no CIVO, 90%) | exp_042 ❌ (CIVO, 10%) |
|--|--|--|
| **exp_041 ✅ (eval>400, 67%)** | Version A (60%) — current + minor | Version C (7%) — C2 rewrite |
| **exp_041 ❌ (collapse, 33%)** | Version B (30%) — Prevention weakened | Version D (3%) — both |

Current state: Wide dual Walker = 3 seeds (exp_032 s1,s2; exp_038 s2), 3/3 CIVO prevention, 1/3 non-CIVO collapse.
With exp_041: 4 Walker seeds total.

---

## VERSION A (60%) — Current text + minor number updates

### Changes needed
- Table 2: `Wide dual (min) & 5 & 4/5$^\|$ & 80\%` (was 4, 3/4, 75%)
- Footnote: `$^\|$Walker 4/4 ($\nve \leq 1.4\times$; 1/4 non-CIVO eval collapse), Cheetah 0/1.`
- §4.6: "3/3 CIVO prevention" → "4/4 CIVO prevention", "1/3 collapses" → "1/4 collapses"
- Conclusion: "3/4 prevention" → "4/5 prevention"
- Practitioner guidelines: "3/4" → "4/5"
- n count: 29 → recalculate with new configs

Narrative: Unchanged. Non-CIVO collapse is "rare" (1/4 = 25%).

---

## VERSION B (30%) — exp_041 ❌ collapse, exp_042 ✅

**Core narrative shift**: Wide dual prevents CIVO universally on Walker (4/4) but 50% of seeds collapse via non-CIVO pathway. "CIVO prevention ≠ stability" becomes a major finding, not a caveat.

### §4.6 Prevention paragraph

**CURRENT:**
```latex
Prevention requires min $+$ capacity: only wide dual-critic maintains $\nve \leq 1.4\times$ (3/3 CIVO prevention), though 1/3 collapses via a non-CIVO pathway (eval $354 \to 120.9$, entropy increase). Prevention's advantage is training efficiency (${\sim}40$K steps saved), not final performance. Cross-environment transfer is limited (Appendix~\ref{sec:dual_critic_appendix}).
```

**VERSION B:**
```latex
Prevention requires min $+$ capacity: wide dual-critic maintains $\nve \leq 1.4\times$ in all Walker seeds (4/4 CIVO prevention), but 2/4 seeds collapse via a mechanistically distinct non-CIVO pathway (exp\_038: eval $354 \to 120.9$; exp\_041: eval $\placeholder{XXX} \to \placeholder{YYY}$; both with actor entropy increase), yielding 50\% performance stability. CIVO prevention eliminates one failure mode but does not address the broader vulnerability created by the trained embedding (\S\ref{sec:f6}). Cross-environment transfer is limited (Appendix~\ref{sec:dual_critic_appendix}).
```

### Table 2 update (Version B)

```latex
Arch. & Wide dual (min) & 5 & 4/5$^\|$ & 80\% \\
```
Footnote:
```latex
$^\|$Walker 4/4 CIVO prevention ($\nve \leq 1.4\times$); 2/4 non-CIVO eval collapse. Cheetah 0/1.
```

### Abstract (Version B)

**CURRENT snippet:**
```
the min operation nonetheless enables CIVO recovery, while prevention requires min $+$ increased capacity.
```

**VERSION B:**
```
the min operation enables CIVO recovery; min $+$ capacity prevents CIVO on Walker (4/4) but half of prevented seeds collapse via non-CIVO mechanisms, showing that CIVO prevention alone does not guarantee stability.
```

### Conclusion (Version B)

**CURRENT:**
```latex
In pure-imagination training, dual critics converge ($\rho > 0.999$), rendering Double Q pessimism ineffective; min $+$ capacity achieves 3/4 prevention on Walker but not cross-environment.
```

**VERSION B:**
```latex
In pure-imagination training, dual critics converge ($\rho > 0.999$), rendering Double Q pessimism ineffective; min $+$ capacity prevents CIVO on Walker (4/4) but 2/4 seeds collapse via non-CIVO mechanisms, and cross-environment transfer fails.
```

### Introduction C3 (Version B)

**CURRENT snippet:**
```latex
\item \textbf{Four-level intervention hierarchy.} ... though the min operation enables recovery through a different mechanism.
```

**VERSION B — append:**
```latex
... though the min operation enables recovery through a different mechanism. CIVO prevention does not guarantee stability: half of prevented seeds collapse via independent non-CIVO pathways.
```

### Discussion — Practitioner guidelines (Version B)

**CURRENT:**
```latex
Wide dual-critic offers the highest prevention rate (3/4, Walker only) but does not transfer cross-environment.
```

**VERSION B:**
```latex
Wide dual-critic prevents CIVO on Walker (4/5 overall, 4/4 Walker) but 50\% of prevented seeds collapse via non-CIVO mechanisms; cross-environment transfer fails.
```

### Narrative note (Version B)
The "multiple pathways" finding (F6, Item 5b) becomes stronger: the dual-critic ablation independently confirms that CIVO elimination does not close all failure modes. The trained embedding creates vulnerability through at least two independent mechanisms. This strengthens the paper's diagnostic contribution but weakens the "intervention hierarchy" as a practical guide.

---

## VERSION C (7%) — exp_041 ✅, exp_042 ❌ (frozen CIVO)

**Core narrative shift**: "Trainability triggers CIVO" weakens to "trainability amplifies CIVO." Frozen embedding can also cause CIVO under specific conditions. The causal claim shifts from "necessary condition" to "dominant factor."

### F3-F5 C2 paragraph

**CURRENT:**
```latex
Frozen embedding (015b) peaks at $1.45\times$ but self-corrects; adding a Gumbel-Softmax gate (022b, NVE $0.63\times$) confirms that \emph{trainability}, not temporal signal availability, is the necessary condition (Appendix~\ref{sec:appendix_factorial}).
```

**VERSION C:**
```latex
Frozen embedding shows heterogeneous results: 015b peaks at $1.45\times$ and self-corrects, but exp\_042 reaches $\nve = \placeholder{X.XX}\times$ [CIVO-positive], indicating that trainability is the \emph{dominant} but not strictly necessary factor. The Gumbel-Softmax gate (022b, NVE $0.63\times$) prevents CIVO entirely, suggesting that continuous gradient flow through the embedding---whether via training or frozen forward conditioning---modulates vulnerability (Appendix~\ref{sec:appendix_factorial}).
```

### §4.6 Prevention paragraph (Version C)
Same as Version A (minor number updates only: 4/4, 1/4).

### Abstract (Version C)

**CURRENT snippet:**
```
we identify the combination of trained temporal embedding and multi-rate data exposure as the causal factor
```

**VERSION C:**
```
we identify trained temporal embedding combined with multi-rate data exposure as the dominant factor (frozen embedding shows occasional CIVO)
```

### Conclusion (Version C)

**CURRENT:**
```latex
identifying trained $\dt$-embedding with multi-rate data exposure as the causal factor behind CIVO
```

**VERSION C:**
```latex
identifying trained $\dt$-embedding with multi-rate data exposure as the dominant factor behind CIVO (frozen embedding triggers CIVO in \placeholder{1/N} configurations)
```

### Introduction C1 (Version C)

**CURRENT:**
```latex
isolate trained $\dt$-embedding $+$ multi-rate exposure as jointly necessary (6/6 seeds, two environments, AUROC${=}0.971$).
```

**VERSION C:**
```latex
isolate trained $\dt$-embedding $+$ multi-rate exposure as the primary trigger (frozen embedding shows occasional CIVO in \placeholder{1/N} configurations; 6/6 trained seeds, two environments, AUROC${=}0.971$).
```

### Narrative note (Version C)
The "necessary condition" → "dominant factor" shift is significant for the causal claim. However, the 90% prior makes this unlikely. If it occurs, the paper's framing shifts from a clean binary (trained = CIVO, frozen = safe) to a graded picture (training greatly amplifies, freezing occasionally insufficient). The Gumbel gate (022b) becomes the clean control point. Need to check if n=29 AUROC changes with the new config.

---

## VERSION D (3%) — exp_041 ❌ + exp_042 ❌

Combine Version B (§4.6, Table 2, prevention claims) with Version C (F3-F5, causal claim).

### Unique interaction effects
- The "multiple pathways" narrative is maximally strengthened: the trained embedding creates CIVO through both trained AND frozen pathways, plus non-CIVO collapse that even CIVO prevention cannot address.
- The paper's contribution shifts from "we identified the problem and found partial solutions" to "we identified a problem that is more pervasive and harder to address than initially apparent."
- Claim strength must be downgraded across the board: "causal factor" → "dominant factor", "3/4 prevention" → "4/5 CIVO prevention but 50% instability"

### Version D section patches
- **F3-F5**: Use Version C text
- **§4.6**: Use Version B text
- **Table 2**: Use Version B numbers (4/5, 80%, 2/4 non-CIVO)
- **Abstract**: Combine both weakened claims:
```
we identify trained temporal embedding combined with multi-rate data exposure as the dominant factor (frozen embedding shows occasional CIVO); min $+$ capacity prevents CIVO on Walker (4/4) but half of prevented seeds collapse via non-CIVO mechanisms
```
- **Conclusion**: Combine:
```latex
identifying trained $\dt$-embedding with multi-rate data exposure as the dominant factor behind CIVO. In pure-imagination training, dual critics converge ($\rho > 0.999$); min $+$ capacity prevents CIVO on Walker (4/4) but 2/4 seeds collapse via non-CIVO mechanisms, and cross-environment transfer fails.
```
- **Introduction C1**: Use Version C text
- **Introduction C3**: Use Version B append

---

## Non-scenario updates (exp_040, exp_043)

These experiments produce narratively useful results regardless of outcome — only number updates needed.

### exp_040 (Cheetah dual s1)
- Updates Cheetah cross-environment count in Table 2 footnote
- If CIVO prevented: Cheetah 0/1 → 1/2 (significant improvement)
- If CIVO not prevented: Cheetah 0/1 → 0/2 (confirms limited transfer, strengthens severity-dependent framing)

### exp_043 (008f s1)
- Additional no-embedding control seed
- Updates "Embedding removed" row in Table 2: 5/5 → 6/6
- Strengthens the "embedding removal = CIVO elimination" baseline

### Global number updates (all versions)
- n=29 → n=`29+new_configs` (recalculate AUROC with new data points)
- Dual-critic n=7 → n=`7+new_dual_configs`
- "14 runs" in detector section → update count

---

## Execution plan (5/25 data lockdown)

1. Receive exp_040-043 final metrics
2. Classify exp_041 (✅ or ❌) and exp_042 (✅ or ❌) → select Version A/B/C/D
3. Apply selected version patches + exp_040/043 number updates
4. Recalculate n, AUROC (if configs added to NVE analysis)
5. Update Table 2, appendix Table, all cross-references
6. Run `check_paper_consistency` + compile
7. Submit to Reviewer
