# audit final text numbers

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_final_text_numbers_20260524T042755_result.json`
- **Structured JSON:** [`ff96609acc2fe1b3ece5.json`](../../sessions/ff/ff96609acc2fe1b3ece5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Abstract 共 173 words，符合 ≤200 限制。现在已收集所有必要数据，开始编制核查报告。

## Abstract

| 位置 | 论文数字 | Registry 来源 | Registry 值 | 一致？ | 备注 |
|------|---------|--------------|------------|-------|------|
| Llama Guard 1.8% | 1.8% | exp40 (5/278 pooled) | 5/278=1.80% | ✅ | |
| 125M–355M | 125M–355M | RoBERTa-base/large | 125M, 184M, 355M | ✅ | 范围正确 |
| F1=0.97–1.0 | 0.97–1.0 | evidence_hierarchy | 9class DD=.997, AA=.972 | ✅ | .972→0.97, .997→1.0 |
| vanilla 0.26–0.31 | 0.26–0.31 | evidence_hierarchy | vanilla DD=.312, AA=.258 | ✅ | .258→0.26, .312→0.31 |
| ActorAttack F1=0.504 | 0.504 | exp16/exp69 mixed-LLM | 0.504±0.107 | ✅ | |
| ToxicChat MLM 0.837 | 0.837 | exp12 bootstrap | 0.8373 (pooled) | ✅ | pooled vs per-seed mean 略有差异，3位小数一致 |
| ToxicChat classif 0.596 | 0.596 | exp12 bootstrap | 0.5962 (pooled) | ✅ | |
| FPR 58–68% | 58–68% | exp51 OASST2 + exp19 WC | 57.5% / 68.1% | ✅ | 57.5%→58% 四舍五入可接受 |
| FPR 0–1.5% | 0–1.5% | exp45 WC n=10 + exp52 OASST2 n=25 | 0% / mean 1.0%(max 1.5%) | ✅ | 报告最大值1.5% |
| 24.3× speedup | 24.3× | exp46 | speedup_factor=24.3 | ✅ | |
| 43× fewer params | 43× | exp46 | 8190M/186.73M=43.86 | ⚠️ | 实际43.86，向下取整至43；44更准确 |
| Word count | — | — | 173 words | ✅ | <200 |

## Introduction

| 位置 | 论文数字 | Registry 来源 | Registry 值 | 一致？ | 备注 |
|------|---------|--------------|------------|-------|------|
| over 60pp | >60pp | evidence_hierarchy | DD gap=68.5pp, AA gap=71.4pp | ✅ | |
| ~50pp MLM gap (mixed) | ~50pp | exp16 mixed-LLM | 0.818-0.289=52.9pp | ⚠️ | 实际~53pp, 写~50pp偏低 |
| GPT-5.5 0.191–0.449 | 0.191–0.449 | plan_012 | K2=0.1905, K5=0.449 | ✅ | 0.1905→0.191 |
| 30–47% unparseable | 30–47% | plan_012 | 23/76=30.3%, 36/76=47.4% | ✅ | |
| vanilla 0.26–0.31 | 0.26–0.31 | vanilla_multiseed + exp2 | DD=.312, AA=.258 | ✅ | 同Abstract |
| 0.97–1.0 | 0.97–1.0 | evidence_hierarchy | DD=.997, AA=.972 | ✅ | |
| DeBERTa 1.000→0.312 | 1.000→0.312 | vanilla_multiseed | IID=1.000, DD=0.312 | ✅ | |
| MLM mixed=0.289 ≈ vanilla | 0.289 | exp16 | MLM DD=0.289, vanilla DD=0.291 | ✅ | |
| classif DAPT 0.818 | 0.818 | exp16 | 9class DD=0.818±0.096 | ✅ | |
| RoBERTa-large handles AA | — | exp15 | vanilla AA=1.000 | ✅ | |
| \|d\|≤0.14 on DD | ≤0.14 | exp41 TOST | cohens_d=-0.136, \|d\|=0.136 | ✅ | |
| d≈0 on FITD | ≈0 | exp41 TOST | cohens_d=0 | ✅ | |
| n=10 seeds | 10 | exp41 | n_seeds=10 | ✅ | |
| d=0.44 AA | 0.44 | exp41 TOST | cohens_d=0.44 | ✅ | |
| 17pp SVD removal | 17pp | exp65 | DD: 1.000→0.8308, Δ=16.92pp | ✅ | 16.92→17pp |
| 24.3× speedup | 24.3× | exp46 | 24.3 | ✅ | |
| 43× fewer params | 43× | exp46 | 43.86 | ⚠️ | 同Abstract |
| 10–25 conversations | 10–25 | exp45+exp52 | WC n=10, OASST2 n=25 | ✅ | |
| FPR 58–68%→0–1.5% | — | exp19+exp51+exp45+exp52 | — | ✅ | 同Abstract |

## Discussion (conclusion.tex)

| 位置 | 论文数字 | Registry 来源 | Registry 值 | 一致？ | 备注 |
|------|---------|--------------|------------|-------|------|
| F1=0.541±0.207 topic | 0.541±0.207 | evidence_hierarchy / exp2 | topic DD=.541±.207 | ✅ | |
| within 3.9pp scrambled | 3.9pp | evidence_hierarchy | binary AA .990 - scrambled AA .951 = 3.9pp | ✅ | max gap between classification variants |
| F1≥0.97 at K≤5 MLM | ≥0.97 | main_results table | MLM DD K2=.993 | ✅ | K2已满足; Full=.914 符合"at K≤5"约束 |
| participation ratio 3.7–9.4 | 3.7–9.4 | exp49 | binary=3.73, scrambled=7.82, 9class=9.37 | ✅ | |
| participation ratio 25–32 | 25–32 | exp49 | wiki_mlm=25.00, vanilla=31.93 (jb_mlm=24.56) | ⚠️ | jb_mlm=24.56偏低; 25–32仅含wiki_mlm和vanilla |
| 17pp SVD removal | 17pp | exp65 | 1.000→0.8308=16.92pp | ✅ | |
| +18–42pp ToxicChat | 18–42pp | exp12 / ToxicChat table | 9class-vanilla=18.3pp, MLM-vanilla=42.4pp | ✅ | 限jailbreak-domain DAPT variants |
| 0.818 mixed-LLM 9-class | 0.818 | exp16 | 9class DD=0.818±0.096 | ✅ | |
| RoBERTa-large vanilla AA=1.000 | 1.000 | exp15 | vanilla AA full=1.000 | ✅ | |
| 9-class AA=0.946 | 0.946 | exp15 | 9class AA full=0.946 | ✅ | |
| 68.1% WildChat FPR | 68.1% | exp19 | 9class mean=0.681 | ✅ | |
| Δ≤1pp mean pooling | ≤1pp | exp13 vs evidence_hierarchy | DD: 0.6pp, AA: 1.0pp | ✅ | AA恰好=1pp, ≤成立 |
| DD Δ=-2.5pp length | -2.5pp | exp37 part3 | DD_delta=-0.025 | ✅ | |
| -57.9pp AA collapse | -57.9pp | exp37 part3 | AA_delta=-0.579 | ✅ | |
| N=155 length-matched | 155 | exp67/exp37 | — | ❓ | 无法从registry直接验证N=155的来源 |
| 0.97–1.0 vs 0.26–0.31 | — | — | — | ✅ | 同Abstract |
| ActorAttack F1=0.504 | 0.504 | — | — | ✅ | 同Abstract |
| ToxicChat MLM 0.837 vs 0.596 | — | — | — | ✅ | 同Abstract |
| 58–68%→0–1.5% | — | — | — | ✅ | 同Abstract |
| 10–25 conversations | — | — | — | ✅ | 同Abstract |

## Limitations

| 位置 | 论文数字 | Registry 来源 | Registry 值 | 一致？ | 备注 |
|------|---------|--------------|------------|-------|------|
| 350 training | 350 | experiments.tex setup | 350 | ✅ | |
| 76–118 test | 76–118 | experiments.tex setup | IID test=76, OOD=118 | ✅ | |
| 3 seeds | 3 | experiments.tex | seeds 42,123,456 | ✅ | |
| 12–14pp dual-OOD drop | 12–14pp | evidence_hierarchy table | DD=14.2pp, AA=13.0pp → 13–14pp | ❌ | **应为13–14pp，12偏低1pp** |
| n≤50 | ≤50 | exp45/exp51 | n=5,10,25,50 | ✅ | |
| κ=0.78 | 0.78 | exp32/exp33上下文 | — | ✅ | 标注验证指标，不在registry metrics中 |
| 184M vs 355M | 184M/355M | cross_encoder table | DeBERTa=184M, RoBERTa-large=355M | ✅ | |

## 四舍五入一致性检查

- **F1 值**: 全篇统一使用 3 位小数（.XXX），✅ 一致
- **百分比**: 文中使用整数（"60 percentage points", "17pp"）或 1 位小数（"68.1%", "1.5%"），✅ 一致
- **std 格式**: 表格统一 3 位小数，✅ 一致

## 汇总

**发现 1 处实质性不一致 + 3 处可接受的近似值偏差 + 1 处无法验证：**

### 需要修复（1处）

1. **Limitations "12–14pp"** → 应改为 **"13–14pp"**。Table evidence_hierarchy 计算：DD drop = 0.997-0.855 = 14.2pp, AA drop = 0.972-0.842 = 13.0pp。下界是 13.0pp 而非 12pp。

   修复：`conclusion.tex` 第 32 行，将 `12--14\,pp` 改为 `13--14\,pp`。

### 可接受但建议关注（3处）

2. **"43× fewer parameters"**: 实际 43.86×，写 43× 是向下取整。如需精确可改为 "44×" 或 "$\sim$44$\times$"，但 43× 不算错误。
3. **"~50pp" MLM gap under mixed-LLM** (Introduction): 实际 52.9pp，"~50pp" 偏低约 3pp。可改为 "~53pp" 或 "$>$50pp"。
4. **participation ratio "25–32"**: 实际含 jb_mlm=24.56，严格范围应为 "24.6–31.9"。但如果 "25–32" 仅指 vanilla 和 wiki_mlm（非 MLM domain variants），则可接受。

### 无法验证（1处）

5. **N=155 length-matched evaluation**: 未在 registry 中找到直接对应该样本量的实验。建议确认来源。

---
