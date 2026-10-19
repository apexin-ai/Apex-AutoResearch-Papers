# deploy exp008 retrain100 restart

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp008-retrain100-restart_20260518T190930_result.json`
- **Structured JSON:** [`c1d62ea4d36d4112ce20.json`](../../sessions/c1/c1d62ea4d36d4112ce20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**总结：**

| 项目 | 状态 |
|------|------|
| `retrain_interval=100` 已同步 | MD5 匹配 `319a13f2` |
| 旧 exp-008 tmux 已清理 | 无残留会话 |
| Dry-run (2 steps, retrain_interval=1) | 全部通过 |
| - Probe retrain acc | 0.9945 (两次重训均如此) |
| - Probe AUROC | 1.0000 |
| - S(t) | step1=0.5694, step2=0.4407 (非零) |
| - 无 OOM | 正常完成 |
| Dry-run final checkpoint | 已清理 |

---
