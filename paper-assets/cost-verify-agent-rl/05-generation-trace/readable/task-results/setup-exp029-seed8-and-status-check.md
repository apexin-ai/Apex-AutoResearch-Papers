# setup exp029 seed8 and status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_exp029_seed8_and_status_check_20260521T155012_result.json`
- **Structured JSON:** [`a80681ee03e8c12f172e.json`](../../sessions/a8/a80681ee03e8c12f172e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Seed 8 配置: 成功
  路径: /root/autodl-tmp/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_seed8_episode.yaml
  seed.train=1024, seed.val=555, CUDA="2,3", paths=exp029-seed8, experiment_name=exp029-seed8-episode-level
  checkpoint 目录已创建

Ray 清理: ray stop 已执行，残留进程均属 Seed 7 活跃训练（预期行为）

Seed 7 (westd): step 8/15, 最新已记录 step 6 train_success=52.34%
  趋势: 31.3% → 44.5% → 49.2% → 69.5% → 39.1% → 52.3% (学到了，但有波动)

Seed 4 (bjb1): step 14/15, 最新已记录 step 12 train_success=20.31%
  趋势: 13.3% → 11.7% → 14.8% → 19.5% → 25.0% → 38.3% → 12.5% → 14.8% → 25.8% → 38.3% → 21.9% → 20.3%
  (表现较差，高方差，学习不稳定)

Watchdog westd: ALIVE (PID 118781, uptime 4h44m)
Watchdog bjb1: ALIVE (PID 313318, uptime 4h44m)
```

---
