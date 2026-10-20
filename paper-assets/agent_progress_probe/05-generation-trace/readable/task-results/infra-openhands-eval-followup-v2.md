# infra openhands eval followup v2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_openhands-eval-followup-v2_20260514T115335_result.json`
- **Structured JSON:** [`78afac4371b707652965.json`](../../sessions/78/78afac4371b707652965.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 probe 的 cross-agent 评估都完成了。汇总结果：

---

## Cross-Agent Zero-Shot 评估结果

### GRU Probe 性能

| Probe | Macro-F1 | Accuracy | F1(stag) | F1(prog) | SWE-agent 内部 Macro-F1 | Delta |
|-------|----------|----------|----------|----------|------------------------|-------|
| conf≥2 (checkpoints/) | **0.5280** | 0.7640 | 0.1943 | 0.8617 | 0.9055 | -0.3775 |
| conf≥0 (checkpoints_full/) | **0.5298** | 0.8344 | 0.1513 | 0.9082 | 0.8468 | -0.3170 |

### 核心发现

**Cross-agent transfer 失败**（< 0.70 阈值）。两个 probe 的 Macro-F1 都仅约 0.53。

**Failure mode 分析：**
- **Stagnation F1 极低**（0.15–0.19）：probe 几乎无法检测 OpenHands 的 stagnation，大量漏检
- **Progress F1 尚可**（0.86–0.91）：但这主要因为 OpenHands 数据严重不平衡（progress 93.4%, stagnation 6.6%），几乎全预测 progress 就能获得高 progress-F1
- conf≥0 probe accuracy 更高（0.83 vs 0.76），但这只是因为它更倾向预测 progress（在不平衡数据上 accuracy 虚高）
- 两个 probe 表现几乎相同，conf≥2 筛选没有带来迁移优势

**根因**：SWE-agent 的 stagnation 行为模式（action embedding 空间分布）与 OpenHands 差异大。SWE-agent stagnation 比例 ~36%，OpenHands 仅 ~6.6%，action 分布差异导致 probe 学到的 stagnation 特征不可迁移。

### Baselines 对比

所有传统 baseline（Random/Majority/CosineSim/Repeat-3）Macro-F1 都在 0.43–0.49 之间，probe 的 0.53 仅略优于随机。LF Oracle（file_diff_delta 单 LF）在 OpenHands 上达到 0.9582，说明标注函数本身跨 agent 迁移性远优于 learned probe。

---
