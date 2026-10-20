# fix home kill start 6144

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_home-kill-start-6144_20260514T113006_result.json`
- **Structured JSON:** [`ffb319ac9c39849eaec4.json`](../../sessions/ff/ffb319ac9c39849eaec4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6144 验证已自动启动。汇报：

**执行结果：**

| 步骤 | 状态 |
|------|------|
| PID 3074797 kill | 成功 |
| val_sweep (home 系列) 停止 | 成功，已完成 home/ckpt-200 (79.57% acc)，后续 home checkpoint 全部跳过 |
| 6144 验证启动 | 自动启动，tmux session `val_6144`，04:32:13 开始 |
| 当前在跑 | `seed123_home/checkpoint-400`，split=val，max_seq_length=6144，batch_size=4 |
| GPU 显存 | 12905MiB / 32607MiB（~40%），100% 利用率 |

脚本会依次跑 seed123 ckpt-400 → ckpt-600，完成后自动输出对比结果。

---
