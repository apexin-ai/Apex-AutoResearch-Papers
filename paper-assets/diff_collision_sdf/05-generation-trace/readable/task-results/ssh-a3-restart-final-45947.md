# ssh a3 restart final 45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a3_restart_final_45947_20260520T074225_result.json`
- **Structured JSON:** [`ccfd4a475c3f715a1e4d.json`](../../sessions/cc/ccfd4a475c3f715a1e4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 步完成。

| 步骤 | 状态 |
|------|------|
| 1. 清理残留进程 | ✅ |
| 2. 确认 checkpoint | ✅ spatial_bowl 无 checkpoint（从 step 0 开始），object_pudding 有 step 2500 |
| 3. 重新提交训练 | ✅ 通过 submit_training_job，修复 `--gpu` 参数（0/1） |
| 4. 验证训练状态 | ✅ 两卡 VRAM ~16.9GB，spatial_bowl step 8 ~12.6s/it，object_pudding step 2511 ~14.9s/it |
| 5. 更新 registry notes | ✅ 记录了根因（`--gpu` default=3）和修复方案 |
| 6. 注册 cron 监控 | ✅ 每 120s 轮询，PID 71494 / 73165 |

**根因修复**：`train_a3_hook.py` 的 `--gpu` 参数默认值为 3（适配 4 卡服务器 westd-35807），在 2 卡服务器 westd-45947 上导致 `CUDA_VISIBLE_DEVICES=3` 指向不存在的 GPU，torch 静默回退到 CPU 训练（339s/it → 修复后 ~13s/it）。

---
