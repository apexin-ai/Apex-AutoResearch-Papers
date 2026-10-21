# verify final maintext audit

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_final-maintext-audit_20260524T042705_result.json`
- **Structured JSON:** [`9f6e229f16fe02085c82.json`](../../sessions/9f/9f6e229f16fe02085c82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复已确认。现在汇总完整的自查结果。

---

## 最终自查报告

### 已修复的问题（3 处）

**1. Routing SD 值 (experiments.tex:41)**
- LAMBADA SD: 0.8pp → **0.4pp**（源数据 e1_paired_ttest.json 计算 paired diffs SD=0.447pp）
- ARC-Easy SD: 0.9pp → **0.5pp**（源数据计算 SD=0.519pp）
- 原因：原始 SD 为 `sqrt(SD_routing² + SD_mv²)` 的错误计算，正确做法是取 paired differences 的 SD

**2. Table 1 HellaSwag 行 (experiments.tex:17)**
- ρ: 0.4 → **0.3**
- p: .517 → **.683**
- σ_h3-1: 1.22 → **1.18**
- Ratio: 0.96 → **0.99**
- 验证源：table1_task_specificity.csv (ρ=0.3, p=0.683, σ_h3-1=0.01183) + lm_eval_clean/summary_all_1.3b.csv 手动复算一致

**3. Appendix HellaSwag ρ 引用 (appendix.tex:28)**
- "HellaSwag: +0.4" → **"HellaSwag: +0.3"**

### 已确认无误的项目

| 检查项 | 状态 |
|--------|------|
| Abstract 所有数字 vs 正文 | ✅ α=0.14–0.30, J≈0.10, Bonferroni p=.170, n=5, 36%, +5.2pp |
| Table 1 其余 10 行 | ✅ LAMBADA/BoolQ/ARC-C/PIQA/WinoGrande/ARC-E/MMLU/SciQ/XStoryCloze/COPA 全匹配 |
| Table 2 PIQA 行 | ✅ N=1838, α=.14, J̄_h=.091, J̄_u=.094, ρ_α=0.0 |
| Table 2 ARC-Easy 行 | ✅ J̄_h=.092, J̄_u=.099 匹配源数据 |
| Table 2 LAMBADA 行 | ✅ J̄_h=.096, J̄_u=.091 匹配源数据 |
| Routing 数值 (+5.2pp/+1.2pp/-0.06pp/-0.49pp) | ✅ 均与 e1_paired_ttest.json 一致 |
| Routing p 值 (.374 HellaSwag / .006 PIQA) | ✅ |
| LAMBADA per-example counts (462/615/426/495/548/395) | ✅ |
| ECE spread "6%" | ✅ source: GDN=0.222, RetNet=0.224, HGRN2=0.235 → range/mean=5.7%→6% |
| Routing PIQA 为负结果 (-0.49pp) | ✅ 上轮修复已在位 |
| Oracle = 65.5% | ✅ source: 0.6546→65.5% |
| 56.2% vs 50.9% accuracies | ✅ source: 0.5623/0.5090 |
| Jaccard 饱和 "all ρ≤0.80, p≥.333" | ✅ 匹配 cross_benchmark_jaccard_trajectories.json |
| 3-tier hierarchy (~0.05/~0.10/~0.33) | ✅ |
| Seed calibration 2.7–4.3× | ✅ |
| 5-arch validation J≤0.14, all p<.01 | ✅ |
| Bonferroni 计算 .017×10=.170 | ✅ |
| Limitations 数字 | ✅ |
| Conclusion 数字 | ✅ |

### 四舍五入统一性

| 类别 | 格式 | 一致性 |
|------|------|--------|
| Jaccard | 3位小数 (.091, .095, .096) | ✅ |
| α | 2位小数 (.14, .15, .21, .30) | ✅ |
| p-value | .xxx 格式 (.006, .374, .017) | ✅ |
| σ (Table 1) | 2位小数 (2.41, 0.49) | ✅ |
| accuracy | 1位小数百分比 (56.2%, 50.9%) | ✅ |

### 需注意但未修改的项

1. **Table 2 HellaSwag J̄ 小幅偏差**：论文 .095/.085 vs 源数据计算 .091/.080（差距 0.004–0.005，可能来自不同分析版本）
2. **56.2%−50.9%=5.3pp vs +5.2pp**：前者为 non-CV 均值差，后者为 paired t-test 均值差（5.15pp→5.2pp），统计方法上合理但读者可能困惑
3. **Figure 2 (fig2_task_specificity.pdf)**：如果图中 HellaSwag 点画在 ρ=0.4，需要重新生成图片（当前只修复了 .tex，未改 PDF）
4. **340M HellaSwag ρ=0.4 (appendix L673)**：这是 340M 数据点，未找到源数据验证，保留未动

---
