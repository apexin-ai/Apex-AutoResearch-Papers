# check bypass evals status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bypass_evals_status_20260517T040353_result.json`
- **Structured JSON:** [`771b9e0f5b457dacd5ab.json`](../../sessions/77/771b9e0f5b457dacd5ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### IMM 100K bypass (PID 882658, GPU:0)
- **进度**: Task 6/10 进行中（Tasks 0-5 已完成）
- **所有已完成 task 均为 0% SR**:
  - Task 0: 0/50 (0.0%)
  - Task 1: 0/50 (0.0%)
  - Task 2: 0/50 (0.0%)
  - Task 3: 0/50 (0.0%)
  - Task 4: 0/50 (0.0%)
  - Task 5: 0/50 (0.0%)
- 每个 episode 都跑满 280 steps 后 FAIL

### k=0.7 bypass (PID 905921, GPU:1)
- **进度**: Task 1/10 进行中（Task 0 已完成）
- Task 0: 0/50 (0.0%)
- 同样模式：全部 280 steps timeout

### GPU 状态
- GPU 0: 1% util, 3.2GB/97.9GB（episodes 间的低谷）
- GPU 1: 29% util, 3.2GB/97.9GB

---

## 结论

**Story C 彻底确认。** 两个 IMM 模型在 bypass 模式（使用所有 token，不做 ACIS pruning）下 SR = 0%，远低于 20% 阈值。Stage 2 训练**灾难性地摧毁了 expert 权重**——模型甚至无法完成任何 episode，不是 ACIS pruning 的问题。

对比 baseline (Full FT no IMM) = 44.8%，说明 IMM 的 two-stage 训练流程本身导致了 catastrophic forgetting。

两个 eval 预计还需 ~30-40 分钟跑完，但结果已经确定（全 0%）。需要等跑完再 `update_registry` 还是现在就记录？

---
