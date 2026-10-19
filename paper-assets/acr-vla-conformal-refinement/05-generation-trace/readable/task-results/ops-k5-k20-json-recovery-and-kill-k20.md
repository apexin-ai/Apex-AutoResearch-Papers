# ops k5 k20 json recovery and kill k20

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_k5-k20-json-recovery-and-kill-k20_20260517T221700_result.json`
- **Structured JSON:** [`82c3dc0fa7b9d7d546f6.json`](../../sessions/82/82c3dc0fa7b9d7d546f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### K=5 (PID 713405, 仍在运行)
- **进度**: 4/10 tasks 完成，第5个 task (ketchup) 正在跑 rollout 9/10
- **Per-task SR**:
  | Task | SR |
  |------|-----|
  | pick_up_the_alphabet_soup | 0% (0/10) |
  | pick_up_the_cream_cheese | 0% (0/10) |
  | pick_up_the_salad_dressing | 20% (2/10) |
  | pick_up_the_bbq_sauce | 30% (3/10) |
- **当前总体 SR**: 5/40 = 12.5% (4个完成的task)
- **JSON 文件尚未生成**（完成全部10 tasks后才写入）

### K=20 (PID 713480)
- **进度**: 1/10 tasks 完成
- **Per-task SR**: alphabet_soup 0% (0/10)
- **JSON 文件不存在**

### K=20 Kill 确认
- 进程 713480 已终止 ✓
- GPU cuda:2 已释放（4MiB idle）✓
- 当前 GPU 占用: GPU 0 = K=5 (3785MiB), GPU 1/2 = idle, GPU 3 = 另一进程 PID 749547 (5645MiB)

---
