# experiment wave3 dir h adversarial

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_wave3-dir-h-adversarial_20260520T094545_result.json`
- **Structured JSON:** [`560abf032cd8d61ac95e.json`](../../sessions/56/560abf032cd8d61ac95e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已经在运行，无需重新启动。当前状态：

**进度**: 57/204 (28%), 速度 ~30s/题, 预计 ~19:05 完成

**中间正确率 (57题)**:
- SC: 34/57 = **59.6%**
- AdvW: 32/57 = **56.1%**

AdvW 暂时低于 SC 3.5pp。看起来 adversarial weighting 在一些 case 上翻转了原本正确的 SC 答案（如 folio_16: SC=Unknown(Y) → AdvW=False(N)）。

脚本代码完整，用 port 8012 上的 vLLM，输出到 `results/direction_h_adversarial/results.json`。还有 adv_only、adv_filter 两个策略会在最终结果中一起报告。

等它跑完后收集最终结果。要现在轮询等待，还是稍后再查？

---
