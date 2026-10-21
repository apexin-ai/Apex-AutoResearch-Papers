# infra check watchdog bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-watchdog-bjb1_20260517T141210_result.json`
- **Structured JSON:** [`3c8f8884f6379e759d46.json`](../../sessions/3c/3c8f8884f6379e759d46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. Watchdog: 正常运行 ✓
- tmux session `hsweep_watchdog` 存在（创建于 15:30）
- PID 930553 正在运行 `watchdog_hsweep.sh`，每 300s 检查一次 PID 920380
- 当前正在 `sleep 300`

### 2. auto_next 配置: 正确 ✓
- 序列: `2:1 → 2:2 → 5:1 → 10:1 → 20:1 → full:1 → ...`
- seed 1 完成后会启动 **h=2, seed=2**（train_seed=20000）
- 配置文件 `_alfworld_hsweep_h2.yaml` 存在
- h=2 seed=2 额外启用了 per-sample advantage logging（`LOG_PER_SAMPLE_ADV=1`）

### 3. 潜在问题: 双触发风险 ⚠️
`launch_hsweep.sh` 末尾自带 auto-chain：
```bash
bash "$(dirname "$0")/auto_next_hsweep.sh" "$H_VALUE" "$SEED"
```
加上 watchdog 也会调用 `auto_next_hsweep.sh`，PID 920380 退出后会**触发两次**。第二次 `tmux new-session` 会因 session 名重复而失败，不会造成实际损害，但会产生错误日志。这是冗余设计，不影响功能。

### 4. 磁盘: 充足
- `/root/autodl-tmp/`: 42G 可用（84% 使用），足够运行下一个 seed

### 5. GPU: 满载运行中
- cuda:0: 100% utilization, 25.8/97.8 GB
- cuda:1: 100% utilization, 25.8/97.8 GB
- 进程: `actor_rollout_update_actor` 在两块卡上运行

**结论**: watchdog 和 auto_next 均正常，seed 1 完成后会自动启动 seed 2，无需人工干预。

---
