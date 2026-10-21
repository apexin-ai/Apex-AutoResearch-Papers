# ssh verify s1 checkpoint

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_s1_checkpoint_20260528T195044_result.json`
- **Structured JSON:** [`9efa551f264013be8934.json`](../../sessions/9e/9efa551f264013be8934.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果汇总

### westd-35807 — ⚠️ 确认存在损坏 checkpoint

| 路径 (均在 `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/` 下) | 大小 | 修改时间 | 状态 |
|---|---|---|---|
| `pi05_lora_baseline_object_pudding_seed1/30000/model.safetensors` | **1,589,248 (1.52 MB)** | May 26 09:32 | **⚠️ 损坏** |
| `pi05_lora_baseline_object_pudding_seed0/30000/model.safetensors` | 7,540,115,784 (7.02 GB) | May 27 17:48 | ✅ 正常 |
| `a1_sdf_pi05_object_pudding_seed1_l005/30000/model.safetensors` | 7,540,115,784 | May 24 21:24 | ✅ 正常 |
| `a1_sdf_pi05_object_pudding_seed1_l01/30000/model.safetensors` | 7,540,115,784 | May 24 21:24 | ✅ 正常 |
| `a1_sdf_pi05_object_pudding_seed1_l1/30000/model.safetensors` | 7,540,115,784 | May 27 17:50 | ✅ 正常 |

损坏目录下**只有 model.safetensors 一个文件**（无 optimizer.pt、metadata.pt），说明这是一个不完整的拷贝/同步产物。

### westd-45947 — ✅ 完好

| 路径 (均在 `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/` 下) | 大小 | 修改时间 | 状态 |
|---|---|---|---|
| `pi05_lora_baseline_object_pudding_seed1/30000/model.safetensors` | 7,540,115,784 (7.02 GB) | May 26 09:32 | ✅ 正常 |
| `pi05_lora_baseline_object_pudding_seed1/best/model.safetensors` | 7,540,115,784 | May 25 08:43 | ✅ 正常 |

该目录包含完整文件集（model.safetensors + optimizer.pt + metadata.pt + baseline_metadata.pt）。

### 关键结论

1. **损坏确认**：westd-35807 上 `pi05_lora_baseline_object_pudding_seed1/30000/model.safetensors` 确实损坏，仅 1.52 MB（正常应为 7.02 GB），且目录不完整
2. **完好副本存在**：westd-45947 上**同路径**的 checkpoint 完好（7.02 GB），可直接用于恢复
3. **Table 4 eval 路径**：`/root/diff_collision_sdf/checkpoints/pi05_lora_baseline_s1/step_30000/` 在 westd-45947 上**不存在**（`/root/diff_collision_sdf/checkpoints/` 整个目录不存在）。实际 eval 用的应该是 `/root/autodl-tmp/checkpoints/...` 路径下的那个，该 checkpoint 完好
4. **其他 seed1 变体**（l005/l01/l1）在 westd-35807 上全部正常（7.02 GB）

**修复方案**：从 westd-45947 的完好副本 scp 到 westd-35807 覆盖损坏文件即可。

---
