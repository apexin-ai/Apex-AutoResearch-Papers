# diagnose eval object v4 task1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-object-v4-task1_20260513T224554_result.json`
- **Structured JSON:** [`2b80e5699eba8e295910.json`](../../sessions/2b/2b80e5699eba8e295910.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结论：**Bug，不是正常难度**

### 确认的 Bug

**`evaluate.py` 第 197-198 行：**
```python
obs = env.set_init_state(init_state)  # 设置 demo 初始状态，返回正确 obs
env.reset()                            # ← BUG：重置到默认状态，丢弃 init_state
```

**LIBERO 官方评估模式（lifelong/evaluate.py:260, metric.py:117）：**
```python
obs = env.set_init_state(init_states_)
# 无 env.reset()
# 然后 5 步零动作让物理引擎稳定
for _ in range(5):
    env.step(np.zeros((env_num, 7)))
```

**影响：**
1. `env.reset()` 将环境重置为默认状态，丢弃了从 demo 录制的 `init_state`
2. `obs` 保存的是 `init_state` 的图像，但实际环境已经是 `reset()` 的状态 → **第一步的观测和环境状态不匹配**
3. 后续步骤的 obs 来自 `env.step()` 是正确的，但环境已经从错误的初始状态开始
4. 缺少 5 步零动作物理稳定步骤（次要问题）

**此 bug 影响所有 10 个 task，不只 alphabet_soup。**

### 当前进度

| 项目 | 状态 |
|------|------|
| 进程 | 仍在运行（tmux session `eval-object-v4-full`, PID 103767） |
| 完成 | Task 1/10 (alphabet_soup: 0/10 = 0%) |
| 预计 | ~2.5h/task × 10 tasks ≈ 25h 总计 |
| 异常 | 无 Traceback、无 Error，纯粹 rollout 全部失败 |

### 修复建议

`rollout_single` 应改为：
```python
def rollout_single(env, init_state, action_fn, max_steps=300):
    obs = env.set_init_state(init_state)
    # 删除 env.reset()
    # 添加物理稳定步骤
    for _ in range(5):
        obs, _, _, _ = env.step(np.zeros(7))
    
    for step in range(max_steps):
        ...
```

### 建议

当前评估结果不可信，应该**终止当前进程、修复后重跑**。继续跑完剩余 9 个 task 只会浪费 ~22.5h GPU 时间。

---
