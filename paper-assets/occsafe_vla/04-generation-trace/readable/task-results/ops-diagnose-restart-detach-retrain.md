# ops diagnose restart detach retrain

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_restart_detach_retrain_20260524T181604_result.json`
- **Structured JSON:** [`24024cf0e084694963bc.json`](../../sessions/24/24024cf0e084694963bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**诊断结果：**
- **崩溃原因**：无法确定。log 已被新进程覆盖，原 PID 775880 的 error traceback 丢失。磁盘充足（154GB avail），排除磁盘满。推测为瞬时 NCCL/OOM 错误。
- **实验已自动重启**：当前 PID 775953 在 GPU 0 上正常运行，从 20K checkpoint 恢复，已跑到 step ~839（全局 ~20839）。无需手动重启。
- **最新 checkpoint**：仍为 20000（崩溃前未到达下一个 save_freq=10000 的存档点 30000）。

**Registry 更新：**
- PID: 775880 → 775953
- 状态: RUNNING（维持不变）
- log: `/root/autodl-tmp/logs/ablation_occ_detach_s0_retrain_resume.log`
- resume_step: 20000

---
