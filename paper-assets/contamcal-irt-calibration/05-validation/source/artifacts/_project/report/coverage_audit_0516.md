# 实验覆盖率审计 — 2026-05-16 (T-9 days to EMNLP ARR)

## 总览

| Claim | 角色 | 状态 | 关键缺口 |
|-------|------|------|----------|
| C1: Characterization | PRIMARY | 🟡 YELLOW | 3B 矩阵不完整；pooled IRT 未跑 |
| C2: Signal Failure | CO-PRIMARY | 🟡 YELLOW | 3B signals 不完整；跨 scale RRF 未聚合 |
| C3: Identifiability | Discussion | 🟢 GREEN | sim_sweep_v7 9/12 充分 |
| C4: Conditional Calibration | DEMOTED | 🟡 YELLOW | pooled fitting 仅 0.5B+1.5B ARC；无 baselines |

---

## Claim 1: Characterization (PRIMARY)

**论点**: 污染效应是 benchmark-dependent、scale-dependent、bidirectional。

### 已有 Evidence

| Evidence | 来源 | 关键 Metrics | 状态 |
|----------|------|-------------|------|
| γ_k 异质性 (ARC γ<0, GSM8K γ>0) | exp-006 pooled ARC/GSM8K | ARC γ=-2.347, GSM8K γ=0.187(n.s.) | ✅ |
| Benchmark sensitivity spectrum | exp-001 1.5B eval | GSM8K +34pp@d100, MMLU <0.5pp, ARC <0.3pp | ✅ |
| 0.5B catastrophic effects | exp-001 0.5B eval | ARC -17pp, HumanEval 变化大 | ✅ |
| 1.5B 完整矩阵 | exp-001 1.5B 16/16 cells | 双 seed × 4 dosage × 4 benchmark | ✅ |
| 1.5B cross-seed 一致性 | exp-001 s42 vs s123 | MC benchmarks <1.2pp variance | ✅ |
| Scale modulation (部分) | exp-001 各 scale | 0.5B catastrophic → 1.5B moderate | ✅ |
| Identifiability validation | exp-004 sim_sweep_v7 | γ_bias [-0.025,+0.056], θ_corr [0.947,0.972] | ✅ 9/12 |

### 缺口

| 缺口 | 级别 | 说明 | 预计耗时 |
|------|------|------|----------|
| **3B eval 矩阵** (当前 7/16) | 🔴 BLOCKING | scale-dependent 论证需要 3 个 scale 点；3B s42 4 cells 训练/eval 中 | 2-3 天 (GPU bound) |
| **Pooled IRT fitting (N≥16)** | 🔴 BLOCKING | 核心 γ_k 估计需要 pooled Bayesian IRT；当前仅 0.5B+1.5B ARC 跑过 | 0.5 天 (blocked on 3B) |
| 3B para_aligned eval | 🟡 NICE | 增加 N 和 robustness，非必需 | 1 天 |
| 7B 数据 | ⚪ SKIP | 可引用文献论证 scale trend，无自有 7B 数据 | N/A |

### Reviewer Concerns 覆盖

- **RC#22 (SFT≠contamination)**: ⚠️ 无 random-data SFT control。**缓解**: 聚焦 1.5B/3B 论述 (<2pp capacity effect)，0.5B 承认 combined effect。
- **RC#23 (N=8/16 vs N≥50 矛盾)**: ⚠️ sim_sweep 无 N=8 条件。**缓解**: 添加 N=8 simulation 条件（D096 rerun 可一并处理）。

---

## Claim 2: Signal Failure (CO-PRIMARY)

**论点**: Min-K++ 方向性反转，S1 唯一可靠，RRF fusion 提升 robustness。

### 已有 Evidence

| Evidence | 来源 | 关键 Metrics | 状态 |
|----------|------|-------------|------|
| Min-K++ directional reversal @0.5B | exp-002 0.5B signals | Cohen's d = -1.2 to -2.7 | ✅ |
| S1 embedding similarity AUC | exp-002 0.5B | AUC > 0.95 | ✅ |
| 0.5B RRF aggregation | exp-003 0.5B | degrades to S1-only | ✅ |
| 1.5B 全信号 (s1+s2+s4) | exp-002 1.5B | 12/12 PASS | ✅ |
| 3B s123 信号 (部分) | exp-002 3B v7 | 9 signal files, 3 merged | ✅ partial |
| 三信号 fusion 决策 (D098) | D098 | s1+s2+s4, 不含 s3_constat | ✅ declared |

### 缺口

| 缺口 | 级别 | 说明 | 预计耗时 |
|------|------|------|----------|
| **3B s42 信号计算** | 🔴 BLOCKING | 跨 scale 信号对比需要 3B 完整数据 | 1-2 天 (blocked on 3B eval) |
| **1.5B+3B RRF 聚合** | 🔴 BLOCKING | 验证 RRF 在大 scale 是否优于 S1-only | 0.5 天 (blocked on signals) |
| **跨 scale 信号对比表** | 🔴 BLOCKING | 论文核心 Table：signal AUC/Cohen's d × scale | 需 signals 完成后 ~2h |
| 0.5B+1.5B s123 信号补算 (D097) | 🟡 NICE | 增加 IRT pool N，提升 robustness | 进行中 |
| S2/S4 @1.5B/3B 有效性验证 | 🟡 NICE | RC#13 contingency — S2/S4 是否在大 scale 恢复 | signals 完成后可分析 |

### Reviewer Concerns 覆盖

- **RC#13 (RRF=S1?)**: ⚠️ 仅 0.5B 有完整 RRF 结果。1.5B/3B RRF 未聚合 → 无法确认 S2/S4 是否在大 scale 有效。**Critical**: 若 1.5B/3B 也退化为 S1-only → 需改写为 "scale-independent S1 dominance"。

---

## Claim 3: Identifiability → Discussion Honest Negative

**论点**: 4PL+γ 模型存在 misspecification (coverage collapse)；Fisher Info 建立 identifiability boundaries。

### 已有 Evidence

| Evidence | 来源 | 关键 Metrics | 状态 |
|----------|------|-------------|------|
| sim_sweep_v7 identifiability | exp-004 | 9/12 conditions, CI95 coverage [0.8,1.0] | ✅ |
| Coverage collapse @real data | exp-006 | 18-33% @95% nominal | ✅ |
| noise_prop_v4 negative result | exp-005 | CI insensitive to σ_e → model simplicity | ✅ |
| Fisher Info threshold derivation | exp-004 | structural AUC≥0.55, practical AUC≥0.70 | ✅ |
| CI width ∝ N^{-0.48} | exp-004 simulation | 3 sample sizes covered | ✅ |

### 缺口

| 缺口 | 级别 | 说明 | 预计耗时 |
|------|------|------|----------|
| sim_sweep auc0.65×3 补跑 (D096) | 🟡 NICE | 12/12 完整性；CmdStan TMPDIR 隔离修复 | ~2h |
| N=8 simulation 条件 | 🟡 NICE | 回应 RC#23 (N=8 vs N≥50 矛盾) | ~1h |

**结论**: 🟢 GREEN。降级为 Discussion 后，当前 evidence 充分。sim_sweep 9/12 + noise_prop negative + coverage collapse empirical 数据形成完整 honest negative 叙事。

---

## Claim 4: Conditional Calibration (DEMOTED)

**论点**: 污染增强 IRT 在 gating 条件下产生可用 point estimates，但 coverage 不可靠。

### 已有 Evidence

| Evidence | 来源 | 关键 Metrics | 状态 |
|----------|------|-------------|------|
| ARC pooled calibration | exp-006 pooled ARC | γ=-2.347, MAE=0.035, Coverage=62.5% | ✅ |
| GSM8K overcorrection (honest negative) | exp-006 pooled GSM8K | γ n.s., MAE 11× worse than raw | ✅ |
| Gating criterion 定义 | paper_framing | γ sig + PPP∈[0.1,0.9] + MAE<raw | ✅ defined |
| Oracle IRT fits | exp-006 oracle | ARC γ=-0.618, GSM8K γ=3.773 | ✅ |
| S1-only pipeline | exp-006 s1only | ARC MAE=0.035, GSM8K γ n.s. | ✅ |

### 缺口

| 缺口 | 级别 | 说明 | 预计耗时 |
|------|------|------|----------|
| **Full pooled IRT (1.5B+3B+0.5B)** | 🔴 BLOCKING | 当前 pooled 仅 0.5B+1.5B N=8；需 3B 数据 | blocked on 3B |
| **≥1 baseline 对比** | 🔴 BLOCKING | 论文必须有 baseline；reviewer 一定会问 | 0.5 天 |
| MMLU/HumanEval IRT fitting | 🟡 NICE | 扩展 benchmark 覆盖 | 0.5 天 |
| SBC diagnostic | 🟡 NICE | 贡献列表里提到但未跑 | 0.5 天 |
| 7 baselines 全集 | 🟡 NICE | 完整对比更强但非必需 | 1 天 |
| Gating criterion empirical validation | 🟡 NICE | 验证 gating 在 held-out 上有效 | 0.5 天 |

### Reviewer Concerns 覆盖

- **RC#19 (coverage collapse)**: ✅ 已有 honest framing + sim_sweep 支撑。
- **RC#20 (GSM8K overcorrection)**: ✅ 已有 gating criterion design。但 gating 未 empirically validated。

---

## Blocking 缺口汇总 (必须 T-9 内完成)

按关键路径排序：

| # | 缺口 | 影响 Claims | 依赖 | 预计完成 |
|---|------|------------|------|---------|
| 1 | **3B s42 eval 完成** (d000/d005/d025/d100 aligned) | C1, C2, C4 | GPU: 3 jobs 进行中, d000 仅需 eval | T-7 (May 18) |
| 2 | **3B signals 计算** (s42 完整 s1+s2+s4) | C2 | 依赖 #1 | T-6 (May 19) |
| 3 | **跨 scale 信号对比表** | C2 | 依赖 #2 | T-6 (May 19) |
| 4 | **1.5B + 3B RRF 聚合** | C2 | 依赖 #2 | T-6 (May 19) |
| 5 | **Pooled IRT fitting** (≥3 scales, per-benchmark γ_k) | C1, C4 | 依赖 #1 (至少 aligned) | T-5 (May 20) |
| 6 | **≥1 baseline 对比** (raw score, naive decontamination) | C4 | 依赖 #5 | T-5 (May 20) |

**关键路径**: 3B s42 eval → 3B signals → RRF + signal table → pooled IRT → baselines → paper draft

**最早可开始写 paper**: T-5 (May 20)，假设 3B aligned 在 T-7 完成。

---

## Nice-to-Have 列表 (时间够就做)

按 ROI 降序：

| # | 任务 | 影响 | 预计耗时 | 优先级理由 |
|---|------|------|---------|-----------|
| 1 | sim_sweep N=8 条件 | RC#23 defense | 1h | 直接回应内部矛盾 |
| 2 | sim_sweep auc0.65×3 补跑 | 完整性 | 2h | 12/12 比 9/12 更好 |
| 3 | SBC diagnostic | 贡献列表 | 4h | 提到但未实现 |
| 4 | MMLU/HumanEval IRT fitting | C4 扩展 | 4h | 增加 benchmark 覆盖 |
| 5 | 3B para_aligned eval | IRT pool N | 1 天 | N=23→31 |
| 6 | S2/S4 scale recovery 分析 | RC#13 defense | 2h | signals 完成后可做 |
| 7 | Additional baselines (5-7 total) | C4 strength | 1 天 | 1个够，7个更好 |
| 8 | Random-data SFT control @0.5B | RC#22 defense | 0.5 天 | 回应 capacity artifact |
| 9 | Gating criterion held-out validation | C4 robustness | 4h | 当前仅 design 无 validation |

---

## 风险评估

### 高风险
- **3B s42 GPU 瓶颈**: 4 个 cell 依赖 GPU 释放。若 d005/d100 SFT 延期 → 整条关键路径后移。**缓解**: 仅用 3B s123 (4 cells) 也可勉强支撑 scale 论点，N 从 23 降到 ~19。
- **RRF @1.5B/3B 仍退化为 S1-only**: 若跨 scale S2/S4 均无效 → Claim 2 需重写 fusion 叙事为 "S1 scale-robust dominance"。论点仍成立但弱于 "fusion improves"。

### 中风险
- **Pooled IRT GSM8K 不收敛**: 0.5B+1.5B 已 negative (γ n.s.)。加 3B 后可能仍不显著 → GSM8K γ 证据仅来自 oracle fit。**缓解**: 论文框架已包含 gating criterion，GSM8K 不 calibrate 是合理结论。
- **N < 20 for pooled fitting**: 若 3B 仅贡献 4 cells → pooled N=20 (excl 0.5B)。论文自己的 N≥50 标准下这仍不足。**缓解**: sim_sweep 跑 N=20 条件验证 bias/coverage 可接受。

### 低风险
- **Claim 3 reviewer pushback**: 已降级为 Discussion，sim_sweep 9/12 充分。
- **s4_selfcritique OOM**: D091/D093 已降级 P1，s1+s2 足够。

---

## 建议优先级排序 (Day-by-Day)

### T-9 ~ T-7 (May 16-18): GPU 密集阶段
- 继续 3B s42 SFT/eval (d005, d025, d100)
- d000_s42 eval 启动（已训练完成）
- 0.5B+1.5B s123 信号补算完成 (D097)

### T-7 ~ T-5 (May 18-20): 信号 + IRT
- 3B signals 计算 (s42 + s123 缺失部分)
- 跨 scale 信号对比表生成
- 1.5B + 3B RRF 聚合
- Pooled IRT fitting (per-benchmark γ_k)
- sim_sweep N=8 条件 + auc0.65 补跑

### T-5 ~ T-3 (May 20-22): Analysis + Baselines
- ≥1 baseline 对比实现
- Gating criterion 结果汇总
- Paper draft 开始 (5-step pipeline)

### T-3 ~ T-0 (May 22-25): Paper Finalization
- Paper writing + iteration
- Figure 生成
- Review + polish
- Submission

---

## 结论

**总体评估**: 🟡 YELLOW — 核心框架和大部分数据就绪，但 3B 矩阵不完整 + pooled IRT 未跑构成两个 hard blockers。Claim 3 (Discussion) 已 GREEN。关键路径压力集中在 T-9 到 T-5 的 GPU 资源分配上。

**最坏情况兜底**: 若 3B s42 无法全部完成，可仅用 3B s123 (4 cells) + 1.5B 完整矩阵 (16 cells) 支撑论文。N=20 (excl 0.5B) 或 N=32 (incl 0.5B，GSM8K/HumanEval only)。论点成立但统计 power 弱于目标。
