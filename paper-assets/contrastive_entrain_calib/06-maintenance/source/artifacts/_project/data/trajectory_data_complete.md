# Complete Experiment Trajectory Data
> Generated: 2026-05-21 | Vanilla baseline SYCONScore = 0.1335

## 1. exp-003: R3-only GRPO — Seed 1 (seed=42)

| Step | SYCONScore | ToF | NoF | vs Vanilla (%) |
|------|-----------|------|------|----------------|
| 1000 | 0.0743 | 0.0387 | 0.9448 | −44.3 |
| 2000 | 0.0846 | 0.0442 | 0.9834 | −36.6 |
| 3000 | 0.0946 | 0.0497 | 0.9724 | −29.1 |
| 4000 | 0.1144 | 0.0608 | 0.9669 | −14.3 |
| 4500 | 0.1337 | 0.0718 | 0.9613 | +0.1 |
| 5000 | 0.1144 | 0.0608 | 0.9669 | −14.3 |
| 5500 | 0.1144 | 0.0608 | 0.9724 | −14.3 |
| 6000 | 0.0846 | 0.0442 | 0.9724 | −36.6 |
| 6500 | **0.1529** | **0.0829** | 0.9834 | **+14.5** |
| 7000 | 0.1046 | — | — | −21.6 |
| 7500 | 0.1046 | — | — | −21.6 |
| 8000 | ⏳ RUNNING | — | — | — |

Best: **ckpt-6500** SYCONScore=0.1529 (+14.5% vs vanilla)
Note: Non-monotonic trajectory — peak at 6500 with regression before and after. Steps 7000/7500 only have SYCONScore (no ToF/NoF breakdown).

## 2. exp-004: ACT (SFT)

| Step | SYCONScore | ToF | NoF | vs Vanilla (%) |
|------|-----------|------|------|----------------|
| 1000 | 0.2048 | 0.1160 | 0.8729 | +53.4 |
| 1500 | 0.1699 | 0.0939 | 0.8895 | +27.3 |
| 2500 | 0.2389 | 0.1381 | 0.8840 | +78.9 |
| 3000 | 0.2058 | 0.1160 | 0.9116 | +54.2 |
| 3500 | 0.2312 | 0.1326 | 0.9006 | +73.2 |
| 4000 | 0.2140 | 0.1215 | 0.8950 | +60.3 |
| 4500 | 0.1875 | 0.1050 | 0.8785 | +40.4 |
| 5000 | 0.2631 | 0.1547 | 0.8785 | +97.1 |
| 5500 | 0.2383 | 0.1381 | 0.8674 | +78.5 |
| 6000 | 0.2618 | 0.1547 | 0.8508 | +96.1 |
| 6500 | 0.2526 | 0.1492 | 0.8232 | +89.1 |
| 7000 | **0.2858** | **0.1713** | 0.8619 | **+114.1** |
| 7500 | 0.2771 | 0.1657 | 0.8453 | +107.6 |
| 8000 | ~0.3013† | — | — | ~+125.7 |

Best: **ckpt-8000** SYCONScore≈0.3013 (+125.7% vs vanilla)
†ckpt-8000 value from parent exp-004 summary (no individual eval entry with ToF/NoF breakdown).
Missing: ckpt-500, ckpt-2000 (no eval entries in registry).

## 3. exp-003-s2: R3-only GRPO — Seed 2 (seed=43)

| Step | SYCONScore | ToF | NoF | vs Vanilla (%) | Source |
|------|-----------|------|------|----------------|--------|
| 500 | 0.0845 | 0.0442 | 0.9503 | −36.7 | exp-003-s2-eval-ckpt500 |
| 1000 | 0.0844 | 0.0442 | 0.9448 | −36.8 | exp-003-s2-eval-ckpt1000 |
| 1500 | 0.1044 | 0.0552 | 0.9503 | −21.8 | exp-003-s2-eval-ckpt1500 |
| 2000 | 0.0846 | — | — | −36.6 | exp-003-eval-s2-ckpt2000 |
| 2500 | ⏳ RUNNING | — | — | — | exp-003-eval-s2-ckpt2500 |
| 3000 | 0.0945 | 0.0497 | 0.9503 | −29.2 | exp-003-eval-s2-ckpt3000 |
| 3500 | ⏳ RUNNING | — | — | — | exp-003-eval-s2-ckpt3500 |

Best so far: **ckpt-1500** SYCONScore=0.1044 (−21.8% vs vanilla)
Note: Seed 2 trajectory consistently below vanilla baseline. Two evals still running.

## 4. exp-008v3: Binary Probe GRPO

| Step | SYCONScore | ToF | NoF | vs Vanilla (%) |
|------|-----------|------|------|----------------|
| 500 | 0.0000 | 0.0000 | 0.9945 | −100.0 |
| 1000 | 0.0110 | 0.0055 | 0.9945 | −91.8 |
| 1500 | 0.0000 | 0.0000 | 1.0000 | −100.0 |
| 2000 | 0.0000 | 0.0000 | 1.0000 | −100.0 |

Conclusion: **Complete failure** — immediate stubbornness collapse. ToF→0 within 500 steps.

## 5. exp-009: Continuous Probe GRPO

| Step | SYCONScore | ToF | NoF | vs Vanilla (%) |
|------|-----------|------|------|----------------|
| 500 | 0.1238 | 0.0663 | 0.9337 | −7.3 |
| 1000 | 0.1141 | 0.0608 | 0.9337 | −14.5 |

Conclusion: **Negative** — monotonic decline, below baseline at both checkpoints.

## 6. exp-014: Continuous Probe GRPO (extended)

| Step | SYCONScore | ToF | NoF | vs Vanilla (%) |
|------|-----------|------|------|----------------|
| 3000 | 0.0110 | 0.9780 | 0.0060 | −91.8 |

Conclusion: **Mode collapse** — model flips on ALL pressure (ToF≈1, NoF≈0). Killed.

## 7. exp-016: ActAdd (steering vectors)

| Alpha | SYCONScore | ToF | NoF | vs Vanilla (%) |
|-------|-----------|------|------|----------------|
| 0.0 | 0.1335 | 0.0718 | 0.9448 | 0.0 |
| 0.5 | 0.1334 | 0.0718 | 0.9392 | −0.1 |
| 1.0 | 0.0846 | 0.0442 | 0.9724 | −36.6 |
| 2.0 | 0.0537 | 0.0276 | 0.9669 | −59.8 |
| 5.0 | 0.0537 | 0.0276 | 0.9613 | −59.8 |

Conclusion: **Negative** — ActAdd improves NoF in WRR metric but destroys ToF. Net negative under SYCONScore.

## 8. exp-012: Llama Cross-Model Probe (diagnostic, no SYCONScore eval)

| Metric | Value |
|--------|-------|
| CV AUROC (best layer 16) | 0.7793 |
| Style-controlled AUROC | 0.9227 |
| Multi-layer AUROC | 0.8130 |
| Random direction AUROC | 0.53 ± 0.054 |
| Gap (d_syc − random) | +0.248 |

Note: Probe analysis only — no SYCONScore training trajectory. Llama sycophancy signal more concentrated than Qwen (gap +0.248 vs +0.108).

## 9. Vanilla Baseline (D027 Reeval)

| Metric | Value |
|--------|-------|
| SYCONScore | 0.1335 |
| ToF | 0.0718 |
| NoF | 0.9448 |

---

## Summary: Best Checkpoint Comparison

| Method | Exp ID | Best Step | SYCONScore | ToF | NoF | vs Vanilla (%) | Status |
|--------|--------|-----------|-----------|------|------|----------------|--------|
| Vanilla (Qwen3-8B) | vanilla-d027-reeval | — | 0.1335 | 0.0718 | 0.9448 | — | baseline |
| **ACT (SFT)** | exp-004 | **ckpt-7000** | **0.2858** | **0.1713** | 0.8619 | **+114.1** | ✅ best confirmed |
| ACT (SFT) | exp-004 | ckpt-8000 | ~0.3013† | — | — | ~+125.7 | †summary only |
| R3-only GRPO s1 | exp-003 | ckpt-6500 | 0.1529 | 0.0829 | 0.9834 | +14.5 | ✅ |
| R3-only GRPO s2 | exp-003-s2 | ckpt-1500 | 0.1044 | 0.0552 | 0.9503 | −21.8 | partial (2 RUNNING) |
| Continuous Probe GRPO | exp-009 | ckpt-500 | 0.1238 | 0.0663 | 0.9337 | −7.3 | ❌ negative |
| Binary Probe GRPO | exp-008v3 | ckpt-1000 | 0.0110 | 0.0055 | 0.9945 | −91.8 | ❌ stubbornness collapse |
| Cont. Probe GRPO ext. | exp-014 | ckpt-3000 | 0.0110 | 0.9780 | 0.0060 | −91.8 | ❌ mode collapse |
| ActAdd (α=0.5) | exp-016 | α=0.5 | 0.1334 | 0.0718 | 0.9392 | −0.1 | ❌ no improvement |
| Llama Probe | exp-012 | — | — | — | — | — | diagnostic only |

---

## Pending Data Points

| Exp ID | Status | Notes |
|--------|--------|-------|
| exp-003-eval-ckpt8000 | ⏳ RUNNING | R3-GRPO s1 last checkpoint |
| exp-003-eval-s2-ckpt2500 | ⏳ RUNNING | R3-GRPO s2 |
| exp-003-eval-s2-ckpt3500 | ⏳ RUNNING | R3-GRPO s2 |
| exp-003-s2-eval-ckpt2500 | 📋 QUEUED | R3-GRPO s2 (duplicate naming) |
| exp-003-s2-eval-ckpt3000 | 📋 QUEUED | R3-GRPO s2 (duplicate naming, success result exists under exp-003-eval-s2-ckpt3000) |
| exp-004-eval-ckpt500 | ❓ MISSING | ACT early checkpoint, never submitted |
| exp-004-eval-ckpt2000 | ❓ MISSING | ACT checkpoint, never submitted |
| exp-004-eval-ckpt8000 | ❓ MISSING | ACT best checkpoint (~0.3013 from parent summary), no individual eval entry |
