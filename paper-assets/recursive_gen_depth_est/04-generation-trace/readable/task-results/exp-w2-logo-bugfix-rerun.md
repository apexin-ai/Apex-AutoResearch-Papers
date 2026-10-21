# exp w2 logo bugfix rerun

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_w2_logo_bugfix_rerun_20260515T200026_result.json`
- **Structured JSON:** [`a8da8482f32bc8c72f89.json`](../../sessions/a8/a8da8482f32bc8c72f89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总报告：

---

## 修复前后对比

### Group 分布
- **修复前**：Group 0-2 = 纯 d1, Group 7-9 = 纯 d3（depth 与 group 完全相关）
- **修复后**：每个 Group 每个 depth 各 500 样本（完全 balanced）

### Sub-B LOGO (block-stratified 10-fold CV)

| Cell | Mean Acc | Std | Range |
|------|---------|-----|-------|
| pythia_nucleus095 | 72.2% | 1.3% | 69.5-74.7% |
| pythia_temp09 | 69.6% | 1.4% | 67.3-71.7% |
| pythia_topk50 | 59.5% | 0.9% | 58.1-60.5% |
| gpt2xl_nucleus095 | 79.9% | 1.2% | 78.2-82.1% |
| gpt2xl_temp09 | 81.6% | 0.8% | 80.3-83.0% |
| gpt2xl_topk50 | 68.7% | 1.1% | 66.9-70.4% |
| olmo_nucleus095 | 73.9% | 0.4% | 73.0-74.6% |
| olmo_temp09 | 76.5% | 1.2% | 74.5-78.8% |
| olmo_topk50 | 66.6% | 0.9% | 65.6-68.3% |
| **MEAN** | **72.1%** | | |

- **旧值**：mean 64%, range 46.6%-76.7%（30pp 跨度）
- **新值**：mean 72.1%, fold 内 range 仅 ~2-5pp
- **变化**：mean +8.1pp，fold variance 大幅下降（因为旧 fold 中 test set depth 极度不均衡）

### Sub-C Negative Control

| 指标 | 旧值 | 新值 |
|------|------|------|
| Depth prediction (mean) | 72.0% | 72.0% |
| Seed group prediction (mean) | **20.8%** | **10.2%** |
| Chance level | 10.0% | 10.0% |
| Depth/SeedGrp ratio | 3.46x | **7.06x** |

- seed_group prediction 从 20.8% 降到 10.2%（**本质上等于 chance level 10%**），确认 groups 不再携带 depth 信息

### 结论
修复有效。旧的 seed_group 可预测性（20.8%）完全是 bug 造成的 depth 泄露，修复后降至 chance。Sub-B LOGO accuracy 上升 8pp 是因为旧的 fold 划分导致某些 fold 测试集缺少某些 depth，现在每个 fold 的 depth 均衡后分类性能更真实。

---
