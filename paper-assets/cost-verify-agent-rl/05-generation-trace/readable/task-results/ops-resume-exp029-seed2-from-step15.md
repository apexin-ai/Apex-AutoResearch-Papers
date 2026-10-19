# ops resume exp029 seed2 from step15

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resume-exp029-seed2-from-step15_20260518T150442_result.json`
- **Structured JSON:** [`49a60c872d2a3894bf72.json`](../../sessions/49/49a60c872d2a3894bf72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 RUNNING。

---

## 总结

| 项目 | 结果 |
|------|------|
| **RAID 健康** | 无 RAID 设备，dmesg 无错误 |
| **磁盘空间** | /root/autodl-tmp 47GB 可用 |
| **step_20 删除** | 已删除（损坏：optim 3.7-3.8GB vs 正常 6.5GB，缺 extra_state/fsdp_config） |
| **step_15 完整性** | 完整：model 2×3.8GB, optim 2×6.5GB, extra_state 2×15K, fsdp_config, huggingface |
| **恢复确认** | `Load from checkpoint folder: .../global_step_15` / `Setting global step to 15` / `Resuming from .../global_step_15` |
| **PID** | 44067 |
| **W&B run ID** | z0lrskjy |
| **GPU 占用** | GPU0: 11.1GB, GPU1: 11.1GB（checkpoint 加载完成后，rollout 阶段会增加） |
| **Config 变更** | `resume_mode: disable` → `resume_mode: auto` |
| **tmux session** | `exp029_seed2` |
| **日志** | `/root/runs/cost-verify-agent-rl/exp029_seed2_resume_step15.log` |

---
