# ops extract 9cell recall

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract_9cell_recall_20260515T230016_result.json`
- **Structured JSON:** [`49bcf2a2a96db6843413.json`](../../sessions/49/49bcf2a2a96db6843413.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部获取。JSON 中每个 cell 有 4 个 classifier（rf, lr, coral, diveye），顺序固定。以下是 9 cell 的 **RF per_class_recall**（源自 `all_results.json`）：

```
| Cell              | d0 recall | d1 recall | d2 recall | d3 recall |
|-------------------|-----------|-----------|-----------|-----------|
| pythia_nucleus    |      99.7 |      81.9 |      58.7 |      72.3 |
| pythia_temp09     |      99.7 |      81.3 |      53.9 |      72.1 |
| pythia_topk50     |      99.5 |      72.3 |      45.6 |      57.5 |
| olmo_nucleus      |      98.8 |      80.5 |      61.5 |      74.3 |
| olmo_temp09       |      99.7 |      87.7 |      66.1 |      77.2 |
| olmo_topk50       |      99.5 |      78.5 |      51.2 |      65.6 |
| gpt2xl_nucleus    |      99.2 |      85.9 |      73.3 |      77.5 |
| gpt2xl_temp09     |      99.5 |      90.9 |      68.8 |      81.9 |
| gpt2xl_topk50     |      98.5 |      79.5 |      52.5 |      71.1 |
```

**原始小数值（供核对）：**

| Cell | d0 | d1 | d2 | d3 |
|---|---|---|---|---|
| pythia_nucleus | 0.9973 | 0.8187 | 0.5867 | 0.7227 |
| pythia_temp09 | 0.9973 | 0.8133 | 0.5387 | 0.7213 |
| pythia_topk50 | 0.9947 | 0.7227 | 0.4560 | 0.5747 |
| olmo_nucleus | 0.9880 | 0.8053 | 0.6147 | 0.7427 |
| olmo_temp09 | 0.9973 | 0.8773 | 0.6613 | 0.7720 |
| olmo_topk50 | 0.9947 | 0.7853 | 0.5120 | 0.6560 |
| gpt2xl_nucleus | 0.9920 | 0.8587 | 0.7333 | 0.7747 |
| gpt2xl_temp09 | 0.9947 | 0.9093 | 0.6880 | 0.8187 |
| gpt2xl_topk50 | 0.9853 | 0.7947 | 0.5253 | 0.7107 |

**备注：**
- JSON 中 cell 名称是 `pythia_nucleus`（非 `pythia_nucleus095`），其余类推
- JSON 中 **无 per_class_precision 或 per_class_f1 字段**，只有 `per_class_recall` 和 `pairwise_auc`
- 每个 cell 还有 `acc_4class`、`acc_3class`、`mae` 指标，需要的话可以补充

---
