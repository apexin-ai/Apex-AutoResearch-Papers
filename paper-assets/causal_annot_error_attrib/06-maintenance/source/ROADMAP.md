# causal_annot_error_attrib — Research Dashboard

> 最后更新: 2026-05-24 10:13 UTC | 更新原因: Round 23 审稿状态同步 + DDL-day 工程保障聚焦

> 详见 paper_framing.md（story/claims）、experiment_plan.yaml（实验列表）

## 核心方向
多分类 LLM 标注误差在因果推断中的偏差传播：K×K 混淆矩阵 × 7 DAG 拓扑偏差分类 + ASV 灵敏度框架 + 校正指导。

## 当前阶段：提交前最终检查

### Target Venue
- **EMNLP 2026**（ARR rolling review，8 页 main text + unlimited refs）
- DDL: 2026-05-25

### Core Claims 覆盖率
| Claim | 完成/总计 | 状态 |
|-------|-----------|------|
| 1. Multi-class bias taxonomy | **5/6 (83%)** | plan_001✅ plan_002✅ plan_008✅ plan_009✅ plan_010✅ plan_003⚠️(API 402, 搁置) |
| 2. ASV framework | **3/3 (100%)** | plan_004✅ plan_005✅ plan_006✅ |
| 3. Correction guidance | **1/1 (100%)** | plan_007✅ |

### 论文状态
- ✅ Main text 8 页（Conclusion + Limitations 在 page 8）
- ✅ 0 undefined references, 0 compilation errors
- ✅ 匿名化完整
- ✅ Round 23 审稿 3.5 (Borderline Conference)，MF-1/2/3 + SF-3 已在 commits bb8c468/c9b3b2b 中处理
- ⏳ Agent 正在修复附录 Overfull warnings
- 3.5→4.0 差距为结构性（Conjecture 1 证明 + 端到端真实因果验证），DDL 前不可修复

### 审稿评分历史
Round 23 (最新): 3.5 Borderline Conference — Reviewer 确认当前 3.5 稳固，无 quick win 可推至 4.0

## 近期任务
- [ ] Agent 完成附录 Overfull 批量修复
- [ ] 最终编译验证（页数 + 无警告）
- [ ] 提交前 checklist 确认
- [x] GPU 释放通知 Manager（D021）
- [x] MF-1/2/3 + SF-3 writing fixes 确认已完成（Reviewer 核实）
- [x] 页数/编译/匿名化工程检查 ✓

## GPU 预算
home-1x5090: 1× RTX 5090（已通知 Manager 释放，本项目不再需要 GPU）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D021 | 2026-05-24 | GPU 无生产性用途，建议释放 home-1x5090 给其他项目 | plan_003, plan_006 |
| D020 | 2026-05-22 | 搁置 plan003 frontier annotations 和 Re-dream；GPU 通知  | plan003_empirical_confusion_matrices, plan006_asv_empirical |
| D019 | 2026-05-22 | Sign flip 检查扩展为全系数检查，论文叙事从 "zero sign flips" 改为 "5 | plan006_asv_empirical, plan011 |
| D018 | 2026-05-22 | Round 1 审稿 3.5→4.0 修复计划：proof 降级 + δ_max 约束 + fram | — |
| D017 | 2026-05-21 | 保持 14 configs / 98 scenarios；ASV-unsafe 阈值 ≤1.0 (3 | plan006_asv_empirical |
| D016 | 2026-05-21 | plan_006 全量结果确认跨K实证验证：K越小bias越大（K=3 IV 252%），F1 di | plan006_asv_empirical, plan003_empirical_confusion_matrices |
| D015 | 2026-05-20 | plan_006 humaid 实证结果确认理论框架：IV 最脆弱(42% bias), colli | plan003_empirical_confusion_matrices, plan005_asv_extended, plan004_asv_framework |
| D014 | 2026-05-20 | plan_007 全量结果确立 Claim 3 correction guidance 层级：PPI | plan007_correction_guidance |
| D013 | 2026-05-20 | plan_009 证实病态矩阵诊断指标（spectral_gap, condition_number | plan009_pathological_matrices |
| D012 | 2026-05-20 | plan_007 预览发现：Frisch-Waugh 定理导致 naive_plugin/MLA 对 | plan007_correction_guidance |


