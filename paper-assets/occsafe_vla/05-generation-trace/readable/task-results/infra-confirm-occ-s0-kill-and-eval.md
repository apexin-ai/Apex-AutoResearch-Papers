# infra confirm occ s0 kill and eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_confirm-occ-s0-kill-and-eval_20260521T065651_result.json`
- **Structured JSON:** [`96ec7af951d42dbfe251.json`](../../sessions/96/96ec7af951d42dbfe251.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### s0 (PID 76998) — 已退出
- **退出时间**: 14:56:24，exitcode 1
- **50000_chkpt 已保存**: `/root/autodl-tmp/checkpoints/occ_s0/...--50000_chkpt` (14:56 创建)
- **退出原因**: 训练完成后正常退出（到达 max_steps 后 save 了 50000_chkpt，然后 exit）。**不是 kill 脚本触发的** — kill 脚本最后一次检查在 14:55:56，此时还没发现 checkpoint，下次检查在 ~14:57:56

### s2 (PID 78171) — 已退出
- PID 已不存在
- **50000_chkpt 也已保存** (14:56 创建)
- 与 s0 同时完成训练

### s1 (PID 80898) — 仍在训练
- 状态正常，584% CPU，cuda:1

### kill 脚本 (PID 86294) — 仍在运行但未触发
- 日志最后一条: `14:55:56 no final checkpoint yet`
- s0/s2 在 kill 脚本下次检查前已自行退出（max_steps 到了）

### eval trigger (PID 85512) — 仍在运行，尚未触发 eval
- 当前正在 sleep 30（PID 87534，14:56 开始）
- 日志全部是 "Waiting..." 状态，还没检测到进程退出
- **预计 ~14:57 醒来后会检测到 s0/s2 PID 已退出，应触发 eval**
- 目前无 `evaluate_safelibero` 进程在运行

### eval 结果
- `/root/occsafe_vla/eval_results/` 只有 `monitor_status.txt`，尚无实际结果

### 结论
s0 和 s2 都是**正常训练完成退出**（非被 kill），50000_chkpt 均已保存。eval trigger 脚本即将（~1 分钟内）检测到退出并启动 eval。建议 1-2 分钟后再检查一次确认 eval 是否成功启动。

---
