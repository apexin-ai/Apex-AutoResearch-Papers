# diagnose exp 002v2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-002v2_20260519T021132_result.json`
- **Structured JSON:** [`fba34eff63be77d1c486.json`](../../sessions/fb/fba34eff63be77d1c486.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：exp-002v2 是被手动 kill 的（D021 决策执行），不是异常崩溃。**

关键发现：
- `logs/exp002v2.log` 在 step 256 干净截断，无 traceback、无 OOM、无 CUDA error
- Adaptive gate 在 step 9 就激活了（`R1=0 for weak samples after step 100`），D021 判定这不利于训练，决定 kill 后禁用 gate 重启
- 旧 run 无 checkpoint 保存
- **exp-002v2 已按 D021 成功重启**（无 adaptive gate），PID 130467 正在 GPU 0 运行，当前 step ~4+，52GB VRAM，95% utilization，运行正常
- GPU 0 不空闲，已被新 run 占用

cron 报告的 "process dead 5x" 可能是 kill 后到重启之间的窗口期检测到的。

---
