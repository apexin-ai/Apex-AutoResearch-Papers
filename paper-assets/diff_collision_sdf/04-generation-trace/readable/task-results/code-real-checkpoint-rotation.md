# code real checkpoint rotation

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_real_checkpoint_rotation_20260520T072623_result.json`
- **Structured JSON:** [`ccaf6927a7fda2b1d0ff.json`](../../sessions/cc/ccaf6927a7fda2b1d0ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两台服务器验证结果：

### westd-35807
```
240:        SAVE_TOTAL_LIMIT = 3
245:        while len(all_ckpt_steps) > SAVE_TOTAL_LIMIT:
```
语法检查：`SYNTAX_OK`

### westd-45947
```
240:        SAVE_TOTAL_LIMIT = 3
245:        while len(all_ckpt_steps) > SAVE_TOTAL_LIMIT:
```
语法检查：`SYNTAX_OK`

### 修改说明

三个训练脚本（`train_baseline.py`、`train_a1_sdf_aux.py`、`train_a3_hook.py`）本身不需要修改——它们都通过 `train_loop() -> save_checkpoint()` 调用链继承 checkpoint 管理。

实际修改的文件是 `/root/autodl-tmp/openpi/scripts/train_pytorch.py`（通过 symlink `/root/colliforce-vla/openpi` 被三个脚本引用），将 `SAVE_TOTAL_LIMIT` 从 5 改为 3。轮转逻辑已存在于 `save_checkpoint` 函数末尾（line 240-250），每次保存后自动删除最旧的 checkpoint，只保留最近 3 个数字命名的 checkpoint 目录（`best/` 目录不受影响）。

---
