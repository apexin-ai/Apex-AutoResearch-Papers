# code wrapper 7d fix

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wrapper-7d-fix_20260513T104644_result.json`
- **Structured JSON:** [`4a0f5d2bfc41f077aea4.json`](../../sessions/4a/4a0f5d2bfc41f077aea4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修改摘要：

### 修改的文件（共 5 个，均在 `/root/acr-vla-conformal-refinement/src/`）

| 文件 | 主要修改 |
|------|---------|
| **utils.py** | `ACTION_DIM=6` → `CORRECTION_DIM=6` + 新增 `FULL_ACTION_DIM=7`；`load_libero_demos` 增加 `ee_states`(6D) 字段；`build_training_samples` 改用 `ee_states` 代替 `joint_states` |
| **smolvla_wrapper.py** | state 参数 `joint_states`(7D) → `eef_state`(6D = ee_pos+ee_axisangle)；`img_transform` 增加 `Resize(256,256)`；`preprocess_obs_batch` 改读 `ee_states`；`generate_k_samples` 输出裁切到 `FULL_ACTION_DIM=7`；新增 `split_action()` 函数 |
| **evaluate.py** | 删除 `pad_action_to_7d`；新增 `get_eef_state()` (quat→axisangle)；env 渲染改为 256×256；所有 action 函数直接返回 7D；CRM 模式中 CGS 只处理前 6D pose，gripper 取 K 样本均值 pass-through |
| **cgs.py** | 默认 `action_dim=CORRECTION_DIM`，只对 6D pose 计算 uncertainty |
| **train_crm.py** | 所有 `ACTION_DIM` → `CORRECTION_DIM`；precompute 中样本切片到 6D；CRM 输入/输出维度 = `H_EFF * CORRECTION_DIM = 30` |

### 验证结果
- `FULL_ACTION_DIM=7, CORRECTION_DIM=6` ✓
- `split_action([1,2,3,4,5,6,7])` → `pose=[1,2,3,4,5,6], grip=[7]` ✓
- package-level + script-level imports ✓
- CRM 337,438 params (维度不变) ✓

**注意**：当前服务器上的模型是 `smolvla_base`（6D action, SO100 数据训练），不是 LIBERO fine-tuned 版本。路径在 `/root/autodl-tmp/models/SmolVLA/lerobot/smolvla_base/`，而非任务描述中的 `/root/autodl-tmp/models/smolvla_libero/`。

---
