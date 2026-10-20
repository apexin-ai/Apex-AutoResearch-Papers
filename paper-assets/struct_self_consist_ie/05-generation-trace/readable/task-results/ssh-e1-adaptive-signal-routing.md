# ssh e1 adaptive signal routing

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_e1-adaptive-signal-routing_20260520T093508_result.json`
- **Structured JSON:** [`7db58718d3ee26f56e1d.json`](../../sessions/7d/7db58718d3ee26f56e1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

E1 完成。结果总结：

**数据**: 16 configs (Qwen3-8B FT × 7, Qwen2.5-72B ZS × 3, Qwen2.5-72B FS × 3, Qwen2.5-7B FT × 3)，0 missing。先用 `compute_signals.py` 为缺少 signal report 的 10 个 config 补算了完整建构方法 F1。

**Label 分布** (5-class): lp_selection=6, none=5, consensus_theta2n=3, consensus_lp_weighted=1, majority_vote=1

**最佳模型: RandomForest (5-class)**
| 指标 | 值 |
|------|-----|
| LOO Accuracy | **56.2%** (9/16) — 未达 60% 目标 |
| Router avg ΔF1 | **+0.39 pp** |
| Always-LP ΔF1 | +0.15 pp |
| Oracle ΔF1 | +0.56 pp |

**Router ΔF1 > Always-LP ΔF1** ✓ (2.6× 提升，达标)

**关键发现**:
- **FT + 低退化 (SciERC)**: consensus_theta2n 最优
- **FT + 高退化 (CoNLL)**: greedy 已最优 (none)
- **FT + 中退化 (FewNERD)**: lp_selection 或 consensus 都有效
- **72B ZS/FS**: 结果分散，是主要误分类来源
- **Top features**: oracle_headroom, degeneracy_rate, base_f1 — 退化率和 headroom 是最强预测因子

**为什么 accuracy < 60%**: 16 个 config 中 5 个 class，其中 2 个 class 只有 1 个样本 (consensus_lp_weighted, majority_vote)；72B configs 之间差异大但数量少。3-class 简化版 (合并 consensus) 结果相同。

产出已保存至 `/root/autodl-tmp/struct_self_consist_ie/artifacts/e1_signal_routing/routing_results.json`。

---
