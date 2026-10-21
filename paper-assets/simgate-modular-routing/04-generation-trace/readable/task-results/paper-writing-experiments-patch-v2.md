# paper writing experiments patch v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments-patch-v2_20260514T112358_result.json`
- **Structured JSON:** [`3d04c4b881fe4369a2ba.json`](../../sessions/3d/3d04c4b881fe4369a2ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。v2 draft 已写入并注册 (`art_20260514_0014da`)。变更摘要：

**Table 1 补全：**
- 扩展为 6 列（Score / 90% CI / Succ.% / Death% / Sim%），修正 CI 标签从 95% → 90%（匹配数据源 plan-003-baseline-245eps）
- 新增 Trained Router (Ours) 行：**-10.70** [-15.25, -6.38]，23.7% success，17.6% death，97.0% sim ratio
- 配套新增解读段落：vs always-det Δ = -1.23（方向性负面但不显著），70.6% fallback rate，强化 C1

**Section 3.3 Seed Stability 段落：**
- 4 seeds balanced_acc: 58.1 ± 0.8%（稳定，仅高于随机 8pp）
- internal_recall: 51.52%–81.82%（range > 30pp，极不稳定）
- 解读：弱信号可复现，但决策边界 seed-dependent → 无法产生稳定的非 always-det 策略
- 更新了 Section 3.3 末尾的总结段落，整合 seed stability 证据

---
