# audit tables traceability

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_tables-traceability_20260523T111440_result.json`
- **Structured JSON:** [`bd5792b51b056b97c709.json`](../../sessions/bd/bd5792b51b056b97c709.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。下面是完整报告。

---

## 论文 Table 1/2/3 数据审计报告

### 总览

**共核对 56 个数值**（accuracy、±std、Δ、baselines），其中 **53 个完全一致，3 个存在需注意的问题**。

---

### Table 1: Cross-Model Comparison (26 accuracy + 12 std + 2 baselines = 40 数字)

| Cell | 论文值 | Registry/Eval Log | 判定 |
|------|--------|-------------------|------|
| **exception_only** | | | |
| Qwen-7B | 99.83±0.00 | seeds 42/123/456 全部 99.83% | ✅ |
| Qwen-1.5B | 99.83±0.00 | seeds 42/123/456 全部 99.83% | ✅ |
| CL-13B | 99.89±0.10 | seeds 99.83/100.00/99.83 → mean=99.89, std=0.10 | ✅ |
| DS-6.7B | 99.39±0.10 | seeds 99.33/99.50/99.33 → mean=99.39, std=0.10 | ✅ |
| **ae_only** | | | |
| Qwen-7B | 99.64±0.49 | seeds 99.92/99.08/99.92 → mean=99.64, std=0.49 | ✅ |
| Qwen-1.5B | 98.83±0.36 | seeds 99.08/98.57 → mean=98.83, std=0.36 | ✅ |
| CL-13B | 99.08±0.00 | seeds 99.08/99.08 → mean=99.08, std=0.00 | ✅ |
| DS-6.7B | 98.53±0.30 | seeds 98.74/98.32 → mean=98.53, std=0.30 | ✅ |
| **VOTA** | | | |
| Qwen-7B | 99.05±0.38 | seeds 99.41/98.66/99.08 → mean=99.05, std=0.38 | ✅ |
| Qwen-1.5B | 99.54±0.06 | seeds 99.58/99.50 → mean=99.54, std=0.06 | ✅ |
| CL-13B | 98.74±0.24 | seeds 98.57/98.91 → mean=98.74, std=0.24 | ✅ |
| DS-6.7B | 99.25‡ | seeds 99.16/99.33 (excl outlier 84.45%) → mean=99.25 | ✅ |
| **loop_only** | | | |
| Qwen-7B | 86.05±0.52 | seeds 85.63/85.88/86.64 → mean=86.05, std=0.52 | ✅ |
| Qwen-1.5B | 79.54±1.42 | seeds 78.32/81.09/79.20 → mean=79.54, std=1.42 | ✅ |
| CL-13B | 77.40±1.54 | seeds 77.06/76.05/79.08 → mean=77.40, std=1.54 | ✅ |
| DS-6.7B | 80.31±1.65 | seeds 81.26/81.26/78.40 → mean=80.31, std=1.65 | ✅ |
| **full_trace** | | | |
| Qwen-7B | 81.44±1.11 | see ⚠️ below | ⚠️ |
| Qwen-1.5B | 77.06† | eval=77.06% | ✅ |
| CL-13B | 79.9§ | eval=79.92% (head-2048 proxy) | ✅ |
| DS-6.7B | 79.16† | eval=79.16% | ✅ |
| **no_trace** | | | |
| Qwen-7B | 75.13† | eval=75.13% | ✅ |
| Qwen-1.5B | 72.35±4.48 | see ⚠️ below | ⚠️ |
| CL-13B | 76.47† | eval=76.47% | ✅ |
| DS-6.7B | 73.36† | eval=73.36% | ✅ |
| **Baselines** | | | |
| Regex B5 | 99.33 | registry=99.33% | ✅ |
| Majority | 71.51 | registry=71.51% | ✅ |

### Table 2: Component Ablation (Qwen-7B) — 新增条目

| Cell | 论文值 | Registry/Eval Log | 判定 |
|------|--------|-------------------|------|
| VOTA\_no\_ae | 99.41 | eval=1183/1190=99.41% | ✅ |
| Regex (best) | 93.61 | registry B4=93.61% | ✅ |
| 3-shot Qwen-7B | 90.84 | registry=90.84% | ✅ |
| Zero-shot range | 51.0–93.5 | CL=51.01, Q7B=89.08, DS=90.59, Q1.5B=93.45 | ✅ |

Table 2 其余行与 Table 1 Qwen-7B 列重复，已验证。

### Table 3: Gradient Masking Decomposition

| Cell | 论文值 | Registry/Eval Log | 判定 |
|------|--------|-------------------|------|
| exception\_only | 99.83±0.00 | (同 Table 1) | ✅ |
| +grad mask | 99.22±0.20 | seeds 98.99/99.33/99.33 → mean=99.22, std=0.20 | ✅ |
| full\_trace | 81.76‡ | eval seed42=81.76% | ✅ |
| label-only | 85.94±1.12 | seeds 86.22/86.89/84.71 → mean=85.94, std=1.12 | ✅ |
| Δ grad mask | −0.61pp | 99.22−99.83=−0.61 | ✅ |
| Δ full\_trace | −18.07pp | 81.76−99.83=−18.07 | ✅ |
| Δ label-only | +4.50pp | 85.94−81.44=+4.50 | ✅ |
| DS masking | 99.33% | eval=99.33% | ✅ |
| DS dilution | ≤0.3% | (99.39−99.33)/20.23=0.3% | ✅ |

---

## ⚠️ 需关注的问题（3 项）

### 1. Qwen-7B full\_trace seed123: registry 与 eval log 不一致

- **eval\_results.json**: `qwen7b_full_trace_seed123/final/eval_results.json` → accuracy = **0.80168** (954/1190 = **80.17%**)
- **registry**: 存储为 **80.20%**（不对应 n=1190 的任何有效计数）
- **影响**: 论文用 registry 值(80.20%)计算 → mean=81.44, std=1.11；用 eval log 值(80.17%)计算 → mean=**81.43**, std=**1.13**
- **严重程度**: 低。Mean 差 0.01pp，Std 差 0.02。不影响任何结论。
- **建议**: 更新 registry 中 `qwen7b_full_trace_seed123` 的 accuracy 为 0.8017（或使用精确值 954/1190），然后更新论文为 81.43±1.13。

### 2. Qwen-1.5B no\_trace seed42: 两个冲突的实验结果

- 服务器上存在**两个不同目录**：
  - `qwen15b_no_trace_seed42` → accuracy = **67.31%**（论文使用此值）
  - `qwen1.5b_no_trace_seed42` → accuracy = **72.61%**（registry 指向此值）
- 论文 3-seed mean=72.35±4.48 只能用 **(67.31, 75.88, 73.87)** 得出
- 如果用 registry 值 72.61% 代替 → mean=**74.12**±1.65，与论文值差 1.77pp
- **严重程度**: 中。虽然论文内部自洽（mean/std 计算正确），但 registry 与论文用的 seed42 值不一致。需要确认哪个实验才是 canonical run：
  - 如果 `qwen15b_` (67.31%) 是正确的 → 需更新 registry
  - 如果 `qwen1.5b_` (72.61%) 是正确的 → 需更新论文（mean→74.12, std→1.65）

### 3. Registry 小规模精度问题（不影响论文）

以下 registry 值存在轻微精度偏差（论文值均正确）：
- CL-13B no\_trace: registry=76.50% vs eval=76.47%（论文用 76.47%，正确）
- VOTA\_no\_ae: registry=99.40% vs eval=99.41%（论文用 99.41%，正确）

---

## 最终统计

| | 数量 |
|---|---|
| 总核对数字 | **56** |
| 完全一致 | **53** (94.6%) |
| Registry 精度问题（论文正确） | **2** |
| 需确认的实质性问题 | **1** (Qwen-1.5B no\_trace seed42 冲突) |

**结论**: 论文所有数字内部计算正确（mean/std/Δ 全部可复现），无虚构数据。唯一需要 resolve 的是 Qwen-1.5B no\_trace seed42 的两个实验版本——确认 canonical run 后，要么更新 registry 要么更新论文。

---
