# code d011 phase0 fix and phase2 dryrun

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d011_phase0_fix_and_phase2_dryrun_20260522T234128_result.json`
- **Structured JSON:** [`89fc18e9219178f56cfd.json`](../../sessions/89/89fc18e9219178f56cfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有任务完成。汇报如下：

---

## D011 Phase 0 结果

### 1. lora_utils.py 同步
**已同步。** westd-35807 缺少 dtype 修复 — lora_A/lora_B 未指定 `dtype=_dtype`，会默认创建 float32 参数（base weight 是 bfloat16）。已用 westd-45947 的修复版覆盖：
- `_dtype = base.weight.dtype` 添加到 `__init__`
- `torch.randn(..., dtype=_dtype)` 和 `torch.zeros(..., dtype=_dtype)`

### 2. Loss logging 修改

**修改文件：** `/root/colliforce-vla/openpi/scripts/train_pytorch.py`（两台服务器）

**A) tqdm postfix**（行 707-712）：添加 `action`, `sdf`, `ee` 三个 loss 组件到每步显示。

**B) W&B**：已有泛化逻辑（遍历 aux_info 所有数值 key 取平均后 wandb.log），无需额外修改。W&B 自动记录：`action_loss`, `sdf_total`, `sdf_l1`, `ee_loss`, `phase`, `eikonal`。

**额外修复：** `logging.basicConfig` 添加 `force=True` 解决 logging.info 被上游模块吞掉的问题（两台服务器的 `train_a1_sdf_aux_pi05.py`）。

### 3. Phase 2 dry-run 结果

在 westd-45947:cuda:0 运行 7 步，`--warmup_phase_steps 2`：

| Step (0-idx) | Phase | total_loss | action_loss | sdf_total | ee_loss |
|---|---|---|---|---|---|
| 0 | 1 | 0.1296 | 0.1257 | 0.1355 | 0.3265 |
| 1 | 1 | 0.1153 | 0.1107 | 0.1376 | 0.3951 |
| 2 | **2** | **0.1525** | 0.1481 | 0.1435 | 0.3639 |
| 3 | 2 | 0.1424 | 0.1382 | 0.1321 | 0.3514 |
| 4 | 2 | 0.1252 | 0.1211 | 0.1267 | 0.3531 |
| 5 | 2 | 0.1193 | 0.1147 | 0.1306 | 0.3925 |
| 6 | 2 | 0.1445 | 0.1403 | 0.1302 | 0.3567 |

- **Phase 1→2 切换确认**：Step 2 total_loss 跳升 0.1153→0.1525（LoRA unfreeze 扰动），符合预期
- **Step 0 trainable params: 658,948，LoRA params: 0**（Phase 1 冻结 LoRA 确认）
- **无 dtype crash，无 NaN**
- GPU 显存已释放，训练正常完成
- Dry-run checkpoint 已清理

### 4. SDF GT 数据

| Scene | 文件 | query_points | sdf_values | range |
|---|---|---|---|---|
| spatial_bowl | `sdf_gt_spatial_bowl.npz` | (4076, 3) | (4076,) | [-0.05, 0.05] |
| object_pudding | `sdf_gt_object_chocolate.npz` | (4084, 3) | (4084,) | [-0.05, 0.05] |

**两个 scene 都有 SDF GT 数据**，两台服务器均存在。

### 5. warmup_phase_steps 确认
代码默认值仍为 `5000`（行 91），dry-run 通过 CLI `--warmup_phase_steps 2` 传参，代码未改动，无需恢复。

---
