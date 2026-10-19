# analysis gru per seed data

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gru_per_seed_data_20260517T050103_result.json`
- **Structured JSON:** [`9faa823f1d2a5a1e2394.json`](../../sessions/9f/9faa823f1d2a5a1e2394.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Per-seed 数据已提取，LaTeX table 已生成。

**结果摘要：**

| Model | Acc | Prec | FPR | Cross.% | Lead |
|-------|-----|------|-----|---------|------|
| GRU-single | 0.799±0.035 | 0.528±0.091 | 0.178±0.028 | 68.2±2.9% | 6.46±2.10 |
| GRU-multi | 0.789±0.027 | 0.510±0.075 | 0.189±0.018 | 68.2±4.4% | **7.01±1.40** |
| LR-single | 0.803±0.037 | 0.547±0.108 | 0.141±0.035 | 47.3±4.8% | 2.40±3.16 |
| LR-multi | 0.800±0.032 | 0.547±0.099 | 0.134±0.036 | 40.3±4.8% | 4.12±2.55 |

**关键发现：**
- GRU 的 crossing rate (68%) 显著高于 LR (40-47%)，说明 GRU 更频繁地触发早期检测
- GRU-multi 的 lead time 最高 (7.01 steps)，且方差最小 (±1.40)，表明多层信息提升了稳定性
- GRU 以更高 FPR 为代价换取了更早的检测（precision-lead tradeoff）
- Seed 间变异性：accuracy 在 ±3.5% 范围内，lead time 变异较大（LR-single 标准差达 3.16）

**产出文件：**
- 服务器端 JSON: `artifacts/diagnostics/gru256_per_seed_results.json`
- LaTeX table: `artifacts/exp_gru256_multilayer/per_seed_table.tex`

---
