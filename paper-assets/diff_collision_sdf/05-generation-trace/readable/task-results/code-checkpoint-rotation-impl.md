# code checkpoint rotation impl

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_checkpoint_rotation_impl_20260520T071800_result.json`
- **Structured JSON:** [`282a221b33a6a05c1eac.json`](../../sessions/28/282a221b33a6a05c1eac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器都已有相同的轮转逻辑。

**结论：任务已完成，无需修改。**

- `openpi/scripts/train_pytorch.py` 的 `save_checkpoint` 函数（L239-249）已包含轮转：`SAVE_TOTAL_LIMIT = 5`，每次保存后自动清理超出 5 个的旧 checkpoint
- 三个脚本（`train_baseline.py`、`train_a1_sdf_aux.py`、`train_a3_hook.py`）都通过 `train_loop → save_checkpoint` 调用链共享此逻辑
- 轮转跳过 `tmp_*` 目录和非数字目录（如 `best/`）
- westd-35807 和 westd-45947 代码一致
- 当前 checkpoint 状态正常：各实验只有 2-3 个 checkpoint，磁盘占用 42%（144G/350G）

---
