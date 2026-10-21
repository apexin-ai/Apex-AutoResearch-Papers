# ssh training progress check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training_progress_check_20260520T022159_result.json`
- **Structured JSON:** [`28aa739bdd820f8a9283.json`](../../sessions/28/28aa739bdd820f8a9283.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部存活，registry 已更新。汇总：

| GPU | 实验 | Step | Loss | VRAM | ETA |
|-----|------|------|------|------|-----|
| cuda:0 | baseline_spatial_bowl_s0 | 3719/30000 (12%) | 0.019 | 37.4 GB | ~26h |
| cuda:1 | baseline_spatial_bowl_s1 | 3948/30000 (13%) | 0.031 | 37.4 GB | ~25h |
| cuda:2 | baseline_object_pudding_s0 | 3980/30000 (13%) | 0.020 | 37.4 GB | ~26h |
| cuda:3 | a1_sdf_spatial_bowl_s0 | 1962/30000 (7%) | 0.262 | 13.4 GB | ~30h |

**A1 Phase 2**: 未触发（step 1962 < 5000），VRAM 13.4GB 符合 Phase 1 预期，日志中无 transition 记录。预计 ~3.2h 后触发。

**Checkpoints**: 3 个 baseline 各有 1 个 ckpt（step 2000）；A1 有 5 个 ckpt（steps 1, 2, 500, 1000, 1500）。

**注意**: Registry 中 checkpoint_path 用的是扁平路径（如 `baseline_spatial_bowl_0/`），实际是嵌套结构（`baseline_spatial_bowl/baseline_spatial_bowl_seed0/`）。

---
