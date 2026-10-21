# plan 7b pilot design

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_plan_7b-pilot-design_20260518T062031_result.json`
- **Structured JSON:** [`afe92d8660c4ce32c3ce.json`](../../sessions/af/afe92d8660c4ce32c3ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan written to `artifacts/pilot_7b_plan.md`.

**Summary of the design:**

**Config A (recommended first)** mirrors the 3B standardized config exactly: r=16, alpha=32, lr=5e-5. The theoretical argument is that 7B has more base parameters so the same LoRA rank produces a *smaller* relative perturbation, making it inherently more conservative than on 3B. This is the most informative test: if it passes, no hyperparameter adjustment needed.

**Fallback chain**: A (lr=5e-5) → B (lr=2e-5) → C (r=8, alpha=16, lr=1e-5). Each step reduces effective LoRA scale by ~2-5x.

**Pass criteria**: MMLU/ARC within 2pp of base, GSM8K within 5pp (the D018 sentinel metric), loss < 1.5 with no divergence.

**Total pilot cost**: ~4-5h on 1x A100 80GB. If Config A passes on first try, the full 7B matrix can start immediately after.

**Key risk flag**: `train_sft.py` default lr is still 2e-4 (the D018-era dangerous value). Every launch command must explicitly pass `--lr 5e-5`.

---
