# research figure audit

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_figure-audit_20260518T075309_result.json`
- **Structured JSON:** [`9fbbdd226d92856712f4.json`](../../sessions/9f/9fbbdd226d92856712f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have a complete picture. Here's the report:

---

## 图表检查报告

### fig1_architecture.pdf（架构图）
- **状态**: 存在（local artifacts）
- **内容**: 只展示 **Treatment Pipeline**（8-class persuasion multitask）vs **Baseline Pipeline**（Vanilla DeBERTa）两条路径
- **需要更新**: **YES**
- **原因**: 缺少全部 7 个 Stage-1 encoder variants。当前只有 2 个（treatment + vanilla）。需要新增：
  - Binary persuasion（plan_013）
  - Scrambled labels（plan_003）
  - Jailbreak MLM / DAPT（plan_017）
  - Wikipedia MLM（plan_018）
  - Topic classification（plan_016v2）
- **建议**: 重新设计架构图，展示 Stage-1 有 7 种 encoder 配置（一个 treatment + 六个 control），然后共享 Stage-2 分类器。或者架构图只保留 treatment pipeline 的详细结构，把 control variants 放到表格/消融实验中展示。

### fig2_cross_attack_bar.pdf（跨攻击柱状图）
- **状态**: 存在（local artifacts）
- **内容**: 只展示 3 个系统（DisPeD / Vanilla DeBERTa / TF-IDF LR）在 IID (Crescendo) / OOD (DD) / OOD (FITD) 上的 F1。**只有 treatment vs vanilla vs tfidf，没有其他 control variants。** 数据来自单 seed（plan_006），不是 3-seed 结果。
- **需要更新**: **YES**
- **原因**:
  1. 缺少所有 control variants（binary, scrambled, MLM, wiki MLM, topic）的 DD OOD 对比
  2. 数据不是最新 3-seed 均值±std
  3. 现有实验结果显示：scrambled (F1=0.99), jailbreak MLM (F1≈0.97), wiki MLM (F1≈0.91), topic (F1≈0.54) 在 DD OOD 上差异显著，这是论文核心 claim 的支撑数据
- **需要包含**: 7 个 variants 在 DD OOD (full) 上的 F1 mean±std（3 seeds），可能还需加 IID 对比

### fig3_strategy_heatmap.pdf（策略转移热力图）
- **状态**: 存在（server results/ + local artifacts）
- **内容**: 3 个子图展示 Crescendo / FITD / Deceptive Delight 的 9×9 策略转移矩阵（raw counts），生成自 `strategy_transition_matrices.json`
- **需要更新**: **NO**
- **原因**: 策略转移矩阵是数据集特征描述，不受模型实验变化影响。数据源（plan_008）未变。

### 其他图表
- **不存在**：fig1_architecture 和 fig2 之外没有其他图表文件
- **paper/ 目录不存在**：尚未开始 LaTeX 论文编写
- **绘图脚本**：只有 `src/plot_strategy_heatmap.py`（生成 fig3）。fig1 和 fig2 是通过 draw-paper-figure skill 在本地生成的，服务器上无对应脚本。

### 总结

| 图表 | 状态 | 需要更新 | 优先级 |
|------|------|---------|--------|
| fig1_architecture | 存在 | YES - 只有 2/7 variants | 中（视论文 framing 决定是否需要全部展示） |
| fig2_cross_attack_bar | 存在 | YES - 缺 control variants + 非 3-seed 数据 | **高**（核心实验结论图） |
| fig3_strategy_heatmap | 存在 | NO | - |

---
