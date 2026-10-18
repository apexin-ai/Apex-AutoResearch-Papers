# ops a6 direct read

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_a6-direct-read_20260524T125134_result.json`
- **Structured JSON:** [`3441afd004472982e961.json`](../../sessions/34/3441afd004472982e961.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A6 结果文件已存在，运行耗时 2175.2 秒（~36 分钟）。关键结果：

### predictor_shift（Shannon MI entropy 作为 DBEI 多样性指标）

| K | diversity_sig | eta_sig |
|---|--------------|---------|
| 3 | **4/12** | **12/12** |
| 5 | **4/12** | **11/12** |
| 7 | **0/12** | **0/12** |

### keff_comparison（DBEI vs k_eff 对比）

| K | keff_sig | diversity_sig |
|---|----------|--------------|
| 3 | 6/12 | 4/12 |
| 5 | **8/12** | 4/12 |
| 7 | 2/12 | 0/12 |

### correlation_dbei_keff
- K3: **-0.625**, K5: **-0.735**, K7: **-0.759**

`shift_pattern_matches_keff`: **false**

### K7 FDR summary
- shannon_fdr_sig: 0/12, keff_fdr_sig: 2/12, eta_in_shannon: 0/12, eta_in_keff: 1/12

**核心发现**：
1. **η（操纵强度）在 K3/K5 几乎全显著**（12/12, 11/12），但 DBEI diversity 本身只有 4/12 显著——说明操纵强度是主要预测因子，面板多样性的独立解释力有限
2. **K7 全面崩塌**（0/12）——面板过大时信号完全消失
3. **DBEI 与 k_eff 强负相关**（-0.63 ~ -0.76），但显著性 pattern 不匹配——k_eff 在 K5 有 8/12 显著，优于 DBEI 的 4/12
4. k_eff 整体表现略优于 Shannon MI entropy 作为多样性度量

---
