# code verify 022b curriculum

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-022b-curriculum_20260517T103738_result.json`
- **Structured JSON:** [`b647374e9f65ac9e4ef7.json`](../../sessions/b6/b647374e9f65ac9e4ef7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Curriculum 代码逻辑 (`models.py:184-195`)

```python
def _update_gate_schedule(self):
    step = self._step
    phase1 = getattr(self._config, 'gate_curriculum_phase1', 25000)
    phase2 = getattr(self._config, 'gate_curriculum_phase2', 75000)
    if step < phase1:
        self._gate_scale = 0.0
    elif step < phase2:
        self._gate_scale = (step - phase1) / (phase2 - phase1)  # ← 潜在除零
    else:
        self._gate_scale = 1.0
    self._effective_max_dt = 1 + self._gate_scale * (max_dt_eff - 1)
```

### phase1=0, phase2=0 是否安全？

**安全。不会除零。**

当 phase1=0, phase2=0 时：
- `step < phase1` → `step < 0` → **永远 False**
- `step < phase2` → `step < 0` → **永远 False**
- 直接进入 `else` 分支：`gate_scale = 1.0`

从 **step=0 开始**：
- `gate_scale = 1.0`
- `effective_max_dt = 1 + 1.0 * (8 - 1) = 8`（假设 gate_max_dt=8）
- Gate 从第一步就完全解锁，Gumbel-softmax 可以自由选择任何 dt

**除零分支 `(step - phase1) / (phase2 - phase1)` 永远不会被执行**，因为它需要 `step >= phase1` 且 `step < phase2`，而 phase1=phase2=0 时这个区间为空。

### configs.yaml 默认值

```yaml
gate_curriculum_phase1: 50000   # 前 50k 步 gate 完全锁定 (gate_scale=0)
gate_curriculum_phase2: 150000  # 50k-150k 步线性解锁
```

这解释了 exp_022 gate 被锁住的原因：默认需要 50k 步 gate 才开始解锁，150k 步才完全解锁。

### 命令行参数是否有效？

`dreamer.py:446` 通过遍历 configs.yaml 的所有 key 动态注册 argparse 参数：
```python
parser.add_argument(f"--{key}", type=arg_type, default=arg_type(value))
```

`--gate_curriculum_phase1 0 --gate_curriculum_phase2 0` 是有效参数，会被正确解析为 int 0，不会被忽略或覆盖。

### 结论

`--gate_curriculum_phase1 0 --gate_curriculum_phase2 0` 完全安全，效果是从训练第一步就完全解锁 gate（gate_scale=1.0, effective_max_dt=gate_max_dt）。

---
