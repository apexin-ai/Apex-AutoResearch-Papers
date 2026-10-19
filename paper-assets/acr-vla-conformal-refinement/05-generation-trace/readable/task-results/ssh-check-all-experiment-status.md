# ssh check all experiment status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-all-experiment-status_20260523T014120_result.json`
- **Structured JSON:** [`d32093d0abb2374eb5a0.json`](../../sessions/d3/d32093d0abb2374eb5a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态总结：

**bjb1-32546** — 6个任务全部正常运行
- 5个方向实验均在 task 3/10，~25分钟已过，预计还需 ~1.5h
- CRM 4-suite 训练进入 epoch 34/50，epoch 33 达到新最佳 val_loss=0.0060

**bjb2-28827**
- Object CRM eval 3个 seed 均在 task 8/10，预计 ~30min 完成。7-task 均值：s42=46.4%, s43=50.0%, s44=49.3%
- Spatial VLA-only **已完成**：mean SR = **79.8%** (78.5/80.5/80.5)。GPU 3-5 空闲可复用

无异常/崩溃。报告已保存到 `artifacts/experiment_status_check.md`。

---
