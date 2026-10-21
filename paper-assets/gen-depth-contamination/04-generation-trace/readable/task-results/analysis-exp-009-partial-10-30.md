# analysis exp 009 partial 10 30

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_009_partial_10_30_20260517T090630_result.json`
- **Structured JSON:** [`2bcbbb0106da6d76180a.json`](../../sessions/2b/2bcbbb0106da6d76180a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 文件完整性
- **ratio_10**: 15/15 ✓
- **ratio_30**: 15/15 ✓
- **ratio_50**: 14/15 (进程运行中，PID 4409，快完成了)

---

### Table 1: Mean±Std

| Ratio | Strategy | MMLU | HellaSwag |
|-------|----------|------|-----------|
| 10% | no_filter | 0.6058±0.0002 | 0.6689±0.0007 |
| 10% | binary_ours | 0.6079±0.0005 | 0.6727±0.0008 |
| 10% | graduated | 0.6066±0.0011 | 0.6700±0.0015 |
| 30% | no_filter | 0.6069±0.0007 | 0.6664±0.0020 |
| 30% | binary_ours | 0.6082±0.0012 | 0.6725±0.0007 |
| 30% | graduated | 0.6072±0.0008 | 0.6665±0.0014 |

---

### Table 2: Paired t-tests

| Ratio | Comparison | ΔMMLU | p(MMLU) | ΔHellaSwag | p(HellaSwag) |
|-------|-----------|-------|---------|------------|--------------|
| 10% | binary vs no_filter | +0.0021 | **0.0010** | +0.0038 | **0.0017** |
| 10% | graduated vs binary | -0.0014 | 0.0917 | -0.0027 | *0.0399* |
| 10% | graduated vs no_filter | +0.0008 | 0.2706 | +0.0011 | 0.0611 |
| 30% | binary vs no_filter | +0.0013 | 0.0739 | +0.0061 | **0.0036** |
| 30% | graduated vs binary | -0.0010 | 0.3018 | -0.0060 | **0.0009** |
| 30% | graduated vs no_filter | +0.0003 | 0.6638 | +0.0002 | 0.6646 |

---

### Table 3: Raw Data (30 data points)

| Ratio | Strategy | Seed | MMLU | HellaSwag |
|-------|----------|------|------|-----------|
| 10% | no_filter | 0 | 0.6060 | 0.6680 |
| 10% | no_filter | 1 | 0.6059 | 0.6688 |
| 10% | no_filter | 2 | 0.6055 | 0.6686 |
| 10% | no_filter | 3 | 0.6056 | 0.6695 |
| 10% | no_filter | 4 | 0.6060 | 0.6696 |
| 10% | binary_ours | 0 | 0.6085 | 0.6733 |
| 10% | binary_ours | 1 | 0.6073 | 0.6717 |
| 10% | binary_ours | 2 | 0.6083 | 0.6731 |
| 10% | binary_ours | 3 | 0.6077 | 0.6734 |
| 10% | binary_ours | 4 | 0.6077 | 0.6721 |
| 10% | graduated | 0 | 0.6048 | 0.6675 |
| 10% | graduated | 1 | 0.6067 | 0.6708 |
| 10% | graduated | 2 | 0.6078 | 0.6697 |
| 10% | graduated | 3 | 0.6072 | 0.6713 |
| 10% | graduated | 4 | 0.6062 | 0.6709 |
| 30% | no_filter | 0 | 0.6058 | 0.6673 |
| 30% | no_filter | 1 | 0.6077 | 0.6671 |
| 30% | no_filter | 2 | 0.6070 | 0.6649 |
| 30% | no_filter | 3 | 0.6068 | 0.6687 |
| 30% | no_filter | 4 | 0.6072 | 0.6638 |
| 30% | binary_ours | 0 | 0.6085 | 0.6727 |
| 30% | binary_ours | 1 | 0.6097 | 0.6722 |
| 30% | binary_ours | 2 | 0.6074 | 0.6717 |
| 30% | binary_ours | 3 | 0.6065 | 0.6725 |
| 30% | binary_ours | 4 | 0.6090 | 0.6735 |
| 30% | graduated | 0 | 0.6079 | 0.6667 |
| 30% | graduated | 1 | 0.6068 | 0.6673 |
| 30% | graduated | 2 | 0.6078 | 0.6650 |
| 30% | graduated | 3 | 0.6076 | 0.6683 |
| 30% | graduated | 4 | 0.6059 | 0.6654 |

---

### 关键发现

1. **binary_ours 在两个 ratio 下都是最佳策略**，尤其在 HellaSwag 上优势显著（10%: +0.38pp, p=0.0017; 30%: +0.61pp, p=0.0036）
2. **graduated 表现不如 binary_ours**，在 30% HellaSwag 上甚至显著更差（-0.60pp, p=0.0009）
3. graduated 与 no_filter 无显著差异，说明 graduated 策略在这两个 ratio 下基本无效

结果已保存到 `/root/autodl-tmp/gen-depth-contamination/artifacts/exp009_v3_partial_10_30.json`。

---
