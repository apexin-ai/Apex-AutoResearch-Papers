# analysis check sensitivity after restart

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_sensitivity_after_restart_20260523T033922_result.json`
- **Structured JSON:** [`8b61fc34aae158c2805d.json`](../../sessions/8b/8b61fc34aae158c2805d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 100754 已结束，脚本正常跑完 128/128 配置，耗时 11912s (~3.3h)。结果已复制到本地。

## 结果汇总

| | Threshold ≥1 | Threshold ≥2 | Threshold ≥3 |
|---|---|---|---|
| **JB / Safe** | 159 / 361 | 304 / 216 | 453 / 67 |
| **JB Rate** | 30.6% | 58.5% | 87.1% |
| **CR-composite best** | L2 (6.5%) | L0 (0.0%) | L8 (25.8%) |
| **Precision best** | L12 (38.7%), 0.725 | L5 (16.1%), 0.892 | L12 (38.7%), 0.972 |
| **Divergence** | **32.2pp** | **16.1pp** | **12.9pp** |
| **Replicated (>15pp)** | **Yes** | **Yes** | **No** (12.9pp) |

关键发现：
- **≥1 和 ≥2 均 replicate**（divergence 32.2pp / 16.1pp，均 >15pp 阈值）
- **≥3 未达标**（12.9pp < 15pp），但这在预期内——87.1% JB rate 下 safe 样本仅 67 个，class imbalance 极端
- Precision best layer 在 ≥3 条件下达到 0.972（L12），说明即使极端 imbalance 下分类器仍能找到高精度层
- CR-composite 在不同 threshold 下选出的层差异大（L2 → L0 → L8），说明该指标对 label 分布敏感

---
