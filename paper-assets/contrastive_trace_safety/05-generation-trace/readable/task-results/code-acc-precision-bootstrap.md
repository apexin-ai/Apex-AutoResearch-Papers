# code acc precision bootstrap

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acc_precision_bootstrap_20260517T000825_result.json`
- **Structured JSON:** [`bb2512ef36f1b9cd9e32.json`](../../sessions/bb/bb2512ef36f1b9cd9e32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果:

| Model | Accuracy diff | p | Precision diff | p | Bonferroni |
|-------|--------------|---|---------------|---|------------|
| **r1-8b** | +8.2pp | 0.005 | +22.4pp | 0.000 | **通过** |
| R1-32B | +6.2pp | 0.13 | +9.4pp | 0.064 | 未通过 |
| QwQ-32B | +0.9pp | 0.83 | +5.8pp | 0.35 | 未通过 |

**关键发现:**
- r1-8b 的 HS 优势在 accuracy 和 precision 上都显著通过 Bonferroni 校正 (α=0.0167)，效应量远强于之前的 FPR bootstrap (p=0.044)
- R1-32B 和 QwQ-32B 效应方向一致 (HS > Text) 但统计不显著，主因是 test set 太小 (n=20, 19)
- R1-32B precision CI=[0.0003, 0.205] 边缘排除 0，暗示更多数据可能达到显著
- QwQ HS probe 存在 convergence warning，可能低估了 HS 性能

报告已存于 `artifacts/acc_precision_bootstrap/report.md`。

---
