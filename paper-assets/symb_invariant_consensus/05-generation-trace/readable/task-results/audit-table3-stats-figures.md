# audit table3 stats figures

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table3-stats-figures_20260523T104426_result.json`
- **Structured JSON:** [`479fafa2b8943d055e26.json`](../../sessions/47/479fafa2b8943d055e26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Audit complete. Here is the full report.

---

## 审计报告：Table 3 + 统计检验 + Figure 数据核查

---

### 任务 A: Table 3 (tab:cross_generator_nli) — Cross-Generator NLI Combo

**Table 位置**: solutions.tex (主表), appendix.tex line 959 tab:nli-combo-full (完整版 Table 28)

#### Mistral-7B
```
  声称值: SC=39.33%, Gap=+15.67, Δ(w=3)=+6.67pp, p<0.001
  实际值: SC=39.33% (236/600), deberta w3 Δ=6.67pp, p=1.13e-05
  来源: file=results/r11_3verifier_canonical.json
  状态: ✅ 完全匹配
```

#### LLaMA-3.1-8B
```
  声称值: SC=72.50%, Gap=-17.50, Δ(w=3)=+0.83pp, p=0.665
  实际值: SC=70.00% (420/600), w3 Δ=+3.33pp, p=0.0519
  来源: file=results/exp092_llama8b_pw_nli_combo/results.json
  状态: ❌ CRITICAL — SC baseline 差 2.5pp (15题)
```
**详细说明**: Combo accuracy 完全匹配 (w1=73.33%, w3=73.33%, w5=72.0%)，但 SC baseline 不一致。论文用 SC=72.50% 计算 Δ=+0.83pp，实际 SC=70.0% → 真实 Δ=+3.33pp (是论文声称值的 **4倍**)。p 值从 0.665 变为 0.0519 (接近显著)。**这改变了论文核心结论 "all generators with SC ≥ 72% show no significant improvement"**。

#### Qwen2.5-14B
```
  声称值: SC=74.00%, Gap=-19.00, Δ(w=3)=+0.67pp, p=0.503
  实际值: SC=73.50% (441/600), w3 Δ=+1.17pp, p=0.2295
  来源: file=results/qwen14b_pw_nli_combo/results.json
  状态: ⚠️ SC baseline 差 0.5pp (3题), Δ和p均受影响
```

#### Qwen3-14B
```
  声称值: SC=85.83% (515/600), w3 combo=86.33%, Δ=+0.50pp, p=0.45
  实际值: SC=85.00% (510/600), w3 combo=86.00%, Δ=+1.0pp, p=0.146
  来源: file=results/d116_qwen3_pw_deberta_large/results.json
  状态: ⚠️ SC和combo都对不上 (5题 SC差, 2题 combo差), 可能使用了不同实验run
```

#### 根因分析
LLaMA 和 Qwen14B 的 combo accuracy 与数据文件完全一致，但 SC baseline 系统性偏高。可能原因：论文用 K=12 traces 统一重算了 SC baseline，但 combo 仍使用原始 (可能 K=10/11) traces 计算。如果属实，**Δ 是从不匹配的 baseline 计算的**，属于方法论错误。

---

### 任务 B: 新增数字核查

#### 94.4% MAX-SAT vs count-only agreement
```
  声称值: "MAX-SAT produces answers identical to count-only on 94.4% of problems on Mistral-7B FOLIO (Table tab:ablation)"
  实际值:
    - tab:ablation 实际内容: Qwen2.5-14B n=804 (不是 Mistral-7B FOLIO!)
    - alpha_ablation (Mistral-7B FOLIO): agreement = 99-100% at all α
    - 94.4% 在任何 results 文件中均未找到
  来源: analysis.tex:15, appendix.tex:399 (tab:ablation)
  状态: ❌ 双重错误
    (1) 交叉引用错误 — 文本说 Mistral-7B FOLIO, 表格是 Qwen2.5-14B n=804
    (2) 94.4% 无数据来源 — alpha_ablation 显示 99-100%
```

#### 90.8% argmax agreement
```
  声称值: (用户要求核查)
  实际值: 论文 LaTeX 中未出现 "90.8"
  来源: r17_argmax_br_metrics.json 个体值: 87.25%-97.55%, 均值=91.27%
  状态: N/A — 该数字不在论文中
```

#### 94% error overlap (analysis.tex:15)
```
  声称值: "94% of errors overlap with SC"
  实际值: 待验证 — 需要对比 SICA error set 与 SC error set
  来源: 原始数据在 intermediates/ 文件中
  状态: ⚠️ 未独立验证
```

---

### 任务 C: 统计检验核查

#### TOST equivalence tests
```
  声称值: ±2pp margin → 4 equivalent, 2 genuinely different, 10 underpowered
  验证: Appendix TOST sensitivity table (line 817-828) 内部一致
         ±1pp → 0/2/14; ±3pp → 10/2/4
  来源: experiments.tex:57, appendix.tex:807-832
  状态: ✅ 内部一致 (无独立 result file 交叉验证)
```

#### BH correction (3-verifier, m=15)
```
  声称值: "Ten of 15 conditions remain significant" (α=0.05)
  实际值: r11_3verifier_canonical.json → bh_correction.n_significant = 10
  来源: file=results/r11_3verifier_canonical.json
  状态: ✅ 匹配
```

#### BH correction (cross-generator, m=12)
```
  声称值: "Two of twelve conditions survive" (Mistral w=3 and w=5)
  验证: Appendix Table 28 显示 Mistral w3 p_BH=6.78e-5, w5 p_BH=7.42e-6
  注意: 此表使用的 SC baseline 可能有误 (见 Task A)
  状态: ⚠️ 内部一致，但依赖于可能错误的 SC baseline
```

#### Bootstrap CI (CCR Spearman ρ)
```
  声称值: ρ=0.839, 95% CI [0.338, 0.990]
  实际值: ρ=0.8389, CI [0.3375, 0.9902]
  来源: file=results/cil_bootstrap_loo.json
  状态: ✅ 匹配 (四舍五入)
```

#### Bootstrap CI (SICA Δ)
```
  声称值 (tab:bootstrap):
    - Qwen-14B FOLIO+PW (n=804): Δ=+0.25pp, CI [-1.12, +1.62]
    - LLaMA-8B StrategyQA (n=200): Δ=+2.00pp, CI [-1.50, +5.50]
    - LLaMA-8B FOLIO (n=204): Δ=-4.41pp, CI [-5.88, +0.98]
  来源: 无独立 result file 可交叉验证
  状态: ⚠️ 无法独立验证
```

---

### 任务 D: Figure 数据核查

**实际 Figure 编号** (from main.aux):
- Figure 1: Pipeline
- Figure 2: Interventions (fig:interventions-summary) — 不是 "SICA vs SC scatter"
- Figure 3: Regime scatter (fig:regime-scatter) — SICA Δ vs SC
- Figure 4: Process-kappa (fig:process-kappa) — 不是 "interventions"
- Figure 7: Capability gap (fig:capability-gap)

#### Figure 2 (Interventions)
```
  声称值: "23 of 27 strategies shown" (caption), "All 27 produce neutral-to-negative" (text)
  验证: 内部一致 (4 omitted for clarity)
  来源: figures/fig2_interventions_compact.pdf
  状态: ⚠️ 需要视觉核查各 strategy Δ 值 — 无法远程读取 PDF 数据点
```

#### Figure 3 (Regime scatter — SICA Δ vs SC)
```
  声称值: 散点图数据应与 Table 1 的 (SC%, SICA%) 对一致
  状态: ⚠️ 需要视觉核查 — 数据点无法从 PDF 提取验证
```

#### Figure 7 (Capability gap scatter)
```
  声称值: Spearman ρ=1.0, p=0.003, n=6
  验证: n=6, ρ=1.0 → 精确排列 p ≈ 1/360 = 0.0028 ≈ 0.003 ✅
  注意: 该图使用的 Gap 值依赖于 Table 3 的 SC baseline — 如果 SC baseline 有误，Gap 值也错
  来源: figures/capability_gap_scatter.pdf
  状态: ⚠️ ρ=1.0 统计上合理，但依赖于可能错误的 SC baseline
```

---

### 汇总

| 优先级 | 问题 | 严重度 |
|--------|------|--------|
| 1 | **LLaMA SC baseline 70.0% vs 72.50%** → Δ 从 +3.33pp 变成 +0.83pp，影响核心结论 | ❌ CRITICAL |
| 2 | **94.4% MAX-SAT agreement 无数据来源** + tab:ablation 交叉引用错误 | ❌ CRITICAL |
| 3 | Qwen3-14B SC 和 combo 均与 d116 文件不匹配 | ⚠️ HIGH |
| 4 | Qwen2.5-14B SC baseline 73.50% vs 74.00% | ⚠️ MEDIUM |
| 5 | Figure 7 Gap 值依赖于可能错误的 SC baseline | ⚠️ MEDIUM |
| 6 | Bootstrap SICA Δ 无独立 result file 验证 | ⚠️ LOW |

**建议优先修复 #1 和 #2**。LLaMA SC baseline 问题可能波及 tab:nli-combo-full (Table 28)、Figure 7、以及 BH cross-generator 校正。需要确认所有 generator 的 SC baseline 来自相同 K=12 trace set 并与 combo 使用相同 traces。

---
