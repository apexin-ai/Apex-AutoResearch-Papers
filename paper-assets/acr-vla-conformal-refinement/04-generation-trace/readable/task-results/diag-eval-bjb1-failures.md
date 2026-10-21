# diag eval bjb1 failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-bjb1-failures_20260513T234522_result.json`
- **Structured JSON:** [`52870d71caf24be3c143.json`](../../sessions/52/52870d71caf24be3c143.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因已清楚。以下是诊断结果：

---

## 诊断结果

### 失败根因（三个实验完全相同）

**`ValueError: executing action in terminated episode`** — 出自 `evaluate.py:203`

```python
def rollout_single(env, init_state, action_fn, max_steps=300):
    env.reset()
    obs = env.set_init_state(init_state)
    for _ in range(5):                          # warm-up loop
        obs, _, _, _ = env.step(np.zeros(7))    # ← line 203, 崩溃点
```

**问题机制：**
1. `env.reset()` 重置环境，`set_init_state()` 设置初始状态
2. `set_init_state()` 可能触发 robosuite 内部的完成判定，将 `self.done` 设为 `True`（例如初始物体位置恰好满足目标条件）
3. 之后的 warm-up `env.step()` 检测到 `self.done == True`，抛出 `ValueError`
4. **warm-up loop 没有 try/except 也没有 done 检查**，异常未被捕获，直接崩溃

对比：主 rollout loop（line 206-213）有 try/except 能兜住这个错误，但 warm-up loop 没有。acr_vla 实验的日志也印证了这一点——在第17步捕获了同样的异常后继续运行，但下一轮 rollout 的 warm-up 又崩了。

### 排除的因素
- **GPU**：4x RTX 4090 正常，温度/显存/利用率均无异常
- **磁盘**：30G 用了 11G (34%)，充裕
- **OOM**：无（dmesg 无法直接检查，但 GPU 显存远未用满）

### 修复方案

修改 `rollout_single` 函数，给 warm-up loop 添加 done 检查和异常保护：

```python
def rollout_single(env, init_state, action_fn, max_steps=300):
    env.reset()
    obs = env.set_init_state(init_state)
    done = False
    for _ in range(5):
        try:
            obs, _, done, _ = env.step(np.zeros(7))
        except ValueError:
            done = True
        if done:
            break

    if done:
        return False, 0

    for step in range(max_steps):
        ...
```

需要改动的文件：`/root/acr-vla-conformal-refinement/src/evaluate.py` 第 199-203 行。需要我直接修改吗？

---
