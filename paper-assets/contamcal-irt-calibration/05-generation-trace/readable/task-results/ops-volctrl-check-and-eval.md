# ops volctrl check and eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_volctrl-check-and-eval_20260523T013614_result.json`
- **Structured JSON:** [`da8c9e0cc070cf99323d.json`](../../sessions/da/da8c9e0cc070cf99323d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练仍在运行，未完成。

**训练状态：**
- PID 752802 活跃，GPU 0 占用 19600MiB / 24564MiB，GPU-Util 97%
- 进度：619/4159 steps（15%），已运行 ~44 分钟
- 预估剩余：~4h18m（按 ~4.3s/step）
- Loss 从 ~1.36 降至 ~1.22，token accuracy 从 ~0.70 升至 ~0.73，训练正常收敛
- lora_adapter 目录已创建（08:52），checkpoint 开始写入

**结论：**训练大概率不是 6h 前启动的，实际运行约 44 分钟，还需约 4.3 小时完成。不启动 eval，不更新 registry。

需要我设置定时检查（约 4.5h 后回来看完成状态并启动 eval）吗？

---
