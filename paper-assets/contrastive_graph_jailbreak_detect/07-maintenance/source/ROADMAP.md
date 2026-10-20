# contrastive_graph_jailbreak_detect — Research Dashboard

> 最后更新: 2026-05-17 08:04 UTC | 更新原因: MVP 两轮 FAIL，项目 KILL

## 核心方向
~~Supervised contrastive graph learning on tool-call dependency graphs for compositional jailbreak detection.~~

**状态: KILLED (D002)**

## Kill 原因
核心假设 "graph structure provides discriminative signal beyond hand-crafted features" 两轮验证均 FAIL:
- Round 1 (one-hot): GIN 0.845 < RF 0.862
- Round 2 (semantic): GIN 0.848 < RF 0.962
- 根因: STAC 84.7% 攻击链仅 2-3 步，61.5% 图有 0 条边，GNN 无结构可学

## 经验教训
Graph learning 项目立项前必须验证数据的图结构特性（节点数/边数/密度分布）。2-3 节点 + 无边 = graph learning 无增量价值。

## GPU 预算
2× RTX 5090 已释放（使用约 3 GPU-hours）。

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D002 | 2026-05-17 | KILL — 核心假设两轮验证均 FAIL，图结构在 STAC 数据上不具备判别性 | exp_001, exp_003 |
| D001 | 2026-05-17 | MVP Round 1 FAIL → Pivot 到语义 embedding 重跑 final ga | exp_001, exp_002 |


