# infra P0 westd 10894 disk full v3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_P0-westd-10894-disk-full-v3_20260521T095817_result.json`
- **Structured JSON:** [`39348cd27a37f0f3ba23.json`](../../sessions/39/39348cd27a37f0f3ba23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验运行中，4 个 GPU 都有显存占用。

## P0 westd-10894 磁盘满修复 v3

### 清理
- 释放空间: 80G（221G → 141G）
- 磁盘状态: 141G/250G (57%)

### Rotation 脚本
- 旧 PID 504685: killed
- 新 PID: 514991
- 策略: 保留 1 个 checkpoint, 300s 间隔

### ablation_occ_detach_s0 重启
- resume checkpoint: `openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--10000_chkpt`
- resume step: 10000
- 新 PID: 515223

### 验证
- finetune.py 进程数: 4 组（每组含 torchrun wrapper + worker）
- GPU 状态: 全部 4 卡有显存占用（GPU0: 15.8G 加载中, GPU1-3: ~62G）
- 磁盘: 110G 可用，充裕

---
