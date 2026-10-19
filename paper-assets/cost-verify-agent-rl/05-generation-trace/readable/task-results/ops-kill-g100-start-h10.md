# ops kill g100 start h10

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-g100-start-h10_20260518T173406_result.json`
- **Structured JSON:** [`2d8c589984d0f21de622.json`](../../sessions/2d/2d8c589984d0f21de622.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**g100 kill 确认**
- PID 714093 已 force kill，GPU 2,3 完全释放（0MiB → 验证通过）
- tmux session 已清理
- Registry: `gsweep_g100_h5_seed1` → DONE, conclusion=negative, metrics 已更新

**hsweep_h10_seed1 启动确认**
- **PID: 34193**
- **W&B run ID: x09p5xd0**
- tmux session: `hsweep_h10`
- GPU 2: 4.7GB, GPU 3: 4.7GB（模型加载中，vLLM 完全启动后会增加至 ~35GB）
- 日志: `/root/autodl-tmp/cost-verify-agent-rl/logs/hsweep_h10_seed1.log`

**factorial_seed2 不受影响** ✓
- PID 576727 正常运行
- GPU 0: 43.6GB, GPU 1: 43.9GB（正在 generate_sequences）

**Registry 更新** ✓
- `gsweep_g100_h5_seed1`: DONE / negative
- `hsweep_h10_seed1`: RUNNING，spec 含完整 provenance

**Cron 监控** ✓
- Job b489d217，每小时 :23 检查 h10 + factorial_seed2 状态

---
