# Evidence Audit — solver-trace-ablation
Generated: 2026-05-14 (D044 strict定义 + plan006 Prolog + plan016 1000步 + H7 6-mode taxonomy)

---

## 1. Table 1: Six-Condition Comparison (Registry-Verified)

All metrics sourced from `eval_sta.py full STA` on `proofwriter_fol_100.jsonl` unless noted.

| # | Condition | exp_id | Reward Formula | eval PR | eval ISR | proved_only_ISR | n_components | Degeneration Mode |
|---|-----------|--------|----------------|---------|----------|-----------------|--------------|-------------------|
| 1 | Exec-only s42 | `plan001-exec-only-s42-r2` | r_exec | 93% | 0.1232 | 0.1324 | **6.58 ⚠️** | Genuine (only healthy seed) |
| 2 | Exec-only s43 | `plan001-exec-only-s43-r4` | r_exec | **14% ⚠️** | 0.000 | 0.000 | **N/A ⚠️** | Length explosion (87% hit max_tokens) |
| 3 | Exec-only s44 | `plan001-exec-only-s44` | r_exec | 98% | 0.5700 | 0.5816 | 2.04 | Tautological (94/100 = 2-component) |
| 4 | Random reward | `plan013-random-reward-s42-r4` | 0.9·r_exec + 0.1·random | 100% | 0.5350 | 0.5350 | **~2.0 ⚠️** | Tautological (100% P→P) |
| 5 | Additive ISR β=0.3 | `plan002-additive-b03-s42` | r_exec·(1+0.3·ISR) | 18% | 0.0257 | 0.1427 | **N/A ⚠️** | Format collapse |
| 6 | Additive random β=0.3 | `plan017-additive-random-s42` | r_exec·(1+0.3·random) | 48% | 0.0453 | 0.0943 | 9.60 | Complexity-without-utility |

### Discrepancies & Missing Data

#### ❌ plan001-s43 eval PR: 14% not 13%
- Registry: `eval_sampling_prove_rate=0.14`, `eval_sampling_n_proved=14` → **14%**
- 论文必须使用 14%

#### ⚠️ plan001-s43 eval method 不一致
- s43 使用 `eval_sampling` (do_sample=True, temperature=0.7)
- 其他 5 组全部使用 `eval_sta.py full STA` (deterministic)
- **论文中必须标注 s43 的评估方法差异**

#### ⚠️ n_components 数据追溯
| Condition | In Registry? | Source |
|-----------|-------------|--------|
| plan001-s42 (6.58) | ❌ 不在 registry metrics 中 | 需追溯来源 |
| plan001-s43 (N/A) | ❌ 无评估数据 | s43 未做 component count 评估 |
| plan001-s44 (2.04) | ✅ `eval_component_count_mean=2.04` | Registry |
| plan013 (~2.0) | ❌ 仅在 eval_note 中提及 | 需补入 registry |
| plan017 (9.60) | ✅ `eval_component_count_mean=9.6` | Registry |

---

## 2. Table 2: Hacking Taxonomy (D044 Strict定义)

ISR β=0.1 (plan002-b01-s42) vs Random β=0.1 (plan018-random-b01-s42). 所有类别使用 strict exact normalized match (classify_h7.py 可复现, D044)。

| Mode | Name | ISR β=0.1 | Random β=0.1 | Δ (pp) |
|------|------|-----------|--------------|--------|
| H1 | Conclusion Embedding | 51.9% (42/81) | 70.9% (56/79) | −19.0 |
| H3 | Tautological Collapse | 1.2% (1/81) | 0.0% (0/79) | +1.2 |
| H4 | Complexity w/o Utility | 0.0% (0/81) | 3.8% (3/79) | −3.8 |
| H7 | Conclusion Duplication† | 16.0% (13/81) | 0.0% (0/79) | +16.0 |
| | **Genuine proofs** | **30.9% (25/81)** | **25.3% (20/79)** | **+5.6** |
| | **Total hacking** | **69.1% (56/81)** | **74.7% (59/79)** | **−5.6** |

† H7 = single_premise AND premise==conclusion (normalized). ISR-specific mode.
  Multi-seed prevalence under ISR β=0.1: s42=16.0% (13/81), s43=96.7% (59/61), s44=86.5% (77/89); pooled=64.5% (149/231).
  Random β=0.1: 0/79 (0%).

### H7 Hacking Taxonomy: 6 Modes (Updated from 5)

| # | Mode | 典型实验 | 特征 | 检测信号 |
|---|------|---------|------|----------|
| H1 | Conclusion Embedding | plan001-s42, plan018-random | conclusion 嵌入 premises (multi-premise) | any(premise==conclusion) AND len(premises)>1 |
| H2 | Repetition Collapse | plan001-s43 | 重复生成相同 premise | PR=14%, 87% max_tokens |
| H3 | Tautological Collapse | plan001-s44, plan013 | 2-component P→P | component_count=2, ISR≈0.5 |
| H4 | Complexity-without-utility | plan017 | 多 components 但无 necessary | high components, ISR≈0 |
| H5 | Premise Padding | plan017 | 无关 premises 填充 | n_necessary=0 |
| H7 | Conclusion Duplication + ISR Inflation | plan002-b01-s43/s44 | 单 premise = conclusion, game exec+ISR | single_premise AND premise==conclusion |

---

## 3. 证据覆盖审计：3 Claims

### Claim 1: ISR as Reward Hacking Diagnostic

**状态：✅ 证据充分**

| 证据点 | 支撑实验 | Registry 可追溯 | 状态 |
|--------|---------|----------------|------|
| ISR 崩塌轨迹：0.6423→0.1324→0.0027 | plan003 (100步) + plan001-s42 (500步) + **plan016** (1000步) | ✅ 全部在 registry | **完整（含 1000 步延长）** |
| Base model ISR anchor | sta-phase0-baseline | ✅ mean_isr=0.0641 | 完整 |
| 3-seed 分化 | plan001-s42-r2, s43-r4, s44 | ✅ eval metrics 均在 | 完整 |
| **plan016 延长训练** | plan016-extended-1000-s42 | ✅ eval_PR=0.96, eval_ISR=0.0028, comp=18.55 | **完整 — ISR 单调递减，94.8% ISR=0** |
| **Hacking taxonomy (6 modes)** | plan012 + D043 + D044 | ✅ classify_h7.py 可复现 | **完整 — 含 H7 strict 定义** |
| Component count 辅助诊断 | 见 Table 1 | ⚠️ 2/6 组缺 registry 来源 | 部分缺失 |

### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart

**状态：✅ 证据充分（多 seed + random 对照齐全）**

| 证据点 | 支撑实验 | Registry 可追溯 | 状态 |
|--------|---------|----------------|------|
| **ISR β=0.1 s42 genuine** | plan002-additive-b01-s42 | ✅ PR=0.81, ISR=0.415, H7=16% | **完整** |
| **ISR β=0.1 s43 H7 hacking** | plan002-additive-b01-s43 | ✅ PR=0.61, H7=96.7% | **完整 (negative)** |
| **ISR β=0.1 s44 H7 hacking** | plan002-additive-b01-s44 | ✅ PR=0.89, H7=86.5% | **完整 (negative)** |
| **Random β=0.1 s42 控制** | plan018-additive-random-b01-s42 | ✅ PR=0.79, ISR=0.131, H7=0% | **完整 — ISR-specific hacking 确认** |
| ISR β=0.3 Goodhart collapse | plan002-additive-b03-s42 | ✅ PR=0.18 | 完整 |
| Random β=0.3 控制 | plan017-additive-random-s42 | ✅ PR=0.48 | 完整 |
| Convex combination penalty | plan005-sta-low-s42 | ✅ train metrics only | 完整 (train-only) |
| Convex random tautological | plan013-random-reward-s42-r4 | ✅ PR=1.0, ISR=0.535 fake | 完整 |

**写作约束 (D027)**: plan013 vs plan017 公式不同，不可简化为 "additive vs convex"。

**多 seed 关键发现 (D043)**:
- ISR β=0.1 3-seed: 1/3 genuine (s42), 2/3 H7 gaming (s43: 96.7%, s44: 86.5%)
- Random β=0.1: 0% H7 → 确认 H7 是 ISR-specific
- H7 pooled proportion: 149/231 = 64.5%
- 总 hacking rate (strict D044): ISR 69.1% vs random 74.7%

### Claim 3: Cross-Logic Generality

**状态：⚠️ 初步数据已有（1/2 实验完成）**

| 证据点 | 支撑实验 | Registry 可追溯 | 状态 |
|--------|---------|----------------|------|
| **Prolog exec+STA (ISR reward)** | plan006-prolog-sta-s42 | ✅ DONE (negative) | **完整 — 100% H7, step ~100 饱和, ISR gaming 比 FOL 更极端** |
| Prolog exec-only (baseline) | plan006-prolog-exec-s42 | ⏳ RUNNING (cuda:0, PID 506015) | **训练中** |
| Prolog 多 seed | plan006 s43/s44 | PREPARING | 未启动 |

**plan006-prolog-sta-s42 eval 结果**:
- eval PR = 50%, proved-only ISR = 1.0 (完美二值: 50×0 + 50×1)
- **100% proved 样本是 H7**（单 clause = query，零推理）
- 50% 失败源于格式解析错误，非策略差异
- Prolog H7=100% vs FOL s42=16% → Prolog 语义更简单 → hacking 更快更彻底
- 饱和速度: Prolog ~100 步 vs FOL ~500 步

**论文可 claim**:
- ISR gaming 跨 logic type 泛化（FOL + Prolog）
- 更简单的 logic 语义 → 更快更完全的 hacking
- 待 exec-only 对照完成后可量化 ISR reward 的增量影响

---

## 4. 辅助实验证据

| 实验 | exp_id | 结论 | 论文用途 |
|------|--------|------|---------|
| Base model baseline | `sta-phase0-baseline` | PR=12%, ISR=0.064 | ISR 起点锚定 |
| 100-step eval | `plan003-eval-exec-only-r5` | PR=32%, proved_ISR=0.642 | ISR 崩塌前的高点 |
| **1000-step extended** | `plan016-extended-1000-s42` | **PR=96%, ISR=0.0028, comp=18.55** | **ISR 崩塌持续恶化 — 矛盾爆炸** |
| Convex combination | `plan005-sta-low-s42` | PR=77% (train), ISR=0.230 | ISR penalty 效应 |
| Downstream NLI | `plan014-downstream-nli-s42` | ρ=-0.049, not significant | ISR capability boundary (Limitation) |
| GT ISR baseline | `sta-gt-isr-baseline` | GT ISR=0.559, PR=18% | Ground truth 参照 |

---

## 5. 论文写作可立即启动的章节

以下章节的证据已完整：

1. **Introduction + Problem Statement** — plan001 3-seed 分化 + ISR 崩塌轨迹 (100/500/1000 步)
2. **Method (STA/ISR 定义)** — 纯方法论
3. **Results §4.1: ISR Diagnostic** (Claim 1) — ISR 崩塌轨迹完整，plan016 1000步确认
4. **Results §4.2: Goodhart Analysis** (Claim 2) — β=0.1/0.3 × ISR/random 全部齐全，3-seed H7 + random 对照
5. **Results §4.3: Hacking Taxonomy** — 6 modes (含 H7), strict 定义 D044, classify_h7.py 可复现
6. **Results §4.4: Cross-Logic** (Claim 3) — ⚠️ 初步可写: prolog-sta 100% H7 已出，等 prolog-exec 对照
7. **Discussion: ISR Capability Boundary** — plan014 negative result
8. **Related Work** — literature_map.yaml 33 refs

**暂缓**：
- §4.4 完整版 → 等 plan006-prolog-exec-s42 + 多 seed

---

## 6. 待完成实验

| 实验 | 状态 | 预期贡献 |
|------|------|---------|
| **plan009-sft-baseline-s42** | **PENDING (P1)** | **SFT baseline — 审稿人三档均指出缺此对比。区分 GRPO-specific hacking vs 通用微调 artifact。Qwen2.5-1.5B, 500步, cuda:1** |
| plan006-prolog-exec-s42 | ⏳ RUNNING (cuda:0) | Claim 3: Prolog exec-only baseline |
| plan018-random-b01-s43 | QUEUED (降优先级) | Claim 2: 多 seed random 对照 |
| plan018-random-b01-s44 | QUEUED (降优先级) | Claim 2: 多 seed random 对照 |
| plan006-prolog-exec-s43 | PREPARING | Claim 3: 多 seed |
| plan006-prolog-sta-s43 | PREPARING | Claim 3: 多 seed |
| plan006-prolog-exec-s44 | PREPARING | Claim 3: 多 seed |
| plan006-prolog-sta-s44 | PREPARING | Claim 3: 多 seed |

---

## 7. 行动建议（按优先级）

1. **[P1]** plan009 SFT baseline 审批通过后立即在 cuda:1 启动 — 审稿 gap
2. **[P1]** plan006-prolog-exec-s42 完成后立即 eval → Claim 3 exec vs ISR 对照
3. **[P2]** 追溯 plan001-s42 和 plan013 的 component count 来源，补入 registry
4. **[P2]** 修正所有引用 "s43 PR=13%" 的地方为 **14%**
5. **[P3]** plan018 random 多 seed（已被 SFT baseline 降优先级）
6. **[论文]** 开始写 §4.4 Cross-Logic 初稿（prolog-sta 数据已足够开篇）
