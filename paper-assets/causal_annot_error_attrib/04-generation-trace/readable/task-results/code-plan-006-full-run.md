# code plan 006 full run

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_006_full_run_20260521T012758_result.json`
- **Structured JSON:** [`3b576957358298a018a7.json`](../../sessions/3b/3b576957358298a018a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here's the summary for the Director's 5 focus areas:

---

## plan_006 全量分析结果 (30 configs × 7 topologies = 210 scenarios)

### 1. K 值对比

| K | Dataset | Mean Bias% | IV Bias% | ASV-unsafe |
|---|---------|-----------|---------|-----------|
| 2 | civil_comments | 36.9% | **116.5%** | 30.2% |
| 3 | vast | 65.3% | **252.3%** | 50.0% |
| 10 | humaid | 12.2% | **30.3%** | 49.2% |

**K=3 bias 最高**（不是 K=2 或 K=10），IV 在 K=3 下 bias 252%。Collider 在所有 K 下最稳健（4.9%-15.7%）。

### 2. F1 vs Bias Disconnect

- civil_comments (qwen2.5-7b): F1 = 0.717–0.746，**但 IV bias 101–131%、exposure bias 51–57%**
- humaid (llama4): F1 = 0.614–0.624，IV bias 40%
- 这验证了 "F1 高不代表因果估计安全" 的核心论点

### 3. 7B vs 235B

- vast: qwen2.5-7b (7B) mean bias **73.5%** vs 235B+ models **59.3%**（7B 更差）
- 7B diag_mean 0.453–0.473 vs 235B diag_mean 0.499–0.570（7B 准确率更低）
- civil_comments 只有 7B 有效数据（diag 0.717–0.749）

### 4. K=2 Sign Flip 验证

**0 sign flips across all K values (K=2, K=3, K=10)**。理论预测确认——column-stochastic C 在这些 DGP 下不产生符号翻转。

### 5. ASV 跨 K Unsafe 率

| K | Unsafe | 最安全 topology | 最危险 topology |
|---|--------|----------------|----------------|
| 2 | 30.2% | confounding/mbias (2/9) | 其余均 3/9 |
| 3 | 50.0% | **mbias (0/12)** | 其余均 7/12 |
| 10 | 49.2% | confounding/collider/mbias (0/9) | mediation/iv/frontdoor (8/9) |

**Overall ASV-unsafe: 92/210 (43.8%)**。mbias 在 K≥3 时始终安全，IV 在所有 K 下始终危险。

---

输出位置: `home-1x5090:/home/sonny/causal_annot_error_attrib/artifacts/plan006_full/`

---
