# code pi05 n action steps fix

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pi05-n-action-steps-fix_20260522T105018_result.json`
- **Structured JSON:** [`5282e2891961f081324a.json`](../../sessions/52/5282e2891961f081324a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**代码修改（4 台服务器均已部署并验证语法）：**
- `pi05_wrapper.py`: `__init__` 新增 `n_action_steps=10` 参数，`predict_action()` 中 action queue 只取前 `n_action_steps` 步（原来取全部 50 步）
- `evaluate.py`: 新增 `--n_action_steps` CLI 参数，传递给 `Pi05Wrapper` 构造函数

**已部署服务器：** bjb1-18228, bjb1-32546, bjb2-28827, bjb2-40593

**已提交实验（bjb1-18228，GPU 1/2/3）：**

| 实验 ID | Seed | GPU | PID | 日志 |
|---------|------|-----|-----|------|
| eval-pi05-vla-only-object-seed42-r4 | 42 | cuda:1 | 905242 | /tmp/eval_pi05_seed42_r4.log |
| eval-pi05-vla-only-object-seed43-r4 | 43 | cuda:2 | 905874 | /tmp/eval_pi05_seed43_r4.log |
| eval-pi05-vla-only-object-seed44-r4 | 44 | cuda:3 | 906424 | /tmp/eval_pi05_seed44_r4.log |

配置：`n_action_steps=10, K=10, max_steps=280, 20 rollouts/task, vla_only mode`。因 GPU 0 有占用，改用 GPU 1/2/3。

---
