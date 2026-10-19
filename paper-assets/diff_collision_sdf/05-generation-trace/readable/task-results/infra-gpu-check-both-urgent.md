# infra gpu check both urgent

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-check-both-urgent_20260529T043625_result.json`
- **Structured JSON:** [`1c08e576d72de0a74471.json`](../../sessions/1c/1c08e576d72de0a74471.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### westd-45947 — `train_pi05_a1_obj_s3_l01`
- **状态: DEAD**
- **GPU**: 0% 利用率，0 MiB 显存占用（完全空闲）
- **崩溃原因**: **磁盘满** — `/root/autodl-tmp` 250G 用了 250G（100%，仅剩 4KB）
- **Traceback**: `shutil.copytree` 在 step 2000 保存 best checkpoint 时触发 `[Errno 28] No space left on device`
- **崩溃时进度**: step 1999/30000（~7%），loss=0.1440, action=0.1432, sdf=0.0358, ee=0.0425
- **已有 checkpoint**: step 2000 目录存在（保存成功），但 best 目录复制失败

### westd-35807 — `train_pi05_lora_baseline_s3_v2`
- **状态: ALIVE** ✓
- **运行时间**: 47 小时
- **GPU 0**: 100% 利用率，19061 MiB 显存占用
- **当前进度**: step 2232/30000（~7%），loss=0.0911, action=0.0911
- **速度**: 1.21s/it，预计剩余 ~9h20m

### 需要处理
westd-45947 数据盘已满，需清理空间后重启训练。可从 step 2000 checkpoint resume。需要清理旧 checkpoint 或无用数据释放空间。

---
