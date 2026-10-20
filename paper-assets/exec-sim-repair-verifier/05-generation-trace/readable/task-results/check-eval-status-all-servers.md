# check eval status all servers

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-status-all-servers_20260514T225345_result.json`
- **Structured JSON:** [`25816d6ba9f88a4f3d80.json`](../../sessions/25/25816d6ba9f88a4f3d80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验的状态：

**1. cls8b-s42-ckpt800-val8192-eval (westd)** — RUNNING, PID 300321
- 进度: 5110/9335 (54.7%), running acc **84.6%**
- 预计 ~11 min 后完成

**2. cls4b-v5-ckpt600-val5120-eval (home)** — RUNNING, PID 3179262
- 进度: 4000/9335 (42.9%), running acc **82.8%**
- 预计 ~42 min 后完成

**3. cls4b-v5-val5120-sweep (home)** — WAITING, PID 3180425
- 正在等 ckpt-600 eval 完成（每 30s 轮询）
- ckpt-600 完成后依次跑 4000 → 4200 → 4400 → 4600，每个 ~70 min，全部完成约 5-6 小时

报告已写入 `artifacts/eval_status_check_20260514.md`。三个 PID 均可用于注册 cron 监控。

---
