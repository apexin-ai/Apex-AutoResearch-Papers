# ssh pertype fewnerd analysis

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_pertype_fewnerd_analysis_20260521T194724_result.json`
- **Structured JSON:** [`319943907db5855db6ad.json`](../../sessions/31/319943907db5855db6ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 seed 全部完成。汇总结果：

## Per-Type MV 分析结果 (FewNERD finetuned, N=8, strict>4)

### Seed 42 / 123 / 456 平均

| Type | N | Greedy F1 | MV F1 | MV Δ | Oracle F1 |
|------|---|-----------|-------|------|-----------|
| person | ~7200 | 0.820 | 0.772 | **-0.04** | 0.911 |
| location | ~8800 | 0.797 | 0.740 | -0.06 | 0.896 |
| art | ~1250 | 0.755 | 0.703 | -0.05 | 0.845 |
| organization | ~6700 | 0.725 | 0.633 | -0.09 | 0.853 |
| building | ~1540 | 0.696 | 0.597 | -0.10 | 0.839 |
| product | ~2260 | 0.657 | 0.549 | -0.11 | 0.810 |
| event | ~1315 | 0.645 | 0.544 | -0.10 | 0.806 |
| other | ~3485 | 0.639 | 0.506 | **-0.13** | 0.857 |

### Correlation(greedy_f1, MV_delta)

| Seed | Unweighted r | Weighted r |
|------|-------------|------------|
| 42 | +0.878 | +0.938 |
| 123 | +0.896 | +0.949 |
| 456 | +0.920 | +0.910 |

### 结论

**相关性是强正值（~0.90），不是负值。** 这意味着：

- **High-F1 types (person, location) MV 损失最小**（Δ ≈ -0.04 ~ -0.06）
- **Low-F1 types (other, product, event) MV 损失最大**（Δ ≈ -0.10 ~ -0.17）

这与 "high-F1 type 的 MV 更差" 假设**相反**。MV 的伤害集中在本身就难的 entity type 上——低 baseline quality 的 type，模型 sample 间一致性也更差，strict MV 的高阈值过滤掉了更多正确 entity。

不存在 "high-F1 type 的 MV confound" 问题。真正的 pattern 是：**harder types → lower agreement → bigger MV penalty**。

---
