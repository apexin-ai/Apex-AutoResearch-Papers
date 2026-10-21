# diag detach ln v2 s4

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_detach_ln_v2_s4_20260528T110837_result.json`
- **Structured JSON:** [`0e378146528ec7040feb.json`](../../sessions/0e/0e378146528ec7040feb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。总结：

**根因：系统 RAM OOM killer（高度疑似）**

westd-10894 上 3 个实验在 19:04 北京时间（11:04 UTC）2 分钟内连续被杀：

| 实验 | GPU | 信号 | 进度 | 损失 |
|------|-----|------|------|------|
| detach_ln_v2_s4 | cuda:1 | SIGTERM (-15) | 90% (step 45085) | ~1.3h 训练量 |
| vanilla_object_s2 | cuda:3 | SIGKILL (-9) | 43% (step 21378) | ~7.4h 训练量 |
| full_occ_bn_v2_s3 | cuda:2 | killed | ~43% | ~7.4h 训练量 |

判据：SIGKILL (-9) 是 OOM killer 标志信号；3 进程近乎同时死亡；无服务器重启；日志中无 Python 错误。dmesg 无权限无法 100% 确认。

所有 GPU 当前完全空闲，无 tmux session，无残留进程。如需重跑，建议先 `free -h` 检查系统 RAM，考虑减少并发实验数（3→2）。已更新 registry（3 个实验的 failure_reason）和 memory.md。

---
