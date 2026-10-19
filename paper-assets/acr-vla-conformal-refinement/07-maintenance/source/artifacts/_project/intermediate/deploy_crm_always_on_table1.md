# CRM Always-On (τ=0.001) Deployment Plan — Table 1

**Purpose**: K=2 CRM always-on baseline. τ=0.001 ensures L2 distance always exceeds threshold → CRM triggers every step.
**Mode**: adaptive_conformal_crm (no code change needed)
**Parameters**: K=2, τ=0.001, max_correction_norm=0.2, n_rollouts=20

## Command Template

```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark {SUITE} --K 2 --seed {SEED} --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_{SUITE}_crm_always_on_k2_norm0.2_seed{SEED}.json"
```

## Server/GPU Assignment (deploy when current τ-sweep completes)

### bjb1-18228 (4 GPUs)

| exp_id | GPU | Suite | Seed |
|--------|-----|-------|------|
| crm-always-on-object-s42 | cuda:0 | object | 42 |
| crm-always-on-object-s43 | cuda:1 | object | 43 |
| crm-always-on-object-s44 | cuda:2 | object | 44 |
| crm-always-on-spatial-s42 | cuda:3 | spatial | 42 |

### bjb1-32546 (4 of 6 GPUs)

| exp_id | GPU | Suite | Seed |
|--------|-----|-------|------|
| crm-always-on-spatial-s43 | cuda:0 | spatial | 43 |
| crm-always-on-spatial-s44 | cuda:1 | spatial | 44 |
| crm-always-on-goal-s42 | cuda:2 | goal | 42 |
| crm-always-on-goal-s43 | cuda:3 | goal | 43 |

### bjb2-28827 (4 of 6 GPUs)

| exp_id | GPU | Suite | Seed |
|--------|-----|-------|------|
| crm-always-on-goal-s44 | cuda:0 | goal | 44 |
| crm-always-on-long-s42 | cuda:1 | long | 42 |
| crm-always-on-long-s43 | cuda:2 | long | 43 |
| crm-always-on-long-s44 | cuda:3 | long | 44 |

**Spare GPUs**: bjb1-32546 cuda:4,5 + bjb2-28827 cuda:4,5 (4 spare, available for Pi05 always-on if Director decides)

## Full Commands (copy-paste ready for submit_training_job)

### Object

1. **crm-always-on-object-s42** → bjb1-18228 cuda:0
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark object --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_object_crm_always_on_k2_norm0.2_seed42.json"
```

2. **crm-always-on-object-s43** → bjb1-18228 cuda:1
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark object --K 2 --seed 43 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_object_crm_always_on_k2_norm0.2_seed43.json"
```

3. **crm-always-on-object-s44** → bjb1-18228 cuda:2
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark object --K 2 --seed 44 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_object_crm_always_on_k2_norm0.2_seed44.json"
```

### Spatial

4. **crm-always-on-spatial-s42** → bjb1-18228 cuda:3
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_spatial_crm_always_on_k2_norm0.2_seed42.json"
```

5. **crm-always-on-spatial-s43** → bjb1-32546 cuda:0
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --K 2 --seed 43 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_spatial_crm_always_on_k2_norm0.2_seed43.json"
```

6. **crm-always-on-spatial-s44** → bjb1-32546 cuda:1
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --K 2 --seed 44 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_spatial_crm_always_on_k2_norm0.2_seed44.json"
```

### Goal

7. **crm-always-on-goal-s42** → bjb1-32546 cuda:2
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_goal_crm_always_on_k2_norm0.2_seed42.json"
```

8. **crm-always-on-goal-s43** → bjb1-32546 cuda:3
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --K 2 --seed 43 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_goal_crm_always_on_k2_norm0.2_seed43.json"
```

9. **crm-always-on-goal-s44** → bjb2-28827 cuda:0
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --K 2 --seed 44 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_goal_crm_always_on_k2_norm0.2_seed44.json"
```

### Long

10. **crm-always-on-long-s42** → bjb2-28827 cuda:1
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed42.json"
```

11. **crm-always-on-long-s43** → bjb2-28827 cuda:2
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 43 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed43.json"
```

12. **crm-always-on-long-s44** → bjb2-28827 cuda:3
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 44 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed44.json"
```

## Hypothesis

All 12 experiments share the same hypothesis:
"K=2 CRM always-on (τ≈0, every-step correction) as Table 1 ablation baseline. Controls for K=2 sampling budget while removing conformal gating, isolating the value of selective triggering vs. blanket correction."

## Timeline

- Current 22 experiments started ~12:30-13:40 UTC (May 27)
- Each eval takes ~3-4h → expected completion ~16:30-17:40 UTC
- Deploy 12 always-on immediately after → complete by ~20:30-21:40 UTC
- DDL: May 28 12:00 UTC (20:00 Beijing) — ~10h margin
