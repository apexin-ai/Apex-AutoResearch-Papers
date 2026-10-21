# ssh a3 dry run verify

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a3_dry_run_verify_20260520T022621_result.json`
- **Structured JSON:** [`03133443b58aa70494d8.json`](../../sessions/03/03133443b58aa70494d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总结果：

## A3 Dry-Run 验证结果

| 检查项 | 结果 | 细节 |
|--------|------|------|
| **train_a3_hook.py 存在** | PASS | 20951 bytes, 2026-05-20 08:21 |
| **依赖模块文件** | PASS | sdf_decoder.py, ee_extractor.py, sdf_gradient_refiner.py 全部存在 |
| **Module import** | PASS | SDFDecoder, EEPositionExtractor, SDFGradientRefiner 均可导入 |
| **Full import chain** | PASS | 包括 openpi 的 pi0_config, training.config, CosineDecaySchedule |
| **--help 输出** | PASS | argparse 正常，显示所有参数（scene, seed, gpu, batch_size, warmup_phase_steps, lambda_refine 等） |
| **SDF GT 数据** | PASS | `sdf_gt_spatial_bowl.npz` (4076 points) 和 `sdf_gt_object_chocolate.npz` (4084 points)，格式正确：keys=[query_points, sdf_values] |

**注意**：SDF GT 数据路径是 `/root/colliforce-vla/data/sdf_gt_*.npz`，不是任务描述中的 `/root/autodl-tmp/colliforce_data/safelibero_spatial/sdf_labels/`（该目录不存在）。

**结论**：A3 代码可以正常启动，无 import 错误、依赖齐全、数据就绪。GPU 释放后可直接运行。

---
