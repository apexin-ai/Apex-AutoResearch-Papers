# code audit curriculum fixed dt

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_audit_curriculum_fixed_dt_20260514T005602_result.json`
- **Structured JSON:** [`e6235f085f7f85a3ee40.json`](../../sessions/e6/e6235f085f7f85a3ee40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出报告

### 1. Curriculum 在 fixed_dt 模式下的确切行为

**结论：Curriculum 在 fixed_dt 模式下完全不生效。原始假设是错误的。**

代码路径 (`models.py:200-205`)：
```python
if self._config.gate_fixed_dt > 0:
    effective_max_dt = float(self._config.gate_fixed_dt)  # 直接取 config 值 = 2.0
    gate_scale = 0.0                                       # gate loss 置零
else:
    self._update_gate_schedule()  # ← curriculum 只在这个分支执行
```

- **Training**: `subsample_variable_dt` 从 step 0 就收到 `effective_max_dt=2.0`，采样 dt∈{1,2}（log-uniform，约 58.5% dt=1, 41.5% dt=2）。**不存在 0-25K 纯 dt=1 阶段。**
- **Imagination** (`models.py:581-598`): `gate_active=False`（因 `gate_fixed_dt != 0`），直接用 `dt=2` hardcode。**也不受 curriculum 控制。**

### 2. 发现的实际 bug 及修复

| Bug | 位置 | 修复 |
|-----|------|------|
| `_effective_max_dt` 在 fixed_dt 模式下永远为 1.0，导致 `gate_entropy_ratio` 指标错误 | models.py:156 (init) vs :202 | 在 fixed_dt 分支加 `self._effective_max_dt = effective_max_dt` |
| `_update_gate_schedule` 硬编码 25K/75K，忽略 config 中的 `gate_curriculum_phase1: 50000` / `phase2: 150000` | models.py:182-185 | 改用 `getattr(self._config, 'gate_curriculum_phase1', 25000)` |

### 3. Commit

`6159e46` — `fix: sync _effective_max_dt in fixed_dt mode + use config curriculum phases`

改动 `models.py`，+6 行 -3 行，不影响 exp_006（已在内存中运行）。

### 4. Dry-run

通过。`--gate_fixed_dt 2` 正常启动，prefill + 训练均无报错。

### 5. 关于 exp_009

由于 curriculum 假设不成立，**exp_009 与 exp_006 配置完全相同**——重跑不会产生新信息。

真正的 train/imagine 分布差异是：训练用 58.5% dt=1 + 41.5% dt=2 混合数据，但 imagination 纯 dt=2。如果要排查这个方向，可能的 exp_009 设计：
- **纯 dt=2 训练**：修改 `subsample_variable_dt` 支持 `min_dt=2`，消除 dt=1 数据
- **纯 dt=1 baseline**：`--gate_fixed_dt 1`（等价于原版 DreamerV3），确认 dt=1 不崩

但 return 崩塌可能有其他原因（reward scaling 在大 dt 下的数值问题、value function 对 dt-conditioned 特征的泛化等），建议先回顾 exp_006 的 tensorboard 看崩塌时其他指标的变化。

---
