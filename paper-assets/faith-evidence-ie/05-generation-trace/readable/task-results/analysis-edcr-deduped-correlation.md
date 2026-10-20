# analysis edcr deduped correlation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_edcr_deduped_correlation_20260518T073429_result.json`
- **Structured JSON:** [`51bc3be30109dbfc6452.json`](../../sessions/51/51bc3be30109dbfc6452.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下。

## 1. 六个独立数据点（DPO 3ep 无 eval 数据）

| Method | Rel-F1 | Evi-F1 | EDCR |
|--------|--------|--------|------|
| SFT baseline | 0.4049 | 0.7986 | 0.6982 |
| RSFT CED (4-seed mean) | 0.4563 | 0.8115 | 0.6503 |
| RSFT flat-NLI (2-seed mean) | 0.4561 | 0.8076 | 0.6505 |
| GRPO QLoRA (kl001 ckpt-100) | 0.2167 | 0.5746 | 0.8539 |
| GRPO bf16 G=8 (ckpt-100) | 0.4549 | 0.8086 | 0.6318 |
| DPO 1ep (fixed) | 0.4034 | 0.8088 | 0.7139 |

## 2. 去重 Spearman 相关性

| Subset | EDCR vs Rel-F1 | p-value | EDCR vs Evi-F1 | p-value |
|--------|---------------|---------|----------------|---------|
| **Full (n=6)** | **ρ = -0.8286** | **0.042** | ρ = -0.5429 | 0.266 |
| No QLoRA (n=5) | ρ = -0.7000 | 0.188 | ρ = -0.2000 | 0.747 |
| No DPO (n=5) | ρ = -0.7000 | 0.188 | ρ = -0.9000 | 0.037 |
| No QLoRA, no DPO (n=4) | ρ = -0.4000 | 0.600 | ρ = -0.8000 | 0.200 |

替代指标：
| Subset | (Evi-F1 − Rel-F1) vs Rel-F1 | p | Evi-F1 vs Rel-F1 | p |
|--------|------------------------------|---|-------------------|---|
| Full (n=6) | ρ = -0.6571 | 0.156 | ρ = 0.6000 | 0.208 |

## 3. Per-relation EDCR 分析 (n=76 relation types, RSFT-CED s44)

| Metric Pair | ρ | p-value | n |
|-------------|---|---------|---|
| **EDCR vs Rel-F1** | **-0.7927** | **< 0.0001** | 76 |
| EDCR vs Evi-F1 | -0.0640 | 0.583 | 76 |
| Evi-F1 vs Rel-F1 | -0.0125 | 0.914 | 76 |
| **Filtered (tp>0, n_pred≥5):** | | | |
| EDCR vs Rel-F1 | **-0.8482** | **< 0.0001** | 74 |
| EDCR vs Evi-F1 | -0.0494 | 0.676 | 74 |

## 4. 结论

**Cross-method (n=6)**: 去重后 EDCR vs Rel-F1 仍显著（ρ = -0.83, p = 0.042），但移除任一异常点后 n 太小失去统计显著性。GRPO QLoRA 是 leverage point（极低 Rel-F1 + 极高 EDCR）。

**Per-relation (n=76) 是最强证据**: EDCR 与 Rel-F1 强负相关（ρ = -0.79, p ≈ 0），但与 Evi-F1 几乎无关（ρ = -0.06, p = 0.58）。这证明 EDCR 捕获了 Evi-F1 正交的信息。

**论文论证策略建议**: cross-method 去重分析报 ρ = -0.83 (p = 0.042, n=6) 作为方向性证据，per-relation 分析报 ρ = -0.79 (p < 0.0001, n=76) 作为核心统计支撑。DPO 3ep 缺少 eval 数据，如需凑齐 7 点需要补跑。

---
