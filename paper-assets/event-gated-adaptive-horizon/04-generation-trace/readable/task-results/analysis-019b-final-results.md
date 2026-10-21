# analysis 019b final results

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_019b-final-results_20260517T145038_result.json`
- **Structured JSON:** [`eb3cf576b1e12a97fa9f.json`](../../sessions/eb/eb3cf576b1e12a97fa9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Verdict: Negative (informative)**

关键发现：
- **Transient CIVO 确认**：NVE 峰值 3.78x @52.5K，与中间分析吻合，但随后快速塌缩至 0.065x
- **Eval 严重退化**：最终 26.64 vs baseline 58.56，仅为 baseline 的 21.4%
- **Gate 全程锁死**：gate_dt_2_frac=1.0, entropy=0.0，从第一个 checkpoint 到最后一个，gate 从未学会调节
- **Value function 永久塌缩**：019b value_mean 最终 4.26 vs baseline 144.57（仅 3%），value 规模再未恢复

与 Walker Walk 的关键区别：Walker 是持续 CIVO（NVE 维持 >1.5x），PickCube 是瞬态 CIVO（剧烈 spike 后 value collapse）。推测 PickCube 稀疏奖励结构导致更快修正但也更灾难性的塌缩。

报告已写入 `artifacts/exp_019b_final_analysis.md`。

---
