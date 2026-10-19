# analyze cqa1 analyzing experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cqa1-analyzing-experiments_20260526T101807_result.json`
- **Structured JSON:** [`383a81da2a1f1851cd0b.json`](../../sessions/38/383a81da2a1f1851cd0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都**仍在运行**，未完成。cron 的 ANALYZING 检测是误报。

### s43 (PID 198442, GPU 4)
- **状态**：进程存活，已运行 4h23m
- **进度**：task 6/10 (STUDY_SCENE1) rollout 15/20 — 约 62.5%（远超 1h 前的 45%）
- **前 5 task SR**：80% / 100% / 95% / 95% / 90%（累计中位）
- **日志**：`/tmp/eval_pi05_long_s43.log` 最后写入 18:17，正常推进
- **JSON**：`logs/eval_long_adaptive_pi05_seed43.json` 时间戳 17:57，是**旧文件**（早于当前 run 启动时间），非本次产出

### s44 (PID 199049, GPU 5)
- **状态**：进程存活，已运行 4h22m
- **进度**：task 6/10 (STUDY_SCENE1) rollout 10/20 — 约 60%
- **前 5 task SR**：90% / 100% / 100% / 85% / 95%
- **日志**：`/tmp/eval_pi05_long_s44.log` 最后写入 18:10，正常推进
- **JSON**：`logs/eval_long_adaptive_pi05_seed44.json` 时间戳 17:58，旧文件

### GPU 状态
- GPU 4: 21% util, 11860 MiB used（占用中）
- GPU 5: 19% util, 11860 MiB used（占用中）

### 结论
**cron 误判**。两个进程依旧存活，GPU 也在用，实验尚未完成（约 60% 进度）。建议把状态从 ANALYZING 改回 RUNNING，约 2.5–3h 后才会真正结束。前 5 task 表现良好（s43 均值 92%，s44 均值 94%），最后 5 task 通常更难，最终 SR 估计 80–85%。

---
