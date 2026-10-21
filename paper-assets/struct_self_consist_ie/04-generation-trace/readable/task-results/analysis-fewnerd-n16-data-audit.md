# analysis fewnerd n16 data audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewnerd_n16_data_audit_20260519T075713_result.json`
- **Structured JSON:** [`a0b020196e5cb5a0ee6a.json`](../../sessions/a0/a0b020196e5cb5a0ee6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

---

### 任务 1a：L143 LP selection "+0.52pp" (N=16)

**来源已确认**：`exp_027_fewnerd_n16/paired_n8_baseline.json`

| 字段 | 值 |
|---|---|
| 实验 | exp_027_fewnerd_n16 |
| 数据集 | FewNERD 5K 子集（非全测试集 37,648） |
| Seed | 42 only |
| N=8 LP delta | +1.37pp |
| N=16 LP delta | +1.88pp |
| **Paired bootstrap (N16−N8)** | **+0.5169pp ≈ +0.52pp** |
| p-value | 0.0034 ≈ 0.003 |

- "+0.52pp" 是 N=8→N=16 的**增量 LP selection 增益**，不是 N=16 的绝对 LP delta
- **问题**：论文引用 `Appendix app:n_scaling`，但该附录只有 SciERC N-scaling 数据（tab:n-scaling, tab:n_scaling_selection），**无任何 FewNERD N=16 数据** → 引用悬空

---

### 任务 1b：L213 Construction "+1.32pp" (N=16)

**无法追溯。**

已检查位置：
- `exp_027_fewnerd_n16/results.json` — 只有 selection 数据（LP Δ=+1.88pp），无 entity construction
- `entity_construction/construction_results.json` — FewNERD 数据来自 N=16 样本（oracle=0.902 确认），但各 θ 的 LP-weighted 结果均不匹配 1.32：
  - θ=0.125（即 2/N=2/16）：介于 t0.1（Δ=−1.49pp）和 t0.15（Δ≈+1.0pp）之间，估算 ≈ −0.25pp
  - θ=0.2：Δ=+1.44pp
  - θ=0.25：Δ=+1.52pp
  - θ=0.3：Δ=+1.36pp
- `entity_construction_fair/bootstrap_tests.json` — FewNERD LP-weighted CV: mean_diff=+1.42pp, CI [0.87, 1.99]
- `entity_construction_fair_n8/multiseed_results.json` — N=8 FewNERD 4-seed mean=+1.40±0.51pp（seed42=+0.88pp）
- Registry `exp_fewnerd_s789_n8` — four_seed_lp_delta_ci95 **下界**=1.32（但这是 N=8 LP selection CI，不是 N=16 entity construction）

**问题汇总**：
1. 数字 1.32 无法对应到任何数据文件
2. "rises to +1.32" 语义矛盾——N=8 multi-seed mean 为 +1.40pp，+1.32 反而更低
3. 同样引用 `Appendix app:n_scaling`，但该附录无 FewNERD construction 数据 → 引用悬空

**最可能来源**：1.32 是 N=8 4-seed LP selection CI 下界（exp_fewnerd_s789_n8），被误标为 N=16 entity construction。

---

### 任务 2：fig_selection_gap caption ρ 核对

**生成脚本**：`code/plot_selection_gap_single.py`（双 Y 轴：bars=ρ, line=ΔF1）

**图中数据**（seed42, SciERC N=8）：

| Signal | 图中 ρ | 表 tab:quality_estimation ρ |
|---|---|---|
| SJ | 0.360 | .360 |
| FK | 0.267 | .267 |
| EM | 0.299 | .295 |
| **VC** | **0.252** | **.379** |
| LP | 0.205 | .205 |

- **VC 是否画了**：是，5 个 signal 全画了（SJ, FK, EM, VC, LP）
- **图中最大 ρ**：SJ = 0.360 ≈ 0.36
- **Caption 写的**："ρ up to 0.38"
- **表中最大 ρ**：VC = 0.379 ≈ 0.38

**问题**：
1. 图中 VC ρ = 0.252，远低于 tab:quality_estimation 的 0.379 — **图中 VC 数据有误**（可能用了 conditional ρ 或其他变体）
2. Caption "ρ up to 0.38" 对应的是 tab:quality_estimation 的 VC=0.379，**但图中实际画的最大值是 SJ=0.36** → 图和 caption 不一致
3. Caption 写 "2-seed mean"，但脚本注释明确标注数据来自 seed42 only

**建议修正**：
- 修复 VC ρ 数据，使其与 tab:quality_estimation 一致（0.379）
- 或：如果图有意使用 conditional ρ，修改 caption 为 "ρ up to 0.36" 并注明 conditional
- 修改 "2-seed mean" 为实际数据来源（seed42 或真正的 multi-seed）

---

### 完整 exp_027_fewnerd_n16 数据（供参考）

| Metric | 值 |
|---|---|
| N instances | 5,000（5K 子集），gold-filtered 4,351 |
| Seed | 42 |
| Greedy F1 | 0.7478 |
| Oracle F1 | 0.9020 |
| Headroom | 15.43pp |
| Degen rate | 4.53%（cf1 gold-filtered）/ 7.07%（results.json） |
| LP sel F1 | 0.7666 |
| LP Δ | +1.88pp, CI [1.41, 2.37], p<0.001 |
| SJ Δ | −1.36pp |
| FK Δ | −1.47pp |
| EM Δ | −2.72pp |
| VC Δ | −2.82pp |
| LP ρ (global) | 0.416 |
| LP ρ (cond) | 0.436 |

---
