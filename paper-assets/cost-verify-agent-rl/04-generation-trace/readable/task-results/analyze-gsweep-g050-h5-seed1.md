# analyze gsweep g050 h5 seed1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_gsweep_g050_h5_seed1_20260517T144350_result.json`
- **Structured JSON:** [`ef687c877f4deffdd0e0.json`](../../sessions/ef/ef687c877f4deffdd0e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**gsweep_g050_h5_seed1: 基础设施故障（conclusion=failed）**

- **0 个训练步骤完成**，hypothesis 从未被测试
- **崩溃原因**：vLLM rollout 初始化时 `torch._inductor/select_algorithm.py` 抛出 `AssertionError: duplicate template name`——这是 westd-47453 上 vLLM 与 PyTorch 版本不兼容
- **无 W&B 数据、无 checkpoint**
- **与 hsweep_h2_seed1 的对比无法进行**

Registry 已更新：metrics（含崩溃原因、阶段、路径）和 notes 均已写入。重试前需修复 westd-47453 上的 vLLM/PyTorch 版本兼容性问题。

---
