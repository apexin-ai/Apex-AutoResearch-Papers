# analysis exp 024 audit discrepancies

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_024_audit_discrepancies_20260517T132239_result.json`
- **Structured JSON:** [`4535ee7bd63ce25e21f7.json`](../../sessions/45/4535ee7bd63ce25e21f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完成。以下是排查报告。

---

## 排查报告

### 差异 1: LP range 0.041 vs 0.060

**原因：mean vs median 混淆**

- 主文 "median LP range = 0.041 nats"（discussion.tex:41, appendix.tex:486）→ 正确，是 **median**
- T ablation 表（appendix.tex:1000）LP range = 0.060 → 实际是 **mean**，但 caption（appendix.tex:992）写的 "LP range: median within-instance range"，**caption 错了**

验证（gold-filtered, n=529）：

| T | 表中值 | mean（实际） | median（实际） |
|---|--------|-------------|---------------|
| 0.5 | 0.022 | 0.022 | 0.015 |
| 0.8 | 0.043 | 0.043 | 0.031 |
| 1.0 | 0.060 | 0.059 | 0.042 |
| 1.2 | 0.075 | 0.073 | 0.058 |

表中值完全匹配 mean，来源是 `exp026_temp_ablation_metrics.py` 的 `lp_range_mean` 字段。

**数据来源**：主文 0.041 来自 `analyze_lp_range_cdf.py`，使用 `exp_012_rerun_1024` 数据。T ablation 表来自 `exp026_temp_ablation_metrics.py`，使用 `exp_012_logprob` 数据。

**修复建议**：将 T ablation 表改用 median 值（0.015, 0.031, 0.042, 0.058），保持 caption 中的 "median"。这样 T=1.0 行与主文 0.041 一致（差 0.001 是数据源差异）。同时更新 appendix.tex:984 中 "LP range increases from 0.022 to 0.075 nats" 为 "from 0.015 to 0.058"。

---

### 差异 2: Degeneracy 17.6% vs 17.8%

**原因：不同的 generation run**

- 主文 17.8% = `exp_012_rerun_1024`（94/529, constant-F1 gold-filtered）
- T ablation 表 17.6% = `exp_012_logprob`（93/529, constant-F1 gold-filtered）
- 同一 checkpoint（ft_002_v2），同一定义，但不同推理 session → 采样随机性导致 1 个实例差异

跨 seed 验证：

| 数据源 | Degeneracy |
|--------|-----------|
| exp_001_seed42_v2 | 18.9% |
| exp_001_seed123_v2 | 18.7% |
| exp_001_seed456_v2_ner | 18.1% |
| exp_012_rerun_1024 | **17.8%** ← 主文 |
| exp_022_seed789 | 18.0% |
| exp_012_logprob | **17.6%** ← T ablation 表 |

全部在 17.6%–18.9% 范围内，0.2pp 差异在正常采样波动范围内。

**修复建议**：T ablation 表的 T=1.0 行应使用 `exp_012_rerun_1024` 数据（与主文一致），将 17.6 改为 17.8。

---

### 具体修改方案

**appendix.tex** 中 T ablation 表（约 line 1000）：

```
% 当前: 1.0 & 17.6 & 0.060 & 0.405 & 0.700 \\
% 改为: 1.0 & 17.8 & 0.041 & 0.405 & 0.700 \\
```

同时需要将其他行的 LP range 也改为 median：
- T=0.5: 0.022 → 0.015
- T=0.8: 0.043 → 0.031
- T=1.2: 0.075 → 0.058

如果改 median 影响过大（正文多处引用 0.022/0.075），**替代方案**：仅改 caption 从 "median" 为 "mean"，并在 T=1.0 行保持 0.060（但需要在正文讨论 LP range 对比时注明 0.041 是 median 而 Table 用 mean）。这个方案改动小但逻辑不够干净。

Fleiss' κ 和 SJ mean 需要使用 `exp_012_rerun_1024` 重新计算（当前 0.405/0.700 来自 exp_012_logprob）。

---
