# Paper Update Checklist: n=50 → n=500

> 生成时间: 2026-05-15 (v2, 全文逐行扫描) | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)
> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不 claim 显著直到 n=500 确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)
> LLaMA (c3_llama, n=50) 和 c4_entropy (n=30) 不在 n=500 范围内

---

## A. 必须更新 — "50" → "500" 文字提及

| # | 文件:行 | 当前文本 | 更新说明 |
|---|--------|---------|---------|
| A1 | abstract.tex:6 | "using 50 MATH-500 problems" | → "500 MATH-500 problems"；注意 LLaMA 仍为 n=50，需分述或脚注 |
| A2 | methodology.tex:10 | "We use 50 problems stratified from MATH-500" | → "We use the full MATH-500 benchmark (500 problems)"；sampling 描述也需改 |
| A3 | results.tex:13 | Table 1 caption: "($n{=}50$ MATH-500 problems)" | → "($n{=}500$...)" |
| A4 | results.tex:34 | Table 2 caption: "medians across 50 problems" | → "500 problems" |
| A5 | appendix_moved.tex:26 | "Four of the 50 problems are excluded" | → "X of the 500 problems"（X 待定） |

## B. 必须更新 — 配对样本量 n=49 / n=46

| # | 文件:行 | 当前值 | 更新说明 |
|---|--------|-------|---------|
| B1 | appendix_disc_analysis.tex:45 | "n{=}49 for DeepSeek (1 excluded) and n{=}46 for Qwen (4 excluded)" | → 新 exclusion 数 |
| B2 | appendix_moved.tex:26 | "n{=}46 valid problems for Qwen (vs. n{=}49 for DeepSeek)" | → 新值 |
| B3 | appendix_moved.tex:93 | Table 7 caption: "n{=}49" | → 新 DS 配对数 |

> ⚠️ **不动**: results.tex:77 的 "n{=}49" 是 LLaMA cross-arch 数据。

---

## C. 必须更新 — DeepSeek 数值（bf16 n=50 → n=500）

### C1. Abstract 内联 (abstract.tex)
- [ ] **L7**: median Δ "$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$"
- [ ] **L7**: d_z "from $0.44$ (small) to $0.80$ (large)"

### C2. Introduction 内联 (introduction.tex)
- [ ] **L14**: "$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$)"

### C3. Results §5.1 (results.tex:5-8)
- [ ] Δ: "$0.39$... to $14.59$... a $37{\times}$ amplification"
- [ ] Random: "$-0.02$ to $1.54$"

### C4. Table 1 — tab:aggregate-ii (results.tex:16-22)
- [ ] **Importance 行**: 0.39 / 1.48 / 7.16 / 14.59
- [ ] **Random 行**: 0.01 / −0.02 / 0.54 / 1.54

### C5. Results §5.2 (results.tex:29)
- [ ] G: "$69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$"
- [ ] II_high: "$0.006$ to $0.053$"
- [ ] Random G: "$G \approx 0.9$--$1.7{\times}$"

### C6. Table 2 — tab:main-results (results.tex:36-53)
全部 32 个数据格（8 rows × II_high/II_mid/II_low/Δ） + 8 个 G 值

| 行 | II_high | II_mid | II_low | Δ | G |
|----|---------|--------|--------|---|---|
| s015 Imp | 0.006 | 0.081 | 0.398 | 0.39 | 69 |
| s015 Rand | 0.093 | 0.097 | 0.103 | 0.01 | 1.1 |
| s020 Imp | 0.015 | 0.203 | 1.496 | 1.48 | 103 |
| s020 Rand | 0.292 | 0.350 | 0.276 | −0.02 | 0.9 |
| s025 Imp | 0.032 | 1.118 | 7.196 | 7.16 | 222 |
| s025 Rand | 0.818 | 0.932 | 1.363 | 0.54 | 1.7 |
| s030 Imp | 0.053 | 2.283 | 14.639 | 14.59 | 274 |
| s030 Rand | 2.503 | 2.592 | 4.041 | 1.54 | 1.6 |

### C7. Figure 1 caption (results.tex:58)
- [ ] "$69{\times}$ to $274{\times}$"

### C8. Results §5.3 Crossover (results.tex:62-66)
- [ ] s=0.25: "$0.032$ vs. $0.818$" (high) / "$7.196$ vs. $1.363$" (low)

### C9. Results §5.6 Stat Validation (results.tex:100-102)
- [ ] Permutation Δ: "from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$"

### C10. Table 3 — tab:cohens-d, DS 列 (results.tex:117-120)
| s | d_z | Δ̃ | CI |
|---|-----|----|----|
| 0.15 | 0.44 | 0.32 | [0.20, 0.47] |
| 0.20 | 0.52 | 1.15 | [0.66, 1.26] |
| 0.25 | 0.68 | 3.97 | [2.83, 5.29] |
| 0.30 | 0.80 | 9.94 | [8.39, 16.65] |

### C11. Conclusion (conclusion.tex:4)
- [ ] "$69{\times}$ to $274{\times}$... ($d_z$: $0.44 \to 0.80$)"

### C12. Discussion (discussion.tex:3-4)
- [ ] "$69$--$274{\times}$"
- [ ] Crossover: "$0.032$ vs. $0.818$" / "$7.196$ vs. $1.363$"

### C13. Appendix Crossover (appendix_moved.tex:11)
- [ ] "$0.032$ vs. $0.818$" / "$7.196$ vs. $1.363$—a $5.3{\times}$ reversal"
- [ ] Reversal magnitudes: "$3.9{\times}$, $5.4{\times}$, $5.3{\times}$, $3.6{\times}$"
- [ ] Fig caption (L17): "$5.3{\times}$"

### C14. Appendix Permutation (appendix_moved.tex:86-105)
- [ ] L86: "99.92th percentile... p_Bonf = 0.0032"
- [ ] L88: inline Δ: "$0.37$... to $9.85$"
- [ ] L88: CI lower bounds: "$0.19 \to 0.69 \to 1.66 \to 6.70$"
- [ ] Table 7 (tab:permutation) — 全部 4 行:

| s | Observed Δ̃ | 95% CI | p_Bonf |
|---|-----------|--------|--------|
| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 |
| 0.20 | 0.97 | [0.69, 1.49] | <0.001 |
| 0.25 | 3.34 | [1.66, 6.64] | <0.001 |
| 0.30 | 9.85 | [6.70, 16.29] | <0.001 |

### C15. Appendix Cross-Model Table (appendix_moved.tex:60)
- [ ] Table 5 (tab:cross-model) DS 行: 0.39 / 1.48 / 7.16 / 14.59

### C16. Appendix Extended Discussion (appendix_disc_analysis.tex:9)
- [ ] "II_high < 0.06 at s ≤ 0.30; at s=0.35, high-phase II rises to 0.105"

### C17. Appendix Statistical Scope (appendix_disc_analysis.tex:45-50)
- [ ] mean/median ratio ~1.6:1
- [ ] Comments: "mean_diff=22.94, median_diff=14.59", "median_diff=9.9436"
- [ ] Permutation CIs in comment: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]

---

## D. 必须更新 — Qwen 数值

### D1. Table 3 — tab:cohens-d, QW 列 (results.tex:117-120)
| s | d_z | Δ̃ | CI |
|---|-----|----|----|
| 0.15 | 0.28 | 0.05 | [−0.01, 0.11]^ns |
| 0.20 | 0.55 | 0.21 | [0.07, 0.40] |
| 0.25 | 0.89 | 1.11 | [0.61, 1.47] |
| 0.30 | 1.02 | 2.62 | [1.72, 3.65] |

### D2. Results §5.4 Cross-Model (results.tex:71)
- [ ] "$\Delta$ increases from $0.04$... to $2.94$"
- [ ] "$d_z{=}0.28$, CI includes zero"
- [ ] "$d_z \geq 0.55$"

### D3. Abstract/Introduction/Conclusion Qwen 内联
- [ ] abstract.tex:10 — "$d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$"
- [ ] introduction.tex:15 — "$d_z \geq 0.55$"
- [ ] conclusion.tex:4 — "$d_z \geq 0.55$"

### D4. Appendix Cross-Model (appendix_moved.tex)
- [ ] Table 5 (tab:cross-model) QW 行: 0.04 / 0.23 / 1.27 / 2.94
- [ ] L48: "at ~1/5 of DeepSeek's magnitude" → 新比例
- [ ] fig:cross-model caption (L69): "one-fifth of DeepSeek's" → 新比例

---

## E. 必须更新 — 图表重新生成

| # | 文件名 | Label | 内容 | 数据来源 |
|---|--------|-------|------|---------|
| E1 | fig1_dose_response.pdf | fig:hero | G vs s + 95% CI shading | experiment_summary_table.json |
| E2 | fig3_crossover.pdf | fig:crossover | s=0.25 crossover bars | experiment_summary_table.json |
| E3 | fig4_bootstrap.pdf | fig:permtest-forest | permutation forest plot | permutation_test_results.json |
| E4 | fig5_crossmodel.pdf | fig:cross-model | DS vs QW Δ curves | cross_model_analysis.json |

---

## F. 必须填入 — 现有 \placeholder{} 值

### F1. 从 n=500 Qwen 数据填入
| # | 文件:行 | Placeholder | 说明 |
|---|--------|-------------|------|
| F1a | abstract.tex:8 | `\placeholder{}` | Qwen s030 random Δ̃ |
| F1b | results.tex:71 | `\placeholder{NULL_PCT}` | Qwen mid-phase null rate % |
| F1c | appendix_moved.tex:30 | `\placeholder{NULL_PCT}` | 同 F1b |
| F1d | appendix_moved.tex:35 | `\placeholder{N_QW}` | Qwen 总有效 n |
| F1e | appendix_moved.tex:41-43 | 12× `\placeholder{}` | Qwen per-phase effective n (3 phase × 4 sparsity) |
| F1f | appendix_disc_analysis.tex:14 | `\placeholder{}` | Qwen random Δ̃ |
| F1g | appendix_disc_analysis.tex:49 | `\placeholder{}` | Qwen random Δ̃ (重复引用) |
| F1h | appendix_results.tex:10 | `\placeholder{}` | Qwen random Δ̃ |
| F1i | appendix_moved.tex:76 | `\placeholder{}` | Qwen random Δ̃ |

### F2. 从 n=500 Cross-model 数据填入
| # | 文件:行 | Placeholder | 说明 |
|---|--------|-------------|------|
| F2a | appendix_results.tex:7 | `\placeholder{}` × 2 | per-problem concordance ρ 和 p |
| F2b | appendix_moved.tex:73 | `\placeholder{}` × 2 | 同 F2a（重复段落） |

### F3. 从 c3_llama 数据填入（与 n=500 无关，可提前填）
| # | 文件:行 | Placeholder | 说明 |
|---|--------|-------------|------|
| F3a | results.tex:81 | `\placeholder{}` | LLaMA random Wilcoxon p (s=0.30) |
| F3b | results.tex:86 | `\placeholder{N_LLAMA}` | LLaMA paired n |
| F3c | results.tex:92-95 | 12+ `\placeholder{}` | Tab 4 全部 (Δ̃, CI, p × 4 levels) |
| F3d | discussion.tex:15 | `\placeholder{}` | LLaMA random Wilcoxon p |

### F4. 从 c5b_pilot 数据填入（与 n=500 无关，可提前填）
| # | 文件:行 | Placeholder | 说明 |
|---|--------|-------------|------|
| F4a | discussion.tex:10 | `\placeholder{ORACLE_PCT}` | oracle recovery % |
| F4b | discussion.tex:10 | `\placeholder{ORACLE_P}` | oracle Wilcoxon p |
| F4c | discussion.tex:10 | `\placeholder{HEUR_PCT}` | heuristic recovery % |
| F4d | discussion.tex:10 | `\placeholder{HEUR_P}` | heuristic Wilcoxon p |

---

## G. 条件更新（取决于 n=500 分析结果）

### G1. Qwen s015 onset threshold
- **若 CI 仍跨零** → 保持 "marginal at s=0.15"、"at s ≥ 0.20"
- **若 CI 不再跨零** → 全部改为 "at all sparsity levels"，删 "marginal" 限定
- **若 s020 也变边缘** → onset 改为 "s ≥ 0.25"
- 受影响: abstract.tex:10, introduction.tex:15, results.tex:71/106, conclusion.tex:4, Table 3 footnote

### G2. Random "7/8 FAIL" 计数
- **若 n=500 random 仍不显著** → 保持 "7/8"
- **若更多 random 条件显著** → 更新计数，调整 "strategy-specific" 措辞
- **若 Qwen s030 random 不再显著** → 简化叙事，删 exception 讨论
- 受影响: abstract.tex:8, conclusion.tex:4, appendix_disc_analysis.tex:14, appendix_results.tex:10

### G3. Qwen s030 random effect size
- **若 d 变大（non-negligible）** → 更新 "negligible" 描述
- **若 d 仍 negligible** → 保持
- 受影响: 所有 Qwen random Δ̃ placeholder 位置

### G4. DS/QW 量级比
- 当前: "~1/5"。n=500 后比例可能变化 → appendix_moved.tex:48/69
- 当前: Spearman ρ=1.0。若不再完全单调 → 更新

### G5. 单调性 (C6/S7→C)
- 若 G 曲线不再严格单调 → 修改 "monotonically increasing"
- 受影响: abstract, introduction, results §5.2, conclusion

### G6. Sub-exponential growth factors
- 当前: 3.8×→4.8×→2.0×（递减）→ 重算
- 受影响: paper_framing.md

### G7. LLaMA 相对量级
- discussion.tex:15 "~7× smaller than Qwen" — Qwen 值更新后可能需重算此比例

---

## H. 不需要更新

| 文件 | 原因 |
|------|------|
| related_work.tex | 文献综述，无数据依赖 |
| background.tex | 公式定义 (II, G, phase segmentation) |
| methodology.tex:1-9 | Models/Sparsity config 不变（仅 Dataset 段更新） |
| analysis.tex | 引用 c4_entropy 数据 (n=30)，独立实验 |
| appendix.tex | formulation details / multiplicative null |
| Tab discrimination-metrics-full | c4_entropy Gini/CV (n=30) |
| Tab entropy-deltas | c4_entropy ΔH (n=30) |
| Tab llama-cross-arch 数值 | c3_llama (n=50)，非 n=500 范围（placeholder 另列于 F3） |
| C5b pilot 数值 | c5b_pilot 独立实验（placeholder 另列于 F4） |
| LLaMA abstract/intro/conclusion 内联 | "$0.020 \to 0.356$" 等 LLaMA 数据不变 |

---

## I. 推荐更新顺序

1. **立即可做**: 填 F3 (LLaMA placeholder) + F4 (C5b pilot placeholder) — 与 n=500 无关
2. **等 n=500 分析完成** → 获取 JSON 输出文件
3. **替换 A (文字 50→500)** + **B (配对 n)**
4. **批量替换 C (DeepSeek 数值)** — 从 experiment_summary_table.json 读取
5. **批量替换 D (Qwen 数值)** — 同上
6. **填入 F1/F2 (n=500 placeholder)**
7. **评估 G (条件更新)** — 根据结果判断叙事调整
8. **重生成 E (图表)**
9. **全文交叉验证**: abstract/intro/conclusion 内联数字 = tables 数字

## J. 数据来源映射

| 数据 | JSON 来源 | 论文位置 |
|------|----------|---------|
| DS median Δ (imp/rand) | experiment_summary_table.json → median_diff | Tab 1, Tab 2, inline §5.1 |
| DS per-phase II | experiment_summary_table.json → per-phase medians | Tab 2 |
| DS G ratios | Tab 2 (II_low / II_high) | Tab 2, inline §5.2 |
| DS Cohen's d_z + Δ̃ [CI] | cohens_d_bf16.json | Tab 3 DS cols |
| QW Cohen's d_z + Δ̃ [CI] | cohens_d_bf16_qwen.json | Tab 3 QW cols |
| Permutation Δ̃ + CI + p | permutation_test_results.json | Tab 7 |
| Cross-model Δ | cross_model_analysis.json | Tab 5 |
| QW per-phase effective n | analyze_n500_unified.py → qwen null rate | Tab (app), inline |
| QW random Δ̃ (s030) | experiment_summary_table.json → qw_rand_s030 | abstract, appendix |
| Per-problem concordance | cross_model_analysis.json → spearman_rho, p | appendix |
