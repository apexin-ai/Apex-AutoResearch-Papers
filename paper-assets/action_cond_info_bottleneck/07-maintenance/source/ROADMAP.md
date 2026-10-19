# action_cond_info_bottleneck — Research Dashboard

> 最后更新: 2026-05-17 22:51 UTC | 更新原因: v7.2 4-suite 完整结果(FAIL) + v7.3 训练已启动

## 核心方向
ACIB (Action-Conditioned Information Bottleneck)：IB 驱动的 token-level importance scoring for compact VLAs。**关键发现链：joint training 梯度污染(-7.8pp) → scorer-only 仅 global bias → connector+scorer spatial conditioning 成功但 drift 严重(-4.85pp avg) → v7.3 LoRA 结构性隔离(训练中)**。Backbone: SmolVLA (64 tokens, 960-dim)。评测: LIBERO 4 suites。

**论文方向：Direction C (Hybrid)**——Method (LoRA exact baseline) + Constraint Discovery Analysis。详见 paper_framing.md (D052)。

## 目标会议
- **CoRL 2026** (PRIMARY): abstract 5/26, paper 5/29 — 距今 9/12 天

## 当前进展
- **阶段**: MVP 验证（v7.3 LoRA 训练中，关键路径）
- v7.2 4-suite 最终结果：**MVP FAIL** (D053)
  - α=0.0 avg=61.25% (-4.85pp vs baseline, sanity FAIL)
  - α=1.0 avg=62.40% (-3.7pp, core gate FAIL, needs ≥64.1%)
  - **正面信号**：scorer 增量 +1.15pp avg，与任务难度正相关（libero_10 +3.0pp）
  - libero_10 drift 损伤最严重 (-12.8pp)：长 horizon 任务对 connector 精度要求最高
- **v7.3 LoRA 训练中**（两张 GPU 满载，~01:50 UTC 完成）
  - cuda:0: connector LoRA rank=8 (~228K trainable)
  - cuda:1: connector-only ablation（判定 connector 可塑性）
- Baseline: spatial 66.0%, object 67.8%, goal 76.4%, libero_10 54.2%, avg 66.1%

## 近期任务
- [x] v7.2 eval 完成，收集 4-suite 结果 (D053)
- [x] v7.3 + connector-only 训练启动
- [ ] v7.3 训练完成 (~01:50 UTC) → Probe A
- [ ] v7.3 α=0.0 spatial sanity (must = baseline 66.0%±1pp)
- [ ] v7.3 α=1.0 full 4-suite eval → MVP 最终判定
- [ ] connector-only 完成 → α=0.0 eval → 判定 connector 可塑性
- [ ] MVP PASS → 修订 paper_framing.md pending claims → 启动 Paper Agent

## v7.3 MVP Pass/Fail 标准
1. Probe A cos < 0.8（spatial conditioning confirmed）
2. α=0.0 = baseline ±1pp（LoRA structural guarantee，验证实现正确性）
3. α=1.0 4-suite avg ≥ baseline - 2pp (≥64.1%)
4. Δ(α=1.0 - α=0.0) 判定：≥+2pp→Scenario A 强 claim；-2pp~+2pp→Scenario B interpretability；≤-2pp→Scenario C reframe

## 时间线
- NOW: v7.3 训练中（~3h）
- ~01:50 UTC: 训练完成 → Probe A (~30min)
- ~02:30 UTC: α=0.0 sanity eval (spatial only, ~2h)
- ~04:30 UTC: α=1.0 full 4-suite eval (~7h)
- ~11:30 UTC May 18: **v7.3 最终结果 → MVP 判定**
- 如 PASS: 立即启动 Paper Agent (Direction C, 8 天写论文)

## GPU 预算
- 已分配: 2× GPU @ westb-13953 (cuda:0, cuda:1)
- 当前占用: cuda:0 v7.3 LoRA 训练, cuda:1 connector-only ablation（满载）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D054 | 2026-05-18 | v7.3 Probe A: Conditional Pass。严格标准未达(1/3 pairs <0 | acib_v73_connector_lora |
| D053 | 2026-05-17 | v7.2 MVP 最终判定：FAIL（α=0.0 avg -4.85pp, α=1.0 avg -3 | acib_v72_eval_alpha00, acib_v72_eval_alpha10 |
| D052 | 2026-05-17 | 采纳 Direction C (Hybrid): LoRA method + constraint  | acib_v72_eval_alpha00, acib_v72_eval_alpha10 |
| D051 | 2026-05-17 | Connector drift 效果是 suite-dependent 的：spatial -6.6 | acib_v72_eval_alpha00, acib_v72_eval_alpha10 |
| D050 | 2026-05-17 | 论文呈现策略：正文 3 核心 constraint (v7/v7.1/v7.2)，v1-v6 工程迭 | acib_v72_eval_alpha00, acib_v72_eval_alpha10 |
| D049 | 2026-05-17 | 采纳 Connector LoRA 方案（v7.3）替代 λ_drift sweep。LoRA 提供 | acib_v72_connector_scorer_seed1 |
| D048 | 2026-05-17 | 诊断确认：无 eval bug。SmolVLA action expert 对 connector  | acib_v72_connector_scorer_seed1 |
| D047 | 2026-05-17 | 放弃两阶段训练方案（会退回 v7.1 global bias），优先 λ_drift sweep ( | acib_v72_connector_scorer_seed1 |
| D046 | 2026-05-17 | v7.2 libero_spatial suite 级结果：α=0.0=59.4%(-6.6pp), | acib_v72_connector_scorer_seed1 |
| D045 | 2026-05-17 | D044 修正：之前报告的 α=0.0=α=1.0=76% 是 per-task 数据而非 suit | acib_v72_connector_scorer_seed1 |

