# ssh dose response progress

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dose-response-progress_20260518T111722_result.json`
- **Structured JSON:** [`ce1dd66fb5c27caa4b0b.json`](../../sessions/ce/ce1dd66fb5c27caa4b0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

### GPU 状态
两张 RTX 5090 均正常工作，GPU-Util 99%，vLLM 进程各占一张卡。

---

### 实验 1: Retry dose-response (cuda:0)
- **进度: 153/200 episodes (76.5%)**
- 当前 task: `lifespan-longest-lived` ep012/019
- 已完成 7 个 task，第 8 个进行中
- 最新文件: 19:16（1 分钟前，持续产出中）
- 启动时间: 14:43，运行 4.5h
- 速率: ~0.57 ep/min
- **ETA: ~1.4h 后完成 (~20:40)**

---

### 实验 2: Reflexion dose-response (cuda:1)
- **N=1: 200/200 COMPLETE** (condition_summary.json 已生成，17:53 完成)
- **N=2: 103/200 (51.5%)**, 当前 task: `identify-life-stages-2` ep003
- N=3,4,5: 未开始
- **总进度: 303/1000 episodes (30.3%)**

速率估算:
- N=1: ~2.6 ep/min (77 min 完成 200 ep)
- N=2: ~1.24 ep/min (随 reflection 轮数增加变慢)

**ETA 估算:**
- N=2 剩余: ~1.3h
- N=3/4/5 随 N 增大会更慢，预计总计还需 ~15-17h
- **预计完成: 明天 ~12:00**

---
