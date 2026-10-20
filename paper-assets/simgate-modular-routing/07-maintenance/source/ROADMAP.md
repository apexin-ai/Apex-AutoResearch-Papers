# simgate-modular-routing — Research Dashboard

> 最后更新: 2026-05-22 09:33 UTC | 更新原因: R28 全部修复完成 + Reviewer 验收 PASS + review_issues.yaml 更新

## 核心方向
**[D126/D127 Framework-centric pivot]** Episode-level counterfactual analysis as a diagnostic framework for understanding when and why deterministic computation helps LLM agents. ScienceWorld case study: death avoidance accounts for ~79% of routing signal (penalty-independent label fraction). 详见 paper_framing.md。

## 当前进展
**R28 fresh review 修复完成（12/15 items PASS），Reviewer 验收 10/10 PASS。** DDL 2026-05-25（剩 ~3 天）。

- 目标：EMNLP 2026 via ARR, Findings (≥3.0)
- **121 个实验全部完成**（53 成功 / 68 阴性+失败+killed）
- R28 Overall 3.0, R1/R2 独立打分均 3.5 Borderline Conference
- ✅ **R28 修复完成**：
  - N2 DAF framing 终极修复：§2.4 添加 P=10/50/100 sensitivity 数值 + label fraction 作为 primary diagnostic
  - N3 Oracle/deterministic：Conclusion 限定 "procedure transfers, not operationalization consistency"
  - N1 Episode-level：Abstract 添加 "episode-level" 限定词
  - W1 Signal/data-limited：§5 对称性改善
  - W2 Concurrent routing：§5 ¶1 末尾 1 句 W7 讨论
  - W4 Taxonomic redundancy：§3 操作定义添加
  - W5 K=11：Limitations 添加 Cameron et al. K≥20-50 引用
  - W1(R28) 72B scope：Limitations 添加
  - W2(R28) Graded failure：Limitations 添加
  - M1 部分完成（仅 Alshiekh 2018；CALM/MoD/Geifman 因超页删除）
  - M3 §1 重复删除 + contributions 压缩
  - M4/M5 wont_fix（页数约束）
- ✅ **W4 64.7% task-type classifier 已写入 §3.6**（D133）
- ✅ **Rebuttal 6 个 Attack 准备完毕**（精简版 ~670 词 + 详细版 ~1200 词）
- ✅ **编译通过**：24 页（主文 8 页），0 errors
- 用户："论文提交的事你不用管，我们会手动去做的"

## 近期任务
- [x] R27 审稿修复全部完成 + Reviewer 验收 PASS
- [x] W4 64.7% 写入正文 §3.6 + 压缩验收 PASS
- [x] R28 fresh review 修复完成 + Reviewer 验收 10/10 PASS
- [x] review_issues.yaml R28 状态全部更新
- [ ] 用户手动提交 ARR（DDL 05-25）

## GPU 预算
- westd-18266: 4× RTX PRO 6000 — GPU 已全部释放（D129），无活跃实验
- D131/D132: 最后阶段不开新 GPU 实验

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D133 | 2026-05-22 | W4 64.7% task-type classifier 写入正文 §3.6（推翻之前 rebut | — |
| D132 | 2026-05-21 | 维持 D131 冻结，不补做 task-level router positive control  | — |
| D131 | 2026-05-21 | DDL 前 4 天不再做新实验，聚焦零错误提交 | — |
| D130 | 2026-05-21 | D130: 接受 Findings 级别 (3.0)，不追 Borderline Conferenc | — |
| D129 | 2026-05-21 | 释放 2× RTX 5090 GPU，不再跑新实验。剩余工作全部是零 GPU 分析/写作。 | gemma-scienceworld-v5 |
| D128 | 2026-05-19 | 预防性跑 #3 扩展 task types：5 个排除 task types × 20 eps fu | — |
| D127 | 2026-05-19 | paper_framing.md 更新为 framework-centric（D126 落地）：C1 | — |
| D126 | 2026-05-19 | R19 Action Matrix: Framework-centric reframing + 2 | — |
| D125 | 2026-05-19 | 终止第三环境 permadeath replication 尝试。MiniHack 0%/0% (无 | minihack-cross-env-pilot, crafter-pilot |
| D124 | 2026-05-19 | MiniHack 导航任务 0% death rate 触发 Day 2 fallback：双轨并行 | minihack-cross-env-pilot |


