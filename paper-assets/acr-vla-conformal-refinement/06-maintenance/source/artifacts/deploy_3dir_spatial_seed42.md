# 3-Direction Quick Sanity Check: Spatial seed42

CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`
(bjb1-32546 and bjb2-40593 both have it)

All commands run from `/root/acr-vla-conformal-refinement/`.

## Direction A: max_correction_norm variants (crm_obs_only + norm clipping)

```bash
# norm=0.3 (relaxed)
tmux new-session -d -s dirA_norm03 "cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.3 2>&1 | tee logs/dirA_norm03_spatial_s42.log; echo EXIT=\${PIPESTATUS[0]}"

# norm=0.1 (moderate)
tmux new-session -d -s dirA_norm01 "cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.1 2>&1 | tee logs/dirA_norm01_spatial_s42.log; echo EXIT=\${PIPESTATUS[0]}"

# norm=0.05 (tight)
tmux new-session -d -s dirA_norm005 "cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.05 2>&1 | tee logs/dirA_norm005_spatial_s42.log; echo EXIT=\${PIPESTATUS[0]}"
```

## Direction B: Adaptive Conformal CRM (K=2, selective correction)

```bash
tmux new-session -d -s dirB_adaptive "cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 2>&1 | tee logs/dirB_adaptive_spatial_s42.log; echo EXIT=\${PIPESTATUS[0]}"
```

Default conformal_threshold=0.074855, max_correction_norm auto-set to 0.2.

## Direction C: ReconVLA (K-sample argmin, no CRM)

```bash
tmux new-session -d -s dirC_reconvla "cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode reconvla --benchmark spatial --seed 42 --n_rollouts 20 --K 10 2>&1 | tee logs/dirC_reconvla_spatial_s42.log; echo EXIT=\${PIPESTATUS[0]}"
```

## Monitor

```bash
# Check all logs
tail -3 logs/dir*_spatial_s42.log

# Check GPU usage
nvidia-smi --query-gpu=index,utilization.gpu,memory.used --format=csv,noheader

# Check tmux sessions
tmux ls
```

## Expected output files

```
logs/eval_spatial_crm_obs_only_norm0.3_seed42.json
logs/eval_spatial_crm_obs_only_norm0.1_seed42.json
logs/eval_spatial_crm_obs_only_norm0.05_seed42.json
logs/eval_spatial_adaptive_conformal_crm_tau0.074855_seed42.json
logs/eval_spatial_reconvla_seed42.json
```
