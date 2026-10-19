# diag exp002v2 adaptive gate check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp002v2-adaptive-gate-check_20260519T015710_result.json`
- **Structured JSON:** [`cf3d30d0db8c66e04904.json`](../../sessions/cf/cf3d30d0db8c66e04904.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**确认：代码中存在 adaptive gate，且已触发，在 step 100 后将 weak 样本的 R1 归零。**

---

### 1. Gate 代码完整逻辑

文件：`/root/contrastive_entrain_calib/training/run_exp002v2_dcgrpo_cosine.py`

**配置常量：**
```python
GATE_WARMUP_STEPS = 10      # 前 10 步收集统计
GATE_ACTIVATE_STEP = 100    # step 100 后执行 gate
```

**Gate 判定条件（step 10 时执行一次）：**
```python
gate = abs(mu) < 0.05 or (abs(mu) > 1e-9 and sd > abs(mu))
```
weak R1 统计：`mean=-0.0256, std=0.1052, n=70`
→ `abs(-0.0256) = 0.0256 < 0.05` → **True → GATED**

**Gate 执行逻辑（step >= 100 后每步执行）：**
```python
if step >= GATE_ACTIVATE_STEP and self._weak_r1_gated:
    for i, s in enumerate(strengths):
        if s == "weak" and i < len(rewards):
            rewards[i] -= self._r1_w * components["r1"][i]
```
对所有 `evidence_strength == "weak"` 的样本，从 combined reward 中减去 R1 分量，等效于 R1=0。

### 2. 影响范围

从 warmup 统计：
- **weak: n=70** (44%)
- medium: n=50 (31%)
- strong: n=40 (25%)

**~44% 的训练样本在 step 100 后变为 R3-only 训练。**

### 3. 日志中的 R1 值

日志中 `r1_mean` 始终非零（范围约 -0.09 ~ +0.02），但这是**原始 R1 component 值**，不是 gate 后的 combined reward。Gate 操作发生在 `rewards[i]` 上（减去 R1 分量），不修改 `components["r1"]`，所以日志不反映 gate 效果。

**实际情况：step 100 后，近半数样本的梯度信号完全不受 R1 驱动。**

### 4. Gate 日志确认

```
2026-05-19 08:06:57,650 [INFO] exp002v2: ADAPTIVE GATE: weak R1 mean=-0.0256 std=0.1052 n=70 -> GATED (R1=0 for weak after step 100)
```

### 5. 注意

`dcgrpo_trainer.py` 实际路径是 `/root/mvp_v2_1_expanded/training/dcgrpo_trainer.py`（run script 中 `sys.path.insert(0, "/root/mvp_v2_1_expanded/training")`），不在 contrastive_entrain_calib 目录下。Gate 中引用的 `self._r1_w` 应来自该父类。

---
