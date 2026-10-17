# entrainment_gated_ft — Research Dashboard

> 最后更新: 2026-05-23 22:51 UTC | 更新原因: Pre-RESET handoff: 论文锁定，等待提交

## 核心方向
Per-example predictive multiplicity in hybrid linear recurrent architectures。详见 paper_framing.md。

## 当前进展
- **阶段**: 论文已锁定，等待 ARR EMNLP 2026 提交（DDL 2026-05-25）
- **审稿状态**: 连续两轮 fresh review 均 3.0 Findings（R16, R17），论文达到 Findings 均衡（D040）
- **数据核查**: 全面审计完成，修复 4 项问题（ECE 17%→6%、Tab 7 全表 14/24 cell、Tab 11 caption、routing 数值统一）
- **匿名仓库**: https://github.com/anonymous-nlp-2026-2/entrainment_gated_ft（61 files，code+data only，paper source 已移除）
- **AI disclosure**: Appendix Y "Use of AI Assistants" 已添加

## 提交状态
- ✅ PDF 编译通过，主文 ≤ 8 页，0 错误
- ✅ code_release.zip 打包（1.1MB, 129 files）
- ✅ 匿名仓库已更新（356217b）
- ✅ ARR checklist 字段已准备（含 E1 AI disclosure）
- ✅ 数据核查完成（~50+ 数值点验证）
- ⏳ 用户确认 checklist（作者列表、GitHub URL）— 多次提醒未回复，deadline 20:30 已过，按默认提交处理

## GPU 预算
- westb-48145:cuda:0 × 1（空闲，所有实验+验证已完成，保留至提交后）
- 无活跃实验，无待跑实验

## 近期任务
- [ ] 用户确认后锁定提交（或按默认提交）
- [ ] 提交后释放 westb-48145

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D040 | 2026-05-23 | R17 后锁定论文为 Findings 均衡点，做最终 polish 后不再迭代审稿 | — |
| D039 | 2026-05-23 | R16 审稿报告 Action Matrix 定稿：结构性叙事重组 + Findings 定位 +  | — |
| D038 | 2026-05-22 | 保持 5-arch 论文呈现，不升级到 6-arch（HGRN outlier） | exp-005 |
| D037 | 2026-05-22 | 整合 4 架构 Jaccard 结果到论文 Appendix，不等 6 架构 | exp-005 |
| D036 | 2026-05-22 | 恢复 exp-005：Zoo 确认含 6 架构，之前取消理由有误 | exp-005 |
| D035 | 2026-05-22 | 取消 exp-005（6 架构扩展不可行），转向替代实验方案 | exp-005 |
| D034 | 2026-05-22 | E4 Pythia seed calibration 结果接受：70M 替代 410M，放 Appe | e4-pythia-seed-calibration |
| D033 | 2026-05-22 | D033: Pythia framing 策略 + 额外架构 stretch goal 标记 | e4-pythia-seed-calibration |
| D032 | 2026-05-22 | D032: 批准 Pythia 410M multi-seed calibration 实验——用  | — |
| D031 | 2026-05-22 | D031: E1 routing 结果 framing——作为 §4.1 supporting an | — |


