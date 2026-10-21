# analysis k5 aggregation v2 disambiguate

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-aggregation-v2-disambiguate_20260524T064548_result.json`
- **Structured JSON:** [`1dffc55936b1c579eb2a.json`](../../sessions/1d/1dffc55936b1c579eb2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整汇报。

---

## 文件元数据

| 文件路径 | 修改时间 | 大小 |
|----------|----------|------|
| `artifacts/results/plan001/k5_aggregation_bootstrap.json` | **May 24 14:13** (最新) | 71,140 B |
| `artifacts/_project/data/k5_aggregation_bootstrap.json` | May 23 14:33 | 71,279 B |
| `artifacts/server_backup/results/plan001/k5_aggregation_bootstrap.json` | May 23 14:32 | 71,279 B |

- **V2 标记**：`_is_valid_score`=0, `fix_description`=0, `v2`=0 — **无 V2 标记**
- 旧版本 2 个（May 23，大小一致 71279B），最新版本 May 24（71140B，略小 139B）

以下数据来自 **最新文件**（May 24）。

---

## === Majority Vote ===

| # | 条件 | keff_fdr_p | η_fdr_p |
|---|------|-----------|---------|
| 1 | MMLU × prompt_injection | **0.0108** | 0.1596 |
| 2 | MMLU × sycophancy | **0.0108** | 0.0531 |
| 3 | MMLU × score_manipulation | **0.0134** | 0.5708 |
| 4 | MMLU × verbosity_bias | **0.0148** | 0.0531 |
| 5 | MMLU × position_bias | 0.1527 | **0.0066** |
| 6 | MMLU × authority_bias | **0.0108** | 0.6622 |
| 7 | ARC × prompt_injection | 0.0944 | 0.6622 |
| 8 | ARC × sycophancy | 0.6132 | 0.0847 |
| 9 | ARC × score_manipulation | **0.0108** | **0.0066** |
| 10 | ARC × verbosity_bias | **0.0262** | 0.3575 |
| 11 | ARC × position_bias | 0.9790 | 0.7920 |
| 12 | ARC × authority_bias | 0.1799 | 0.1596 |

**K_eff sig: 7/12** (p<0.05) | **η_max sig: 2/12** (p<0.05)

---

## === Weighted Vote ===

| # | 条件 | keff_fdr_p | η_fdr_p |
|---|------|-----------|---------|
| 1 | MMLU × prompt_injection | **0.0090** | 0.1054 |
| 2 | MMLU × sycophancy | **0.0090** | 0.1054 |
| 3 | MMLU × score_manipulation | **0.0152** | 0.5101 |
| 4 | MMLU × verbosity_bias | **0.0152** | 0.0516 |
| 5 | MMLU × position_bias | 0.0657 | **0.0132** |
| 6 | MMLU × authority_bias | **0.0090** | 0.5083 |
| 7 | ARC × prompt_injection | 0.0657 | 0.7837 |
| 8 | ARC × sycophancy | 0.6127 | 0.1054 |
| 9 | ARC × score_manipulation | **0.0090** | **0.0162** |
| 10 | ARC × verbosity_bias | **0.0369** | 0.4929 |
| 11 | ARC × position_bias | 0.9786 | 0.7837 |
| 12 | ARC × authority_bias | 0.1486 | 0.4929 |

**K_eff sig: 7/12** | **η_max sig: 2/12**

---

## === Threshold Supermajority ===

| # | 条件 | keff_fdr_p | η_fdr_p |
|---|------|-----------|---------|
| 1 | MMLU × prompt_injection | **0.0064** | **0.0376** |
| 2 | MMLU × sycophancy | **0.0072** | **0.0126** |
| 3 | MMLU × score_manipulation | **0.0072** | 0.4799 |
| 4 | MMLU × verbosity_bias | **0.0122** | 0.0504 |
| 5 | MMLU × position_bias | 0.1555 | **0.0060** |
| 6 | MMLU × authority_bias | **0.0064** | 0.5971 |
| 7 | ARC × prompt_injection | 0.0923 | 0.1196 |
| 8 | ARC × sycophancy | 0.3294 | 0.0562 |
| 9 | ARC × score_manipulation | **0.0012** | 0.0504 |
| 10 | ARC × verbosity_bias | **0.0142** | 0.0953 |
| 11 | ARC × position_bias | 0.4249 | 0.9949 |
| 12 | ARC × authority_bias | 0.4290 | 0.1675 |

**K_eff sig: 7/12** | **η_max sig: 3/12**

---

## === Bayesian ===

| # | 条件 | keff_fdr_p | η_fdr_p |
|---|------|-----------|---------|
| 1 | MMLU × prompt_injection | **0.0096** | 0.8881 |
| 2 | MMLU × sycophancy | **0.0076** | 0.8881 |
| 3 | MMLU × score_manipulation | **0.0076** | 0.3533 |
| 4 | MMLU × verbosity_bias | **0.0118** | 0.2064 |
| 5 | MMLU × position_bias | 0.0908 | **0.0132** |
| 6 | MMLU × authority_bias | **0.0096** | 0.3533 |
| 7 | ARC × prompt_injection | 0.2907 | 0.8881 |
| 8 | ARC × sycophancy | 0.0783 | 0.8881 |
| 9 | ARC × score_manipulation | **0.0076** | **0.0462** |
| 10 | ARC × verbosity_bias | **0.0362** | 0.8881 |
| 11 | ARC × position_bias | 0.5692 | 0.8881 |
| 12 | ARC × authority_bias | 0.0832 | 0.8881 |

**K_eff sig: 7/12** | **η_max sig: 2/12**

---

## 汇总表

| Method | η_max sig (p<0.05) | K_eff sig (p<0.05) | K_eff 方向 |
|--------|-------------------|--------------------|-----------|
| Majority Vote | 2/12 | 7/12 | 7正 / 0负 |
| Weighted Vote | 2/12 | 7/12 | 7正 / 0负 |
| Threshold Supermajority | **3/12** | 7/12 | 7正 / 0负 |
| Bayesian | 2/12 | 7/12 | 7正 / 0负 |

关键观察：
- **K_eff 在所有 4 种聚合方式下完全一致**：7/12 显著，全部正向，显著的条件也相同（MMLU 除 position_bias 外的 4 条 + authority_bias + ARC 的 score_manip + verbosity_bias）
- **η_max 整体较弱**，Threshold Supermajority 多出 1 个显著条件（MMLU×prompt_injection 的 0.0376）
- 多个 η_fdr_p 卡在 0.05 边缘：0.0504（Threshold 的 verbosity 和 ARC×score_manip）、0.0516（Weighted 的 verbosity）、0.0531（Majority 的 sycophancy/verbosity）
- 文件**无 V2 标记**，存在 3 个版本（最新 May 24 与旧版 May 23 有 139B 差异）

---
