# ec_hte_llm_annotation — Research Dashboard

> 最后更新: 2026-05-24 06:11 UTC | 更新原因: 三路任务全部完成（终审PASS+review issues修复确认+rebuttal文档），等用户提交决策

## 核心方向
识别并形式化 LLM 标注误分类异质性 × CATE 异质性的交互偏差机制，提出 EC-HTE 层级贝叶斯分层校正框架。详见 paper_framing.md。

## 当前阶段
**DDL 冲刺 — EMNLP 2026 ARR 5/25（今天）**

### 论文状态
- 主文 8 页（≤8 页限制），含 appendix 共 32 页
- 编译 0 errors, 0 undefined refs, 0 warnings
- Abstract ~179 words
- Framing 优化完成：Warning 55% / Diagnostic 30% / EC-HTE 15%
- 7 维终审全部 PASS（Reviewer 确认）
- 7 项 review_issues 修复确认（Paper Agent 确认）
- Rebuttal talking points 文档就绪（344 行，16 题）

### 分数评估
- R17=3.5 → R18=3.0（降分原因：MF1/MF2/SF1-7 共 12 项写作问题）
- 12 项全部修复 + 3 项 framing 优化后，预估 3.0-3.5
- 天花板 ~3.5；突破需新 evidence，当前 real LLM Δπ∈[0.10, 0.20] 低于 EC-HTE 阈值 0.15

### 实验总览
成功 36 / 负向 5 / killed 1 / 共 42

### 核心 evidence 盘点
| Evidence | 状态 | 位置 |
|----------|------|------|
| Bias identity R²≥0.97 | ✅ 已在主文 | §5.2 |
| Sign reversal 14.9% (τ=0.03) | ✅ 已在主文+Fig 1 | §1, §5.2 |
| 8/8 real LLMs bias amplification | ✅ 已在主文 | §5.2, Fig 1C |
| Cross-estimator (DIM/CF/R-learner) | ✅ 主文+appendix | §5.3, App S |
| Diagnostic AUC 1.0/0.86/0.63 | ✅ 已在主文 | §5.4 |
| EC-HTE 7.4× bias reduction | ✅ 已在主文 | §5.3 |
| Real data EC-HTE failure + 原因 | ✅ 诚实报告 | §5.4, App A.6 |
| Operating conditions | ✅ 已在主文 | §5.4 |
| 11 LLM-dataset R²=0.975 | ✅ 已在 appendix | App V |
| Stance cross-task validation | ✅ 已在 appendix | App (new) |

## 近期任务
- [x] Framing 优化 3 项（abstract/intro/operating conditions）
- [x] Stance appendix 修复 + 编译
- [x] 图文件完整性检查：7/7 引用文件全部存在
- [x] 附录可发现性：6 forward refs + 2 表格迁移
- [x] makecell warning 修复
- [x] Review issues 7 项 in_progress 全部确认修复
- [x] Rebuttal talking points 文档
- [x] 7 维终审 PASS
- [ ] **等用户决策：是否提交 5/25 DDL**

## GPU 预算
- **当前无 GPU 资源**——如需 GPU 实验需向 Manager 申请新实例
- local-cpu: CPU-only，可跑 MC 模拟

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D027 | 2026-05-24 | M1 asymmetric 结果 framing：R² 正向报主文，method compariso | exp-041 |
| D026 | 2026-05-24 | 保留 AUC=0.86，registry exp-005 的 0.833 来自早期小数据集，figu | exp-005 |
| D025 | 2026-05-23 | Stance detection 纳入 appendix 作为 cross-task 验证 + 边界 | — |
| D024 | 2026-05-23 | Stance detection 实验结果不纳入论文，仅作 rebuttal 备料 | stance_detection |
| D023 | 2026-05-23 | Dream 三档评分 3.5/3.0/2.5 — reframe 未达 4.0 目标，结构性问题需修 | — |
| D022 | 2026-05-23 | 取消 Task K (Pipeline 概念图)，保留 sign-reversal 3-panel  | — |
| D021 | 2026-05-22 | 全面优化冲刺：双轨并行（实验+写作），保3.5冲4，提交前最后一轮内部审稿 | — |
| D020 | 2026-05-22 | Round 3审稿报告处理：12/17 issues已在当前版本解决，仅需修复页数超限+小幅文本调整 | exp-019, exp-023 |
| D019 | 2026-05-22 | Hetero-τ 4模型K=4结果作为rebuttal材料，不写入论文 | exp-023 |
| D018 | 2026-05-21 | C1 framing: coverage-led narrative + heterogeneity | exp-008, exp-001 |

