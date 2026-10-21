# event-gated-adaptive-horizon — Research Dashboard

> 最后更新: 2026-05-30 04:25 UTC | 更新原因: 论文写作优化全部完成（P1-P3 融入 + Follow-up A/B/C），等待服务器恢复

> 最后更新: 2026-05-30 | 更新原因: 论文写作优化全部完成，等待服务器恢复

## 核心方向
DreamerV3 中 trained dt_embedding 驱动的 CIVO（Conditioning-Induced Value Overestimation）是 **6-DoF multi-joint locomotion 特异性现象**。详见 paper_framing.md。

## 当前进展
**阶段**: 🔬 Research — ICLR 2027 投稿准备
- **投稿目标**: **ICLR 2027**（~10月 DDL，4 个月 runway）
- **实验统计**: 213 completed + 1 RUNNING（westd 宕机，状态未知）
- **论文**: 46 页（10 主文 + 36 附录），编译通过
- **Reviewer 评分预估**: 6.8-7.0；STORM Scenario A 可达 7.5+
- **硬件**: westd-51268 SSH 不可达 >16h。已向 Manager 正式申请新 AutoDL 实例
- **审稿**: Round 8（fresh ICLR-targeted）待用户审批
- **通信**: 飞书 API 月配额耗尽（6/1 重置），通过 Manager 转发

## 已完成的质量改进
- [x] D181-D183: 论文质量强化 + ICLR 重构 + 写作打磨
- [x] STORM DMC 适配代码预写 + 三场景预写文本
- [x] 引用审计：2 个 bib 问题修复
- [x] Related Work 定位审计 + failure case 讨论 + clarity 打磨
- [x] Reviewer 叙事微调：§4 预告句 + Intro §4 重框架 + onset rate CI
- [x] Cold-start 部署包（setup_env.sh + launch_commands.md）
- [x] STORM 实验设计文档（Reviewer 已审查，灰色地带 + confounds 已补）
- [x] 阴性实验 pattern 分析（43 个 negative，4 个 cross-category pattern）
- [x] P1-P3 pattern 融入 §4 + P4 Discussion（6 处修改，量化 SGS/RAVE/TCN 失败 pattern）
- [x] §4 unifying paragraph 聚合统计（wide dual-critic 跨环境数据）
- [x] P4 Discussion 措辞精化（引用 exp_008f，NVE 诊断价值关联）
- [x] STORM 设计文档更新（Config C mandatory + grey zone + confounds + GPU 预算）

## 阻塞项
| 阻塞 | 等待 | 影响 |
|------|------|------|
| westd-51268 不可达 | Manager 回复：新实例 or 恢复 | 所有 GPU 实验 |
| Round 8 审稿 | 用户审批 | 论文迭代 |

## GPU 恢复后优先级（D184）
1. walker_no_dt_emb_s0_r2 状态确认/重启（C2 control，~6h）
2. STORM Phase 1 baseline（~6h GPU）
3. STORM Phase 2：Config A (trigger) + B (no-emb) + C (frozen, mandatory)（~18h GPU）

## Reviewer 关键发现
- 6.8→7.5 唯一杠杆是 STORM 实验（scope 扩展）
- 写作层面优化已完成，接近上限
- STORM Config C (frozen control) 从 optional 升为 mandatory
- 阴性 pattern P1-P3 已融入 §4，P4 强化 NVE 诊断价值叙事

## review_issues 状态
- 仅 1 个 in_progress：N-R4-1（ICLR 2027 模板切换）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D184 | 2026-05-29 | D184: STORM transformer WM 实验采用 Phase 1/Phase 2 分阶 | — |
| D183 | 2026-05-29 | D183: 6 项低成本写作打磨（F6 defense + Abstract hook + sect | — |
| D182 | 2026-05-29 | ICLR 2027 论文重构：新增 "Why Standard Remedies Fail" sec | — |
| D181 | 2026-05-29 | 论文质量强化：Gap 1 (零跨环境迁移) + Gap 2 (SGS 悖论量化) + Abstrac | — |
| D180 | 2026-05-29 | Quadruped baseline 判定 unhealthy（125K NVE=6.6×，9/11 | exp_quadruped_baseline_s0_r2, exp_quadruped_008d_s0, exp_humanoid_baseline_s0 |
| D179 | 2026-05-29 | Quadruped baseline NVE 轨迹不乐观（6/10 > 2.0），降低 scope  | exp_quadruped_baseline_s0_r2, exp_humanoid_baseline_s0 |
| D178 | 2026-05-29 | 排除 Humanoid Walk 作为 CIVO 隔离实验环境；CIVO scope 限定为 bas | exp_humanoid_baseline_s0, exp_humanoid_008d_s0, exp_quadruped_baseline_s0_r2 |
| D177 | 2026-05-29 | 放弃 Humanoid 200K 实验，跳过 humanoid_008d_s0，优先 Quadrup | exp_humanoid_baseline_s0, exp_humanoid_008d_s0, exp_quadruped_baseline_s0_r2 |
| D176 | 2026-05-28 | CoRL DDL 到期未提交，venue fallback 触发：默认目标 AAAI 2027 (7 | — |
| D175 | 2026-05-28 | 启动 Phase 1 环境扩展实验（Humanoid + Quadruped），D171 不阻止新环 | exp_humanoid_baseline_s0, exp_humanoid_008d_s0, exp_quadruped_baseline_s0, exp_quadruped_008d_s0 |






