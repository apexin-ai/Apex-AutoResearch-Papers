# analysis exp cheetah 008a s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_cheetah_008a_s0_20260527T171059_result.json`
- **Structured JSON:** [`b4eaf38315d333c3b8f1.json`](../../sessions/b4/b4eaf38315d333c3b8f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**exp_cheetah_008a_s0 → SUCCESS**

| 指标 | s0 | s1 |
|------|-----|-----|
| eval_return_105K | 366.2 | 281.2 |
| value_mean_105K | 164.6 | 164.3 |
| **NVE_105K** | **0.449** | **0.584** |
| eval_return_peak | 483.0 (85K) | 519.6 (75K) |
| civo_alert | 0 | 0 |

两个 seed 均 NVE << 2.0，civo_alert 始终为 0。Untrained dt=2 embedding 在 Cheetah Run 上同样产生 value suppression，C3 cross-env 泛化验证通过。Registry 已更新为 DONE，报告已注册 (`art_20260527_a60e39`)。

---
