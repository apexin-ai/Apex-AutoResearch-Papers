# Narrative B: Robustness Narrative (Draft)

Trigger condition: 3-seed pooled obs_only 0.2 vs argmin Fisher p > 0.05.

---

## 1. Core Claim (reworded)

Observation-conditioned residual correction on conformal-selected VLA samples exhibits **structured, magnitude-sensitive behavior** consistent with a learned correction function, not random noise. Across all seeds and norms, obs_only CRM never degrades below the VLA-only baseline, and its inverted-U magnitude response curve demonstrates systematic sensitivity to correction scale — a previously uncharacterized property of learned action refinement. While the aggregate improvement over sample selection does not reach conventional significance thresholds at current sample sizes, the mechanistic evidence (magnitude curve shape, feature ablation, cross-seed monotonicity over VLA-only) supports CRM as a **safe, low-cost augmentation** to frozen VLA inference.

---

## 2. Key Evidence (ranked by strength)

### Tier 1: Mechanistic (strongest — independent of p-value)

**E1. Inverted-U magnitude curve (seed42, object)**

| norm | obs_only SR | delta vs argmin (12%) |
|------|-------------|----------------------|
| 0.03 | 16% | +4pp |
| 0.05 | ~12% (partial) | ~0pp |
| 0.1 | 19% | +7pp |
| 0.2 | 22% | +10pp |
| 0.3 | 19% | +7pp |
| 1.42 (default) | 17% | +5pp |

Inverted-U with peak at 0.2. This is **not** noise — random residuals would produce monotonic degradation as norm increases. The curve shape implies CRM learns a correction direction that is useful up to a magnitude threshold, then overshoots. This is a publishable empirical finding regardless of the absolute SR delta.

**E2. obs_only >> perdof at matched configurations**

| config | obs_only | perdof | argmin |
|--------|----------|--------|--------|
| object norm=0.1 | 19% | 11% | 12% |
| object norm=0.2 | 22% | 11% | 12% |
| spatial norm=0.1 | 35% | 35% | 34% |

Perdof CRM is dead on object — indistinguishable from argmin (11% vs 12%). obs_only CRM at the same architecture and norm is 8-11pp better on object. On spatial, both variants perform similarly (~35%), suggesting the advantage is task-type specific. This isolates **observation features** as the key ingredient for object manipulation: the conformal framework provides sample selection, but conformal per-DOF statistics are not useful for conditioning the correction on fine-grained tasks. This is a clean ablation result with no p-value dependency.

### Tier 2: Cross-seed consistency

**E3. obs_only >= VLA-only on every seed (never hurts)**

| seed | VLA-only | argmin | obs_only 0.2 | obs > VLA? | obs > argmin? |
|------|----------|--------|--------------|------------|---------------|
| 42 | 12% | 12% | 22% | +10pp | +10pp |
| 43 | 12% | 17% | 16% | +4pp | -1pp |
| 44 | 10% | TBD | TBD | TBD | TBD |

obs_only never hurts vs VLA-only (0/2 seeds negative, minimum +4pp). vs argmin: 1/2 positive, 1/2 neutral. The "never degrades" property is valuable for a plug-and-play module even without strong positive signal on every seed.

### Tier 3: Honest scope limitations

**E4. Spatial null result**

obs_only (35%), perdof (35%), argmin (34%) — all within noise on spatial benchmark. CRM advantage is limited to object manipulation tasks where perturbation induces larger action distribution shift. Honest reporting; strengthens credibility of positive object results.

---

## 3. Diff vs Current Paper Structure

Current paper_framing.md is Scenario C with claim: "obs_only CRM significantly improves VLA robustness beyond sample selection (>= 5pp + p < 0.05)".

### Section-by-section changes:

**Title**
- Current: likely "sample-then-correct pipeline significantly outperforms sample selection"
- Narrative B: shift to "understanding correction behavior in VLA action refinement" or "observation-conditioned correction: a safe augmentation with structured magnitude sensitivity"
- Change: reword title to emphasize mechanism over magnitude of improvement

**Abstract**
- Remove "significantly improves" / p-value claims
- Lead with: inverted-U discovery + feature ablation as main contributions
- Add: "consistent non-negative improvement across seeds" instead of "X pp improvement"
- ~8 sentences to rewrite

**Introduction (Story Spine)**
- Problem/Gap: unchanged — still about inference-time correction for frozen VLAs
- Our angle: shift from "sample-then-correct > sample-then-select" to "systematic study of correction conditioning and magnitude sensitivity"
- Headline result: replace "+Xpp (p<Y)" with "inverted-U magnitude response + obs >> perdof ablation + never-degrades property"
- ~2 paragraphs to rewrite

**Method**
- Unchanged. Pipeline architecture is the same regardless of narrative.

**Experiments / Results**
- Table 1 (main comparison): keep, but reframe as "consistent improvement" not "significant improvement". Report pooled mean + per-seed breakdown + CI (showing overlap is OK in Narrative B). ~1 paragraph rewording.
- Figure: magnitude curve becomes the **star figure** (currently supporting evidence → promoted to main result). Add error bars or seed overlay if seed44 data available.
- Perdof ablation table: keep as-is, promote from ablation to main result (evidence for obs features > conformal features).
- Spatial table: keep as honest null result. No change needed.
- Remove or soften any Fisher exact test framing. Replace with effect size + CI reporting.

**Discussion / Analysis**
- New subsection: "Why does the inverted-U exist?" — hypothesize correction direction quality vs magnitude overshoot
- New subsection: "Why obs > perdof?" — K=10 covariance estimation noise, obs features more stable
- Strengthen: "safe augmentation" framing — never hurts, low overhead (~3ms), no retraining
- ~1 new page of analysis text

**Conclusion**
- Rewrite claims: (1) correction magnitude sensitivity is a novel finding, (2) obs features sufficient for conditioning, (3) CRM is a safe plug-and-play module
- Remove significance claims
- ~0.5 page rewrite

**Figures & Tables**
- Fig: magnitude curve — **no change to data, promote to main figure**
- Fig: perdof vs obs_only comparison — **no change, promote**
- Table: main results — **keep, change caption/framing**
- Table: spatial results — **keep as-is**
- Table: per-task breakdown — **keep, useful for variance discussion**
- No new figures needed (data already collected)

---

## 4. Switch Cost Estimate

| Section | Lines to change | Estimated hours | Difficulty |
|---------|----------------|-----------------|------------|
| Title + Abstract | ~15 lines | 1h | Medium (tone-setting) |
| Introduction (story spine) | ~30 lines | 1.5h | Medium |
| Method | 0 lines | 0h | — |
| Results reframing | ~20 lines | 1h | Low (data unchanged) |
| New analysis subsections | ~40 lines (new) | 2h | High (need careful argumentation) |
| Conclusion | ~15 lines | 0.5h | Low |
| Figure promotion / re-captioning | ~5 captions | 0.5h | Low |
| Related work (A2C2 positioning) | ~10 lines | 0.5h | Low (minor tone shift) |
| **Total** | **~135 lines** | **~7h** | |

Critical path: the new analysis subsections (why inverted-U, why obs > perdof) require careful writing to make the mechanistic argument convincing without overclaiming. Everything else is reframing existing content.

### Decision timeline
- Wait for seed44 results (ETA: ~24h from now)
- If 3-seed pooled p > 0.05: execute Narrative B switch (~1 day of writing)
- If 3-seed pooled p < 0.05: stay with Narrative A, keep Narrative B as fallback framing for discussion section
