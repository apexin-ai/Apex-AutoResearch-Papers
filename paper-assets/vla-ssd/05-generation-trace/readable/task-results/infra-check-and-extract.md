# infra check and extract

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-and-extract_20260515T092752_result.json`
- **Structured JSON:** [`bbd36ad16947f3cb1ae3.json`](../../sessions/bb/bbd36ad16947f3cb1ae3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**完成汇总：**

| 步骤 | 状态 |
|------|------|
| Shard 1 下载 | 6,948,961,960 bytes ✓ |
| 3 shards 验证 | 805 + 154 + 23 tensors, 全部 OK ✓ |
| Dry-run | 输出 (272, 33, 4096) shape, 正常 ✓ |
| Trained 提取 (GPU 0) | 已提交: `openvla-trained-extract`, log: `~/runs/vla-ssd/openvla-trained-extract.log` |
| Untrained 提取 (GPU 1) | **未提交** — `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/` 不存在，需要先初始化 untrained checkpoint |

---
