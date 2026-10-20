# code factorial exp 008ab

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_factorial_exp_008ab_20260514T011354_result.json`
- **Structured JSON:** [`595ae78ed5646f33bda7.json`](../../sessions/59/595ae78ed5646f33bda7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. GPU 清理
两张 GPU 均已清空（0 MiB / 0%），所有 python/dreamer 进程已终止。

### 2. subsample_variable_dt 工作机制

`tools.py:763` 定义的函数，按 batch 维度对 replay 轨迹做 variable-dt 子采样：
- 每个 batch element 从 log-uniform `[min_dt, effective_max_dt]` 采样一个 dt
- dt>1 时跳帧：累计折扣奖励、取 continuation 最小值
- `effective_max_dt <= 1` 时直接返回原始数据（无子采样）

在 `models.py:202-205`，`gate_fixed_dt > 0` 时 `effective_max_dt = gate_fixed_dt`，**同一个值同时控制 imagination dt 范围和 subsample dt 范围**，导致无法独立做析因实验。

### 3. 代码改动

**Commit**: `576ab86` — `feat: add gate_subsample_max_dt to decouple subsample range from imagination dt`

**configs.yaml** (line 116):
```yaml
gate_subsample_max_dt: 0    # 0=follow effective_max_dt (backward compatible), >0=override subsample range
```

**models.py** (lines 213-217，在 subsample_variable_dt 调用前):
```python
subsample_max_dt_override = getattr(self._config, 'gate_subsample_max_dt', 0)
if subsample_max_dt_override > 0:
    subsample_eff_dt = float(subsample_max_dt_override)
else:
    subsample_eff_dt = effective_max_dt
```
然后传 `effective_max_dt=subsample_eff_dt` 给 `subsample_variable_dt`。

`self._effective_max_dt`（imagination 用）不受影响，保持由 `gate_fixed_dt` 控制。

### 4. Dry-run 结果
两个实验均成功完成 200 steps dry-run，产出 metrics.jsonl、tfevents、train_eps，无报错。

### 5. 完整启动命令

**exp_008a** — 隔离 subsample 效应（imagination dt=2，subsample 禁用）：
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_fixed_dt2_no_subsample --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1"
```

**exp_008b** — 隔离 imagination 效应（imagination dt=1，subsample dt∈{1,2}）：
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008b_fixed_dt1_subsample2 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2"
```

| 实验 | gate_fixed_dt | gate_subsample_max_dt | imagination dt | 训练数据 |
|------|--------------|----------------------|----------------|---------|
| 008a | 2 | 1 | dt=2 | 纯 dt=1（无子采样） |
| 008b | 1 | 2 | dt=1（标准 DreamerV3） | dt∈{1,2} 混合 |

---
