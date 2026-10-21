# D028 核心数字一致性审计报告

审计日期：2026-05-14

---

## 一、数据宇宙地图

项目存在 **三套独立数据源**，数字混用是不一致的根因。

| 编号 | 数据源 | Tasks | Episodes | 用途 | 可靠性 |
|------|--------|-------|----------|------|--------|
| **A** | plan-001b 完整版 | 11 | 245 | plan-012 decomposition 分析 | ★★★ 权威 |
| **B** | prescreening 全集 | 30 | 249 | 早期探索性分析 | ★★ 每 task 仅 5-9 eps |
| **C** | plan-001b 早期子集 | 11 | 194 | plan-003 baseline + SFT 训练数据 | ★★★ 权威（用途不同） |

### 11 Tasks（A、C 共享任务列表）

chemistry-mix, find-animal, find-non-living-thing, freeze, grow-fruit, identify-life-stages-1, identify-life-stages-2, inclined-plane-determine-angle, lifespan-longest-lived, lifespan-longest-lived-then-shortest-lived, measure-melting-point-unknown-substance

---

## 二、权威数字表

### 2.1 Decomposition 分析（plan-012-full，数据源 A）

| 指标 | 值 | 来源文件 | 验证状态 |
|------|---|---------|---------|
| Δ_full | **+29.60** | `results/plan_012_decomposition` (CSV) | ✅ 加权平均验算一致 |
| Δ_nd | **+2.84** | registry plan-012-full | ✅ 与 daf 计算一致 |
| death_avoidance_fraction | **90.41%** | = 1 - 2.84/29.60 | ✅ |
| pearson_r | **0.9698** | registry plan-012-full | ✅ (death_rate_diff vs delta) |
| pearson_p | **8.12e-07** | registry plan-012-full | ✅ |
| n_tasks | **11** | CSV 行数 | ✅ |
| n_episodes | **245** | CSV n 列求和 | ✅ (20+20+40+20+20+20+20+20+25+20+20) |
| death_rate_int (agg) | **0.429** | registry | ✅ |
| death_rate_det (agg) | **0.163** | registry | ✅ |
| label_dist | det=86, int=9, no_pref=150 | CSV det_pref/int_pref/no_pref 列 | ✅ |

**来源文件**：`results/plan_012_decomposition`（CSV，与 `results/death_decomposition_preliminary.csv` 内容相同）

#### Per-task decomposition（来源 A）

| Task | n | Δ_full | Δ_nd | dr_int | dr_det | det_pref | int_pref | no_pref |
|------|---|--------|------|--------|--------|----------|----------|---------|
| chemistry-mix | 20 | 21.80 | 0.00 | 0.45 | 0.25 | 6 | 2 | 12 |
| find-animal | 20 | 26.65 | 0.00 | 0.50 | 0.25 | 5 | 0 | 15 |
| find-non-living-thing | 40 | 9.58 | 9.58 | 0.00 | 0.00 | 16 | 4 | 20 |
| freeze | 20 | 30.50 | 0.00 | 0.55 | 0.25 | 6 | 0 | 14 |
| grow-fruit | 20 | 25.10 | 0.00 | 0.45 | 0.20 | 6 | 1 | 13 |
| identify-life-stages-1 | 20 | 47.50 | 0.00 | 0.55 | 0.10 | 9 | 0 | 11 |
| identify-life-stages-2 | 20 | 30.00 | 0.00 | 0.50 | 0.20 | 6 | 0 | 14 |
| inclined-plane-determine-angle | 20 | 36.00 | 0.00 | 0.55 | 0.20 | 7 | 0 | 13 |
| lifespan-longest-lived | 25 | 44.00 | 0.00 | 0.56 | 0.16 | 11 | 1 | 13 |
| lifespan-longest-lived-then-shortest-lived | 20 | 40.80 | 0.00 | 0.45 | 0.10 | 8 | 1 | 11 |
| measure-melting-point-unknown-substance | 20 | 30.05 | 0.00 | 0.55 | 0.25 | 6 | 0 | 14 |

### 2.2 Baseline 评估（plan-003-baseline，数据源 C）

| 策略 | continuous_score | CI_90 | success_rate | death_rate | sim_ratio |
|------|-----------------|-------|-------------|-----------|-----------|
| always-internal | **-37.16** | [-43.39, -31.43] | 12.37% | 40.72% | 0.0 |
| always-deterministic | **-11.64** | [-17.39, -6.55] | 23.71% | 18.56% | 1.0 |
| oracle | **-9.03** | [-14.14, -4.15] | 24.23% | 16.49% | 0.962 |
| random | **-23.75** | [-29.60, -18.11] | 16.49% | 28.35% | 0.503 |
| trained-router (v6) | -11.64 | [-17.39, -6.55] | 23.71% | 18.56% | 1.0 |

**n_episodes = 194, n_tasks = 11**
**来源文件**：`results/plan_003_eval/overall_results.json`

> ⚠️ **trained-router 完全退化**：与 always-deterministic 数字完全相同，sim_ratio=1.0 说明 router 100% 选择 deterministic。该行不可用于论文。

### 2.3 Keyword Baseline（plan-011-rule-based）

| 版本 | 关键词数 | Episodes | 匹配率 | Episode准确率 | 退化方向 | 来源文件 |
|------|---------|----------|--------|-------------|---------|---------|
| v1 | 20 | 204 | 85.8% | 97.65% | → always-det | `results/rule_based_accuracy_v1_rerun.json` |
| v2 | 17 | 203 | 4.9% | 1.19% | → always-internal | `results/rule_based_accuracy_v2_test.json` |
| v3 | 9 | 225 | 6.1% | 23.26% | → always-internal | `results/rule_based_accuracy_v3.json` |

> 三版均结构性失效。v1 "高准确率" 是 "connect" 关键词假阳性（匹配 3963 次）。

### 2.4 SFT 训练数据

| 指标 | 值 | 来源文件 | 验证 |
|------|---|---------|------|
| 样本数 | **2040** | `data/plan-004-implicit/implicit_sft.jsonl` | ✅ wc -l = 2040 |
| deterministic 标签 | **1830** (89.7%) | `data/plan-004-implicit/conversion_summary.json` | ✅ |
| internal 标签 | **210** (10.3%) | 同上 | ✅ |
| 来源 episodes | **68** (有 preference 的) | 从 194 eps 中提取 | ✅ 与 plan-005 routing_patterns 一致 |
| 总 steps | 2040 | 来自 68 episodes 的 step-level 标签 | ✅ |

> `data/plan-004-v3/implicit_sft.jsonl` 与上述文件完全相同（2040 行，同分布）。

---

## 三、不一致清单

### INC-1：death_decomposition_report.json ≠ plan-012-full（⚠️ 严重）

| | death_decomposition_report.json | plan-012-full (CSV) |
|---|---|---|
| Tasks | 30 | **11** ← 权威 |
| Episodes | 249 | **245** ← 权威 |
| Δ_full | 38.33 | **29.60** ← 权威 |
| Δ_nd | 0.48 | **2.84** ← 权威 |
| death_frac | 98.75% | **90.41%** ← 权威 |
| r | 0.9864 | **0.9698** ← 权威 |

**原因**：`death_decomposition_report.json` 使用 prescreening 30-task 数据（数据源 B），不是 plan-012-full。文件名极易混淆。

### INC-2：Episode 数量差异 245 vs 194（已解释，非错误）

| Task | plan-003 (C) | plan-012 (A) | 增量 |
|------|-------------|-------------|------|
| chemistry-mix | 20 | 20 | 0 |
| find-animal | 15 | 20 | +5 |
| find-non-living-thing | 35 | 40 | +5 |
| freeze | 20 | 20 | 0 |
| grow-fruit | 15 | 20 | +5 |
| identify-life-stages-1 | 15 | 20 | +5 |
| identify-life-stages-2 | 15 | 20 | +5 |
| inclined-plane-determine-angle | 15 | 20 | +5 |
| lifespan-longest-lived | 9 | 25 | +16 |
| lifespan-longest-lived-then-shortest-lived | 15 | 20 | +5 |
| measure-melting-point-unknown-substance | 20 | 20 | 0 |
| **总计** | **194** | **245** | **+51** |

**原因**：plan-001b 追加 rebalance 实验，将 8 个 task 扩展到 ≥20 eps。plan-003 baseline 在扩展前运行。

**影响**：plan-003 baseline 与 plan-012 decomposition **不可直接对比**（不同 episode 集合）。SFT 数据（2040 samples）来自 194-episode 子集。

### INC-3：plan005/routing_metrics.json 混合数据源

30 tasks，episode 数量与 prescreening 和 plan-001b 都不完全匹配（如 find-animal=25, grow-fruit=18）。是混合数据源。**不应用于论文。**

### INC-4：rule_based_accuracy 各版本 episode 数不一致

v1=204, v2=203, v3=225。不同版本使用不同 task 子集。

### INC-5：死亡率指标命名不统一

- plan-003: `catastrophic_failure_rate`
- plan-012 CSV: `death_rate_int` / `death_rate_det`
- decomposition report: `int_death_rate` / `det_death_rate`

含义相同，论文统一为 "death rate"。

### INC-6：death_decomposition_preliminary_OLD.csv 过时

OLD 版本 chemistry-mix=10 eps（总 235），当前版本=20 eps（总 245）。OLD 版本已弃用。

---

## 四、论文写作建议

### Table 1: Baseline Comparison → 用 plan-003 (194 eps)

| Strategy | Score |
|----------|-------|
| Always-Internal | -37.16 |
| Always-Deterministic | -11.64 |
| Oracle | -9.03 |
| Random | -23.75 |

> 删除 trained-router 行（退化）。

### Death Decomposition → 用 plan-012-full (245 eps)

Δ_full=+29.60, Δ_nd=+2.84, DAF=90.41%, r=0.9698 (p=8.12e-07)

### Keyword Baseline → 用 plan-011 v3

Episode accuracy=23.26%，结构性失效。

### SFT Data → 用 data/plan-004-implicit/implicit_sft.jsonl

2040 samples, 89.7% det / 10.3% internal.

### ⚠️ 绝对不引用

1. `death_decomposition_report.json` 的 30-task 数字
2. `plan005/routing_metrics.json`
3. `results/plan_c_test_labels/` 下任何文件（标签损坏）
4. `death_decomposition_preliminary_OLD.csv`
5. trained-router 结果

---

## 五、数据谱系图

```
plan-001b 实验执行
├── 初始跑 → 194 episodes (11 tasks)  [数据源 C]
│   ├── plan-003: baseline eval (always-int/det/oracle/random)
│   ├── plan-005: routing pattern analysis → 68 episodes with preference
│   │   └── plan-004: implicit_sft.jsonl (2040 samples)
│   └── plan-002: explicit router training (v1-v6, all degenerate except ablation-b)
│
├── rebalance 追加 → +51 episodes → 245 episodes (11 tasks)  [数据源 A]
│   └── plan-012-full: death decomposition (Δ=29.60, daf=90.41%, r=0.9698)
│
prescreening 实验
└── 30 tasks × 5-9 eps → 249 episodes  [数据源 B]
    ├── death_decomposition_report.json (Δ=38.33, daf=98.75%, r=0.9864)
    ├── plan005/routing_metrics.json (混合版)
    └── rule_based_accuracy 各版本
```

---

## 六、遗留问题

1. **Baseline 与 decomposition 的 episode 集不匹配**：baselines (194 eps) 与 decomposition (245 eps) 不在同一 episode 集上。论文若在同一表中呈现，需声明或在 245 eps 上重跑 baselines。
2. **SFT 数据不含追加 episodes**：2040 样本来自 194-episode 子集。扩展到 245 episodes 后训练数据未更新。
3. **无有效 trained-router 结果**：plan-002-formal-v6 退化。plan-004-ablation-b 非退化（internal recall=51.5%）但未做 end-to-end eval。