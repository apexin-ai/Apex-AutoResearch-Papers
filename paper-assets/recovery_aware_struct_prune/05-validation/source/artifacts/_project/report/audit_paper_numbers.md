# 论文数字提取清单

审计日期: 2026-05-25
审计范围: docs/paper/{abstract,introduction,method,related_work,experiments,conclusion,limitations,ethics,appendix}.tex + tables/*.tex + figures/paper/gen_*.py

## 统计

- A类(实验结果): ~140个
- B类(模型/超参): ~35个
- C类(统计描述): ~25个
- D类(派生计算): ~30个

---

## 逐文件数字清单

### abstract.tex

| 行号 | 数字 | 上下文 | 分类 | 备注 |
|------|------|--------|------|------|
| 1 | 7B | "7B reasoning model" | B | DeepSeek-R1-Distill-Qwen-7B |
| 1 | four (4) | "across four criteria" | C | CKA-only/Standard/RASP/Random |

### introduction.tex

| 行号 | 数字 | 上下文 | 分类 | 备注 |
|------|------|--------|------|------|
| 7 | 96.5% | "96.5\% parameter retention" | A | 来自 selfhealing2025 外部引用 |
| 10 | 7B | DeepSeek-R1-Distill-Qwen-7B | B | |
| 10 | 20% | "20\% MLP channel sparsity" | C | ⚠ 详见一致性检查 |
| 10 | 4.4 (×) | "4.4 times the peak RL reward" | D | 0.354/0.081=4.37→4.4 ✓ |
| 10 | 1 (pp) | "within 1 percentage point" | D | 上界描述 |
| 17 | 20% | "20\% sparsity" 图1 caption | C | |
| 17 | 1.14 (pp) | "$\|\Delta\| \leq 1.14$\,pp" | D | α=2.0 时 +1.14 |
| 28 | $\alpha{=}2.0$ | 峰值 α | B | |
| 28 | 66.11% | GSM8K α=2.0 | A | 对应 Table 3 ✓ |
| 31 | -1.36 (pp) | ShortGPT GSM8K Δ | A | 43.37-44.73=-1.36 ✓ |
| 35 | 20-25% | 解耦适用范围 | C | |
| 35 | $p{<}0.05$ | TOST | A | |
| 35 | 7 of 8 | TOST 通过 | C | |
| 35 | 15% | 解耦边界 | C | |
| 36 | four (4) | 四个评价指标 | C | |
| 37 | 20% | "20\% sparsity" | C | |
| 37 | 51-64% | SFT recovery range | A | 51.25-63.91 ✓ |
| 37 | 1.14 (pp) | "at most 1.14\,pp" | D | α=2.0 |
| 37 | 300 | training steps | B | |

### method.tex

| 行号 | 数字 | 上下文 | 分类 | 备注 |
|------|------|--------|------|------|
| 17 | $n_Q{=}28$ | DeepSeek-R1-Distill-Qwen-7B | B | |
| 17 | $n_{KV}{=}4$ | | B | |
| 17 | $G{=}7$ | 28/4=7 | D | ✓ |
| 17 | 7 Q + 1 KV | GQA group | B | |
| 29 | 28 | "28 MLP channel groups" Layer 27 | B | |
| 37 | $M{=}512$ | calibration set | C | |
| 64 | $O(L \cdot k^2)$ | CKA 计算复杂度 | B | $k \le 28$ |
| 65 | 28 | $k \le 28$ | B | |
| 65 | <2 min | CKA 计算时间 | A | |
| 69 | $\rho \geq 0.964$ | Spearman 稳定性 | A | 对应 Table |
| 75 | 40% | per-layer capacity floor | B | $\tau=0.4$ |
| 75 | {0.3, 0.4, 0.5, 0.6} | τ ablation | C | |
| 91 | $\alpha{=}0$ | reduces to Standard | B | |
| 93 | $\alpha{=}2.0$ | 峰值 | B | |
| 93 | 66.11% | α=2.0 GRPO acc | A | |
| 93 | +1.72 (pp) | over CKA-only | D | 66.11-64.39=1.72 ✓ |
| 115 | 20% | sparsity | C | |
| 122 | 1, 2 | 阶段编号 | B | |

### related_work.tex

| 行号 | 数字 | 上下文 | 分类 | 备注 |
|------|------|--------|------|------|
| 10 | 96.5% | selfhealing2025 retention | A | 外部 |
| 15 | 1.8 (pp) | "$\|\Delta\| \leq 1.8$\,pp" | D | MATH-500 α=2.0 时的最大值 |
| 17 | 5-30% | RL 参数更新比例 | A | 外部引用 |

### experiments.tex

| 行号 | 数字 | 上下文 | 分类 | 备注 |
|------|------|--------|------|------|
| 18 | 20% | sparsity | C | |
| 28 | 7B | DeepSeek-R1 | B | |
| 29 | $N{=}1{,}319$ | GSM8K size | C | |
| 30 | 90.83% | Unpruned greedy GSM8K | A | |
| 33 | 20% | structured sparsity | C | ⚠ 详见一致性 |
| 33 | 200 of 784 | MLP groups | C | 200/784=25.5% ⚠ |
| 33 | 28 | layers | B | |
| 33 | ~1.45B | params removed | A | 实际 7.62-6.16=1.46B |
| 33 | 40% | retention floor | B | |
| 33 | $\alpha{=}1.0$ | RASP main | B | |
| 33 | 512 | TRL default tokens | B | Random |
| 33 | 1,024 | other methods tokens | B | |
| 37 | <2% | post-prune accuracy | A | |
| 38 | 2 (epochs) | SFT | B | |
| 38 | 7,473 | GSM8K examples SFT | C | |
| 38 | 37 min | SFT wall time | A | |
| 38 | $1{\times}10^{-6}$ | GRPO lr | B | |
| 38 | $\beta{=}0.01$ | KL coef | B | |
| 38 | $T{=}0.4$ | temperature | B | |
| 38 | 100 | GRPO steps | B | |
| 38 | 1,000 | GRPO problems | C | |
| 39 | 3 | seeds | C | |
| 39 | 64.39% | CKA-only mean | A | |
| 39 | 0.19 pp | CKA-only std | A | |
| 39 | 59.84% | Standard mean | A | |
| 39 | 0.38 pp | Standard std | A | |
| 39 | $p{<}0.001$ | Welch's t | A | |
| 40 | 9.56 pp | "Unpruned"-warmup gap | D | 90.83-81.27=9.56 ✓ |
| 40 | 90.83% | pre-warmup | A | |
| 41 | 2× | RTX PRO 6000 GPUs | B | |
| 41 | 94 GB | VRAM | B | |
| 47 | 20% | sparsity | C | |
| 50 | 0.354 | CKA-only peak reward | A | |
| 50 | 0.125 | CKA-only min $f_0$ | A | |
| 51 | 0.14-0.19 | Random reward range | A | |
| 51 | 0.300 | Random min $f_0$ | A | |
| 51 | 0.50 | Standard $f_0$ | A | |
| 51 | 0.081 | Standard peak reward | A | |
| 51 | 0.675 | RASP $f_0$ | A | |
| 51 | 0.010 | RASP reward decline | A | |
| 73 | 4.4× | peak reward gap | D | 0.354/0.081 ✓ |
| 73 | $\|\Delta\| < 1$ pp | 上界 | D | |
| 73 | +0.48 | CKA-only Δ | A | 64.39-63.91 ✓ |
| 73 | +0.55 | Standard Δ | A | 59.84-59.29 ✓ |
| 73 | -0.53 | Random Δ | A | 50.72-51.25 ✓ |
| 73 | -0.61 | RASP Δ | A | 60.88-61.49 ✓ |
| 74 | 20-25% | 解耦范围 | C | |
| 76 | 15% | 边界 | C | |
| 76 | 5.69 pp | SFT 15% gap | D | 72.18-66.49 ✓ |
| 76 | 7.20 pp | GRPO 15% gap | D | 72.76-65.56 ✓ |
| 76 | 1 pp | 上界 | D | |
| 76 | 1.14 pp | α=2.0 Δ | D | |
| 78 | $\varepsilon{=}2$ pp | TOST margin | B | |
| 78 | $4\times$ | 4× cross-seed σ | D | 2/0.19≈10× actually, 2/0.38≈5× — 取近似 |
| 78 | $N{=}1{,}319$ | TOST samples | C | |
| 78 | 7/8 | TOST 通过 | C | |
| 78 | 0.37 pp | seed range | A | 64.59-64.22=0.37 ✓ |
| 78 | 300 | extended steps | B | |
| 79 | 2 pp | "$\|\Delta\| < 2$\,pp" MBPP | D | 实际最大 +1.34 |
| 81 | -1.36 pp | ShortGPT GSM8K | A | |
| 81 | +4.01 pp | ShortGPT MBPP | A | 14.44-10.43 ✓ |
| 81 | 1.8 pp | fine-grained 上界 | D | MATH-500 α=2.0 |
| 90 | {0.5, 1.0, 2.0, 3.0, 4.0} | α 范围 | B | |
| 90 | 66.11% | α=2.0 peak | A | |
| 90 | 1.14 pp | 上界 | D | |
| 90 | 62.77% | α=4.0 | A | |
| 91 | 23.0% | MATH-500 α=1.0 worst | A | |
| 91 | 27.2-27.6% | higher-α 集群 | A | |
| 92 | 30% | sparsity cliff | C | |
| 92 | 19% | param reduction | D | 1.46/7.62=0.192 ✓ |
| 92 | ~28% | memory reduction | A | |
| 102 | $\mu{=}0.62$ | CKA-only layer CKA mean | A | 实算 0.6202 ✓ |
| 109 | 5.5× | 300-step gap | D | 0.308/0.056=5.50 ✓ |
| 116 | $\mu{=}0.62$ | CKA-only | A | |
| 116 | $\mu{=}0.90$ | Standard | A | 实算 0.9039 ✓ |
| 116 | $\mu{=}0.92$ | Random | A | 实算 0.9233 ✓ |
| 116 | $\mu{=}0.88$ | RASP | A | 实算 0.8822 ✓ |
| 118 | L0-9 | 早层 | C | |
| 118 | 72.5% | CKA-only 移除集中度 | A | |
| 118 | 2.89× | gradient ratio | A | |
| 118 | 55/56 | 显著层 | C | |
| 118 | $p{<}0.05$ | | A | |
| 119 | 22% | CKA-only truncation | A | |
| 119 | 655 (tokens) | CKA-only mean | A | |
| 119 | 44% | Standard truncation | A | |
| 119 | 1,128 (tokens) | Standard mean | A | |
| 123 | 100, 300 | step extension | B | |
| 123 | 0.054-0.058 | Standard reward range | A | 与 fig5 数据一致 |
| 123 | 0.5 | $f_0$ threshold | B | |
| 123 | 5.5× | gap | D | |
| 123 | 0.308 | CKA-only step 300 | A | 0.3075 → 0.308 ✓ |
| 123 | 0.056 | Standard step 300 | A | 0.0562 → 0.056 ✓ |
| 124 | 10 (steps) | Standard 进入 collapse | B | |
| 124 | 0.5 | $f_0$ | B | |
| 124 | 0.35 | CKA-only $f_0$ | A | |
| 129 | 1.5B | scale | B | |
| 129 | 1.0% | post-prune Math-7B | A | |
| 129 | 51.50% | CKA-only Math-7B | A | |
| 129 | 21.00% | Standard Math-7B | A | |
| 130 | 30.5 pp | cross-model gap | D | 51.50-21.00=30.50 ✓ |
| 130 | 4.6 pp | primary | D | 64.39-59.84=4.55, rounded 4.6 ⚠ |

### conclusion.tex

| 行号 | 数字 | 上下文 | 分类 | 备注 |
|------|------|--------|------|------|
| 5 | 20-25% | sparsity range | C | |
| 5 | mean \|Δ\| = 0.54 pp | four criteria | D | (0.48+0.55+0.61+0.53)/4=0.5425 ✓ |
| 5 | 1.8 pp | max across benchmarks | D | MATH-500 α=2.0 |
| 5 | 4.4× | peak reward gap | D | |
| 6 | 20% | sparsity | C | |
| 6 | <2% | post-prune | A | |
| 6 | 51-64% | recovery range | A | |
| 6 | 300 | steps | B | |
| 9 | ~100 | diagnostic steps | B | |

### limitations.tex

| 行号 | 数字 | 上下文 | 分类 | 备注 |
|------|------|--------|------|------|
| 3 | 两个 (7B, 1.5B) | Qwen2.5 模型 | C | |

### ethics.tex

无数字。

### appendix.tex

| 行号 | 数字 | 上下文 | 分类 | 备注 |
|------|------|--------|------|------|
| 16 | $2 \times 10^{-5}$ | SFT lr | B | |
| 16 | $1 \times 10^{-6}$ | GRPO lr | B | |
| 17 | 1, 1 | batch size | B | |
| 18 | 8, 1 | grad accumulation | B | |
| 19 | 2,048 | max seq len | B | |
| 20 | 1,024, 512 | max new tokens | B | |
| 22 | 2 epochs / 100 steps | | B | |
| 23 | 0.01 | KL β | B | |
| 24 | 0.4 | sampling temp | B | |
| 25 | 8 | generations per prompt | B | |
| 28 | 50 | reward_desert_patience | B | |
| 80 | 72.0 | Dense TPS | A | |
| 80 | 20.1 | Dense TTFT (ms) | A | |
| 80 | 13.9 | Dense per-token (ms) | A | |
| 80 | 7.62 | Dense params (B) | A | |
| 81 | 58.3 | CKA TPS | A | |
| 81 | 16.4 | CKA TTFT | A | |
| 81 | 16.7 | CKA per-token | A | |
| 81 | 6.16 | CKA params | A | |
| 82 | 58.2 | Standard TPS | A | |
| 82 | 16.4 | Standard TTFT | A | |
| 82 | 16.7 | Standard per-token | A | |
| 82 | 6.16 | Standard params | A | |
| 87 | ~28% | memory reduction | A | |
| 88 | 18% | TTFT improvement | D | (20.1-16.4)/20.1=18.4% ✓ |
| 88 | 20.1→16.4 | | A | |
| 89 | 19% | per-token decrease | D | (72.0-58.3)/72.0=19.0% ✓ |
| 89 | 72.0→58.3 | | A | |
| 89 | 13.9→16.7 | | A | |
| 90 | 58.3 vs 58.2 | identical throughput | A | |
| 97 | α=2.0 | peak | B | |
| 97 | 64.97% | SFT α=2.0 | A | |
| 97 | 66.11% | GRPO α=2.0 | A | |
| 97 | +1.14 pp | Δ | A | |
| 98 | α=0.5 | | B | |
| 98 | 60.73% | SFT α=0.5 | A | ⚠ 与 fig1 数据不一致 |
| 98 | 61.18% | GRPO α=0.5 | A | ⚠ 与 fig1 数据不一致 |
| 99 | α=1.0 | | B | |
| 99 | 0.061 | RASP peak reward | A | |
| 99 | 60.88% | RASP GRPO | A | |
| 99 | -0.61 pp | Δ | A | |
| 100 | α=3.0 | | B | |
| 100 | 64.14% | SFT α=3.0 | A | |
| 100 | 63.46% | GRPO α=3.0 | A | |
| 100 | -0.68 pp | Δ | A | |
| 100 | 2.65 pp | drop from peak | D | 66.11-63.46=2.65 ✓ |
| 101 | α=4.0 | | B | |
| 101 | 62.77% | GRPO α=4.0 | A | |
| 101 | 61.94% | SFT α=4.0 | A | |
| 101 | +0.83 pp | Δ | A | |
| 101 | 0.146→0.256→0.198 | reward trajectory | A | |
| 102 | 1.14 pp | 上界 | D | |
| 107 | 100, 300 | steps | B | |
| 108 | 64.37% | CKA-only seed 42 at 300 | A | |
| 108 | 59.29% | Standard at 300 | A | |
| 108 | 0.38 pp | std | A | |
| 109 | 0.354 | peak step 100 | A | ⚠ peak at step 50 实际是 0.3544 |
| 109 | 0.308 | step 300 | A | |
| 110 | 0.054-0.058 | Standard range | A | |
| 117 | 27.4%, 25.6%, 21.6%, 16.6% | MATH-500 SFT | A | |
| 117 | 27.6%, 27.0%, 23.0%, 15.0% | MATH-500 GRPO | A | |
| 118 | 4.6 pp | GSM8K SFT gap | D | 63.91-59.29=4.62 ⚠ 论文写4.6 |
| 118 | 1.8 pp | MATH-500 SFT gap | D | 27.4-25.6=1.8 ✓ |
| 118 | 0.6 pp | MATH-500 GRPO gap | D | 27.6-27.0=0.6 ✓ |
| 120 | 53.0% | dense MATH-500 | A | |
| 120 | 90.83% | dense GSM8K | A | |
| 120 | 2,048 | token limit | B | |
| 121 | 22% | CKA truncation | A | |
| 121 | 655 | CKA mean tokens | A | |
| 121 | 44% | Standard truncation | A | |
| 121 | 1,128 | Standard mean tokens | A | |
| 122 | ~8 pp | α SFT range MATH-500 | A | ⚠ 实算 6.2 pp |
| 122 | ~2 pp | stderr | A | |
| 122 | 2048 | token limit | B | |
| 128 | $N{=}374$ | MBPP size | C | |
| 132 | +1.25 pp | MBPP mean | D | (1.34+1.07+1.34)/3=1.25 ✓ |
| 132 | $N{=}374$ | | C | |
| 132 | ~1.7 pp | stderr | A | |
| 142 | 256/512/1024 | calibration sizes | C | |
| 142 | 0.964 to 0.979 | Spearman range | A | 对应表 |
| 147 | $N{=}200$ | gradient samples | C | |
| 158 | 2.89× | CKA vs Standard ratio | A | |
| 158 | 55/56 | sig layers | C | |
| 159 | 2.26× | CKA vs RASP | A | |
| 159 | 56/56 | | C | |
| 160 | 1.28× | RASP vs Standard | A | |
| 160 | 45/56 | | C | |
| 165 | 64.39%, 60.88%, 59.84% | recovery hierarchy | A | |
| 172 | 64.37% | seed 42 | A | |
| 172 | 64.22% | seed 123 | A | |
| 172 | 64.59% | seed 456 | A | |
| 172 | 64.39% | mean | A | |
| 172 | 0.19 pp | std | A | |
| 173 | 59.84% | Standard mean | A | |
| 173 | 0.38 pp | std | A | |
| 174 | 4.55 pp | gap | D | 64.39-59.84 ✓ |
| 184 | 4% | Standard 30% | A | |
| 184 | 1.6% | CKA 30% | A | |
| 184 | 0% | RASP 30% | A | |
| 200 | 64.39, 0.19, 3 | multi-seed table | A | |
| 201 | 59.84, 0.38, 3 | | A | |
| 202 | 60.88, 1 | | A | |
| 203 | 50.72, 0.15, 3 | | A | |
| 205 | 72.76, 0.57, 3 | 15% CKA | A | |
| 206 | 65.56, 0.50, 3 | 15% Std | A | |
| 210 | 4.55 pp | gap 20% | D | ✓ |
| 210 | 64.22--64.59% | CKA range | A | |
| 210 | 59.44--60.20% | Standard range | A | ⚠ 实算 seed456 GRPO=60.28 (>60.20) |
| 211 | 0.76 pp vs 0.37 pp | observed ranges | D | 60.20-59.44=0.76, 64.59-64.22=0.37 |
| 212 | 50.57%, 50.72%, 50.87% | Random seeds | A | |
| 212 | 0.15 pp | σ | A | |
| 212 | 0.30 pp | range | D | 50.87-50.57=0.30 ✓ |
| 212 | 51.25% | SFT | A | |
| 213 | -0.68, -0.53, -0.38 pp | Random Δ | D | 51.25-50.57/72/87 ✓ |
| 214 | 59.21% vs 59.29% | Standard SFT 差异 | A | |
| 214 | 0.08 pp | Δ | D | ✓ |
| 215 | 7.20 pp | 15% gap | D | ✓ |
| 215 | 72.76 vs 65.56 | | A | |
| 215 | $t{\approx}16.4$ | | A | |
| 215 | $p{<}0.001$ | | A | |
| 215 | 72.10--73.09%, 65.13--65.43% | seed ranges 15% | A | |
| 229-237 | cross-sparsity 表 | (见表) | A | |
| 243 | +7.20 pp | 15% gap | D | ✓ |
| 244 | 80.1% | retention | D | 72.76/90.83=80.11% ✓ |
| 245 | -7.20, -8.42 | Standard decline | D | 66.49-59.29, 59.29-50.87 ✓ |
| 245 | -8.27, -3.79 | CKA decline | D | 72.18-63.91, 63.91-60.12 ✓ |
| 246 | 0.008 | Standard 25% peak reward | A | |
| 256 | 35.48, 22.29, 26.16 | 1.5B accs | A | |
| 256 | -0.15, -0.61 pp | 1.5B Δ | A | |
| 257 | 49.81% | 1.5B dense | A | |
| 257 | 90.83% | 7B dense | A | |
| 265 | $N{=}200$ | Math-7B size | C | |
| 272 | 1.0%, 51.50%, 27.0% | CKA Math-7B | A | |
| 272 | 3.53 (stderr) | binomial | D | sqrt(0.515*0.485/200)=0.0353 ✓ |
| 273 | 18.5%, 21.00%, 36.5% | Standard Math-7B | A | |
| 273 | 2.88 stderr | | D | sqrt(0.21*0.79/200)=0.0288 ✓ |
| 278 | 1.0%, 18.5%, 51.50%, 21.00% | Math-7B 复述 | A | |
| 280 | 40%, 48.60%, 243/500, 83.8%, 2048 | EOS/GRPO/truncation | A | 243/500=48.6% ✓ |
| 285 | 28 layers | | B | |
| 285 | 20% | sparsity | C | |
| 286 | L0--9, 72.5% | CKA early-layer | A | |
| 286 | L16--27 | preserved late | C | |
| 287 | L16-18, L22, L25-26 | Standard distribution | C | |
| 290 | 65 (groups) | CKA exclusive | A | |
| 290 | L6-9, L27 | | C | |
| 291 | 46+ (groups) | Standard exclusive | A | |
| 291 | L16-18, L22, L25-26 | | C | |
| 293 | $\mu{=}0.62$, 0.90 | | A | |
| 304 | <0.001 | RASP KL | A | |
| 304 | ~0.004-0.005 | Random KL | A | |
| 308 | $\alpha{=}1.0$ | | B | |
| 308 | <0.001 | KL | A | ⚠ 实际 RASP max=0.001119 (微超) |
| 309 | 0.001-0.003 | CKA/Standard KL | A | 数据范围合理 |
| 309 | ~0.004-0.005 | Random | A | |
| 313 | 0.001, 0.5, 1.0 | depth-first synthetic | B | |
| 313 | 20% | sparsity | C | |
| 317 | ~10%, ~8% | SFT/GRPO depth-first | A | |
| 317 | $N{\approx}50$--88 | early stopped | C | |
| 326 | $N{=}1{,}319$ | | C | |
| 326 | 100 steps | | B | |
| 326 | $\tau{=}0.4$ | default | B | |
| 332 | 0.3, 65.05%, +0.68 | floor 0.3 | A | |
| 333 | 0.4, 64.37% | default | A | |
| 334 | 0.5, 61.71%, -2.66 | | A | 64.37-61.71=2.66 ✓ |
| 335 | 0.6, 62.02%, -2.35 | | A | 64.37-62.02=2.35 ✓ |
| 342 | +0.68 pp | | D | |
| 342 | -2.66, -2.35 pp | | D | |
| 342 | 0.31 pp | 0.5/0.6 diff | D | 62.02-61.71=0.31 ✓ |
| 342 | ~1.3 pp | stderr | A | |
| 348 | $N{=}1{,}319$ | | C | |
| 348 | 20% | sparsity | C | |
| 350 | $\varepsilon$ | margin | B | |
| 361-369 | TOST 表数值 | (per-seed Δ) | A | 详见一致性检查 |
| 374 | 2 pp | $\varepsilon$ | B | |
| 374 | 4× | σ multiplier | D | 2/0.19≈10.5× ⚠ 论文说4× (应基于Standard σ=0.38?: 2/0.38=5.3 也不是4) |
| 374 | 0.19 pp | σ | A | |
| 375 | 2 pp | | B | |
| 375 | 7/8 | | C | |
| 375 | -0.99 pp | borderline | A | |
| 375 | $p{=}0.069$ | | A | |
| 376 | 3 pp | | B | |
| 376 | 8/8 | | C | |
| 376 | $p{<}0.002$ | | A | |
| 377 | 1 pp | | B | |
| 377 | $N{=}1{,}319$ | | C | |
| 384 | 15% | | C | |
| 384 | +1.51 pp | CKA-guided amp | D | 7.20-5.69=1.51 ✓ |
| 388 | 96.5% | external retention | A | |
| 388 | 20-25% | sparsity | C | |

### tables/tab1_recovery_gradient.tex

| 数字 | 上下文 | 备注 |
|------|--------|------|
| 20% | sparsity | |
| 0.354, 0.285, 0.125 | CKA peak/mean/min $f_0$ | |
| 0.190, 0.164, 0.300 | Random | |
| 0.081, 0.050, 0.500 | Standard | |
| 0.061, 0.031, 0.675 | RASP | |

### tables/tab2_decoupling.tex

| 数字 | 上下文 | 备注 |
|------|--------|------|
| $N{=}1{,}319$, 20% | |
| 81.27, 81.27, 0.00, 0.669 | Unpruned | |
| 64.97, 66.11, +1.14 | α=2.0 | |
| 63.91, 64.39, ±0.19, +0.48, 0.354 | CKA-only | |
| 59.29, 59.84, ±0.38, +0.55, 0.081 | Standard | |
| 61.49, 60.88, -0.61, 0.061 | RASP α=1.0 | |
| 51.25, 50.72, ±0.15, -0.53, 0.190 | Random | |
| 44.73, 43.37, -1.36 | ShortGPT | |

### tables/tab_math500.tex

| 数字 | 上下文 | 备注 |
|------|--------|------|
| $N{=}500$, 2048 tokens | |
| 0.6 pp, 4.62 pp | GRPO/GSM8K SFT gaps in caption | 4.62=63.91-59.29 ⚠ 主文写4.6 |
| 53.0 | dense | |
| 20% method: 27.4/27.6, 25.6/27.0, 21.6/23.0, 16.6/15.0 | |
| Δ: +0.2, +1.4, +1.4, -1.6 | |
| α: 26.8/26.8, 25.6/27.4, 23.6/--, 27.8/27.2 | 0.5/2.0/3.0/4.0 |
| Δ α: +0.0, +1.8, --, -0.6 | |
| 25%: 18.8/17.6, 15.4/-- | -1.2, -- | |
| 73.6% at 4096 | dense truncation | |

### tables/tab_mbpp.tex

| 数字 | 上下文 | 备注 |
|------|--------|------|
| $N{=}374$ | |
| ~75% | code capability loss | |
| ~1 pp | range | |
| +4.01 pp, 1.55 stderr | ShortGPT | |
| Dense: 53.48 | |
| CKA 20%: 12.83/14.17/+1.34 | |
| Standard 20%: 12.03/13.10/+1.07 | |
| RASP α=1.0 20%: 11.76/13.10/+1.34 | |
| ShortGPT 20%: 10.43/14.44/+4.01 | |

### tables/tab_cka_stability.tex

| 数字 | 上下文 | 备注 |
|------|--------|------|
| $\rho \geq 0.964$, 0.964/0.979 | 256/512/1024 | |

### tables/table3_alpha.tex

| 数字 | 上下文 | 备注 |
|------|--------|------|
| $N{=}1{,}319$, 20% | |
| α=0.5: 60.73/61.18/+0.45 | |
| α=1.0: 61.49/60.88/-0.61 | |
| α=2.0: 64.97/66.11/+1.14 | |
| α=3.0: 64.14/63.46/-0.68 | |
| α=4.0: 61.94/62.77/+0.83 | |

### tables/table4_sparsity_cliff.tex

| 数字 | 上下文 | 备注 |
|------|--------|------|
| 30% | sparsity | |
| Standard: N=200, 4%, 5.5% EOS | |
| RASP α=1: N=200, 0%, 3.0% EOS | |
| CKA: N=500, 1.6%, 8/500 | |

### tables/tab5_cross_scale.tex

| 数字 | 上下文 | 备注 |
|------|--------|------|
| 20%, 100 steps | |
| CKA: 0.354/64.39, 0.238/35.48 | 7B/1.5B |
| Standard: 0.081/59.84, 0.084/22.29 | |
| RASP α=1: 0.061/60.88, 0.099/26.16 | |
| Random: 0.190 | 7B only |

---

## 内部一致性检查

### ✅ 已验证一致

| 数字 | 位置1 | 位置2 | 结果 |
|------|-------|-------|------|
| 64.39% CKA-only GRPO | exp.tex:39 | tab2:13 | ✓ |
| 59.84% Standard GRPO | exp.tex:39 | tab2:14 | ✓ |
| 4.4× peak reward | intro:10, exp:73, concl:5 | 0.354/0.081=4.37 | ✓ |
| mean \|Δ\|=0.54 | concl:5 | (0.48+0.55+0.61+0.53)/4=0.5425 | ✓ |
| 90.83% Unpruned | exp:30, exp:40, app:120, app:257 | | ✓ |
| 81.27% Unpruned post-SFT | tab2:11 | exp:40 (隐含 9.56 pp gap) | ✓ |
| $f_0$ 值 (0.125/0.300/0.500/0.675) | exp:50, tab1, fig3 | | ✓ |
| α=2.0 peak (64.97/66.11/+1.14) | intro:28, method:93, exp:90, app:97, tab2:12, tab3:12 | | ✓ |
| ShortGPT GSM8K -1.36 pp | intro:31, exp:81, tab2:18 | | ✓ |
| ShortGPT MBPP +4.01 pp | exp:81, tab_mbpp:16 | | ✓ |
| 7.20 pp 15% GRPO gap | exp:76, app:215, app:243 | | ✓ |
| 5.5× 300-step gap | exp:109, exp:123 | | ✓ |
| 19% / ~28% param/mem reduction | exp:92, app:73, app:87 | | ✓ |
| RASP α=1.0 reward 0.061 | exp:51, tab1, tab2:15, tab5 | | ✓ |
| 51-64% SFT recovery range | intro:37, concl:6 | tab2 实际 51.25-63.91 | ✓ |
| $\|\Delta\| ≤ 1.14$ pp | intro:17, exp:76, app:102 | α=2.0 最大 | ✓ |
| 1.5B 三方法排序 | exp:129 | tab5 | ✓ |
| 30.5 pp cross-model | exp:130 | 51.50-21.00 | ✓ |
| Spearman ρ ≥ 0.964 | method:69 | tab_cka_stability | ✓ |
| 2.89× gradient ratio | exp:118, app:158 | | ✓ |

### ⚠ 发现的问题（按严重度排序）

| # | 严重度 | 位置1 | 位置2 | 差异说明 |
|---|--------|-------|-------|---------|
| **1** | **HIGH** | gen_fig1_dose_response.py:32-33 | table3_alpha.tex:10-14 | **Fig 1 的 SFT/GRPO 硬编码值与 Table 3 不一致**（详见下方） |
| **2** | **MEDIUM** | intro.tex:10 "20% MLP channel sparsity"; exp.tex:33 "20% structured sparsity, all removing 200 of 784 MLP channel groups" | app.tex:88 "Pruning reduces parameters by 19%" | **200/784 = 25.5% MLP groups, 不是 20%**。看似"20% sparsity"是相对于总模型参数（19% rounded），但 intro 写 "MLP channel sparsity" 是术语错误 |
| **3** | **MEDIUM** | app.tex:122 "SFT accuracy varies by ${\sim}$8\,pp across $\alpha$ values" | tab_math500.tex α SFT 值 | 实际 max-min = 27.8-21.6 = 6.2 pp，"~8 pp" 偏大 |
| **4** | **LOW** | exp.tex:130 "4.6 pp difference on the primary model" | exp.tex:39, tab2 64.39-59.84=4.55 | 4.55 rounded to 4.6（合理近似）；但 tab_math500.tex caption 写 "4.62 pp"——同一数字两种舍入并存 |
| **5** | **LOW** | exp.tex:78 "$4\times$ cross-seed $\sigma$" | app.tex:374 "$2$\,pp because it is approximately $4\times$ the observed cross-seed standard deviation ($\sigma{=}0.19$\,pp for CKA-only)" | 2/0.19 = 10.5×，不是 4×。若以 Standard σ=0.38 计算 = 5.3×，也不是 4×。"4×" 数字来源不明 |
| **6** | **LOW** | app.tex:308 "near-zero KL ($<$0.001)" | gen_fig_appendix_kl.py:42 RASP max=0.001119 | RASP KL 实际值有少数点 (0.001022, 0.001119, 0.001043) 略超 0.001 |
| **7** | **LOW** | app.tex:109 "CKA-only reward rises from 0.354 (peak at step 100) to 0.308 (step 300)" | 0.354 > 0.308 | "rises from X to Y" 当 X > Y 时是反向表述（语义错误，非数字错误） |
| **8** | **LOW** | app.tex:210 "Standard: 59.44--60.20\%" | 从 TOST 反推 seed 456 GRPO = 59.29 + 0.99 = **60.28**, 不是 60.20 | 范围上界与重算 0.08 pp 差异 |
| **9** | **LOW** | exp.tex:33 "~1.45B parameters" pruned | app.tex 7.62-6.16 = 1.46B | 1.45 vs 1.46 rounding |
| **10** | **VERY LOW** | exp.tex:81, related:15 "$\|\Delta\| \leq 1.8$\,pp" fine-grained | exp.tex:73 "$\|\Delta\| < 1$ pp" 20% sparsity | 不冲突：20% 是 <1 pp，1.8 是涵盖 α=2.0 时的最大值。表述兼容但需读者解读 |

### 详细分析：Issue #1（Fig 1 数据不一致）

```
              gen_fig1_dose_response.py     table3_alpha.tex / app:97-101
α=0.5  SFT/GRPO:  64.52 / 65.05    vs   60.73 / 61.18    ⚠ 差异约 4 pp!
α=1.0  SFT/GRPO:  61.49 / 60.88    vs   61.49 / 60.88    ✓ 一致
α=2.0  SFT/GRPO:  64.97 / 66.11    vs   64.97 / 66.11    ✓ 一致
α=3.0  SFT/GRPO:  64.06 / 64.59    vs   64.14 / 63.46    ⚠ GRPO 差 1.13 pp!
α=4.0  SFT/GRPO:  62.02 / 62.77    vs   61.94 / 62.77    ⚠ SFT 差 0.08 pp (微差)
```

**结论**：Fig 1 中 α=0.5 与 α=3.0 的数据明显与 Table 3 / Appendix text 不一致；α=4.0 SFT 有小差。Figure caption 的 "$|\Delta| \leq 1.14$ pp" 描述在两个数据集上都成立（因 α=2.0 给出 +1.14），所以读者不会从 caption 发现矛盾，但内部数据源不统一。

**疑似原因**：Fig 1 数据可能是早期实验值（pre-rerun）；Table 3 是后续重跑值。需检查 W&B / 原始日志确认哪个为真。

### 详细分析：Issue #2（"20% sparsity" 术语）

- `intro.tex:10`: "20\% MLP channel sparsity"
- `intro.tex:37`: "20\% sparsity"
- `intro.tex:35`: "20--25\% fine-grained MLP sparsity"
- `exp.tex:33`: "20\% structured sparsity, all removing 200 of 784 MLP channel groups across 28 layers (${\sim}$1.45B parameters)"
- `exp.tex:92`: "pruning reduces parameters by 19\%"
- `app.tex:73`: "Pruning reduces parameters by 19\%"

**数学**：
- 200/784 = **25.5%** MLP channel groups
- 1.46B/7.62B = **19.2%** total parameters
- "20%" 既不等于 25.5%（MLP channels）也不精确等于 19.2%（total params）

**推测**：作者用 "20% structured sparsity" 作为目标设定值（target sparsity），但实际去掉的 MLP groups 比例（25.5%）和总参数比例（19%）都不是 20%。在 intro 写 "20\% MLP channel sparsity" 是不准确（应该是 25.5%）。这是术语滥用，但若读者按"约 20% reduction"理解则可接受。

---

## 图表脚本数据源

| 脚本 | 输出文件 | 数据来源 | 硬编码数据点 | 论文引用 |
|------|---------|---------|-------------|---------|
| gen_fig1_dose_response.py | fig1_dose_response.pdf | 硬编码 | sft_acc=[64.52,61.49,64.97,64.06,62.02], grpo_acc=[65.05,60.88,66.11,64.59,62.77], CKA baseline=64.39 | intro.tex:16 ⚠ Issue #1 |
| gen_fig1_framework.py | fig1_framework.pdf | 硬编码 (示意图) | "+2.2pp advantage" 标注（论文文本中未提及）；"Peak 0.081" Standard, "Peak 0.061" RASP, collapse step 90 / step 10 | (论文引用 fig1_method_framework.pdf, 文件名不同；脚本与论文图可能不是同一来源) |
| gen_fig2_reward_accuracy.py | fig2_reward_accuracy.pdf | 硬编码 | RASP grpo=61.87, Standard grpo=58.91 ⚠ 与现行 Table 2 不一致 | **未被引用**（orphan figure） |
| gen_fig2_reward_trajectories.py | fig2_reward_trajectories.pdf | 硬编码 | unpruned/CKA/Random/Standard/RASP 各 step reward 序列；CKA peak 0.3544 (step 50), Standard 0.0813 (step 40), Random 0.190 (step 70), RASP 0.06125 (step 50) | exp.tex:9 ✓ |
| gen_fig3_collapse_dynamics.py | fig3_collapse_dynamics.pdf | 硬编码 | $f_0$ 与 grad_norm 序列；CKA min $f_0$=0.125, Random=0.300, Standard=0.500, RASP=0.675 | exp.tex:15 ✓ |
| gen_fig4_cka_heatmap.py | fig4_cka_heatmap.pdf | 硬编码 | 28 层 CKA(dense, pruned)；μ 实算: CKA=0.6202, Standard=0.9039, Random=0.9233, RASP=0.8822 | exp.tex:101 ✓ |
| gen_fig5_extended_training.py | fig5_extended_training.pdf | 硬编码 | Standard 300-step reward {150:0.055, 200:0.054, 250:0.058, 300:0.0562}, CKA 300-step reward {300:0.3075} 等 | exp.tex:108 ✓ |
| gen_fig_appendix_kl.py | fig_appendix_kl.pdf | 硬编码 (注释: "W&B/server logs 2026-05-18") | KL 序列；RASP max=0.001119 略超 "<0.001" claim | app.tex:303 ✓ |
| gen_fig_sft_grpo_scatter.py | fig_sft_grpo_scatter.pdf | 硬编码 | 与 Table 2/3/cross_sparsity 一致 | exp.tex:67 ✓ |
| (无脚本) | fig_intra_layer_cka.pdf | unknown | — | method.tex:28 |
| (无脚本) | fig_pruning_decisions.png | unknown | — | method.tex:114 |
| (无脚本) | fig1_method_framework.pdf | unknown (脚本 gen_fig1_framework.py 输出名不同) | — | intro.tex:42 |

---

## D类派生计算验证

| # | 位置 | 论文写的 | 推导过程 | 正确? |
|---|------|----------|---------|-------|
| 1 | concl:5 | mean \|Δ\| = 0.54 pp | (0.48+0.55+0.61+0.53)/4 = 0.5425 | ✓ |
| 2 | intro:10, exp:73, concl:5 | 4.4× peak reward gap | 0.354/0.081 = 4.37 → 4.4 | ✓ |
| 3 | exp:39, app:174, app:210 | 4.55 pp gap | 64.39-59.84 = 4.55 | ✓ |
| 4 | exp:76, app:215, app:243 | 7.20 pp gap (15%) | 72.76-65.56 = 7.20 | ✓ |
| 5 | exp:76 | 5.69 pp SFT 15% gap | 72.18-66.49 = 5.69 | ✓ |
| 6 | app:384 | +1.51 pp amplification | 7.20-5.69 = 1.51 | ✓ |
| 7 | exp:109, exp:123 | 5.5× 300-step | 0.308/0.056 = 5.50 | ✓ |
| 8 | exp:40 | 9.56 pp warmup gap | 90.83-81.27 = 9.56 | ✓ |
| 9 | exp:92, app:73 | 19% param reduction | 1.46/7.62 = 0.1916 ≈ 19% | ✓ |
| 10 | app:88 | 18% TTFT improve | (20.1-16.4)/20.1 = 18.41% | ✓ |
| 11 | app:89 | 19% per-token decrease | (72.0-58.3)/72.0 = 19.03% | ✓ |
| 12 | exp:130 | 30.5 pp cross-model | 51.50-21.00 = 30.50 | ✓ |
| 13 | exp:130 | 4.6 pp primary | 64.39-59.84 = 4.55 → 4.6 | ✓ (但 caption 用 4.62) |
| 14 | app:100 | 2.65 pp from α=2 peak | 66.11-63.46 = 2.65 | ✓ |
| 15 | method:93 | +1.72 pp α=2.0 over CKA | 66.11-64.39 = 1.72 | ✓ |
| 16 | app:132 | +1.25 pp MBPP mean | (1.34+1.07+1.34)/3 = 1.25 | ✓ |
| 17 | exp:81, tab_mbpp:16 | +4.01 pp ShortGPT MBPP | 14.44-10.43 = 4.01 | ✓ |
| 18 | intro:31, exp:81, tab2 | -1.36 pp ShortGPT GSM8K | 43.37-44.73 = -1.36 | ✓ |
| 19 | app:244 | 80.1% retention | 72.76/90.83 = 80.11% | ✓ |
| 20 | app:245 | -7.20, -8.42 Std decline | 66.49-59.29, 59.29-50.87 | ✓ |
| 21 | app:245 | -8.27, -3.79 CKA decline | 72.18-63.91, 63.91-60.12 | ✓ |
| 22 | app:213 | Random Δ -0.68, -0.53, -0.38 | 51.25-{50.57,50.72,50.87} | ✓ |
| 23 | app:212 | Random range 0.30 pp | 50.87-50.57 = 0.30 | ✓ |
| 24 | app:174, app:210 | CKA seed range 0.37 pp | 64.59-64.22 = 0.37 | ✓ |
| 25 | app:211 | Std seed range 0.76 pp | 60.20-59.44 = 0.76 | ✓ (但参见 Issue #8) |
| 26 | app:214 | 0.08 pp SFT diff | 59.29-59.21 = 0.08 | ✓ |
| 27 | app:280 | 48.60% (243/500) | 243/500 = 48.6% | ✓ |
| 28 | app:272 | 3.53 stderr | sqrt(0.515*0.485/200) = 0.0353 | ✓ |
| 29 | tab_math500 caption | 4.62 pp GSM8K SFT gap | 63.91-59.29 = 4.62 | ✓ |
| 30 | tab_math500 caption | 0.6 pp MATH GRPO gap | 27.6-27.0 = 0.6 | ✓ |
| 31 | exp:118 | 1.8 pp MATH SFT gap | 27.4-25.6 = 1.8 | ✓ |
| 32 | app:342 | 2.66, 2.35 floor drops | 64.37-{61.71, 62.02} | ✓ |
| 33 | app:342 | 0.31 pp floor 0.5/0.6 diff | 62.02-61.71 = 0.31 | ✓ |
| 34 | concl:5 | 1.8 pp max | MATH-500 α=2.0 +1.8 | ✓ |
| 35 | exp:33 | 1.45B params | 1.46B 实算 | ≈ |
| 36 | app:122 | ~8 pp α range MATH-500 | 27.8-21.6 = 6.2 | ⚠ |
| 37 | exp:78, app:374 | 4× cross-seed σ | 2/0.19 = 10.5× | ⚠ |
| 38 | intro:10, exp:33 | "20% MLP channel sparsity" | 200/784 = 25.5% | ⚠ |
| 39 | method:17 | G=7 (28/4) | 28/4 = 7 | ✓ |

---

## 总结

### 数据保真度评估
- **绝大多数数字（>95%）内部一致**：tables 之间、tables 与正文之间、tables 与脚本之间的核心数据高度一致。
- **派生计算几乎全部正确**（mean、ratio、difference、percentage 等手动验证 39 项中 36 项正确，3 项有小问题）。

### 需立即修复
1. **gen_fig1_dose_response.py** 硬编码值与 Table 3 不一致（α=0.5/3.0 显著不一致）。应统一数据源——要么重新生成 Fig 1 使用 Table 3 的值，要么修改 Table 3 / Appendix 文字使用 Fig 1 的值（前者更可能正确）。

### 建议修复
2. "20% MLP channel sparsity" 在 intro/exp 重复出现，但实际 MLP 群组比例为 25.5%。可改为 "20% structured sparsity (≈25% MLP groups, 19% total params)" 或类似精确表述。
3. App:122 "~8 pp" α SFT range 改为 "~6 pp" 更准确。
4. App:374 "4× cross-seed σ" 推导不清楚——重新检查 σ 选择或修改倍数描述。

### 风格/语义问题（非数字错误）
5. App:109 "rises from 0.354 to 0.308" 应改为 "moves between 0.354 (peak) and 0.308 (step 300)" 或类似避免方向矛盾。
6. App:308 "near-zero KL (<0.001)" 应改为 "≈0.001" 或 "<0.0012"，因实际有点超 0.001。

### Orphan / 文件管理
7. fig2_reward_accuracy.py 是 orphan（生成的 fig 不在论文中使用），且包含与现行数据不一致的硬编码值。建议删除或加注释。
8. fig1_framework.py 的输出 fig1_framework.pdf 与论文引用的 fig1_method_framework.pdf 文件名不一致，并含 "+2.2pp advantage" 等论文不再使用的旧文案。需确认论文用的 fig1_method_framework.pdf 是哪个版本/由哪个脚本生成。
