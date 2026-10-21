# exp death proximal labeling router

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_death-proximal-labeling-router_20260519T162129_result.json`
- **Structured JSON:** [`90e57b913138f34e3035.json`](../../sessions/90/90e57b913138f34e3035.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。

**结论：负面结果。** 5 个模型（full, k10, k5, k3, k1）全部对 internal 类别 0% recall，Step BA(all) ≈ 0.50，Episode BA = 0.50。

**根本原因**：death_asymmetry episode 是单类的（全部标为 deterministic），death-proximal 过滤只减少 deterministic 样本，不改善类别平衡（10.3% → 13.4% internal 比例变化微乎其微）。9:1 的类别不平衡导致模型学会全预测 deterministic。

**已完成**：
- 5 个模型训练 + 评估（修复了 Qwen3 thinking token 解析 bug）
- 结果报告写入 `artifacts/death-proximal-labeling-router/`
- Registry 更新为 DONE (negative)，含完整 metrics
- Memory 记录教训

---
