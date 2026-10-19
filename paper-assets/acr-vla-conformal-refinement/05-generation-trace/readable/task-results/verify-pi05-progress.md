# verify pi05 progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_pi05-progress_20260521T030633_result.json`
- **Structured JSON:** [`cb0e189275460014d456.json`](../../sessions/cb/cb0e189275460014d456.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## π0.5 Baseline Eval 状态

**进程**: PID 802634 存活，已运行 1h18m
**GPU**: GPU 0 占用 13.5GB/24.6GB，利用率 37%

**进度**: 10 个 task 中：
- Task 1 `pick_up_the_alphabet_soup` — 完成，**0/20 (0%)**
- Task 2 `pick_up_the_cream_cheese` — 进行中，rollout 10/20，**0/10**

约完成 1.5/10 tasks。按当前速度（~52min/task），预计还需 **~7.5 小时**。

**⚠️ 关键问题：SR 目前为 0%。** 两个 task 共 30 个 rollout 全部失败，高度怀疑是 **normalization mismatch** 问题——π0.5 训练用 MEAN_STD normalization，而 wrapper 可能用了 QUANTILES。如果后续 task 继续 0%，这次 eval 的结果无效，需要修复 normalization 后重跑。

建议：可以现在就检查 `pi05_wrapper.py` 的 normalization 配置，确认是否与训练时一致，不必等全部 10 个 task 跑完再发现问题。

---
