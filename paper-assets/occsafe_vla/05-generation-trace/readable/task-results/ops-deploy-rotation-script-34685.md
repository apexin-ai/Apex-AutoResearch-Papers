# ops deploy rotation script 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-rotation-script-34685_20260522T140656_result.json`
- **Structured JSON:** [`41e699b2aba9e4e2bec3.json`](../../sessions/41/41e699b2aba9e4e2bec3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报如下：

**Rotation 脚本**: PID 151027，已在后台运行，每 5 分钟扫描一次，每个实验目录保留最新 1 个 checkpoint。

**日志**: `/root/rotation_new.log`（尚未创建，说明当前各目录均 ≤1 个 checkpoint，无需删除）

**当前 checkpoint 分布**（4 个实验各有 1 个 checkpoint + 1 个运行目录）:

| 实验 | 内容 |
|------|------|
| cutoff_s0 | `...--image_aug/`, `...--image_aug--10000_chkpt` |
| cutoff_s1 | `...--image_aug/`, `...--image_aug--10000_chkpt` |
| depth_s0 | `...--image_aug/`, `...--image_aug--10000_chkpt` |
| depth_s1 | `...--image_aug/`, `...--image_aug--10000_chkpt` |

**磁盘**: `/root/autodl-tmp` 350G 总量，已用 81G，可用 270G (24%)。

---
