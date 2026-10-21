## westd-35807 清理结果

- 清理前: 147 GB used / 350 GB (204 GB free)
- 清理后: 126 GB used / 350 GB (225 GB free)
- 释放空间: ~21 GB

### 删除项
| 目录 | 大小 | 状态 |
|------|------|------|
| baseline_object_pudding/ | — | 已被其他 Worker 删除 |
| baseline_spatial_bowl/ | — | 已被其他 Worker 删除 |
| a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed0/ | 22G | ✅ 本次删除 |
| tmp_* 目录 | — | 无残留 |
| *dry* 目录 | — | 无残留 |
| pi05_lora_baseline_*（顶层） | — | 无残留 |

### 保留项（活跃实验）
| 目录 | 大小 |
|------|------|
| a1_sdf_pi05_object_pudding_seed1_l005 | 22G |
| a1_sdf_pi05_object_pudding_seed1_l01 | 22G |
| a1_sdf_pi05_object_pudding_seed2_l005 | 22G |
| a1_sdf_pi05_object_pudding_seed2_l01 | 22G |
| **checkpoints 总计** | **86G** |

---

## westd-45947 磁盘状态

- 当前: 176 GB used / 250 GB (75 GB free)
- checkpoints 总计: 132G

### 各目录占用
| 目录 | 大小 | 状态 |
|------|------|------|
| a1_sdf_pi05_object_pudding/seed0_l005 | ~22G | 🟢 活跃实验 |
| a1_sdf_pi05_object_pudding/seed0_l01 | ~22G | 🟢 活跃实验 |
| a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed0 | 22G | ⚠️ 可清理 |
| a1_sdf_pi05_spatial_bowl | 0 | ⚠️ 空目录，可删 |
| a3_grad_refine_object_pudding | 22G | ⚠️ 可清理（旧 A3） |
| a3_grad_refine_spatial_bowl | 22G | ⚠️ 可清理（旧 A3） |
| baseline_object_pudding | 6.6G | ⚠️ 可清理（旧 baseline） |
| baseline_object_pudding_eval | 19G | ⚠️ 可清理（eval 完成） |

### 可清理汇总（待 Director 批准）
- pi05_lora_baseline_object_pudding_seed0: 22G
- a3_grad_refine_object_pudding: 22G
- a3_grad_refine_spatial_bowl: 22G
- baseline_object_pudding: 6.6G
- baseline_object_pudding_eval: 19G
- **合计可释放: ~91.6G**（清理后可达 ~167G free）

---

## 结论

- **westd-35807: SAFE** — 225 GB free，充足
- **westd-45947: SAFE（但建议清理）** — 75 GB free > 50 GB 阈值，但有 ~91.6G 旧 checkpoints 可清理。建议 Director 批准删除旧 A3 和 baseline 以释放空间。
