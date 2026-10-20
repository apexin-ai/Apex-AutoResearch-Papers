# Handover — 2026-05-15

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
（无）

## 近期结论
- **entail_001** (failed): Claim-level entailment check（premises + prior claims ⊢ claim）能区分正确和错误推理链（Cohen's d > 0.15）
- **mvp_003** (negative): Z3 subprocess 隔离 + 量词修复 + PCV 后，IC 能区分正确和错误推理链
- **mvp_002** (failed): 量词修复 + PCV 后，Z3 IC 能区分正确和错误推理链（正确链 IC 显著高于错误链）

## 趋势
成功 0 / 负向 1 / 失败 2 / 共 4

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
autodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3

## 告警
- mvp_001: 已被终止 — unknown
- mvp_002: 训练失败 — unknown
- entail_001: 训练失败 — unknown
