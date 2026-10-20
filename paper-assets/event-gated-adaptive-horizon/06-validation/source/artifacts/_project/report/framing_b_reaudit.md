# Framing B Re-Audit: Per-Section Diff Checklist

> Date: 2026-05-16 | Framing: **B — Diagnostic paper + SGS as informative negative result**
> Governing decisions: D059 (Framing B approved), D061 (gradient decomposition: reward=0, obs=93%)
> NVE diagnostic: 7/8 accuracy, AUROC=0.933, 1 FP (008e_v3_s2 non-CIVO)

---

## 1. Abstract

**Current status:** NOT WRITTEN

**Framing B requirements:**
- Diagnostic analysis paper positioning (not method paper)
- Core question: "Why does temporal abstraction fail in world-model RL?"
- Key findings: trained dt_embedding → CIVO → stochastic collapse
- NVE diagnostic framework: 7/8, AUROC=0.933
- Gradient decomposition: 93% obs decoders, 0% reward → reward-only SGS is architectural no-op
- TAWM contrast: dt-conditioning succeeds in MPC (TAWM, ICML 2025) but fails in imagination-based AC
- Scope: DreamerV3 + Walker Walk (+ Cheetah pending)

**Outline (≤150 words):**
1. Temporal abstraction via variable-rate imagination is a natural extension of world-model RL, but consistently degrades performance [1 sentence]
2. We present a systematic diagnostic analysis identifying trained dt-embedding as the necessary condition for conditioning-induced value overestimation (CIVO) [1 sentence]
3. Gradient decomposition reveals 93% of dt_emb gradients come from observation decoders (0% reward), making reward-only stop-gradient an architectural no-op [1 sentence]
4. NVE diagnostic threshold achieves AUROC=0.933 for CIVO detection [1 sentence]
5. Contrast with TAWM: dt-conditioning succeeds in MPC but fails in imagination-based AC — architecture-specific vulnerability [1 sentence]
6. Scoped to DreamerV3/RSSM; actionable guidelines for future temporal abstraction work [1 sentence]

**Legacy framing risks:** N/A (not yet written)

**Missing content:** Entire section

---

## 2. Introduction

**Current status:** NOT WRITTEN

**Framing B requirements:**
- Open with temporal abstraction as longstanding RL goal (options, macro-actions)
- World-model RL as natural testbed (modify imagination dt without changing env interaction)
- Puzzle framing: all attempts at variable-rate imagination degrade performance — why?
- TAWM contrast as novelty anchor: dt-conditioning works in MPC (TD-MPC2) but fails in imagination-based AC → architecture-specific vulnerability, not a generic negative
- Contribution list:
  1. Causal chain: trained dt_emb → CIVO (NVE>1.5x) → stochastic collapse
  2. NVE diagnostic framework (7/8 accuracy, AUROC=0.933)
  3. Gradient decomposition revealing reward=0 pathway (SGS = no-op)
  4. 2×2 ablation matrix closing the causal loop (D049)
- NOT a method paper — no new algorithm proposed
- Scope disclaimer: DreamerV3 + RSSM

**Legacy framing risks:** N/A (not yet written)

**Missing content:** Entire section. Must be written from scratch per story arc in paper_framing.md.

---

## 3. Related Work

**Current status:** NOT WRITTEN

**Framing B requirements:**
- Temporal abstraction in model-free RL: options framework (Sutton 1999), FiGAR, action repeat
- World-model RL: Dreamer family, IRIS, TWM
- **TAWM (Nhu et al., ICML 2025)** — CRITICAL: dt-conditioning succeeds in TD-MPC2 (MPC setting). Must position as: "dt-conditioning is not inherently broken; the vulnerability is specific to imagination-based actor-critic." This is the key novelty upgrade (D037)
- Variable-rate planning in world models (limited prior work)
- Value overestimation in MBRL: Lu et al. 2018 (delusional bias), Janner et al. 2019 (model exploitation). **Must explicitly differentiate** CIVO from Lu et al.'s delusional bias (different mechanism: model imprecision + learned conditioning amplification vs policy-class constraints)
- Diagnostic/analysis papers as a genre (precedent for non-method contributions)

**Legacy framing risks:** N/A (not yet written)

**Missing content:** Entire section. TAWM positioning is the single most important item for novelty defense.

---

## 4. Method (paper/method.md)

**Current status:** DRAFT v1, 144 lines. Covers §3.1 (Background), §3.2 (NVE diagnostic), §3.3 (Causal analysis + RSSM fidelity + mitigation).

### 4.1 Diff items

**DIFF-M1: §3 title — consider repositioning as "Methodology" or "Diagnostic Framework"**
- Current: "3. Methodology" — acceptable for diagnostic paper
- No change needed

**DIFF-M2: "The Delusional Critic Hypothesis" heading (line 39) → rename**
- Current: `### The Delusional Critic Hypothesis`
- Required: `### Conditioning-Induced Value Overestimation (CIVO)`
- The subsection body (lines 41-43) already uses "CIVO" and differentiates from Lu et al. Good.
- But line 43 still says: `We term this the *CIVO*, drawing on Lu & Schuurmans' concept of delusional policies, where function approximation introduces inconsistencies in Q-learning backups.`
- **Action:** Rename heading. Revise body to lead with CIVO definition, then note Lu et al. analogy as secondary (not "drawing on" — that implies derivation). Emphasize: CIVO is model-induced (temporal extrapolation error), Lu et al.'s delusion is policy-class-induced. Keep distinction explicit per D037.

**DIFF-M3: §3.3 "Mitigation: dt=1 Imagination" (lines 135-143) — MAJOR UPDATE NEEDED**
- Current: Presents 008e_v3 seed 1 as 95% baseline recovery, single-seed success. Lines 142-143 say "seed 2 is in progress."
- Framing B reality: **008e_v3_s2 COLLAPSED** (eval 715→137, nve=3.78x). C6 partially falsified (D038/D040).
- **Actions:**
  1. Remove "Mitigation" framing entirely — dt=1 imagination is NOT a robust mitigation
  2. Rewrite as "Imagination Step Size as Causal Variable" — the diagnostic point (trained dt_emb + dt=1 still collapses at 1/2 rate) is the finding
  3. Add s2 collapse data with mechanism contrast table (value-driven CIVO in 008d vs eval-driven instability in 008e_v3_s2)
  4. Add 009a baseline s2 stability data ruling out seed fragility
  5. Reframe: trained dt_embedding creates vulnerability through multiple pathways (Pathway A: CIVO via dt>1 imagination; Pathway B: non-CIVO policy instability independent of imagination dt)
  6. Remove lines 142-143 ("ongoing" language for s2)

**DIFF-M4: Add §3.X — Gradient Decomposition of dt_embedding (NEW SUBSECTION)**
- Not in current draft at all. This is a D061 finding.
- **Content:**
  - torch.autograd.grad analysis on dt_emb.weight
  - Gradient source breakdown: obs decoders 93% (1.505), KL 7% (0.119), reward 0% (0.000)
  - Implication 1: reward_dt_emb_detach (016e) is architectural no-op
  - Implication 2: dt_emb training is driven by observation reconstruction, not reward
  - Implication 3: Full-SGS (018) removing obs decoder gradients is the real gradient-level intervention
- **Placement:** After RSSM fidelity analysis (before or after the mitigation/causal-variable section)

**DIFF-M5: Add SGS as informative negative result (NEW SUBSECTION or folded into gradient decomposition)**
- 016e experiment: reward_dt_emb_detach=True
- Result: collapse at 95K (nve=10.42x), indistinguishable from 008d stochastic variation
- Interpretation: reward-only SGS is no-op because reward gradient to dt_emb = 0 by architecture
- Previously interpreted as "SGS delays collapse ~50K" — **this interpretation is WITHDRAWN** (D061)
- Frame as: "The null result is informative: it eliminates reward head as CIVO gradient pathway and redirects attention to observation decoders"

**DIFF-M6: 2×2 ablation matrix (D049) — not yet in method.md**
- The 2×2 matrix (trained/frozen/removed × subsample ON/OFF) is referenced in ROADMAP but not in method section
- Should add 015b (frozen dt_emb, subsample ON) result: peak nve 1.45x@55K → self-corrected → gradient starvation collapse
- This fills the ablation picture: trained=CIVO, frozen=sub-threshold transient, removed=blocked

**DIFF-M7: NVE diagnostic power update**
- Current draft (lines 70-71): "4/4 classification accuracy" — still accurate for threshold separation
- Framing B adds: AUROC=0.933, 7/8 overall accuracy, 1 FP (008e_v3_s2 non-CIVO late collapse)
- **Action:** Add AUROC=0.933 and 7/8 framing after the 4/4 threshold statement. Reference nve_sensitivity_table.tex. Clarify: 4/4 is for trained-vs-removed at threshold; 7/8 includes all conditions with 008e_v3_s2 as FP due to non-CIVO mechanism.

### 4.2 Legacy framing risks in method.md

| Line(s) | Issue | Action |
|---------|-------|--------|
| 39 | "The Delusional Critic Hypothesis" heading | Rename to "Conditioning-Induced Value Overestimation (CIVO)" |
| 43 | "drawing on Lu & Schuurmans' concept of delusional policies" | Weaken to "analogous to" and add explicit differentiation |
| 135 | "Mitigation: dt=1 Imagination with Multi-Rate Training" | Remove "Mitigation" framing; rewrite as diagnostic finding |
| 137-139 | "zero-cost mitigation" / "achieves eval return 869.9" (single seed only) | Remove mitigation language; add s2 collapse data |
| 142-143 | "seed 2 is in progress" | Replace with s2 collapse results + mechanism analysis |

### 4.3 Missing content in method.md

| Item | Priority | Notes |
|------|----------|-------|
| Gradient decomposition subsection (D061) | P0 | Core Framing B contribution |
| SGS informative negative (016e + D061) | P0 | Required by Framing B |
| 015b frozen dt_emb results | P1 | Completes 2×2 matrix |
| 008e_v3_s2 collapse + dual pathway analysis | P0 | C6 partially falsified |
| AUROC=0.933 / 7/8 framing | P1 | NVE strength update |

---

## 5. Experimental Setup (paper/sections/experimental_setup.md)

**Current status:** DRAFT v1, 130 lines. Covers §4.1 (Base architecture), §4.2 (Environment), §4.3 (Factorial design + Table 1), §4.4 (NVE diagnostic), §4.5 (Training details).

### 5.1 Diff items

**DIFF-E1: Table 1 (factorial table, lines 55-78) — needs new rows**
- Missing experiments: 015b (frozen dt_emb), 016e (SGS/reward detach), 009a/009b/009c (seeds)
- **Action:** Add rows for:
  - 015b: frozen dt_emb, subsample ON, H=15, dt=2 imag → "Frozen embedding control"
  - 016e: trained dt_emb + reward_dt_emb_detach, subsample ON, H=8, dt=2 imag → "Stop-gradient (reward)" or "SGS control"
  - Possibly 018 (planned) as a footnote row
- Seed replication rows (009a/b/c) can be listed as notes under existing rows rather than separate rows

**DIFF-E2: §4.2 Environment — update cross-env status**
- Lines 35-41: mentions Cheetah Run and Cartpole Swingup with footnote "in progress"
- 010a Cheetah baseline is now RUNNING (ROADMAP)
- **Action:** Keep footnote but update wording if 010a completes before submission. Remove Cartpole Swingup if it won't be run (focus resources on Cheetah).

**DIFF-E3: §4.4 NVE diagnostic — add AUROC and 7/8 framing**
- Current: 4/4 classification (lines 111-113)
- **Action:** Add paragraph after threshold definition:
  - AUROC=0.933 across all 8 experimental conditions (task B2)
  - 7/8 accuracy with 1 FP (008e_v3_s2, identified as non-CIVO late collapse via trajectory analysis)
  - Reference nve_sensitivity_table.tex
  - Supplementary task B1 (@1.7x): AUROC=1.0, 8/8

**DIFF-E4: §4.5 Training details — update seed info**
- Line 129: "key conditions (baseline, 008d, 008f, 008e_v3) add seed 2"
- **Action:** Update to reflect completed seed 2 runs: 009a (baseline s2, complete, stable), 009b (008d s2, complete, self-corrected), 009c (008f s2, complete), 008e_v3_s2 (complete, collapsed via non-CIVO pathway). Remove "in progress" language.

**DIFF-E5: "event-gated variable-rate imagination" naming (line 15)**
- Current: "We introduce an *event-gated variable-rate imagination* mechanism"
- Framing B is a diagnostic paper — the mechanism being studied failed. The naming suggests we're proposing it.
- **Action:** Reword: "We study a *variable-rate imagination* mechanism..." or "We investigate the following modifications to the DreamerV3 imagination pipeline..."

### 5.2 Legacy framing risks in experimental_setup.md

| Line(s) | Issue | Action |
|---------|-------|--------|
| 15 | "We introduce an event-gated variable-rate imagination mechanism" | Reword — we study/investigate, not introduce |
| 57 | Table caption: "unless noted" for dt=2 default | Fine, but add 016e row |
| 87 | "mitigation condition (008e_v3)" | Remove "mitigation" label — partially falsified |
| 109 | "we will update to the mean of seeds 1 and 2 once..." | Update: 009a baseline s2 is now complete; update normalization |

### 5.3 Missing content in experimental_setup.md

| Item | Priority | Notes |
|------|----------|-------|
| 016e (SGS) in factorial table | P0 | Core Framing B experiment |
| 015b (frozen) in factorial table | P1 | Completes 2×2 matrix |
| AUROC/7/8 in diagnostic section | P1 | Matched with method.md update |
| Updated seed status | P1 | Remove "in progress" language |

---

## 6. Results

**Current status:** NOT WRITTEN

**Framing B requirements:**
Structure as diagnostic findings, not performance claims:

**Finding 1 (C1):** All dt>1 configurations degrade performance
- 3 configs: 005 (learned gate), 006 (fixed dt=2), 007 (fixed dt=4)
- Learning curves overlay (hero figure)

**Finding 2 (C2):** Trained dt_embedding is the necessary condition for CIVO
- 008d vs 008f (primary causal comparison): trained → nve 2.09x → collapse; removed → nve ≤1.02x → stable
- 4/4 threshold separation across seeds
- 2×2 matrix: trained/frozen/removed × subsample

**Finding 3 (C3):** Untrained dt_embedding suppresses value drift
- 008a: 85% baseline at 105K, nve 0.59-0.93x
- 008c vs 008a: horizon effect

**Finding 4 (C4):** Longer dt amplifies degradation
- dt=1 (~950) > dt=2 (485) > dt=4 (177) monotonic

**Finding 5 (C5):** Subsampling/horizon are secondary factors
- 008e_v3 s1: subsample ON + dt=1 imag → 95% baseline

**Finding 6 (C6, partially falsified):** dt=1 imagination does not prevent collapse
- 008e_v3_s2 collapsed (eval 715→137, nve=3.78x)
- Dual pathway analysis: CIVO (Pathway A, 008d) vs non-CIVO policy instability (Pathway B, 008e_v3_s2)
- 009a baseline s2 stable → config-caused

**Finding 7 (NEW — Framing B core):** Gradient decomposition reveals reward=0 pathway
- dt_emb gradient: obs decoders 93%, KL 7%, reward 0%
- 016e SGS = no-op (informative negative)
- Reframes understanding of which pathways drive dt_emb training

**Finding 8: NVE diagnostic framework performance**
- task B2: 7/8, AUROC=0.933, 1 FP
- task B1 (supplementary): 8/8, AUROC=1.0
- Threshold sensitivity analysis (nve_sensitivity_table.tex)

**Legacy framing risks:** N/A (not yet written, but must NOT include):
- "SGS delays collapse" — WITHDRAWN (D061)
- "dt=1 imagination as practical mitigation" — PARTIALLY FALSIFIED (D038/D040)
- "delusional critic" terminology

**Missing content:** Entire section

---

## 7. Discussion

**Current status:** NOT WRITTEN

**Framing B requirements:**

1. **CIVO mechanism explanation**: Why trained dt_embedding causes overestimation
   - RSSM fidelity gap at dt>1 (Table: absolute errors + ratios)
   - 008d reward gap (2.78x) = critic receives confident but biased reward signals
   - 008f reward gap (1.01x) = no differentiation → no bias → no CIVO

2. **Gradient decomposition implications** (D061)
   - dt_emb is trained by observation reconstruction, not reward
   - Reward-only SGS is no-op → future interventions must target obs decoder pathway
   - Full-SGS (018) as the correct gradient-level test

3. **Dual vulnerability pathways** (D040)
   - Pathway A (CIVO): value-driven, entropy ↓, requires dt>1 imagination (008d)
   - Pathway B (non-CIVO policy instability): eval-driven, entropy ↑, independent of imagination dt (008e_v3_s2)
   - Trained dt_embedding as common root, but mechanisms diverge

4. **Value self-correction** (009b)
   - Transient nve>1.5x → self-correction (009b s2) vs sustained → collapse (008d s1)
   - Hypothesis: "point of no return" where feedback loop locks
   - Connection to primacy bias (Qiao et al. 2023), early outlier runs (Bjorck et al. 2022)

5. **TAWM contrast** (D037 — CRITICAL for novelty)
   - TAWM: dt-conditioning succeeds in TD-MPC2 (MPC)
   - Our finding: fails in imagination-based AC
   - Key difference: MPC re-plans from real states; imagination-based AC compounds errors across full rollout
   - Novelty upgrade: "architecture-specific vulnerability, not generic failure"

6. **Connection to MBRL overestimation literature**
   - Lu et al. 2018: delusional bias (policy-class) — differentiate from CIVO (model-induced)
   - Janner et al. 2019: model exploitation — CIVO is a specific instance mediated by temporal conditioning
   - Why model-free temporal abstraction doesn't suffer the same failure

**Legacy framing risks:** Must ensure:
- No "SGS delays collapse" claim
- No "delusional critic" usage
- No "dt=1 imagination solves the problem" framing
- 008f positioned as causal control, not recommended approach

**Missing content:** Entire section

---

## 8. Limitations

**Current status:** NOT WRITTEN

**Framing B requirements:**
1. Single primary environment (Walker Walk) — Cheetah pending (010a)
2. Limited seed count (2 seeds per key condition; stochastic collapse hard to characterize)
3. NVE threshold calibrated and evaluated on same data (not independent validation)
4. NVE confidence intervals wide: 95% CI = [47.3%, 99.7%] for 7/8
5. Only one base algorithm (DreamerV3); generalizability to other world-model architectures discussed but not tested
6. No formal causal inference framework (interventional, not observational, but not a formal DAG-based analysis)
7. Full-SGS (018) and Cheetah cross-env results pending at submission
8. 008e_v3_s2 collapse mechanism (Pathway B) not fully characterized — entropy increase noted but root cause unclear

**Legacy framing risks:** N/A (not yet written)

**Missing content:** Entire section

---

## 9. Conclusion

**Current status:** NOT WRITTEN

**Framing B requirements:**
- Restate core finding: trained dt_embedding is the necessary condition for CIVO in imagination-based AC
- Gradient decomposition: 93% obs decoders, 0% reward → reward pathway is architectural null
- NVE as practical diagnostic tool (AUROC=0.933)
- TAWM contrast: dt-conditioning is not inherently broken — the vulnerability is specific to imagination + learned dynamics
- Actionable guidance: don't use trained dt_embedding in imagination-based AC without safeguards; target obs decoder pathway for interventions
- Open questions: Full-SGS effectiveness (018), cross-environment generality, Pathway B characterization

**Legacy framing risks:** N/A (not yet written)

**Missing content:** Entire section

---

## Global Diff Items (cross-cutting)

### G1: "delusional critic" → CIVO full-text replacement (D037)

**Affected files:**
- `paper/method.md` line 39: heading "The Delusional Critic Hypothesis"
- `paper/method.md` line 43: "We term this the *CIVO*, drawing on Lu & Schuurmans'"

**Action:** Rename heading; rewrite body to define CIVO first, Lu et al. as analogy (not derivation). Search entire paper directory for any other occurrences before declaring clean.

### G2: 016e narrative — MUST be "no-op", not "delays collapse" (D061)

**Old claim (D057/D058, WITHDRAWN):** "SGS delays collapse ~50K steps"
**Correct claim (D061):** "016e reward_dt_emb_detach is a no-op; reward gradient to dt_emb = 0 by architecture. Observed timing differences from 008d are stochastic variation."

**Affected files:** Not yet in any written section (016e hasn't been written up yet), but MUST be checked in any future draft. The paper_framing.md exp_016e entry is already updated.

### G3: 008e_v3 — NOT a mitigation, partially falsified (D038/D040)

**Old claim:** "dt=1 imagination = practical mitigation (95% baseline recovery)"
**Correct claim:** "dt=1 imagination does not prevent collapse (1/2 seeds collapse via non-CIVO pathway). Trained dt_embedding creates vulnerability through multiple pathways."

**Affected files:**
- `paper/method.md` lines 135-143: entire "Mitigation" subsection must be rewritten
- `paper/sections/experimental_setup.md` line 87: "mitigation condition (008e_v3)"

### G4: TAWM positioning (D037 novelty upgrade)

**Status:** Not in any existing section.
**Required in:** Related Work (primary), Introduction (contribution claim), Discussion (mechanism contrast)
**Key sentence:** "TAWM (Nhu et al., ICML 2025) demonstrates that dt-conditioning succeeds in MPC settings (TD-MPC2), establishing that the vulnerability we identify is specific to imagination-based actor-critic training, not an inherent limitation of temporal conditioning."

### G5: 2×2 ablation matrix (D049)

**Status:** Referenced in ROADMAP but not yet in paper sections.
**Required in:** Results section, Discussion
**Content:** trained/frozen/removed × subsample ON/OFF matrix showing CIVO status per cell

### G6: Figures needed

| Figure | Status | Content |
|--------|--------|---------|
| Fig 1: Learning curves (hero) | Not created | All experiments overlaid |
| Fig 2: NVE trajectories | Not created | Healthy vs pathological separation |
| Fig 3: Factorial grid | Exists (updated per ROADMAP) | 2×2 matrix visualization |
| Fig 4: Causal diagram | Not created | dt_emb → CIVO → collapse chain |
| Fig 5: dt magnitude comparison | Not created | dt=1/2/4 monotonic decline |
| Fig 6: 008e_v3 dual seed | Exists (updated per ROADMAP) | s1 healthy + s2 collapse |
| Table: RSSM fidelity | In method.md | Needs absolute + ratio side-by-side |
| Table: NVE sensitivity | nve_sensitivity_table.tex | AUROC=0.933, exists |
| Table: Gradient decomposition | Not created | obs 93%, KL 7%, reward 0% |

---

## Priority-Ordered Execution Plan

### P0 — Blocking for submission

1. Rewrite `paper/method.md` §3.3 "Mitigation" → dual pathway finding (DIFF-M3)
2. Add gradient decomposition subsection to method.md (DIFF-M4)
3. Add SGS informative negative subsection (DIFF-M5)
4. Rename "Delusional Critic Hypothesis" → CIVO (DIFF-M2)
5. Write Results section (Section 5)
6. Write Introduction
7. Write Abstract
8. Write Discussion (especially TAWM contrast, dual pathways, gradient implications)
9. Add 016e to factorial table (DIFF-E1)
10. Update NVE diagnostic with AUROC=0.933 (DIFF-M7, DIFF-E3)

### P1 — Important but not blocking

11. Write Related Work (especially TAWM)
12. Write Limitations
13. Write Conclusion
14. Add 015b to factorial table and results
15. Update seed status / remove "in progress" language (DIFF-E4)
16. Reword "event-gated" as diagnostic study language (DIFF-E5)
17. Create gradient decomposition table
18. Update baseline normalization with 009a (DIFF-E4, experimental_setup.md line 109)

### P2 — Polish

19. Create missing figures (Fig 1, 2, 4, 5)
20. Cross-reference consistency check (method ↔ experimental_setup)
21. Final "delusional critic" grep across all files
22. Ensure RSSM fidelity table shows absolute + ratio everywhere
