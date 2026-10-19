# code repe corrected layers

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_repe_corrected_layers_20260517T151647_result.json`
- **Structured JSON:** [`1da84f24f8b2f8b9f4b4.json`](../../sessions/1d/1da84f24f8b2f8b9f4b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果已保存到 `artifacts/exp_r3_repe_corrected_layer/results.json`。

## 新旧对比

### R1-32B (L10 → L63)
| Metric | Old (L10) | New (L63) | Delta |
|---|---|---|---|
| bal_acc | 0.6707 | 0.5588 | **-0.1119** |
| precision | 0.5538 | 0.3891 | -0.1647 |
| pre_cp_fpr | 0.2423 | 0.4986 | +0.2563 |
| coverage | 0.4500 | 0.6000 | +0.1500 |
| lead_mean | 6.3 | 12.0 | +5.7 |

### QwQ-32B (L2 → L60)
| Metric | Old (L2) | New (L60) | Delta |
|---|---|---|---|
| bal_acc | 0.6661 | 0.7562 | **+0.0901** |
| precision | 0.4193 | 0.5118 | +0.0925 |
| pre_cp_fpr | 0.3997 | 0.3089 | -0.0908 |
| coverage | 0.7368 | 0.7368 | 0.0000 |
| lead_mean | 13.4 | 11.9 | -1.5 |

**总结**：
- **R1-32B 在 corrected layer (L63) 上 RepE 性能明显下降**：bal_acc 从 0.67 降到 0.56，pre_cp_fpr 几乎翻倍（0.24→0.50），说明最后一层的 mean-difference direction 对 safety commitment 区分力很弱。
- **QwQ-32B 在 corrected layer (L60) 上 RepE 性能反而提升**：bal_acc 从 0.67 升到 0.76，precision 从 0.42 升到 0.51，pre_cp_fpr 从 0.40 降到 0.31。

这进一步支持了论文的论点：简单的 unsupervised direction (RepE) 在同等层上仍然不如 supervised probe，尤其是 R1-32B 上差距更大。

---
