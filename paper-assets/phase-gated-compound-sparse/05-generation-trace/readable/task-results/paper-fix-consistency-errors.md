# paper fix consistency errors

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-consistency-errors_20260514T114426_result.json`
- **Structured JSON:** [`c98ca13127783c21035b.json`](../../sessions/c9/c98ca13127783c21035b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

0 个 TeX error。以下是完整报告：

---

## 报告

### (a) Table 4 修复

**位置**：`results.tex` 第 119 行，`\label{tab:cross-model}` 表格 Qwen2.5-7B 行

**修改**：`0.24` → `0.23`（Qwen s020 列）

**依据**：`experiment_summary_table.json` 中 `bf16_qw_imp_s020.median_diff = 0.234979`，四舍五入两位小数为 0.23，不是 0.24。其余三列值正确（s015=0.04, s025=1.27, s030=2.94）。

---

### (b) Table 5 两个数据源差异对比

Table 5 (`tab:cohens-d`) 的 d_z 取自 `cohens_d_bf16.json`/`cohens_d_bf16_qwen.json`，Δ̃ 和 CI 取自 `rebootstrap_b10000_results.json`。`canonical_bf16_stats.json`（paper_figures/）也有 B=10000 bootstrap 结果但随机种子不同。

#### Δ̃ (median diff) 对比

| 实验 | canonical | rebootstrap (论文用) | 差值 |
|------|-----------|---------------------|------|
| DS s015 | 0.3508 | 0.3236 | +0.027 |
| DS s020 | 1.1363 | 1.1520 | −0.016 |
| DS s025 | 4.0174 | 3.9686 | +0.049 |
| DS s030 | 9.9538 | 9.9436 | +0.010 |
| QW s015 | 0.0623 | 0.0476 | +0.015 |
| QW s020 | 0.2860 | 0.2075 | +0.078 |
| QW s025 | 1.1545 | 1.1087 | +0.046 |
| QW s030 | 2.5936 | 2.6194 | −0.026 |

#### 95% CI 对比

| 实验 | canonical CI | rebootstrap CI (论文用) |
|------|-------------|------------------------|
| DS s015 | [0.249, 0.444] | [0.199, 0.472] |
| DS s020 | [0.741, 1.254] | [0.655, 1.256] |
| DS s025 | [3.005, 5.390] | [2.829, 5.292] |
| DS s030 | [8.424, 16.701] | [8.392, 16.653] |
| **QW s015** | **[0.010, 0.123]** | **[−0.005, 0.110]** |
| QW s020 | [0.095, 0.478] | [0.067, 0.402] |
| QW s025 | [0.726, 1.472] | [0.609, 1.469] |
| QW s030 | [1.719, 3.897] | [1.722, 3.651] |

**关键差异：Qwen s015 CI 跨零判断不一致**
- **rebootstrap**（论文采用）：CI = [−0.005, 0.110]，**跨零** → 论文标注 "ns"（marginal）
- **canonical**：CI = [0.010, 0.123]，**不跨零** → 若用此源则 s015 也 significant

这是两个源中最具实质性影响的差异。其余条目的差异均不改变任何定性结论。

---

### (c) s035 II_high=0.105 来源追溯

**不在 canonical_bf16_stats.json 中。** canonical 仅有 s035 的 d_z 值（0.815237），无 per-phase II 指标。

**实际来源**：`/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s035/profiling_results.json` 第 61 行，`"median": 0.105141`（高稀疏度相位的 II 中位数）。

**佐证**：实验日志 `/root/autodl-tmp/pacs/logs/bf16_ds_imp_s035.log:168` 记录 `II[high_sparsity, 0.35]: median=+0.1051 95%CI=[+0.0800, +0.1460]`。

该值来自主四级范围之外的补充实验（s=0.35），直接从原始 profiling 输出提取，未汇入 experiment_summary_table.json 或 canonical_bf16_stats.json。

---
