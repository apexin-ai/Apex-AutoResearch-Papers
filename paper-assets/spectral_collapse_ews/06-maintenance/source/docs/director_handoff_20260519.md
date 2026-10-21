# Director Handoff — 2026-05-19 07:30 UTC

## 项目状态一句话
EMNLP 2026 ARR Long Paper (DDL May 25)，论文 8 pages 上限已达，r_crit ∈ (0.25, 0.3] 精度 ±0.025，Phase 1 接近完成，Phase 2 multi-seed 启动中。

## 在跑实验
- **exp_009 (r=0.25, cuda:0)**: Gen 3/10, ~14h remaining. Type II confirmed (Gen 1 dip -4.6, Gen 3 rebound +17.8). 关键实验——10gen 数据将确认 r=0.25 长期 trajectory。
- **exp_010 (pure_collapse seed43, cuda:1)**: 刚启动 (~7:00), Phase 2 multi-seed 第一个实验。10gen ~20h.

## 已完成实验
| exp_id | condition | r | seed | gens | result |
|--------|-----------|---|------|------|--------|
| exp_001 | pure_collapse | 0 | 42 | 10 | success, Type I |
| exp_004 | fixed_mix | 0.5 | 42 | 10 | success, Type III |
| exp_006 | adaptive | 0.5 | 42 | 10 | negative (controller silent) |
| exp_007 | fixed_mix | 0.2 | 42 | 5 | success, Type II (dip-then-recovery) |
| exp_008 | fixed_mix | 0.3 | 42 | 10 | success, Type III, SLV=2511.1 |

## r_crit Phase Diagram 数据
| r | trajectory | SLV Gen 10 (or last) | Type |
|---|-----------|---------------------|------|
| 0 | collapse | 2179 | I |
| 0.2 | dip-then-recovery | 2399 (Gen 5) | II |
| 0.25 | dip-then-recovery | 2381 (Gen 3, running) | II |
| 0.3 | monotonic expansion | 2511 | III |
| 0.5 | monotonic expansion | 2572 | III |

r_crit ∈ (0.25, 0.3], EMA non-decreasing condition 在 r=0.25 的 t=2 失败, r=0.3 的 t≥2 全满足。

## 论文当前状态
- 8 pages (上限), latest commit `d7052de`
- C1 (三相 spectral pattern): strong evidence
- C2 (SLV as monitor): strong evidence
- C3 (signal attenuation paradox): strong evidence, all 7 alt-EWS reverse
- C4 (phase diagram): medium-strong, r_crit (0.25, 0.3] with 5 data points
- Abstract/Conclusion 已覆盖 C4 (commit 49b94cb)
- §4.5 有完整 Type I/II/III 描述 + dip 幅度单调递减 + r_crit meaning
- §2.2/abstract/conclusion bound 已同步到 (0.25, 0.3] (commit d7052de)
- Conclusion 有 monitoring preemption (commit 91042fb)
- Intro L19 已修复 (不再 claim multi-scale/multi-seed)
- Soundness ~2.5/4, 达 3/4 需: multi-seed 1组 + exp_007 resume 10gen

## 排期
- cuda:0: exp_009 r=0.25 (~14h) → exp_007 resume 10gen (~10h) → r=0.2 seed43
- cuda:1: exp_010 pure seed43 (~20h) → pure seed44 → r=0.5 seed43
- 所有 Phase 2 launch scripts 已就绪: `/root/spectral_collapse_ews/scripts/`

## 待做（按优先级）
1. exp_009 Gen 5+ 数据到后: 更新 §4.5 r=0.25 描述, 确认 10gen trajectory
2. exp_010 完成后: 验证 C1 三阶段 multi-seed 一致性
3. exp_007 resume to 10gen: 验证 r=0.2 长期 trajectory (当前只有 5gen)
4. §4.5 最终版: 加入 r=0.25 10gen 数据, 可能加 mini-table
5. Phase 2 multi-seed 数据 → error bars, 修改 Table 1
6. Limitations 更新 (multi-seed 完成后)

## 分析已完成
- 二阶 EWS (plan_023): r=0 持续负, r=0.2 仅 Gen 2 负, r=0.5 Gen 8 才转负. Discussion level.
- Controller activation window: r=0 Gen 4-10 激活, r=0.2 从未激活 (max Δ_t=0.0019 < τ), r=0.5 从未激活.

## 关键决策
- D027: C5 (second-order EWS) 降为 Discussion/future work
- D028: r_crit 从 trajectory shape transition 重新定义
- D029: r_crit 收紧至 (0.25, 0.3]

## 教训
- cron 回调不可靠: exp_008 完成后 cuda:1 空闲 2.5h, Agent 没自动接力. 需主动 check.
- Agent 报告 gen 进度时可能混淆 synthetic data generation step 和 training completion (M010).
- Reviewer 可能基于 stale version 审查 (M009).
