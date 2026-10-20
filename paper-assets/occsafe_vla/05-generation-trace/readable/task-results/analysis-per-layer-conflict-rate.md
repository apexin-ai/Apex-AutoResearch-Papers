# analysis per layer conflict rate

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per_layer_conflict_rate_20260524T134602_result.json`
- **Structured JSON:** [`d7f55d01231027333a44.json`](../../sessions/d7/d7f55d01231027333a44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心发现：

**假设被反转**——late layers 冲突更少，不是更多。

| Encoder | Early | Mid | Late |
|---------|-------|-----|------|
| **DINOv2** | 49.8% | 49.9% | 49.9% |
| **SigLIP** | 49.7% | 49.6% | **25.8%** (Full_OCC) / **25.3%** (Random) |

两个关键模式：

1. **DINOv2 全层均匀 ~50%**：action 和 aux 梯度在所有深度完全正交（等价于随机独立方向），无论 early/late。

2. **SigLIP late layers 冲突率骤降至 ~25%**：siglip_21~24 低至 19-21%，说明 action 和 OCC 辅助梯度在高层语义层是**协同的（aligned）**，而非对抗。逐层看：siglip_18=43% → siglip_20=26% → siglip_22=20% → siglip_25=24%。

论文可用结论：OCC auxiliary loss 不会在 late vision encoder layers 与 action learning 竞争，反而在 SigLIP 高层语义特征空间中两个任务梯度方向趋于一致。Full_OCC 和 Random 表现一致，说明这是结构性特征而非 OCC target 质量的结果。

产出文件：
- `per_layer_conflict_rate.csv` — 完整逐层数据（49层 × 2条件）
- `per_layer_summary.json` — 分组汇总
- Registry `gradient_analysis_mixed_seed.metrics.per_layer_conflict` 已更新

---
