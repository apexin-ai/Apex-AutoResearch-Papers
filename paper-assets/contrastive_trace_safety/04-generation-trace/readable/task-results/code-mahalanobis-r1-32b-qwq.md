# code mahalanobis r1 32b qwq

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mahalanobis_r1_32b_qwq_20260517T145609_result.json`
- **Structured JSON:** [`414522e61420fedab125.json`](../../sessions/41/414522e61420fedab125.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总:

## 4-Model Mahalanobis Comparison

| Model | Layer | safe_MD | post_MD | separation | Best PCA |
|-------|-------|---------|---------|------------|----------|
| R1-8B | L28 | 6.66 | 6.73 | 0.07 | (prev) |
| OT-7B | L16 | 7.68 | 7.71 | 0.03 | (prev) |
| R1-32B | L63 | 6.73 | 6.88 | 0.15 | pca_64 |
| QwQ-32B | L60 | 3.22 | 3.42 | 0.20 | pca_16 |

所有 4 个模型 separation 均 < 0.21，Mahalanobis distance 无判别力。即使 crossing rate 最高的配置（R1-32B: 0.65, QwQ: 0.58），对应的 false alarm rate 也极高（0.45, 0.42），几乎等同于随机检测。

**结论: 4/4 模型 Mahalanobis 均失败。** 结果已保存至:
- `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mahalanobis_r1_32b/results.json`
- `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mahalanobis_qwq/results.json`

---
