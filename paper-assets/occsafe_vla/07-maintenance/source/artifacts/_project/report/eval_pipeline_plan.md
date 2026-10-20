# V2 Eval Pipeline Plan
> Generated: 2026-05-27 ~09:45 UTC | Deadline: 2026-05-28 12:00 UTC

---

## ⚠️ CRITICAL: 2 Experiments Crashed on westd-10894

| Experiment | GPU | Crash Time | Last Checkpoint | Steps Remaining |
|-----------|-----|-----------|----------------|-----------------|
| detach_ln_v2_s0c_r2 | cuda:2 | 14:29:15 local | 20000 | 30005 (~7.7h) |
| full_occ_ln_v2_s0d | cuda:3 | 15:10:46 local | 20000 | 30005 (~7.7h) |

**Action required**: Restart both with `--resume` from 20k checkpoint immediately. GPUs 2,3 on 10894 are idle (0% util, 0 MiB).

---

## 1. Training Status Summary

### westd-34685 (all 4 GPUs busy)
| Experiment | GPU | Step | Progress | ETA (remaining) | Est. Completion (UTC) |
|-----------|-----|------|----------|----------------|----------------------|
| detach_ln_v2_s1_35 | cuda:0 | ~28417/50005 | 57% | ~5.5h | ~15:15 |
| detach_ln_s4 | cuda:1 | ~28454/50005 | 57% | ~5.5h | ~15:15 |
| ablation_occ_detach_s4 | cuda:2 | ~25594/50005 | 51% | ~6.3h | ~16:00 |
| mvp_occ_s4 | cuda:3 | ~25587/50005 | 51% | ~6.3h | ~16:00 |

### westd-10894
| Experiment | GPU | Step | Progress | ETA (remaining) | Est. Completion (UTC) |
|-----------|-----|------|----------|----------------|----------------------|
| full_occ_ln_v2_s1c_r2 | cuda:0 | ~22784/50005 | 45% | ~7.0h | ~16:45 |
| full_occ_ln_v2_s2_r2 | cuda:1 | ~22800/50005 | 45% | ~7.0h | ~16:45 |
| detach_ln_v2_s0c_r2 | cuda:2 | **CRASHED** | — | needs restart | ~17:30 (if restarted now) |
| full_occ_ln_v2_s0d | cuda:3 | **CRASHED** | — | needs restart | ~17:30 (if restarted now) |

---

## 2. Eval Script

**Script**: `/root/occsafe_vla/openvla-oft/vla-scripts/evaluate_safelibero.py`
- Also available at: `/root/occsafe_vla/eval/eval_safelibero.py`
- Config via draccus dataclass, not argparse
- Key params: `--pretrained_checkpoint`, `--num_rollouts 50`, `--task_suite_name libero_spatial`
- Default `num_rollouts` is 20 — **must override to 50**
- Env vars needed: `MUJOCO_GL=egl`, `CUDA_VISIBLE_DEVICES=<GPU>`, `MUJOCO_EGL_DEVICE_ID=<PHYS_GPU>`

**Checkpoint path pattern**:
```
/root/autodl-tmp/checkpoints/<exp_name>/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--<run_id_note>
```
The final checkpoint (latest, no step suffix) is the one to use for eval.

---

## 3. Eval Commands — 8 Experiments

### westd-34685

**Exp 1: detach_ln_v2_s1_35** (cuda:0, ETA ~15:15 UTC)
```bash
CUDA_VISIBLE_DEVICES=0 MUJOCO_EGL_DEVICE_ID=0 MUJOCO_GL=egl \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s1 \
  --task_suite_name libero_spatial \
  --num_rollouts 50
```

**Exp 2: detach_ln_s4** (cuda:1, ETA ~15:15 UTC)
```bash
CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 MUJOCO_GL=egl \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s4 \
  --task_suite_name libero_spatial \
  --num_rollouts 50
```

**Exp 3: ablation_occ_detach_s4** (cuda:2, ETA ~16:00 UTC)
```bash
CUDA_VISIBLE_DEVICES=2 MUJOCO_EGL_DEVICE_ID=2 MUJOCO_GL=egl \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/ablation_occ_detach_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s4 \
  --task_suite_name libero_spatial \
  --num_rollouts 50
```

**Exp 4: mvp_occ_s4** (cuda:3, ETA ~16:00 UTC)
```bash
CUDA_VISIBLE_DEVICES=3 MUJOCO_EGL_DEVICE_ID=3 MUJOCO_GL=egl \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/mvp_occ_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--mvp_occ_s4 \
  --task_suite_name libero_spatial \
  --num_rollouts 50
```

### westd-10894

**Exp 5: full_occ_ln_v2_s1c_r2** (cuda:0, ETA ~16:45 UTC)
```bash
CUDA_VISIBLE_DEVICES=0 MUJOCO_EGL_DEVICE_ID=0 MUJOCO_GL=egl \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s1c \
  --task_suite_name libero_spatial \
  --num_rollouts 50
```

**Exp 6: full_occ_ln_v2_s2_r2** (cuda:1, ETA ~16:45 UTC)
```bash
CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 MUJOCO_GL=egl \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s2 \
  --task_suite_name libero_spatial \
  --num_rollouts 50
```

**Exp 7: detach_ln_v2_s0c_r2** (cuda:2, CRASHED — needs restart first, ETA ~17:30 UTC if restarted now)
```bash
CUDA_VISIBLE_DEVICES=2 MUJOCO_EGL_DEVICE_ID=2 MUJOCO_GL=egl \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s0c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s0c \
  --task_suite_name libero_spatial \
  --num_rollouts 50
```

**Exp 8: full_occ_ln_v2_s0d** (cuda:3, CRASHED — needs restart first, ETA ~17:30 UTC if restarted now)
```bash
CUDA_VISIBLE_DEVICES=3 MUJOCO_EGL_DEVICE_ID=3 MUJOCO_GL=egl \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s0d/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s0d \
  --task_suite_name libero_spatial \
  --num_rollouts 50
```

---

## 4. Scheduling Logic

**Principle: eval immediately on each GPU as its training finishes. Don't wait for all 8.**

### Wave 1 (~15:15 UTC): 34685 cuda:0,1
- detach_ln_v2_s1_35 and detach_ln_s4 finish → start eval on cuda:0 and cuda:1

### Wave 2 (~16:00 UTC): 34685 cuda:2,3
- ablation_occ_detach_s4 and mvp_occ_s4 finish → start eval on cuda:2 and cuda:3

### Wave 3 (~16:45 UTC): 10894 cuda:0,1
- full_occ_ln_v2_s1c_r2 and full_occ_ln_v2_s2_r2 finish → start eval on cuda:0 and cuda:1

### Wave 4 (~17:30 UTC): 10894 cuda:2,3 (if restarted promptly)
- detach_ln_v2_s0c_r2 and full_occ_ln_v2_s0d finish → start eval on cuda:2 and cuda:3

### Eval completion estimate:
- Each eval: ~1-1.5h (50 rollouts × 10 tasks, action chunking 8-step)
- Wave 1 evals done by ~16:45 UTC
- Wave 4 evals done by ~19:00 UTC
- All evals done by ~19:00 UTC May 27 — well before deadline

---

## 5. Gradient Analysis v2

### Script
`/root/occsafe_vla/scripts/gradient_analysis_v2.py` (exists on westd-34685 only)

**Note**: `run_gradient_analysis_v2.py` does NOT exist. The script runs directly.

### Already-completed checkpoints for 5 conditions

| Condition | Checkpoint | Server |
|-----------|-----------|--------|
| Cell 1: Full OCC BN | `/root/autodl-tmp/checkpoints/full_occ_bn_v2_s1/openvla-7b+...--full_occ_bn_v2_s1` | westd-34685 |
| Cell 2: Full OCC LN | `/root/autodl-tmp/checkpoints/full_occ_ln_s3_v2/openvla-7b+...--full_occ_ln_s3_v2` | westd-10894 |
| Cell 3: Detach BN | `/root/autodl-tmp/checkpoints/detach_bn_v2_s0/openvla-7b+...--detach_bn_v2_s0` | westd-34685 |
| Cell 4: Detach LN | `/root/autodl-tmp/checkpoints/detach_ln_s3/openvla-7b+...--detach_ln_s3` | westd-34685 (v1) |
| Vanilla | `/root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+...--vanilla_v2_s1` | westd-34685 |

**Issue**: Cell 2 completed checkpoint is only on 10894. Cell 4 only has v1 checkpoint on 34685.

### Options:
1. **Run gradient analysis on 10894** — copy the script there, use local Cell 2 checkpoint, but Cell 1/3/Vanilla are on 34685
2. **Run on 34685 after training finishes** — use a free GPU, but Cell 2 checkpoint needs to be copied from 10894
3. **Split runs** — run Cell 2 separately on 10894, rest on 34685, merge results

**Recommended**: Wait for currently-training v2 checkpoints to finish. Once training completes, we'll have all 5 conditions with v2 checkpoints. Run gradient analysis on whichever server has the most conditions locally available.

### Gradient analysis config JSON template (for 34685, assuming checkpoints copied/available):
```json
{
  "Cell1_FullOCC_BN": {"checkpoint_dir": "/root/autodl-tmp/checkpoints/full_occ_bn_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_bn_v2_s1"},
  "Cell2_FullOCC_LN": {"checkpoint_dir": "<TO_BE_FILLED>"},
  "Cell3_Detach_BN": {"checkpoint_dir": "/root/autodl-tmp/checkpoints/detach_bn_v2_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_bn_v2_s0"},
  "Cell4_Detach_LN": {"checkpoint_dir": "<TO_BE_FILLED_AFTER_TRAINING>"},
  "Vanilla": {"checkpoint_dir": "/root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1"}
}
```

### Launch command:
```bash
CUDA_VISIBLE_DEVICES=<FREE_GPU> \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla && \
python scripts/gradient_analysis_v2.py \
  --config /root/occsafe_vla/gradient_v2_config.json \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --num_batches 200
```

Est. time: ~2h for all 5 conditions sequentially.

---

## 6. Timeline Summary

| Time (UTC) | Event |
|------------|-------|
| **NOW** | ⚠️ Restart crashed detach_ln_v2_s0c_r2 + full_occ_ln_v2_s0d on 10894 |
| ~15:15 | 34685: detach_ln_v2_s1_35 + detach_ln_s4 finish → start eval |
| ~16:00 | 34685: ablation_occ_detach_s4 + mvp_occ_s4 finish → start eval |
| ~16:45 | 34685 Wave 1 evals done; 10894: s1c + s2 finish → start eval |
| ~17:00 | 34685: Start gradient analysis on free GPU |
| ~17:30 | 34685 Wave 2 evals done; 10894: restarted exps finish → start eval |
| ~18:15 | 10894 Wave 3 evals done |
| ~19:00 | All 8 evals done; gradient analysis done |
| **May 28 12:00** | Deadline — ~17h buffer ✅ |

---

## 7. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Crashed exps not restarted promptly | Push timeline by hours | Restart NOW with --resume |
| Eval script fails (dependency/config) | Blocks all evals | Dry-run one eval command on 34685 using existing detach_bn_v2_s0 checkpoint before training finishes |
| Gradient analysis checkpoint mismatch | Delays analysis | Use existing v1 checkpoints as fallback for Cell 4 |
| EGL device mismatch | Eval hangs or wrong GPU | Always match MUJOCO_EGL_DEVICE_ID to physical GPU index |
