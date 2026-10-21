# analysis 019b detector retrospective

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_019b-detector-retrospective_20260517T105035_result.json`
- **Structured JSON:** [`4edb0e94a47d3cedffd3.json`](../../sessions/4e/4edb0e94a47d3cedffd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Detector 在 step 52,500 触发，判定为 True Positive。**

### 核心发现

| | Walker Walk (collapse) | PickCube (019b) |
|---|---|---|
| 触发时间 | <65K | 52.5K |
| 触发类型 | TP (persistent CIVO) | TP (transient CIVO) |
| NVE 峰值 | 持续上升 | 3.78× then deflation → 0.08× |
| Gate 效果 | dt=2 不足以阻止 collapse | dt=2 足够，系统自我恢复 |

触发机制：step 32.5K 和 52.5K 两个窗口同时满足 magnitude (NVE > 0.49) 和 acceleration (> 0.1) 条件，在 [32.5K, 42.5K, 52.5K] 窗口达到 2/3 persistence 阈值。

### 对论文的影响

**正面：cross-environment claim 得到支持。** Detector 在 locomotion 和 manipulation 两种环境中都正确识别 CIVO，触发时间一致（均在 65K 前）。

**Discussion 建议 framing：**
- PickCube 展示的是 transient CIVO（detector 在急性期触发，系统随后自我纠正），与 Walker Walk 的 persistent CIVO 形成对比
- Detector 在两种模式下都能在早期检出，这是 early warning system 的正确行为
- 诚实承认 PickCube 只有 1 个 trigger 实验，统计效力有限，但机制层面的泛化已验证

报告已保存至 `artifacts/analysis_civo_detector_pickcube_backtest.md`。

---
