# ops disk cleanup plan 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-plan-35807_20260528T232051_result.json`
- **Structured JSON:** [`7bc6dcfb0f0da2d934b6.json`](../../sessions/7b/7bc6dcfb0f0da2d934b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，以下是清理清单。

---

## 空目录 / 近空目录（可直接删除）

| 路径 | 内容 | 大小 |
|------|------|------|
| `.../a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005_p2abl/` | 仅 wandb_id.txt，无 checkpoint | 4K |
| `.../a1_sdf_pi05_object_pudding/phase2_lambda0_s0_stage1/` | 仅 wandb_id.txt，无 checkpoint | 4K |
| `.../a1_sdf_pi05_object_pudding/phase2_stage1_seed0_l005_v3/` | 仅 wandb_id.txt，无 checkpoint | 4K |
| `.../a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed1/30000/` | 空目录（0 bytes，find -empty 检出） | 0 |

小计: ≈ 0 GB（可忽略，但清理目录结构）

---

## 中间 checkpoint（删除候选）

所有路径前缀: `/root/autodl-tmp/checkpoints/`

### a1_sdf_pi05_object_pudding_seed0_l0
保留: `best/` (7.2G), `12000/` (7.2G, 最高 step)
删除:
- `10000/` — **7.2 GB**

### a1_sdf_pi05_object_pudding_seed0_l005
仅有 `30000/` (7.2G) — **无需清理**

### a1_sdf_pi05_object_pudding_seed0_l01
仅有 `30000/` (7.2G) — **无需清理**

### a1_sdf_pi05_object_pudding_seed0_l1
保留: `best/` (7.2G), `30000/` (7.2G, 最高 step)
删除:
- `29999/` — **7.2 GB**

### a1_sdf_pi05_object_pudding_seed1_l005
保留: `best/` (15G), `30000/` (7.2G, 最高 step)
删除:
- `29999/` — **7.2 GB**

### a1_sdf_pi05_object_pudding_seed1_l01
保留: `best/` (15G), `30000/` (7.2G, 最高 step)
删除:
- `29999/` — **7.2 GB**

### a1_sdf_pi05_object_pudding_seed1_l1
保留: `best/` (7.2G), `30000/` (7.2G, 最高 step)
删除:
- `29999/` — **7.2 GB**

### a1_sdf_pi05_object_pudding_seed2_l0
保留: `best/` (7.2G), `18000/` (7.2G, 最高 step)
删除:
- `16000/` — **7.2 GB**

### a1_sdf_pi05_object_pudding_seed2_l005
保留: `best/` (15G), `30000/` (7.2G, 最高 step)
删除:
- `29999/` — **7.2 GB**

### a1_sdf_pi05_object_pudding_seed2_l01
保留: `best/` (15G), `30000/` (7.2G, 最高 step)
删除:
- `29999/` — **7.2 GB**

### phase2_stage1_seed0_l005
保留: `best/` (7.2G), `10000/` (7.2G, 最高 step)
删除:
- `9999/` — **7.2 GB**

### pi05_lora_baseline_object_pudding_seed0
仅有 `30000/` (7.2G) — **无需清理**

### a1_sdf_pi05_spatial_bowl_seed0_l005
保留: `best/` (7.2G), `30000/` (7.2G, 最高 step)
删除:
- `29999/` — **7.2 GB**

### pi05_lora_baseline_spatial_bowl_seed0
保留: `best/` (7.2G), `30000/` (7.2G, 最高 step)
删除:
- `29999/` — **7.2 GB**

---

## 汇总

| 类别 | 项数 | 预估回收空间 |
|------|------|-------------|
| 空/近空目录 | 4 个 | ≈ 0 GB |
| 中间 checkpoint | 11 个目录 | **79.2 GB** |
| **总计** | **15 项** | **≈ 79.2 GB** |

清理后数据盘可用空间预计从 4.3 GB 增至 ~83.5 GB（约 24% 可用）。等你确认后再执行删除。

---
