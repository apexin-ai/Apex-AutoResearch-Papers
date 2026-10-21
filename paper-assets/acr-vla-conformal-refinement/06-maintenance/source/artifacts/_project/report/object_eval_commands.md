# Object Benchmark Eval Commands

Baseline reference: eval-object-v8-full (VLA-only K=1) = **13% success rate** (DONE)

---

## 1. eval-acr-object — ACR-VLA (per-DOF CRM)

- **exp_id**: `eval-acr-object`
- **Server**: bjb1-18228, GPU 0
- **Model**: ACR-VLA (SmolVLA + CRM per-DOF, K=10)
- **Checkpoint**: `/root/autodl-tmp/checkpoints/crm/crm_best.pt`
- **Est. runtime**: ~3-4h

```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode acr_vla \
  --benchmark object \
  --n_rollouts 10 \
  --seed 42 \
  --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-acr-object.log
```

---

## 2. eval-reconvla-object — SampleConsensus

- **exp_id**: `eval-reconvla-object`
- **Server**: bjb1-18228, GPU 1
- **Model**: SampleConsensus (scalar Euclidean argmin, K=10)
- **Checkpoint**: N/A (no CRM)
- **Est. runtime**: ~3-4h

```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode reconvla \
  --benchmark object \
  --n_rollouts 10 \
  --seed 42 \
  --K 10 \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-reconvla-object.log
```

---

## 3. eval-scalar-unc-object — Scalar CRM

- **exp_id**: `eval-scalar-unc-object`
- **Server**: bjb1-18228, GPU 2
- **Model**: CRM-scalar_unc (3D scalar uncertainty, K=10)
- **Checkpoint**: `/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt`
- **Est. runtime**: ~3-4h

```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode crm_scalar \
  --benchmark object \
  --n_rollouts 10 \
  --seed 42 \
  --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-scalar-unc-object.log
```

---

## 4. eval-vla-mean-object — K=10 Mean Action

- **exp_id**: `eval-vla-mean-object`
- **Server**: bjb2-40593, GPU 0
- **Model**: SmolVLA K=10 mean action (no conformal)
- **Checkpoint**: N/A (no CRM)
- **Est. runtime**: ~3-4h

```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode vla_only \
  --baseline_mode mean \
  --benchmark object \
  --n_rollouts 10 \
  --seed 42 \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-vla-mean-object.log
```

---

## 5. eval-k5-object — K=5 CRM

- **exp_id**: `eval-k5-object`
- **Server**: bjb1-18228, GPU 3
- **Model**: CRM per-DOF with K=5
- **Checkpoint**: `/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt` ⚠️ *pending crm-train-k5 completion*
- **Est. runtime**: ~3h

```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode crm_perdof \
  --benchmark object \
  --n_rollouts 10 \
  --seed 42 \
  --K 5 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm/k5/crm_best.pt \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-k5-object.log
```

---

## GPU Allocation Summary

| Server | GPU | Experiment | Dependency |
|--------|-----|-----------|------------|
| bjb1-18228 | 0 | eval-acr-object | spatial evals done |
| bjb1-18228 | 1 | eval-reconvla-object | spatial evals done |
| bjb1-18228 | 2 | eval-scalar-unc-object | spatial evals done |
| bjb1-18228 | 3 | eval-k5-object | crm-train-k5 done |
| bjb2-40593 | 0 | eval-vla-mean-object | eval-vla-mean-spatial done |

## Notes

- VLA-only K=1 baseline already done: eval-object-v8-full = 13% (no need to rerun)
- All commands use `MUJOCO_EGL_DEVICE_ID=0` (framework handles GPU remapping via CUDA_VISIBLE_DEVICES)
- n_rollouts=10, seed=42, matching spatial eval configuration
- eval-k5-object blocked on crm-train-k5 — verify checkpoint exists before launching
- Runtime estimates based on eval-object-v8-full (VLA-only K=1, ~3h on bjb2-40593 single 4090D); K=10 modes may be slightly slower
