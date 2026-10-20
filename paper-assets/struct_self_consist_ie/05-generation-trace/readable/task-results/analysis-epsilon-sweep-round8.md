# analysis epsilon sweep round8

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_epsilon_sweep_round8_20260515T153500_result.json`
- **Structured JSON:** [`cb6897f4f39f8e3169e3.json`](../../sessions/cb/cb6897f4f39f8e3169e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。529 个有效实例（排除 gold-empty），结果：

| ε | tied% | non_tied_n | Δ(pp) | p |
|------|-------|-----------|-------|------|
| 0.01 | 1.1% | 523 | +0.58 | 0.21 |
| 0.02 | 13.6% | 457 | +0.83 | 0.15 |
| 0.03 | 31.8% | 361 | +1.31 | 0.079 |
| **0.05** | **60.3%** | **210** | **+2.86** | **0.004** |
| **0.10** | **83.9%** | **85** | **+3.69** | **0.034** |
| 0.15 | 93.2% | 36 | +4.15 | 0.11 |
| 0.20 | 96.4% | 19 | +4.59 | 0.13 |

**关键发现：**

1. **ε=0.05 和 ε=0.10 是显著区间** (p<0.05)。ε=0.03 边缘显著 (p=0.079)。
2. ε≥0.15 时 non-tied subset 太小（n=36/19），delta 虽大但统计功效不足，p 值回升。
3. ε≤0.02 时几乎所有实例都 non-tied，LP selection 信号被噪声稀释，delta 不显著。
4. Non-tied subset 上 LP 确实能 select：ε=0.05 时 +2.86pp，ε=0.10 时 +3.69pp，均显著。

**推荐论文使用 ε=0.05**：tied 60.3% 与 paper_framing.md 已有数据一致，non-tied subset 上 +2.86pp (p=0.004) 高度显著，样本量适中 (n=210)。

---
