# research check random reward isr field

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check-random-reward-isr-field_20260514T002625_result.json`
- **Structured JSON:** [`02843df4791e091e5980.json`](../../sessions/02/02843df4791e091e5980.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：**`isr_mean` 在 `random_reward` 模式下 = 真实 ISR（实际上恒为 0.0）**。

关键逻辑链：

**1. `random_reward` 分支（行 173-186）：**
```python
elif reward_mode == "random_reward":
    result = _fast_fn({}, cleaned, solver,
                      execution_weight=1.0, sta_weight=0.0, timeout=5)
    proved = result["execution_reward"] > 0
    if proved:
        rand_val = rng.random()
        reward_val = exec_weight * 1.0 + sta_weight * rand_val
        result["random_reward"] = rand_val
    else:
        reward_val = 0.0
        result["random_reward"] = 0.0
```

注意：调用 `_fast_fn` 时传入 `sta_weight=0.0`，所以 `result["sta_reward"]` 恒为 0.0。

**2. isr 取值（行 ~193）：**
```python
isr = result.get("sta_reward", 0.0)
```

**3. isr_mean 写入 log（行 ~229）：**
```python
step_buf["isr_sum"] += isr
# ...
"mean_isr": step_buf["isr_sum"] / n,
# ...
"isr_mean": step_stats.get("mean_isr", 0.0),
```

**结论：**
- `isr_mean` 取的是 `result["sta_reward"]`，即 STA reward 函数返回的真实 ISR 值
- 但由于 `random_reward` 分支调用时传 `sta_weight=0.0`，`fast_sta_reward` 不会计算 STA 分数，返回的 `sta_reward` = 0.0
- 所以 **`isr_mean` 在 random_reward 模式下应恒为 0.0**

如果你观察到 step 9 的 `isr_mean=0.5`，这不太正常——可能需要检查 `fast_sta_reward` 在 `sta_weight=0.0` 时是否仍然计算了 ISR，或者该 log 条目是否来自其他 reward_mode 的运行。

---
