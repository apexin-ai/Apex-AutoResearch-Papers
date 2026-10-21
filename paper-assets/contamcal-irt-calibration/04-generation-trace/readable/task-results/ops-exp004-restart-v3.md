# ops exp004 restart v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp004-restart-v3_20260514T071046_result.json`
- **Structured JSON:** [`2f41ca74fe089afa104e.json`](../../sessions/2f/2f41ca74fe089afa104e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**已完成条件**：
- `auc0.55_n20` — 10/10 seeds ✓
- `auc0.55_n50` — 10/10 seeds ✓

**部分完成（恢复中）**：
- `auc0.55_n100` — 7/10，剩余 seeds 7,8,9
- `auc0.8_n20` — 7/10，剩余 seeds 7,8,9（当前正在运行）
- `auc0.8_n50` — 1/10，剩余 seeds 1-9

**未开始**（7 条件）：`auc0.65_{n20,n50,n100}`, `auc0.8_n100`, `auc0.9_{n20,n50,n100}`

**总计剩余**：85 runs

| 项目 | 值 |
|------|-----|
| PID | 411032 |
| 日志 | `/tmp/exp004_sweep_20260514_071141.log` |
| Registry | `exp_004_sim_sweep_v2` → RUNNING |
| Crontab | 每 10 分钟检查 PID 存活，死亡写 `/tmp/exp004_watchdog.log` |

---
