# code appendix data gar mmlu 15b

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_appendix_data_gar_mmlu_15b_20260524T150629_result.json`
- **Structured JSON:** [`e14646386b9f8d5bc654.json`](../../sessions/e1/e14646386b9f8d5bc654.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。生成的附录素材汇总：

**第 4 项：数据集统计**
- `tab_dataset_stats.tex` — UltraChat-200K 源数据 207,865 → 过滤≥5轮 17,302 → 采样 8,000 训练 / 50+50+200 评估；平均 5.6 轮 (5–7)
- UltraChat 无 topic 标签，跳过 topic 分布图

**第 5 项：GAR 定义鲁棒性**
- `tab_gar_robustness.tex` — 4 种 token selection × 3 条件完整表，含 Turn-1 GAR / Mid-turn GAR / Gap Ratio
- `fig_gar_robustness_grouped.pdf` — 分组柱状图（Base 近零 → TG/SS 大幅提升）

**第 6 项：MMLU 质量保留**
- `tab_mmlu_detail.tex` — 4 类别 × 6 条件详表（STEM/Social Sci/Humanities/Other + Overall + Δ），最大降幅仅 0.77pp
- `fig_mmlu_comparison.pdf` — 分组柱状图对比

**第 7 项：Qwen-1.5B 跨尺度**
- `tab_qwen15b_results.tex` — Phase 1 诊断（79.8% GAR 衰减）+ Phase 2 TG 训练（β=0: p=0.005, β=5: p<0.001），含 CI 和 Wilcoxon 效应量

---
