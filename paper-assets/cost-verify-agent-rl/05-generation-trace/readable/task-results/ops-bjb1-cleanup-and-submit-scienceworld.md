# ops bjb1 cleanup and submit scienceworld

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_cleanup_and_submit_scienceworld_20260522T040444_result.json`
- **Structured JSON:** [`4dcbf0ca3ee2a43dad59.json`](../../sessions/4d/4dcbf0ca3ee2a43dad59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

| 项目 | 结果 |
|------|------|
| **磁盘清理** | 2 个 symlink + 2 个 SCP 副本目录已删除，当前 /root/autodl-tmp 可用 49GB |
| **GPU** | cuda:0, cuda:1 均空闲（0 MiB 占用） |
| **Config** | v4 参数确认正确：15 steps, save_freq=5, group_size=16, env_groups=8, 2 GPU, val_before_train=True, JVM 修复就位 |
| **Dry-run** | ScienceWorld 初始化 OK（30 tasks），Hydra config 解析 OK |
| **训练提交** | PID=385902, tmux session=`scienceworld_grpo_cell_c_v4`, log=`~/runs/cost-verify-agent-rl/scienceworld_grpo_cell_c_v4.log` |

---
