# fix fewnerd r value deep investigation

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_fewnerd_r_value_deep_investigation_20260516T061932_result.json`
- **Structured JSON:** [`8fe40733741a661cccb4.json`](../../sessions/8f/8fe40733741a661cccb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Line 148's "$p < 10^{-10}$" for MAVEN is conservatively correct (actual p is 7e-42). No change needed there.

---

## 根因分析

三个 r 值来自**同一组 1953 type pairs**的**同一份 confusion matrix** (predictions_exp2.json)，差异的唯一根因是 **Y 变量定义**：

| 分析 | Y 变量 | 嵌入来源 | r | 来源 |
|------|--------|----------|---|------|
| bootstrap_ci.py | confusion **rate** = (c_ij+c_ji)/(gold_i+gold_j) | type_embeddings.pt | **0.112** | 论文 Table 2 |
| cross_embedding_sensitivity.py | raw confusion **count** = c_ij+c_ji | sim_matrix.pt | **0.138** | 附录分析 |
| "exp002 原始 r=0.156" | **不是点估计** — 是 r=0.112 的 naive bootstrap CI 上界 [0.076, **0.156**] | — | — | CI 上界 |

验证：
- case-sensitive vs case-insensitive 对结果**无影响**（两者产生相同的 859 confusion events）
- sim_matrix.pt vs type_embeddings.pt 差异极小（max diff=0.004，对 r 影响 <0.001）
- count_filter（count_6/count_12）未参与——三个分析都聚合了所有 count 条件

**根因总结**：rate 归一化消除了 gold frequency 的混淆效应（高频类型天然有更多 confusion events），降低了 r；raw count 未消除此效应，r 更高。r=0.156 是 CI 边界，非独立分析结果。

## 推荐论文值

**r = 0.112（confusion rate）**，原因：
1. 论文方法节明确定义 "confusion rate—the fraction of t_i gold instances misclassified as t_j"
2. rate 控制了 gold frequency 混淆
3. 更保守（下界），不会被 reviewer 质疑为 inflation

## 已做修改

文件：`docs/paper/results.tex`

| 位置 | 原值 | 新值 | 原因 |
|------|------|------|------|
| L57 p-value | $<10^{-12}$ | $7{\times}10^{-7}$ | 原值是 Spearman p，非 Pearson p |
| L58 p-value | $<10^{-10}$ | $7{\times}10^{-42}$ | 使用实际 Pearson p |
| Caption | 无计算说明 | 添加 confusion rate 定义、聚合方式、bootstrap 参数 | 让读者可复现 |
| Caption p-threshold | $p < 10^{-10}$ | $p \ll 0.001$ | 与修正后的 Few-NERD p 值一致 |

---
