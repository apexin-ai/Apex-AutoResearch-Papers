# ops 41312 kill and launch

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_41312_kill_and_launch_20260518T013900_result.json`
- **Structured JSON:** [`811f5b2d425beb86440e.json`](../../sessions/81/811f5b2d425beb86440e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

| 步骤 | 结果 |
|------|------|
| Kill 145556 | ✓ SIGTERM 成功 |
| 数据检查 | ✓ scored_data_60.jsonl 存在 (950MB) |
| contamination_60_adaptive_seed456 | ✓ PID 156657, cuda:1, 46539 MiB |
| contamination_60_uniform_seed456 | ✓ PID 156802, cuda:2, 46539 MiB |

注：原始命令中的 `--dataloader_num_workers 0` 不被 `pretrain_weighted.py` 支持，已去掉后重新提交成功。GPU 1 和 2 均已占用约 46.5GB 显存，训练正常运行。

---
