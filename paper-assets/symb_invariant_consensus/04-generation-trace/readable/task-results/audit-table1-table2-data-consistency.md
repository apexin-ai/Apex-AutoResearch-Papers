# audit table1 table2 data consistency

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table1-table2-data-consistency_20260523T102233_result.json`
- **Structured JSON:** [`82486c70e9d8b47aac83.json`](../../sessions/82/82486c70e9d8b47aac83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All p-values match perfectly after alpha tiebreaking. I now have the complete picture. Here is the comprehensive report.

---

## Table 1 & Table 2 数据正确性核查报告

### 方法说明
论文中的 SC 值使用了 **alphabetical tiebreaking**（平票时按字母序选答案）。原始结果文件存储的是旧版 tiebreaking 值，需要重算后比较。已对所有可验证条件进行了重算并比对 McNemar p 值。

---

### Table 1 (`tab:main_results`, experiments.tex)

| 行 | 条件 | 状态 | 说明 |
|---|------|------|------|
| T1-01 | Mistral-7B × PW-D5 | ⚠️ 无法核查 | 原始实验文件 exp-046 不在本服务器（来自旧服务器 25068） |
| T1-02 | Mistral-7B × LogiQA | ✅ 一致 | Alpha tiebreak 后 SC=50.00%, SICA=51.50%, Δ=+1.50, p=0.581 全部吻合 |
| T1-03 | Mistral-7B × FOLIO(s123) | ✅ 一致 | SC=54.41%(tiebreak), SICA=57.35%, Δ=+2.94, p=0.070 |
| T1-04 | Mistral-7B(3s) × FOLIO | ✅ 一致 | 3-seed={123,456,789} 均值 SC=56.53%, SICA=56.70%, Δ=+0.16 |
| T1-05 | Mistral-7B × FOLIO(s456) | ✅ 一致 | SC=55.88%(tiebreak), SICA=55.88%, p=1.000 |
| T1-06 | Mistral-7B × FOLIO(s789) | ✅ 一致 | SC=59.31%, SICA=56.86%, Δ=-2.45, p=0.267 |
| T1-07 | LLaMA-8B × FOLIO | ✅ 一致 | SC=66.18%, SICA=61.76%, Δ=-4.41, p=0.093 |
| T1-08 | LLaMA-8B × StrategyQA | ⚠️ 无法核查 | 服务器上未找到 StrategyQA 结果文件 |
| T1-09 | Qwen2.5-14B × FOLIO(ICL) | ⚠️ 无法核查 | 未找到对应的 Qwen2.5-14B ICL 结果文件 |
| T1-10 | Qwen2.5-14B × PW-D5 | ✅ 一致 | SC=74.00%(tiebreak), SICA=71.50%, Δ=-2.50, p=0.011 |
| T1-11 | Qwen2.5-14B(4s) × FOLIO | ✅ 一致 | 报告默认种子值（^{4s}为确认性标注）。SC=75.98%(tiebreak), SICA=75.49% |
| T1-12 | Qwen2.5-7B × FOLIO | ⚠️ 无法核查 | 实验目录存在但无 results.json（仅日志） |
| T1-13 | Qwen2.5-14B × LogiQA | ✅ 一致 | SC=79.00%(tiebreak), SICA=78.00%, Δ=-1.00, p=0.625 |
| T1-14 | Qwen3-14B × FOLIO | ✅ 一致 | SC=83.33%, SICA=84.80%（来源: exp_folio_2x2_qwen3） |
| T1-15 | Qwen3-14B × PW-D5 | ✅ 一致 | SC=85.83%(tiebreak), SICA=85.67%, Δ=-0.17, p=1.000 |
| T1-16 | Qwen3-14B(think) × FOLIO | ⚠️ 无法核查 | 仅存 38/204 问题的部分结果 |

**Table 1 小结**: 11/16 行已验证一致，5 行因源文件缺失无法核查，0 行发现不一致。

---

### Table 2 (`tab:frontier-scb`, analysis.tex)

| 行 | 模型 | 状态 | 说明 |
|---|------|------|------|
| T2-01 | Mistral-7B (self) | ✅ 一致 | SC=55.88%, n_err=90 |
| T2-02 | LLaMA-8B (self) | ⚠️ 无法核查 | SC/Δ 为 "---"；BR=2.88 未找到独立源文件 |
| T2-03 | Qwen-14B (self) | ✅ 一致 | SC=75.98%(tiebreak), n_err=49, Δ=-0.49 |
| T2-04 | R1-Distill-8B (cross) | ✅ 一致 | SC=74.51%, n_err=52, BR=2.92, Δ=+2.45 全部吻合 |
| T2-05 | **gpt-4o (self)** | ❌ **不一致** | 详见下方 |
| T2-06 | gpt-4.1 (cross) | ✅ 一致 | SC=82.84%, n_err=35, BR=2.70, Δ=-1.47 |
| T2-07 | gpt-5.5 (cross) | ✅ 一致 | SC=84.31%, n_err=32, Δ=+0.49 |
| T2-08 | o3 (cross) | ❌ 小幅不一致 | n_err=34（数据）vs 35（论文），差 1 |
| T2-09 | Gemini-2.5-Pro (cross) | ❌ 小幅不一致 | Δ=-1.05（数据）vs -1.10（论文），差 0.05pp |

---

### ❌ 严重问题：T2-05 gpt-4o

| 指标 | 论文声称值 | 实际数据值 | 来源 |
|------|-----------|-----------|------|
| SC(%) | 73.91 | **76.96** | e6_gpt4o_folio204/results.json |
| n_err | 53 | **47** | 204 - 157 |
| BR | 2.94 | **2.65** | 重算（28个SC错误问题） |
| Δ(pp) | -1.80 | **-1.96** | 75.00 - 76.96 |

- Alpha tiebreaking 后 SC 仍为 76.96%（6个平票问题分辨结果不变）
- 论文中 73.91% 不对应任何 n=204 的整数比（151/204=74.02%, 150/204=73.53%）
- 即使用 n_err=53 倒推，SC 应为 74.02% 而非 73.91%（论文内部也不自洽）
- 最可能原因：**论文使用了不同的 gpt-4o 运行结果**（API 非确定性），但该运行的结果未保存在本服务器

---

### ❌ 小幅问题

1. **o3 n_err**: 数据 = 196-162 = **34**, 论文写 **35**（差 1）
2. **Gemini Δ**: 数据 = (82-83)/95×100 = **-1.05**pp, 论文写 **-1.10**pp（差 0.05）

---

### ⚠️ 无法核查的条件（5 条）

| 条件 | 原因 |
|------|------|
| Mistral-7B × PW-D5 | 源实验 exp-046 在旧服务器 25068 上 |
| LLaMA-8B × StrategyQA | 未找到结果文件 |
| Qwen2.5-14B × FOLIO(ICL) | 未找到对应文件 |
| Qwen2.5-7B × FOLIO | 实验无 results.json |
| Qwen3-14B(think) × FOLIO | 仅 38/204 部分结果 |

---

### 需要处理的优先级

1. **[必须修复]** gpt-4o 行：要么找到原始运行数据并确认，要么用当前 e6 数据更新 Table 2（SC=76.96%, n_err=47, BR=2.65, Δ=-1.96）
2. **[建议修复]** o3 n_err: 35 → 34
3. **[建议修复]** Gemini Δ: -1.10 → -1.05
4. **[建议补全]** 将 5 个无法核查条件的源数据上传到本服务器

---
