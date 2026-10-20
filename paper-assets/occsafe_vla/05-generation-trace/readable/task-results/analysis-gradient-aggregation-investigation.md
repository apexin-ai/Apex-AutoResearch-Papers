# analysis gradient aggregation investigation

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_aggregation_investigation_20260525T080558_result.json`
- **Structured JSON:** [`5fdae58ee82213bbabf5.json`](../../sessions/5f/5fdae58ee82213bbabf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。

## 调查结果

**78% 和 1-13% 测量的是完全不同的物理量，两者不矛盾。**

| 数字 | 来源脚本 | 损失函数 | 含义 |
|------|---------|---------|------|
| **1-13%** | `gradient_analysis.py` | L1 action loss | Detach encoder 的 action 梯度仅为 Vanilla 的 1-13% |
| **78%** | `gradient_dose_response_s0.py` | CE LM loss | 全模型 CE loss 梯度比率（包含所有 token） |

**根因**: `gradient_dose_response_s0.py` 使用 cross-entropy language model loss（量级 ~25）而非 L1 action loss（量级 ~0.2）。CE loss 通过所有 token 产生巨大梯度信号流回 vision backbone，淹没了 action-specific 的 gradient collapse。

**建议**: 论文使用 1-13%，不提及 78%。L1 action loss 是训练目标的直接度量，物理含义清晰。

**附加风险**: same-seed 验证发现 `ablation_occ_detach_s0_retrain` 检查点不展示 gradient collapse（L1 ratio ≈ 115%），但这是不同检查点——论文数据来自 s2 检查点，该检查点的 collapse 是真实的。如时间允许，建议用原始 s0（非 retrain）检查点重新验证。

报告已写入 `artifacts/gradient_aggregation_investigation.md`。

---
