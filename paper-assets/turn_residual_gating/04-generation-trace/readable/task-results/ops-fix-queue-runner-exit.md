# ops fix queue runner exit

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_queue_runner_exit_20260522T232824_result.json`
- **Structured JSON:** [`22e3c1266c88db2565f3.json`](../../sessions/22/22e3c1266c88db2565f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Queue runner 没有退出，一切正常运行。** Cron 报告有误。

### 状态汇总

| 项目 | 状态 |
|------|------|
| **tmux session** | `queue_runner` 活跃 |
| **当前执行** | [2/8] AR N=50 existing — sub-step [2/4] UG s42 (PID 51492, 运行 5min+) |
| **GPU** | 72% 利用率, 22GB/98GB |
| **已完成** | [1/8] SS s42 eval (跳过,之前已完成), [2/8] sub-step [1/4] TG s42 AR N=50 ✓ |
| **Log 未更新原因** | Python stdout 通过 `tee` 管道输出有缓冲延迟，不代表进程停了 |

### Queue 剩余计划 (set -euo pipefail)

1. ~~[1/8] SS s42 eval~~ — 已跳过
2. **[2/8] AR N=50 existing s42** — 正在执行 (TG✓, **UG 进行中**, PCGrad/LO 待执行)
3. [3/8] SS s123 train + eval
4. [4/8] SS s456 train + eval
5. [5/8] Base s123 train + eval
6. [6/8] Base s456 train + eval
7. [7/8] TG s123 train + eval
8. [8/8] TG s456 train + eval

### 风险提示

脚本使用 `set -euo pipefail`。如果任何 eval/train 子步骤非零退出，整个 queue 会立即终止。当前运行正常，但后续 item 如果某个训练脚本不存在或 eval 报错，queue 会中断。不过脚本内 `run_and_eval` 函数对缺失脚本做了 `return 0` 保护，主要风险来自 Python 脚本本身的运行时错误。

**无需干预，继续等待即可。**

---
