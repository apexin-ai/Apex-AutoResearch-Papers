# code mvp A 001 v2

**crosscoder behavioral circuit transplant** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-A-001-v2_20260510T130325_result.json`
- **Structured JSON:** [`38f21cecd6f752b22dfb.json`](../../sessions/38/38f21cecd6f752b22dfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
WORKER_RESULT:
status: completed
exp_id: mvp-A-001
server: home-1x5090
command: bash -c "export HF_HOME=/home/sonny/ssd2/sonny.fu/.hf_cache && source /home/sonny/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/crosscoder-bct && python3 mvp_experiment.py 2>&1 | tee /home/sonny/crosscoder-bct/run.log"
pid: (tmux session mvp-A-001, already completed)

RESULTS SUMMARY:
  Gate 1 (Crosscoder convergence): PASS — recon_loss 0.403→0.114, L0=457.6
  Gate 2 (Donor-exclusive features): PASS — 22 features with ratio>3.0 (top: feat[1353] ratio=6.93)
  Gate 3 (Activation movement ≥50%): FAIL — movement_ratio=0.62% (nearly zero effect)
  Gate 4 (PPL ≤1.05): PASS — ppl_ratio=1.0196
  Gate 5 (DA tokens loss ↓≥10%): FAIL — da_improvement=-0.28% (slightly worsened)
  Overall: FAIL

DIAGNOSIS:
  The rank-1 surgery formula (outer product projection on W_out) barely moved the target activations.
  scale=5.93 was applied but movement was only 0.6%. The surgery operated on feature k=1353
  which had low absolute activation (s_d_norm=0.178, s_t=0.026) — possibly too weak a feature
  to produce measurable behavioral change via a single rank-1 update on MLP W_out.

NOTE: Fixed a bug in TransformerLens 3.2.1 (line 1885 of loading_from_pretrained.py) where
Pythia checkpoint loading passed empty string as token causing httpx.LocalProtocolError.
```

---
