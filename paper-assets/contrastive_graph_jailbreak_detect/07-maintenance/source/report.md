# Handover — 2026-05-17

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
（无）

## 近期结论
- **exp_003_gin_semantic_mvp** (failed): Semantic MiniLM-L6 node embeddings remove tool-identity shortcut, allowing GIN+SupCon to learn structural patterns and exceed RF by >5pp AUROC on cross-mode holdout (final MVP gate)
- **exp_002_rf_baseline** (failed): Hand-crafted graph features + RF provides a weaker baseline than learned GNN representations, with GIN+SupCon exceeding RF by >5pp AUROC on cross-mode holdout
- **exp_001_gin_supcon_mvp** (failed): GIN+SupCon on tool-call dependency graphs achieves cross-failure-mode holdout AUROC > 0.70, demonstrating that graph structure captures generalizable attack patterns beyond specific failure modes

## 趋势
成功 0 / 负向 0 / 失败 3 / 共 3

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
bjb2-32660: 无 GPU 信息

## 告警
- exp_001_gin_supcon_mvp: 训练失败 — unknown
- exp_002_rf_baseline: 训练失败 — unknown
- exp_003_gin_semantic_mvp: 训练失败 — unknown
