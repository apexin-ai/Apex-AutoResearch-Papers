# code update tost json

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update-tost-json_20260521T094636_result.json`
- **Structured JSON:** [`0ecf0fcdfd512097bd42.json`](../../sessions/0e/0ecf0fcdfd512097bd42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已更新。结果汇总与 Director 近似值对比：

### 精确计算结果

| Condition | Margin | mean_diff | SE | p_TOST | Equivalent? |
|-----------|--------|-----------|------|--------|-------------|
| **DD** | 5pp | 0.0000 | 0.0032 | 0.000047 | **Yes** |
| **DD** | 3pp | 0.0000 | 0.0032 | 0.000344 | **Yes** |
| **DD** | 2pp | 0.0000 | 0.0032 | 0.001599 | **Yes** |
| **AA** | 5pp | 0.0054 | 0.0262 | 0.0817 | No |
| **AA** | 3pp | 0.0054 | 0.0262 | 0.2002 | No |
| **AA** | 2pp | 0.0054 | 0.0262 | 0.3033 | No |

| Condition | Cohen's d (paired) |
|-----------|--------------------|
| DD | 0.0 |
| AA | 0.0923 |

### 与 Director 近似值对比

| 指标 | Director 近似 | 精确值 | 偏差 | 备注 |
|------|-------------|--------|------|------|
| DD all margins | p < 0.001 | 5pp: 4.7e-5, 3pp: 3.4e-4, 2pp: 1.6e-3 | — | **2pp 的 p=0.0016 > 0.001**，Director 说"all < 0.001"略有偏差，但仍 < 0.05 |
| AA 5pp | p = 0.08 | p = 0.0817 | < 0.01 | 一致 |
| AA 3pp | p ≈ 0.20 | p = 0.2002 | < 0.01 | 一致 |
| AA 2pp | p ≈ 0.31 | p = 0.3033 | < 0.01 | 一致 |
| DD Cohen's d | ≈ 0 | 0.0 | 0 | 一致 |
| AA Cohen's d | ≈ 0.18 | **0.0923** | **0.088** | **偏差 > 0.02，标注** |

**关键偏差**：
1. **DD 2pp**: Director 称 "all p < 0.001"，实际 p = 0.0016（仍显著，但严格来说 > 0.001）
2. **AA Cohen's d**: Director 近似 0.18，精确值 0.0923，**偏差 0.088 >> 0.02 阈值**。实际效应量比 Director 估计的更小（negligible 级别）

---
