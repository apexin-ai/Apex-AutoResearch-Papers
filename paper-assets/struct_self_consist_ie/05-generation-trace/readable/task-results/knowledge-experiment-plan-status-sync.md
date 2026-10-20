# knowledge experiment plan status sync

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_experiment-plan-status-sync_20260520T003006_result.json`
- **Structured JSON:** [`690b8f0cee9fc32d704c.json`](../../sessions/69/690b8f0cee9fc32d704c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 一致性报告

### 1. experiment_plan.yaml vs Registry 差异

**4 个 RUNNING 实验全部不在 experiment_plan.yaml 中：**

| 实验 ID | Registry 状态 | Plan 中是否存在 | 备注 |
|---------|-------------|----------------|------|
| `exp_qwen25_72b_fewshot` | RUNNING (updated 05-19 17:42) | **缺失** | 无进度/ETA 记录 |
| `exp_qwen25_7b_fewnerd` | RUNNING, 0.7% (registry 过时) | **缺失** | 任务称 88.8%，registry 停在 05-19 11:36 |
| `exp_qwen25_14b_fewnerd` | RUNNING, 15.7% (registry 过时) | **缺失** | 任务称 53.0%，registry 停在 05-19 12:47 |
| `exp_qwen25_32b_fewnerd` | RUNNING, 5.3% (registry 过时) | **缺失** | 任务称 37.3%，registry 停在 05-19 11:36 |

### 2. Registry 进度严重滞后

所有 4 个实验的 registry 进度与任务提供的最新进度差距巨大（registry 最后更新在 05-19，已过去 ~12-24 小时）。任务给出的进度远高于 registry 记录。

### 3. 后续步骤（signals/construction）计划条目

**Plan 中无任何关于 7B/14B/32B 推理后续步骤的条目。** 具体缺失：
- 7B/14B/32B FewNERD 推理完成后的 signals 计算步骤
- `analyze_fewnerd_results.py` 运行条目
- `wnut17_entity_construction.py` 运行条目
- `format_for_scaling.py` 触发条目
- 跨模型规模 scaling 分析汇总条目

Plan 中现有的 Few-NERD 条目（exp-020 `fewnerd_smoke`、exp-021 `fewnerd_full`）是针对 Qwen3-8B 的，与当前 Qwen2.5 多规模 scaling 实验无关。

### 总结

1. **Plan 完全缺失这 4 个 scaling 实验**——它们是在 plan 之外启动的，需要补充条目
2. **Registry 进度过时**——4 个实验的进度/ETA 均需更新
3. **后续 pipeline 步骤无计划**——7B/14B/32B 训练完成后的推理、信号计算、scaling 分析均无对应条目，存在流程断档风险

---
