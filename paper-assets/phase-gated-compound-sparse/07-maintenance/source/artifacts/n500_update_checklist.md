# n=500 更新清单

> 论文：Phase-Modulated Compound Sparsity (EMNLP 2026 ARR)
> 当前数据：n=50 MATH-500（DeepSeek n=49, Qwen n=46, LLaMA n=49）
> 目标数据：n=500 MATH-500
> 生成日期：2026-05-14
> 硬约束：D054 (median only), D059 (within-imp d_z only), D015 (emergent interaction framing), D056 (C5b→future work), D060 (LLaMA→suggests)

---

## 统计汇总

| 分类 | 数量 |
|------|------|
| data_update（数字替换） | 48 |
| figure_update（重新生成） | 5 |
| claim_update（措辞调整） | 11 |
| structural（结构变动） | 4 |
| constraint_check（硬约束合规） | 6 |
| **总计** | **74** |

---

## §0 Abstract (abstract.tex)

### A01 [data_update] Line 6 — 样本量
- **当前**: `50 MATH-500 problems`
- **替换**: `500 MATH-500 problems`
- **依赖**: n=500 DeepSeek/Qwen 有效样本量（扣除 degenerate phase 后实际 n）

### A02 [data_update] Line 7 — DeepSeek 主结果
- **当前**: `median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$`
- **替换**: n=500 DeepSeek importance Δ 值（4 个 sparsity level）
- **来源**: experiment_summary_table.json → median_diff

### A03 [data_update] Line 7 — DeepSeek d_z 和 p
- **当前**: `paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$`
- **替换**: n=500 DeepSeek within-importance paired d_z（4 值）+ 新 p-values
- **注意**: D059 — 此处 d_z 是 within-importance (low−high)，合规 ✓

### A04 [data_update] Line 8 — Random baseline 统计
- **当前**: `Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$)`
- **替换**: n=500 random 条件的 PASS/FAIL 计数 + 例外条件的 p 和效应量
- **注意**: D059 — random 条件不报 d_z，改为 Wilcoxon p + median_diff

### A05 [data_update] Line 9 — Crossover 数值
- **当前**: `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` 和 `$7.196$ vs.\ $1.363$`
- **替换**: n=500 s=0.25 crossover 的 4 个 II 中位数

### A06 [data_update] Line 10 — Qwen 复现
- **当前**: `$d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$`
- **替换**: n=500 Qwen within-importance d_z + Spearman ρ + permutation p

### A07 [data_update] Line 10 — LLaMA 数值
- **当前**: `$d_z$ ($0.19 \to 0.34$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}} = 0.029$)`
- **替换**: LLaMA 数据未变（n=49），但需确认是否也跑 n=500
- **注意**: D059 违规 ⚠️ — 此 d_z 是 imp-vs-rand，应改为 Wilcoxon p + median_diff
- **注意**: D060 — 当前用 "suggests"，合规 ✓

### A08 [data_update] Line 10 — LLaMA 倍数比
- **当前**: `${\sim}$1/40 the absolute magnitude`
- **替换**: 用 n=500 DeepSeek 数据重算 LLaMA/DeepSeek 比值

---

## §1 Introduction (introduction.tex)

### I01 [data_update] Line 14 — DeepSeek 主结果
- **当前**: `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$; Bonferroni-corrected $p < 0.005$)`
- **替换**: 与 A02/A03 同步

### I02 [data_update] Line 15 — Qwen d_z
- **当前**: `$d_z \geq 0.55$`
- **替换**: n=500 Qwen within-importance d_z 下界

### I03 [data_update] Line 15 — LLaMA 倍数
- **当前**: `$\sim$1/40 the magnitude`
- **替换**: 与 A08 同步

### I04 [data_update] Line 16 — Random PASS/FAIL 统计
- **当前**: `7/8 conditions non-significant`
- **替换**: n=500 random PASS/FAIL 计数

---

## §4 Experimental Setup (methodology.tex)

### M01 [data_update] Line 10 — 样本量
- **当前**: `50 problems stratified from MATH-500`
- **替换**: `500 problems from MATH-500`（去掉 "stratified"，500 ≈ 全集）

### M02 [data_update] Line 18 — 偏度统计
- **当前**: `mean/median ratios up to 43:1`
- **替换**: n=500 的 mean/median ratio
- **注意**: D054 — 此处引用 mean/median 比作为选择 median 的理由，合规 ✓

### M03 [data_update] Line 22 — p-value 总结
- **当前**: `All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.`
- **替换**: n=500 permutation test 结果

---

## §5 Results (results.tex)

### R01 [data_update] Lines 8 — §5.1 aggregate Δ
- **当前**: `$\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification`
- **替换**: n=500 Δ 值 + 新倍数

### R02 [data_update] Line 8 — Random Δ 范围
- **当前**: `$-0.02$ to $1.54$`
- **替换**: n=500 random Δ 范围

### R03 [data_update] Line 13 — Table 1 标题样本量
- **当前**: `$n{=}50$ MATH-500 problems`
- **替换**: `$n{=}500$`（或实际有效 n）

### R04 [data_update] Lines 19-20 — Table 1 (aggregate-ii) 全部数据
- **当前**:
  ```
  Importance & 0.39 & 1.48 & 7.16 & 14.59
  Random     & 0.01 & −0.02 & 0.54 & 1.54
  ```
- **替换**: n=500 median Δ 值（8 个数字）

### R05 [data_update] Line 29 — §5.2 severity gradient G
- **当前**: `$69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$`
- **替换**: n=500 G 值
- **注意**: D031/D033 决定 gradient ratio 仅作辅助描述；确认 n=500 是否仍报 G

### R06 [data_update] Line 29 — high-phase II 范围
- **当前**: `$\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$`
- **替换**: n=500 high-phase median II 范围

### R07 [data_update] Line 29 — Random G 范围
- **当前**: `$G \approx 0.9$--$1.7{\times}$`
- **替换**: n=500 random G 范围

### R08 [data_update] Lines 34, 40-50 — Table 2 (main-results) 全部数据
- **当前**: "50 problems" + 24 个数据单元格（6列×4组）
- **替换**: n=500 全部 per-phase median II + Δ + G（24 个数字 + caption 中 n）

### R09 [figure_update] Lines 55-60 — Figure 1 (fig1_dose_response.pdf)
- **当前**: 基于 n=50 bf16 数据
- **操作**: 用 n=500 数据重新生成 fig1_dose_response.pdf
- **注意**: caption 中 "$69{\times}$ to $274{\times}$" 需同步更新

### R10 [data_update] Line 66 — §5.3 Crossover 数值
- **当前**: `$0.032$ vs.\ $0.818$`, `$7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal`
- **替换**: n=500 s=0.25 crossover 值 + 倍数

### R11 [data_update] Line 71 — §5.4 Qwen Δ 范围
- **当前**: `$\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$`
- **替换**: n=500 Qwen Δ 值

### R12 [data_update] Line 71 — DeepSeek/Qwen 倍数比
- **当前**: `${\sim}1/5$ the magnitude`
- **替换**: n=500 Qwen/DeepSeek 比值

### R13 [data_update] Line 71 — Qwen 统计
- **当前**: `Spearman $\rho = 1.0$; gradient permutation $p = 0.043$`
- **替换**: n=500 Qwen 对应统计量

### R14 [data_update] Line 71 — Qwen s015 d_z
- **当前**: `$d_z{=}0.28$, CI includes zero`
- **替换**: n=500 Qwen s015 d_z + CI
- **注意**: D052 预注册——若 s015 仍 ns，叙事改为 "emerges above threshold"

### R15 [data_update] Line 71 — Qwen d_z 下界
- **当前**: `$d_z \geq 0.55$`
- **替换**: n=500 Qwen s≥0.20 d_z 值

### R16 [data_update] Line 77 — §5.5 LLaMA 样本量
- **当前**: `$n{=}49$ paired problems`
- **替换**: 确认 LLaMA 是否也跑 n=500；若仍 n=49 则保留

### R17 [constraint_check] Lines 79 — §5.5 LLaMA d_z（D059 违规 ⚠️）
- **当前**: `monotonically increasing paired $d_z$ ($0.19 \to 0.26 \to 0.29 \to 0.34$)`
- **问题**: 此 d_z 是 imp-vs-rand paired Cohen's d，D059 禁止报告
- **修改**: 删除 imp-vs-rand d_z，改为 Wilcoxon p + median_diff

### R18 [constraint_check] Lines 79 — LLaMA within-importance d_z
- **当前**: `within-strategy phase gradient $d_z$ (low $-$ high) is consistently large at all sparsity levels ($d_z \in [1.00, 1.12]$)`
- **状态**: 合规 ✓（within-importance），数值可能需更新（若 LLaMA 重跑）

### R19 [constraint_check] Lines 79 — LLaMA random d_z
- **当前**: `$d_z \in [0.35, 0.45]$`
- **问题**: D059 — random 不报 d_z
- **修改**: 改为 "random eviction also shows non-trivial phase gradient" + Wilcoxon p

### R20 [data_update] Lines 81 — LLaMA 倍数比
- **当前**: `${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen`
- **替换**: 用 n=500 DeepSeek/Qwen 数据重算比值

### R21 [structural] Lines 83-98 — Table 3 (llama-cross-arch) 重构
- **当前**: d_z 列报告 imp-vs-rand Cohen's d
- **问题**: D059 违规 — 整列需要替换
- **修改**: d_z 列改为 within-importance d_z（或删除 d_z 列，改为 Wilcoxon p + median_diff）
- **数据**: 若 LLaMA 不重跑，数值不变但列定义需改

### R22 [data_update] Lines 92-95 — Table 3 数据行
- **当前**: 4 行 (d_z, Δ̃ [CI], p_Bonf)
- **替换**: 若 LLaMA 重跑则全部更新；若不重跑，仅结构变动

### R23 [data_update] Line 104 — §5.6 permutation test 结果
- **当前**: `$p_{\text{Bonf}} < 0.005$`, `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$`
- **替换**: n=500 permutation test 统计

### R24 [data_update] Lines 106 — DeepSeek d_z 范围
- **当前**: `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)`
- **替换**: n=500 DeepSeek within-importance d_z

### R25 [data_update] Lines 106 — Qwen d_z
- **当前**: `$d_z{=}0.28$, CI includes zero`, `$d_z \geq 0.55$`, `$d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$`
- **替换**: n=500 Qwen d_z 值

### R26 [data_update] Lines 113-123 — Table 4 (cohens-d) 全部数据
- **当前**: 4 行 × (DS d_z, Δ̃ [CI], QW d_z, Δ̃ [CI])
- **替换**: n=500 paired d_z + bootstrap Δ̃ + CI（16 个数字）

---

## §6 Analysis (analysis.tex)

### AN01 [data_update] Line 4 — Gini 系数范围
- **当前**: `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)`
- **替换**: n=500 Gini Δ 范围（若 C4 entropy 分析基于 n=500 重跑）
- **注意**: C4 已降为 supporting analysis (D045/D046)，数值可能不变

### AN02 [data_update] Line 6 — DeepSeek entropy Δ 范围
- **当前**: `$\Delta\mathcal{H} \in [-0.047, -0.040]$`
- **替换**: 若 C4 基于 n=500 重跑则更新

### AN03 [data_update] Line 6 — Qwen entropy 反转
- **当前**: `$s{=}0.25$ ($\Delta\mathcal{H} = +0.045$)`
- **替换**: 若 C4 基于 n=500 重跑则更新

---

## §7 Discussion (discussion.tex)

### D01 [data_update] Line 5 — Gradient 范围
- **当前**: `$69$--$274{\times}$`
- **替换**: 与 R05 同步

### D02 [data_update] Line 5 — Crossover 数值
- **当前**: `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` 和 `$7.196$ vs.\ $1.363$`
- **替换**: 与 R10 同步

### D03 [data_update] Line 11 — LLaMA 倍数
- **当前**: `${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen`
- **替换**: 与 R20 同步

### D04 [constraint_check] Line 11 — LLaMA d_z（D059 违规 ⚠️）
- **当前**: `within-strategy phase gradient $d_z \geq 1.0$`
- **状态**: 这是 within-importance d_z，合规 ✓

### D05 [constraint_check] Line 11 — LLaMA random d_z（D059 违规 ⚠️）
- **当前**: `$d_z \in [0.35, 0.45]$`
- **修改**: 与 R19 同步——删除 d_z，改为定性描述 + Wilcoxon p

### D06 [claim_update] Line 11 — LLaMA 语言（D060）
- **当前**: `provides partial support for the qualitative pattern`
- **状态**: 合规 ✓（"partial support"）

---

## §8 Conclusion (conclusion.tex)

### C01 [data_update] Line 4 — Gradient 范围
- **当前**: `$69{\times}$ to $274{\times}$`
- **替换**: 与 R05 同步

### C02 [data_update] Line 4 — d_z 范围
- **当前**: `$d_z$: $0.44 \to 0.80$`
- **替换**: 与 R24 同步

### C03 [data_update] Line 4 — Random PASS/FAIL
- **当前**: `7/8 conditions non-significant`
- **替换**: 与 I04 同步

### C04 [data_update] Line 4 — Qwen d_z
- **当前**: `$d_z \geq 0.55$`
- **替换**: 与 R15 同步

### C05 [data_update] Line 4 — LLaMA 倍数
- **当前**: `$\sim$1/40 the magnitude`
- **替换**: 与 A08 同步

### C06 [constraint_check] — C5b future work（D056）
- **当前**: `These findings motivate phase-aware sparsity allocation for reasoning model deployment.`
- **状态**: 合规 ✓ — 作为 motivation 而非 contribution claim

---

## Limitations (limitations.tex)

### L01 [data_update] Line 1 — 架构描述
- **状态**: 无直接 n=50 数据，无需数字更新

### L02 [claim_update] Line 4 — 样本量描述
- **当前**: 未直接提及 n=50，但 "exclusively on MATH-500" 成立
- **替换**: n=500 后可加 "using 500 problems from MATH-500"

---

## Appendix A (appendix.tex) — Formulation + Multiplicative Null

### AP01 [data_update] Line 38 — Multiplicative null G 范围
- **当前**: `$G_{\times} = 58$--$241{\times}$`
- **替换**: n=500 multiplicative null G 值（需重算）

---

## Appendix B (appendix_results.tex) — Cross-Model Summary

### AR01 [data_update] Line 7 — Per-problem concordance
- **当前**: `mean $\rho = -0.11$, $p = 0.926$`
- **替换**: n=500 cross-model concordance（Spearman ρ + p）

### AR02 [data_update] Line 10 — Random PASS/FAIL 模式
- **当前**: `3/4 FAIL`, `4/4 FAIL`
- **替换**: n=500 random PASS/FAIL 计数

### AR03 [data_update] Line 10 — Qwen random s030 例外
- **当前**: `$p = 0.012$`, `$d_z = -0.04$`
- **替换**: n=500 结果
- **注意**: D059 — 不报 d_z，改为 Wilcoxon p + median_diff

---

## Appendix C (appendix_moved.tex) — Crossover + Cross-Model + Permutation + Analysis

### AM01 [data_update] Line 11 — Crossover 全部数值
- **当前**: `$0.032$ vs.\ $0.818$`, `$7.196$ vs.\ $1.363$`, `$5.3{\times}$`, `$3.9{\times}$, $5.4{\times}$, $5.3{\times}$, $3.6{\times}$`
- **替换**: n=500 crossover 值（所有 4 个 sparsity level 的 reversal magnitude）

### AM02 [figure_update] Lines 13-18 — Figure 3 (fig3_crossover.pdf)
- **操作**: 用 n=500 数据重新生成
- **caption**: `$5.3{\times}$` 需同步更新

### AM03 [data_update] Line 26 — Qwen 排除数
- **当前**: `Four of the 50 problems are excluded`, `$n{=}46$`, `$n{=}49$`
- **替换**: n=500 的 DeepSeek/Qwen 有效 n

### AM04 [data_update] Lines 39-40 — Table (cross-model) 全部数据
- **当前**: DeepSeek [0.39, 1.48, 7.16, 14.59], Qwen [0.04, 0.23, 1.27, 2.94]
- **替换**: n=500 median Δ 值（8 个数字）

### AM05 [figure_update] Lines 45-50 — Figure 5 (fig5_crossmodel.pdf)
- **操作**: 用 n=500 数据重新生成
- **caption**: "one-fifth" 比例需同步更新

### AM06 [data_update] Lines 52-53 — Per-problem concordance（重复 AR01）
- **替换**: 与 AR01 同步

### AM07 [data_update] Lines 55-56 — Random PASS/FAIL（重复 AR02/AR03）
- **替换**: 与 AR02/AR03 同步

### AM08 [data_update] Lines 62, 73 — Permutation test 样本量
- **当前**: `$n{=}49$`
- **替换**: n=500 有效 n

### AM09 [data_update] Lines 68 — CI lower bounds
- **当前**: `$0.19 \to 0.69 \to 1.66 \to 6.70$`
- **替换**: n=500 CI lower bounds

### AM10 [data_update] Lines 79-82 — Table (permutation) 全部数据
- **当前**: 4 行 (observed Δ̃, 95% CI, p_Bonf)
- **替换**: n=500 permutation test 结果（12 个数字）

### AM11 [figure_update] Lines 87-92 — Figure 4 (fig4_bootstrap.pdf)
- **操作**: 用 n=500 数据重新生成

### AM12 [data_update] Lines 111-122 — Table (discrimination-metrics-full) 全部数据
- **当前**: 8 行 (ΔGini, ΔCV)
- **替换**: 若 C4 分析基于 n=500 重跑则更新（16 个数字）

### AM13 [data_update] Lines 137-139 — Entropy delta 描述
- **当前**: DeepSeek `$\Delta\mathcal{H} \in [-0.047, -0.040]$`, Qwen s025 `$+0.045$`
- **替换**: 若 C4 分析基于 n=500 重跑则更新

### AM14 [data_update] Lines 149-162 — Table (entropy-deltas) 全部数据
- **当前**: 8 行
- **替换**: 若 C4 分析基于 n=500 重跑则更新

---

## Appendix D (appendix_disc_analysis.tex) — Extended Discussion + Limitations

### AD01 [data_update] Line 4 — Random Gini 范围
- **当前**: `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$`
- **替换**: 若 C4 基于 n=500 重跑则更新

### AD02 [data_update] Line 11 — High-phase II 上限
- **当前**: `$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$`; `$s = 0.35$, high-phase II rises to $0.105$`
- **替换**: n=500 high-phase median II 值

### AD03 [data_update] Line 14 — Random 7/8 统计
- **当前**: `7/8`, `$p{=}0.012$`, `$d_z{=}{-}0.04$`
- **替换**: 与 A04 同步
- **注意**: D059 — 不报 d_z

### AD04 [data_update] Lines 44-47 — 统计范围详情
- **当前**: `$n{=}49$ ... $n{=}46$`, mean/median ratio `${\sim}1.6{:}1$`, permutation CI 值
- **替换**: n=500 统计

### AD05 [data_update] Line 49 — Qwen random s030 例外
- **当前**: `$p{=}0.012$`, `$d_z{=}{-}0.04$`
- **替换**: 与 AR03 同步
- **注意**: D059 — 不报 d_z

### AD06 [data_update] Lines 53-57 — Growth rate 描述
- **当前**: `$3.8{\times} \to 4.8{\times} \to 2.0{\times}$`
- **替换**: n=500 Δ growth rate

---

## 图表重新生成清单

| # | 文件名 | 数据来源 | 引用位置 |
|---|--------|----------|----------|
| F1 | fig1_dose_response.pdf | n=500 DeepSeek imp+rand G vs s | results.tex:57, caption:58 |
| F2 | fig3_crossover.pdf | n=500 DeepSeek s=0.25 crossover | appendix_moved.tex:15 |
| F3 | fig4_bootstrap.pdf | n=500 permutation test forest plot | appendix_moved.tex:89 |
| F4 | fig5_crossmodel.pdf | n=500 DeepSeek+Qwen Δ comparison | appendix_moved.tex:47 |
| F5 | (unnamed hero figure if separate) | 确认是否与 fig1 相同 | results.tex:57 |

---

## 硬约束合规审查

### HC01 [D054] II 只报 median + median bootstrap CI ✅
- abstract/results/discussion 全文使用 median ($\widetilde{\mathrm{II}}$)
- methodology.tex:18 提及 mean/median ratio 作为选择 median 的理由 ✓
- **注意**: n=500 更新时确认所有新数字均为 median

### HC02 [D059] d_z 只报 within-importance ⚠️ 6 处违规
| 位置 | 当前内容 | 问题 |
|------|---------|------|
| abstract.tex:8 | random `$d_z{=}{-}0.04$` | imp-vs-rand d_z |
| results.tex:79 | LLaMA `$d_z$ ($0.19 \to 0.34$)` | imp-vs-rand d_z |
| results.tex:79 | random `$d_z \in [0.35, 0.45]$` | random d_z |
| results.tex:88-97 | Table 3 d_z 列 | imp-vs-rand d_z |
| discussion.tex:11 | `$d_z \in [0.35, 0.45]$` | random d_z |
| appendix_disc_analysis.tex:14,49 | `$d_z{=}{-}0.04$` | random d_z |

**修改方案**: 所有 imp-vs-rand 和 random d_z 替换为 Wilcoxon p + median_diff；Table 3 d_z 列替换为 within-importance d_z 或移除

### HC03 [D015] Framing: emergent phase-strategy interaction ✅
- abstract.tex:4 使用 "emergent phase-strategy interaction" ✓
- 全文无 "importance is broken" 叙事 ✓

### HC04 [D056] C5b 已降为 §8 future work ✅
- discussion.tex:8 讨论 phase-aware budget 作为 implication（未 claim 实现）✓
- conclusion.tex:5 "motivate phase-aware sparsity allocation" ✓
- **注意**: D056 确认 c5b_pilot gate_failed (oracle 18% < 30%)，论文不应 claim C5b 成功

### HC05 [D060] C8 LLaMA 用 suggests/partial support ✅
- abstract.tex:10 "suggests cross-architecture generalization" ✓
- discussion.tex:11 "provides partial support" ✓
- conclusion.tex:4 "partially extends" ✓
- results.tex:77-81 "The qualitative pattern replicates" — **borderline**，建议改为 "The qualitative pattern is directionally consistent"

### HC06 [硬约束 #6] Random 也有正 II，区分信号是 gradient ✅
- results.tex Table 2 显示 random 有正 II ✓
- 叙事正确区分："compound severity depends qualitatively on eviction strategy" ✓
- **注意**: n=500 random 数据可能有不同 pattern，需重新验证此叙事

---

## 按 Section 分布

| Section | 更新点数 |
|---------|---------|
| Abstract | 8 |
| Introduction | 4 |
| Methodology | 3 |
| Results | 26 |
| Analysis | 3 |
| Discussion | 6 |
| Conclusion | 6 |
| Limitations | 2 |
| Appendix (formulation) | 1 |
| Appendix (results summary) | 3 |
| Appendix (moved content) | 14 |
| Appendix (disc+limitations) | 6 |
| **Total** | **82** (含重复引用) |
| **Unique** | **~70** |

---

## 高风险点（可能需要改叙事）

### RISK-1: Qwen s015 是否仍然 non-significant
- D052 预注册：若 n=500 Qwen s015 仍 ns，叙事改为 "compound effect emerges above a model-dependent threshold"
- D061 已确认 n=500 下 Qwen s015 显著 (p<0.0001)——**如果最终数据确认，此风险解除**
- 影响范围：abstract, introduction, results §5.4, §5.6, conclusion

### RISK-2: Random PASS/FAIL 模式可能变化
- n=50 下 7/8 FAIL（Qwen s030 borderline PASS d≈0）
- n=500 功效更高，可能检测到更多 borderline 显著
- 影响范围：需重新评估 "no significant phase modulation" 叙事
- D059 保护：不报 random d_z，用 Wilcoxon p + median_diff 更 robust

### RISK-3: LLaMA 数据是否跑 n=500
- 当前 LLaMA 仅 n=49
- 若不重跑：DeepSeek/Qwen 倍数比需重算（分母变了）
- 若重跑：全部 LLaMA 数据需更新

### RISK-4: D059 Table 3 重构
- Table 3 (llama-cross-arch) 的核心组织方式围绕 imp-vs-rand d_z
- 删除 d_z 列后需要替代结构，可能影响 §5.5 整段叙事

### RISK-5: Crossover pattern 在 n=500 是否稳定
- crossover 是论文的一个 key finding
- n=500 的 crossover 倍数和位置可能变化
- 影响范围：abstract, results §5.3, discussion, appendix

### RISK-6: C4 entropy 分析是否需要基于 n=500 重跑
- 当前 C4 降级为 supporting analysis (D045/D046)
- 若不重跑：analysis.tex 和 appendix 表格保留 n=50 数据，需标注
- 若重跑：AN01-AN03, AM12-AM14, AD01 全部更新

---

## P2: 新增内容（此前遗漏）

### NEW-1 [P2/structural] C5b Pilot 结果段落 — 当前完全缺失
- **问题**: paper_framing (D056) 要求论文 §6 Discussion 诚实报告 C5b pilot 结果 + future work。当前 discussion.tex 仅在 "Implications for deployment" 泛泛提及 "phase-aware compression budget" 但未报告 pilot 数值。
- **当前文本** (discussion.tex:7-8): `A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains.`
- **需要插入**: discussion.tex 的 "Implications for deployment" 段落末尾（Line 8 之后），或 conclusion.tex 末尾新增 "Future Work" 段落
- **内容**: 报告 C5b pilot: oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但 95% CI 均跨零，未达 30% recovery gate。明确声明 phase-aware mitigation 是 future work，需更精细 phase boundary estimation。可提及 heuristic > oracle 悖论暗示 phase boundary 最优粒度是开放问题。
- **来源**: paper_framing.md RC3, D056

### NEW-2 [P2/claim_update] Qwen Mid-Phase 45.2% Null Rate Caveat — 当前完全缺失
- **问题**: Qwen 在 mid-phase 有 45.2% 的 null rate（II=0 的 problem 比例），论文未提及此 caveat。
- **影响**: 当论文报告 Qwen mid-phase II 中位数时，读者不知道近半数 problem 在该 phase 无 compound interaction。
- **插入位置选项**:
  - (a) results.tex §5.4 (cross-model, Line 71 附近): 在 Qwen 数据描述后添加 "Qwen mid-phase measurements are attenuated by a 45.2% null rate (II=0), reflecting problems where compound interaction is absent in intermediate phases."
  - (b) appendix_moved.tex §Cross-Model (Line 26 附近): 在 Qwen exclusion 描述后添加
  - (c) limitations.tex: 新增段落
- **推荐**: 选项 (a)——在 §5.4 提及，不隐藏到 appendix

### NEW-3 [P1/claim_update] "mean ρ" 残留 — 疑似 D054 边界违规
- **位置 1**: appendix_results.tex:7 — `mean $\rho = -0.11$`
- **位置 2**: appendix_moved.tex:53 — `mean $\rho = -0.11$`（重复内容）
- **问题**: D054 禁用 mean。虽然这里是 Spearman ρ 的均值而非 II 的 mean，但为避免 reviewer 质疑，建议改为 `median $\rho$` 或改措辞为 "per-problem Spearman correlations averaged across conditions ($\bar{\rho} = -0.11$)"，明确不是 II 的 mean。
- **优先级**: P1（措辞调整）

### NEW-4 [P1/claim_update] results.tex:77 — "The qualitative pattern replicates" 措辞强度
- **当前**: `The qualitative pattern replicates`
- **问题**: D060 要求 LLaMA claim 用 "suggests"/"provides partial support"。"replicates" 过强。
- **改为**: `The qualitative direction is consistent` 或 `The directional pattern is consistent`
- **位置**: results.tex Line 77（§5.5 Cross-Architecture 第一句）

---

## 更新后统计汇总

| 分类 | 数量 |
|------|------|
| data_update（数字替换） | 48 |
| figure_update（重新生成） | 5 |
| claim_update（措辞调整） | 11 (+3) |
| structural（结构变动） | 4 (+1) |
| constraint_check（硬约束合规） | 6 |
| **总计** | **74** |
