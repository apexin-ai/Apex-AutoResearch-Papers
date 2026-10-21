# ops baselines discrepancy audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_baselines-discrepancy-audit_20260516T173659_result.json`
- **Structured JSON:** [`24b58ee3565cfa53bb8b.json`](../../sessions/24/24b58ee3565cfa53bb8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 差异根因总结

两个文件由**不同脚本**产生，存在 **4 处实质性差异**：

| 维度 | unfiltered（权威） | baselines（新 Worker） |
|------|-------------------|----------------------|
| 脚本 | `fix_tail_decay_and_eval.py` | `eval_8gen_logo_baselines.py` |
| 数据量 | **37,058 行**（全量） | **34,131 行**（inner join 丢 llama 1743 行、mistral 1184 行） |
| 训练采样 | **无 downsample** | **有 downsample**（类别平衡） |
| F1 聚合 | **Pooled** macro F1（所有 fold 预测拼接→一次 F1） | **Per-gen 平均**（8 个 F1 取均值） |
| 随机种子 | 42 | 789 |

**影响最大的两个因素**：
1. **F1 聚合方式** — pooled 和 per-gen average 是不同指标，数学上不可等价；pooled 会被大 generator（数据多的）主导
2. **Inner join 丢数据** — baselines 因需要 detector scores 做 inner join，llama/mistral 各丢约 37%/24% 的行，而这两个 generator 恰恰表现最差，导致 per-gen 平均被进一步拉低

README 已写入 `/root/gen-depth-fingerprint/results/README.md`。

---
