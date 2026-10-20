# analysis plan 002 generative v1

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-002-generative-v1_20260514T080716_result.json`
- **Structured JSON:** [`3da1c57d4f5811bc6f14.json`](../../sessions/3d/3da1c57d4f5811bc6f14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，结果已写入 `artifacts/plan-002-generative-v1-analysis.md`。

**核心发现**:

1. **训练成功完成**，loss 收敛健康：5.44 → 0.20，eval_loss 持续下降（0.39 → 0.28 → 0.26），无过拟合
2. **Checkpoint 完整**：final_adapter (25.7MB) + 2 个中间 checkpoint
3. **⚠️ 关键缺陷：internal_recall 未知**。`compute_metrics` 函数已定义但**未传入 Trainer**，训练期间只输出了 eval_loss，没有 routing_acc / internal_recall / det_recall
4. **结论: PENDING** — 无法判定 success/negative，需要单独跑 eval 子命令

**下一步**: 需要运行 `python src/training/generative_router_sft.py eval --adapter_path checkpoints/plan-002-generative-v1/final_adapter ...` 来获取实际路由指标，与 ablation-b (internal_recall=51.5%) 对比。是否现在跑 eval？

---
