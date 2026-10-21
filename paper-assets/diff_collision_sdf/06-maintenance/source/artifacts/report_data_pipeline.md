# LIBERO → ColliForce-VLA Training Data Pipeline Report

## Summary

Built and executed a complete data pipeline that extracts training data from LIBERO expert demonstrations and packages it into HDF5 files compatible with openpi (pi0) training format, with additional EE position GT and SDF GT for collision-aware fine-tuning.

## Output Files

| File | Size | Episodes | Avg Length |
|------|------|----------|------------|
| `spatial_bowl_train.hdf5` | 403.4 MB | 50 | 101 steps |
| `object_chocolate_train.hdf5` | 715.9 MB | 50 | 160 steps |

Location: `/root/autodl-tmp/colliforce_data/`

## Data Format (per episode)

| Field | Shape | Dtype | Description |
|-------|-------|-------|-------------|
| `observations/agentview` | [T, 224, 224, 3] | uint8 | Third-person camera (resized from 128x128) |
| `observations/eye_in_hand` | [T, 224, 224, 3] | uint8 | Wrist camera (resized from 128x128) |
| `observations/state` | [T, 8] | float32 | ee_pos(3) + ee_axisangle(3) + gripper(2) |
| `actions` | [T, 7] | float32 | Delta EE: pos(3) + rot(3) + gripper(1) |
| `ee_positions` | [T, 3] | float32 | EE position GT (world frame) |

### Per-scene SDF GT

| Field | Shape | Description |
|-------|-------|-------------|
| `sdf_gt/query_points` | [N, 3] | 3D query positions |
| `sdf_gt/sdf_values` | [N] | Signed distance, range [-0.05, 0.05] |

## Task Details

### spatial_bowl
- **Task**: pick up the black bowl between the plate and the ramekin and place it on the plate
- **Suite**: libero_spatial, index 0
- **Episodes**: 50, length range [75, 168], avg 101
- **Action range**: [-1.0, 1.0]
- **EE pos range**: x=[-0.229, 0.118], y=[-0.030, 0.201], z=[0.910, 1.199]
- **SDF GT**: 4076 points

### object_chocolate
- **Task**: pick up the chocolate pudding and place it in the basket
- **Suite**: libero_object, index 8
- **Episodes**: 50, length range [145, 224], avg 160
- **Action range**: [-1.0, 1.0]
- **EE pos range**: x=[-0.159, 0.097], y=[-0.275, 0.315], z=[0.008, 0.336]
- **SDF GT**: 4084 points

## Alignment with openpi Format

The output aligns with openpi's `LeRobotLiberoDataConfig`:
- **State**: 8-dim = eef_pos(3) + eef_axisangle(3) + gripper_qpos(2), matching `observation/state` in openpi
- **Actions**: 7-dim delta EE (already deltas in LIBERO, no conversion needed)
- **Images**: 224x224 RGB, matching pi0 input resolution
- **Additional fields**: `ee_positions` (EE GT for collision loss) and `sdf_gt` (scene-level SDF) are extensions not in standard openpi but needed for ColliForce-VLA

## Key Design Decisions

1. **Direct extraction over MuJoCo replay**: The LIBERO demo HDF5 files contain stored observations (`agentview_rgb`, `ee_pos`, `ee_ori`, `gripper_states`), eliminating the need for MuJoCo state replay. This is faster and avoids MuJoCo rendering dependencies.

2. **Orientation format**: The LIBERO demos store `ee_ori` as 3D axis-angle (not quaternion). No conversion needed — the values map directly to the openpi state format.

3. **Image resizing**: Source images are 128x128, resized to 224x224 via PIL bilinear interpolation to match pi0's expected resolution.

4. **EE position GT = ee_pos**: The EE position ground truth is extracted directly from the stored `ee_pos` observations, which are the same as `robot0_eef_pos` in MuJoCo — the 3D world-frame position of the robot end-effector.

## Pipeline Script

`/root/colliforce-vla/generate_training_data.py`

Key features:
- Auto-detects HDF5 observation key naming conventions (handles both `robot0_eef_pos`/`ee_pos` styles)
- Auto-detects orientation format (quaternion vs axis-angle)
- Gzip-compressed image storage
- Outputs per-task statistics and `pipeline_results.json`
- torch.load monkeypatch for torch 2.8 compatibility

## Source Data

Downloaded from HuggingFace `yifengzhu-hf/LIBERO-datasets` via direct HTTP:
- `libero_spatial/pick_up_the_black_bowl_..._demo.hdf5` (485.2 MB)
- `libero_object/pick_up_the_chocolate_pudding_..._demo.hdf5` (760.4 MB)

Stored at `/root/autodl-tmp/libero_datasets/`
