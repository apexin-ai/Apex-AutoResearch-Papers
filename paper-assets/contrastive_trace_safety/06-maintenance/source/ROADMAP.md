# contrastive_trace_safety — Research Dashboard

> 最后更新: 2026-05-23 01:27 UTC | 更新原因: Round 31 修复完成，bootstrap CI/classifier sensitivity 完成，GPU 释放，更新为最终状态

## 核心方向
Reasoning model 安全轨迹的对比隐状态分析：揭示 layer selection bias 对安全探针结论的决定性影响。详见 paper_framing.md。

## 当前进展
- **阶段**: Research → 论文最终修订（DDL 2026-05-25 ARR）
- **论文状态**: Round 31 审稿修复完成（commits 517a09d + 77c6e1f + a283fd9），等待复审
- **Overall**: 3.0 (Findings)，R1=3.5 (Borderline Conference) / R2=3.0 (Findings)
- **9 项修复**: MF1 32B exploratory 控制 ✅ / MF2 multi-layer probing 文献 ✅ / MF3 conditional inference ✅ / SF1-6 全部 ✅
- **页面**: 8 主文 + 26 appendix/refs = 34 页，Conclusion 完整在 p8，0 critical warnings
- **Bootstrap CI (D067)**: 31.7pp divergence (95% CI [3.2, 48.4], p=0.015)，已整合到论文
- **Classifier sensitivity**: 3 threshold 完成，rebuttal 备弹存档（不入正文）
- **跨架构**: Gemma-2 compression 1.28× ✅ / Gemma-4 无 compression 0.70× ✅ / R1-8B 1.54× (metric-selected) ✅

## 近期任务
- [x] Bootstrap CI → 已完成，31.7pp (p=0.015) 整合到论文 (D067/D068)
- [x] Classifier sensitivity → 已完成，3 threshold 存档作 rebuttal 备弹
- [x] Round 31 审稿 9 项修复 (D068)
- [x] SF4 页面溢出修复 (a283fd9)
- [ ] **等待用户审批复审卡** ← 阻塞项
- [ ] **复审通过后根据意见微调**
- [ ] **ARR 提交（DDL 2026-05-25，用户手动）**

## GPU 预算
- westd-49253 (4×RTX PRO 6000): 已由 Manager 回收
- westd-15904 (1×RTX PRO 6000): 已通知 Manager 释放（所有实验+分析完成）
- 当前无 GPU 占用

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D069 | 2026-05-23 | R32 Action Matrix: 3 fixes (page compliance + MDL  | — |
| D068 | 2026-05-22 | Round 31 审稿报告 Action Matrix 定稿 — 9 项写作修复，无新实验 | sf3_quadratic_residual |
| D067 | 2026-05-22 | AdvBench divergence 从 58pp 更新为 bootstrap-validated | advbench_layer_bias_r1_8b, advbench_layer_bias_gemma2 |
| D066 | 2026-05-22 | 删除 R40 cosine profile 图 + 补 Tab gemma_compression  | advbench_layer_bias_r1_8b, advbench_layer_bias_gemma2, advbench_layer_bias_gemma4 |
| D065 | 2026-05-22 | 跨架构 cosine compression 结果：Gemma-2 有 compression (0 | advbench_layer_bias_gemma4, advbench_layer_bias_gemma2 |
| D064 | 2026-05-22 | Gemma 跨架构策略调整：probe-based layer selection → geomet | advbench_layer_bias_gemma4, advbench_layer_bias_gemma2 |
| D063 | 2026-05-22 | Gemma-4 v2: 14/520 JB (2.7%), divergence 14.7pp —  | advbench_layer_bias_gemma4 |
| D062 | 2026-05-22 | AdvBench v1→v2: 修正分类器后 divergence 42pp→58pp，论文已更新为 | advbench_layer_bias_r1_8b |
| D061 | 2026-05-22 | R1-8B AdvBench Phase 2 完成：C1 layer selection bias  | advbench_layer_bias_r1_8b |
| D060 | 2026-05-22 | 用户批准 A+B：Gemma-2 二值层偏差 + Gemma-4-E4B reasoning 复制， | advbench_layer_bias_r1_8b, advbench_layer_bias_gemma2, advbench_layer_bias_gemma4 |

