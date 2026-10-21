# ops c5 log fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c5_log_fix_20260519T221251_result.json`
- **Structured JSON:** [`0847923ce83ec3d1a657.json`](../../sessions/08/0847923ce83ec3d1a657.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 结果

**训练状态** (Step 3350, ~45h 运行):
- Loss: ~0.085 | Arm: ~0.068 | Grip: ~0.671 | LR: 1e-4
- 进程 PID 47691 正常运行，未中断

**日志情况**:
- 旧 tee 日志 **实际上是正常的** — tee 进程 (PID 47692) 存活，`/root/autodl-tmp/importance_margin_vla_compress/logs/train_c5_roboflamingo_gpu1.log` 有 139 行，内容到 Step 3350（最新）
- 额外设置了 pipe-pane 备份日志: `/root/runs/c5_roboflamingo_v2.log`（cat 进程 PID 52998 已启动，等下次输出时开始写入）

**两个日志路径**:
1. `/root/autodl-tmp/importance_margin_vla_compress/logs/train_c5_roboflamingo_gpu1.log` — tee 持续写入（主日志）
2. `/root/runs/c5_roboflamingo_v2.log` — pipe-pane 备份（新增）

训练每 50 步输出一行，间隔约 40 分钟，下次输出（Step 3400）时两个日志都会更新。

---
