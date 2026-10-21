# code coverage bias selectivity gru seed

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_coverage_bias_selectivity_gru_seed_20260517T131645_result.json`
- **Structured JSON:** [`8b022e1a18bd6dada08f.json`](../../sessions/8b/8b022e1a18bd6dada08f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项任务全部完成。

---

## 结果汇总

### Task A: Coverage/排除偏差分析

| Model | Total | Included | Excluded | Rate | Flag |
|-------|-------|----------|----------|------|------|
| r1_8b | 268 | 209 | 59 | 22.0% | HIGH |
| r1_32b | 100 | 100 | 0 | 0.0% | LOW |
| qwq_32b | 95 | 95 | 0 | 0.0% | LOW |

r1_8b 排除的 59 条 traces 全部是 jailbreak 且无任何 safety label（模型直接生成有害内容，没有安全推理阶段）。排除 traces 显著更短（mean 38.0 vs 46.3, Mann-Whitney p=0.0001）。排除是任务定义的固有限制（无 commitment point 可标注），非采样偏差。

### Task B: R1-32B Layer 10 Selectivity CI

| Metric | Value |
|--------|-------|
| Real accuracy | 0.7077 |
| Random mean | 0.5511 |
| Selectivity | **15.7pp** |
| Bootstrap mean | 15.9pp |
| Bootstrap std | 3.1pp |
| 95% CI | **[9.7, 21.9]pp** |
| p-value | **< 0.001** |

Layer 10 selectivity 显著 > 0。注意：使用 static features + PCA(128)，结果为 15.7pp 而非预期的 7.5pp，可能因特征类型（static vs temporal）或 PCA 配置不同。

### Task C: GRU Per-Seed 70/30

| Seed | bal_acc | crossing | lead | fpr |
|------|---------|----------|------|-----|
| 42 | 0.796 | 0.714 | 2.96 | 0.143 |
| 123 | 0.743 | 0.778 | 11.16 | 0.311 |
| 456 | 0.729 | 0.508 | 9.03 | 0.179 |
| 789 | 0.833 | 0.683 | 7.65 | 0.187 |
| 1024 | 0.758 | 0.873 | 10.09 | 0.328 |
| **mean±std** | **0.772±0.038** | **0.711±0.121** | **8.2±2.9** | **0.229±0.075** |

对比原 single-seed (bal_acc=0.839, cross=0.721, lead=3.5)：bal_acc 多 seed 均值降低约 6.7pp，方差较小(std=0.038)；crossing_rate 稳定；lead_mean 方差大(std=2.9)，说明 lead time 对数据划分敏感。

---
