# monitor cuda0 b01s45 to b02s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_cuda0-b01s45-to-b02s43_20260516T040042_result.json`
- **Structured JSON:** [`9ab1492764bd49b35b7b.json`](../../sessions/9a/9ab1492764bd49b35b7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有系统日志可查。综合已有信息出报告。

## sweep-isr-b01-s45 完成报告

- **总步数**: 219/500
- **结论**: **FAILED** — 进程被 SIGKILL (exit code 137) 杀死于 step 219，时间 2026-05-16T04:00:01Z
- **崩溃原因**: exit code 137 = SIGKILL，最可能是系统 OOM killer（RAM 不足，非 GPU OOM）
- **checkpoint**: `checkpoint-200/` 存在（~15GB，完整模型权重）

### Metrics

| 指标 | overall (219 steps) | last 50 steps |
|------|-------------------:|-------------:|
| prove_rate | 0.2357 | 0.4750 |
| isr_mean | 0.1127 | 0.2172 |
| reward_mean | 0.2470 | 0.4967 |
| loss | 0.0106 | 0.0138 |
| parse_rate | 1.0000 | 1.0000 |

### reward_log 全部字段
`step, reward_mean, reward_std, prove_rate, isr_mean, parse_rate, random_mean, loss, lr, beta_t, timestamp`

### GPU 状态
- **cuda:0**: 0 MiB, 0% — 已释放
- **cuda:1**: 80077 MiB, 89% — 有其他任务运行
- **磁盘**: 152G/250G used (99G avail)

### 备注
训练趋势向好（prove_rate 从 0 爬升到 last50 avg 0.475），但 step 219 被 kill。如需完整 500 步数据，需要从 checkpoint-200 resume 或重训。Resume 时注意 C012 约束（验证步数语义）。

---
