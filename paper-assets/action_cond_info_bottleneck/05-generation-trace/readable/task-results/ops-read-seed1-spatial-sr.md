# ops read seed1 spatial sr

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-seed1-spatial-sr_20260516T185201_result.json`
- **Structured JSON:** [`077a28d2c64e6171ebfd.json`](../../sessions/07/077a28d2c64e6171ebfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**libero_spatial eval 尚未完成。** 当前状态：

| 指标 | 值 |
|------|-----|
| 进度 | Task 8/10 运行中（task 8 已完成 7/10 episodes） |
| 剩余 | ~task 8 剩 3 episodes + task 9 全部 10 episodes |
| eval_info.json | 未生成（suite 完成后才写入） |
| libero_object 目录 | 不存在（spatial 未完成） |

**tmux 中间数据**（已部分滚出缓冲区）：
- 在之前的 tmux 捕获中看到 `running_success_rate` 在 **43.5% ~ 46.9%** 之间波动
- 当前 tmux 只剩下正在跑的 task 8 的 `running_success_rate=0.0%`（该 task 内暂无成功 episode）

**预估**：
- spatial 完成还需约 20-40 分钟
- 最终精确 SR 将出现在 `/root/autodl-tmp/v7_eval_fixed_seed1/libero_spatial/eval_info.json`

**中间信号 vs baseline**：
- 中间 running_success_rate ≈ **44-47%**（不含 task 8/9 数据）
- Baseline (smolvla_libero spatial) = **66.0%**
- 当前看起来 **显著低于 baseline**（-19~22 pp），但 task 8/9 的结果可能改变最终值

需要等 eval_info.json 生成后再确认最终数字。要我过 30 分钟后再来查看吗？

---
