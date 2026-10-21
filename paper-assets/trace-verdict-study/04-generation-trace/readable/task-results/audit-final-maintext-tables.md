# audit final maintext tables

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_final-maintext-tables_20260523T191655_result.json`
- **Structured JSON:** [`ca593dbf58c12589c1a8.json`](../../sessions/ca/ca593dbf58c12589c1a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已就绪。开始逐项核对。

---

## 数据审计报告

### 一、Abstract 6 个核心数字

```
[Abstract] "77--82%" → Table 1 full_trace 4 models means: 77.06/79.16/79.9/81.44
  → range = 77.06--81.44 → ⚠️ 上界 81.44 ≈ 81，非 82；82.35 仅为 Qwen-7B 单 seed 最大值

[Abstract] "≥99.33%" → DS seed42=99.33, seed456=99.33 (全模型全 seed 最低)
  → registry: DS seeds 99.33/99.50/99.33 → ✅

[Abstract] "28.49%" → regex_nomarker_baseline: B5_nomarker_acc=0.2849 → ✅

[Abstract] "97.65%" → nomarker 3-seed: 96.55/98.32/98.07, mean=97.647 → ✅

[Abstract] "≤4%" → 0.61pp / 18.07pp = 3.37% → ✅ (前提是 grad mask mean=99.22)
  → ⚠️ 但 registry 3 seeds 均为 99.33 (见 Table 3 详细核对)

[Abstract] "12pp" → SFT 99.83 − GPT-4o 87.98 = 11.85pp ≈ 12pp → ✅
  → GPT-4o 来源: fewshot_gpt4o_exception_only_0shot: 0.8798 → ✅
```

### 二、Table 1 (cross_model) 逐格核对

**exception_only 行：**
```
[T1] Qwen-7B  99.83±0.00 → seeds 99.83/99.83/99.83 → ✅
[T1] Qwen-1.5B 99.83±0.00 → seeds 99.83/99.83/99.83 → ✅
[T1] CL-13B   99.89±0.10 → seeds 99.83/100.00/99.83, mean=99.89, std=0.098≈0.10 → ✅
[T1] DS-6.7B  99.39±0.10 → seeds 99.33/99.50/99.33, mean=99.39, std=0.098≈0.10 → ✅
```

**ae_only 行：**
```
[T1] Qwen-7B  99.64±0.49 → seeds 99.92/99.08/99.92, mean=99.64, std=0.49 → ✅
[T1] Qwen-1.5B 98.83±0.36 → seeds 99.08/98.57 (2-seed), mean=98.83, std=0.36 → ✅
[T1] CL-13B   99.08±0.00 → seeds 99.08/99.08, identical → ✅
[T1] DS-6.7B  98.53±0.30 → seeds 98.74/98.32 (2-seed), mean=98.53, std=0.30 → ✅
```

**VOTA 行：**
```
[T1] Qwen-7B  99.05±0.38 → seeds(v5) 99.41/98.66/99.08, mean=99.05, std=0.38 → ✅
[T1] Qwen-1.5B 99.54±0.06 → seeds 99.58/99.50 (2-seed), mean=99.54, std=0.06 → ✅
[T1] CL-13B   98.74±0.24 → seeds 98.57/98.91 (2-seed), mean=98.74, std=0.24 → ✅
[T1] DS-6.7B  99.25‡ (2-seed) → seeds(excl 42) 99.16/99.33, mean=99.25 → ✅
```

**loop_only 行：**
```
[T1] Qwen-7B  86.05±0.52 → seeds 85.63/85.88/86.64, mean=86.05, std=0.526≈0.52 → ✅
[T1] Qwen-1.5B 79.54±1.42 → seeds 78.32/81.09/79.20, mean=79.54, std=1.42 → ✅
[T1] CL-13B   77.40±1.54 → seeds 77.06/76.05/79.08, mean=77.40, std=1.54 → ✅
[T1] DS-6.7B  80.31±1.65 → seeds 81.26/81.26/78.40, mean=80.31, std=1.65 → ✅
```

**full_trace 行：**
```
[T1] Qwen-7B  81.44±1.11 → seeds 81.76/80.20/82.35, mean=81.44, std=1.11 → ✅
[T1] Qwen-1.5B 77.06† → registry qwen15b_full_trace_seed42=0.7706 → ✅
[T1] CL-13B   79.9§ → registry codellama13b_head2048_seed42=0.7992≈79.9 → ✅
[T1] DS-6.7B  79.16† → registry deepseek_full_trace_seed42_v3=0.7916 → ✅
```

**no_trace 行：**
```
[T1] Qwen-7B  75.13† → registry no_trace_seed42_v5=0.7513 → ✅
[T1] Qwen-1.5B 72.35±4.48 → seeds 67.31/75.88/73.87, mean=72.35, std=4.48 → ✅
[T1] CL-13B   76.47† → registry=0.7650, 但 910/1190=0.76471 → ⚠️ registry 四舍五入，论文值正确
[T1] DS-6.7B  73.36† → registry deepseek_no_trace_seed42=0.7336 → ✅
```

**Baselines：**
```
[T1] Regex B5 99.33 → registry B5=0.9933 → ✅
[T1] Majority 71.51 → registry=0.7151 → ✅
```

### 三、Table 2 (ablation) 核对

```
[T2] ae_only      99.64†  CI[99.26,99.87] Tier 1 → mean=99.64 ✅
[T2] exception_only 99.83 CI[99.58,100.00] Tier 1 → 99.83 ✅
[T2] VOTA         99.05§  CI[98.49,99.50]        → mean=99.05 ✅
[T2] VOTA_no_ae   99.41   CI[98.90,99.80]        → registry=0.9940→99.40, 论文99.41 → ⚠️ 微小四舍五入
[T2] loop_only    86.05‡  CI[83.97,87.96] Tier 2 → mean=86.05 ✅
[T2] full_trace   81.44±1.11                      → mean=81.44 ✅
[T2] no_trace     75.13   CI[72.77,77.48]        → 75.13 ✅
[T2] Regex (best) 93.61                           → B4=0.9361 ✅
[T2] 3-shot       90.84                           → fewshot_qwen7b=0.9084 ✅
[T2] Zero-shot    51.0--93.5                      → CL=51.01, Q1.5B=93.45 ✅
```

### 四、Table 3 (density decomposition) 核对

```
[T3] exception_only  99.83±0.00           → ✅
[T3] +grad mask      99.22±0.20  Δ−0.61pp → ❌ registry 3 seeds 均为 99.33±0.00
     论文 seeds "98.99/99.33/99.33" → mean=99.22, std=0.20（内部一致）
     但 registry gradient_masking_qwen7b_seed{42,123,456} 均记录 accuracy=0.9933
     seed42 注明 "metrics empty (None conclusion)"，可能原始值为 98.99 但被覆盖
     → ≤4% 结论不受影响 (0.61/18.07=3.4% 或 0.50/18.07=2.8%)，但具体数值需确认

[T3] full_trace      81.76‡    Δ−18.07pp → seed42_v5=0.8176 ✅
     脚注 "3-seed mean 81.44%±1.11"    → ✅

[T3] label-only      85.94±1.12 Δ+4.50pp → seeds 86.22/86.89/84.70, mean=85.94, std=1.12 ✅
     Δ vs full_trace: 85.94−81.44=4.50pp → ✅
```

### 五、正文引用数字交叉核对

**Introduction：**
```
[Intro] "77--82%" complete traces → range 77.06--81.44 → ⚠️ 同 Abstract
[Intro] "≥99%" exception_only → min across means = 99.39 → ✅
[Intro] "18--23pp gap" → exc−full_trace: 18.39/22.77/19.99/20.23 → range 18--23 → ✅
[Intro] "71pp" regex drop → 99.33−28.49=70.84≈71 → ✅
[Intro] ">97%" SFT nomarker → 97.65% → ✅
[Intro] "99.4--100%" cross-dataset → HE→MBPP=99.41, MBPP→HE=100.0 → ⚠️ MBPP→HE 无 registry 数据
[Intro] "≤4%" gradient dilution → ✅
[Intro] "≥99.33%" → ✅
[Intro] "23--27pp" exception lift → lifts: 24.70/27.48/23.42/26.03 → range 23--27 ✅
```

**Experiments：**
```
[Exp §3.1] "spanning only 0.50pp" exc_only cross-model → 99.89−99.39=0.50 → ✅
[Exp §3.1] "loop_only spans 8.57pp" → 86.05−77.40=8.65pp → ⚠️ 应为 8.65 非 8.57
[Exp §3.1] "σ=4.48pp" no_trace → Qwen-1.5B no_trace std=4.48 → ✅
[Exp §3.2] "ae_only on DeepSeek, 98.53%±0.30" → ✅
[Exp §3.2] "loop_only on Qwen-7B, 86.05%" → ✅
[Exp §3.2] "12.48pp" → 98.53−86.05=12.48 → ✅
[Exp §3.2] "Qwen +10.92pp(7B) +7.19pp(1.5B); DS +6.95pp; CL +0.93pp" →
            86.05−75.13=10.92 ✅; 79.54−72.35=7.19 ✅; 80.31−73.36=6.95 ✅; 77.40−76.47=0.93 ✅
[Exp §3.2] B4 "93.61%" → ✅
[Exp §3.2] "trailing by 6.22pp" → 99.83−93.61=6.22 → ✅
[Exp §3.2] "+3.62--23.86pp" → ⚠️ VOTA gap 用 seed42(99.41)=23.86 而非 3-seed mean(99.05)=23.50
            no_trace +3.62 ✅; full_trace +4.37 ✅; exc +6.22 ✅
[Exp §3.2] "Zero-shot spans 51.0--93.5% (42.44pp range)" → 93.45−51.01=42.44 → ✅
[Exp §3.2] "3-shot ICL (90.84%) improves only 1.76pp" → 90.84−89.08=1.76 → ✅
[Exp §3.2] "SFT compresses to 0.50pp (99.39--99.89%)" → ✅
[Exp §3.2] "6--49pp gap" → 6.38--48.88 → 6--49 → ✅
[Exp §3.2] "GPT-4o (84.45%)" no_trace → registry=0.8445 → ✅
[Exp §3.2] "GPT-4.1 (77.31%)" no_trace → registry=0.7731 → ✅
[Exp §3.2] "SFT 99.83% vs GPT-4o 87.98%" → ✅
[Exp §3.3] "97.65% ± 0.96 (seeds 96.55/98.32/98.07)" → ✅
[Exp §3.3] "Qwen-1.5B: 97.82%, drop of 2.01pp" → registry=97.80 → ⚠️ 97.82 vs 97.80
[Exp §3.3] "~2pp accounts for ~9% of 24.70pp" → 2.18/24.70=8.8%≈9% → ✅
[Exp §3.3] "B5 99.33% collapses to 28.49%" → ✅
[Exp §3.3] "SFT nomarker 97.65% exceeds B4 by 4.04pp" → 97.65−93.61=4.04 → ✅
[Exp §3.3] "HE→MBPP 99.41% (N=4,270)" → registry=0.9941 → ✅
[Exp §3.3] "MBPP→HE 100.0% (N=1,640)" → ⚠️ registry 无存储指标，不可验证
[Exp §3.3] "no_trace: 70.56% vs 69.02% majority" → registry=0.7056/0.6902 → ✅
[Exp §3.3] "67.99% vs 61.65%" MBPP→HE no_trace → ⚠️ 不可验证
[Exp §3.3] "cross-dataset drops to 95.5% (−3.9pp)" → 95.46≈95.5, 99.41−95.46=3.95≈3.9 → ✅
[Exp §3.4] "18.07pp gap (99.83% vs 81.76%)" → ✅
[Exp §3.4] "99.22% (mean −0.61pp)" → ❌ 同 Table 3 issue
[Exp §3.4] "≤4% of 18.07pp" → ✅ (无论用 0.61 还是 0.50)
[Exp §3.4] "label-only +4.50pp" → ✅
[Exp §3.4] "DS 99.33%, CL 100% under masking" → registry ✅
[Exp §3.5] "1024-token (77.23%) vs 512-token (80.42%, p=.002)" → ✅
[Exp §3.5] "no-limit 81.76%" → ✅
[Exp §3.5] "tail-2048 exceeds head-2048 by 15.5--22.6pp" → 15.5/22.6/16.3 → ✅
[Exp §3.5] "+13.2--22.0pp" at 384→512 → 13.7/13.2/15.5/22.0 → ✅
[Exp §3.5] "[93.61%, 98.24%]" tail-512 all seeds → ✅
[Exp §3.5] "2--5pp residual gap" → max gap=4.33pp(DS) → ⚠️ 上界应为 ~4 而非 5
[Exp §3.5] "ECE=0.0027 vs 0.171, 63×" → 0.171476/0.002717=63.1 → ✅
[Exp §3.5] "ECE < 0.007" all models → max=0.0064(DS) → ✅
```

**Discussion：**
```
[Disc] "3--6pp full_trace lift" → lifts: 6.31/4.71/3.43/5.80 → range 3.4--6.3 ≈ 3--6 → ✅
[Disc] "23--27pp exception lift" → lifts: 24.70/27.48/23.42/26.03 → ✅
[Disc] "97.65% under marker removal" → ✅
[Disc] "28.49%" regex collapse → ✅
[Disc] "63× better calibration" → ✅
```

**Conclusion：**
```
[Conc] "≥99.33%" → ✅
[Conc] "77--82%" → ⚠️ 同 Abstract
[Conc] "18--23pp" → ✅
[Conc] "≤4% dilution" → ✅
[Conc] "99.4--100%" cross-dataset → ⚠️ MBPP→HE 不可验证
[Conc] "93--98%" tail fallback → tail-512 range 93.6--98.2 → ✅
```

### 六、Appendix 数据核对

```
[App full_qwen] exception_only S42/123/456=99.83 all → ✅
[App full_qwen] ae_only S42=99.92 S123=99.08 S456=99.92, mean=99.64±0.49 → ✅
[App full_qwen] VOTA S42=99.41 S123=98.66 S456=99.08, mean=99.05±0.38 → ✅
[App full_qwen] label_only S42=86.22 S123=86.89 S456=84.70, mean=85.94±1.12 → ✅
[App full_qwen] loop_only S42=85.63 S123=85.88 S456=86.64, mean=86.05±0.52 → ✅
[App full_qwen] full_trace S42=81.76 S123=80.20 S456=82.35, mean=81.44±1.11 → ✅
[App full_deepseek] exception_only 99.33/99.50/99.33 → ✅
[App full_deepseek] VOTA 84.45/99.16/99.33 → ✅

[App per_class] "Full Trace (LO)" acc=85.94 → ❌ 表标注 seed 42，但 85.94 是 3-seed mean；
               seed42 实际值=86.22 (registry: full_trace_label_only_seed42=0.8622)
               F1 值来自 seed42 (pass_f1=0.9063, fail_f1=0.7397 ✓)，仅 accuracy 错误

[App calibration] ECE/Brier (Qwen-7B conditions) → 与 registry 一致 ✅
[App calibration_cross] 4 models ECE → 与 registry cross_model_calibration_eval 一致 ✅
[App calibration_model_level] → ❌ 与 calibration_cross 表数值冲突：
     Qwen-1.5B: 0.0014 vs 0.0020
     Qwen-7B:   0.0017 vs 0.0027
     DS-6.7B:   0.0048 vs 0.0064
     两表均标注 "seed 42, N=1190"，但 ECE 值不同，疑为不同 bin 策略或计算版本
```

### 七、精度统一性

```
主表 (T1/T2/T3): 一般 2 位小数 (99.83, 98.53 等)
CL full_trace: 79.9 (1 位) → ⚠️ 其他 cell 均 2 位
Appendix tail tables: 1 位小数 (78.9, 93.6 等) → 与主表不同但可接受
ECE/Brier: 小数位数不一（0.0004 vs 0.005）→ 可接受
```

---

## 汇总

| 类别 | 数量 |
|------|------|
| 核对总数 | ~85 项 |
| ✅ 一致 | 72 |
| ⚠️ 轻微/可讨论 | 10 |
| ❌ 需修复 | 3 |

### ❌ 需修复（3 项）

1. **Table 3 gradient masking 99.22±0.20**：Registry 3 seeds 均记录 99.33，mean 应为 99.33±0.00。论文 seeds "98.99/99.33/99.33" 内部自洽，但与 registry 不符。seed42 registry 注明 "metrics empty"，可能原始值 98.99 被后续覆写。需确认 seed42 实际值。≤4% 结论不受影响。

2. **Appendix per_class 表 "Full Trace (LO)" accuracy**：表标注 seed 42，但 accuracy=85.94 是 3-seed mean（seed42 实际为 86.22）。应改为 86.22。

3. **Appendix 两个 calibration 表 ECE 数值冲突**：tab:calibration\_cross 和 tab:calibration\_model\_level 对同一模型同一条件报告不同 ECE（如 Qwen-7B: 0.0027 vs 0.0017），两表均标注 seed 42 / N=1190。需统一或标注计算方法差异。

### ⚠️ 需关注（10 项）

1. **"77--82%"**：Table 1 mean 范围 77.06--81.44，严格说应为 77--81%。82% 仅为单 seed 最大值。
2. **"loop_only spans 8.57pp"**：实际 86.05−77.40=8.65pp。
3. **"+3.62--23.86pp"**（SFT vs regex）：VOTA gap 23.86 用 seed42(99.41) 非 3-seed mean(99.05)=23.50。
4. **"2--5pp" tail residual gap**：最大实际 gap 仅 4.33pp(DS)，非 5pp。
5. **Qwen-1.5B nomarker "97.82%"**：Registry=97.80%（0.02pp 差）。
6. **MBPP→HE 100.0% / 67.99%**：Registry 无存储指标，不可从 registry 验证。
7. **CL no_trace 76.47 vs registry 76.50**：Registry 四舍五入，论文值 910/1190=76.47 正确。
8. **cross-dataset nomarker "95.5%"**：实际 95.46%。
9. **VOTA_no_ae 99.41 vs registry 99.40**：1183/1190=99.41%，registry 四舍五入。
10. **CL full_trace "79.9"**（1 位小数）：其他 cell 均 2 位。

---
