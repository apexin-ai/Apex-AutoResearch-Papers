# ops emergency disk cleanup 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency_disk_cleanup_34685_20260524T214548_result.json`
- **Structured JSON:** [`28c496618cb79e616c82.json`](../../sessions/28/28c496618cb79e616c82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cutoff_45k_s1 已成功重启，正在加载 20000 checkpoint。GPU 0 已在使用。

## 总结

| 项目 | 状态 |
|------|------|
| **磁盘** | 100% → 45%，释放 ~193GB |
| **cutoff_15k_s1** (GPU1, PID 861222) | 存活，运行 9h51m |
| **cutoff_25k_s2** (GPU2, PID 998208) | 存活，运行 4h41m |
| **reverse_cutoff_s2** (GPU3, PID 999132) | 存活，运行 4h41m |
| **cutoff_45k_s1** (GPU0) | 已从 step 20000 恢复重启 |

**cutoff_45k_s1 崩溃详情**：训练到 step ~28068 后磁盘满，在保存 step 30000 checkpoint 时写 safetensors 失败（`No space left on device`）。30000 checkpoint 不完整（1/4 shards），已删除。从完整的 20000 checkpoint 恢复。

- 新 PID: 20913（wrapper: 20838）
- Log: `/root/runs/occsafe_vla/cutoff_45k_s1_resume_20260525_054812.log`

---
