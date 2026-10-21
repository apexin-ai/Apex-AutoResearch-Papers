# analysis 019b ve trajectory

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_019b-ve-trajectory_20260517T145650_result.json`
- **Structured JSON:** [`3fc765fcf574b5222592.json`](../../sessions/3f/3fc765fcf574b5222592.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。产出保存在 `artifacts/analysis/exp_019b_analysis.json`。

关键结论：

1. **V/E trajectory**: Raw V/E peak = **5.66** @52.5K (NVE = 3.78× vs baseline)。Value 在 32.5K 达到峰值 27.17 后单调下降至 ~4.26，eval 在 52.5K 跌至谷底 3.69 后缓慢恢复。

2. **Eval 对比**: 019b final 26.64 vs 019a_v2 baseline 58.56，性能损失 54.5%。尽管 CIVO 自行消退，永久伤害已造成。

3. **Detector backtest = True Negative (TN)**：V/E spike 呈振荡模式（up-DOWN-up-DOWN），最大连续加速 streak = 2（需要 3 才触发）。Detector 正确不触发，因为 transient CIVO 自行消退，不满足"持续加速"条件。

4. **关键时间线**: onset ~22.5K → peak 52.5K → deflation 62.5K-102.5K → eval recovery peak 132.5K (26.87) → stable low regime。

---
