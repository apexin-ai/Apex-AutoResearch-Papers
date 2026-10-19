# code bocpd ot7b w3

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bocpd_ot7b_w3_20260517T131605_result.json`
- **Structured JSON:** [`8a3ca6059767900d4112.json`](../../sessions/8a/8a3ca6059767900d4112.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

## OT-7B BOCPD/CUSUM (W=3, Layer 16, n_test=47)

| Method | Det Rate | Mean Lead | Med Lead |
|--------|----------|-----------|----------|
| **FCP t=0.5 k=2** | **89.4%** | **11.83** | **10.5** |
| FCP t=0.5 k=3 | 74.5% | 8.71 | 7.0 |
| FCP t=0.3 k=3 | 78.7% | 11.92 | 10.0 |
| CUSUM t=0.2 h=2 | 74.5% | 7.46 | 6.0 |
| CUSUM t=0.3 h=2 | 70.2% | 6.03 | 5.0 |
| FCP t=0.5 k=5 | 46.8% | 5.09 | 4.5 |
| **BOCPD (all λ)** | **0.0%** | — | — |

## 关键发现

**BOCPD 在 OT-7B 上完全失败**（所有 lambda 值检测率 0%），原因：
- W=3 的 probe scores 极度 spiky（在 1-2 步内从 0 跳到 1）
- BOCPD 的 Gaussian 模型假设均值渐变，run-length posterior R[0] 永远不超过 hazard rate (1/λ)

## 与 R1-8B 对比

| | R1-8B | OT-7B |
|--|-------|-------|
| BOCPD λ=10 det | 93.0% | **0%** |
| FCP det (t=0.5 k=5) | 65.1% | 46.8% |
| FCP det (t=0.5 k=2) | — | 89.4% |
| FCP mean lead | 4.89 | 11.83 |

**结论：commitment dynamics 是 model-specific 的** — R1-8B 渐进式（BOCPD 有效），OT-7B 突变式（简单阈值最优）。这强化了论文叙事：不同模型的 commitment pattern 不同，需要自适应检测策略。

结果 JSON 保存在服务器 `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_bocpd_ot7b_w3/results.json`。

---
