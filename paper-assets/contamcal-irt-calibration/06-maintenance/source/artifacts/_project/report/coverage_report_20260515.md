# Coverage Report — contamcal-irt-calibration
**Date**: 2026-05-15 | **Deadline**: EMNLP 2026 ARR May 25 (10 days)

---

## 1. Core Claim Coverage Matrix

### Claim 1: Characterization (PRIMARY)
*Contamination effects are benchmark-dependent and scale-dependent. IRT γ_k captures bidirectional effects.*

| Component | Status | Evidence |
|-----------|--------|----------|
| 0.5B SFT × dosages (s42) | ✅ | d000/d005/d100 complete. d025 failed 2× (not critical — 3 dosages sufficient) |
| 0.5B SFT × dosages (s123) | ✅ | d000/d005/d100 complete |
| 1.5B SFT × dosages (s42+s123) | ✅ | Full 4×2 matrix complete. Cross-seed variance <1.2pp on MC benchmarks |
| 3B SFT s42 alpha=32 | 🏃 | d000_v3 (cuda:4, 25%), d025_v3 (queued), d100_v2 (cuda:1, 30%) — ETA ~12-15h |
| 3B SFT s123 alpha=32 | 🏃/✅ | d000/d005/d025 already alpha=32 ✅. d100 retraining (cuda:0) |
| 3B Eval (aligned) | 🏃 | Most complete; d005_s123 aligned running cuda:2. d100_s123 para missing |
| ARC forgetting evidence | ✅ | 3 independent chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83) |
| GSM8K inflation evidence | ✅ | 3B s123: d000=0.18→d100=0.73 (+55pp). Per-benchmark γ_k heterogeneity confirmed |
| Scale modulation | ✅ | 0.5B d100 ARC=29-37% (catastrophic) vs 3B d100 ARC=84% (mild) |
| Per-benchmark γ_k | ✅ | MMLU/ARC insensitive (<0.5pp), GSM8K highly sensitive (+34pp@d025) |

**Verdict: 🟡 Mostly covered.** 3B alpha=32 retrains are the gap. 0.5B+1.5B data alone can tell the story; 3B completes the scale dimension.

---

### Claim 2: Signal Failure (CO-PRIMARY)
*Min-K++ directional reversal at small scales. S1 embedding only reliable signal.*

| Component | Status | Evidence |
|-----------|--------|----------|
| 0.5B signals (S1/S2/S4) | ✅ | exp-002: 9/9 PASS. S1 AUC 0.95-0.995 at d005 |
| 1.5B signals | ✅ | exp-002: 12/12 PASS |
| 3B signals | ❌ | exp-002 failed twice (GPU conflicts). **NOT STARTED for valid run** |
| Min-K++ reversal (0.5B) | ✅ | Cohen's d = -1.2 to -2.7 at d100. Headline finding |
| Signal × scale × dosage heatmap | 🟡 | 0.5B+1.5B available. 3B missing → heatmap has gap at largest scale |
| RRF = S1-only in practice | ✅ | exp-003 + exp-008 confirm 0/3 signals survive across regimes |
| S2/S4 at 1.5B/3B verification | 🟡 | 1.5B done. 3B missing (contingency C2 in paper_framing) |

**Verdict: 🟡 Core finding (Min-K++ reversal) solid. 3B signals are a gap but not fatal — can present 0.5B+1.5B and note 3B as future work if time runs out.**

---

### Claim 3: Identifiability
*Fisher Information establishes structural vs practical thresholds. N≥50 domain-method mismatch.*

| Component | Status | Evidence |
|-----------|--------|----------|
| Simulation sweep (exp-004) | 🏃 | v6+v7 running on CPU. v1-v5 all failed. 66/80 seeds done in earlier run |
| D056 key finding | ✅ | Coverage collapse = model misspecification (DGP=model → 90-100% coverage; real data → 20-33%) |
| Fisher Info derivation | ❌ | Theoretical work not yet written. CPU-only, no GPU dependency |
| N≥50 threshold argument | ✅ | CI width ∝ N^{-0.48} from simulation. Coverage collapse at N<30 confirmed |
| SBC diagnostic | 🟡 | Planned but not run on real data |

**Verdict: 🟡 D056 finding is strong. Simulation sweep nearly done. Fisher Info derivation is a writing task — can be done in parallel.**

---

### Claim 4: Conditional Calibration (DEMOTED)
*When conditions met (2PL for open-ended, 4PL for MCQ, AUC≥0.70), calibration produces usable estimates.*

| Component | Status | Evidence |
|-----------|--------|----------|
| ARC IRT fitting | ✅ | 2PL works. MAE=0.035 |
| GSM8K IRT fitting | ✅ | NUTS converges (Rhat=1.008, ESS=956, 0 divergences) |
| Pooled IRT (multi-seed) | ❌ | Needs redo with alpha=32 3B data + complete eval matrix |
| Baselines comparison (7) | ❌ | DCR, linear regression, etc. not formally run. B4 MAE=0.040 noted |
| Gating criterion implementation | ❌ | γ significant AND PPP ∈ [0.1,0.9] AND calibrated MAE < raw MAE |
| GSM8K overcorrection (negative result) | ✅ | MAE 11× worse than raw — honest negative result |
| Coverage analysis | ✅ | 20-69% at 95% nominal — below target but characterized |

**Verdict: 🔴 Significant gaps. Pooled IRT rerun and baselines are blocking. This claim is demoted, so partial coverage may be acceptable if framed as preliminary.**

---

## 2. Pipeline Dependency Chain & Timeline

```
3B SFT alpha=32 (4 jobs)          ──→ 3B Eval (aligned+para)  ──→ 3B Signals  ──→ Pooled IRT  ──→ Paper
  ~12-15h remaining                    ~3-4h per model              ~6-12h          ~4-8h
  ETA: May 16 AM                       ETA: May 16 PM              ETA: May 17     ETA: May 18
                                                                                        │
exp-004 sim sweep (CPU) ─────────────────────────────────────────────────────────────────┘
  ~few hours remaining                                                              
  ETA: May 15-16                                                                    

Fisher Info derivation (writing) ────────────────────────────────────────────────────────┘
  ~1 day                                                                            

Paper writing ──────────────────────────────────────────────────────────────────────────
  Needs: May 18-25 (7 days) — TIGHT but feasible for 8-page paper
```

### Estimated Wall-Clock Timeline

| Date | Milestone |
|------|-----------|
| May 15-16 | 3B SFT alpha=32 retrains complete; exp-004 sim sweep finishes |
| May 16-17 | 3B aligned+para evals complete (parallel across GPUs) |
| May 17-18 | 3B signal computation (exp-002); pooled IRT with full data |
| May 18 | **All experiments complete** (optimistic) |
| May 18-24 | Paper writing (7 days: intro+method day 1-2, results day 3-4, figures day 5, polish day 6-7) |
| May 25 | **SUBMISSION** |

---

## 3. Critical Path Bottlenecks

### Bottleneck 1: 3B Alpha=32 SFT Retraining (BLOCKING)
- 4 jobs running/queued on cqa1-21977 (cuda:0,1,4 + 1 queued)
- At ~30% progress → ~8-10h remaining per job
- **Risk**: GPU contention or failure could delay by 12-24h
- **Mitigation**: Jobs are parallelized across GPUs; 6× 4090D available

### Bottleneck 2: 3B Signal Computation (exp-002)
- Failed twice due to GPU conflicts
- Cannot start until SFT checkpoints exist
- **Risk**: Third failure would push timeline by another day
- **Mitigation**: Follow C001/C003/C004 constraints strictly

### Bottleneck 3: Pooled IRT Rerun
- Needs complete eval data from ALL scales × dosages × seeds
- CPU-bound but depends on all upstream GPU work
- **Risk**: If data quality issues found (like D036), may need iteration

### Bottleneck 4: Paper Writing (7 days)
- Zero figures currently exist
- Fisher Info derivation not written
- 35+ citations to compile
- **Risk**: 7 days for a full EMNLP paper is tight; typically needs 10-14 days
- **Mitigation**: Many results already characterized in memory/decisions; writing is synthesis not discovery

---

## 4. Priority Ranking

### MUST DO (paper cannot submit without these)

| Priority | Task | Est. Time | Blocking? |
|----------|------|-----------|-----------|
| P0 | Complete 3B alpha=32 SFT (4 jobs) | ~12h | Yes — all downstream |
| P0 | 3B aligned eval (after SFT) | ~8h total | Yes — IRT input |
| P0 | 3B signal computation (exp-002) | ~8h | Yes — Claim 2 heatmap |
| P0 | Pooled IRT with N≥16 models | ~6h | Yes — Claims 1+4 |
| P0 | Paper writing (8 pages + appendix) | ~7 days | Final output |
| P0 | 5 required figures | ~2 days | Paper completeness |
| P0 | Fisher Info derivation (appendix) | ~1 day | Claim 3 |

### SHOULD DO (significantly strengthens paper)

| Priority | Task | Est. Time | Impact |
|----------|------|-----------|--------|
| P1 | 3B para eval (paraphrase robustness) | ~8h | Strengthens Claim 1 |
| P1 | Formal baselines comparison (7 baselines) | ~2 days | Claim 4 defense |
| P1 | SBC diagnostic on real data | ~4h CPU | Claim 3 coverage gap |
| P1 | Calibration gating criterion implementation | ~4h | Claim 4, Concern #20 |

### CAN DROP (nice-to-have, not essential for submission)

| Priority | Task | Impact if dropped |
|----------|------|-------------------|
| P2 | exp-008 instruct RL proxy | Concern #3 defense weaker; frame as future work |
| P2 | 0.5B d025 SFT retry | 3 dosages sufficient without d025 |
| P2 | Oracle matched N=8 rerun | Can note in limitations |
| P2 | GSM8K longer NUTS chains | Current convergence adequate |
| P2 | HumanEval (appendix only) | Already demoted |

---

## 5. Risk Assessment Summary

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| 3B SFT fails/delays | Low | HIGH | 3 of 4 jobs already running; GPUs allocated |
| exp-002 3B signals fail again | Medium | HIGH | Strict C001-C004 compliance; clean GPU before submit |
| Pooled IRT reveals new issues | Medium | Medium | D056 already diagnosed misspecification; frame honestly |
| Paper writing takes >7 days | High | HIGH | Start writing intro+method NOW with existing 0.5B+1.5B data |
| Fisher Info derivation blocks | Low | Medium | Theoretical work, no dependencies |

### Overall Assessment

**Feasibility: TIGHT but POSSIBLE** with disciplined execution.

The critical insight: **start paper writing immediately** using 0.5B + 1.5B data (which is complete). 3B results can be slotted in as they arrive (May 17-18). Don't wait for all experiments to finish before writing — the story spine, method section, related work, and most of the results can be drafted now.

**Biggest risk**: the 7-day writing window. This is the true bottleneck, not the experiments. A realistic schedule allocates:
- May 15-17: Write intro, related work, method (using existing data)
- May 17-19: Write results as 3B data arrives; create figures
- May 19-21: Write discussion, limitations, conclusion; Fisher derivation
- May 21-23: Full draft review, polish, citation check
- May 23-24: Final formatting, abstract, supplementary
- May 25: Submit

If 3B signals (exp-002) fail a third time, the paper can still be submitted with 0.5B+1.5B signal data and 3B SFT/eval data, noting 3B signals as in-progress. This weakens Claim 2's scale coverage but doesn't invalidate the Min-K++ reversal finding.
