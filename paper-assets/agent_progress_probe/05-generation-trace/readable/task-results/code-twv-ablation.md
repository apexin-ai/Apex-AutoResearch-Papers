# code twv ablation

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_twv-ablation_20260514T173937_result.json`
- **Structured JSON:** [`c7d3f3ea9b68a150c3ed.json`](../../sessions/c7/c7d3f3ea9b68a150c3ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All registered. Here's the final summary:

## TWV Ablation Results (exp_id: twv-ablation) — **NEGATIVE**

| Variant | F1 | Acc |
|---|---|---|
| **MV baseline** | **0.8946** | 0.8932 |
| twv_full (σ=3.0) | 0.8703 | 0.8912 |
| twv_no_temporal (σ=3.0) | 0.8845 | 0.9034 |
| twv_no_smooth (hard) | 0.6992 | 0.7820 |
| σ=1.0 | 0.8105 | 0.8504 |
| **σ=2.0** | **0.9003** | **0.9157** |
| σ=5.0 | 0.8078 | 0.8513 |
| σ=7.0 | 0.8216 | 0.8595 |

**Gradient hypothesis TWV_full > TWV_no_temporal > MV at σ=3.0: REJECTED.** Both TWV variants underperform MV at that σ.

**σ sweep** shows a sharp, narrow peak at **σ=2.0** (F1=0.9003) — the only σ beating MV. Performance degrades steeply on both sides: σ=1.0 drops to 0.81, σ=3.0 to 0.87. This confirms the original `run_tlm.py` choice of σ=2.0 was correct but fragile.

Key takeaways:
- Gaussian smoothing is essential (hard shift → 0.699, catastrophic)
- Temporal lag profiles hurt at σ=3.0 (no_temporal 0.884 > full 0.870), suggesting the lag offsets interact badly with wider kernels
- TWV's advantage over MV is real but razor-thin (+0.6% F1) and confined to a single σ value

---
