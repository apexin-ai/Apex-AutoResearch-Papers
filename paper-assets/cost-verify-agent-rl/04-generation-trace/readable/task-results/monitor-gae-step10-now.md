# monitor gae step10 now

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gae-step10-now_20260517T191713_result.json`
- **Structured JSON:** [`7701306266324151f6e6.json`](../../sessions/77/7701306266324151f6e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**grep 命令：**
- `10/15` — 完成，耗时 4:31:14
- `11/15` — 完成，耗时 4:57:04（刚打印出来）
- `12/15` — 尚未出现

当前进度：**11/15 (73%)**，正在执行 step 12 的训练。

**tail -300 输出**（截断后末尾关键内容）：

step 10 的 eval 指标：
- `val-core/unknown/reward/mean@32: 1.25`
- `val-env/AlfworldSG/pass@1: 0.125`
- `val-env/AlfworldSG/non-zero/pass@1: 1.0`
- `critic/score/mean: 0.078125`
- `timing_s/step: 1608.81`
- `perf/throughput: 523.06`
- `timing_s/train_total: 15726.04`
- `timing_s/total: 16273.79`

进度条显示 `73% | 11/15 [4:57:04<1:51:02, 1665.66s/it]`，之后已进入 step 12 的 actor 训练（可见 `compute_policy_loss` 日志）。

---
