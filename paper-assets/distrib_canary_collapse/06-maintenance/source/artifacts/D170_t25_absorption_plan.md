# D170 T=25 Data Absorption Plan

> Generated: 2026-05-21 | Status: T=25 四格 RUNNING (~20-24%)
> 前置：D170_narrative_drafts.md 已覆盖 16/20 cells (T=5/10/15/20)

---

## A. 当前叙事状态评估

### D170 草稿已覆盖的 claims

| 段落/位置 | 覆盖内容 | T=25 依赖程度 |
|-----------|----------|--------------|
| Abstract 选项 A | T=5 blind zone + α_c left-shift (T=20 为 max T) | ⚠️ 需改 max T=25 |
| Abstract 选项 B | 3-T sync-dip + power-law contour | ⚠️ 3-T→4-T 或 dissolution 改写 |
| Intro C1 扩展 | T=5 blind zone + T=15 left-shift + landscape stabilization | 🟡 T=25 扩展但不改核心 |
| Results: T=5 blind zone | α_c(5)≥1.0 理论验证 | ✅ 无依赖 |
| Results: T=15 left-shift | α_c(15)≈0.304 predict-then-verify | ✅ 无依赖 |
| Results: landscape stabilization | T=15≈T=20 镜像 | ⚠️ T=25 决定是否继续稳定 |
| Results: 6/8 ceiling + sync-dip | 7 cells ceiling + 3-T dip invariance | 🔴 核心依赖：dip 是 3-T 还是 4-T？ceiling 是否打破？|
| Results: 综合段 | "16 confirmed cells" | 🔴 → "20 confirmed cells" |
| Scenario A draft | dissolution 措辞 | 🔴 启用或废弃 |
| Scenario B draft | permanence 措辞 | 🔴 启用或废弃 |

### 关键数字需更新清单
- Phase Diagram 表格：T=25 行 4 格填充
- Figure ref: fig_phase_diagram → 20/20 heatmap
- α_c(T) 约束点：从 "1 calibration + 3 consistency" → "1 calibration + 4 consistency"（#57）
- predict-then-verify scoreboard：T=25 新增 4 条目

---

## B. 场景化吸收模板

### 场景 A：Dissolution（T=25 α=0.60 > 0/8）

**预期整行**：α=0.45 ≥5/8, α=0.50 = 6/8, α=0.60 > 0/8, α=0.75 = 6/8

#### B.1a Abstract 改写

**选项 B（推荐，因 dissolution 增加叙事复杂性）**：

当前：
> ...a synchronous dip at α=0.60 persisting across three observation lengths (T=10, 15, 20: all 0/8)...

改为：
> ...a synchronous dip at α=0.60 that persists across T=10–20 (0/8 at each) but dissolves by T=25 (X/8), revealing a transient detection blind spot rather than a permanent structural barrier...

（X 填实际值）

#### B.1b Introduction C1 改写

当前最后一句：
> The synchronous dip at α=0.60 persists invariantly across T=10, 15, and 20 (0/8 at each), ruling out power-deficit explanations.

改为：
> The synchronous dip at α=0.60 persists across T=10–20 (0/8 at each) but dissolves at T=25 (X/8), consistent with increasing statistical power eventually overcoming synchronous interference—the dip is a finite-horizon phenomenon, not a structural barrier.

#### B.1c Results: 6/8 ceiling + sync-dip 段落

当前最后两句（"Meanwhile, α=0.60..."起）全部替换：

> Meanwhile, α=0.60 exhibits a transient synchronous dip: 0/8 across T=10, 15, and 20, but rising to X/8 at T=25. The dip's dissolution at extended observation length, combined with the near-miss at T=20 (FDR p=0.064), supports the interpretation that synchronous interference between canary and downstream signals is power-dependent rather than structural: sufficient observation length allows the √T-scaled test statistic to overcome the reduced temporal resolution at this contamination level.

若 X ≥ 6/8（完全恢复）追加：
> The T=25 recovery to 6/8 closes the synchronous gap entirely, confirming that all contamination levels above α_c(T) are eventually detectable.

若 X = 2-4/8（部分恢复）追加：
> The partial recovery (X/8 vs. the 6/8 ceiling at other α values) suggests that synchronous interference at α=0.60 weakens but does not fully vanish within 25 generations, consistent with the S×R model's prediction of reduced temporal resolution at intermediate contamination.

#### B.1d Results: 综合段

"16 confirmed cells" → "20 confirmed cells"

追加一句：
> The complete 20-cell phase diagram confirms two major landscape features: a power-law detection boundary α_c(T) that sweeps leftward with increasing T, and a transient synchronous dip at α=0.60 that dissolves at sufficient observation length.

#### B.1e C2 Theory (paper_framing) 影响

- α_c(25)≈0.232 检验：α=0.45 若 ≥5/8 → 又一个 consistency check PASS
- S×R 竞争模型升级：sync-dip dissolution 成为 S×R 的 **quantitative prediction success**——√T scaling 最终压倒 R(α) 下降
- predict-then-verify scoreboard 新增条目，dissolution 算 PASS（S×R 预测 √T 最终克服 sync）
- C2 可升级为 stronger claim：**"α > α_c(T) is sufficient for eventual detection"**（#57 不再需要 "necessary but not sufficient" caveat）

#### B.1f Constraint 更新

- #58 sync-dip 措辞：从 "persists across all tested T≥10" → "persists across T=10–20 but dissolves at T=25"
- #57 α_c(T)：T=25 成为第 5 个约束点（1 calibration + 4 consistency checks）
- #54 Power Theory：dissolution 提供 √T scaling 的直接实证（sync-dip 区域 √T 增长最终克服 R 下降）

---

### 场景 B：Permanence（T=25 α=0.60 = 0/8）

**预期整行**：α=0.45 ≥5/8, α=0.50 = 6/8, α=0.60 = 0/8, α=0.75 = 6/8

#### B.2a Abstract 改写

**选项 B（推荐，permanence 强化 landscape 结构性）**：

当前已近乎可用。改为：
> ...a synchronous dip at α=0.60 persisting across all four observation lengths (T=10, 15, 20, 25: 0/8 at each), establishing it as a structural feature of the detection landscape...

#### B.2b Introduction C1 改写

当前最后一句改为：
> The synchronous dip at α=0.60 persists across all tested observation lengths from T=10 to T=25 (0/8 at each), establishing a permanent detection blind spot that power-deficit explanations cannot account for—α=0.60 exceeds α_c(T) at all T≥10, yet remains undetectable.

#### B.2c Results: 6/8 ceiling + sync-dip 段落

当前最后两句替换为：

> Meanwhile, α=0.60 yields 0/8 across all four observation lengths (T=10, 15, 20, 25)—a structural synchronous dip that persists despite α=0.60 exceeding α_c(T) at every tested T≥10. This four-point invariance definitively rules out statistical power as the explanation: at T=25, the test has 2.5× the effective sample size of T=10, yet the dip remains unchanged. The S×R competition model explains this as a stable equilibrium: at α≈0.60, the relaxation time τ_relax matches the observation interval, causing canary and downstream signals to synchronize and destroying the lag structure that PermG requires for detection.

#### B.2d Results: 综合段

"16 confirmed cells" → "20 confirmed cells"

追加：
> The complete 20-cell phase diagram reveals three structural features: (1) a power-law detection boundary α_c(T) sweeping leftward with T, (2) a permanent synchronous dip at α=0.60 bisecting the detectable region, and (3) a 6/8 detection ceiling consistent with MAUVE-pair bottleneck.

#### B.2e C2 Theory (paper_framing) 影响

- α_c(T) 公式仍成立（α=0.60 是 S×R 非单调例外，不是 α_c failure）
- C2 需要 caveat："α > α_c(T) is necessary but not sufficient"
- **C3 升级**：multi-method necessity 升级——single method (PermG) 在 α=0.60 永久失效，其他方法（spectral、distribution-level）成为必需 → Discussion 强调 MMCT 框架的不可替代性
- S×R 模型从 "predicts non-monotonicity" 升级为 "predicts permanent resonance cancellation"

#### B.2f Constraint 更新

- #58：从 "persists across all tested T≥10" → "persists across T=10–25 (four observation lengths), established as structural invariant"，删除 "near-miss suggests potential dissolution"
- C2 paper_framing：追加 "structural blind spots exist even above α_c(T)"

---

### 场景 D（低概率）：T=25 α=0.45 = 0/8

**意味着**：T=15=6/8 → T=20=5/8 → T=25=0/8，detection power 随 T 反转。√T scaling 在 near-boundary 区域失败。

**紧急处理**：
1. 检查实验完整性（gen 目录 + all_metrics.json，遵守 C005: EXIT_CODE=129 不等于失败）
2. 若数据完整 → 检查是否 seed-specific（T=25 s42 vs T=15 s42/s43）
3. 叙事影响：α_c(T) 在 boundary 附近非单调 → 不能再声称 "monotonic left-shift"
4. 论文措辞退化："α_c(T) decreases monotonically" → "α_c(T) shows an overall leftward trend but exhibits non-monotonic fluctuations near the detection boundary"
5. 需要额外实验：T=25 α=0.45 s43 cross-seed 验证

---

## C. α=0.60 Dissolution 专项

### 这是论文最关键的单格（D176 标注 ★）

**当前证据链**：
- T=10 α=0.60: PermG=0/8 (s42=0/8, s43=0/8, 双 seed 一致)
- T=15 α=0.60: PermG=0/8 (s42=0/8, s43 RUNNING)
- T=20 α=0.60: PermG=0/8 (s42=0/8, s43 RUNNING) + **near-miss p_fdr=0.064**
- T=25 α=0.60: RUNNING (★)

**Near-miss 信号**：T=20 的 p_fdr=0.064（差 0.014 未过 0.05）暗示 dissolution 可能正在发生。

### C.1 Dissolution confirmed (>0/8) → C2 impact

**C2 S×R 竞争模型**：
- 当前措辞（#58）："Sync dip persists across all tested T≥10"
- 改为："Sync dip represents a transient phase alignment that dissolves when √T-scaled power overcomes synchronous interference"
- **关键叙事升级**：S×R 模型不仅解释 non-monotonicity 的存在，还正确预测了其 T-dependent dissolution → 从 "qualitative explanation" 升级为 "quantitative predictive framework"

**C2 predict-then-verify**：
- 若 dissolution 与 √T scaling 预测的 T=25 rate 一致（locked prediction ~2-3/8）→ S×R 得到最强验证
- 若 dissolution 但幅度远超/远低于预测 → 记录为 systematic bias 的另一个数据点

**C3 multi-method necessity**：
- 弱化为 "necessary in moderate-T regimes (10≤T≤20)"
- Discussion 段落从 "permanent blind spot demands multi-method" 改为 "transient blind spots in moderate T motivate multi-method as default practice"

**具体改写位置**（D170 + 论文正文）：
1. `D170_narrative_drafts.md` Results 综合段最后一句 → 用 B.1d 模板
2. `D170_narrative_drafts.md` "6/8 ceiling and sync-dip" 段 → 用 B.1c 模板
3. `paper_framing.md` C2 section："Predicts 4 regimes" 列表 → Regime (III) 追加 "transient at sufficient T"
4. `paper_framing.md` #58 约束 → 更新措辞
5. Introduction C1 扩展段最后一句 → 用 B.1b 模板
6. Abstract → 用 B.1a 模板

### C.2 Permanence confirmed (=0/8) → C2/C3 impact

**C2 S×R 竞争模型**：
- Regime (III) sync dip 升级为 "permanent structural feature"
- 需要追加机制解释：为什么 √T scaling 无法克服 α=0.60 的同步效应？
- 候选解释：τ_relax(0.60) 精确匹配 Δt，不是 near-match 而是 exact resonance → √T 增长被 exact cancellation 完全抵消
- C2 paper_framing 追加："The permanence of the α=0.60 dip suggests exact resonance between contamination-induced relaxation and observation interval, a prediction not derivable from the basic S×R model without additional free parameters"

**C3 multi-method necessity**：
- 升级为与 C1 并列的核心贡献
- 叙事力度最强：**即使 α > α_c(T)，single-method detection 永久失效**
- 这是审稿人最难攻击的 contribution——4-T invariant + 理论预期 vs 实际不符 = genuine finding

**C1 phase diagram**：
- "Detectable region with embedded blind spots" 成为 landscape 的核心描述
- Phase diagram 图注需要标注 α=0.60 列为 structural blind channel

**具体改写位置**（同上列表，改用 B.2c/B.2b/B.2a 模板）

### C.3 Near-miss 边界情况处理

若 T=25 α=0.60 PermG = 1/8（仅一对刚过 FDR threshold）：
- 叙事上算 dissolution，但需 qualify："marginal dissolution (1/8, single pair)"
- 不能说 "gap closes"，只能说 "first evidence of dissolution"
- 建议追加 cross-seed (s43) 验证再最终定性

若 T=25 α=0.60 PermG = 0/8 但有 near-miss p_fdr < 0.064（比 T=20 更接近）：
- 叙事上算 permanence，但 Discussion 追加趋势分析：T=20 p=0.064 → T=25 p=0.0XX → "approaching dissolution at longer horizons"
- 这实际是最有叙事张力的结果——"dissolution in progress but not yet complete"

---

## D. Cross-seed 数据整合方案

### 当前 cross-seed 实验状态

| 实验 | Seed | GPU | 用途 |
|------|------|-----|------|
| t15_a045_s43 | s43 | 17855:2 | α=0.45 left-shift cross-seed |
| t15_a060_s43 | s43 | 17855:1 | sync-dip T=15 cross-seed |
| t20_a060_s43_v2 | s43 | 17855:4 | sync-dip T=20 cross-seed |
| t20_a045_s43 | s43 | 19828:1 | near-boundary T=20 cross-seed |

### D.1 整合优先级

**P0（robustness 核心）**：
1. **t15_a045_s43**：若 s43 也 ≥6/8 → α_c left-shift 跨 seed 确认，论文可删除 "single-seed" caveat
2. **t20_a060_s43_v2**：若 s43 也 =0/8 → sync-dip T=20 跨 seed 确认（当前仅 s42）

**P1（叙事加强）**：
3. **t15_a060_s43**：sync-dip T=15 跨 seed（s42 已 0/8）
4. **t20_a045_s43**：near-boundary 5/8 的 cross-seed 验证（最 informative：s43 也 5/8 → ceiling decay confirmed；s43=6/8 → s42 的 5/8 是 boundary noise）

### D.2 论文整合位置

**Phase Diagram 表格**：主表保持 s42 数据（20 cells），脚注或 Appendix 表报告 cross-seed 验证结果。

**正文措辞模板**：

对于 cross-seed 一致的格：
> "cross-validated with seed s43 (X/8, consistent)"——插入对应 Results 段落的相关句子后面，括号内。

对于 cross-seed 不一致的格（如 t20_a045 s42=5/8 vs s43≠5/8）：
> 需要根据差异幅度判断：
> - ±1/8 差异（如 5/8 vs 6/8）："boundary-adjacent stochastic variation (s42=5/8, s43=6/8)"
> - ≥2/8 差异：需要独立段落讨论，可能影响 claim 强度

**Robustness 支撑具体写法**：

在 Results 最后或 Discussion 开头追加一段（~3 句）：
> "Cross-seed validation at select cells confirms the stability of the detection landscape: [列举一致结果]. The one-pair variations observed at boundary-adjacent cells (e.g., α=0.45, T=20: s42=5/8, s43=X/8) are consistent with stochastic fluctuation at the phase boundary rather than seed-dependent landscape structure."

### D.3 Cross-seed 数据到达后的操作流程

1. 实验完成 → 运行 5method 分析 → 提取 PermG fwd 值
2. 对比 s42 值：一致（±1/8）→ 直接插入括号注释；不一致（≥2/8）→ 诊断 + 独立讨论
3. 更新 Phase Diagram Appendix 表（dual-seed 版本）
4. 更新 paper_framing.md 对应约束的 seed caveat

---

## E. T=25 数据到达后的执行清单

### E.1 数据验证（≤1h）
- [ ] 每格检查 gen 目录完整性 + all_metrics.json（遵守 C005: EXIT_CODE=129 不等于失败）
- [ ] 运行 5method 分析（PermG fwd 为主指标，遵守 M037: 只用 PermG 列）
- [ ] 提取 PermG fwd counts + FDR p-values
- [ ] 记录每格 near-miss p-values（尤其 α=0.60）

### E.2 场景判定（10min）
- [ ] α=0.60 PermG ≥1/8？→ Scenario A (dissolution) → 执行 B.1 系列模板
- [ ] α=0.60 PermG = 0/8？→ Scenario B (permanence) → 执行 B.2 系列模板
- [ ] α=0.45 PermG = 0/8？→ Scenario D (theory failure) → 紧急诊断
- [ ] α=0.45/0.50/0.75 是否都 ≥5/8？→ 确认 landscape stabilization 延伸至 T=25

### E.3 叙事更新（≤3h）
- [ ] 更新 Phase Diagram 表格（D170 + 论文正文）
- [ ] 用本文档对应场景模板改写 D170 的 6 个位置（Abstract/Intro/Results×3/综合段）
- [ ] 更新 paper_framing.md 约束 #57/#58
- [ ] 锁定 T=25 predict-then-verify 结果 → `artifacts/t25_predictions_scored.json`
- [ ] 生成 20/20 heatmap 定稿

### E.4 predict-then-verify T=25 scoreboard（需预锁定）

基于 T=10 sigmoid + √T scaling（√(25/10)=1.581）：

| α | T=10 actual | z_T10 | z_T25 | predicted rate | predicted count | CI |
|---|-------------|-------|-------|----------------|-----------------|-----|
| 0.45 | 0/8 | -2.608 | -4.124 | ~0.00 | 0/8 | [0, ~7]* |
| 0.50 | 6/8 | +0.663 | +1.048 | 0.853 | 7/8 | [~1, 8]* |
| 0.60 | 0/8 (dip) | -0.319 | -0.504 | 0.307 | 2-3/8 | [2, 3]** |
| 0.75 | 6/8 | +0.680 | +1.076 | 0.859 | 7/8 | [6, 8] |

\* α=0.45/0.50 CI 宽因 α_c uncertainty 横跨 transition（同 T=20 #55）
\** α=0.60 CI 窄因 fixed T=10 rate（不含 α_c uncertainty）

**⚠️ 已知 bias**：T=20 的 predict-then-verify 显示系统性保守偏差（α=0.45 predicted 0/8 actual 5/8）。T=25 α=0.45 大概率也会超预测，但不影响 falsifiability 框架的诚实报告。

**关键 falsifiable test**：α=0.75（CI=[6,8]）——若 <6/8 则 √T scaling 在检出区被证伪。

---

## F. 措辞红线（T=25 数据无论何结果都必须遵守）

1. **α_c(T) √T 公式**（#57）：T=25 只是第 5 个约束点（1 calibration + 4 consistency），不是 "5-point fit confirmed"
2. **Predict-then-verify**（#59）：报告 PASS/FAIL + actual vs CI，不说 "validated"
3. **6/8 ceiling**（#60）：若 T=25 出现 7/8 或 8/8，需要更新 ceiling 叙事；若维持 5-6/8，ceiling 追加第 4 个 T 值
4. **PermG only**（M037）：dose-response 图表只用 PermG 列，K≥3 冻结
5. **C005**：EXIT_CODE=129 不等于失败，先检查 gen 目录
6. **C008/C009**：threshold 用 registry 3σ + direction filter peak_lag < 0
