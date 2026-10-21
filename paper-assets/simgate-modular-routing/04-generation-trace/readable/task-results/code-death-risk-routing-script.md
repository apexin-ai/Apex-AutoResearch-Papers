# code death risk routing script

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_death-risk-routing-script_20260517T091306_result.json`
- **Structured JSON:** [`f54a0a0753c18c2d8624.json`](../../sessions/f5/f54a0a0753c18c2d8624.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有结果匹配：

| 指标 | 预期 | 实际 |
|------|------|------|
| always-det | -9.47 | -9.47 |
| always-internal | -39.07 | -39.07 |
| optimal threshold | 0, score -11.03, delta -1.56 | 0, -11.03, -1.56 |
| find-non-living-thing | 唯一零死亡, +18.9/+28.5 | 0% death, +18.9/+28.5 |
| 其余10 tasks | 45-56% | 45-56% |
| bootstrap CI | [-8.87, +5.92] | [-9.01, +5.89] |

Bootstrap CI 微小差异来自 Python `random` 模块实现差异，方法一致（unpaired resampling）。

- **脚本路径**: `/root/autodl-tmp/simgate-modular-routing/scripts/death_risk_routing.py`
- **输入数据**: `/root/autodl-tmp/simgate-modular-routing/results/baseline_245eps/episode_details.jsonl`
- **运行**: `python3 scripts/death_risk_routing.py`

---
