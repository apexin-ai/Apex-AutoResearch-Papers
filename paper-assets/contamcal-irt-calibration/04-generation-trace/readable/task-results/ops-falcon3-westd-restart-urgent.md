# ops falcon3 westd restart urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-westd-restart-urgent_20260522T080727_result.json`
- **Structured JSON:** [`8d8e1752081a8cd17517.json`](../../sessions/8d/8d8e1752081a8cd17517.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**不需要重启——4 个 Falcon3 训练已在运行中，参数全部正确。**

| GPU | tmux session | PID | dosage | lr | 启动时间 |
|-----|---|---|---|---|---|
| 0 | `sft_falcon3_7b_d000_s42_v2` | 599908 | d000 | 5e-5 ✓ | 15:50:06 |
| 1 | `sft_falcon3_7b_d005_s42_v2` | 600191 | d005 | 5e-5 ✓ | 15:50:12 |
| 2 | `sft_falcon3_7b_d025_s42_v2` | 600346 | d025 | 5e-5 ✓ | 15:50:16 |
| 3 | `sft_falcon3_7b_d050_s42_v2` | 600602 | d050 | 5e-5 ✓ | 15:50:19 |

4 卡 GPU 利用率 98-100%，显存分别占用 72/96/71/55 GB（共 98 GB/卡）。所有训练约 17 分钟前已启动，带 `_v2` 后缀，`--lr 5e-5` 已确认。无需操作。

---
