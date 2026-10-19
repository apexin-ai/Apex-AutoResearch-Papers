# §4.X Cross-VLA Generalization — Section Outline

> Drafted 2026-05-21 | Paper: "Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs" | Target: CoRL 2026
> Status: π0.5 numbers [PENDING] — full baseline eval deploying on bjb1-32546 (3 seeds × Object + Spatial); CRM training/eval not yet started.

---

## Section role in paper

This section answers **R5 (single-backbone)** and tests **C3 (applicability boundaries)** with a third VLA architecture at an intermediate scale. With SmolVLA (0.4B, flow-matching) carrying the main analysis and OpenVLA (7B, tokenized) anchoring the determinism boundary, π0.5 (3.6B, flow-matching) probes whether CRM remains useful when the frozen backbone is already strong.

The section is **not** a hero result — it is a generalization test framed honestly: scale up the backbone by ~9× and re-run the same plug-and-play pipeline. The expected outcome is a modest absolute gain ceiling tied to backbone saturation, contrasted with SmolVLA's larger headroom. This pattern, combined with the OpenVLA failure mode, makes the boundary argument concrete: CRM gains are gated by (i) stochastic candidate diversity and (ii) un-saturated baseline SR.

---

## Proposed structure

### 4.X.1  Setup: three backbones on a shared pipeline

Three frozen VLAs differ along two axes that the analysis predicts matter — action-head stochasticity and baseline saturation:

| Backbone | Size | Action head | Stochastic at T=eval? | Baseline LIBERO-Object SR |
|---|---|---|---|---|
| SmolVLA | 0.4B | Flow-matching | Yes (naturally diverse across K) | 10.8 % ± 1.3 % (n=9) |
| π0.5 | 3.6B | Flow-matching | Yes (assumed; quick verify 50 trials) | 72 % (quick verify, 10/10 non-zero; full SR [PENDING]) |
| OpenVLA-v2 | 7B | Discretized tokens (T=0.5) | No (8/10 identical actions; per-DOF σ² < 1e-30 on 5/7 DOFs) | 69 % (D093 LOCKED) |

Pipeline held constant across backbones: K candidates from the frozen VLA → argmin-to-centroid selection → obs-only CRM residual (||δ||₂ ≤ 0.2) → action executed. The only backbone-specific change is the CRM input dim (SmolVLA 960, π0.5 2048, OpenVLA 4096); architecture and training recipe are identical. CRM is trained on per-backbone VLA-rollout caches over the same 20 LIBERO tasks (Object + Spatial). Each cell reports mean ± std over 3 seeds × 50 rollouts/task × 10 tasks unless stated.

### 4.X.2  Cross-VLA results (Table X) — anchor on Δ over backbone-matched baseline

The fair comparison is **Δ within each backbone**, not absolute SR across backbones (different action spaces, different fine-tuning, different baseline saturation).

**Table X — Cross-VLA Generalization (LIBERO-Object, K=2 Plan A)**

| Backbone | VLA-only baseline | + CRM (Plan A K=2) | Δ (abs / rel) | Stochastic? | Notes |
|---|---|---|---|---|---|
| SmolVLA 0.4B | 10.8 % ± 1.3 % (n=9) | **18.3 % ± 2.1 %** (n=≥3) | **+7.5 pp / +69 %** | yes | Main result, LOCKED |
| π0.5 3.6B | [PENDING n=3] | [PENDING n=3] | [PENDING] | yes | Quick verify 72 %; CRM pipeline ETA ≤72 h |
| OpenVLA 7B | 69 % | 0 % (CRM collapses) | **−69 pp** | **no** | D093 LOCKED — boundary case |

**LIBERO-Spatial** (held-in, secondary):

| Backbone | VLA-only | + CRM (Plan A K=2) | Δ |
|---|---|---|---|
| SmolVLA 0.4B | 29.4 % ± 1.5 % | **35.0 % ± 1.0 %** | **+5.6 pp / +19 %** |
| π0.5 3.6B | [PENDING] | [PENDING] | [PENDING] |
| OpenVLA 7B | [not run — out of scope after D093] | — | — |

*Numbers in bold are LOCKED; [PENDING] cells will be filled once the bjb1-32546 deployment completes and the CRM precompute → projection (2048→960) → eval pipeline finishes (~10–15 GPU-h after baseline harvest).*

### 4.X.3  Result narrative (to be finalized after π0.5 numbers land)

Three pre-registered prediction paths, written before π0.5 numbers are in, so the reader can audit which one realized:

- **P1 — Modest gain (Δ ∈ [+1, +4] pp):** consistent with diminishing returns: a 72 % baseline leaves ~28 pp of headroom, and CRM operates within a bounded correction radius (Sec. 4.2 magnitude analysis) that does not scale with backbone capacity. Reports as "CRM generalizes to a 9× larger backbone with reduced but positive absolute gain — relative improvement attenuates as baseline saturates."
- **P2 — Neutral (Δ ∈ [−1, +1] pp, p > 0.1):** consistent with the OpenVLA boundary partially generalizing: π0.5 candidates may be too tightly clustered for argmin-to-centroid to expose a meaningful correction target. Reports as "the determinism axis matters more than the scale axis; once K-sample diversity is low, CRM's correction signal vanishes regardless of architecture."
- **P3 — Negative (Δ < −1 pp):** consistent with C3 task-shift mode: CRM trained on per-backbone caches may carry π0.5-specific biases that fight π0.5's already-competent policy. Reports as "high-capacity stochastic backbones can be actively harmed by post-hoc residual correction — a sharpening of the C3 boundary."

The section commits to reporting whichever outcome materializes, including per-task breakdowns (especially if Δ is driven by a small subset, as on LIBERO-Long).

### 4.X.4  Applicability boundary: when does CRM help?

Two prerequisites, stated as a falsifiable rule and supported by the cross-VLA evidence:

> **CRM helps iff (i) the backbone produces ≥ ε action diversity across K samples at deployment temperature, AND (ii) the baseline SR has ≥ Δ_min headroom on the target distribution.**

- **(i) Stochasticity prerequisite — OpenVLA case.** OpenVLA at T=0.5 yields 8/10 identical action chunks (per-DOF variance < 1e-30 on 5 of 7 DOFs). Argmin-to-centroid degenerates (all K candidates collapse to one point), the CRM input is therefore out-of-distribution relative to its training cache, and the residual points off-manifold — the same input-shift failure mode documented at K=1 for SmolVLA (10.3 % < 10.8 % baseline). The result is not a tuning failure; it is the prerequisite (i) being violated.
- **(ii) Headroom prerequisite — π0.5 (preliminary) and SmolVLA.** SmolVLA's +7.5 pp / +69 % Object gain is supported by a 10.8 % baseline with ~89 pp of unrealized success. π0.5's quick-verify 72 % baseline limits the absolute Δ_max recoverable by any bounded-magnitude residual. The section reports both absolute and relative Δ, and explicitly states that a +2–4 pp gain on a 72 % baseline is a **different kind of evidence** than a +7.5 pp gain on an 11 % baseline — it tests whether the correction direction is correct on a competent policy, not whether the policy is rescued from near-failure.

These two prerequisites unify the cross-VLA table into a single rule rather than three separate stories. The OpenVLA collapse is a confirmed boundary (D093 LOCKED, n=3 seeds × 10 trials/task), not a method failure to be hidden — it is the most informative data point for delineating where CRM applies.

### 4.X.5  Honest discussion (paragraph-level, not glossed)

Three points the section must say out loud, not bury in supplementary:

1. **Diminishing returns are expected and reported.** At a 72 % baseline, even a perfect oracle has a ceiling of +28 pp. Any +X pp on π0.5 should be read against that ceiling, not against SmolVLA's +7.5 pp. We report Δ_abs, Δ_rel, and the fraction of remaining headroom recovered (Δ_abs / (100 − baseline)).
2. **Cross-VLA is generalization evidence, not a SOTA claim.** The contribution is the analysis (C1 correction > selection; C2 conditioning–magnitude interaction; C3 boundaries). The cross-VLA table tests whether C1–C3 predict outcomes on backbones the analysis was not built on. π0.5 results are framed as a falsification test of C3, not as a benchmark race.
3. **The boundary is the result.** A method that works on SmolVLA, attenuates on π0.5, and collapses on OpenVLA is more useful to the community than one claimed to work universally — it tells practitioners which deployment settings to expect a gain in. The section will close on this framing, explicitly aligned with the C3 boundary argument from §4.4.

---

## Provenance / evidence anchors (for paper_provenance.yaml)

| Cell | exp_id(s) | Status |
|---|---|---|
| SmolVLA Object baseline 10.8 % | aggregate of `eval-vla-only-object-seed{42..50}` | LOCKED |
| SmolVLA Object Plan A 18.3 % | `eval-plan-a-object-seed{42,43,44}` | LOCKED (D094) |
| SmolVLA Spatial baseline 29.4 % | `eval-vla-only-spatial-seed{42..45}` | LOCKED |
| SmolVLA Spatial Plan A 35.0 % | `eval-plan-a-spatial-seed{42,43,44}` | LOCKED (D094) |
| OpenVLA baseline 69 % | OpenVLA-v2 eval, 10 trials × 10 tasks | LOCKED (D087/D093) |
| OpenVLA CRM 0 % | OpenVLA CRM eval (D093) | LOCKED |
| π0.5 baseline quick verify 72 % | `eval-pi05-baseline-object-seed42-r2` (50 rollouts, 10/10 tasks non-zero) | LOCKED quick-verify only |
| π0.5 baseline full eval | bjb1-32546 deployment, 3 seeds × Object + Spatial | **PENDING** |
| π0.5 + CRM Plan A | not yet trained (CRM projection 2048→960 ~10–15 GPU-h after baseline harvest) | **PENDING** |

Every numeric cell in the section will trace back to a registry exp_id before submission (per memory.md M013 lesson: no abstract labels in provenance).

---

## Writing checklist (apply during drafting)

- [ ] Every number in the section traces to a concrete `eval-*` exp_id.
- [ ] Δ reported in both pp and % relative; headroom fraction Δ / (100 − baseline) given for π0.5.
- [ ] OpenVLA 0 % discussed as **boundary evidence**, not as a method bug to apologize for.
- [ ] π0.5 result (whichever of P1/P2/P3 materializes) reported without re-framing post-hoc; per-task breakdown included if Δ < +3 pp.
- [ ] No cherry-picking: if any seed is excluded, exclusion criterion is named *before* numbers are quoted (cf. D084 seed42 exclusion).
- [ ] Cross-VLA comparison emphasizes within-backbone Δ; absolute-SR cross-backbone is shown only as a footnote with the caveat that action spaces and fine-tuning regimes differ.
- [ ] Section ends on the unified prerequisite rule (stochasticity + headroom), tying back to C3.

## Open questions / blockers

- **π0.5 full baseline** ETA: pending bjb1-32546 6-GPU job. Acceptance criterion before harvest: 3 seeds × Object + Spatial all > 60 % SR (consistent with quick-verify 72 %).
- **π0.5 CRM training**: requires obs cache (2048-dim) precompute + projection layer training (2048→960 reuses SmolVLA CRM head) OR fresh CRM with obs_dim=2048. Decision A in `pi05_crm_pipeline_plan.md` chooses obs_dim=2048; the section assumes that path.
- **Statistical test**: with n=3 seeds × 10 tasks × 50 rollouts/task = 1500 trials per cell, paired Welch t-test on per-task SR is the planned default; Mann–Whitney U as robustness check.
- **Latency parity**: confirm π0.5 K=2 batched latency ≤ 1.5× K=1 (SmolVLA achieves K-invariant batched inference; π0.5 yet to be profiled).
