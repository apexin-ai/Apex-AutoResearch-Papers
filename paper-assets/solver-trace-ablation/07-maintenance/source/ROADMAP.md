# solver-trace-ablation (PGPF) — Research Dashboard

> 最后更新: 2026-05-13 10:21 UTC | 更新原因: 采纳 Reviewer warnings：多 seed 策略、LC 风险预案、PGPF-S 定位调整

## 核心方向
将 Kovac et al. (EMNLP 2025) 的 model collapse 预测属性（LC, SN, Quality）转为逐样本过滤准则（PGPF），验证 property-specific 过滤优于 confidence-based 过滤。详见 paper_framing.md。

## 当前阶段
**MVP 验证 — Phase 1 准备中**

### Phase 0 完成 ✅ (CONDITIONAL PASS)
- LC 和 SN 与所有属性正交（|r|, |ρ| < 0.35）
- Quality vs Confidence Spearman ρ = -0.998（rank 冗余），有效属性空间 3 维
- D002: Phase 1 用 LC + SN + Confidence；D003: 正交性检查同时用 Pearson + Spearman
- 遗留：LC 动态范围窄 [0, 0.021]；退化生成需修 attention_mask

### Phase 1 设计（3 代过滤对比）
- Qwen2.5-1.5B + OpenHermes (8K/1K/1K), 3 generations, mix_ratio=0.5
- 5 条件：No Filter / Random / Confidence-only / PGPF-S (LC+SN+Conf) / Lexical-only
- 主指标：held-out PPL degradation
- Pass 条件：(1) deg(NoFilter) ≥ 5% (2) PGPF-S vs Conf ≥ 5% relative (3) PGPF-S < Random

### 多 seed 策略（两阶段）
- **阶段 A**：seed=42 单次跑，做 gate check（~15-20 GPU-hours）
- **阶段 B**：gate check 通过后补 seed=123, 7（~30-40 GPU-hours），用于论文 variance 报告
- 单 seed 结果仅为 pilot，论文最终需 ≥3 seeds

## 目标投稿
AAAI 2027（abstract ~Jul 25, paper ~Aug 1）— 约 11 周

## 近期任务
- [ ] Agent 修复 Phase 1 代码：attention_mask + sanity filter + PGPF-S 改 3 属性
- [ ] Agent 调查 LC 动态范围问题
- [ ] Agent 100 样本 sanity check 验证生成质量修复
- [ ] Agent 填写 experiment_plan.yaml
- [ ] Agent 提交 Phase 1 实验审批
- [ ] Phase 1 gate check 通过 → 补 seeds → complete_mvp → post-MVP-kickoff

## GPU 预算
- 分配：autodl-pgpf cuda:0 + cuda:1（2×RTX PRO 6000 96GB）
- Phase 0 消耗：~3 GPU-hours
- Phase 1 阶段 A：~15-20 GPU-hours
- Phase 1 阶段 B：~30-40 GPU-hours
- 全项目（MVP 通过后）：~200-300 GPU-hours

## 关键风险 + 预案
1. **LC 区分度不足** → Lexical-only 条件验证；若失败考虑用 reward model / diversity metric 替代 LC
2. **Novelty 天花板** → 靠阈值轨迹 + property 交互产出 surprising insight
3. **28% 基线接受率** → 需显著改进实验设计
4. **PGPF-S 定位调整** → 从"替代 confidence"转为"增强 confidence"（paper_framing.md 已更新）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D003 | 2026-05-13 | 修正正交性 pass criteria：同时检查 Pearson 和 Spearman，取 max( | phase0_score_v3 |
| D002 | 2026-05-13 | Phase 0 PASS：属性正交性验证通过，有效属性空间 3 维（LC, SN, Quality/ | phase0_score_v3, phase0_ortho_v2 |
| D001 | 2026-05-13 | 放弃 EMNLP 2026 ARR May 25，重定向至 AAAI 2027（abstract J | — |



