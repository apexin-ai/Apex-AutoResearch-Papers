# diagnose seed7 mask check result

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed7_mask_check_result_20260522T193051_result.json`
- **Structured JSON:** [`e130784bd95daa109594.json`](../../sessions/e1/e130784bd95daa109594.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

BrokenPipeError 在第 8529 行，日志共 8577 行。结果输出在日志末尾（BrokenPipeError 之后），说明这个错误是 vLLM 清理阶段的 pipe 断开，eval 本身已完成。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| **状态** | 完成（进程已退出，结果已输出） |
| **enable_response_mask** | `True`（config 中确认） |
| **OOD pass@1** | **0.0**（134 episodes） |
| **OOD success** | 0.0 |
| **action_is_valid** | 0.9915 |
| **action_is_effective** | 1.0 |
| **response_length** | 4888.9 |
| **raw_reward** | 0.0 |
| **num_actions** | 50.0（全部 hit max） |
| **val-core reward mean@134** | 0.0 |

**解读：** seed7 step5 checkpoint 在 `enable_response_mask=True` 下 OOD pass@1 = 0.0%，134 episodes 全部失败。action_is_valid 很高（99.1%）说明模型格式没问题，但所有 episode 都用满了 50 步上限仍未完成任务。

这与 Reviewer 预期的"mask 不影响 eval generation"**不一致**——如果 mask=false baseline 的 OOD 结果不是 0.0%，那说明 response_mask 在 eval 阶段确实产生了影响；如果 baseline 也是 0.0%，则说明 step5 checkpoint 本身在 OOD 上就是 0%，与 mask 无关。需要对比 mask=false 的结果来下结论。

---
