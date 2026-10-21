# data collect expert trajectories

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_collect-expert-trajectories_20260514T130957_result.json`
- **Structured JSON:** [`ec75f33788aa88d7fe62.json`](../../sessions/ec/ec75f33788aa88d7fe62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程都在正常运行：
- **Expert collection** (PID 340587): 运行 2m36s, CPU 104%, RSS 141MB - 纯 CPU 任务
- **exp015 训练** (PID 334705): 运行 25m46s, CPU 2.4% (GPU 主导) - 不受影响

收集速度约 100 games / 2.5 min ≈ 40 games/min。3553 个 game 预计 ~90 分钟完成。

收集脚本已在后台稳定运行，支持断点续传。可用以下命令监控进度：
```bash
wc -l /root/autodl-tmp/expert_trajectories/expert_trajectories.jsonl
cat /root/autodl-tmp/logs/expert_collection.log
```

---
