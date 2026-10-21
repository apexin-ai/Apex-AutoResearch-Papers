# ops w1 table4 baseline data

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w1_table4_baseline_data_20260517T163357_result.json`
- **Structured JSON:** [`30a32aa9fd6c53813ae3.json`](../../sessions/30/30a32aa9fd6c53813ae3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the summary:

---

## Table 4 Baseline 数据可用性

### 当前 Table 4 配置

根据 Round 2 审稿评论，当前 Table 4 实际使用 **N=16** 配置（1.5B×8 + 3B×8），结果目录：`pooled_irt_2pl_gamma_n16_fixed/`。现有数据：

| 方法 | MMLU MAE | ARC MAE | τ |
|------|----------|---------|---|
| B0 Raw | 0.0155 | 0.0338 | **未计算** |
| B3 Vanilla 2PL | 0.0068 | 0.0158 | **未计算** |
| ContamCal (2PL+γ) | 0.0072 | 0.0201 | **未计算** |

τ (Kendall tau) 对所有方法均未计算。`compute_vanilla_2pl_tau_fullitems.py` 曾启动但尚未产出 JSON 结果。

### 各 Baseline 数据可用性

**已有完整代码但未在 N=16/J=13 上运行的（均在 `baselines.py` 中）：**

| 代码名 | 对应任务中的 | 状态 | 计算时间估计 |
|--------|------------|------|------------|
| B1_remove_rescore | — | 代码就绪，N=24 已验证 | CPU, <10s |
| B2_2pl_gamma | 近似 B2 | 代码就绪，需 Stan | ~5-10 min/benchmark |
| B3_vanilla_4pl | 已有独立结果 | N=16 已有 `vanilla_2pl_n16_fixed/` | 已完成 |
| B4_linear_regression | B4 | 代码就绪，N=24 已验证 | CPU, <10s |
| B5_emperor_mitigation | — | 代码就绪，N=24 已验证 | CPU, <10s |
| B6_dcr_fuzzy | B6 | 代码就绪，N=24 已验证 | CPU, <10s |

**任务要求但 baselines.py 中不存在的：**

| Baseline | 状态 | 复杂度 |
|----------|------|--------|
| B1: DRC (dosage/100) | **需新写** | 极简，用 dosage 直接作为校准信号，~10 行代码 |
| B2: Per-domain 2PL+γ | **部分可用** | `mmlu_domain_irt_no05B/` 已有 J=13 domain-level fits（8 domains），需提取 + 聚合为 per-model MAE/τ |
| B5: Threshold classifier | **需新写** | 极简，binary at median RRF，~10 行代码 |

### 主要阻塞

1. **无预存数据矩阵**：J=13/N=16 的 response matrix (`all_y.npy`) 和 exposure matrix (`all_exposure.npy`) 均未保存。需通过 `load_pooled_eval_results()` 从 `eval_results/` 和 RRF scores 重建。

2. **Kendall τ 全缺**：所有方法（包括已有的 B0/B3/ContamCal）的 τ 值都不在现有结果 JSON 中，需用 `evaluate_calibration.py` 统一计算。

3. **Ground truth 按需计算**：通过 `compute_ground_truth()` 函数从 d000 模型原始准确率推导，未持久化。

### 估计总工作量

- 实现 B1-DRC 和 B5-Threshold：~30 min 编码
- 聚合 B2 per-domain 结果：~30 min
- 在 N=16 上运行全部 baselines + τ：~20 min（CPU baselines <1min + Stan baselines ~15 min）
- **总计：~1.5 小时**，不需要 GPU。

---
