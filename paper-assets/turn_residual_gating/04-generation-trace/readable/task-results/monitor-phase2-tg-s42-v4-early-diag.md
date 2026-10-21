# monitor phase2 tg s42 v4 early diag

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_phase2_tg_s42_v4_early_diag_20260518T162313_result.json`
- **Structured JSON:** [`7e95d322bfe118f5eace.json`](../../sessions/7e/7e95d322bfe118f5eace.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 次 SSH 连接全部失败，诊断结果如下：

```
SSH 状态: 连接失败(重试3次) — Unable to connect to port 20861 on 36.103.198.204
日志可读性: 不可读（无法连接服务器）
当前步数: 未知
gate_std 趋势: 无数据
L4 状态: 无数据
总 loss: 无数据
GAR 稳态: 无数据
诊断结论: 数据不足无法判断 — 服务器 westd-20861 端口不可达，可能服务器已关机/重启/网络中断
```

服务器端口 20861 完全不可达（连接立即被拒绝，非超时），最可能的原因是：
1. 服务器实例已被回收或重启
2. 端口映射失效

建议检查 SeetaCloud 控制台确认实例状态。如果实例已停止，v4 训练也随之中断。

---
