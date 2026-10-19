# ssh eval precheck

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_precheck_20260521T071621_result.json`
- **Structured JSON:** [`0acf8635da9a6b1350a8.json`](../../sessions/0a/0acf8635da9a6b1350a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## Eval 预检报告

### 1. L1 norm 修复状态: **OK**
- `eval_safelibero.py:389` — `displacement = np.sum(np.abs(current_positions[name] - initial_positions[name]))` ✓
- `COLLISION_THRESHOLD = 0.001` (line 92) ✓
- `np.linalg.norm` 仅用于 shift_magnitude (305)、jerk smoothness (405)、debug display (627)，均不影响碰撞判定

### 2. eval_batch.sh 状态: **OK，但 A3 checkpoint 目录尚不存在**
- 语法检查: `bash -n` 通过
- scenes: `spatial_bowl`, `object_pudding` ✓
- methods: `baseline a1 a3 a3_no_refine` ✓
- 碰撞阈值: 继承自 eval_safelibero.py 默认 0.001（eval_batch.sh 不单独传 `--collision_threshold`）✓
- dry-run baseline spatial_bowl seed0 → 正确解析到 `checkpoints/baseline_spatial_bowl/baseline_spatial_bowl_seed0/30000` ✓
- dry-run a3 spatial_bowl → **SKIP: checkpoint dir not found** `a3_grad_refine_spatial_bowl/a3_grad_refine_spatial_bowl_seed0`（预期，A3 还在训练中）
- `--dry_run` 参数可用 ✓

### 3. norm_stats.json 状态: **OK**
- 每个 checkpoint step 目录内都自带 `assets/&lt;suite>/norm_stats.json`
- 项目级 `assets/` 目录也有备份副本
- eval 脚本通过 openpi 的 `load_norm_stats(checkpoint_dir / "assets", asset_id)` 加载，无需额外 symlink

### 4. Dry-run / Import 结果: **OK**
- `python scripts/eval_safelibero.py --help` 正常输出，所有 import 无报错
- eval_batch.sh dry-run 正确构建命令行

### 5. SDF GT 文件
- `sdf_gt_spatial_bowl.npz`: **存在** (112KB)
- `sdf_gt_object_pudding.npz`: **缺失** ⚠️ — A3 eval object_pudding 场景需要此文件

### 6. SCP 命令模板
- westd-35807 上无 `~/.ssh/config`，无法直接 SSH 到 westd-45947
- **需要从本地中转**，或在 westd-35807 上配置 SSH key
- A3 checkpoint 目标路径: `/root/autodl-tmp/checkpoints/a3_grad_refine_spatial_bowl/a3_grad_refine_spatial_bowl_seed0/&lt;step>/`
- 等 A3 训练完成后需确认 westd-45947 上的实际 checkpoint 路径再拷贝

### 7. Checkpoint 清单

| Method | Scene | Seed | Steps | 状态 |
|--------|-------|------|-------|------|
| baseline (full-FT) | spatial_bowl | 0 | 29999, 30000, best | ✅ 完成 |
| baseline (full-FT) | object_pudding | 0 | 29999, 30000, best | ✅ 完成 |
| baseline (LoRA) | spatial_bowl | 0 | 2000, 4000, best | ✅ 完成 |
| baseline (LoRA) | object_pudding | 0 | 2000, 4000, best | ✅ 完成 |
| A1 (full-FT) | spatial_bowl | 0 | 14000, 16000, 18000, best | ✅ 完成 |
| A1 (full-FT) | object_pudding | 0 | 4000, 6000, best | ✅ 完成 |
| A1 (LoRA) | spatial_bowl | 0 | _(空，仅 wandb_id.txt)_ | ⏳ 未开始/刚创建 |
| A1 (LoRA) | object_pudding | 0 | 2000, best | ✅ 有 checkpoint |
| A3 | * | * | — | ⏳ 训练中 (westd-45947) |

### 8. 磁盘空间
- `/root/autodl-tmp`: 350G total, 232G used, **119G free** (67%) — 足够存放 A3 checkpoint

### 需修复项

1. **`sdf_gt_object_pudding.npz` 缺失** — A3 eval object_pudding 需要此文件。需要从训练服务器拷贝或重新生成。
2. **westd-45947 → westd-35807 SCP 通道** — 两台机器间无直接 SSH 连接，需规划传输方案（本地中转 / 配置 SSH key / 用 autodl-tmp 共享存储等）。

---
