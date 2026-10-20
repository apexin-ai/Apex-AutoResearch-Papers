# Gradient Ratio 溯源调查报告

> 调查日期：2026-05-14 | 严重性：P0 论文诚信

---

## 结论摘要

1. **"47-104×" 来源已确认**：Reviewer agent 用 `seg low_mean / high_mean` 计算，s015 因 mean 为负替换为 median ratio。D028 原文采纳，未注明公式混用。
2. **Registry gradient_paired_aggregate 存在跨实验公式不一致**：s015/s025 存的是 median ratio，s020/s030 存的是 mean **差值**（不是比值）。
3. **所有 ratio 指标因 high-phase II 近零而本质不稳定**，不适合作为论文 headline number。
4. **推荐**：median difference（D031 已采纳）+ Cohen's d 作为补充。

---

## 问题 1："47-104×" 出自哪里？

### 直接来源

D028（2026-05-14 06:42 UTC），数字由 **Reviewer agent** 在 06:40 UTC 的审查报告中计算。

### 计算公式

Reviewer 使用 `interaction_index.low_sparsity.mean / interaction_index.high_sparsity.mean`（segment-level aggregate mean ratio）：

| s | high_mean | low_mean | low/high ratio | D028 报告值 |
|---|-----------|----------|----------------|-------------|
| 0.15 | **-0.150** | 2.406 | **-16.02** (负，无意义) | 69× (替换为 median ratio) |
| 0.20 | 0.129 | 6.029 | 46.76 | 47× |
| 0.25 | 0.303 | 25.853 | 85.39 | 85× |
| 0.30 | 0.555 | 57.795 | 104.19 | 104× |

**D028 的 "47-104×" = s020(47) 到 s030(104) 的 mean ratio 范围，s015 因 mean 为负而用 median ratio (69) 替代。Director 未注明公式混用。**

### 为什么 fp16 的 "11-42×" 也不匹配

fp16 registry 存储的是 `bootstrap_gradient_paired`（paired bootstrap 计算的 gradient），计算方式与 bf16 的 aggregate ratio 完全不同：
- v6_importance_s015: bootstrap_gradient_paired = 11.53
- v6_importance_s020: bootstrap_gradient_paired = 11.05
- v6_importance_s025: bootstrap_gradient_paired = 35.72
- v6_importance_s030: bootstrap_gradient_paired = 41.92

这是第四种不同的计算方式。

---

## 问题 2：Registry s020 = 5.90 为何异常低？

### 根因：Worker 2 计算的是差值，不是比值

Registry 中 `gradient_paired_aggregate` 由**两个不同 Worker** 使用**两个不同公式**写入：

| Worker | 负责实验 | 公式 | 结果 |
|--------|---------|------|------|
| Worker 1 (06:21 UTC) | s015, s025 | `low_median / high_median` | 69.24, 222.35 |
| Worker 2 (06:41 UTC) | s020, s030 | `low_mean - high_mean` | **5.90**, **57.24** |

**s020 的 5.90 = 6.029 - 0.129 = 5.90（mean 差值），不是比值。** 同一字段名 `gradient_paired_aggregate` 在不同实验中存储了完全不同的量。

如果 s020 用 Worker 1 的公式（median ratio），结果为 **103.10**。

### 后续 batch2 Worker 检测到不一致

batch2 Worker (06:46 UTC) 重新计算了 s020=103.10, s030=274.24（使用 median ratio），但**未更新 registry**。

---

## 问题 3：Registry s025 = 222.35 为何异常高？

### 根因：high_median 极小导致 ratio 膨胀

s025 使用 Worker 1 的公式 `low_median / high_median = 7.196 / 0.032 = 222.35`。

high_median = 0.032 非常小（接近零），导致比值膨胀。而 D028 的 85× 用的是 `low_mean / high_mean = 25.853 / 0.303 = 85.39`，因为 high_mean (0.303) >> high_median (0.032)。

**两个看似针对同一实验的 "gradient" 指标差 2.6 倍，原因是 mean vs median 选择在 high-phase 分布高度偏斜时产生巨大差异。**

---

## High-Phase II 近零分析

per-problem high-phase II 数据显示分母系统性接近零：

| Sparsity | high n | near-zero (|x|<0.01) | negative | median | mean |
|----------|--------|----------------------|----------|--------|------|
| 0.15 | 49 | **14 (29%)** | **24 (49%)** | 0.00012 | -0.013 |
| 0.20 | 49 | **8 (16%)** | **22 (45%)** | 0.0036 | 0.0025 |
| 0.25 | 49 | **8 (16%)** | **21 (43%)** | 0.0099 | 0.134 |
| 0.30 | 49 | **5 (10%)** | **15 (31%)** | 0.034 | 0.198 |

高比例的近零和负值使得 **任何 ratio 指标** 都不稳定。

---

## 问题 4：推荐指标

### 全指标对比表

| 指标 | s015 | s020 | s025 | s030 | 单调? | EPS敏感? | 可解释? |
|------|------|------|------|------|-------|---------|--------|
| **D. seg median diff** | **0.39** | **1.48** | **7.16** | **14.59** | **✓** | **否** | **强** |
| **G. Cohen's d** | **0.60** | **0.72** | **0.95** | **1.12** | **✓** | **否** | **强（标准）** |
| H. Rank-biserial r | 0.59 | 0.77 | 0.80 | 0.83 | ✓ | 否 | 强（标准） |
| C. seg mean diff | 2.56 | 5.90 | 25.55 | 57.24 | ✓ | 否 | 中（受 outlier 影响） |
| E. per-prob median ratio (EPS=0.01) | 13.87 | 50.34 | 78.78 | 175.77 | ✓ | **是（变化 2×）** | 弱 |
| A. seg median ratio | 69.24 | 103.10 | 222.35 | 274.15 | ✓ | N/A | 弱（膨胀） |
| B. seg mean ratio | -16.02 | 46.76 | 85.39 | 104.19 | ✗ (s015负) | N/A | **不可用** |

### EPS 敏感性（per-problem ratio）

| EPS | s015 | s020 | s025 | s030 |
|-----|------|------|------|------|
| 0.001 | 14.05 | 54.07 | 79.79 | 175.77 |
| 0.01 | 13.87 | 50.34 | 78.78 | 175.77 |
| 0.05 | 6.15 | 20.07 | 50.58 | 129.81 |
| 0.10 | 3.24 | 10.77 | 38.74 | 79.78 |

EPS 从 0.01 变到 0.1，s015 ratio 从 14× 降到 3×（变化 4.3 倍），不可接受。

### 推荐方案

**主指标：Segment-level median difference (II_low - II_high)**
- 值：0.39, 1.48, 7.16, 14.59
- 优点：单调递增、不涉及除法、不受 outlier 影响、完全可复现
- 论文表述："The compound interaction in the low-sparsity phase exceeds the high-sparsity phase by 0.39 to 14.59 (median II difference), scaling monotonically with sparsity level."
- **D031 已采纳此方案**

**补充指标：Cohen's d**
- 值：0.60, 0.72, 0.95, 1.12（中等→大效应）
- 优点：审稿人熟知的标准化效应量、单调、不受 EPS 影响
- 论文表述："Effect sizes range from medium (d=0.60 at s=0.15) to large (d=1.12 at s=0.30)."

**弃用所有 ratio 指标**：high-phase II 系统性近零（29-49% 样本 < 0.01），ratio 本质不稳定。Registry 已有 3 种不同 "gradient" 计算结果差距 50×，证明 ratio 不可靠。

---

## Registry 数据完整性问题清单

| 问题 | 受影响实验 | 建议 |
|------|-----------|------|
| gradient_paired_aggregate 存储差值而非比值 | bf16_importance_s020, s030 | 更新或删除该字段 |
| 字段名暗示 ratio 但实际是 difference | s020 (5.90), s030 (57.24) | 重命名或统一公式 |
| D028 混用 mean ratio + median ratio | 所有 4 个实验 | 更正 D028 或标注废弃 |
| ROADMAP 中 "47-104×" 不可从 registry 复现 | N/A | 更新 ROADMAP 使用推荐指标 |

---

## 文件溯源链

1. **Reviewer agent report** → feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer.jsonl, line 1596, 2026-05-14T06:40:09 UTC
2. **D028** → decisions.yaml, 2026-05-14 06:42 UTC
3. **Worker 1 (s015/s025 registry)** → worker_analysis_bf16_imp_s015_s025_20260514T062105.log
4. **Worker 2 (s020/s030 registry)** → worker_analysis_bf16_importance_s020_s030_20260514T064103.log
5. **batch2 Worker (detected inconsistency)** → worker_analysis_bf16_batch2_random_and_imp_20260514T064655.log
