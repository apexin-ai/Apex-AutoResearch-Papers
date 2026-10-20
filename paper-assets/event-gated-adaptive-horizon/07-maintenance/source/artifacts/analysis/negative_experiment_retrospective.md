# Negative Experiment Retrospective

**Date**: 2026-05-17
**Purpose**: Manager 要求复盘所有 negative 实验，检查是否有被遗漏的方法改进线索。

---

## 逐实验复盘

### Line 1: Learned Gate (003→004→005)

#### exp_003_event_gated_v2
- **证伪说明了什么**: imagination 中 gate 输出 dt∈{1,...,8} 无约束，而 RSSM 只在 subsample curriculum 限定的 dt 上训练过。对未见大 dt 的预测是噪声 → progressive poisoning。
- **当时怎么处理**: 修复 dt clipping + logits masking，进入 v3 (004)。
- **回头看对不对**: 正确。这是明确的实现 bug，不是方法问题。
- **Parent**: exp_001_baseline (implicit)

#### exp_004_event_gated_v3
- **证伪说明了什么**: gate_loss 爆炸 — compute_gate_targets 用 gate_max_dt=8 但 logits masking 用 effective_max_dt，cross-entropy ~3e8。
- **当时怎么处理**: 统一 effective_max_dt 为唯一 dt 来源，进入 v4 (005)。
- **回头看对不对**: 正确。又一个实现 bug。
- **Parent**: exp_003_event_gated_v2

#### exp_005_event_gated_v4 ⭐ (Director 重点关注)
- **证伪说明了什么**: 3 轮 bug 修复后，gate 机制本身 PASS（entropy/H_eff/structure 全达标），但 hard categorical gate + variable-rate imagination 与 actor-critic 优化存在**结构性冲突**。gate_scale>0.5 后 return 不可恢复地下降（541→99）。
- **当时怎么处理**: 放弃 "learned gate" 整条线。转向诊断 CIVO 现象。
- **回头看对不对**: **值得重新审视。** 005 的问题链是：learned gate → variable dt imagination → RSSM 对高 dt 预测不准 → value overestimation → collapse。但 005 用的是 **trained dt_emb**。根据后续发现（C2: trained dt_emb 是 CIVO 必要条件），如果用 **untrained dt_emb (dim=0) + learned gate**，gate 仍可选择 dt，但不会触发 CIVO。这个组合**从未测试过**。
- **Parent**: exp_004_event_gated_v3 → 补为 exp_001_baseline

**遗漏线索**: untrained dt_emb + learned gate 是未探索的方法变体。008f 证明 dim=0 消除 CIVO；005 证明 gate 本身能学到有意义的 dt pattern。两者组合可能同时获得 adaptive horizon 的好处和 CIVO safety。

---

### Line 2: Fixed-dt Diagnostics (006→007)

#### exp_006_fixed_dt2
- **证伪说明了什么**: fixed dt=2（无 learned gate）也崩了。这排除了 "gate 学习机制是问题根源" 的假设。问题在 dt=2 **imagination** 本身（RSSM 在 dt=2 上预测不准 → value 过估 → collapse）。这就是后来命名为 CIVO 的现象。
- **当时怎么处理**: 这个 negative 实际上是**关键发现** — 它把问题定位从 "gate 坏了" 缩窄到 "dt>1 imagination 有毒"。启动 008 系列消融。
- **回头看对不对**: 完全正确。006 是项目转折点，从 "做方法" 转向 "理解失败"。
- **Parent**: exp_005_event_gated_v4

#### exp_007_fixed_dt4
- **证伪说明了什么**: dt=4 太粗（action temporal resolution 不足），不是 CIVO 而是简单的 under-learning。Value 被抑制（v/e 6-13%），与 dt=2 的 over-estimation 完全相反。
- **当时怎么处理**: 确定 dt sweet spot ∈ {1,2}，后续只测 dt=2。
- **回头看对不对**: 正确。dt=4 的失败模式不同，不提供 CIVO 诊断信息。
- **Parent**: exp_006_fixed_dt2

---

### Line 3: Subsample/Horizon (008c)

#### exp_008c_no_subsample_dt2_h8
- **证伪说明了什么**: subsample OFF + dt=2 imagination + H=8 → plateau at 60% baseline（无 collapse，但学习极慢）。与 008a (H=15, 也无 collapse 但 NVE 低) 对比 → H=8 和 H=15 在 subsample OFF 时都不崩，说明 subsample ON (mixed dt training data) 是 CIVO 的关键 co-factor。
- **当时怎么处理**: 结论纳入 2×2 消融矩阵，锁定 "trained dt_emb + subsample ON" 为 CIVO 必要条件组合。
- **回头看对不对**: 正确，但有遗漏。008c 虽然不崩但性能差（60% baseline），说明 subsample OFF + dt=2 imagination 也不是好方案。这个 negative 暗示：**如果想用 dt>1 imagination，必须找到一种不触发 CIVO 的 dt_emb 方案**（后来 008f dim=0 做到了 85% baseline）。
- **Parent**: exp_008d_subsample_on_h8 → 应为 exp_006_fixed_dt2（都是 dt=2 imagination 系列）

---

### Line 4: Multi-seed Replication (009b, 009c, 009e)

#### exp_009b_008d_walker_s2
- **证伪说明了什么**: CIVO onset (NVE=2.05×) 在 seed=2 上复现，但没有 collapse（self-correction）。证伪了 "CIVO 必然导致 collapse" 的强假设，建立了 "CIVO onset is deterministic, collapse is stochastic" 的核心洞察。
- **当时怎么处理**: 修正叙事 — collapse rate stochastic, NVE diagnostic universal。
- **回头看对不对**: 完全正确。这个 negative 比一个 success 更有价值 — 它精确揭示了 CIVO 的概率性质。
- **Parent**: exp_008d_subsample_on_h8 ✓

#### exp_009c_008f_walker_s2
- **证伪说明了什么**: dt_embed_dim=0 seed=2 在 75K 后持续下降（359→148），不复现 008f seed=1 的 zigzag 恢复（→503）。说明 no_dt_emb 方案的性能有 seed 依赖性，不如 seed=1 暗示的那么好。
- **当时怎么处理**: 接受 cross-seed 不一致，但保留 C2 结论（NVE<1.5× universal 跨 seed）。
- **回头看对不对**: 部分正确。NVE 指标确实 universal (<1.5×)，但 **performance level** 有 seed 依赖。论文报告 008f 系列时应该用 multi-seed mean 而非 cherry-pick seed=1。实际上，seed=2 的 148@105K (15% baseline) 比 trained dt_emb 还差 — 这暗示 **no_dt_emb 方案在某些 seed 上 performance 很差，作为方法贡献需要谨慎 claim**。
- **Parent**: exp_008f_no_dt_embed_subsample_on_h8 ✓

#### exp_009e_008d_walker_s1
- **证伪说明了什么**: 名义上是 seed=1 复现 008d，实际上因为 009e 与 008d 共享 seed=1，不是独立观测。后来发现配置可能有问题（D071）。
- **当时怎么处理**: 不计入独立样本，启动 008d_civo_trigger_s3 (seed=3) 作为第三独立 seed。
- **回头看对不对**: 正确。重复 seed 无统计意义。
- **Parent**: exp_008d_subsample_on_h8 ✓

---

### Line 5: Frozen dt_emb (015b)

#### exp_015b_frozen_dt_emb
- **证伪说明了什么**: Frozen（存在但不训练）dt_emb → gradient starvation（actor_loss→0），不是 CIVO。NVE 短暂升到 1.45× 然后自修正。说明 CIVO 需要 dt_emb **actively training**（不断学习 dt-specific representations），仅存在不够。
- **当时怎么处理**: 纳入 2×2 矩阵结论：trained=CIVO, frozen=gradient starvation, dim=0=safe。
- **回头看对不对**: 正确。精确隔离了 "训练" vs "存在" 的因果效应。
- **Parent**: exp_008d_subsample_on_h8 ✓

---

### Line 6: SGS Interventions (016e→018v2→018_s2)

#### exp_016e_sgs_walker_s1
- **证伪说明了什么**: Reward-only SGS (detach dt_emb in reward head) 是 architectural no-op — reward gradient 通过 reward head 本身就不经 dt_emb（梯度分解确认 reward gradient to dt_emb ≈ 0）。016e 与 008d 的差异（onset timing）纯属 cross-seed variation。
- **当时怎么处理**: 撤回 "SGS delays collapse" 解读。确认 reward pathway 不是 CIVO 根因。
- **回头看对不对**: 正确。016e 的真正贡献是揭示梯度结构（reward ≠ 通向 dt_emb 的通路），缩小 viable intervention 搜索空间。
- **Parent**: exp_008d_subsample_on_h8 ✓

#### exp_018v2_full_sgs_walker_s1 ⭐ (Director 重点关注)
- **证伪说明了什么**: Full-SGS (detach ALL decoder gradients from dt_emb) seed=1 — NVE peak=1.66× (CIVO onset), 但 105K 时未完全 collapse (eval=448, 46% baseline)。Late collapse detected @112K。CIVO reduction 79% vs 008d 但未完全消除。
- **当时怎么处理**: 与 018_s2 合并判断为 "SGS 不可靠" (collapse_rate=0.5)。结论：CIVO 是 representation-level，切梯度不够。
- **回头看对不对**: **诊断可能不够深。** 考虑：
  1. 018v2 的 NVE=1.66× 远低于 008d 的 4.12×（79% reduction）— SGS **确实大幅抑制了 CIVO**
  2. 018v2 eval=448 vs 008d eval=83 — SGS 使 performance 从 8.6% 恢复到 46% baseline
  3. Collapse 在 112K 才开始（vs 008d 的 60K），晚了 52K 步
  4. **可能的解释**: SGS 消除了 gradient-mediated CIVO（主通路），但 representation-level co-adaptation 仍通过 KL loss 的 implicit gradient 绕路。如果我们同时 freeze dt_emb + SGS，可能完全消除？但 015b 证明 freeze 导致 gradient starvation...
  5. **更可能的解释**: dt_emb 通过 world model 的 shared encoder 间接影响 value function，即使 decoder 梯度被切。World model 训练时 dt_emb concatenated 到 state，这本身改变了 latent space geometry。
- **Parent**: exp_008d_subsample_on_h8 ✓

#### exp_018_full_sgs_s2
- **证伪说明了什么**: Full-SGS seed=2 完全 collapse (eval=40.8@105K)。与 018v2 seed=1 (eval=448) 形成鲜明对比 → SGS 的保护效果 seed-dependent。
- **当时怎么处理**: 确认 SGS 不可作为可靠 intervention。降级为 informative negative。
- **回头看对不对**: 正确决策。但没有深挖**为什么 seed=2 崩而 seed=1 不崩**。可能原因：seed=2 的 replay buffer sampling sequence 恰好在早期产生更多 dt=2 transitions，加速 dt_emb representation specialization，overwhelm SGS 的保护。
- **Parent**: exp_018v2_full_sgs_walker_s1 ✓

---

### Line 7: Pathway B (008e_v3_s2)

#### exp_008e_v3_walker_s2
- **证伪说明了什么**: trained dt_emb + subsample ON + **dt=1 imagination** + H=15 seed=2 也崩溃了（715→137@105K）。这证伪了 C6 原假设 "dt=1 imagination prevents collapse"。崩溃机制是 Pathway B (Imagination-Reality Divergence)，不是 CIVO。
- **当时怎么处理**: 识别为第二种崩溃机制（Pathway B），与 CIVO (Pathway A) 分离。用 exp_020 matched-seed 控制确认 trained dt_emb 是 Pathway B 的必要条件。
- **回头看对不对**: 完全正确。这个 negative 导致发现第二种失败模式，丰富了论文故事。
- **Parent**: exp_008e_v3_subsample_on_dt1_h15 ✓

---

## 被遗漏的方法改进线索

### 线索 1: untrained dt_emb + learned gate（高优先级）

**推理链**:
- 005 证明 learned gate 能产生有意义的 dt pattern (entropy/structure PASS)
- 005 失败因为 trained dt_emb → CIVO
- 008f 证明 dt_embed_dim=0 消除 CIVO，但牺牲了所有 dt-conditioning 信息
- **未测试**: dt_embed_dim=0 (或 untrained/fixed embedding) + learned Gumbel gate

**预期**: Gate 根据 state 选择 dt（保留 adaptive horizon 能力），但 world model 不通过 trained embedding 学习 dt-specific representations（避免 CIVO）。Gate 的 decision 直接用于 subsample step selection，而非通过 embedding 间接影响 RSSM。

**风险**: 无 dt embedding 时，RSSM 无法区分 dt=1 和 dt=2 transitions → gate 选择的 dt>1 imagination 步骤可能仍然不准。但 008f 已证明这种配置至少达到 85% baseline（seed=1）。

**实验设计**: 与 005 相同配置，仅 `--gate_dt_embed_dim 0`（如果参数存在）或等价实现。

### 线索 2: 008f 作为方法贡献（需谨慎）

**现状**: 008f (no dt_emb, subsample ON) seed=1 达到 503@105K (52% baseline)，是所有 dt>1 配置中最高的。
**但**: seed=2 (009c) 只有 148@105K (15% baseline)，seed=3 (008f_s3) 结论=success 但具体数字需确认。

**评估**: 如果 multi-seed mean 显著高于 trained dt_emb 的 21.3% (C1)，则 "remove trained dt_emb" 确实是一个 practical mitigation — 不是 intervention（不修复 CIVO），而是 avoidance（不触发 CIVO）。

**论文定位**: 与 detector 互补 — detector 检测 CIVO onset，dim=0 是 preventive architecture choice。

### 线索 3: SGS + 更短训练

018v2 在 105K 时 eval=448 (46% baseline)，到 112K 才开始 late collapse。如果训练到 80K 停止（by detector trigger），SGS 可能在 "检测窗口内" 是有效的 — 即 SGS 将 CIVO onset 延迟足够久让 detector 有时间触发。这可以作为 "detector + SGS 联合方案" 的 story，但需要更多数据支撑。

---

## 推导链修正

| exp_id | 当前 parent | 修正 parent | 原因 |
|--------|-----------|-----------|------|
| exp_005_event_gated_v4 | exp_001_baseline | **exp_004_event_gated_v3** | 005 是 004 修复后的重试 |
| exp_004_event_gated_v3 | (无) | **exp_003_event_gated_v2** | 004 是 003 bug fix 后的重试 |
| exp_003_event_gated_v2 | (无) | **exp_001_baseline** | 首个 gate 实验基于 baseline |
| exp_008c_no_subsample_dt2_h8 | (无) | **exp_006_fixed_dt2** | 008c 是 006 的 subsample OFF 对照 |
| exp_007_fixed_dt4 | (无) | **exp_006_fixed_dt2** | 007 是 006 的 dt=4 对照 |
| exp_006_fixed_dt2 | exp_005_event_gated_v4 | ✓ 已正确 | — |

---

## 总结

### 方法贡献候选（按优先级）
1. **CIVO Online Detector** — 当前主线，进行中
2. **Architecture Avoidance (dim=0)** — 已有数据但 multi-seed 不一致，需更多 seed
3. **Adaptive dt without trained embedding** — 未测试，最有方法新颖性但需新实验

### 被正确关闭的线
- Learned Gumbel gate + trained dt_emb → 结构性 CIVO，正确关闭
- dt=4 → 太粗，无 CIVO 但性能差，正确关闭
- Reward-only SGS → architectural no-op，正确关闭
- Full-SGS as reliable intervention → collapse_rate=0.5，正确降级

### 诊断不够深的
- **018v2 vs 018_s2 的 seed 差异**：为什么 seed=1 延迟 52K 步而 seed=2 正常速度 collapse？未深挖 replay buffer 中 dt>1 transition 的分布差异。
- **009c 的 performance decline**：no_dt_emb seed=2 为什么在 75K 后持续下降？这是否暗示 subsample ON 本身（非 dt_emb）也有 subtle 负面效应？
