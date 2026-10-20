# code add gate autocorr logging

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add_gate_autocorr_logging_20260513T193933_result.json`
- **Structured JSON:** [`94ea23decab651ff764b.json`](../../sessions/94/94ea23decab651ff764b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**修改**: `models.py` 第 512-521 行（原第 511 行 `gate_entropy_ratio` 之后插入）

**autocorr 计算逻辑**:
- `dts` 形状 `(time, batch)`，沿 time 维度对每个 batch 元素计算 lag-1 自相关
- 中心化 → 计算方差和相邻项协方差 → 除以方差得 autocorr → clamp 到 [-1, 1]
- 对所有 batch 元素取均值，写入 `metrics["gate_dt_autocorr"]`
- 序列长度 ≤ 1 时输出 0.0

**语法验证**: `import models` → OK

**注意**: 此修改不影响当前运行的 exp_001 (PID 9409) 和 exp_005 (PID 51721)，只在下次启动实验时生效。

---
