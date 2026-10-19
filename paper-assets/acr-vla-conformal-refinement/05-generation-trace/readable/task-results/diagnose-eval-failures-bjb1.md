# diagnose eval failures bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-failures-bjb1_20260513T233539_result.json`
- **Structured JSON:** [`145d35d95769761135b0.json`](../../sessions/14/145d35d95769761135b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因已定位。

---

- **失败原因**：`rollout_single` 在每个 episode 开始时只调 `env.set_init_state()` 而不调 `env.reset()`，robosuite 的 `done` 标志未被清除，后续 `env.step()` 抛出 `ValueError: executing action in terminated episode`。

- **详细分析**：

  三个实验的 traceback 完全一致，崩溃点在 `evaluate.py:203`：

  ```python
  def rollout_single(env, init_state, action_fn, max_steps=300):
      obs = env.set_init_state(init_state)
      for _ in range(5):
          obs, _, _, _ = env.step(np.zeros(7))  # ← 这里崩溃
  ```

  `set_init_state()` 设置了初始状态但不重置 robosuite 内部的 `self.done` 标志。当前一个 episode 正常结束（`done=True`，成功完成任务）或异常终止后，环境仍处于 terminated 状态。robosuite `base.py:376` 检查到 terminated 就抛异常。

  `eval-acr-spatial-v2` 的日志最能说明问题——它在 step 17 先触发了一次（被 try/except 捕获，返回 False），但下一个 rollout 的 warm-up steps（第 203 行）在 try/except 之外，直接 crash 了整个进程。

- **修复建议**：

  在 `rollout_single` 中，`set_init_state` 之前加 `env.reset()`：

  ```python
  def rollout_single(env, init_state, action_fn, max_steps=300):
      env.reset()                          # ← 加这行
      obs = env.set_init_state(init_state)
      for _ in range(5):
          obs, _, _, _ = env.step(np.zeros(7))
  ```

  同时，warm-up 步骤也应放进 try/except 内，避免同类异常再次 crash 整个进程。

- **是否可重试**：是，修复代码后直接重跑即可。这是确定性的代码 bug，与 OOM/GPU/环境无关。

---
