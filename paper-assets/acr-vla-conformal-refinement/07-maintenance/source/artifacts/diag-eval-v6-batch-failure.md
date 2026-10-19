# 诊断报告：eval 三实验批量失败

**日期**: 2026-05-13  
**服务器**: bjb1-18228  
**涉及实验**: eval-spatial-v6-full, eval-acr-spatial-v2, eval-reconvla-spatial-v3

## 根因

**同一根因**：`src/evaluate.py:203` 的 warm-up 循环在环境已终止时调用 `env.step()`，触发 robosuite 的终止检查。

```
ValueError: executing action in terminated episode
  at robosuite/environments/base.py:376
```

### 调用链

```
evaluate.py:299  evaluate() → rollout_single()
evaluate.py:203  rollout_single() → env.step(np.zeros(7))  ← warm-up, 无 try/except
robosuite/base.py:376  → raise ValueError("executing action in terminated episode")
```

### 为什么三个实验同时失败

`rollout_single()` 的 warm-up 循环（第 201-203 行）：

```python
def rollout_single(env, init_state, action_fn, max_steps=300):
    obs = env.set_init_state(init_state)
    for _ in range(5):
        obs, _, _, _ = env.step(np.zeros(7))  # ← 无保护，终止态直接崩溃
```

问题：
1. `set_init_state()` 不一定清除 robosuite 内部的 `done` 标志
2. 前一个 rollout 结束后 `done=True` 残留到下一次 rollout
3. warm-up 步骤没有 try/except 包裹 → ValueError 直接 propagate 到顶层 → 进程退出
4. 主循环（第 206-212 行）有 try/except 保护，但 warm-up 没有

### 各实验失败时机

| 实验 | 失败位置 | 说明 |
|------|---------|------|
| eval-spatial-v6-full (vla_only) | 第一个 task 的第一个 rollout | env 创建后未 reset，done 可能默认 True |
| eval-reconvla-spatial-v3 | 第一个 task 的第一个 rollout | 同上 |
| eval-acr-spatial-v2 | 某 task 的第 6 个 rollout | 前一个 rollout 结束后 done=True 残留 |

## 系统状态（排除其他因素）

- **GPU**: 4x RTX 4090，正常工作，无 OOM
- **磁盘**: 根分区 34%，数据盘 46%，充足
- **非 CUDA/OOM/import 错误**

## 修复方案

**文件**: `src/evaluate.py`，第 200-203 行

修改前：
```python
def rollout_single(env, init_state, action_fn, max_steps=300):
    obs = env.set_init_state(init_state)
    for _ in range(5):
        obs, _, _, _ = env.step(np.zeros(7))
```

修改后：
```python
def rollout_single(env, init_state, action_fn, max_steps=300):
    env.reset()  # 清除前一个 rollout 的 terminated 状态
    obs = env.set_init_state(init_state)
    for _ in range(5):
        obs, _, _, _ = env.step(np.zeros(7))
```

**一行修复**：在 `set_init_state()` 前加 `env.reset()` 清除 robosuite 的 `done` 标志。

### 为什么这样修

- `env.reset()` 会将 robosuite 内部状态（包括 `self.done`）重置为初始值
- 随后 `set_init_state()` 加载指定的初始状态覆盖环境，不影响功能
- 不需要修改 warm-up 逻辑或添加 try/except（治标不治本）

## 需要改代码

是。改 `src/evaluate.py` 第 201 行，插入一行 `env.reset()`。
