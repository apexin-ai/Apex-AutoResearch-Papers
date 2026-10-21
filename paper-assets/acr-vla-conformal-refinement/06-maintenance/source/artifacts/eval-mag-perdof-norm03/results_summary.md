# eval-mag-perdof-norm03 Results

**Experiment**: CRM v3-norm per-DoF, max_correction_norm=0.3, LIBERO spatial benchmark
**CRM checkpoint**: `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt` (337,438 params)
**Config**: n_rollouts=10, max_steps=300, seed=42, K=10, mode=acr_vla

## Per-Task Results

| Task | Description | Success | Rate |
|------|-------------|---------|------|
| T0 | between_plate_and_ramekin | 7/10 | 70.0% |
| T1 | next_to_ramekin | 5/10 | 50.0% |
| T2 | from_table_center | 1/10 | 10.0% |
| T3 | on_cookie_box | 1/10 | 10.0% |
| T4 | in_top_drawer | 0/10 | 0.0% |
| T5 | on_ramekin | 0/10 | 0.0% |
| T6 | next_to_cookie_box | 9/10 | 90.0% |
| T7 | on_stove | 1/10 | 10.0% |
| T8 | next_to_plate | 2/10 | 20.0% |
| T9 | on_wooden_cabinet | 0/10 | 0.0% |
| **Overall** | **10 tasks** | **26/100** | **26.0%** |

## Notes

- Process exited normally (EXIT_CODE=0)
- Server: bjb2-28827
- Log: `/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm03.log`
