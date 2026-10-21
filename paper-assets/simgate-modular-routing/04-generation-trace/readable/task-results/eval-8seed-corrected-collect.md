# eval 8seed corrected collect

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_8seed-corrected-collect_20260515T225948_result.json`
- **Structured JSON:** [`b1f93a8eba8bf28ebd04.json`](../../sessions/b1/b1f93a8eba8bf28ebd04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 8 个 seed 的 corrected eval 结果已完成。汇总如下：

=== 8-seed Corrected Eval Results ===

| Seed | Old (leaky) | Corrected | Δ |
|------|-------------|-----------|---|
| 42   | 0.5761      | 0.5706    | -0.0055 |
| 43   | 0.4852      | 0.6399    | +0.1547 |
| 44   | 0.6074      | 0.5543    | -0.0531 |
| 45   | 0.5467      | 0.5614    | +0.0147 |
| 46   | 0.4463      | 0.5545    | +0.1082 |
| 47   | 0.5185      | 0.5008    | -0.0177 |
| 48   | 0.5370      | 0.4803    | -0.0567 |
| 49   | 0.6111      | 0.5930    | -0.0181 |
| **Mean±Std** | **0.541±0.058** | **0.557±0.050** | **+0.016** |

关键发现：
- Corrected eval 的均值 **略高于** leaky eval（0.557 vs 0.541），说明修正 eval 后性能没有下降，反而微升
- 标准差从 0.058 降到 0.050，seed 间稳定性略有改善
- Seed 43 和 46 corrected 后提升明显（+0.15, +0.11），seed 44 和 48 略有下降（-0.05, -0.06）
- 结果已保存在服务器 `results/seed-robustness-corrected/` 目录

---
