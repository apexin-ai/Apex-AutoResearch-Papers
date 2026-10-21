# debug vtc m64v6 crash

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_vtc-m64v6-crash_20260521T174353_result.json`
- **Structured JSON:** [`43cc590a6f0c144313c7.json`](../../sessions/43/43cc590a6f0c144313c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### 状态：崩溃（非正常结束）

实际训练日志是 `train_m64v6.log`（不是 v5 日志）。

### 时间线

| 事件 | 时间 | 备注 |
|------|------|------|
| v5 启动尝试 | 05-21 16:27 | 立即崩溃：`Network is unreachable`，无法从 HF Hub 加载数据集 |
| v6 启动 | 05-21 17:16 | 成功加载模型+数据集，开始训练 |
| checkpoint 保存 | 05-21 22:19 | `checkpoint_step10000.pt` (4.8GB) |
| eval | 05-22 00:44 | step 15000, eval/action_loss=3.0712 |
| **日志中断** | 05-22 01:43 | step=17050, loss=2.7953 |

### 关键发现

- **最后 step**: 17050/100000（仅完成 17%）
- **最后 checkpoint**: step 10000（如恢复将丢失 ~7000 步）
- **崩溃原因**: **日志末尾无任何错误信息或 traceback**，进程静默死亡。这高度指向被外部信号杀死（OOM killer 的 SIGKILL 或系统级终止）。训练指标本身完全正常（loss ~2.8-3.0，grad norm 稳定 ~0.8-1.0，无发散迹象）。
- 无法通过 `ssh_read_only` 检查 `dmesg`（被 whitelist 拦截），因此无法确认是否 OOM。

### v5 vs v6 说明

`train_openvla_sc_m64_seed42_v5.log` 是一次失败的启动尝试，因 AutoDL 网络不可达崩溃在数据集加载阶段，从未进入训练。真正的训练跑在 `train_m64v6.log` 里。

---
