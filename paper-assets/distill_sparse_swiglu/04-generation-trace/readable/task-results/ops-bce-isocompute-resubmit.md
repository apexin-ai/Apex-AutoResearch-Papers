# ops bce isocompute resubmit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bce_isocompute_resubmit_20260515T194431_result.json`
- **Structured JSON:** [`13ac887433e8c21d44df.json`](../../sessions/13/13ac887433e8c21d44df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行，Step 100 已输出，速度 0.91s/step（比 v1 的 1.14s/step 更快）。

## 汇报

**1) 崩溃原因**
原 bce_isocompute_s42 (PID 120879) 在 step 500/2700 后静默退出：
- 日志无任何 error/traceback，最后输出为 step 500 的正常 metrics
- tmux session 已消失，且无退出码文件（`/tmp/agent-ml-exit/bce_isocompute_s42.exit` 不存在），说明 EXIT trap 未触发
- 磁盘空间正常（root 46%, data 11%），排除磁盘满
- dmesg 不可访问（容器权限），无法确认 OOM killer
- **结论：tmux session 被外部操作意外终止**（非 OOM、非磁盘满、非代码 crash）

**2) 重提交状态**
- exp_id: `bce_isocompute_s42_v2`
- 已在 cuda:0 上正常运行，Step 100 已输出
- 速度 0.91s/step，预计总耗时 ~41 分钟（2700 步）

**3) PID 和日志路径**
- PID: 123984（实际 python 进程 123989）
- 日志: `~/runs/distill_sparse_swiglu/bce_isocompute_s42_v2.log`
- tmux session: `bce_isocompute_s42_v2`

---
