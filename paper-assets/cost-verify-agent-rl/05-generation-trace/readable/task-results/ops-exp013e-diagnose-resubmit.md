# ops exp013e diagnose resubmit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp013e-diagnose-resubmit_20260514T091627_result.json`
- **Structured JSON:** [`9c9c846dad4fe4fbee7a.json`](../../sessions/9c/9c9c846dad4fe4fbee7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## exp013e 崩溃诊断报告

### 1. 崩溃原因

**`ray.exceptions.ActorUnavailableError`** — `train.py:208` (`ray.get(runner.run.remote(config))`)

```
RPC error: Socket closed rpc_code: 14
```

一个 Ray actor 进程意外死亡，导致 RPC 连接断开。崩溃发生在 **validation step 5 完成之后**（所有 val 指标已成功输出），向 training step 6 过渡时。

### 2. 排除的原因

| 可能原因 | 状态 | 证据 |
|---------|------|------|
| cgroup OOM | **排除** | `memory.events` 显示 `oom_kill 0` |
| 系统 OOM | **排除** | `dmesg` 无 OOM 记录 |
| CUDA OOM | **排除** | 日志无 CUDA OOM 错误 |
| 磁盘满 | **排除** | `/root/autodl-tmp/` 剩余 118GB (46%) |

Ray worker 日志已被 `ray stop --force` 清除，无法确定 actor 内部的精确死因。最可能是 vLLM worker 在 validation→training 切换时的内存峰值或内部错误（未触及 cgroup 硬限制但可能接近）。

### 3. 当前资源状态

- **GPU**: 2× RTX PRO 6000 完全空闲 (0MiB / 97887MiB, 0% util)
- **系统内存**: cgroup 限制 220GB，当前占用 ~131GB（空闲态）
- **磁盘**: 118GB 可用
- **残留进程**: 无（Ray 已停止，tmux session 已清理）
- **Checkpoint**: `exp008_grpo/global_step_5` 完整可用；exp013e 未产生任何 checkpoint

### 4. 代码修复状态

- `object_store_memory = 30 * 1024**3` 硬编码在 `train.py:203`，已就位

### 5. 结论

**可以安全重新提交。** 这是一个 Ray actor 瞬态崩溃，无持久性根因。建议重提交时设置 `HYDRA_FULL_ERROR=1` 环境变量，如果再次崩溃可获取完整堆栈。

---
