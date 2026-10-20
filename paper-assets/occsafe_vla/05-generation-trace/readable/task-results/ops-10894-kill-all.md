# ops 10894 kill all

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894-kill-all_20260527T002229_result.json`
- **Structured JSON:** [`426f9ad783c5da33a382.json`](../../sessions/42/426f9ad783c5da33a382.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**

- 所有 8 个目标进程已成功 kill（5 个有 GPU 占用的 + 3 个无 GPU 占用的）
- 无 torchrun/finetune/evaluate 残留进程
- **GPU 显存已全部释放**（4 张卡均 0 MiB used）
- 注意：GPU 0 和 GPU 2 仍显示 100% utilization，但显存已归零——这是 GPU 故障的表现（与 Director 判断一致），非正常负载

---
