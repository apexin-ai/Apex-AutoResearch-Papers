# diagnose subsample max dt

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_subsample_max_dt_20260520T040203_result.json`
- **Structured JSON:** [`222030c19cd66cd65661.json`](../../sessions/22/222030c19cd66cd65661.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到了完整的命令行。两个实验的关键参数：

**exp_027 (TCN):**
```
--gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2
```

**exp_028 (RAVE):**
```
--gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99
```

两个都有 `--gate_fixed_dt 2`，没有 `--gate_subsample_max_dt`。

现在追踪代码逻辑确认最终生效值。

## 诊断结论

### 代码路径追踪 (`models.py` `_train()` 方法)

```python
# gate_fixed_dt = 2 > 0 → 进入 fixed dt 分支
effective_max_dt = float(self._config.gate_fixed_dt)  # = 2.0

# gate_subsample_max_dt = 0 (默认值，命令行没覆盖)
subsample_max_dt_override = getattr(self._config, 'gate_subsample_max_dt', 0)  # = 0
if subsample_max_dt_override > 0:
    subsample_eff_dt = float(subsample_max_dt_override)
else:
    subsample_eff_dt = effective_max_dt  # = 2.0  ← fallback 到 effective_max_dt

# 最终调用：
tools.subsample_variable_dt(data, 8, discount, effective_max_dt=2.0, min_dt=1)
```

### 关键发现

**`gate_subsample_max_dt=0` fallback 到的是 `effective_max_dt`，而 `effective_max_dt` 在 `gate_fixed_dt=2` 时等于 `2.0`，不是 `gate_max_dt=8`。**

所以 `subsample_variable_dt` 收到 `effective_max_dt=2`，会从 log-uniform[1, 2] 采样 dt，每个 batch element 获得 dt=1 或 dt=2。这与 bjb1-45299 显式传 `--gate_subsample_max_dt 2` 的效果**完全一致**。

### 回答你的三个问题

1. **`gate_subsample_max_dt` 实际生效值**：0（默认值），但 fallback 到 `effective_max_dt=2.0`，最终 subsample 的 effective_max_dt = **2**。

2. **是否能正确诱导 CIVO**：**能。** `subsample_variable_dt` 以 effective_max_dt=2 运行，产生 dt=1 和 dt=2 混合的训练数据，dt>1 的 transition 存在于训练中。日志中 `gate_dt_*` 指标显示的是 imagination 阶段（全部 dt=2 是因为 gate_fixed_dt=2 固定了 imagination dt），不是 subsample dt。

3. **不需要 kill。** 两台服务器的 subsample 行为等价，实验配置正确。bjb1-45299 的 `--gate_subsample_max_dt 2` 是冗余的（在 `gate_fixed_dt=2` 下 fallback 值已经是 2）。

---
