# diagnose pi05 action queue fix status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-action-queue-fix-status_20260521T054823_result.json`
- **Structured JSON:** [`266d446476546a008922.json`](../../sessions/26/266d446476546a008922.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

**修复已应用，verify 已完成，但结果不理想。**

### 1. 代码修改状态：✅ 完整且正确
- **文件位置**：`/root/acr-vla-conformal-refinement/src/pi05_wrapper.py`（不在 `src/models/` 下）
- **wrapper 实现**（pi05_wrapper.py）：
  - L22: `from collections import deque`
  - L63: `self._action_queue = deque()` in `__init__`
  - L382-384: `reset_action_queue()` clears queue
  - L386-408: `predict_action()` 队列空时推理→入队，非空时 `popleft()` 返回
  - chunk 取 K 样本均值（`samples[0].mean(dim=0)`）
- **evaluate.py wiring**：
  - L174-175: `wrapper.predict_action(...)` 被正确调用（PI05 路径）
  - L480-481: 每个 rollout 开始前调用 `wrapper.reset_action_queue()`

### 2. Quick verify 结果：❌ SR = 0%
- **运行参数**：`--task_filter bbq_sauce`, `n_rollouts=5`, `seed=42`, `vla_only`
- **输出**：`logs/pi05_action_queue_quicktest.json`
- **结果**：`pick_up_the_bbq_sauce`: 0/5 (0%)
- **日志**：`/tmp/pi05_quicktest.log`（完整结束，无 exception）

### 3. 环境状态
- GPU 0：空闲（0 MiB / 24564 MiB）
- 无 evaluate/pi05 进程在跑
- 旧 PID 831620 已不存在

### 4. 关键观察
- 修复代码本身没问题，wiring 正确
- 但 **只测了 1 个 task（bbq_sauce）** 就 5/5 失败
- 成功标准是「任何 task SR > 0%」，单 task 测试不能证伪修复
- 日志里没有 gripper 维度的诊断打印，无法直接看 gripper 是否已不再恒定

**建议**（如需）：跑全部 10 个 object tasks 各 5 rollouts，确认是否真有 0 task 成功。是否要启动？

---
