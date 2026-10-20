# eco_alpha_beta_diversity — Research Dashboard

> 最后更新: 2026-05-21 14:13 UTC | 更新原因: MVP 真实数据 FAIL，启动延伸验证（D002）

## 核心方向
将生态学 alpha-beta-gamma 多样性分解（Hill numbers + Jost 乘法分区 + Baselga 丰度分解）应用于 LLM 时代文本生态系统，从数学上解释"创造力-多样性悖论"。主投 TACL。

## 当前进展
- **阶段**: MVP 延伸验证（D002）
- **服务器**: 本机执行（CPU）
- **MVP 词汇级结果**: FAIL — alpha↑ 弱 / beta↓ 不显著(q=1) / cosine r=0.03 / rarefaction 后信号消失
- **正面信号**: Baselga 分解 PASS（balanced-variation 92%）、q=2 beta 显著下降、趋势方向全部正确
- **FAIL 部分归因**: size-based rarefaction 过于激进(31词) + FAIL test 2 设计退化（ratio 近似常数）

## MVP 延伸方案（D002）

**目标**: 排除测试方法缺陷后重新评估 kill/go

1. **Coverage-based rarefaction**: 替换 size-based（31词截断），用 coverage standardization 或多截断点（50/75/100词）敏感性分析
2. **FAIL test 2 重设计**: 改为 per-pair Baselga ratio 变异的 R² 预测（而非条件均值恢复）
3. **决策规则**:
   - Coverage-based 后 q=1 alpha↑ AND beta↓ 显著 → PASS MVP
   - Coverage-based 后仍无信号 → 申请 1 张 RTX 6000 做语义级快速验证（1-2 GPU·h）
   - 语义级也无信号 → kill 项目

## 近期任务
- [x] MVP 代码编写 + 知识文件初始化
- [x] 真实数据 MVP 运行（结果 FAIL）
- [ ] Coverage-based rarefaction 分析
- [ ] FAIL test 2 重设计 + 重跑
- [ ] 最终 kill/go 判断

## GPU 预算
MVP 延伸不需要 GPU。如需语义级验证：1 张 RTX 6000 96GB，1-2 GPU·h。用户已表示可提供。

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D004 | 2026-05-21 | KILL 项目：词汇级 + 语义级 MVP 均 FAIL，用户确认归档 | mvp_001, mvp_002 |
| D003 | 2026-05-21 | 词汇级 MVP 彻底 FAIL（coverage-based 确认 alpha↑ 是长度伪影），启动 | — |
| D002 | 2026-05-21 | MVP 词汇级 FAIL 但不立即 kill：延伸 MVP 做 coverage-based rar | — |
| D001 | 2026-05-21 | MVP 方案：在 Doshi & Hauser 数据集上用词汇级 Hill number + Bas | — |

