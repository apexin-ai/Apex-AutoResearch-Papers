# diagnose eval acr spatial v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-acr-spatial-v2_20260513T233304_result.json`
- **Structured JSON:** [`910d475c9ca803fe009e.json`](../../sessions/91/910d475c9ca803fe009e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因已清楚。分析完成：

**两个 traceback，同一个 bug：**

1. **第一个 traceback**（被 try/except 捕获，没有致命）：`rollout_single` 第 208 行 `env.step(action_7d)` 抛出 `ValueError: executing action in terminated episode`。这发生在 step 17，说明 env 在 step 17 之前已经 `done=True`（任务成功了），但由于上一步的 `done` 检查逻辑，代码继续调用了 `env.step()`。被 except 捕获后返回 `(False, 17)` — 把一次成功误判为失败，但不致命。

2. **第二个 traceback**（致命，导致 EXIT_CODE=1）：在 `rollout_single` 第 203 行，即函数开头的预热循环 `obs, _, _, _ = env.step(np.zeros(7))`。这个预热循环执行 5 次 zero-action step，但**没有检查 `done`**。如果 env 在前一次 rollout 结束后处于 terminated 状态且没有被正确 reset，这里就会崩。

**根因**：`rollout_single` 用 `env.set_init_state(init_state)` reset 环境，但 robosuite 在 `done=True` 后要求先调用 `env.reset()` 才能重新 step。`set_init_state` 可能没有清除 terminated flag，导致下一次 rollout 的预热 step 在 terminated episode 上执行。

```json
{"root_cause":"rollout_single line 203: env.step(np.zeros(7)) in warmup loop raises ValueError('executing action in terminated episode') because env.set_init_state() does not clear the terminated flag from the previous rollout","error_type":"infrastructure","fix_steps":["在 rollout_single 的 env.set_init_state(init_state) 之前添加 env.reset()，确保 terminated flag 被清除","或者在预热循环前加 done 检查: obs = env.reset(); env.set_init_state(init_state); obs = env._get_observations()","同时在主循环中，done=True 时应立即 break 或 return，避免再次 step 到 terminated env"],"can_auto_fix":true,"progress":"跑到了 task 1/10 的 rollout 5/10 (first task, 2/5 success before crash)","full_traceback":"Traceback (most recent call last):\n  File \"/root/acr-vla-conformal-refinement/src/evaluate.py\", line 358, in &lt;module>\n    main()\n  File \"/root/acr-vla-conformal-refinement/src/evaluate.py\", line 354, in main\n    evaluate(args)\n  File \"/root/acr-vla-conformal-refinement/src/evaluate.py\", line 299, in evaluate\n    success, steps = rollout_single(env, init_state, action_fn,\n  File \"/root/acr-vla-conformal-refinement/src/evaluate.py\", line 203, in rollout_single\n    obs, _, _, _ = env.step(np.zeros(7))\n  File \"/root/miniconda3/lib/python3.12/site-packages/libero/libero/envs/env_wrapper.py\", line 88, in step\n    return self.env.step(action)\n  File \"/root/miniconda3/lib/python3.12/site-packages/libero/libero/envs/bddl_base_domain.py\", line 808, in step\n    obs, reward, done, info = super().step(action)\n  File \"/root/miniconda3/lib/python3.12/site-packages/robosuite/environments/base.py\", line 376, in step\n    raise ValueError(\"executing action in terminated episode\")\nValueError: executing action in terminated episode"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "rollout_single line 203: env.step(np.zeros(7)) in warmup loop raises ValueError('executing action in terminated episode') because env.set_init_state() does not clear the terminated flag from the previous rollout",
    "error_type": "infrastructure",
    "fix_steps": [
      "在 rollout_single 的 env.set_init_state(init_state) 之前添加 env.reset()，确保 terminated flag 被清除",
      "或者在预热循环前加 done 检查: obs = env.reset(); env.set_init_state(init_state); obs = env._get_observations()",
      "同时在主循环中，done=True 时应立即 break 或 return，避免再次 step 到 terminated env"
    ],
    "can_auto_fix": true,
    "progress": "跑到了 task 1/10 的 rollout 5/10 (first task, 2/5 success before crash)",
    "full_traceback": "Traceback (most recent call last):\n  File \"/root/acr-vla-conformal-refinement/src/evaluate.py\", line 358, in &lt;module>\n    main()\n  File \"/root/acr-vla-conformal-refinement/src/evaluate.py\", line 354, in main\n    evaluate(args)\n  File \"/root/acr-vla-conformal-refinement/src/evaluate.py\", line 299, in evaluate\n    success, steps = rollout_single(env, init_state, action_fn,\n  File \"/root/acr-vla-conformal-refinement/src/evaluate.py\", line 203, in rollout_single\n    obs, _, _, _ = env.step(np.zeros(7))\n  File \"/root/miniconda3/lib/python3.12/site-packages/libero/libero/envs/env_wrapper.py\", line 88, in step\n    return self.env.step(action)\n  File \"/root/miniconda3/lib/python3.12/site-packages/libero/libero/envs/bddl_base_domain.py\", line 808, in step\n    obs, reward, done, info = super().step(action)\n  File \"/root/miniconda3/lib/python3.12/site-packages/robosuite/environments/base.py\", line 376, in step\n    raise ValueError(\"executing action in terminated episode\")\nValueError: executing action in terminated episode"
  }
}
```

</details>

---
