# ICRA 2027 Venue Analysis — CoRL → ICRA 转投评估

Generated: 2026-05-29

## 1. ICRA 2027 基本信息

| Item | Details |
|------|---------|
| 会议 | IEEE International Conference on Robotics and Automation (ICRA) 2027 |
| 地点 | COEX, Seoul, Republic of Korea |
| 会期 | 2027-05-24 ~ 2027-05-28 |
| Submission DDL | **尚未公布**（官网 2027.ieee-icra.org/contribute 显示 "detailed schedules will be updated soon"） |
| DDL 预估 | **2026-09-15 ± 1 周**（参考 ICRA 2026 DDL = 2025-09-15/16 PST，ICRA 2025 DDL = 2024-09-15） |
| 从现在到预估 DDL | **~3.5 个月**（2026-05-29 → 2026-09-15） |

Sources:
- [ICRA 2027 Official](http://2027.ieee-icra.org/)
- [ICRA 2027 Calls for Papers](https://2027.ieee-icra.org/contribute/)
- [ICRA 2026 DDL Extended](https://2026.ieee-icra.org/announcements/paper-submission-deadline-is-extended-to-sept-16-2359-pst/)

## 2. 格式要求对比

| Dimension | CoRL 2026 (当前) | ICRA 2027 (预估) |
|-----------|------------------|-------------------|
| 模板 | `corl_2026.sty` (单栏) | IEEEtran (双栏) |
| 正文页限 | 8 页 (含 Limitations) | 6 页正文 + 无限 refs **或** 8 页含 refs（ICRA 2026 改为 8 页，待 2027 确认） |
| References | 不计页限，单独页 | 包含在页限内（传统）或不计（2025+ 新规） |
| Appendix | 允许，不计页限 | **不允许 appendix**（所有内容必须在正文页限内） |
| 栏数 | 单栏 | 双栏 |
| 审稿方式 | 双盲 | 双盲 |
| Supplementary | 单 zip (OpenReview) | 视频鼓励，代码可选 |
| Limitations section | 必需 (计入 8 页) | 非必需（但推荐） |

**关键差异：ICRA 不允许 appendix。** 当前论文 8 页 appendix（12 个 section）的内容必须要么压入正文、要么放 supplementary、要么删除。

Sources:
- [ICRA Paper Format (IEEE-RAS)](https://www.ieee-ras.org/contribute/paper-submission)
- [ICRA 2026 Final Paper Instructions](https://2026.ieee-icra.org/contribute/final-paper-submission-instructions/)
- [ICRA LaTeX Template](https://www.underleaf.ai/templates/icra)

## 3. 改动量评估

### 3.1 必须改动（High Effort）

| 项 | 工作量 | 说明 |
|----|--------|------|
| **模板迁移** | 中 | CoRL 单栏 → IEEEtran 双栏。需重新排版所有 figure/table/equation。双栏下图表宽度减半，需调整 figure* 和 table* 的使用 |
| **Appendix 内容处理** | 高 | 当前 8 页 appendix 含 12 section（multi-seed results, threshold sensitivity, per-task breakdowns, null distribution, oracle details, training details, eval seed robustness, stepwise analysis, TSR collapse mechanism）。策略：(1) 核心证据压入正文 (2) 完整表格放 supplementary PDF (3) 删除冗余 |
| **页限压缩** | 高 | 双栏 6 页 ≈ 单栏 4 页文字量。当前 8 页单栏正文需压缩约 50%。即使 ICRA 2027 沿用 8 页制，双栏 8 页 ≈ 单栏 5.3 页，仍需压缩 33% |
| **References 格式** | 低 | 从 `\bibliography{references}` 切换到 IEEEtran bib style。可能需要调整 bib key 和条目格式 |

### 3.2 内容调整（Medium Effort）

| 项 | 工作量 | 说明 |
|----|--------|------|
| **Narrative 调整** | 中 | ICRA 偏系统/应用，CoRL 偏学习方法。当前 framing（"evaluation methodology critique"）对 ICRA 也合适，但可能需要加强 system-level implications（如 real-world deployment, hardware safety） |
| **Related work 扩展** | 低 | ICRA 审稿人更关注传统 robotics safety（CBF, potential fields, motion planning），当前 related work 已覆盖这些，可能需要加 1-2 个 ICRA-native 引用 |
| **Seed3 结果整合** | 低~中 | 如果 seed3 在 DDL 前完成，需更新 Claim 3 数据（不影响 framing，只改数字） |

### 3.3 无需改动

- paper_switch.py Scenario B/C 机制仍适用（只需更新 anchor 位置）
- 核心 claims 和 narrative 不变
- 所有 experimental data 不变

## 4. Scope Fit 评估

### ICRA 覆盖领域
ICRA 覆盖 robotics 全领域，包括但不限于：Manipulation, Machine Learning for Robotics, Robot Safety, Human-Robot Interaction, Motion Planning, Perception, Learning from Demonstration。

### 本文 fit 分析

| 维度 | 评估 | 说明 |
|------|------|------|
| **Topic relevance** | ★★★★☆ | VLA safety + collision avoidance + SDF = ICRA 核心话题（manipulation + safety + perception） |
| **Methodology** | ★★★★☆ | Evaluation methodology paper + negative results，ICRA 接受此类贡献 |
| **Practical impact** | ★★★★★ | 论文直接关注 deployment safety（action collapse = real-world hazard），ICRA 审稿人对此敏感 |
| **Audience match** | ★★★★☆ | ICRA 有大量 VLA/robot learning 审稿人，但也有传统 control 审稿人可能不熟悉 VLA |
| **Negative results risk** | ★★★☆☆ | ICRA 对 negative results 的接受度略低于 CoRL/NeurIPS，但本文的 dfCAR 贡献是 positive 的 |

**总体 fit: 强。** 论文的 system-safety 角度非常适合 ICRA。主要风险是 negative-results framing 在传统 ICRA 审稿人中的接受度。

## 5. 转投时间线

| 时间 | 事项 |
|------|------|
| 2026-06 ~ 2026-07 | CoRL 审稿期。利用此时间：(1) 完成 seed3 实验 (2) 开始 IEEEtran 模板迁移 (3) 压缩正文 |
| 2026-07 中旬 | CoRL notification（预计）。若被拒，启动全速 ICRA 转投 |
| 2026-07 ~ 2026-08 | ICRA 版本精修：压缩 appendix、调整 narrative、排版 |
| 2026-09-01 | 内部 deadline：ICRA 版本完成初稿 |
| ~2026-09-15 | ICRA 2027 submission DDL（预估） |

**结论：3.5 个月充裕，但模板迁移 + 页限压缩是主要工程量。建议 CoRL 审稿期间即启动 IEEEtran 排版，不等结果。**

## 6. 建议

1. **立即可做**：创建 `docs/paper_icra/` 目录，复制 .tex 文件，替换模板为 IEEEtran
2. **CoRL 审稿期间**：完成模板迁移的 skeleton（不改内容，只排版），验证双栏下图表的可读性
3. **收到 CoRL 结果后**：根据 reviewer feedback 同步改进内容，若接收则不需转投；若拒则内容改进 + ICRA 格式 = 快速提交
4. **Appendix 处理策略**：将 per-task breakdown (A.5, A.6)、null distribution (A.7)、oracle details (A.8) 压入 supplementary PDF；将 training details (A.10) 压入正文 method section；删除 eval seed robustness (A.12) 和 stepwise (A.9) 除非空间允许
