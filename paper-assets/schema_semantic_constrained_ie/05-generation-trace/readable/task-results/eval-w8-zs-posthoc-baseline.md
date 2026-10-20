# eval w8 zs posthoc baseline

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_w8_zs_posthoc_baseline_20260516T071609_result.json`
- **Structured JSON:** [`884101d013492d948c62.json`](../../sessions/88/884101d013492d948c62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 5 组数据已收集完毕。汇总如下：

---

## 零样本 Post-hoc Filtering 汇总表

| Model | Dataset | Triples | Reject% | R_F1_before | R_F1_posthoc | R_F1_constrained | TP_before | TP_after | TP_lost | R_recall_before | R_recall_after | Recall_drop |
|-------|---------|---------|---------|-------------|-------------|------------------|-----------|----------|---------|-----------------|----------------|-------------|
| Mistral-7B | SciERC | 1584 | **20.27%** | 0.0376 | 0.0394 | 0.0367 | 48 | 44 | 4 | 4.93% | 4.52% | -0.41pp (−8.3%) |
| Qwen3-8B | SciERC | 1724 | **16.76%** | 0.0823 | 0.0863 | 0.0836 | 111 | 104 | 7 | 11.40% | 10.68% | -0.72pp (−6.3%) |
| Llama-3.1-8B | SciERC | 1274 | **13.89%** | 0.0268 | 0.0271 | 0.0254 | 30 | 28 | 2 | 3.10% | 2.90% | -0.20pp (−6.5%) |
| Qwen3-8B | DocRED | 17497 | **48.12%** | 0.0774 | 0.0961 | 0.0823 | 1137 | 1010 | 127 | 9.46% | 8.40% | -1.06pp (−11.2%) |
| Llama-3.1-8B | DocRED | 16437 | **42.18%** | 0.0598 | 0.0744 | 0.0627 | 850 | 802 | 48 | 7.00% | 6.60% | -0.40pp (−5.7%) |

### Rejection 细分

| Model | Dataset | RV (relation vocab) | ET (entity type) | DR (domain/range) | Total |
|-------|---------|---------------------|------------------|--------------------|-------|
| Mistral-7B | SciERC | 27 | 103 | 191 | 321 |
| Qwen3-8B | SciERC | 24 | 14 | 251 | 289 |
| Llama-3.1-8B | SciERC | 7 | 0 | 170 | 177 |
| Qwen3-8B | DocRED | 5189 | 692 | 2538 | 8419 |
| Llama-3.1-8B | DocRED | 2635 | 13 | 4285 | 6933 |

---

## 关键发现（与预期叙事不同）

**意外结果：零样本下 post-hoc 的 R_F1 在所有 5 组中都 ≥ constrained decoding。**

- Post-hoc 通过删除 FP 提升 precision，recall 损失有限（TP_lost 占总 rejected triples 的 1-2%）
- Constrained decoding 在 ZS 下反而降低了 R_F1，因为强制约束干扰了模型的自然生成分布，导致整体质量下降

**ZS rejection rate vs FT rejection rate 对比**：
- ZS rejection: 14%–48%（远高于 FT 的 <3%）
- DocRED 尤其严重：模型生成大量无效 relation 名称（RV 占 rejection 主体）

**Recall 损失**：
- 绝对值: 0.2pp–1.06pp
- 相对值: 5.7%–11.2%
- DocRED Qwen3 最严重：127 个 TP 被误删

**论文论述需要调整**：数据表明 ZS 下 constrained decoding 的价值不在于"保留 TP"（post-hoc 也保留了大部分），而在于别的维度（如输出格式规范性、downstream usability）。或者反过来——这个数据支持的结论是 post-hoc 在 ZS 下是更优策略。

---
