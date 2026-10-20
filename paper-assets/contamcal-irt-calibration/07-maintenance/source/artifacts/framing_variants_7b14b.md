# Framing Variants: 7B/14B Results

> 目的：结果出来后 15 分钟内决定走哪条路。每个 variant 有明确触发条件和论文调整模板。

---

## 触发指标定义

| 指标 | 来源 | 计算方式 |
|------|------|----------|
| Deltacc | d000 vs d100 accuracy per benchmark | raw accuracy shift (pp) |
| gamma_k | per-benchmark 2PL+gamma IRT fit (pooled up to 14B) | posterior mean + 95% CI |
| RRF tau | Kendall's tau between RRF-ranked theta and clean theta | pooled across dosages |
| S2/S4 AUC | Min-K++/perplexity signal discriminability at 7B/14B | per-dosage AUC |

---

## Variant A: Null 持续

### 触发条件（全部满足）
- 7B/14B aggregate Deltacc <= 1.5pp on MMLU, ARC, GSM8K
- gamma_k 95% CI includes 0 for majority of benchmarks at 7B/14B scale
- RRF tau >= 0.55 (theta ranking preservation intact)
- MMLU domain-level pattern consistent with <=3B (STEM gamma > 0, non-STEM misfit)

### Title
保留当前：**"Does SFT-Injected Benchmark Contamination Need Calibration? An IRT Decomposition from 0.5B to 14B"**
- 仅将 scope 从 "<=3B" 升级到 "0.5B to 14B"

### Abstract 关键句模板
- "Across five model scales (0.5B to 14B) and three benchmarks, SFT-injected contamination produces negligible aggregate accuracy shifts (<=1.5pp at scales >=1.5B), even at 100% dosage."
- "Our IRT decomposition reveals that this aggregate null masks structured heterogeneity: STEM domains show significant positive gamma while non-STEM domains exhibit model misfit, a pattern stable from 1.5B to 14B."
- "The scale-invariance of this null finding suggests that SFT-route contamination may not warrant post-hoc score calibration for aggregate benchmarking."

### Introduction C1/C2/C3 调整要点
- **C1 (Characterization)**: 升级 scope, domain heterogeneity confirmed across 0.5B-14B. 新增 scale-invariance finding: STEM gradient persists at 7B/14B. 如果 Llama-3.1-8B 也 null, 加 cross-family invariance claim
- **C2 (Signal Failure)**: 检查 Min-K++ 在 7B/14B 方向. 如果正常化: "scale-dependent signal reliability: reversal at <=1.5B, recovery at >=7B". 如果仍 reverse: 更强 cautionary finding
- **C3 (Identifiability)**: N 增加 (+12-16 models) 更接近 N>=30. 如果 coverage improves, 支持 "N was the bottleneck" narrative

### Results 新增 Section Outline
- **Section: Scale Invariance Analysis**
  - Table: Deltacc by scale (0.5B / 1.5B / 3B / 7B / 14B) x benchmark x dosage
  - Figure: gamma_k vs model scale (flat line = scale invariance)
  - MMLU domain gamma at 7B/14B vs <=3B comparison
  - Statistical test: Kruskal-Wallis on gamma across scales (p > 0.05 = no scale effect)

### Discussion 新增 Talking Points
- Scale-invariance implies SFT contamination is a data-level property, not a capacity-level phenomenon
- 与 pre-training contamination 区分: SFT injection exposure 机制不同于 web-scale pre-training, null finding 不能直接推广
- Practical implication: for SFT-route contamination, investing in detection may have higher ROI than calibration
- 与 Emperor's New Clothes (ICML 2025) 呼应: mitigation strategies fail, but calibration may also be unnecessary for SFT-route

### 与现有 Claims 兼容性
| Claim | 状态 | 调整 |
|-------|------|------|
| Aggregate null (<=3B) | **保留 + 强化** | scope 扩展到 <=14B |
| MMLU Simpson's paradox | **保留** | 验证 7B/14B 一致性 |
| ARC forgetting | **保留** | 检查 7B/14B 是否仍 forgetting 或转为 null |
| Min-K++ reversal | **保留或修改** | 取决于 7B/14B signal behavior |
| N>=50 recommendation | **保留** | N 增加缩小 gap 但可能仍 < 50 |
| GSM8K as negative control | **保留** | 应在 7B/14B 继续 null |
| "calibration is conditionally possible" | **保留** | 加 "but may be unnecessary for SFT-route" |
| gamma as diagnostic only | **保留** | gamma 继续 diagnostic role |

---

## Variant B: 效应增大

### 触发条件（任一满足）
- 7B 或 14B 任一 benchmark Deltacc > 2pp (非 0.5B capacity artifact)
- gamma_k 95% CI excludes 0 for 7B/14B on >=2 benchmarks (new, not present at <=3B)
- MMLU aggregate gamma becomes significantly non-zero at 7B/14B (Simpson's paradox resolves)
- ARC forgetting reverses to inflation at 7B/14B

### 灰色地带判断规则
- 1.5pp < Deltacc < 2.5pp: 需结合 gamma CI 和 effect size 综合判断
- gamma CI barely excludes 0: 用 Bayes factor 或 ROPE 辅助判断
- 仅 14B 有效应但 7B 没有: framing 为 "transition threshold between 7B and 14B"
- Effect size (Cohen's d) vs <=3B: 翻倍以上 lean Variant B, 增加 <50% lean Variant A with caveats

### Title
- **Option 1**: "SFT-Injected Benchmark Contamination Shows Scale-Dependent Transition: An IRT Decomposition from 0.5B to 14B"
- **Option 2 (更保守)**: "Does SFT-Injected Benchmark Contamination Need Calibration? Scale-Dependent Effects Revealed by IRT Decomposition"

### Abstract 关键句模板
- "While SFT-injected contamination produces negligible aggregate accuracy shifts at scales <=3B (<=1pp), we observe a qualitative transition at larger scales: 7B/14B models show [X]pp shifts on [benchmark], with IRT gamma estimates whose credible intervals exclude zero."
- "This scale-dependent transition suggests that larger models' increased capacity enables more effective exploitation of memorized benchmark content."
- "Our IRT decomposition framework captures this transition, providing both scale-conditional calibration and a diagnostic decomposition of when contamination begins to matter."

### Introduction C1/C2/C3 调整要点
- **C1 (Characterization, reframed)**: 从 "aggregate null masks domain heterogeneity" 变为 "scale-dependent transition with domain modulation". 核心 finding: contamination effects negligible below capacity threshold, then emerge. MMLU domain pattern 可能变化:
  - STEM gradient 增强: "larger models amplify STEM-specific memorization"
  - non-STEM 也出现 gamma > 0: "capacity enables broader domain exploitation"
  - Simpson's paradox 消失: "domain effects converge at scale"
- **C2 (Signal Failure)**: 如果 S2/S4 在 7B/14B 恢复有效, signal reliability 也 scale-dependent. RRF 在 7B/14B 可能真正 multi-signal (S1+S2+S4)
- **C3 (Identifiability)**: 更多 models, better identifiability. 如果 gamma 在 7B/14B 更容易 identify: "larger effects improve statistical identifiability"
- **C4 (Calibration, PROMOTED back to co-primary)**: 从 demoted 升级. Calibration value proposition 变强: "without calibration, 7B/14B scores overestimate by [X]pp"

### Results 新增 Section Outline
- **Section: Scale-Dependent Contamination Transition**
  - Table: Deltacc by scale x benchmark x dosage (highlight transition point)
  - Figure: gamma_k vs model scale (inflection curve, not flat line)
  - Critical scale identification: at what parameter count does effect emerge?
  - 如果 7B null 但 14B positive: transition between 7B-14B
  - 如果 7B 已 positive: transition between 3B-7B
- **Section: Calibration at Scale** (if calibration becomes necessary)
  - MAE improvement at 7B/14B vs <=3B (should be larger if effect is larger)
  - Coverage analysis with increased N

### Discussion 新增 Talking Points
- **Capacity hypothesis (谨慎表述)**: larger models may have sufficient capacity to both retain general abilities AND exploit memorized benchmark items. 用 "consistent with" 不用 "demonstrates". 不能 overclaim causality
- **Mechanism ambiguity**: 效应增大可能因为 (a) 更大模型更好地 memorize SFT data, (b) 更大模型对 fine-tuning 的 capacity overhead 更大, (c) 分布偏移效应与 scale 交互. 这些无法区分, 必须 acknowledge
- **SFT =/= pre-training**: SFT injection 的 exposure 机制不同于 web-scale pre-training. 即使 SFT-route 在 7B/14B 有效应, 不能直接推广到 pre-training contamination. 标注为 future work
- **Practical implications shift**: 从 "calibration may be unnecessary" 变为 "calibration becomes increasingly important at larger scales, precisely where contamination is hardest to detect"
- **Emperor's New Clothes 重定位**: 从 "mitigation fails but doesn't matter" 变为 "mitigation fails AND it matters at scale, calibration is the remaining option"

### 与现有 Claims 兼容性
| Claim | 状态 | 调整 |
|-------|------|------|
| Aggregate null (<=3B) | **保留但限定 scope** | "at scales <=3B" not "in general" |
| MMLU Simpson's paradox | **保留或修改** | 取决于 7B/14B aggregate gamma |
| ARC forgetting | **保留或修改** | 如果 7B/14B ARC 转为 inflation: "scale-dependent direction reversal" |
| Min-K++ reversal | **保留但限定** | "at small scales" |
| N>=50 recommendation | **保留** | 更多 models help |
| GSM8K as negative control | **可能需删除** | 如果 7B/14B GSM8K 有效应 |
| "calibration is conditionally possible" | **升级** | "calibration is necessary at scale AND feasible" |
| gamma as diagnostic only | **升级** | gamma 变为 quantitative measure of scale-dependent effect |

---

## 决策流程

```
7B/14B results arrive
         |
         v
   Deltacc across benchmarks?
         |
    +----+----+
  <=1.5pp    >2pp (any benchmark)
    |         |
    v         v
 gamma CI     Variant B
 includes 0?
    |
  Yes (majority)
    |
    v
 Variant A
```

灰色地带 (1.5-2.5pp or gamma CI marginal):
1. 计算 Bayes factor for gamma != 0
2. 对比 7B vs 3B effect size (Cohen's d)
3. Effect size 翻倍以上: lean Variant B
4. Effect size 增加 <50%: lean Variant A with caveats

---

## 两个 Variant 共享的不变部分

无论哪个 variant, 以下不变:
- IRT framework (2PL+gamma / 4PL+gamma)
- Fisher Information identifiability analysis
- Measurement error model
- Signal evaluation methodology (AUC mapping)
- 6-metric evaluation protocol
- SFT injection experimental design
- Baseline comparisons (7 baselines)
- Related Work, Method sections 的大部分结构
- Appendix 结构

主要变化集中在: Abstract, Introduction (framing + contributions), Results, Discussion, Conclusion
