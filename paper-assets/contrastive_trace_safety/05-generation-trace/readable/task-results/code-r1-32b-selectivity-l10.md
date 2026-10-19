# code r1 32b selectivity l10

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r1_32b_selectivity_l10_20260517T001541_result.json`
- **Structured JSON:** [`4e872c4682a89343a5db.json`](../../sessions/4e/4e872c4682a89343a5db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

**R1-32B Layer 10 Selectivity = 7.5pp**（低于旧 layer 2 的 16.8pp）

| Metric | Layer 10 | Layer 2 (旧) |
|--------|----------|-------------|
| Real probe bal_acc | 58.3% | — |
| Random mean | 50.8% ± 5.1% | — |
| Selectivity | 7.5pp | 16.8pp |

Layer 10 信号反而更弱。Random baseline 方差大（有单次 rep 达 61.3% 超过 real probe），说明 layer 10 对 C2 任务的 step-level 区分力不强。Layer 2 的 16.8pp 仍是 R1-32B 更可靠的 selectivity 结果。

报告已写入 `artifacts/report_r1_32b_selectivity_l10.md`。

---
