# fix unified crm r3 restart

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_unified-crm-r3-restart_20260522T113037_result.json`
- **Structured JSON:** [`26be8735e0dbd0b36c6a.json`](../../sessions/26/26be8735e0dbd0b36c6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D113 全部完成。

**执行摘要：**

| 步骤 | 结果 |
|------|------|
| bjb1-18228 Long cache K 值 | K=10 ✓ |
| rsync Long cache 到 bjb1-32546 | 1.4GB 传输完成 ✓ |
| bjb1-32546 4 suite K 值验证 | object/spatial/goal/long 全部 K=10 ✓ |
| 清除旧 checkpoint | 已清除 ✓ |
| `--input_mode` 参数确认 | 支持 obs_only ✓ |
| 训练启动 | bjb1-32546 cuda:3, tmux session `train-crm-unified-r3` ✓ |
| Registry | `train-crm-unified-4suite-r3` → RUNNING ✓ |

训练参数：224,555 samples, 4 suites, K=10, obs_only mode, 50 epochs, batch_size=32, lr=1e-3, CRM 327K params。

---
