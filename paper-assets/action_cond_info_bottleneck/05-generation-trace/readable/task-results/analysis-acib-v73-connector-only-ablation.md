# analysis acib v73 connector only ablation

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acib_v73_connector_only_ablation_20260518T004901_result.json`
- **Structured JSON:** [`d058df2b9ec6f6bc02e1.json`](../../sessions/d0/d058df2b9ec6f6bc02e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总：

## v73 Connector-Only Ablation 结果

**训练状态**: 正常完成，20k 步，1.9h，final task_loss=0.0397

**Probe A 结果**:

| 测量对象 | Cos Similarity | 结论 |
|----------|---------------|------|
| Connector output | 0.999991 (bit-identical) | Connector 不接收 language，输出天然 language-invariant |
| Untrained scorer importance | 0.999999 | 随机初始化 scorer 不产生有意义的 language 区分 |
| v7.2 trained scorer (对比) | [0.593, 0.944] | 训练后 scorer 产生强 language 依赖 |

**Connector Weight Drift**: 13.7%（v7.2 为 0.4%，因 v73 无 drift regularization）

**结论**: **Probe A cos ≈ 1.0 → 判定 PASS**。Scorer contrastive learning 是 spatial conditioning 的必要组件。仅 connector tuning 不产生 language-dependent features。v7.2 中观察到的 importance map 语言依赖（cos 低至 0.593）完全由 contrastive loss 驱动。

建议 registry: **success** (ablation confirms hypothesis)

---
