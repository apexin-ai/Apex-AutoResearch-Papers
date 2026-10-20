# n=500 Paper Update Plan — Section-by-Section Diff Spec

> 生成日期: 2026-05-14
> 前置依赖: n500_paper_patch_plan.md（逐行数值替换清单）
> 本文档补充: 每个 section 的 claim 强度评估 + 条件分支逻辑 + Qwen caveat + C8/C5b 专项

---

## 硬约束（Paper Worker 必读）

| 约束 | 来源 | 含义 |
|------|------|------|
| 指标只用 **median + median bootstrap CI** | D054 | 禁止 mean，所有表格/正文/caption 一律 median |
| d_z 只报 **within-importance**（low−high 配对） | D059 | imp-vs-rand d_z 和 random d_z 全部删除，改用 Wilcoxon p + median_diff |
| LLaMA 为 **qualitative pattern**，不做定量跨架构比较 | D060 | 禁用 "confirms"，只用 "suggests"/"provides partial support"/"directionally consistent" |

---

## §Abstract (abstract.tex)

### 当前 n=50 数据引用
- L6: `50 MATH-500 problems`
- L7: DeepSeek Δ `0.39→14.59`, d_z `0.44→0.80`, `p < 0.005`
- L8: random `7/8 conditions`, Qwen s030 `p=0.012`, `d_z=-0.04`（**D059 违规**）
- L9: crossover II 数值 `0.032 vs 0.818`, `7.196 vs 1.363`
- L10: Qwen `d_z ≥ 0.55`, `ρ=1.0`, `p=0.043`; LLaMA `d_z (0.19→0.34)`（**D059 违规**）, `~1/40`

### n=500 更新操作
1. `50` → `500`
2. 替换所有 DeepSeek/Qwen 数值为 n=500 结果
3. **D059 修复**:
   - L8: 删 `d_z=-0.04`，改为 `negligible median difference`
   - L10: 删 LLaMA imp-vs-rand d_z 序列，改为 `Wilcoxon signed-rank test reaching significance at s=0.30 (p_Bonf=X)`
4. LLaMA `~1/40` → 用 n=500 DeepSeek Δ 重算比值

### Claim 强度调整逻辑
- **若 n=500 CI 变窄且不跨零**: 可加强 → 删除 `(small)` 修饰词，直接报 d_z 值
- **若 Qwen s015 CI 仍跨零**: 保持 `s ≥ 0.20` 下界，不加强
- **若 Qwen s015 CI 排除零**: 可改为 `s ≥ 0.15`，abstract 同步
- **若 random PASS/FAIL 比例变化**: 更新 `7/8` 为实际比例

---

## §1 Introduction (introduction.tex)

### 当前 n=50 数据引用
- L14: DeepSeek Δ `0.39→14.59`, d_z `0.44→0.80`, `p < 0.005`
- L15: Qwen `d_z ≥ 0.55`, LLaMA `~1/40`
- L16: `7/8 conditions non-significant`

### n=500 更新操作
1. L14: 与 abstract Q3/Q4/Q5 同步替换
2. L15: 与 abstract Q9/Q11 同步
3. L16: 与 abstract Q6 同步

### Claim 强度调整逻辑
- Introduction 措辞已较保守（`partially extends`），n=500 后无需改措辞方向
- 若 n=500 效应量增大（d_z > 1.0），可在 `($d_z$: X → Y)` 后加 `(large)` 标注

---

## §2 Related Work (related_work.tex)

### n=50 数据引用: **无**
### n=500 更新操作: **无**（纯引用区分，不含实验数据）

---

## §3 Background (background.tex)

### n=50 数据引用: **无**（只有公式定义）
### n=500 更新操作: **无**

---

## §4 Experimental Setup (methodology.tex)

### 当前 n=50 数据引用
- L10: `50 problems stratified from MATH-500`
- L18: `mean/median ratios up to 43:1`
- L22: `All tests yield p_Bonf < 0.005`

### n=500 更新操作
1. L10: `50 problems stratified from MATH-500` → `500 problems from MATH-500`（删 "stratified"，500≈全集）
2. L18: `43:1` → n=500 实际 mean/median ratio
3. L22: 更新 p 值（预期 n=500 仍 <0.005，但需确认实际值）

### Claim 强度: 无需调整（方法描述）

---

## §5 Results (results.tex)

### 当前 n=50 数据引用（按子节）

**§5.1 Strategy-Dependent Severity (L1-23)**
- L8: Δ `0.39→14.59`, `37×` amplification; random `-0.02 to 1.54`
- Table 1 (tab:aggregate-ii): 8 个数据单元格, caption `n=50`
  - Importance: 0.39, 1.48, 7.16, 14.59
  - Random: 0.01, -0.02, 0.54, 1.54

**§5.2 Phase-Modulated Amplification (L26-60)**
- L29: G `69×→274×`, II_high `0.006→0.053`, random G `0.9–1.7×`
- Table 2 (tab:main-results): 24 个数据单元格, caption `50 problems`
  - 完整 per-phase II breakdown（8行×3列 II + Δ + G）
- Fig 1 (fig1_dose_response.pdf): G vs s 曲线, caption `69×→274×`

**§5.3 Crossover (L63-67)**
- L66: II 数值 `0.032 vs 0.818`, `7.196 vs 1.363`, `5.3× reversal`

**§5.4 Cross-Model (L68-72)**
- L71: Qwen Δ `0.04→2.94`, `~1/5`, `ρ=1.0`, `p=0.043`, `d_z=0.28 CI includes zero`, `d_z ≥ 0.55`

**§5.5 Cross-Architecture (L74-98)**
- L79: LLaMA d_z `0.19→0.26→0.29→0.34`（**D059 违规**）, `p=0.029`, `Δ=0.020 [0.002,0.043]`
- L79: within-imp d_z `[1.00, 1.12]`（合规）, random d_z `[0.35, 0.45]`（**D059 违规**）
- L81: `~40× smaller than DeepSeek`, `~7× smaller than Qwen`
- Table 3 (tab:llama-cross-arch): d_z 列为 imp-vs-rand（**D059 违规，需重构**）

**§5.6 Statistical Validation (L101-127)**
- L104: permutation `p < 0.005`, `0.37→9.85`
- L106: DeepSeek d_z `0.44→0.80`, Qwen d_z `0.28→1.02`, `0.89/1.02 vs 0.68/0.80`
- Table 4 (tab:cohens-d): 16 个数据单元格（DS/QW × 4 sparsity × d_z + Δ[CI]）

### n=500 更新操作

**Tables 替换清单**:

| Table | ID | 需替换单元格数 | 数据来源 |
|-------|----|--------------|---------|
| Table 1 | tab:aggregate-ii | 8 + caption n | n=500 experiment_summary_table.json median_diff |
| Table 2 | tab:main-results | 24 + caption n | n=500 per-phase median II |
| Table 3 | tab:llama-cross-arch | **重构**: d_z列→within-imp d_z 或删除 d_z 列改为 Wilcoxon p + Δ̃ | LLaMA 不重跑→数值不变但列定义改 |
| Table 4 | tab:cohens-d | 16 | n=500 within-imp d_z + paired median diff + CI |

**Figures 替换清单**:

| Figure | 文件 | 数据来源 | 操作 |
|--------|------|---------|------|
| Fig 1 | fig1_dose_response.pdf | n=500 G values (imp+rand) | 重绘，caption G值同步 |

**D059 修复** (§5.5):
- L79 `paired d_z (0.19→...→0.34)` → `Wilcoxon signed-rank tests with median paired difference increasing from X to Y`
- L79 `d_z ∈ [0.35, 0.45]` → `random eviction also shows a non-trivial phase gradient (Wilcoxon p < X)`
- Table 3: d_z列→within-importance d_z (low−high)，caption 相应修改

**C8 限定语修复** (§5.5):
- L79 `The qualitative pattern replicates` → `The qualitative pattern is directionally consistent`（唯一需修改处，其余已合规）

### Claim 强度调整逻辑

**§5.4 Cross-Model — Qwen onset threshold 关键分支**:
- **若 Qwen n=500 s015 d_z CI 排除零**: onset threshold 从 `s ≥ 0.20` 改为 `s ≥ 0.15`，L71 删 `CI includes zero`，改为 `d_z=X [CI_lo, CI_hi]`
- **若 Qwen n=500 s015 CI 仍跨零**: 保持 `marginal at s=0.15, reliable at s ≥ 0.20`，在后续文字加 caveat: `the onset threshold for reliable detection appears model-dependent (DeepSeek: s ≥ 0.15; Qwen: s ≥ 0.20)`
- **若 Qwen n=500 s020 CI 也跨零**: 升级 caveat 为 `s ≥ 0.25`，narrative 改为 `compound effect emerges above threshold sparsity (~s020-s025)`

**§5.6 Statistical Validation — n=500 power 增益**:
- n=500 预期 CI 收窄 ~√10 倍，d_z 估计更稳定
- 若所有 CI lower bounds > 0: 可删除 `marginal` 相关修饰语
- 若 permutation p 值从 `< 0.005` 变为 `< 0.001`: 更新但不改措辞

---

## §6 Analysis (analysis.tex)

### 当前 n=50 数据引用
- L4: Gini Δ `0.030–0.081` (DS), `0.010–0.020` (QW)
- L6: entropy Δ𝓗 `[-0.047, -0.040]` (DS), `+0.045` (QW s025)

### n=500 更新操作
- **条件性**: C4 entropy 分析是否基于 n=500 重跑？
  - **若重跑**: 替换所有 Gini/CV/entropy 数值
  - **若不重跑**: 保留 n=50 数值，添加脚注 `Mechanism analysis based on a 30-problem subset; main results use n=500`

### Claim 强度: 无需调整（机制分析，结论不变）

---

## §7 Discussion (discussion.tex)

### 当前 n=50 数据引用
- L5: G `69–274×`, crossover II `0.032 vs 0.818`, `7.196 vs 1.363`, `G ≈ 1`
- L11: LLaMA `~40× smaller`, `~7× smaller`, `d_z ≥ 1.0`, `d_z ∈ [0.35, 0.45]`（**D059 违规**）

### n=500 更新操作
1. L5: 与 §5 同步更新所有数值
2. **D059 修复**: L11 删 random d_z `[0.35, 0.45]`，改为定性描述 + Wilcoxon p
3. L11: `~40×/~7×` 用 n=500 重算

### 新增内容
- **C5b pilot 结果** (B2 预写文本): 插入 L8 段末（`Extended discussion in Appendix~\ref{app:extended-discussion}.` 之前）
  - 内容: oracle recovery 18% < 30% gate, heuristic 32% CI 跨零, 作为 future work
  - 这是 §8 future work 的铺垫

### Claim 强度调整
- 若 n=500 G 值变化幅度 ≤20%: `far exceeds a naive "somewhat worse" prediction` 保留
- 若 G 值大幅缩小（如 274× → <100×）: 需调弱 `far exceeds` 措辞

---

## §8 Conclusion (conclusion.tex)

### 当前 n=50 数据引用
- L4: G `69×→274×`, d_z `0.44→0.80`, `7/8`, `d_z ≥ 0.55`, `~1/40`

### n=500 更新操作
1. 全部数值与 §5/Abstract 同步
2. 若 n=500 效应增强: 可从 `strongly modulated` 加强为 `robustly modulated`（谨慎）

### 新增内容
- L5 之后追加一句指向 discussion C5b: `A preliminary pilot of phase-aware budget reallocation yielded 18\% oracle recovery, below pre-registered thresholds, motivating joint phase--strategy optimization as future work (\S\ref{sec:discussion}).`

### C5b §8 Future Work 准确性验证
当前 conclusion.tex L5: `These findings motivate phase-aware sparsity allocation for reasoning model deployment.`
- **问题**: 这句暗示 mitigation 是直接可行的，但 C5b pilot 已经 gate_failed
- **修复**: 改为 `These findings motivate phase-aware sparsity allocation as a promising but non-trivial direction: a preliminary oracle pilot recovered only 18\% of compound interaction, suggesting that effective mitigation requires joint optimization of budget allocation and strategy selection across phases.`

---

## Limitations (limitations.tex)

### 当前 n=50 数据引用
- L1: LLaMA `d_z ∈ [0.35, 0.45]`（隐含在定性描述中，无具体数字）
- L11: `s ∈ {0.15, 0.20, 0.25, 0.30}`

### n=500 更新操作
- L1: 无具体数字需替换（定性描述），但审查 LLaMA 措辞是否合规 → 已合规（`partially extends`）
- **新增**: L1 末尾加 `Cross-architecture validation is based on n=50; repeating at n=500 is future work.`（若 LLaMA 不重跑）

### Claim 强度
- 若 n=500 CI 全部排除零: 可删除 `$n{=}49$ paired problems` statistical scope 中关于小样本的讨论，或改为 `$n{=}X$ paired problems (primary models) and $n{=}49$ (cross-architecture)`
- Statistical scope (L44-50): `n=49`/`n=46` → `n=X`/`n=Y`（n=500 有效问题数）

---

## Appendix

### appendix.tex
- L38: multiplicative null G `58–241×` → n=500 值

### appendix_results.tex
- L7: per-problem concordance `ρ=-0.11, p=0.926` → n=500 值
- L10: random PASS/FAIL 计数 + `p=0.012`, `d_z=-0.04`（**D059 违规**）

### appendix_moved.tex

**Tables**:
| Table | ID | 操作 |
|-------|----|------|
| tab:cross-model | L30-43 | 替换 8 单元格 |
| tab:permutation | L70-85 | 替换 12 单元格 + caption n |
| tab:discrimination-metrics-full | L103-123 | 条件性：C4 重跑则替换 |
| tab:entropy-deltas | L143-163 | 条件性：C4 重跑则替换 |

**Figures**:
| Figure | 文件 | 操作 |
|--------|------|------|
| fig3_crossover.pdf | L15 | n=500 s=0.25 per-phase median → 重绘 |
| fig4_bootstrap.pdf | L89 | n=500 paired d_z + permutation CI → 重绘 |
| fig5_crossmodel.pdf | L47 | n=500 DS/QW paired median diffs → 重绘 |

**文本**:
- L11: crossover 全部数值（6 个数字 + 4 个比值）
- L26: `Four of the 50 problems excluded` → `X of 500 problems excluded`
- L53/56: per-problem concordance + random d_z（**D059 违规**）
- L62/73: `n=49` → n=500 值
- L68: CI lower bounds `0.19→0.69→1.66→6.70`

### appendix_disc_analysis.tex
- L4: random Gini 范围 `−0.031 to −0.073; Qwen: −0.019 to −0.045`（条件性）
- L11: `II_high < 0.06`, `0.105`
- L14: `7/8`, `p=0.012`, `d_z=-0.04`（**D059 违规**）
- L45-50: statistical scope 全部 n 值 + 偏度统计 + permutation CI
- L57: growth rate `3.8×→4.8×→2.0×`

---

## Qwen Caveat 专项

### 触发条件
**若 Qwen n=500 mid-phase (s015/s020) 仍不显著**:

### 需加 caveat 的位置

| # | 文件 | 位置 | 当前文本 | 需加的限定 |
|---|------|------|---------|-----------|
| QC1 | abstract.tex:10 | Qwen 结果句 | `$d_z \geq 0.55$` | 加 `at $s \geq 0.20$`（若 s015 仍不显著）|
| QC2 | results.tex:71 | §5.4 末尾 | Qwen cross-model | 插入 B1 预写文本（imp-vs-rand 衰减 caveat）|
| QC3 | appendix_moved.tex:28 | cross-model detail | `Qwen reproduces the monotonic severity gradient` | 加 `at $s \geq 0.20$; the effect is marginal at $s{=}0.15$` |
| QC4 | limitations.tex | 新增 | （无） | 加 `The onset sparsity for reliable phase modulation is model-dependent` |
| QC5 | paper_framing.md | C2 预注册 | `叙事改为 'compound effect emerges above threshold sparsity (~s020)'` | 执行预注册承诺 |

### 若 Qwen n=500 s015 显著
- 删除所有 `marginal at s=0.15` 限定
- onset threshold 统一为 `s ≥ 0.15`
- abstract/introduction 可加强为 `replicates at all four sparsity levels`

### Qwen imp-vs-rand 对比
D058 记录 n=50 imp-vs-rand 全不显著。n=500 后:
- **若仍全不显著**: 在 §5.4 加 B1 caveat（已预写），说明 within-importance gradient robust 但 strategy contrast attenuated
- **若 s025/s030 显著**: 报告为 `strategy contrast reaches significance at higher sparsity`
- **若全显著**: 删 caveat，报告为 `strategy contrast replicates on Qwen at all levels`

---

## C8 限定语专项

### 当前 LLaMA partially_confirmed 措辞审查

| # | 文件:行号 | 当前文本 | 状态 |
|---|----------|---------|------|
| 1 | abstract.tex:10 | `suggests cross-architecture generalization, though at...` | ✅ 合规 |
| 2 | introduction.tex:15 | `partially extends to a distinct architecture` | ✅ 合规 |
| 3 | results.tex:79 | `The qualitative pattern replicates` | ⚠️ 需改为 `is directionally consistent` |
| 4 | results.tex:81 | `qualitatively consistent...substantially weaker` | ✅ 合规 |
| 5 | discussion.tex:11 | `provides partial support for the qualitative pattern` | ✅ 合规 |
| 6 | conclusion.tex:4 | `partially extends cross-architecture` | ✅ 合规 |
| 7 | limitations.tex:2 | `partially extends the findings beyond` | ✅ 合规 |
| 8 | appendix_disc_analysis.tex:33 | `provides partial support` | ✅ 合规 |

**唯一需修改**: #3 results.tex:79

### n=500 后是否需要调整 C8
- LLaMA 不重跑 n=500（未在 ROADMAP 中），所以 C8 数据不变
- n=500 改变的是 DeepSeek/Qwen 的 Δ 绝对值 → 重算 LLaMA/DS 和 LLaMA/QW 的比值
  - 当前: `~40× smaller` (DS), `~7× smaller` (QW)
  - n=500 后: 分母变化 → 比值可能变化
  - **操作**: 等 n=500 DS/QW Δ 出来后重算，更新 abstract/results/discussion/conclusion 中的倍数

---

## C5b §8 Future Work 专项

### 当前状态
- C5b: `future_work`（D056: oracle recovery 18% < 30% gate, heuristic 32% CI 跨零）
- 论文**无独立 Future Work section**

### 当前提及位置
| # | 文件 | 内容 | 准确性 |
|---|------|------|--------|
| 1 | discussion.tex:8 | `A phase-aware compression budget...could mitigate...` | ⚠️ 过于乐观——未提及 pilot 失败 |
| 2 | conclusion.tex:5 | `These findings motivate phase-aware sparsity allocation...` | ⚠️ 同上 |

### 需要的修改
1. **discussion.tex**: L8 段末插入 B2 预写文本（pilot 结果: oracle 18% < 30% gate）
2. **conclusion.tex**: L5 改写，加入 pilot 限定（见上文 §8 Conclusion 部分）
3. **验证 paper_framing.md 中 C5b 描述**: `oracle recovery 18%, heuristic 32% CI 跨零, 方向正确但效应量不足` → 与论文叙事一致 ✅
4. **Heuristic > Oracle 悖论**: paper_framing.md 提到值得在论文中提及 → 在 discussion B2 文本中加一句: `Notably, the heuristic boundary (token position ratio) yielded higher recovery (32\%) than the oracle (18\%), suggesting that optimal phase granularity for mitigation may differ from that for characterization---an open question for future work.`

---

## Figures 完整重绘清单

| # | 文件 | 引用位置 | n=500 数据源 | 操作 |
|---|------|---------|-------------|------|
| F1 | fig1_dose_response.pdf | results.tex:57 | n=500 G values from experiment_summary_table.json | 重绘: G vs s, imp solid + rand dashed, 95% bootstrap CI |
| F2 | fig3_crossover.pdf | appendix_moved.tex:15 | n=500 s=0.25 per-phase median II | 重绘: grouped bar, 3 phases × 2 strategies |
| F3 | fig4_bootstrap.pdf | appendix_moved.tex:89 | n=500 within-imp d_z + permutation CI | 重绘: forest plot, 4 sparsity levels |
| F4 | fig5_crossmodel.pdf | appendix_moved.tex:47 | n=500 DS/QW paired median Δ | 重绘: line plot, DS solid + QW dashed, symlog Y |

生成方式: 服务器端 `/root/autodl-tmp/pacs/analysis/generate_paper_figures.py`（draw-paper-figure skill）
样式: serif, 9pt, hidden top/right spines, 300 dpi

---

## Tables 完整替换清单

| # | Table ID | 文件:行号 | 单元格数 | 依赖 |
|---|----------|----------|---------|------|
| T1 | tab:aggregate-ii | results.tex:10-23 | 8 + caption | n=500 DS imp+rand Δ |
| T2 | tab:main-results | results.tex:31-53 | 24 + caption | n=500 DS per-phase II |
| T3 | tab:llama-cross-arch | results.tex:83-98 | **重构** | D059: 列定义改为 within-imp d_z；数值不变（LLaMA 不重跑） |
| T4 | tab:cohens-d | results.tex:108-124 | 16 | n=500 DS/QW within-imp d_z + Δ[CI] |
| T5 | tab:cross-model | appendix_moved.tex:30-43 | 8 | n=500 DS/QW Δ |
| T6 | tab:permutation | appendix_moved.tex:70-85 | 12 + caption | n=500 permutation Δ + CI + p |
| T7 | tab:discrimination-metrics-full | appendix_moved.tex:103-123 | 16 | **条件**: 仅 C4 重跑 |
| T8 | tab:entropy-deltas | appendix_moved.tex:143-163 | 8 | **条件**: 仅 C4 重跑 |

---

## 执行顺序

### Phase 1: 数据到手立即执行（~2h）
1. 跑 n=500 analysis pipeline: median II + bootstrap CI + d_z within-importance + permutation test
2. 生成 experiment_summary_table.json（n=500 版）
3. 替换 T1, T2, T4, T5, T6 表格数据
4. 替换全文 ~77 处数值引用（详见 n500_paper_patch_plan.md A2 清单）
5. 重绘 F1-F4 图表

### Phase 2: D059 合规修复（~1h，可与 Phase 1 并行）
6. 修复 10 处 D059 违规（详见 n500_paper_patch_plan.md A3 清单）
7. 重构 Table 3 (tab:llama-cross-arch) 列定义

### Phase 3: 文本修改（~1h，依赖 Phase 1 结果）
8. 评估 Qwen s015 CI → 决定是否触发 Qwen caveat
9. 修复 C8 限定语（results.tex:79 一处）
10. 插入 C5b future work 文本（discussion.tex + conclusion.tex）
11. 插入 Qwen caveat（若触发）
12. 插入 mid-phase null rate 说明（若 n=500 确认高 null rate）

### Phase 4: 一致性验证（~30min）
13. 全文 grep 所有 n=50 相关数字确认无遗漏
14. 交叉验证 abstract/introduction/results/conclusion 数值一致性
15. 确认 paper_framing.md 与论文最终文本同步
16. 编译 PDF 检查无 LaTeX 错误
