> **⛔ DEPRECATED — DO NOT USE** (Director 指令 2026-05-16)
> 本文件含 NVE/ve_ratio 混淆错误（6.59x 是 raw ve_ratio，不是 NVE）。
> 权威审计文档：`artifacts/_project/report/framing_b_reaudit.md`（使用正确的 NVE=10.42x）。

# ~~Framing B Re-audit: 逐章节 Diff 清单~~ [DEPRECATED]

**Date**: 2026-05-16
**Framing**: B — 诊断论文 + SGS informative negative result
**Drivers**: D059 (Framing B approved), D061 (016e = no-op), D040 (C6 partially falsified)
**Scope**: 所有论文章节对齐 Framing B。不修改文件，仅列出变更清单。

---

## 核心事实变更表

| # | 旧解读 | 新解读 (Framing B) | 来源 | 关键数字 |
|---|--------|-------------------|------|----------|
| F1 | 016e SGS 延迟 collapse | 016e SGS 是 architectural no-op（reward→dt_emb 梯度恒为 0） | D061 | reward grad norm = 0.000 |
| F2 | CIVO 由 reward head co-adaptation 驱动 | CIVO 由 obs decoder 梯度驱动（93%），reward head 是 free-rider | D061 | obs 1.505 (93%), KL 0.119 (7%), reward 0.000 (0%) |
| F3 | dt=1 imagination 是 practical mitigation | dt=1 imagination 消除 Pathway A (CIVO) 但不消除 Pathway B (eval-driven instability)，1/2 seeds 崩溃 | D040 | 008e_v3_s2: 715@95K→137@105K, nve=3.78x |
| F4 | Full-SGS 待定 | Full-SGS (018) 移除 93% 梯度，是真正的 gradient-level intervention | D060 | planned |
| F5 | NVE: AUROC=1.0 | NVE: AUROC=0.933, 7/8 accuracy, 1 FP (008e_v3_s2 non-CIVO) | D054 | B2 threshold ≥1.5x@35K+ |

---

## 1. Abstract（未起草 → 从零撰写）

### 必须包含的 claims（按 Framing B）

- [ ] **C1**: 所有 dt>1 配置均降级（3 configurations）
- [ ] **C2**: trained dt_emb 可靠触发 pathological NVE>1.5x（4/4 separation），collapse 是 stochastic（1/2 seeds）
- [ ] **CIVO 术语**: 使用 "conditioning-induced value overestimation"，不用 "delusional critic"
- [ ] **NVE 诊断**: AUROC=0.933, 7/8 accuracy（不是 1.0）
- [ ] **梯度分解**: dt_emb 93% 梯度来自 obs decoders, 0% 来自 reward → reward SGS 是 no-op
- [ ] **多条崩溃路径**: Pathway A (CIVO, value-driven) + Pathway B (eval-driven instability)
- [ ] **TAWM 对比**: dt-conditioning 在 MPC 成功但在 imagination-based AC 失败 → architecture-specific vulnerability
- [ ] **Mitigation**: dt=1 imagination 是 partial mitigation（消除 CIVO 但不消除所有 failure modes）

### 约束

- CoRL 格式 abstract 通常 150-200 words，需要高度压缩
- 不要提 "stochastic downstream outcomes" 细节，留给 intro 展开

---

## 2. Introduction（未起草 → 从零撰写）

### Contribution list（Framing B 版本）

- [ ] **(1)** 系统性因果诊断：factorial experiment isolating trained dt_emb 为 CIVO 必要条件
- [ ] **(2)** NVE 诊断指标：AUROC=0.933, 7/8 accuracy，区分 pathological vs benign overestimation
- [ ] **(3)** 多条脆弱性路径：dt=1 imagination 消除 CIVO 但 1/2 seeds 仍崩溃（non-CIVO pathway）
- [ ] **(4)** 梯度分解 + SGS informative negative：93% obs decoders, 0% reward → reward SGS = no-op → observation reconstruction 是 dt_emb 训练的主驱动
- [ ] **(5)** TAWM 对比 novelty：dt-conditioning 在 MPC (TD-MPC2) 成功 vs imagination-based AC 失败

### 关键措辞

- [ ] **不要写** "dt=1 imagination is a practical mitigation" → 改为 "dt=1 imagination eliminates CIVO but does not prevent all collapse modes"
- [ ] **不要写** "SGS delays collapse" → 已撤回
- [ ] **引用 TAWM** (Nhu et al., ICML 2025) 作为 novelty 支撑

---

## 3. Related Work（未起草 → 从零撰写）

### 必须覆盖的文献领域

- [ ] Temporal abstraction in model-free RL（options, FiGAR, action repeat）
- [ ] World-model RL（Dreamer family, IRIS, TWM）
- [ ] Variable-rate planning in world models（TAWM 必须出现）
- [ ] Value overestimation in MBRL（Janner et al. 2019; Lu & Schuurmans 2018 delusional bias — 明确区分 CIVO vs delusional bias）
- [ ] Stop-gradient in representation learning（可选，如果 space 允许）

### 约束

- [ ] **不要** claim "gradient stopping on reward head" 是 viable mitigation — D061 已排除
- [ ] **明确区分** Lu et al. 2018 的 delusional bias（policy-class constraints）和本文 CIVO（model imprecision + learned conditioning）
- [ ] 检查 `artifacts/related_work_draft.md` 是否有可复用内容

---

## 4. Methodology — `paper/method.md`（已起草，需修改）

### 4.1 §3.1 — "The Delusional Critic Hypothesis" 标题和内容

**文件**: `paper/method.md:39-43`

- [ ] **RENAME** section title: ~~"The Delusional Critic Hypothesis"~~ → **"The CIVO Hypothesis"** 或 **"Conditioning-Induced Value Overestimation"**
  - 旧: `### The Delusional Critic Hypothesis` (line 39)
  - 新: `### Conditioning-Induced Value Overestimation (CIVO)`
- [ ] **UPDATE** line 43: ~~"We term this the *CIVO*, drawing on Lu & Schuurmans..."~~ → 保留 CIVO 定义但 section title 对齐

### 4.2 §3.3 Mitigation 段落 — C6 partial falsification

**文件**: `paper/method.md:135-143`

- [ ] **REWRITE** mitigation section — 当前写法将 008e_v3 呈现为成功 mitigation，忽略 seed 2 崩溃
  - 旧 (line 139): "At 105K steps, it achieves eval return 869.9 (exp_008e_v3, seed 1), 95% of baseline"
  - 新: 保留 seed 1 数据，**ADD** seed 2 崩溃数据 (715@95K→137@105K, nve=3.78x)，标注 1/2 seeds 崩溃
- [ ] **REWRITE** line 142-143: ~~"(1) the result rests on a single independent seed (seed 1; seed 2 is in progress)"~~ → seed 2 已完成且崩溃
  - 新: "(1) seed 2 (008e_v3_s2) collapsed via a non-CIVO pathway (eval-driven instability, entropy ↑) — dt=1 imagination eliminates CIVO (Pathway A) but not all failure modes (Pathway B)"
- [ ] **UPDATE** 措辞: ~~"This is the only tested configuration that simultaneously avoids pathological overestimation..."~~ → 加限定 "in 1/2 tested seeds"
- [ ] **ADD** Pathway A vs B 区分表（008d CIVO: value explosion→entropy↓ vs 008e_v3_s2 non-CIVO: eval crash→entropy↑）

### 4.3 新增 §3.X — Selective Gradient Stopping (SGS)

**文件**: `paper/method.md` — 在 §3.3 Mitigation 之后新增

- [ ] **ADD** new subsection: "Selective Gradient Stopping (SGS)"
  - 定义 SGS: 在 backprop 中 detach dt_emb 与特定 loss head 之间的梯度通路
  - Reward-only SGS (016e): `sg(e_Δt)` 仅在 reward head 前
  - Full-SGS (018): `sg(e_Δt)` 在所有 non-KL head 前（obs decoders + reward + cont）
  - 动机: 测试 CIVO 是 gradient-driven（特定 head 训练 dt_emb）还是 representation-level

### 4.4 新增 — Gradient Decomposition 方法

**文件**: `paper/method.md` — 在 SGS 之后

- [ ] **ADD** paragraph on gradient decomposition methodology:
  - `torch.autograd.grad` per-head analysis of dt_emb.weight
  - 独立计算每个 loss component 对 dt_emb.weight 的 gradient norm
  - 报告各 head 贡献占总 gradient norm 的比例

### 4.5 RSSM Fidelity Analysis — 微调

**文件**: `paper/method.md:127-131`

- [ ] **ADD forward reference** after line 131: "§X.X shows that this reward gap is a downstream effect of features learned via obs reconstruction gradients (93%), not the cause of dt_emb's temporal specialization (see gradient decomposition, Table X)."

---

## 5. Experimental Setup — `paper/sections/experimental_setup.md`（已起草，需修改）

### 5.1 Factorial Table (Table 1) — 新增行

**文件**: `paper/sections/experimental_setup.md:55-78`

- [ ] **ADD** 016e row after line 75 (005 之前):
  ```
  016e & SGS (reward) & trained$^*$ & on & 8 & 2 & Gradient intervention \\
  ```
  Footnote: `$^*$trained but reward head gradients detached from dt-embedding`
- [ ] **ADD** 018 row (if results available):
  ```
  018 & Full-SGS & trained$^\dagger$ & on & 8 & 2 & Gradient intervention \\
  ```
  Footnote: `$^\dagger$trained but all non-KL head gradients detached`
- [ ] **UPDATE** table caption (line 57): mention gradient intervention conditions

### 5.2 Base Architecture — 修正

**文件**: `paper/sections/experimental_setup.md:30`

- [ ] **UPDATE** line 30: ~~"All other DreamerV3 components...remain unmodified"~~ → 加注 "except for gradient flow modifications in the SGS conditions (§X.X)"

### 5.3 Multi-seed Replication — 更新

**文件**: `paper/sections/experimental_setup.md:89`

- [ ] **UPDATE** line 89: ~~"Multi-seed runs for the mitigation condition (008e_v3) with seeds 1 and 2 are in progress"~~ → "Multi-seed runs for the mitigation condition (008e_v3) are complete: seed 1 achieves 95% baseline recovery; seed 2 collapses via a non-CIVO pathway (§X.X)."

### 5.4 Key Controlled Comparisons — 新增

**文件**: `paper/sections/experimental_setup.md:80-87`

- [ ] **ADD** new bullet after 008e_v3 item (line 87):
  - `008d vs 016e` (trained dt_emb vs trained with reward SGS; all else equal): isolates reward gradient pathway as a contributor to CIVO. Both collapse → reward pathway carries no gradient signal (§X.X).

---

## 6. SGS Informative Negative — `paper/sections/sgs_informative_negative.md`（已起草，需修正）

### 6.1 NVE 数字错误 ⚠️

**文件**: `paper/sections/sgs_informative_negative.md:31`

- [x] **VERIFIED** line 31: "$10.42\times$ at step 95K" is correct (normalized NVE from registry `civo_nve_peak: 10.42`). 6.59x is the raw V/E ratio, not the normalized NVE.

### 6.2 Seed 说明混淆

**文件**: `paper/sections/sgs_informative_negative.md:33`

- [ ] **CLARIFY** line 33: ~~"Both experiments use different random seeds in practice (exp_016e: seed 1; exp_008d: seed 1, but with different initialization order due to the code modification)"~~ → 简化为 "Both experiments use seed 1; differences in timing and magnitude are within the range of cross-seed variation observed in the broader 008d seed replications (Table X)."

### 6.3 "Delayed but Equivalent Collapse" 标题

**文件**: `paper/sections/sgs_informative_negative.md:25`

- [ ] **CONSIDER RENAME**: 当前标题暗示 "delayed"，但 D061 确认 016e 是 no-op，timing difference 归因于 random variation。建议: ~~"Delayed but Equivalent Collapse"~~ → **"Equivalent Collapse: The SGS Is a No-Op"**

### 6.4 Overall — 已基本完整

- [ ] Section 整体结构合理（hypothesis → experiment → null result → gradient decomposition → implications）
- [ ] **VERIFY** 梯度 norm 数字与 D061 一致: obs 1.505 (93%), KL 0.119 (7%), reward 0.000 (0%) ✓ (line 51-56)
- [ ] **VERIFY** Full-SGS (018) forward reference (line 71) — 如果 018 结果在 DDL 前出来，需要更新

---

## 7. Results（未起草 → 从零撰写，但 `sgs_informative_negative.md` 覆盖部分内容）

### 7.1 Finding 结构（Framing B 版本）

| Finding | Claim | 实验 ID | 关键数字 | Status |
|---------|-------|---------|----------|--------|
| F1 | 所有 dt>1 降级 | 005, 006, 007 | 006 peak 485→collapse; 007 peak 177 (33% baseline) | 不变 |
| F2 | trained dt_emb → NVE>1.5x (4/4) | 008d, 009b, 008f, 009c | 008d: 1.71x@35K→4.12x@55K; 009b: 1.62x@45K | 不变 |
| F3 | untrained dt_emb 抑制 value drift | 008a, 008c | 008a@105K=778 (85% baseline), nve 0.59-0.93x | 不变 |
| F4 | longer dt 放大问题 | 006, 007 | dt=1 ~950 > dt=2 485 > dt=4 177 | 不变 |
| F5 | horizon/subsample 是次要因素 | 008a, 008c, 008e_v3 | 008c (H=8) ~242 vs 008a (H=15) 778 | 不变 |
| F6 | dt=1 imag 不阻止所有 collapse | 008e_v3 s1, s2 | s1: 869.9 (95% baseline); s2: 137 (collapsed, nve=3.78x) | **修改**: 旧=dt=1 is mitigation → 新=partial, 1/2 collapsed via non-CIVO |
| **F7** | **Reward SGS = no-op** | **016e** | **peak 326.7@75K→31.7@95K, NVE=10.42x; reward grad=0** | **新增** |
| **F8** | **梯度分解: obs 93%, reward 0%** | **D061** | **obs 1.505, KL 0.119, reward 0.000** | **新增** |

### 7.2 F6 修改细节

- [ ] 旧 claim: "dt=1 imagination achieves 95% baseline recovery"
- [ ] 新 claim: "dt=1 imagination achieves 95% baseline recovery in 1/2 seeds (seed 1: 869.9@105K). Seed 2 collapses to 137@105K (nve=3.78x) via a non-CIVO pathway characterized by eval-driven instability (entropy ↑) rather than value-driven exploitation (entropy ↓)."
- [ ] **ADD** 008e_v3_s2 vs 008d collapse mechanism 对比表:

| 特征 | 008d s1 (CIVO) | 008e_v3_s2 (non-CIVO) |
|------|----------------|----------------------|
| value 变化 | 爆炸 +130%@55K | 温和 +13%→-12% |
| eval 变化 | 先升后跌 -43% | **先跌** -81% |
| nve 驱动 | value 分子 | eval 分母 |
| actor_entropy | ↓ (lock-in) | **↑** (de-specialization) |
| 机制 | critic overestimate→actor exploit | eval crash→value lag |

- [ ] **ADD** 009a baseline s2 稳定数据 (618→596→836) 排除 seed 脆弱假说

### 7.3 F7 + F8 新增内容

- [ ] **ADD** 016e 学习曲线数据: peak 326.7@75K→31.7@95K, NVE=10.42x@95K
- [ ] **ADD** 016e vs 008d 对比: 两者均 collapse，timing 差异归因于随机变异
- [ ] **ADD** gradient decomposition table (Table X):

| Loss Component | Grad Norm | Share (%) |
|----------------|-----------|-----------|
| Observation decoders | 1.505 | 93 |
| KL dynamics | 0.119 | 7 |
| Continuation head | <0.001 | <1 |
| Reward head | 0.000 | 0 |
| **Total** | **1.624** | **100** |

- [ ] **ADD** 两条 implications: (1) CIVO 不是 reward-gradient-driven; (2) reward head 的 2.78x gap 是 obs-learned features 的 downstream effect

### 7.4 NVE Sensitivity Table — 已有

**文件**: `paper/tables/nve_sensitivity_table.tex` — 已正确，无需修改
- B2 (main): AUROC=0.933, 87.5%, 1 FP (IRD)
- B1 (app.): AUROC=1.000, 100%, n_pos=2

### 7.5 Main Results Table — 新增 016e 行

- [ ] **ADD** 016e 到 main results table:
  ```
  016e | SGS (reward detach) | trn* | ON | 8 | 31.7@95K | 10.42× | Collapsed (no-op)
  ```

---

## 8. Discussion（未起草 → 从零撰写）

### 8.1 §5.1 CIVO Mechanism — 梯度不对称性

- [ ] **INCLUDE** 四阶段反馈环描述（trained e_Δt → biased latent → reward gap 2.78x → critic exploitation → actor lock-in）
- [ ] **ADD** 梯度不对称发现段落:
  - "While the CIVO feedback loop operates through reward predictions (Stage 1), the dt-embedding itself is trained overwhelmingly by observation decoders (93%) and receives zero gradient from the reward head. The reward head's 2.78× prediction gap is a free-rider effect — it exploits features that dt_emb learned for observation reconstruction, not features shaped by reward gradients."
- [ ] **ADD** implication: reward→dt_emb 干预（016e）是 no-op，真正的干预目标是 obs→dt_emb

### 8.2 §5.2 CIVO Two-Stage Amplification

- [ ] **INCLUDE**: dynamics bias 1.68x (36%) + actor exploitation (64%), bootstrap CI confirms

### 8.3 §5.3 Value Self-Correction (009b)

- [ ] **INCLUDE**: 009b transient nve>1.5x → self-correction, sustained vs transient 区分, "point of no return" 概念

### 8.4 §5.4 Multiple Vulnerability Pathways

- [ ] **INCLUDE** D040 三条崩溃路径:
  - Pathway A: CIVO (008d, 006) — trained dt_emb → dt=2 imagination optimism → value inflation → actor exploitation. NVE>1.5x sustained
  - Pathway B: Imagination-Reality Divergence (008e_v3_s2) — world model ceiling → eval crash → entropy ↑. NVE passive (denominator-driven)
  - Pathway C: Gradient Starvation (015b) — frozen dt_emb → representation drift → actor_loss→0. NVE transient
- [ ] **ADD** 016e 作为 Pathway A 的梯度证据: Pathway A 不是 reward-gradient-driven

### 8.5 §5.5 dt-Embedding Dilemma

- [ ] **旧 dilemma**: {remove dt_emb (008f, 消除 CIVO 但 reward MAE 75x), keep dt_emb (collapse risk)}
- [ ] **新 dilemma 扩展**: 三角困境 — (a) remove (008f, safe but degraded), (b) keep + dt=1 imag (008e_v3, partial, 1/2 collapse via Pathway B), (c) keep + SGS (016e reward SGS = no-op; Full-SGS 018 = pending, removes 93% obs gradient)
- [ ] **KEY**: 梯度分解缩小了 intervention target — 从 "regulate dt_emb" 到 "specifically target obs decoder→dt_emb gradient pathway"

### 8.6 §5.6 Implications for Temporal Abstraction

- [ ] **不要写** ~~"gradient stopping"~~ 泛称 → 改为 "gradient stopping on observation-decoder pathways (Full-SGS), which removes 93% of the embedding's training signal"
- [ ] **不要写** ~~"reward gradient stopping could mitigate"~~ — D061 已排除
- [ ] **ADD**: TAWM 对比 — dt-conditioning 在 MPC 成功因为 MPC 不做 imagination-based actor-critic training，vulnerability 是 architecture-specific
- [ ] **ADD**: 推荐 hierarchical approaches (THICK, Hieros) 避免 flat dt-conditioning 的根因

### 8.7 §5.7 Limitations

- [ ] Single primary environment (Walker Walk)，Cheetah/Cartpole in progress
- [ ] Small seed count (2 seeds per condition)
- [ ] NVE threshold 是 empirical marker，非 formal hypothesis test
- [ ] 016e/008d timing difference 无法 definitively 排除 partial SGS effect（但梯度分解强烈支持 no-op 解读）

---

## 9. Conclusion（未起草 → 从零撰写）

### Finding 枚举（Framing B 版本，6 条）

- [ ] **(1)** 所有 dt>1 配置降级（C1: 006, 007, 005）
- [ ] **(2)** trained dt_emb 可靠触发 NVE>1.5x，4/4 separation，collapse stochastic 1/2（C2）
- [ ] **(3)** untrained dt_emb 抑制 value drift，85% baseline@105K（C3: 008a）
- [ ] **(4)** dt=1 imagination 消除 CIVO 但不消除所有 collapse modes，1/2 seeds 崩溃 via non-CIVO pathway（C6, D040）
- [ ] **(5)** NVE 诊断: AUROC=0.933, 7/8 accuracy, distinguishes CIVO from non-CIVO collapse（D054）
- [ ] **(6)** 梯度分解: dt_emb 93% gradient from obs decoders, 0% reward → reward SGS (016e) = no-op, obs reconstruction 是 temporal co-adaptation 的主驱动（D061）

### Future Directions（3 条）

- [ ] **(1)** Hierarchical approaches (THICK, Hieros) 避免 flat dt-conditioning 根因
- [ ] **(2)** Full-SGS (018): detach obs decoder→dt_emb gradient (removes 93%), 区分 gradient-driven vs representation-level CIVO。~~Reward gradient stopping~~ 已排除。
- [ ] **(3)** Transformer world models 是否有相同 vulnerability（IRIS, TWM 无 RSSM 但有类似 temporal conditioning 可能）

---

## 10. Figures

### 已规划 → 需更新

| Fig | 内容 | 状态 | Framing B 变更 |
|-----|------|------|---------------|
| Fig 1 | Hero: learning curves (all experiments) | 规划中 | **ADD** 016e trace，标注 no-op |
| Fig 2 | NVE trajectories (healthy vs pathological) | 规划中 | **ADD** 016e NVE trace; **ADD** 008e_v3_s2 trace (non-CIVO collapse) |
| Fig 3 | Factorial grid summary (2×2) | 规划中 | 无变更 |
| Fig 4 | Causal diagram | 规划中 | **UPDATE** 加入 gradient decomposition: obs decoders→dt_emb (93%) 标注 |
| Fig 5 | dt=1 vs dt=2 vs dt=4 | 规划中 | 无变更 |
| Tab 1 | RSSM fidelity | 规划中 | **ADD forward ref** to gradient decomposition |

### 新增 Figures

| Fig | 内容 | 数据来源 |
|-----|------|----------|
| **Fig X** | 016e vs 008d learning curves overlay — visual no-op evidence | 016e, 008d eval logs |
| **Fig Y** | Gradient decomposition bar chart (obs 93%, KL 7%, reward 0%) | D061 |
| **Fig Z** | 008e_v3_s2 collapse mechanism: dual panel (eval+value+entropy timeline) vs 008d | 008e_v3_s2, 008d logs |
| **Tab X** | Gradient decomposition table (in §Results or §SGS section) | D061 |

---

## 11. Cross-Cutting Constraints

### 数字一致性

| 数据点 | 正确值 | 来源 | ⚠️ 冲突 |
|--------|--------|------|---------|
| 016e peak eval | 326.7@75K | registry | — |
| 016e collapse eval | 31.7@95K | registry | — |
| 016e NVE | **10.42x@95K** | registry (`civo_nve_peak`) | 10.42x is the normalized NVE; 6.59x is the raw V/E ratio — use normalized |
| 008d NVE@55K | 4.12x | registry | — |
| 008e_v3_s2 NVE@105K | 3.78x | registry | — |
| NVE AUROC | 0.933 | D054 | 早期版本用 1.0 → 必须用 0.933 |
| NVE accuracy | 7/8 (87.5%) | D054 | — |
| Gradient: obs | 1.505 (93%) | D061 | — |
| Gradient: KL | 0.119 (7%) | D061 | — |
| Gradient: reward | 0.000 (0%) | D061 | — |

### 禁止措辞

| ❌ 不要写 | ✅ 替换为 | 原因 |
|-----------|----------|------|
| "SGS delays collapse" | "SGS is an architectural no-op" | D061 撤回延迟解读 |
| "SGS partially effective" | 同上 | D057/D058 解读已撤回 |
| "delusional critic" | "conditioning-induced value overestimation (CIVO)" | D037 术语决定 |
| "dt=1 imagination is a practical mitigation" | "dt=1 imagination eliminates CIVO but does not prevent all collapse" | D040 C6 partially falsified |
| "reward gradient stopping could mitigate" | "reward gradient stopping is an architectural no-op" | D061 |
| "AUROC=1.0" | "AUROC=0.933" | D054 corrected |

---

## 12. Priority Edit Order

| 优先级 | 章节 | 内容 | 工作量 |
|--------|------|------|--------|
| **P0** | `sgs_informative_negative.md` | VERIFIED NVE 10.42x is correct (normalized), FIX seed 说明 | 小 (1 处修改) |
| **P1** | `method.md` §3.3 Mitigation | REWRITE: 加 008e_v3_s2 崩溃数据, partial falsification | 中 |
| **P2** | `method.md` §3.1 | RENAME "Delusional Critic Hypothesis" → CIVO | 小 |
| **P3** | `method.md` 新增 SGS + gradient decomposition sections | ADD 2 new subsections | 中 |
| **P4** | `experimental_setup.md` Table 1 | ADD 016e/018 rows, update multi-seed notes | 小 |
| **P5** | §4 Results | 从零撰写 F1-F8 | 大 |
| **P6** | §5 Discussion | 从零撰写 (梯度不对称、多路径、dilemma、TAWM) | 大 |
| **P7** | §6 Conclusion | 从零撰写 6 findings + 3 future directions | 中 |
| **P8** | §1 Introduction | 从零撰写 contribution list (5 items) | 中 |
| **P9** | Abstract | 从零撰写 (150-200 words) | 中 |
| **P10** | §2 Related Work | 从零撰写 | 中 |
| **P11** | Figures | 新增 016e overlay + gradient bar chart + 008e_v3_s2 mechanism | 中 |

---

## 附录: 实验 ID 快速参考

| ID | 配置 | 结果 | 角色 |
|----|------|------|------|
| 001 | Baseline (dt=1, H=15) | ~950 stable | Reference |
| 005 | Learned gate | 541→99 collapse | C1 evidence |
| 006 | Fixed dt=2, trained, sub ON, H=15 | 485→135 collapse | C1, C2 evidence |
| 007 | Fixed dt=4, trained, sub ON, H=15 | peak 177 | C4 evidence |
| 008a | Untrained, sub OFF, H=15 | 778@105K (85% baseline) | C3 evidence |
| 008c | Untrained, sub OFF, H=8 | ~242 plateau | C5 evidence |
| 008d | Trained, sub ON, H=8 | collapse, NVE 4.12x@55K | C2 primary, CIVO exemplar |
| 008e_v3 s1 | Trained, sub ON, H=15, dt=1 imag | 869.9@105K (95% baseline) | C6 partial (Pathway A eliminated) |
| 008e_v3 s2 | Same, seed 2 | 137@105K (collapsed, nve=3.78x) | C6 partial falsification (Pathway B) |
| 008f | Removed (d=0), sub ON, H=8 | stable, reward MAE 75x | C2 causal control |
| 009a | Baseline seed 2 | stable (618→596→836) | Rules out seed fragility |
| 009b | 008d seed 2 | 268@105K, self-corrected | C2 stochastic collapse evidence |
| 009c | 008f seed 2 | nve≤1.26x | C2 no-emb control seed 2 |
| 015b | Frozen dt_emb | gradient starvation | Pathway C |
| **016e** | **Reward SGS (detach)** | **326.7→31.7 collapse, NVE=10.42x** | **F7: no-op evidence** |
| **018** | **Full-SGS (all detach)** | **planned** | **True gradient intervention** |
