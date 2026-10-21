# DDL-Critical Eval Plan (Updated 04:17 UTC May 28)
# All libero_object experiments abandoned per Director decision.
# Focus: 3 DDL-critical factorial experiments on 34685 + 1 on 10894
# batch_idx reset bug: processes won't auto-exit, manual kill required after 50000_chkpt

## Eval 1+2 FIRST (~06:28 UTC), then Eval 0 (~08:42 UTC)

## Eval 0: detach_ln_v2_s2 (Cell 4, seed 44) — THIRD to trigger
- Trigger: ~08:42 UTC May 28 (batch_idx 25000 needed, currently at 7740)
- Server: westd-34685, GPU: cuda:0 (kill PID 47162 first)
- MUJOCO_EGL_DEVICE_ID: 0
- Checkpoint: /root/autodl-tmp/checkpoints/detach_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s2--50000_chkpt
- STATUS: TRAINING (PID 47162, batch_idx ~7740/50005, ~1.08 it/s)
- Command:
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python3 vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s2--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42"
```
- Expected: Cell 4 n=2→n=3 (CRITICAL: reaches ANOVA minimum)
- Registry: detach_ln_v2_s2_eval

## Eval 1: full_occ_ln_v2_s3 (Cell 2, seed 47) — FIRST to trigger
- Trigger: ~06:28 UTC May 28 (batch_idx 10000 needed, currently at 1310)
- Server: westd-34685, GPU: cuda:2 (kill PID 56474 first)
- MUJOCO_EGL_DEVICE_ID: 2
- STATUS: TRAINING (PID 56474, batch_idx ~1310/50005, ~1.08 it/s)
- Checkpoint: /root/autodl-tmp/checkpoints/full_occ_ln_v2_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s3--50000_chkpt
- Command:
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 python3 vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s3--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42"
```
- Expected: Cell 2 n=4→n=5 (5th seed)
- Registry: full_occ_ln_v2_s3_eval

## Eval 2: detach_ln_v2_s3 (Cell 4, seed 45) — FIRST to trigger (parallel with Eval 1)
- Trigger: ~06:28 UTC May 28 (batch_idx 10000 needed, currently at 1313)
- Server: westd-34685, GPU: cuda:3 (kill PID 56822 first)
- MUJOCO_EGL_DEVICE_ID: 3
- STATUS: TRAINING (PID 56822, batch_idx ~1313/50005, ~1.09 it/s)
- Checkpoint: /root/autodl-tmp/checkpoints/detach_ln_v2_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s3--50000_chkpt
- Command:
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 python3 vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s3--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42"
```
- Expected: Cell 4 n=2→n=3 (critical: reaches minimum for ANOVA)
- Registry: detach_ln_v2_s3_eval

## SafeLIBERO 10 Tasks Coverage
evaluate_safelibero.py with --task_suite_name libero_spatial covers all 10 tasks:
T0: bowl_between_plate_ramekin
T1: bowl_next_to_ramekin
T2: bowl_from_table_center
T3: bowl_on_cookie_box
T4: bowl_in_top_drawer
T5: bowl_on_ramekin
T6: bowl_next_to_cookie_box
T7: bowl_on_stove
T8: bowl_next_to_plate
T9: bowl_on_wooden_cabinet

Each task: 50 rollouts = 500 total episodes
Output: TSR, CAR, per-task breakdown, collision counts

## Eval 3: detach_ln_v2_s4 (Cell 4, seed 46) — post-DDL risk
- Trigger: ~11:40 UTC May 28 (only 20min before DDL)
- Server: westd-10894, GPU: cuda:1
- MUJOCO_EGL_DEVICE_ID: 1
- Checkpoint: /root/autodl-tmp/checkpoints/detach_ln_v2_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s4--50000_chkpt
- NOTE: Eval takes ~45min, so this likely won't finish before DDL 12:00 UTC. Include only if training finishes early enough.

## Post-Eval
After Eval 1+2 complete (~07:15 UTC) and Eval 0 (~09:30 UTC):
1. Update registry with metrics
2. Rerun statistical_tests.py with full data (Cell 2 n=5, Cell 4 n=3 or n=4)
3. Update ANOVA table, Table 1/2 in paper
4. Update figures (factorial_2x2, fig1_overview)
5. Final compile
6. DDL 12:00 UTC — Eval 0+1+2 results should all be in by ~09:30 UTC
