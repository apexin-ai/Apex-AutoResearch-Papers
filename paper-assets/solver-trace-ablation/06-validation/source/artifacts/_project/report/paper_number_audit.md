# 数字审计报告

## 汇总
- 总数字数: 127
- 匹配: 119 (✅)
- 不匹配: 1 (⚠️)
- 无法追溯: 7 (❓)

---

## 逐项

### abstract.tex

| 数字 | 来源实验 | Registry 值 | 状态 |
|------|----------|------------|------|
| 93% prove rate | plan001-s42-r2 | eval_prove_rate=0.93 | ✅ |
| 87% conclusion embedding | plan001-s42-r2 | h1_rate=0.871 → 87.1% | ✅ |
| ISR=1 / ISR=0 | 定义 | N/A | ✅ |
| ISR 0.642 | plan003 | proved_only_isr=0.6423 | ✅ |
| ISR 0.003 | plan016 | isr=0.003 (paper_framing: 0.0027) | ✅ |
| 99.5% degradation | 计算 | (0.642-0.003)/0.642=99.53% | ✅ |
| PR 32% | plan003 | prove_rate=0.32 | ✅ |
| PR 96% | plan016 | prove_rate=0.96 | ✅ |
| 100 to 1000 steps | plan003/plan016 | 100步/1000步 | ✅ |
| Qwen3-4B | 模型名 | N/A | ✅ |
| 92.9% genuine (SFT) | plan009-sft-s42-r4 | genuine_rate=0.929 | ✅ |
| β=0.1, 64.5% H7 | plan002-b01 3-seed | 149/231=64.5% | ✅ |
| 0% random H7 | plan018 3-seed | 0/256=0% | ✅ |
| 1.06× premise-matched | paper_framing D051 | 0.2578/0.2434=1.059 | ✅ |
| β=0.3 PR 18% | plan002-b03-s42 | 无 eval 指标 | ❓ |
| β=0.3 random PR 48% | plan017 | eval_prove_rate=0.48 | ✅ |
| 3/3 Prolog gaming, 0% genuine | plan006-prolog-sta 3-seed | s42:0%, s43:0%, s44:0% | ✅ |
| 6 reward conditions | 实验设计 | 6 条件 | ✅ |
| 2 logic types | 实验设计 | FOL + Prolog | ✅ |
| 3 seeds | 实验设计 | 42, 43, 44 | ✅ |
| 7 hacking modes | taxonomy | 7 种 | ✅ |

### introduction.tex

| 数字 | 来源实验 | Registry 值 | 状态 |
|------|----------|------------|------|
| 93% prove rate | plan001-s42-r2 | eval_prove_rate=0.93 | ✅ |
| 87% conclusion embedding | plan001-s42-r2 | h1_rate=0.871 | ✅ |
| ISR 0.642→0.132→0.003 | plan003/plan001-s42-r2/plan016 | 0.6423/0.1324/0.003 | ✅ |
| 99.5% degradation | 计算 | 同上 | ✅ |
| PR 32%→96% | plan003/plan016 | 0.32/0.96 | ✅ |
| 94.8% ISR=0 at 1000 steps | plan016 | 无此细项 (registry 仅记录 isr=0.003) | ❓ |
| PR std ±0.47 (exec-only 3-seed) | 计算 | (93,14,98)→σ=47.1pp | ✅ |
| 92.9% genuine SFT | plan009-sft-s42-r4 | genuine_rate=0.929 | ✅ |
| β=0.1, 64.5% H7 | plan002-b01 3-seed | 149/231=64.5% | ✅ |
| 0% random H7 | plan018 3-seed | 0/256 | ✅ |
| 1.06× | D051 | 0.2578/0.2434 | ✅ |
| β=0.3 PR 18% | plan002-b03-s42 | 无 eval 指标 | ❓ |
| β=0.3 random PR 48% | plan017 | eval_prove_rate=0.48 | ✅ |
| Prolog s42 ISR*=0.037 | plan006-prolog-exec-s42 | proved_only_isr=0.037 | ✅ |
| Prolog s43 ISR*=0.015 | plan006-prolog-exec-s43-r3 | proved_only_isr=0.015 | ✅ |
| Prolog s44 ISR*=0.387, n=21 | plan006-prolog-exec-s44 | proved_only_isr=0.3866, n_proved=21 | ✅ |
| ~16% genuine residual (FOL) | ISR β=0.1 3-seed | (30.9+3.3+13.5)/3=15.9% | ✅ |
| **"<16% under any RL condition"** | **多实验** | **Random β=0.1 mean=18.7%; ISR s42=30.9%** | **⚠️** |
| 7 hacking strategies | taxonomy | 7 | ✅ |
| 0.642→0.132→0.003 (结论贡献1) | 同上 | 同上 | ✅ |
| SFT 92.9% genuine | plan009-sft-s42-r4 | genuine_rate=0.929 | ✅ |
| 1.06× (贡献2) | D051 | 同上 | ✅ |
| 3/3 Prolog gaming 0% genuine (贡献3) | plan006-prolog-sta | 同上 | ✅ |

### related_work.tex

| 数字 | 来源 | 状态 |
|------|------|------|
| 无定量实验数字 | — | ✅ |

### method.tex

| 数字 | 来源 | 状态 |
|------|------|------|
| ISR ∈ [0,1] | 定义 | ✅ |
| n+1 solver calls | 定义 | ✅ |
| K=8 rollouts | 实验配置 | ✅ |
| β ∈ {0.1, 0.3} | 实验配置 | ✅ |
| 7 hacking modes | taxonomy | ✅ |

### experiments.tex

| 数字 | 来源实验 | Registry 值 | 状态 |
|------|----------|------------|------|
| 500-example FOLIO subset | 数据配置 | train_500_seed42.jsonl (C001) | ✅ |
| 500 steps / 1000 steps | 训练配置 | — | ✅ |
| 3 seeds (42,43,44) | 训练配置 | — | ✅ |
| K=8 | 训练配置 | — | ✅ |
| 100 held-out eval set | eval 配置 | n_problems=100 | ✅ |
| **Fig.2 caption: 6.58→18.55 components** | plan003→plan016 | plan016: 18.55 ✅; plan003: 无 component count | ❓ (6.58) |
| Fig.2 caption: 94.8% ISR=0 | plan016 | 无此细项 | ❓ |
| 100 steps PR=32%, ISR*=0.642 | plan003 | prove_rate=0.32, proved_only_isr=0.6423 | ✅ |
| 500 steps PR=93%, ISR=0.132 | plan001-s42-r2 | eval_prove_rate=0.93, proved_only_isr=0.1324 | ✅ |
| 87.1% H1 at 500 steps | plan001-s42-r2 | h1_rate=0.871 | ✅ |
| 1000 steps PR=96%, ISR=0.003 | plan016 | prove_rate=0.96, isr=0.003 | ✅ |
| H1=100% at 1000 steps | plan016 | h1_rate=1.0 | ✅ |
| Components 6.58→18.55 | plan003/plan016 | plan016: 18.55 ✅; plan003: 无 | ❓ (6.58) |
| s42 exec: PR=93%, H1=87.1% | plan001-s42-r2 | ✅ | ✅ |
| s43 exec: PR=14%, ISR=0.000, 87% max-len | plan001-s43-r4 | PR=0.14, ISR=0 ✅; 87% max-len 无 | ❓ (87%) |
| s44 exec: PR=98%, H7=100%, comp=2.04 | plan001-s44 | PR=0.98, h7_rate=1, comp=2.04 | ✅ |
| PR σ=±47pp | 计算 | (93,14,98)→σ=47.1 | ✅ |
| SFT PR=14%, ISR*=0.571 | plan009-sft-s42-r4 | eval_prove_rate=0.14, proved_only_isr=0.571 | ✅ |
| SFT 92.9% genuine (13/14) | plan009-sft-s42-r4 | genuine_count=13, genuine_rate=0.929 | ✅ |
| SFT H1=1/14 (7.1%), H7=0 | plan009-sft-s42-r4 | h1_count=1, h1_rate=0.071, h7_count=0 | ✅ |

**Table 1 (goodhart-landscape):**

| 行 | 数字 | Registry 验证 | 状态 |
|---|------|--------------|------|
| Base 0-shot | PR=12% | sta-phase0-baseline: prove_rate=0.12 | ✅ |
| SFT | PR=14, ISR*=0.571, H7=0, H1=7, Gen=93 | plan009-sft: 全部匹配 | ✅ |
| Exec-only | PR=93, ISR*=0.132, H7=0, H1=87, Gen=13 | plan001-s42-r2: 全部匹配 | ✅ |
| ISR β=0.1 | PR=77±14, H7=65, H1=17, Gen≈16 | 3-seed计算: mean=77, σ=14; H7=149/231=64.5%→65%; H1 per-seed mean=17.3%→17; Gen≈15.9%→16 | ✅ |
| Random β=0.1 | PR=85±6, ISR*=0.086±.039, H7=0, H1=81, Gen=19 | 3-seed: PR mean=85.3→85, σ=5.5→6; ISR*=0.086; H1=81.3→81; Gen=18.7→19 | ✅ |
| ISR β=0.3 | PR=18, ISR*=0.143 | plan002-b03: 无 eval 指标 | ❓ |
| Random β=0.3 | PR=48, ISR*=0.094 | plan017: PR=0.48, ISR*=0.0943→0.094 | ✅ |

**Table 2 (beta01-3seed):**

| 行 | 数字 | Registry 验证 | 状态 |
|---|------|--------------|------|
| s42 ISR | PR=81, ISR*=0.415, H7=16.0, H1=51.9, Gen=30.9 | plan002-b01-s42: PR=0.81, ISR*=0.4154, H7=0.16, H1=0.519, Gen=0.309 | ✅ |
| s43 ISR | PR=61, ISR*=0.830, H7=96.7, H1=0, Gen=3.3 | plan002-b01-s43: PR=0.61, ISR*=0.8301, H7=0.967 | ✅ |
| s44 ISR | PR=89, ISR*=0.902, H7=86.5, H1=0, Gen=13.5 | plan002-b01-s44: PR=0.89, ISR=0.803/0.89=0.902, H7=0.865 | ✅ |
| ISR mean | 77±14 | (81+61+89)/3=77, σ=14.2 | ✅ |
| s42 Rand | PR=79, ISR*=0.131, H7=0, H1=70.9, Gen=29.1 | plan018-s42: PR=0.79, ISR*=0.1314 | ✅ |
| s43 Rand | PR=88, ISR*=0.058, H7=0, H1=93.2, Gen=6.8 | plan018-s43-r2: H7=0, H1=93.2, Gen=6.8 | ✅ |
| s44 Rand | PR=89, ISR*=0.070, H7=0, H1=79.8, Gen=20.2 | plan018-s44: PR=0.89, ISR*=0.0695 | ✅ |
| Rand mean | 85±6, ISR*=0.086±.039, H1=81.3±11, Gen=18.7±11 | 计算验证全部匹配 | ✅ |
| Footnote: 0.258 vs 0.243 = 1.06× | D051 | paper_framing: 0.2578 vs 0.2434 | ✅ |

**Premise-count confound paragraph:**

| 数字 | Registry 验证 | 状态 |
|------|--------------|------|
| 5.58 components (ISR s42) | plan002-b01-s42: eval_component_count_mean=5.58 | ✅ |
| 8.46 components (Random s42) | plan018-s42: eval_component_count_mean=8.46 | ✅ |
| 0.258 (n=11) vs 0.243 (n=21) = 1.06× | paper_framing D051 | ✅ |
| 15/26 have 1-2 premises | paper_framing: 26-11=15 | ✅ |
| Raw 2.4× (invalidated) | paper_framing D051 | ✅ |

**High-dose paragraph:**

| 数字 | 来源 | 状态 |
|------|------|------|
| PR 18% (ISR β=0.3) | plan002-b03 | ❓ (无 eval 指标) |
| 5.2× degradation | 93/18=5.17→5.2 | ✅ (if 18% correct) |
| Random PR=48%, 2.7× | plan017: PR=0.48, 48/18=2.67→2.7 | ✅ |

**Table 3 (prolog-crosslogic):**

| 行 | 数字 | Registry 验证 | 状态 |
|---|------|--------------|------|
| FOL exec s42: PR=93, ISR*=0.132 | plan001-s42-r2 | ✅ |
| FOL exec s43: PR=14, ISR*=0.000 | plan001-s43-r4 | ✅ |
| FOL exec s44: PR=98, ISR*=0.582 | plan001-s44: proved_only_isr=0.5816 | ✅ |
| Prolog exec s42: PR=83, ISR*=0.037 | plan006-prolog-exec-s42 | ✅ |
| Prolog exec s43: PR=56, ISR*=0.015 | plan006-prolog-exec-s43-r3 | ✅ |
| Prolog exec s44: PR=21, ISR*=0.387 | plan006-prolog-exec-s44: proved_only_isr=0.3866 | ✅ |
| Prolog STA s42: PR=50, ISR*=1.000, H7=100% | plan006-prolog-sta-s42: PR=0.5, ISR*=1.0, H7=1.0 | ✅ |
| Prolog STA s43: PR=38, ISR*=0.185, 38/38 | plan006-prolog-sta-s43: PR=0.38, ISR*=0.1853 | ✅ |
| Prolog STA s44: PR=97, ISR*=0.912, 95/97 | plan006-prolog-sta-s44: PR=0.97, ISR=0.885/0.97=0.912, H7_func=0.979→95/97 | ✅ |
| σ=47pp FOL, σ=31pp Prolog | 计算 | (93,14,98)→47pp; (83,56,21)→31pp | ✅ |
| 185 proved (Prolog STA total) | 50+38+97 | 185 | ✅ |
| s42: 50/50 proved | plan006-prolog-sta-s42: eval_proved_count=50 | ✅ |
| s44: 95/97 n_nec=1 | plan006-prolog-sta-s44 | ✅ |

**Taxonomy section:**

| 数字 | Registry 验证 | 状态 |
|------|--------------|------|
| H1: 52-93% across RL | range of non-zero per-seed values | ✅ |
| H7: 64.5% vs 0% | ISR 149/231 vs Random 0/256 | ✅ |
| Tautological: 94%, comp=2.04 | plan001-s44: comp_count_2=94/100, comp=2.04 | ✅ |
| s43: 87% max length | 无此指标 | ❓ |
| Contradiction: 18.55 at 1000 steps | plan016: components=18.55 | ✅ |
| Complexity-w/o-utility: 3.8% | paper_framing D038 | ✅ |
| ~68-81% total conclusion embedding | s42对比: ISR 67.9% vs Random 70.9% | ✅ |
| SFT 92.9% genuine | plan009-sft: genuine_rate=0.929 | ✅ |

### discussion.tex

| 数字 | 来源实验 | Registry 值 | 状态 |
|------|----------|------------|------|
| Spearman ρ=-0.049, p=0.187 | plan014 | spearman_rho=-0.049, spearman_p=0.187 | ✅ |
| 1.06× vs raw 2.4× | D051 | paper_framing一致 | ✅ |
| "over half" of genuine have 1-2 prem | D051 | 15/26=57.7% | ✅ |

### conclusion.tex

| 数字 | 来源实验 | Registry 值 | 状态 |
|------|----------|------------|------|
| 0.642→0.132→0.003 | plan003/plan001-s42-r2/plan016 | 0.6423/0.1324/0.003 | ✅ |
| 32%→96% | plan003/plan016 | 0.32/0.96 | ✅ |
| H7=64.5% | ISR β=0.1 3-seed | 149/231=64.5% | ✅ |
| 1.06× | D051 | ✅ | ✅ |
| β=0.3 PR 18% | plan002-b03 | 无 eval 指标 | ❓ |
| 0% genuine Prolog | plan006-prolog-sta 3-seed | ✅ | ✅ |
| 7 hacking modes | taxonomy | 7 | ✅ |
| Qwen3-4B, 500 FOLIO | 配置 | ✅ | ✅ |
| ρ=-0.049, n.s. | plan014 | ✅ | ✅ |
| 3 seeds | 配置 | ✅ | ✅ |

---

## 不匹配详情

### ⚠️ introduction.tex line 50: "<16% under any RL condition"

**原文**: "an SFT baseline confirms hacking is RL-specific (92.9\% genuine vs.\ $<$16\% under any RL condition"

**问题**: "<16% under any RL condition" 表述不准确。

| 条件 | Genuine % |
|------|-----------|
| ISR β=0.1 s42 | **30.9%** |
| Random β=0.1 s42 | **29.1%** |
| Random β=0.1 s44 | **20.2%** |
| Random β=0.1 3-seed mean | **18.7%** |
| ISR β=0.1 3-seed mean | ~15.9% |
| Exec-only s42 | 12.9% |

多个 RL 条件的 genuine rate 超过 16%。ISR β=0.1 的 3-seed mean 约 16% 是唯一勉强符合的，但 random β=0.1 mean=18.7% 和多个单 seed 值远超 16%。

**建议修正**: 改为 "92.9\% genuine vs.\ $\leq$20\% under RL conditions" 或 "vs.\ substantially lower genuine rates under all RL conditions (\S\ref{sec:goodhart})"。

---

## 无法追溯详情

| # | 数字 | 出现位置 | 原因 |
|---|------|----------|------|
| 1 | plan002-b03 eval PR=18% | abstract, intro, experiments Table 1, conclusion | Registry 仅有训练指标，无 eval_prove_rate。paper_framing 记录 eval PR=0.18 但 registry 未记录 |
| 2 | plan002-b03 ISR*=0.143 | experiments Table 1 | 同上，可从 all-sample ISR=0.026 / PR=0.18 间接推算 ≈0.144 |
| 3 | Component count 6.58 (100步) | experiments §5.2, Fig.2 caption | plan003 registry 无 component count 指标 |
| 4 | 94.8% ISR=0 (1000步) | intro line 26, experiments §5.2, Fig.2 caption | plan016 registry 无 per-sample ISR 分布细项 |
| 5 | s43 exec-only "87% hit max token" | experiments §5.2, taxonomy §5.4 | plan001-s43-r4 registry 无此指标 |

注：#1/#2 的数字在 paper_framing 中有记录，可能来自未注册到 registry 的评估脚本结果。#3-#5 来自 raw data 分析，registry 只记录 summary metrics。

---

## 写作约束检查

- [x] **不标 "no hacking"**: 论文对 SFT 用 "near-zero hacking" (92.9% genuine)，未使用 "no hacking" ✅
- [x] **plan013 vs plan017 不简化为 "additive vs convex"**: 论文未提及 plan013/convex 对照 ✅
- [x] **D051: 2.4x 作废，1.06x 定论**: 论文仅在 premise-count confound 段引用 "raw 2.4×" 作为被推翻的对照，定论为 1.06× ✅
- [x] **"significantly" 需统计检验**: 全文未出现 "significantly" ✅
- [x] **"consistently" 需多数据集**: 全文未出现 "consistently" 作数据声明 ✅
- [ ] **⚠️ "<16% under any RL condition"** 违反数据准确性 → 见上方不匹配详情

---

## 引用审计

### 论文引用 → bib 对照

所有 22 个 \cite{} key 均在 references.bib 中有对应条目：✅

| Citation Key | 出现文件 | Bib 存在 |
|-------------|---------|----------|
| satlm | intro, related | ✅ |
| logic-lm | intro, related | ✅ |
| linc | intro, related | ✅ |
| deepseekmath | intro, method, experiments | ✅ |
| mellgren-prolog-grpo | intro, related | ✅ |
| logic-rl | intro, related | ✅ |
| skalse-reward-hacking | intro, related | ✅ |
| reward-hacking-survey | intro | ✅ |
| demillo1978 | intro, related, method | ✅ |
| manheim-goodhart-taxonomy | intro, related, experiments, discussion | ✅ |
| karwowski-goodhart-rl | intro, related, experiments | ✅ |
| gao-reward-overoptimization | intro, related, experiments, discussion | ✅ |
| jia-harman-survey | related, method | ✅ |
| just-mutants-real-faults | related | ✅ |
| lightman-verify-step | related | ✅ |
| math-shepherd | related | ✅ |
| rlsf | related | ✅ |
| rubric-grpo | related | ✅ |
| pan-reward-misspecification | related | ✅ |
| lorp | related | ✅ |
| fover-pei2025 | related | ✅ |
| folio | related, experiments | ✅ |

### 关键论文引用检查

| 论文 | 是否引用 |
|------|---------|
| deepseekmath | ✅ |
| logic-lm | ✅ |
| linc | ✅ |
| satlm | ✅ |
| gao-reward-overoptimization | ✅ |
| manheim-goodhart-taxonomy | ✅ |

### 引用缺失

无引用缺失。所有任务要求检查的关键论文均已引用。

### Bib 中未被引用的条目（32 个）

deepseek-r1, deepproblog, neurasp, thought-like-pro, reward-shaping-rlhf, rlvr-reasoning, gao-effective-rl-reward, prof-process-outcome, moskovitz-constrained-rlhf, progrs-outcome-conditioned, qwen-prm-lessons, offutt-coupling, llmorpheus, mutation-guided-meta, mutation-consistency-llm, deepmutation, inform-reward-hacking, mo-grpo, energy-loss-reward-hacking, spurious-rewards, bondarenko-spec-gaming, kim-game-formalization, proofwriter, nl2fol, logica2, kwa-catastrophic-goodhart, rafailov-daa-scaling, huang-chi-squared, coste-rm-ensembles, bipars, dapo, fover-kamoi2026, deepseek-prover-v15, alphaproof

注：未引用条目不构成错误，但提交前应清理 bib 文件，避免 LaTeX 警告。

---

## paper_framing 内部一致性

paper_framing 中 s42 ISR β=0.1 genuine 有两处数值：
- D038→D044 段: "30.9% (25/81)" — 与 registry (genuine_rate=0.309, genuine_count=25) 一致
- 主表格: "32.1% (26)" — 与 registry 不一致 (多了 1 个 genuine)

**论文采用的是 30.9% (25/81)**，与 registry 一致。paper_framing 主表格的 32.1% (26) 是 paper_framing 自身的笔误。
