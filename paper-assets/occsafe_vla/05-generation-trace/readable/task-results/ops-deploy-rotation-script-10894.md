# ops deploy rotation script 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-rotation-script-10894_20260522T140456_result.json`
- **Structured JSON:** [`75e5e79b02de95f03915.json`](../../sessions/75/75e5e79b02de95f03915.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Checkpoint rotation 已就绪：**

- **PID**: 991149，正常运行中
- **日志**: `/root/rotation_new.log`（暂无删除记录，正常）
- **磁盘**: `/root/autodl-tmp` 250G 总量，已用 97G，剩余 **154G (39%)**
- **当前 checkpoint 分布**（4 个实验各有 1 个 checkpoint）：

| 实验 | checkpoint |
|------|-----------|
| ablation_occ_detach_s2 | 20000_chkpt |
| ablation_random_occ_s2 | 20000_chkpt |
| depth_s2 | 20000_chkpt |
| depth_s3 | 20000_chkpt |

脚本每 5 分钟扫描一次，每个实验目录只保留最新 1 个 checkpoint，30K checkpoint 写入后旧的 20K 会被自动清理。

---
