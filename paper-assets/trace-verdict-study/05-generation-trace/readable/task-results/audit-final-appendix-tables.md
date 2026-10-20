# audit final appendix tables

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_final-appendix-tables_20260523T191706_result.json`
- **Structured JSON:** [`c1382d13434b72a9625e.json`](../../sessions/c1/c1382d13434b72a9625e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Audit complete. Here is the full report.

---

## Appendix Tables 5–23 数据审计报告

**核对范围**: 19 个数据表, ~250+ 个数值单元格
**数据源**: registry (36 experiments), table1_final.json, regex_baseline_results.json, debugbench_results.json, cross_model_calibration_results.json/txt, trace_ablation_bootstrap.json, calibration_metrics_summary.txt

---

### ❌ 必须修复 (4 issues)

**Issue 1: tab:per_class — 3 行 Acc 列用了 3-seed mean, P/R/F1 用 seed42**

Caption 标注 "seed 42"，但 VOTA/loop_only/Full Trace (LO) 的 Acc 列是 3-seed mean：

| Row | Acc(论文) | 来源 | Acc(seed42) | P/R/F1验算→Acc |
|-----|----------|------|-------------|---------------|
| VOTA, Qwen-7B | 99.05 | 3-seed mean | 99.41 | Pass R=99.18 → 7 errors → **99.41** |
| loop_only, Qwen-7B | 86.05 | 3-seed mean | 85.63 | Pass R=87.07 + Fail R=82.01 → 171 errors → **85.63** |
| Full Trace (LO), Qwen-7B | 85.94 | 3-seed mean | 86.22 | Pass R=93.18 + Fail R=68.73 → 164 errors → **86.22** |

修复方案：将这 3 行的 Acc 改为 seed42 值 (99.41/85.63/86.22)。

---

**Issue 2: VOTA regex Δ 三处不一致**

| 位置 | 值 | 来源 |
|------|---|------|
| tab:regex_cross_format (appendix table) | Δ=+23.50 | 99.05(3-seed) − 75.55 |
| appendix text (§B.10 inline) | +23.86 | 99.41(seed42) − 75.55 |
| experiments.tex line 105 | "+3.62–23.86pp" | same seed42 calc |

表和正文自相矛盾。修复方案：统一为 +23.50 (与表一致，用 3-seed mean) 或全改为 +6.22 (exception_only) 作为 max Δ 并重述。

---

**Issue 3: 两个 calibration 表 ECE 值不同**

tab:calibration_cross (§B.8) 和 tab:calibration_model_level (§C.1) 报告了同一组实验的不同 ECE：

| Model | tab:calibration_cross ECE | tab:calibration_model_level ECE | 差异 |
|-------|--------------------------|-------------------------------|------|
| Qwen-1.5B | 0.0020 | 0.0014 | −0.0006 |
| Qwen-7B | 0.0027 | 0.0017 | −0.0010 |
| DeepSeek-6.7B | 0.0064 | 0.0048 | −0.0016 |
| CodeLlama-13B | 0.0020 | 0.0020 | 0.0000 |

数据溯源：tab:calibration_cross 来自 cross_model_calibration_results.txt (bins 0.5–1.0)；tab:calibration_model_level 来自 plan019 run (不同 bin 配置)。

修复方案：统一 bin 配置，保留一个表删除另一个，或在 caption 明确标注 bin 差异。

---

**Issue 4: Qwen-7B tail-256 两表数值不一致**

| 表 | 值 |
|----|---|
| tab:trace_length (§B.7) | 77.48 |
| tab:tail_cross_model (§B.7) | 78.9 |

同一实验 (Qwen-7B, seed=42, N=1190) 不应有两个不同数值。78.9 可能误用了 head-256 (78.82→78.8)。

修复方案：核实原始 eval 结果，统一为正确值。

---

### ⚠️ 需确认 (4 items)

| # | 位置 | 问题 | 详情 |
|---|------|------|------|
| 5 | tab:calibration, full_trace ECE | 0.096 vs raw 0.0946 | 0.0946 at 3dp = 0.095, not 0.096 |
| 6 | tab:tail512_seeds, Qwen-7B σ | 2.05 vs computed 2.03 | 微小差异，可能由于显示精度 |
| 7 | tab:tail_cross_model, CL exc_only | 99.89 (3-seed mean) | 其他列均为 seed42，此处混用 |
| 8 | tab:density, grad mask 3-seed | mean=99.22±0.20 | seed123 registry 状态 PREPARING，未见结果 |

---

### ✅ 已验证一致 (全部表)

| Table | 内容 | 核对数 | 结果 |
|-------|------|--------|------|
| tab:full_qwen | Qwen-7B 全条件全 seed | 24 cells | ✅ mean/std 全部正确 |
| tab:full_deepseek | DS-6.7B 全条件全 seed | 16 cells | ✅ |
| tab:exc_subcomponent | 3 子成分 ablation | 12 cells | ✅ registry 完全匹配 |
| tab:trace_length | Head-truncation 4 条件 | 8 cells + CIs | ✅ bootstrap JSON 完全匹配 |
| tab:trace_length_pairwise | 12 对 pairwise bootstrap | 48 cells | ✅ JSON 精确匹配 |
| tab:tail512_seeds | 4 模型 ×3 seed at tail-512 | 20 cells | ✅ (σ 微偏 ⚠️) |
| tab:head_vs_tail | 4 模型 head vs tail | 9 cells | ✅ gaps 精确 |
| tab:calibration | Qwen-7B 5 条件 calibration | 10 cells | ✅ (full_trace ECE ⚠️) |
| tab:calibration_cross | 4 模型 cross-model cal | 12 cells | ✅ 与 raw data 匹配 |
| tab:exception_type | 10 类异常分类准确率 | 20 cells | ✅ 样本总和=1190 |
| tab:dedup | 去重统计 | 9 cells | ✅ 比例精确 |
| tab:regex | 6 regex baselines | 8 cells | ✅ JSON 完全匹配 |
| tab:regex_cross_format | 4 格式 SFT vs regex | 12 cells | ✅ Δ 算术正确 |
| tab:zeroshot_cross_model | 4 模型 zero-shot vs SFT | 16 cells | ✅ 范围/Δ 正确 |
| tab:debugbench | DebugBench 3 条件 | 8 cells | ✅ JSON 完全匹配 |
| tab:hyperparams | 超参数 | config | ✅ (非数据) |
| tab:train_time | 训练时间 | config | ✅ (非数据) |

---

### 主文↔Appendix 引用一致性

| 主文引用 | 值 | Appendix 值 | 状态 |
|----------|---|-------------|------|
| ECE 63× gap (experiments.tex:198) | 0.171/0.0027=63.3 | tab:calibration | ✅ |
| All ECE<0.007 (experiments.tex:199) | ref tab:calibration_model_level | 0.0014–0.0048 | ✅ |
| "+3.62–23.86pp" (experiments.tex:105) | — | tab:regex_cross_format max Δ=23.50 | ❌ |
| nomarker 97.65±0.96 (experiments.tex:120) | — | 无 appendix 表 | ✅ (自洽) |
| Cross-dataset 99.41% N=4270 (experiments.tex:127) | — | 无 appendix 表 | ✅ |
| Tier boundary 12.48pp (experiments.tex:100) | 98.53−86.05 | tab:cross_model | ✅ |

---

### 汇总

| 类别 | 数量 |
|------|------|
| 核对总数 | ~250 cells |
| ✅ 一致 | ~240 |
| ❌ 必须修复 | **4** (per_class 3行 Acc, VOTA Δ 矛盾, 2个 calibration 表, tail-256 矛盾) |
| ⚠️ 需确认 | **4** (rounding/labeling/registry gap) |

4 个 ❌ 都是同类问题：**seed42 vs 3-seed mean 混用**或**不同运行结果未统一**。建议在 DDL 前统一数据源并 one-pass 替换。

---
