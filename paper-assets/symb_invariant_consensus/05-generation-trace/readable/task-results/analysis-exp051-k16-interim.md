# analysis exp051 k16 interim

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp051-k16-interim_20260519T021809_result.json`
- **Structured JSON:** [`41803e662ea788a604ca.json`](../../sessions/41/41803e662ea788a604ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Exp-051 K Sensitivity Interim 分析

### 进度

| K | 完成 | 状态 |
|---|------|------|
| 4 | 204/204 | ✅ done |
| 8 | 204/204 | ✅ done |
| 12 | 204/204 | ✅ done (exp-033) |
| 16 | 194/204 | ⏳ running, folio_195 |
| 20 | 0/204 | pending (K=16完成后自动开始) |

### K Sensitivity 结果

```
   K |     n |    SC% |  SICA% |   delta |   b |   c | p-value
-----+---------+--------+--------+---------+-----+-----+---------
   4 |   204 |  54.41 |  52.94 |  -1.47  |   7 |  10 |  0.6291
   8 |   204 |  57.35 |  56.37 |  -0.98  |   4 |   6 |  0.7539
  12 |   204 |  54.41 |  59.31 |  +4.90  |  12 |   2 |  0.0129 *
  16 |   194 |  55.67 |  57.22 |  +1.55  |  10 |   7 |  0.6291  (interim)
  20 |     - |      - |      - |       - |   - |   - |       -
```

### 趋势

1. **K=4, K=8: SICA 反而降低准确率**（-1.47pp, -0.98pp），均不显著。trace 太少，约束提取信号不足，反而引入噪声。
2. **K=12 是最佳点**：delta +4.90pp，唯一统计显著 (p=0.013)。discordant pair 极度不对称（b=12 vs c=2），说明约束有效纠错。
3. **K=16 (interim): SICA 有帮助但弱于 K=12**（+1.55pp），不显著。b/c=10/7，不对称性远弱于 K=12。

呈**倒 U 型**趋势：SICA 增益随 K 先升后降，K=12 处峰值。K=16 和 K=20 完成后可确认下降趋势。

---
