# investigate eval vla mean object seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_eval-vla-mean-object-seed43_20260515T155443_result.json`
- **Structured JSON:** [`42ea87604b91d008c947.json`](../../sessions/42/42ea87604b91d008c947.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

**eval-vla-mean-object-seed43 确认在 bjb1-32546 cuda:1 运行。**

| 字段 | 值 |
|------|------|
| 服务器 | bjb1-32546 |
| GPU | cuda:1, 5609MiB |
| tmux PID | 111709 |
| Python PID | 111718 |
| 状态 | R (running), 419 threads |
| 启动时间 | 15:47 UTC (~8h 前) |

**Registry 已有完整 metadata**（server、pid、gpu 均已记录），无需补充。

**异常信号：日志只有 11 行，模型和环境加载完成后零 rollout 输出。** 命令带 `-u`（unbuffered），8 小时无进度输出不正常。对比 seed=42 同一时间段已完成 7.5/10 tasks。GPU 内存也异常高（seed43: 5609MiB vs seed42: 1887MiB）。可能挂死或卡在第一个 rollout。

**bjb1-32546 cuda:1 被此进程占用，不可用。**

**需要处理：**
1. 需要注册 cron 监控
2. 建议检查进程是否 hang（看 GPU util 是否有波动，或 strace 查系统调用），8h 零 rollout 输出大概率有问题

---
