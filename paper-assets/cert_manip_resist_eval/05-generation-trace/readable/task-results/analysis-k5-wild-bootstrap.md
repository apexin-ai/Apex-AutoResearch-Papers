# analysis k5 wild bootstrap

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-wild-bootstrap_20260523T004308_result.json`
- **Structured JSON:** [`2262a54af011a4d1a6c2.json`](../../sessions/22/2262a54af011a4d1a6c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是 **Cross-K Comparison Table** 和论文 framing 分析：

---

## Cross-K Bootstrap Comparison (Wild Cluster Bootstrap, BH FDR α=0.05)

| Panel Size | Method | K_eff FDR sig | η_max FDR sig | K_eff direction |
|:-----------|:-------|:-------------|:-------------|:---------------|
| **K=3** | Bootstrap v2 (3-pos max-p) | **1/12** | **5/12** | 1+ / 0- |
| **K=5** | Bootstrap (5-pos max-p) | **7/12** | **0/12** | 7+ / 0- |

### K=5 vs K=3 对比（同一 method: wild cluster bootstrap）

| K=5 clustered SE → bootstrap deflation | K_eff | η_max |
|:---------------------------------------|:------|:------|
| Clustered SE | 10/12 | 7/12 |
| Wild cluster bootstrap | **7/12** | **0/12** |
| Deflation | 3 conditions lost | ALL 7 lost |

---

## 关键发现

1. **K_eff 从 K=3 的 1/12 升到 K=5 的 7/12** — panel size 增大后，judge diversity (K_eff) 成为主导因素，且全部为正向效应 (更高 diversity → 更高 ASR)

2. **η_max 从 K=3 的 5/12 降到 K=5 的 0/12** — individual vulnerability 在 5-position max-p bootstrap 下完全失去显著性。即使 raw max-p 很小（如 mmlu×verbosity_bias η max_p=0.0053），FDR 校正后仍不显著（fdr_p=0.0636）

3. **验证通过**：arc×sycophancy K_eff β = -0.1567（K=3 参考值 -0.192），方向一致（负），说明回归 spec 可靠

4. **5-position max-p 比 clustered SE 保守得多** — 这是 intentional 的。Clustered SE 给出 K_eff 10/12、η_max 7/12 可能有 over-rejection。Bootstrap 是更可靠的推断

## 论文 Framing 影响

结论必须是 **K-dependent**：
- K=3: η_max 主导（individual model vulnerability 是 panel ASR 的主要预测因子）
- K=5: K_eff 主导（judge diversity 反转为主要预测因子，individual vulnerability 不再显著）

这支持一个 **"diversity-vulnerability transition"** 的叙事：小 panel 下攻击成功主要取决于最弱 judge 的脆弱性；大 panel 下，judges 之间的有效独立性 (K_eff) 成为决定性因素。增加 panel 规模不仅降低 ASR，还改变了 ASR 的决定机制。

---
