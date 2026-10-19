# analysis excluded traces

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_excluded_traces_20260517T044124_result.json`
- **Structured JSON:** [`6d13419d0caf44c6fa5d.json`](../../sessions/6d/6d13419d0caf44c6fa5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

---

## Excluded Traces Analysis (r1_8b, W=15, layer=2)
**10 excluded / 33 included from 43 test traces**

### 排除原因

| 原因 | 数量 |
|------|------|
| 仅 Text probe 无正预测 | 7 |
| 仅 HS probe 无正预测 | 2 |
| 两者均无正预测 | 1 |

主要由 Text probe 的 recall 不足导致（7/10），而非 HS probe 问题。

### 统计比较

| 特征 | Excluded (n=10) | Included (n=33) | Mann-Whitney p |
|------|----------------|-----------------|----------------|
| Trace 长度 (steps) | mean=51.2, median=46.5 | mean=43.9, median=44.0 | p=0.274 |
| CP 绝对位置 | mean=39.8, median=42.0 | mean=32.5, median=33.0 | p=0.262 |
| CP 相对位置 (0-1) | mean=0.729, median=0.853 | mean=0.688, median=0.829 | p=0.350 |
| 正标签比例 | mean=0.271, median=0.147 | mean=0.312, median=0.171 | p=0.350 |

所有标签分布：excluded 和 included 中均无 all-zero 标签的 trace（Fisher p=1.0）。

### 结论

**未检测到系统性偏差。** 所有统计检验均不显著（最低 p=0.262）。排除是纯机制性的（probe 未产生正预测），不与 trace 长度、CP 位置或正标签比例系统性关联。

值得注意的是，excluded traces 的正标签比例 *偏低*（mean 0.271 vs 0.312），但差异不显著。这可以解释为：正标签少 → 正类信号弱 → probe 更倾向全预测为负。

输出已保存至 `artifacts/acc_precision_bootstrap/excluded_traces_analysis.txt`。

---
