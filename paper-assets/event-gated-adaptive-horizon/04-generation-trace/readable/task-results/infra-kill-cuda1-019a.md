# infra kill cuda1 019a

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill-cuda1-019a_20260516T220015_result.json`
- **Structured JSON:** [`570b6fe19797032c3783.json`](../../sessions/57/570b6fe19797032c3783.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**Kill**: 成功。`kill 614980` 后 5 秒内进程退出。

**cuda:1 状态**: 干净。nvidia-smi 显示 cuda:1 仅 1MiB 占用，0% 利用率，无 python 进程。GPU 0 上 PID 612881 不受影响。

**019a_v2 分析 — 进程并未失败，是被正常 kill 的活跃训练**:
- 最后日志写入时间：`06:00:14`（kill 前 40 秒），进程一直在正常训练
- 进度：step **41,600** / 200,000（20.8%），episode 208，FPS ~6.18
- train_return 波动在 4~72 之间，多数 18~30；最后一次 eval（step 32,500）eval_return = 33.19
- checkpoint：仅 `latest.pt`（05:35 写入），`checkpoint_every=50000` 所以第一个正式 checkpoint 尚未触发
- 无 tmux session 关联
- 无 error log，stderr 为空

结论：019a_v2 没有 hang 或 crash，是正常运行中的 baseline 训练被手动 kill。cuda:1 已完全释放可用。

---
