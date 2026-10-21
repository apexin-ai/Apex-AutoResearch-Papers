# analysis sub b logo fix

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sub-b-logo-fix_20260516T011436_result.json`
- **Structured JSON:** [`b2dec8b5de8bbb717974.json`](../../sessions/b2/b2dec8b5de8bbb717974.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告：W2 Domain Bias LOGO Bug 修复 (RR3-W4)

### 修复内容

**v1 的 `get_seed_ids()` 用 per-depth 顺序编号（`np.arange(mask.sum())`）推断 seed article ID。** 经验证，数据文件内 seed_id 确实是 0-4999 顺序排列，所以 v1 结果碰巧正确。但此依赖行顺序的假设不够健壮。

**v2 修复：** 直接从 raw `depth_*.jsonl` 文件读取实际 `seed_id` 字段，并加入验证（train/test 无 seed 泄露、groups 深度均衡）。脚本路径：`src/w2_domain_bias_v2.py`

### Sub-B 结果（LOGO vs Standard CV）

| Cell | LOGO | Std CV | Drop | Min Fold | Max Fold |
|------|------|--------|------|----------|----------|
| pythia_nucleus095 | 72.2% | 72.2% | +0.05pp | 69.5% | 74.7% |
| pythia_temp09 | 69.6% | 69.5% | -0.16pp | 67.3% | 71.7% |
| pythia_topk50 | 59.5% | 59.1% | -0.35pp | 58.1% | 60.5% |
| gpt2xl_nucleus095 | 79.9% | 80.0% | +0.06pp | 78.2% | 82.1% |
| gpt2xl_temp09 | 81.6% | 81.8% | +0.18pp | 80.3% | 83.0% |
| gpt2xl_topk50 | 68.7% | 68.4% | -0.37pp | 66.9% | 70.4% |
| olmo_nucleus095 | 73.9% | 73.6% | -0.31pp | 73.0% | 74.6% |
| olmo_temp09 | 76.5% | 76.7% | +0.25pp | 74.5% | 78.8% |
| olmo_topk50 | 66.6% | 66.6% | -0.07pp | 65.6% | 68.3% |
| **MEAN** | **72.1%** | **72.0%** | **-0.08pp** | **58.1%** | |

**结论：LOGO accuracy 与 standard CV 几乎无差异（mean drop = -0.08pp），确认 depth signal 不是 seed article domain artifact。** v1 的数字与 v2 一致，说明 v1 的 `get_seed_ids()` 顺序编号碰巧映射正确。

### Sub-C（负对照）

| Cell | Depth Pred | Seed Group Pred | Chance | Ratio |
|------|-----------|-----------------|--------|-------|
| Mean | 72.0% | 10.2% | 10.0% | 7.1x |

Seed group 预测精度在 chance level（10%），depth 预测远超 chance（72%），确认特征编码的是递归深度而非 seed article 信息。

### Sub-A 注意事项

`per_class_recall` 是 **train-set memorization**（`rf_full.predict(X)` on training data），所有值 99.9-100%。如果论文 appendix 引用了 Sub-A 的 per_class_recall 作为分类性能指标，需标注这是训练集指标而非泛化指标。CV accuracy（59-82%）才是正确的泛化精度。

### "8pp drop 和 22.9% min" 说明

当前数据中不存在这些数字。v1 和 v2 的 LOGO drop 均为 ~0pp，最低 fold accuracy 为 58.1%。如果论文中报告了 8pp drop / 22.9% min，这些数字可能来自更早的（未保存的）错误版本，需要更新为此次重跑的结果。

---
