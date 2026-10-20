# audit text consistency

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_text-consistency_20260523T111458_result.json`
- **Structured JSON:** [`b7f91c7db58b08aa2e5d.json`](../../sessions/b7/b7f91c7db58b08aa2e5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All files read. Now performing systematic cross-reference audit.

---

## 数字一致性审计报告

### Ground Truth 提取（experiments.tex Tables 1/2/3）

**Table 1 (cross_model):** exception_only: 99.83/99.83/99.89/99.39 | full_trace: 81.44/77.06/79.9/79.16 | no_trace: 75.13/72.35/76.47/73.36 | Regex B5: 99.33 | Majority: 71.51

**Table 2 (ablation):** exception_only 99.83 | ae_only 99.64 | VOTA 99.05 | loop_only 86.05 | full_trace 81.44 | no_trace 75.13 | Regex best 93.61 | 3-shot 90.84 | Zero-shot 51.0–93.5

**Table 3 (density):** exception_only 99.83 | grad_mask 99.22±0.20 (Δ=−0.61pp) | full_trace 81.76 (matched seed) | label_only 85.94±1.12 (Δ=+4.50pp)

---

### 逐文件扫描结果

#### Abstract (main.tex:22–25)

```
[main.tex:22] "77--82%" → Table 1 full_trace range: 77.06–81.44 → ✅
[main.tex:22] "≥99.33%" → per-seed min (DS S42/456=99.33) → ✅
[main.tex:23] "28.49%" → experiments.tex:123 B5 nomarker=28.49 → ✅
[main.tex:23] "97.65%" → experiments.tex:120 nomarker mean=97.65 → ✅
[main.tex:24] "≤4% of the 18--23pp gap" → 0.61/18.07=3.4%, 18.07–22.77pp range → ✅
```

#### Introduction (introduction.tex)

```
[introduction.tex:15] "77--82%" → Table 1 full_trace 77.06–81.44 → ✅
[introduction.tex:15] "≥99%" → min per-seed 99.33, ≥99% correct → ✅
[introduction.tex:15] "18--23pp gap" → 18.07–22.77pp → ✅
[introduction.tex:17] ">97%" → nomarker 97.65%(7B), 97.82%(1.5B) → ✅
[introduction.tex:19] "≤4%" → ✅
[introduction.tex:26] "≥99.33%" → ✅
```

```
[introduction.tex:28] "69pp" regex drop → B5: 99.33−28.49=70.84pp → ❌ 应为 ~71pp
[introduction.tex:28] "2pp" SFT drop → 99.83−97.65=2.18pp → ⚠️ 四舍五入 (experiments.tex 写 2.18pp)
```

```
[introduction.tex:28] "99.4--100%" cross-dataset → 99.41/100.0 → ✅
[introduction.tex:30] "≥98.53%" → ae_only DS-6.7B=98.53 → ✅
[introduction.tex:30] "(77--86%)" → loop_only 77.40–86.05 → ✅
[introduction.tex:30] "12+pp" → 98.53−86.05=12.48pp → ✅
[introduction.tex:32] "≤4%" → ✅
```

#### Discussion (discussion.tex)

```
[discussion.tex:12] "93--97%" tail-truncated → tail-512: 93.6–98.2%, tail-2048: 95.0–97.9% → ⚠️ 上界偏低 (实际上限 98.2%)
[discussion.tex:22] "97.65%" → ✅
[discussion.tex:22] "28.49%" → ✅
[discussion.tex:22] "63×" → 0.171/0.0027=63.3× → ✅
[discussion.tex:28] "Qwen +10.9pp" → 10.92pp → ✅ (四舍五入)
[discussion.tex:28] "CodeLlama +0.9pp" → 0.93pp → ✅ (四舍五入)
```

```
[discussion.tex:25] "4--9pp of the ~27pp headroom" → full_trace−no_trace 实际范围:
  Qwen-7B: 81.44−75.13=6.31pp
  Qwen-1.5B: 77.06−72.35=4.71pp
  CL-13B: 79.9−76.47=3.43pp
  DS-6.7B: 79.16−73.36=5.80pp
  实际范围 = 3.43–6.31pp → ❌ "9pp" 无数据支撑，上界应为 ~6pp
```

```
[discussion.tex:25] "24--27pp" exception lift → 实际: 23.42(CL)–27.48(1.5B)pp → ⚠️ 下界应为 23pp (CL-13B=23.42pp)
```

#### Conclusion (conclusion.tex)

```
[conclusion.tex:3] "≥99.33%" → ✅
[conclusion.tex:3] "77--82%" → ✅
[conclusion.tex:3] "18--23pp" → ✅
[conclusion.tex:3] "≤4% dilution" → ✅
[conclusion.tex:3] "99.4--100%" → ✅
[conclusion.tex:4] "93--97%" → ⚠️ 同 discussion，上界偏低
```

#### experiments.tex 正文数字

```
[experiments.tex:51] "loop_only spans 8.57pp" → 86.05−77.40=8.65pp → ⚠️ 应为 8.65pp
[experiments.tex:105] "+3.62--23.86pp" SFT vs regex →
  appendix Table regex_cross_format VOTA Δ=+23.50pp (99.05−75.55)
  但 23.86pp = 99.41(S42)−75.55 → ❌ 正文用 S42，附录 Table 用 mean，不一致
```

```
[experiments.tex:46] "0.50pp across architectures" → 99.89−99.39=0.50pp → ✅
[experiments.tex:97] "+0.78pp" exc vs VOTA → 99.83−99.05=0.78pp → ✅
[experiments.tex:100] "12.48pp" → 98.53−86.05=12.48pp → ✅
[experiments.tex:101] "+10.92pp/+7.19pp/+6.95pp/+0.93pp" → 86.05−75.13/79.54−72.35/80.31−73.36/77.40−76.47 → ✅
[experiments.tex:103] "6.22pp" SFT−B4 → 99.83−93.61=6.22pp → ✅
[experiments.tex:108] "42.44pp range" → 93.45−51.01=42.44pp → ✅
[experiments.tex:108] "1.76pp" 3-shot improvement → 90.84−89.08=1.76pp → ✅
[experiments.tex:109] "0.50pp (99.39--99.89%)" → ✅
[experiments.tex:120] "2.18pp" → 99.83−97.65=2.18pp → ✅
[experiments.tex:122] "~9%" marker contribution → 2.18/24.70=8.8%≈9% → ✅
[experiments.tex:122] "24.70pp" → 99.83−75.13=24.70pp → ✅
[experiments.tex:124] "4.04pp" → 97.65−93.61=4.04pp → ✅
[experiments.tex:134] "18.07pp" → 99.83−81.76=18.07pp → ✅
[experiments.tex:138] "≤4%" → 0.61/18.07=3.4% → ✅
[experiments.tex:167] "+4.50pp" → 85.94−81.44=4.50pp → ✅
[experiments.tex:167] "≤26%" → 4.50/18.07=24.9%, ≤26% → ✅
[experiments.tex:170] "≤0.3% dilution of 20.23pp gap" → DS: 99.39−79.16=20.23pp; 99.39−99.33=0.06pp; 0.06/20.23=0.30% → ✅
[experiments.tex:196] "ECE = 0.0027 vs 0.171, 63×" → 0.171/0.0027=63.3× → ✅
```

#### Appendix 内部一致性

**❌ 两个 calibration 表报告相同数据 (exception_only, seed 42) 的 ECE 值不一致：**

| Model | Table calibration_model_level (L820) | Table calibration_cross (L586) |
|-------|-------------------------------------|-------------------------------|
| Qwen-1.5B | ECE=0.0014 | ECE=0.0020 |
| Qwen-7B | ECE=0.0017 | ECE=0.0027 |
| CL-13B | ECE=0.0020 | ECE=0.0020 |
| DS-6.7B | ECE=0.0048 | ECE=0.0064 |

主文 Table calibration (L557) Qwen-7B ECE=0.0027 与 calibration_cross 一致，与 calibration_model_level 矛盾。

→ **experiments.tex:197 "all four models achieve ECE < 0.005"**: 若以 calibration_model_level 为准 (max=0.0048) 则 ✅；若以 calibration_cross 为准 (DS=0.0064) 则 ❌

**❌ per_class 表 (appendix L1–31) 声称 seed 42 但 3 个条目使用了 multi-seed mean：**

| Condition | per_class Acc | Full results S42 | Full results Mean |
|-----------|--------------|-------------------|-------------------|
| VOTA | 99.05 ❌ | 99.41 | 99.05 |
| loop_only | 86.05 ❌ | 85.63 | 86.05 |
| Full Trace (LO) | 85.94 ❌ | 86.22 | 85.94 |

这 3 个条目的 Acc 列使用的是 3-seed mean 而非 seed 42 值。此外 VOTA 的 P/R 值隐含 Acc≈99.41%，与报告的 99.05% 矛盾。

**❌ appendix regex_cross_format 表与同段文字不一致：**
```
[appendix.tex:765] 文字: "VOTA (+23.86pp)" → 99.41(S42)−75.55
[appendix.tex:780] 表格: "VOTA +23.50pp" → 99.05(mean)−75.55
```

---

### 汇总

| 类别 | 数量 |
|------|------|
| 总共核对跨文件引用 | **52** |
| ✅ 一致 | **42** |
| ❌ 不一致 | **7** |
| ⚠️ 格式/精度问题 | **5** |

#### ❌ 不一致项（需修复）

1. **introduction.tex:28** — "69pp" regex drop → 实际 99.33−28.49=**70.84pp**，应改为 ~71pp
2. **discussion.tex:25** — "4--9pp" full_trace lift → 实际 3.43–6.31pp，上界 9pp 无数据支撑，应改为 ~3–6pp
3. **experiments.tex:105 + appendix.tex:765** — "+23.86pp" 使用 VOTA S42 (99.41)，但 appendix Table regex_cross_format 用 mean (99.05) 得 +23.50pp，两处应统一
4. **appendix per_class 表** — VOTA/loop_only/label_only 三行 Acc 列使用 3-seed mean 而非声明的 seed 42 值
5. **appendix 两个 calibration 表** — calibration_model_level vs calibration_cross 对同一数据报告不同 ECE 值（DS-6.7B: 0.0048 vs 0.0064），导致 "ECE < 0.005" claim 在一个表中不成立
6. **experiments.tex:197** — "all four models achieve ECE < 0.005" 依赖 calibration_model_level 表，但 calibration_cross 表显示 DS-6.7B ECE=0.0064>0.005
7. **discussion.tex:25** — "24--27pp" exception lift → CL-13B 为 23.42pp，下界应为 ~23pp

#### ⚠️ 格式/精度问题

1. **introduction.tex:28** — "2pp" vs experiments.tex "2.18pp"（四舍五入但差 0.18pp）
2. **discussion.tex:12 / conclusion.tex:4** — "93--97%" tail-truncated → 实际上限达 98.2%（tail-512 CL-13B），应为 93–98%
3. **experiments.tex:51** — "8.57pp" loop_only span → 实际 86.05−77.40=8.65pp（差 0.08pp）
4. **experiments.tex:108** — zero-shot max "93.5%" → 实际 93.45%（四舍五入）
5. **introduction.tex:28** — "2pp" 与同文件后文 contribution list 没有精确数字，而 experiments.tex 写 2.18pp

---
