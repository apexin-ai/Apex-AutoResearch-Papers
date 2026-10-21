# code r7 qwq position baseline

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r7_qwq_position_baseline_20260518T053447_result.json`
- **Structured JSON:** [`7d917ce5bf027766db46.json`](../../sessions/7d/7d917ce5bf027766db46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。汇总如下：

```
QwQ-32B Position-only Baseline (Layer L60 corrected):

Method                   Bal_Acc   Precision    FPR
─────────────────────────────────────────────────────
Position 2D              0.817     0.519       0.247
Position temporal W3     0.832     0.519       0.241
HS probe L60 W3          0.796     0.564       0.217

HS probe vs Position 2D gaps:
  Precision: +4.5pp (0.564 vs 0.519)
  FPR:       -3.0pp (0.217 vs 0.247)

HS probe vs Position temporal W3 gaps:
  Precision: +4.5pp (0.564 vs 0.519)
  FPR:       -2.5pp (0.217 vs 0.241)
```

关键发现：
- Position baseline 的 bal_acc 反而略高于 HS probe (0.832 vs 0.796)，因为位置信息本身就有一定预测力（harmful steps 偏向 trace 后段）
- 但 HS probe 在 precision 和 FPR 上均优于 position baseline，说明 hidden state 提供了超越位置信息的区分能力
- Position baseline 100% crossing rate 但 precision 仅~0.52（接近随机），大量 false positive；HS probe precision 更高 (0.564)、FPR 更低 (0.217)

---
