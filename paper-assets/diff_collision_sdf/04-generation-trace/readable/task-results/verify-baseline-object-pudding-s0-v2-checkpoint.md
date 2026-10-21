# verify baseline object pudding s0 v2 checkpoint

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_baseline_object_pudding_s0_v2_checkpoint_20260521T044111_result.json`
- **Structured JSON:** [`469918a78eb17a2e6005.json`](../../sessions/46/469918a78eb17a2e6005.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### baseline_object_pudding_s0_v2 Checkpoint

| 项目 | 详情 |
|------|------|
| **checkpoint 路径** | `/root/autodl-tmp/checkpoints/baseline_object_pudding/baseline_object_pudding_seed0/` |
| **保存的 steps** | 29999, 30000, best |
| **step 30000 文件** | `model.safetensors` (6.6G) + `optimizer.pt` (12G) + `metadata.pt` (3.2K) |
| **总目录大小** | 55G |
| **best loss** | 0.003305 @ step 29999 |
| **checkpoint 完整性** | **完整** — 三个 step 目录均含 model.safetensors / optimizer.pt / metadata.pt |

另外还有一个 LoRA 变体 checkpoint：`baseline_lora_object_pudding_seed0/`，保存了 step 2000 和 best。

### 磁盘状态

| 总容量 | 已用 | 可用 | 使用率 |
|--------|------|------|--------|
| 350G | 223G | 128G | 64% |

### a1_sdf_spatial_bowl_s0_v3 状态

**已崩溃** — 在 step 6499/30000 (22%) 处因磁盘满报错退出：
```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

日志路径：`/root/autodl-tmp/logs/a1_sdf_spatial_bowl_s0_v3.log`

现在磁盘已恢复到 128G 可用（可能之前的临时文件已清理），但 a1_sdf 实验需要重新启动。其最新 checkpoint 停留在 step 6000（目录 `/root/autodl-tmp/checkpoints/a1_sdf_object_pudding/a1_sdf_object_pudding_seed0/`，保存了 step 4000 和 6000）。

---
