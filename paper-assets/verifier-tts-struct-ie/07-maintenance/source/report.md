# Handover — 2026-05-11

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
（无）

## 近期结论
- **mvp-004-sequential** (negative): Sequential self-refinement（K轮迭代修正）在 SciERC NER 上优于 greedy 和 parallel 聚合，sequential@K≥3 > greedy ≥ 1.0 F1 点 ← 基于 mvp-001
- **mvp-001** (success): 并行 TTS（生成 N 个候选 + 结构自洽性 IoU 聚合）在 SciERC NER 上优于单次 greedy 抽取，self-consistency@N≥8 > greedy@N=1 ≥ 1.0 F1 点
- **mvp-002-re** (negative): RE 有实体对+关系类型的结构约束，self-consistency/freq-merge 在 relation 三元组级别匹配下信号更强，aggregation@N≥8 > greedy ≥ 1.0 F1 点

## 趋势
成功 1 / 负向 3 / 失败 0 / 共 4

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
home-1x5090: 无 GPU 信息
seetacloud-bjb2-structtts: 无 GPU 信息

## 告警
（无）
