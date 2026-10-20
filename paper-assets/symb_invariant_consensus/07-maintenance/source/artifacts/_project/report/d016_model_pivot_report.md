# D016 Model Pivot Report: QwQ-32B → Qwen2.5-14B-Instruct

**Date**: 2026-05-16
**Server**: westd-32608 (AutoDL)
**GPU**: A6000 48GB

---

## Phase 0: 5th Question Verification (QwQ-32B)

Completed run of 5 ProofWriter questions (proofwriter_5_l3l1_fix.json) with QwQ-32B, K=12.

| Metric | Value |
|--------|-------|
| n_problems | 5 |
| K | 12 |
| SICA accuracy | 4/5 = 80% |
| SC accuracy | 4/5 = 80% |
| Total wall time | 4180.1s |

**5th question (31_Q12)**: gold=False, SICA=Unknown (WRONG), SC=Unknown (WRONG), SC votes: Unknown:8, False:2, True:2, constraints extracted from 12/12 traces, 3 unique after dedup.

## Phase 1: QwQ-32B vLLM Shutdown

- Killed PID 129131 (QwQ-32B vLLM server)
- GPU memory freed successfully
- Confirmed no residual processes on port 8000

## Phase 2: Qwen2.5-14B-Instruct Deployment

| Step | Details |
|------|---------|
| Download method | ModelScope CDN (HuggingFace proxy too slow on AutoDL ~200KB/s) |
| Download time | ~28 min (8 safetensors shards, 3.6-3.7GB each) |
| Model path | `/root/autodl-tmp/models/Qwen2.5-14B-Instruct` |
| vLLM PID | 174291 |
| vLLM startup | ~50s (model loading 7.8s + torch.compile 17.9s + CUDA graphs ~6s) |
| GPU memory | 27.57 GiB |
| max-model-len | 8192 |
| gpu-memory-utilization | 0.85 |

vLLM API confirmed at `localhost:8000`, model ID = `/root/autodl-tmp/models/Qwen2.5-14B-Instruct`.

## Phase 3: C0 Precheck Results

**Config**: K=6, T=0.7, max_tokens=4096

### FOLIO (10 questions)

| # | ID | Label | Distribution | Multi? | SC Answer | SC Correct? |
|---|-----|-------|-------------|--------|-----------|-------------|
| 1 | folio_000 | True | True:5, Unknown:1 | Yes | True | V |
| 2 | folio_001 | True | True:5, Unknown:1 | Yes | True | V |
| 3 | folio_002 | True | True:5, Unknown:1 | Yes | True | V |
| 4 | folio_003 | True | Unknown:6 | No | Unknown | X |
| 5 | folio_004 | True | True:6 | No | True | V |
| 6 | folio_005 | True | True:6 | No | True | V |
| 7 | folio_006 | True | Unknown:4, True:2 | Yes | Unknown | X |
| 8 | folio_007 | True | True:6 | No | True | V |
| 9 | folio_008 | True | True:6 | No | True | V |
| 10 | folio_009 | True | True:6 | No | True | V |

- **Multi-candidate rate**: 4/10 = **40%**
- **SC accuracy**: 8/10 = **80%**
- **Time**: 104s

### ProofWriter (16 questions)

| # | ID | Label | Distribution | Multi? | SC Answer | SC Correct? |
|---|-----|-------|-------------|--------|-----------|-------------|
| 1 | AttNeg-OWA-D5-979_Q9 | True | True:4, Unknown:2 | Yes | True | V |
| 2 | RelNoneg-OWA-D5-1036_Q11 | True | Unknown:6 | No | Unknown | X |
| 3 | AttNeg-OWA-D5-891_Q1 | True | True:6 | No | True | V |
| 4 | AttNeg-OWA-D5-347_Q11 | True | True:3, Unknown:3 | Yes | True | V |
| 5 | RelNoneg-OWA-D5-616_Q7 | True | Unknown:4, True:2 | Yes | Unknown | X |
| 6 | AttNeg-OWA-D5-399_Q3 | True | True:6 | No | True | V |
| 7 | RelNoneg-OWA-D5-173_Q11 | True | True:3, Unknown:3 | Yes | True | V |
| 8 | AttNoneg-OWA-D5-971_Q5 | True | True:6 | No | True | V |
| 9 | AttNoneg-OWA-D5-702_Q1 | True | True:6 | No | True | V |
| 10 | AttNoneg-OWA-D5-844_Q1 | True | True:6 | No | True | V |
| 11 | RelNeg-OWA-D5-498_Q8 | False | True:5, False:1 | Yes | True | X |
| 12 | AttNoneg-OWA-D5-20_Q10 | False | Unknown:5, True:1 | Yes | Unknown | X |
| 13 | RelNeg-OWA-D5-173_Q10 | False | False:3, Unknown:3 | Yes | False | V |
| 14 | RelNoneg-OWA-D5-251_Q10 | False | Unknown:6 | No | Unknown | X |
| 15 | RelNeg-OWA-D5-721_Q8 | False | False:6 | No | False | V |
| 16 | AttNoneg-OWA-D5-500_Q8 | False | False:4, Unknown:2 | Yes | False | V |

- **Multi-candidate rate**: 8/16 = **50%**
- **SC accuracy**: 11/16 = **69%**
- **Time**: 175s

### Combined Summary

| Metric | FOLIO | ProofWriter | Combined |
|--------|-------|-------------|----------|
| Questions | 10 | 16 | 26 |
| Multi-candidate rate | 40% | 50% | **46%** |
| SC accuracy | 80% | 69% | **73%** |
| Time (s) | 104 | 175 | **280** |

**C0 gate: PASS** (multi-candidate rate 46% >= 20% threshold)

### Observations

- Model generates substantial disagreement on hard problems (3:3 splits on multiple ProofWriter questions)
- `False` label problems are particularly challenging: only 3/6 correct via SC
- `Unknown` is over-predicted — appears as majority answer when gold is True or False
- Multi-candidate rate higher than expected, suggesting the 14B model has enough reasoning diversity for SICA

## Phase 4: Smoke Test — Full SICA Pipeline

Ran 2 multi-candidate ProofWriter problems through the complete SICA pipeline (trace generation → constraint extraction → dedup → MaxSAT scoring).

| Problem | Gold | SICA | SC | SC Votes | Constraints | Satisfied Ratio | Time |
|---------|------|------|----|----------|-------------|-----------------|------|
| AttNeg-OWA-D5-347_Q11 | True | Unknown (X) | Unknown (X) | 5/6 | 26 | 25/26 = 96.2% | 43.3s |
| RelNeg-OWA-D5-498_Q8 | False | True (X) | True (X) | 6/6 | 21 | 20/21 = 95.2% | 33.6s |

- **Pipeline functional**: All stages (trace gen, constraint extraction, dedup, MaxSAT) completed without errors
- **SICA agreed with SC** on both problems — neither method rescued these hard cases
- **Constraint extraction working**: 21-26 constraints extracted per problem, high satisfaction ratios
- **Latency**: ~33-43s per problem with K=6 (acceptable for batch evaluation)

## Summary

| Phase | Status | Key Result |
|-------|--------|------------|
| Phase 0: 5th Q verification | DONE | SICA=SC=80% on 5 QwQ-32B questions |
| Phase 1: Stop QwQ-32B | DONE | GPU freed |
| Phase 2: Deploy Qwen2.5-14B | DONE | vLLM serving, 27.6 GiB GPU memory |
| Phase 3: C0 precheck | **PASS** | Multi-candidate 46% (>=20%), SC 73% |
| Phase 4: Smoke test | DONE | Pipeline end-to-end functional |

**Next steps**: Full evaluation (30 FOLIO + 30 ProofWriter) with K=12 to compare SICA vs SC accuracy on the new model.
