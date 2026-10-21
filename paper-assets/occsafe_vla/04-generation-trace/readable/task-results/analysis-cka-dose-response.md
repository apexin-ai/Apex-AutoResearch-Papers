# analysis cka dose response

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cka_dose_response_20260525T054451_result.json`
- **Structured JSON:** [`dd3e2021f1b7a56d18f0.json`](../../sessions/dd/dd3e2021f1b7a56d18f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CKA Dose-Response Results (Partial — 3/7 conditions)

### Summary

| Condition | DINOv2 CKA (mean) | DINOv2 CKA (min) | SigLIP CKA (mean) | SigLIP CKA (min) |
|-----------|-------------------|-------------------|--------------------|--------------------|
| Vanilla (s0) | **0.968** | 0.903 | **0.956** | 0.853 |
| Full OCC (s0) | **0.962** | 0.871 | **0.962** | 0.896 |
| Cutoff 15K (s1) | **0.520** | 0.383 | **0.927** | 0.785 |

### Key Finding

**Cutoff 15K causes dramatic DINOv2 representation divergence** — CKA drops to 0.52 (vs ~0.96 for Vanilla and Full OCC), with middle blocks (10-14) as low as 0.40. SigLIP is more resilient (0.93 mean), with degradation concentrated in later blocks.

This is paradoxical: cutoff_15k has CAR=0.804 (better than Vanilla 0.788), yet its DINOv2 encoder is far more diverged from pretrained. Continuous OCC gradient flow (Full OCC) stabilizes the vision encoder; discontinuous flow (cutoff) causes optimization instability that pulls DINOv2 away from pretrained but doesn't hurt downstream performance.

### What's Missing

4 conditions still training on westd-34685 (~8% done, ETA ~12h from now):
- cutoff_25k_s2_v3 (GPU 0)
- cutoff_45k_s1_v3 (GPU 2)  
- cutoff_15k_s2 (GPU 3)
- reverse_cutoff_s2_v3 (GPU 1)

When they complete, only their LoRA adapters (~463MB each) need to be transferred to 10894 to run the full 7-condition analysis. The script at `/root/autodl-tmp/analysis/cka_dose_response/cka_dose_response.py` is ready — just add the new paths to the `CONDITIONS` dict.

### Outputs
- PDF/PNG: `artifacts/figures/cka_dose_response.{pdf,png}`
- JSON: `artifacts/cka_dose_response_results.json`
- Remote: `/root/autodl-tmp/analysis/cka_dose_response/` on westd-10894

---
