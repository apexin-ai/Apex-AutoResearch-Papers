# cleanup 34685 disk intermediate checkpoints

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_34685_disk_intermediate_checkpoints_20260527T165011_result.json`
- **Structured JSON:** [`2259fdab45a77a194f53.json`](../../sessions/22/2259fdab45a77a194f53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果**：
- 可用空间：89G → **148G**（释放 59G）
- 删除内容：cutoff_25k_s1_v2、mvp_occ_s4、vanilla_v2_s1、vanilla_v2_s2 的 40000_chkpt（各 15G）
- 保留：每个实验的 50000_chkpt（50K final）均完好
- 正在运行的 4 个实验未受影响

148G 接近 149G 目标，差 1G 在 du 舍入误差范围内。如需进一步清理，detach_ln_s3 的 40000_chkpt（15G）也可清理，但它不在明确批准的列表中。

---
