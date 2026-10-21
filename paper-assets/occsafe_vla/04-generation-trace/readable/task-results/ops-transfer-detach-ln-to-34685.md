# ops transfer detach ln to 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_transfer_detach_ln_to_34685_20260524T074058_result.json`
- **Structured JSON:** [`4faedf4e62bf1ca77c0d.json`](../../sessions/4f/4faedf4e62bf1ca77c0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

传输成功。

| | westd-10894 (源) | westd-34685 (目标) |
|---|---|---|
| 大小 | 15G | 15G |
| 文件 | 完整 | 完整（21个文件 + lora_adapter 子目录） |

"file changed as we read it" 是 tar 的常见无害警告（可能是日志或临时文件），大小一致，关键模型文件（4个 safetensors、action_head/occ_head/proprio_projector checkpoint、lora_adapter）全部到位。

三个 checkpoint 现在都在 westd-34685 上，可以开始 same-seed 梯度分析。

---
