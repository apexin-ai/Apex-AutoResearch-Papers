# code check scalar unc mode

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-scalar-unc-mode_20260515T013823_result.json`
- **Structured JSON:** [`de8ecc1cfa00367e3b45.json`](../../sessions/de/de8ecc1cfa00367e3b45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息齐全。

`evaluate.py` 中 `--mode` 的可选值（第67行）：
`vla_only`, `crm_scalar`, `crm_perdof`, `acr_vla`, `crm_obs_only`, `reconvla`

scalar_unc 对应的 mode 就是 **`crm_scalar`**。关键差异：
- `crm_scalar` → `unc_dim = 3`（标量不确定性）
- `crm_perdof` / `acr_vla` → `unc_dim = 40`（逐自由度不确定性）
- `crm_obs_only` → `unc_dim = 0`

在 `select_action_crm` 中（第178-179行），`crm_scalar` 模式会通过 `_to_scalar_uf()` 将不确定性特征压缩为标量形式后送入 CRM。

完整可执行命令：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1"
```

注意加了 `CUDA_VISIBLE_DEVICES=2` 以绑定 cuda:2。

---
