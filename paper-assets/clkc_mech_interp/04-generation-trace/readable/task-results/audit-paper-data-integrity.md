# audit paper data integrity

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper-data-integrity_20260525T195002_result.json`
- **Structured JSON:** [`20ddc6c5fbb4eb5d1dd0.json`](../../sessions/20/20ddc6c5fbb4eb5d1dd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整审计报告：

---

## 项目 1: Llama 单种子 probe 准确率

**文件**: `probe_results_bootstrap_n2000.json` **不存在**
**替代文件**:
- `/root/clkc_mech_interp/data/llama31/probe_per_layer.json` — 仅含 EN→EN，32 层
- `/root/clkc_mech_interp/data/llama31/probe_results_multiseed.json` — 仅含 EN→EN，3 seeds

| 方向 | 论文写的 | 文件里的 | 是否一致 |
|------|----------|----------|----------|
| EN→EN | 77.6% @L15 | probe_per_layer: **92.2%** @L15; multiseed seed42: **92.75%** @L15 | ⚠️ **严重不一致**：文件数值比论文高 ~15pp |
| ZH→ZH | 72.1% | 无数据（文件仅含 EN→EN） | ❌ 文件未找到 |
| EN→ZH | 59.6% | 无数据 | ❌ 文件未找到 |
| ZH→EN | 70.6% | 无数据 | ❌ 文件未找到 |

**备注**: `bootstrap_n2000.py` 脚本存在但无输出文件。服务器上不存在任何包含 4 方向 cross-lingual probe 数据的文件。论文声称的 EN→EN 77.6% 与现有文件中的 92.2-92.7% 差距巨大，可能是完全不同的实验设置（n=2000 bootstrap vs 原始 probe），但无法在服务器上验证。

---

## 项目 2: Qwen 单种子 probe 准确率和 asymmetry CI

**文件**: `probe_results_bootstrap_n2000.json` **不存在**
**替代文件**:
- `/root/clkc_mech_interp/data/qwen3/probe_results.json` — 仅含 EN→EN，36 层
- `/root/clkc_mech_interp/data/qwen3/probe_results_multiseed.json` — 仅含 EN→EN，3 seeds

| 方向 | 论文写的 | 文件里的 | 是否一致 |
|------|----------|----------|----------|
| EN→EN | 75.0% @L24 | probe_results: **74.8%** @L22; multiseed seed456: **70.2%** @L24 | ⚠️ 不一致：最佳层不同（L22 vs L24），数值接近但不匹配 |
| ZH→ZH | 72.6% | 无数据 | ❌ 文件未找到 |
| EN→ZH | 67.3% | 无数据 | ❌ 文件未找到 |
| ZH→EN | 73.2% | 无数据 | ❌ 文件未找到 |
| Asymmetry CI | [-0.6, 13.7] | 无数据 | ❌ 文件未找到 |

---

## 项目 3: AUROC 数据

**文件**: `/root/clkc_mech_interp/results/auroc_all_models.json`

| 模型 | 指标 | 论文写的 | 文件里的 | 是否一致 |
|------|------|----------|----------|----------|
| Llama | AUROC | 0.981 | 0.9808 | ✅ 一致（四舍五入） |
| Llama | Bal.Acc | 92.7% | 92.67% | ✅ 一致 |
| Gemma | AUROC | 0.931 | 0.9313 | ✅ 一致（四舍五入） |
| Gemma | Bal.Acc | 88.1% | 88.11% | ✅ 一致 |
| Qwen | AUROC | 0.771 | 0.7705 | ✅ 一致（四舍五入） |
| Qwen | Bal.Acc | 71.4% | 71.37% | ✅ 一致 |

---

## 项目 4: Token overlap 分析

**文件**: ❌ 无结果文件
**搜索路径**: `/root/clkc_mech_interp/data/`, `/root/clkc_mech_interp/results/`, 全目录 find overlap/jaccard
**找到的**: 仅有源码脚本（`src/token_overlap.py`, `src/token_overlap_en_de.py`, `src/token_overlap_enhanced.py`），无输出结果

| 指标 | 论文写的 | 文件里的 | 是否一致 |
|------|----------|----------|----------|
| EN-ZH Jaccard | 3-4% | — | ❌ 文件未找到 |
| EN-DE Jaccard | 14.8% | — | ❌ 文件未找到 |
| Llama r | -0.15, p=0.012 | — | ❌ 文件未找到 |

---

## 项目 5: Gemma COMET 三等分分析

**文件**: `/root/clkc_mech_interp/data/gemma2_v2/comet_tertile_ablation.json`

| 指标 | 论文写的 | 文件里的 | 是否一致 |
|------|----------|----------|----------|
| Δ (high-low) | +10.3 pp | 10.28 pp | ✅ 一致（四舍五入 10.3） |
| Fisher p | 0.278 | 0.277996 | ✅ 一致 |
| Low tertile bal_acc | — | 52.3% | （论文未单独列出） |
| High tertile bal_acc | — | 62.6% | （论文未单独列出） |

---

## 项目 6: Selectivity control

**文件**: `/root/clkc_mech_interp/results/random_labels_selectivity.json`

| 指标 | 论文写的 | 文件里的 | 是否一致 |
|------|----------|----------|----------|
| Permuted labels 范围 | 49.2-51.0% | Gemma 49.2%, Qwen 49.7%, Llama **51.1%** | ⚠️ 上界不一致：文件 51.1% vs 论文 51.0% |
| Selectivity gap 范围 | 21-40 pp | Qwen 21.3, Llama 38.9, Gemma 39.6 pp | ✅ 基本一致（21.3-39.6 ≈ 21-40） |

**各模型详情**:
- Llama: permuted_mean=51.05%, selectivity=38.9 pp
- Gemma: permuted_mean=49.24%, selectivity=39.6 pp
- Qwen: permuted_mean=49.69%, selectivity=21.3 pp

---

## 项目 7: 数据重叠统计

**文件**: ❌ 无结果文件
**搜索路径**: 全目录 find overlap/dedup
**结果**: 未找到任何 overlap 或 dedup 结果文件

| 指标 | 论文写的 | 文件里的 | 是否一致 |
|------|----------|----------|----------|
| Three-way overlap | 3.5% (23 questions) | — | ❌ 文件未找到 |
| Pairwise | 7.2%-24.8% | — | ❌ 文件未找到 |

---

## 项目 8: Cross-seed stability

**文件**: 从各模型 `probe_results_multiseed.json` 提取 `balanced_accuracy_std`

| 模型 | 论文写的 | 文件里的 | 是否一致 |
|------|----------|----------|----------|
| Llama | ±0.12% | std=0.0012 → ±0.12% | ✅ 一致 |
| Gemma | ±1.32% | std=0.0132 → ±1.32% | ✅ 一致 |
| Qwen | ±1.90% | std=0.019 → ±1.90% | ✅ 一致 |

---

## 项目 9: N=136 L13 steering 全 alpha 值

**文件**: `/root/clkc_mech_interp/data/llama31/steering_results_L13_last.json`

**⚠️ 关键发现：该文件是 N=201 数据，不是 N=136。服务器上不存在任何 N=136 的 steering 结果文件。**

| Alpha | steering_flips | control_flips | fisher_p | 
|-------|---------------|---------------|----------|
| -20 | 45 | 51 | 0.5587 |
| -10 | 35 | 23 | 0.1179 |
| -5 | 12 | 17 | 0.4412 |
| +5 | 38 | 17 | 0.0034 |
| **+10** | **57** | **27** | **0.000337** |
| +20 | 65 | 62 | 0.8302 |

| 指标 | 论文写的 | 文件里的 | 是否一致 |
|------|----------|----------|----------|
| alpha=+10 fisher_p | p=0.0003 | 0.000337 | ✅ 数值一致（四舍五入 3 位有效数字） |
| 数据来源 | 暗示 N=136 | **N=201** | ⚠️ **论文声称 p=0.0003 确认来自 N=201 数据，非 N=136** |

---

## 项目 10: Seed replication (seed=123)

**文件**: `/root/clkc_mech_interp/data/llama31/steering_results_L13_last_seed123.json`

同样是 N=201 数据，seed=123。

| Alpha | steering_flips | control_flips | fisher_p |
|-------|---------------|---------------|----------|
| -20 | 40 | 63 | 0.0117 |
| -10 | 25 | 55 | 0.000258 |
| -5 | 11 | 16 | 0.4260 |
| +5 | 35 | 14 | 0.00204 |
| +10 | 60 | 30 | 0.000478 |
| +20 | 72 | 45 | 0.0042 |

Baseline 分布与 seed=42 完全相同（neither=56, contextual=131, both=10, parametric=4），确认使用相同测试集。

---

## 项目 11: TOST power 值

**文件**: `/root/clkc_mech_interp/results/tost_bayesian_equivalence.json`

| 指标 | 文件值 |
|------|--------|
| Llama observed_diff | 1.2 pp |
| Qwen observed_diff | 0.5 pp |
| Llama power @margin=10 | 0.5839 |
| Qwen power @margin=10 | 0.5342 |
| Llama min margin for 80% power | 12.3 pp |
| Qwen min margin for 80% power | 12.8 pp |
| Llama BF01 (prior=5) | 1.528 ("anecdotal evidence for equivalence") |
| Qwen BF01 (prior=5) | 1.506 ("anecdotal evidence for equivalence") |

（论文中具体数字未在任务中给出，此处列出文件原始值供对照）

---

## 项目 12: N=201 L13 directional flips 数量

**文件**: `/root/clkc_mech_interp/data/llama31/steering_results_L13_last.json` (N=201)

从所有 alpha 值中统计 `steering_p2c` + `steering_c2p`:

| Alpha | p2c | c2p | 小计 |
|-------|-----|-----|------|
| -20 | 1 | 1 | 2 |
| -10 | 0 | 1 | 1 |
| -5 | 0 | 0 | 0 |
| +5 | 0 | 2 | 2 |
| +10 | 0 | 3 | 3 |
| +20 | 1 | 0 | 1 |
| **合计** | **2** | **7** | **9** |

| 指标 | 论文写的 | 文件里的 | 是否一致 |
|------|----------|----------|----------|
| Directional flips 总数 | Flips: 9 | 9 | ✅ 一致 |
| 数据来源 | — | 确认来自 N=201 | （N=136 数据不存在于服务器） |

---

## 总结

| 类别 | 状态 |
|------|------|
| ✅ 数值完全一致 | 项目 3 (AUROC), 项目 5 (COMET), 项目 8 (cross-seed std), 项目 9 (fisher_p 值本身), 项目 12 (flips=9) |
| ⚠️ 有差异 | 项目 1 (**Llama EN→EN 92.7% vs 论文 77.6%，差 15pp**), 项目 2 (peak layer L22 vs L24), 项目 6 (permuted上界 51.1% vs 51.0%), 项目 9 (**p=0.0003 来自 N=201 非 N=136**) |
| ❌ 文件缺失 | 项目 1 的 4 方向数据, 项目 2 的 4 方向 + asymmetry CI, 项目 4 (token overlap), 项目 7 (数据重叠) |

**最严重的问题**:
1. **Llama 论文声称 EN→EN 77.6% 但服务器文件显示 92.7%** — 差距 15pp，无法用四舍五入解释。bootstrap_n2000 脚本存在但无输出文件，可能是完全不同的实验设定，但结果无法验证。
2. **N=136 steering 数据完全不存在** — 所有 Llama steering 文件都是 N=201。论文如果引用了 N=136 的数据，这些数据不在服务器上。
3. **4 方向 cross-lingual probe 数据（ZH→ZH、EN→ZH、ZH→EN）完全缺失** — 论文声称的多方向数字无法核实。

---
