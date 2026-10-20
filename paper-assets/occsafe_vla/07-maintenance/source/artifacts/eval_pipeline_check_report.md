# Eval Pipeline Edge Case Check Report

Date: 2026-05-26

---

## 1. Checkpoint Path Pattern

### Naming Convention
Reference: `mvp_occ_s3_v2` on westd-10894 confirmed the exact pattern:
```
/root/autodl-tmp/checkpoints/{exp_id}/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--{exp_id}--50000_chkpt
```
All 8 eval commands match this pattern exactly.

### Experiment Directory Existence

| exp_id | Server | Dir Exists | Latest Checkpoint |
|--------|--------|-----------|-------------------|
| reverse_cutoff_s2_v2 | westd-10894 | YES | 30000_chkpt |
| full_occ_ln_v2_s0 | westd-10894 | YES | 10000_chkpt |
| full_occ_ln_v2_s1 | westd-10894 | YES | 10000_chkpt |
| detach_ln_v2_s0 | westd-10894 | YES | 10000_chkpt |
| vanilla_v2_s1 | westd-34685 | YES | 30000_chkpt |
| vanilla_v2_s2 | westd-34685 | YES | 30000_chkpt |
| detach_ln_s3 | westd-34685 | YES | 30000_chkpt |
| cutoff_25k_s1_v2 | westd-34685 | YES | 30000_chkpt |

- All 8 experiment directories exist on the correct servers.
- `--50000_chkpt` subdirectories do not yet exist (training in progress). This is expected given ETAs.
- Cross-validated: `mvp_occ_s3_v2` (completed) has `--50000_chkpt` directory with full model files (config.json, model.safetensors.index.json, lora_adapter/, dataset_statistics.json, tokenizer files).

### Verdict
- **Checkpoint path pattern**: CONFIRMED correct from completed experiment
- **exp_id spelling**: All match actual directory names on disk
- **50000_chkpt naming**: CONFIRMED from mvp_occ_s3_v2

---

## 2. Eval Script Parameter Consistency

Scripts are **identical** on both servers (verified head -100 output matches exactly).

| Parameter | In Command | In Script (dataclass default) | Status |
|-----------|-----------|------------------------------|--------|
| `--pretrained_checkpoint` | Full path | `""` | Correct param name |
| `--num_rollouts 50` | 50 | 20 (default) | Correct param name, correctly overrides default |
| `--seed 42` | 42 | 42 (default) | Correct (redundant but harmless) |
| `--task_suite_name libero_spatial` | libero_spatial | `"libero_spatial"` (default) | Correct |

Additional script parameters that use sane defaults:
- `collision_threshold`: 0.001 (not overridden, matches SafeLIBERO paper)
- `num_steps_wait`: 10 (warmup steps, not overridden)
- `use_l1_regression`: True (matches OFT training)
- `num_images_in_input`: 2 (matches OFT training)
- `use_proprio`: True (matches OFT training)
- `lora_rank`: 32 (matches training `lora-r32`)

### Verdict
- **All parameter names correct**
- **No `--num_trials_per_task` anywhere** — the correct name is `--num_rollouts`
- **Defaults align with training config**

---

## 3. Per-Task Output Format

Examined: `/root/occsafe_vla/artifacts/safelibero_libero_spatial_20260526_191231.json` (ablation_occ_detach_s3_v2, 50 rollouts)

### JSON Structure
```json
{
  "config": {
    "checkpoint": "/root/autodl-tmp/checkpoints/.../--50000_chkpt",
    "task_suite": "libero_spatial",
    "num_rollouts": 50,
    "collision_threshold": 0.001,
    "seed": 42
  },
  "tasks": {
    "<task_description_string>": {
      "task_id": 0,
      "n": 50,
      "successes": 50,
      "safe": 49,
      "tsr": 1.0,
      "car": 0.98,
      "obstacles": ["obj1", "obj2", ...],
      "episodes": [...]
    },
    ...
  },
  "per_episode": [
    {
      "task_id": 9,
      "task_name": "...",
      "episode_idx": 49,
      "max_displacement": 0.0,
      "collision_detected": false,
      "trajectory_length": 122,
      "task_success": true
    },
    ...
  ],
  "summary": {
    "total_episodes": 500,
    "tsr": 0.922,
    "car": 0.794,
    "total_collisions": 103,
    "displacement_stats": {
      "min": 0.0, "max": 0.738218, "mean": 0.007708, "median": 0.0
    }
  }
}
```

### Field Name Mapping
- Task-level: `tsr`, `car` (not `success_rate`, `collision_rate`)
- Summary-level: `tsr`, `car`
- Per-episode: `task_success`, `collision_detected`, `max_displacement`

### Verdict
- Format is well-structured and consistent with previous eval runs
- 500 episodes total = 10 tasks x 50 rollouts (correct for libero_spatial)

---

## 4. MUJOCO_EGL_DEVICE_ID Check

Rule: `MUJOCO_EGL_DEVICE_ID` must match **physical GPU number** (not CUDA logical index).
Since `CUDA_VISIBLE_DEVICES=N` maps to a single physical GPU, `MUJOCO_EGL_DEVICE_ID=N` must equal the same physical GPU.

| Experiment | Server | CUDA_VISIBLE_DEVICES | MUJOCO_EGL_DEVICE_ID | Match? |
|-----------|--------|---------------------|---------------------|--------|
| reverse_cutoff_s2_v2 | westd-10894 | 0 | 0 | YES |
| full_occ_ln_v2_s0 | westd-10894 | 1 | 1 | YES |
| full_occ_ln_v2_s1 | westd-10894 | 2 | 2 | YES |
| detach_ln_v2_s0 | westd-10894 | 3 | 3 | YES |
| vanilla_v2_s1 | westd-34685 | 0 | 0 | YES |
| vanilla_v2_s2 | westd-34685 | 1 | 1 | YES |
| detach_ln_s3 | westd-34685 | 2 | 2 | YES |
| cutoff_25k_s1_v2 | westd-34685 | 3 | 3 | YES |

### Verdict
- All 8 commands correctly pair CUDA_VISIBLE_DEVICES with MUJOCO_EGL_DEVICE_ID

---

## 5. Output Path

Commands do **not** specify `--output_path`. The script auto-generates:
```
/root/occsafe_vla/artifacts/safelibero_libero_spatial_YYYYMMDD_HHMMSS.json
```

The `config.checkpoint` field inside the JSON identifies which experiment the result belongs to.

---

## Summary

### Passed
- Checkpoint path pattern matches confirmed training output convention
- All 8 exp_id directories exist on correct servers with correct spelling
- Eval script parameters: `--num_rollouts`, `--seed`, `--task_suite_name`, `--pretrained_checkpoint` all correct
- Eval scripts identical on both servers
- MUJOCO_EGL_DEVICE_ID correctly matches physical GPU for all 8 commands
- JSON output format consistent across existing eval results
- libero_spatial correctly has 10 tasks, producing 500 total episodes at 50 rollouts

### Needs Attention
- **Output file identification**: No `--output_path` specified, so results are timestamp-named. After batch eval, must match results to experiments via `config.checkpoint` in each JSON. Consider adding `--output_path /root/occsafe_vla/artifacts/{exp_id}_eval.json` to each command for easier identification.
- **Field naming**: Registry code that reads results must use `tsr`/`car` (not `success_rate`/`collision_rate`). Verify downstream code matches.
- **Pre-launch check**: All 8 `--50000_chkpt` directories don't exist yet (training in progress). Each eval must only be launched after confirming `ls /root/autodl-tmp/checkpoints/{exp_id}/...-{exp_id}--50000_chkpt/config.json` exists.

### Must Fix
- (none found)
