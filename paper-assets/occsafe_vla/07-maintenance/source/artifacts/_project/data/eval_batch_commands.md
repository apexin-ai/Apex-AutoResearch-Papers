# Eval Batch Commands — v2 Factorial + n=5 Runs

All evals: 50 rollouts/task, 10 tasks (libero_spatial), seed 42.
Eval takes ~50-55 min per experiment on a single GPU.

## Checkpoint Path Pattern

```
/root/autodl-tmp/checkpoints/<EXP_ID>/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--<EXP_ID>--50000_chkpt
```

## SSH Command Template (via ssh_execute)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=<GPU> MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/<EXP_ID>/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--<EXP_ID>--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42' > ~/runs/occsafe_vla/<EVAL_LOG>_eval.log 2>&1 &
echo "PID=$!"
```

---

## westd-10894 (4 experiments)

### 1. full_occ_ln_v2_s0d (Cell 2, seed 42, cuda:3)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s0d/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s0d--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42' > ~/runs/occsafe_vla/full_occ_ln_v2_s0d_eval.log 2>&1 &
echo "PID=$!"
```

### 2. full_occ_ln_v2_s1c_r2 (Cell 2, seed 43, cuda:0)
Actual checkpoint exp_id: `full_occ_ln_v2_s1c`

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s1c--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42' > ~/runs/occsafe_vla/full_occ_ln_v2_s1c_r2_eval.log 2>&1 &
echo "PID=$!"
```

### 3. full_occ_ln_v2_s2_r2 (Cell 2, seed 44, cuda:1)
Actual checkpoint exp_id: `full_occ_ln_v2_s2`

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s2--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42' > ~/runs/occsafe_vla/full_occ_ln_v2_s2_r2_eval.log 2>&1 &
echo "PID=$!"
```

### 4. detach_ln_v2_s0c_r2 (Cell 4, seed 42, cuda:2)
Actual checkpoint exp_id: `detach_ln_v2_s0c`

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s0c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s0c--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42' > ~/runs/occsafe_vla/detach_ln_v2_s0c_r2_eval.log 2>&1 &
echo "PID=$!"
```

---

## westd-34685 (4 experiments)

### 5. detach_ln_v2_s1_35 (Cell 4, seed 43, cuda:0)
Actual checkpoint exp_id: `detach_ln_v2_s1`

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s1--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42' > ~/runs/occsafe_vla/detach_ln_v2_s1_35_eval.log 2>&1 &
echo "PID=$!"
```

### 6. mvp_occ_s4 (Cell 1 n=5, seed 46, cuda:3)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/mvp_occ_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--mvp_occ_s4--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42' > ~/runs/occsafe_vla/mvp_occ_s4_eval.log 2>&1 &
echo "PID=$!"
```

### 7. ablation_occ_detach_s4 (Cell 3 n=5, seed 46, cuda:2)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/ablation_occ_detach_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s4--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42' > ~/runs/occsafe_vla/ablation_occ_detach_s4_eval.log 2>&1 &
echo "PID=$!"
```

### 8. detach_ln_s4 (Cell 4 n=5, seed 46, cuda:1)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s4--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42' > ~/runs/occsafe_vla/detach_ln_s4_eval.log 2>&1 &
echo "PID=$!"
```

---

## Monitoring Eval Progress

```bash
# Check if eval is still running
ps -p <PID> -o pid= 2>/dev/null && echo "RUNNING" || echo "DONE"

# Check progress (which task, which rollout)
tail -5 ~/runs/occsafe_vla/<exp>_eval.log

# Check final result
tail -20 ~/runs/occsafe_vla/<exp>_eval.log
# Look for: TSR = X.XXXX | CAR = X.XXXX
```

## Post-Eval: Collecting CAR Values

Results JSON saved to `/root/occsafe_vla/artifacts/safelibero_libero_spatial_<timestamp>.json`.
Extract CAR from the summary line in the log or from JSON:
```bash
grep "CAR" ~/runs/occsafe_vla/<exp>_eval.log
```

## Cell Mapping for ANOVA

| Cell | Gradient Flow | Norm Type | Experiments |
|------|--------------|-----------|-------------|
| Cell 1 (Full OCC BN) | ON | BN | mvp_occ_s4 (n=5 run) |
| Cell 2 (Full OCC LN) | ON | LN | full_occ_ln_v2_s0d, s1c_r2, s2_r2 |
| Cell 3 (Detach BN) | OFF | BN | ablation_occ_detach_s4 (n=5 run) |
| Cell 4 (Detach LN) | OFF | LN | detach_ln_v2_s0c_r2, s1_35, detach_ln_s4 (n=5 run) |
