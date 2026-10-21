# ssh fix exp011 resubmit

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-exp011-resubmit_20260519T174222_result.json`
- **Structured JSON:** [`d4d990899b3d9c35354f.json`](../../sessions/d4/d4d990899b3d9c35354f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_011 正在跑，不需要重新提交。

- **PID**: 319889（存活）
- **GPU 0**: 92% 利用率，51053 MiB 显存占用
- **进度**: 生成阶段 32640/40000 samples（~81.6%），正在推进

Registry 状态还是 PREPARING 是因为 cron reconcile 没能匹配到进程。需要我手动更新 registry 状态为 RUNNING 吗？

---
