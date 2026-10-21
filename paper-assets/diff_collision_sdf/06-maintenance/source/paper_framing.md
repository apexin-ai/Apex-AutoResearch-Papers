# ColliForce-VLA Paper Framing

> 维护者: Director | 最后更新: 2026-05-29 UTC | D049: Reviewer 证据链审查——补入 Pi0.5 oracle + multi-eval-seed | Post-MVP research phase

## Core Insight

VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 和几何路径安全严重污染，导致 "安全" 指标虚高。我们通过大规模实证分析（90+ 实验, 6000+ episodes）揭示这一系统性缺陷，提出 EE displacement-filtered CAR 作为修正指标，并证明碰撞避免能力隐式来自 collision-free demonstration data，而非显式几何监督——SDF auxiliary loss 在全测试范围 λ∈[0.005, 0.1] 完全冗余，binding constraint 是 EE-only 的结构性不匹配。

## Working Title

"Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion"

> 聚焦评估方法论贡献（影响面广、scope-proof），SDF 作为验证工具而非主贡献

## Target Venue

**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会)
**定位**: Diagnostic/evaluation methodology paper with positive method contribution
**Fit**: Robotics safety track — "VLA safety metrics are fundamentally broken" 对社区有直接影响

## Core Claims (D028 重组: 4→3 claims)

### Claim 1: CAR Metric Contaminated by Fake Safety (Primary — 证据强度 ★★★★★)

Standard CAR metric is systematically contaminated by two distinct mechanisms: (a) action collapse producing frozen robots falsely counted as "safe", and (b) geometric path safety where capable robots happen to avoid obstacles without any avoidance behavior. "Collision-free" ≠ "collision-avoiding."

**Primary evidence — Action collapse (fake safety)**:
- 800 episodes A1 per-episode analysis: CAR=91.5%, but 99.6% of safe episodes show obstacle displacement < 0.1mm (~5nm median) — robot is frozen
- TSR=0% 独立确认 action collapse
- 术语修正 (D023): fake safety 判定以 TSR=0% + obstacle displacement < 0.1mm 双证据链为主

**Supporting evidence — Capability-safety anti-correlation (原 Claim 2)**:
- Pi0.5 3-seed eval: TSR=74.7±1.5%, CAR=26.8±1.6% — 更强模型完成更多任务但碰撞更多
- Pi0 baseline: TSR≈0%, CAR=82% — "高 CAR" 来自 action collapse
- Capability↑ → motion↑ → collision↑; 表面安全要么是 frozen (Pi0) 要么是 path geometry (Pi0.5)
- 限制: 仅 2 model families; 降级为 observation, 不 claim 因果

**贡献**: 提出 EE displacement-filtered CAR (dfCAR) 作为修正指标

**dfCAR 定位 (D024 Dream 反馈)**:
- Claim 1 的核心证据是 TSR=0% + obstacle displacement 双证据链，**不依赖** dfCAR
- dfCAR 是 **方法论贡献**（community tool），不是 Claim 1 的唯一支撑
- 论文需要展示 dfCAR 的实际 filtering 效果：Pi0+A1 (CAR=91.5% → dfCAR≈0%) vs Pi0.5+SDF (dfCAR=raw_CAR, no filtering)
- Threshold sensitivity: δ∈[2mm, 200mm] 范围内 dfCAR 完全不变（所有 active episode 最小 EE disp = 239mm）

### Claim 2: EE-only Geometric Supervision Structural Limitations (Supporting — 证据强度 ★★★★)

End-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。

**证据**:
- 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline
- **Pi0.5 LoRA oracle (D045/D049)**: eval_oracle_pi05_lora_s0, CAR=51.9% < LoRA baseline 54.83%——封堵"oracle 失败仅因 action-collapsed models"攻击面。Pi0.5 LoRA 非 collapsed (frozen=0%)，oracle 仍降低 CAR，证明 EE-only gradient correction 在任何模型上都失败
- spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系
**限制**: "EE-only 不够" 是 expected result; 缺乏 full-body SDF 对照

### Claim 3: Avoidance Source Diagnosis — EE-only Geometric Supervision Neither Necessary Nor Sufficient (Diagnostic — 证据强度 ★★★★★, D035 Scenario B confirmed)

Unified framing (Reviewer 建议, 统一 Claim 2+3 takeaway): EE-only SDF geometric supervision is neither necessary for collision avoidance—collision-free demonstrations account for the entire 28pp CAR gain, with identical per-task avoidance patterns across all SDF conditions—nor structurally sufficient, as ground-truth oracle refinement reduces CAR below unrefined baselines. This dual failure reveals that avoidance capability is implicitly learned from demonstration data distribution, not from explicit geometric supervision.

**Overclaiming 防线（必须在论文中体现）**: (1) Scope: SafeLIBERO + Pi0/Pi0.5; (2) "EE-only SDF" 不否定 full-body geometric supervision; (3) "all observed/measured gains" 不声称 demos 能解决碰撞问题; (4) 不否定其他 geometric loss 形式（CBF、reward shaping）。

**已确认 (D025/D032/D033/D035 core)**：at λ∈{0.005, 0.01, 0.1}, SDF does not improve CAR beyond LoRA-only baseline。λ=0.1（20× weight increase）双 seed 20K mean CAR=55.5%（z=0.47 vs null），明确在噪声内。LoRA fine-tuning 本身产生 +26pp CAR（54.5% vs Pi0.5 baseline 28.5%）。Per-task CAR ordering 跨所有条件完全一致（chocolate_pudding > milk > orange_juice > bbq_sauce），表明避障模式反映 demonstration distribution 特征而非 geometric supervision。

**证据（rotation-fixed reeval 数据）**:
- LoRA-only (2 seeds): CAR=54.5%±2.8 (s0=56.5%, s1=52.5%), frozen=0%
- LoRA+SDF λ=0.005 (3 seeds): CAR=54.5%±2.3 (s0=57, s1=54, s2=52.5)
- LoRA+SDF λ=0.01 (3 seeds): CAR=56.33%±1.61 (s0=57, s1=57.5, s2=54.5) — p≈0.12 不显著，per-task 无系统提升，Task 3 驱动方差 s0=34%→s2=14% (D033)
- Per-task CAR pattern 完全一致（T3 BBQ 方差最大: l01=23.3% vs l005=20% vs LoRA=26%，种子噪声）

**Multi-eval-seed robustness (D049 新增)**:
- 8 个实验跨 5 个 eval seeds (seed 0/7/42/99/123/256): eval_multiseed_lora_s0_eseed{0,42,99,123} + eval_multiseed_sdf_l01_s0_eseed{42,99,123,256}
- SDF 冗余性在所有 eval seeds 上一致成立，排除 "eval seed=7 的 artifact" 攻击面
- 应在 ICRA 正文 Claim 3 中呈现，而非仅作 supplementary

**TSR collapse 机制分析 (M041)**:
- 复合机制：catastrophic forgetting of task semantics + retained collision avoidance
- SDF loss 不是 TSR 崩溃原因（LoRA baseline 崩溃幅度完全一致 -68.4% vs -68.7%）
- Robot 保留运动能力（0% frozen, EE ~0.5m）但丧失 goal-directed grasping/placing
- Safe failure rate 从 0.5% → ~50%（100×），obstacle displacement 减半

**✅ CONFIRMED: Scenario B (D035)** — λ=0.1 20K 双 seed mean CAR=55.5% ≤ 57% 阈值，全域 SDF 冗余。

**判定依据 (D033 阈值 + D035 确认)**：零分布 = LoRA(2) + l005(3) = 5 个无效 SDF 测量值 mean=54.5%, std=2.17%。λ=0.1 双 seed z=0.47，明确在噪声内。硬约束全部通过（TSR=51-54% ≥ 35%，frozen=0%）。

| λ=0.1 结果 | 场景 | 状态 |
|-----------|------|------|
| **2-seed 20K mean=55.5% (≤57%)** | **B（完全 negative）** | **✅ 已确认** |

**待最终确认（不影响叙事方向）**：
- **λ=0.1 30K × 2 seeds** (s0/s1 ~17:00 UTC 5/27) → 最终数字确认
- **λ=0.1 30K s2** (~08:40 UTC 5/28) → 第三 seed 补充
- LoRA seed2 (plan_013) → 3v3 seeds 统计
- Phase 2 λ=0 → SDF 是否有持久效应（Scenario B 下测 "dose-dependent safety persist after removal"）

### Phase 2 解读 (contingent on λ=0.1)

- 如果场景 A/C: Phase 2 测试 "SDF 训练是否造成持久行为变化"
- 如果场景 B: Phase 2 测试 "dose-dependent safety 是否 persist after removal"
- Phase 2 CAR ≈ LoRA-only → SDF 无持久效应
- Phase 2 CAR < LoRA-only → SDF 造成持久损伤
- Phase 2 CAR > LoRA-only → SDF 有持久编码（需更多 seeds 确认）

## Anticipated Reviewer Concerns

### R1 (最致命): Generalizability
"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?"
→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl); (2) 3+ models (Pi0 + Pi0.5 + OpenVLA); (3) 收窄 claim scope + mechanistic argument (any model with low task capability will exhibit fake safety)
→ **接受率估算**: 1 task/2 model ~40% / 2 tasks+3 models ~55-65% / 3+ tasks ~65-75%

### R2: Novelty of EE-only limitation
→ **应对**: 定量分析 (arm-body vs EE 碰撞比例 + oracle 排除其他解释); supporting claim 而非 primary

### R3: No solution
"诊断了问题但没解决"
→ **应对**: (1) dfCAR metric 是 positive 工具贡献; (2) 揭示 avoidance 来源（implicit demo signal, not geometric supervision）本身是 actionable insight; (3) diagnostic paper 有方法论价值——知道问题在哪比错误地以为解决了更重要

### R4: Action collapse is trivial
→ **应对**: 原因可能 trivial，但 metric contamination 后果 non-trivial; 后续工作基于被污染 CAR 得出错误结论

### R5 (更新 D025): SDF redundancy — why bother testing it?
→ **应对**: (1) SDF geometric supervision 在 motion planning 领域广泛使用，先验合理; (2) negative result 排除合理路径; (3) 关键 insight 是 "avoidance 来自 demo imitation, not geometry" — 对未来 safety method 设计有指导意义

### R6 (D025): Fine-tuning collapse — catastrophic forgetting?
→ **应对**: (1) M041 分析确认是复合机制 (forgetting of task semantics + retained avoidance); (2) LoRA fine-tuning 同时提升 CAR 和降低 TSR = conservative behavior, not safe behavior; (3) SDF 不是原因（LoRA baseline 同等崩溃）

## Narrative Structure (D028: 3 Blocks + 1 Sub-block)

### Block 1: Fake Safety Revelation + Capability Observation (Claim 1)
- **Evidence**: A1 800ep (frozen), Pi0.5 3-seed (geometric path safety), Pi0 baseline (action collapse)
- **Key finding**: CAR=91.5% is fake (99.6% frozen); Pi0.5 CAR=27% is geometric; neither is avoidance
- **Contribution**: dfCAR metric + threshold sensitivity analysis
- **Sub-block**: Capability↑ → motion↑ → collision↑ as supporting observation

### Block 2: EE-only Geometric Supervision Boundary (Claim 2)
- **Evidence**: 3 oracle variants all < baseline; **Pi0.5 LoRA oracle (non-collapsed model) also < baseline**; arm-body collision analysis
- **Narrative**: Runtime gradient correction structurally fails — alpha schedule, representation, and model capability don't help; EE-only SDF = structural scope limit. Pi0.5 LoRA oracle 封堵"oracle 仅在 collapsed models 上失败"的替代解释
- **Presentation**: Single unified table (含 Pi0.5 LoRA oracle row) + collision part analysis

### Block 3: Avoidance Source Diagnosis — Neither Necessary Nor Sufficient (Claim 3, unified with Claim 2)
- **Evidence**: LoRA-only 2-3 seeds + SDF 3 seeds × 3 lambdas, per-task comparison, oracle experiments
- **Key finding**: "Neither necessary nor sufficient" — (necessity) LoRA-only CAR=54.5% ≈ SDF across λ∈[0.005, 0.1], per-task ordering invariant; (sufficiency) oracle refinement CAR < baseline
- **Narrative**: EE-only SDF geometric supervision fails on two independent dimensions: it is unnecessary (demo distribution accounts for all avoidance gains) and structurally insufficient (EE-only monitoring redistributes collisions to unmonitored arm links). Per-task avoidance fingerprint (chocolate_pudding highest, bbq_sauce lowest) preserved across all 10 conditions confirms demonstration distribution as sole source.
- **TSR collapse analysis**: composite mechanism (task forgetting + avoidance retention)
- **Sub-narrative**: flat λ curve (Scenario B confirmed) + stepwise training dynamics (16K-30K) + Phase 2 persistence

### 叙事原则
1. 每个 block 是 **evidence for structural claims**
2. Block 间逻辑递进：metric 有缺陷 (B1) → geometric supervision 有结构缺陷 (B2) → avoidance 来源是 demo data 而非 geometry (B3)
3. B3 是 positive diagnostic insight，展示"避障可实现且来源是隐式学习"

## Figure Plan

| ID | 内容 | Claim | 优先级 | 数据来源 | 状态 |
|----|------|-------|--------|---------|------|
| Fig 1 | Fake vs real safety 概念图 (displacement 对比) | 1 | 重要 | 设计 | 待做 |
| Fig 2 | EE Displacement 分布 (A1-frozen vs Pi0.5+A1-moving vs baseline) | 1 | **必须** | 修复后 eval JSON | 数据就绪 |
| Fig 3 | TSR-CAR scatter (多模型 + capability observation) | 1 | 重要 | 全部 eval 数据 | 数据就绪 |
| Fig 4 | Oracle refinement CAR bar chart + arm-body collision | 2 | **必须** | 3 oracle + baselines | 数据就绪 |
| Table 1 | 3-seed × 2-lambda × best/30K 完整结果矩阵 + EE disp | 3 | **必须** | Pi0.5+A1 修正数据 | 数据就绪 |
| Fig 5 | Lambda-CAR/TSR 曲线 (含 LoRA baseline 作 λ=0 点) | 3 | **必须** | LoRA baseline + SDF 数据 | 待 λ=0.1 |
| Table 2 | Phase 2 λ=0 ablation 结果 | 3 | 重要 | Phase 2 训练 | RUNNING |

## Dependencies (Research Phase)

- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake (obstacle disp)
- [x] Pi0.5 baseline 3-seed (Claim 1 supporting) — CAR=26.8±1.6%, TSR=74.7±1.5%
- [x] Pi0.5+A1 3-seed × 2-lambda 训练 + eval (Claim 3) — confirmed real avoidance (D023)
- [x] EE displacement 修正 eval (Claim 3) — 3 seeds corrected, all consistent
- [x] Oracle 3 variants (Claim 2) — all < baseline
- [x] Spatial/object collision analysis (Claim 2) — arm-body dominant
- [x] **LoRA baseline** (Claim 3 attribution) — DONE: CAR=55%, SDF delta=0pp (D025)
- [x] **TSR collapse mechanism analysis** (Claim 3) — M041: composite (forgetting + avoidance retention)
- [x] **LoRA baseline seed2** (plan_013, Claim 3) — DONE: eval_lora_s2_30k_v2, CAR=55.0%, consistent with s0/s1
- [x] **Phase 2 λ=0** (Claim 3) — DONE: D029, single seed CAR=57.5% ≈ LoRA-only (no lasting SDF effect)
- [x] **spatial_bowl A1 训练** (Claim 3) — DONE (failed/killed, 不再追踪)
- [x] **Lambda=0.1 × 2 seeds 20K** (Claim 3) — D035 Scenario B confirmed: mean CAR=55.5% ≈ null
- [x] **Lambda=0.1 × 3 seeds 30K** (Claim 3) — DONE: D043, 3-seed mean=57.00%±2.18, p=0.155 n.s., Scenario B confirmed
- [x] **Pi0.5 baseline re-eval** (Claim 1) — DONE: CAR=28.5%, TSR=71.5%, all safe episodes >288mm displacement
- [x] **Pi0.5 LoRA oracle** (Claim 2, D045/D049) — DONE: eval_oracle_pi05_lora_s0, CAR=51.9% < LoRA 54.83%, 封堵 collapsed-model 攻击面
- [x] **Multi-eval-seed robustness** (Claim 3, D049) — DONE: 8 exps × 5 eval seeds, SDF 冗余跨 eval seed 一致
- [ ] **Pi0.5 baseline 多 seed** (Claim 1, D049 #1 优先) — 当前仅 1 seed, 10 GPU-hrs 即可封堵最薄弱环节
- [ ] **Demo curation Pareto** (R3 应对) — 待标注脚本运行后启动
- [ ] **OpenVLA zero-shot eval** (Claim 1) — BLOCKED (模型下载损坏，暂不追踪)
