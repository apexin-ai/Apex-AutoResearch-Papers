# check full gpu status and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full_gpu_status_and_eval_20260521T140201_result.json`
- **Structured JSON:** [`c7e08f9f348804ba5d91.json`](../../sessions/c7/c7e08f9f348804ba5d91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。3 个实验仍在训练中，无新完成实验需要跑 eval。

| GPU | 实验 | 状态 | Step/Total | Holdout PPL | OWT PPL | Wiki PPL |
|-----|------|------|------------|-------------|---------|----------|
| cuda:0 | detect_remove_q05 | 运行中 | 4410/6103 (72%) | — | — | — |
| cuda:1 | bs16_adaptive_tau07 | 运行中 | 523/6103 (9%) | — | — | — |
| cuda:2 | uniform_epoch_matched_indep_lr | 已完成+eval | 2533/2533 | 18.062 | 18.650 | 15.511 |
| cuda:3 | random_reweight_baseline | 运行中 | 3592/6103 (59%) | — | — | — |

预计完成时间：
- **detect_remove_q05**: ~1h 内完成（剩 1693 步，~2.08s/step）
- **random_reweight_baseline**: ~1.5h 完成（剩 2511 步，~2.2s/step）
- **bs16_adaptive_tau07**: ~3.8h 完成（剩 5580 步，~2.46s/step）

---
