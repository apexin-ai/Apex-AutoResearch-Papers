# fix d134 pipeline oom restart

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d134-pipeline-oom-restart_20260518T105107_result.json`
- **Structured JSON:** [`461aa6b83fee42a11036.json`](../../sessions/46/461aa6b83fee42a11036.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

```
Config 确认: per_device_batch_size=2, gradient_accumulation_steps=4, num_generations=4
  (YAML 默认 batch=4/grad_accum=2，之前 pipeline 缺 CLI 覆盖导致 OOM)

修复措施:
  1. train 命令添加 --per_device_batch_size 2 --gradient_accumulation_steps 4
  2. 移除 set -eo pipefail，改用 PIPESTATUS + || true 容错
  3. 清理失败的 s47 输出目录后重启

新 PID: 2018 (GPU 0, 84778 MiB / 97887 MiB)
Step 30/500 确认无 OOM（之前在 step 21 崩溃）
磁盘: 193G/250G used, 58G available

预计时间: ~11s/step → ~92min/run (train), eval+classify ~15min/run
  10 runs 总计 ~18h
```

---
