# analysis v2 gradient analysis

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v2_gradient_analysis_20260526T100632_result.json`
- **Structured JSON:** [`b5a1eaf797d17df1a776.json`](../../sessions/b5/b5a1eaf797d17df1a776.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

V2 梯度分析完成。核心结果：

## V2 Gradient Analysis Summary

| Metric | Vanilla | Full OCC | Detach |
|---|---|---|---|
| Action grad norm | 0.584 | 0.531 | 0.753 |
| OCC grad norm | N/A | 0.008 | 0.005 |
| OCC/Action ratio | N/A | 1.45% | 0.66% |
| Cosine sim (act vs OCC) | N/A | **-0.001** | **0.000** |
| Conflict rate | N/A | **49.95%** | **49.98%** |
| DINOv2/SigLIP ratio | 1.025 | 1.043 | 1.038 |
| Projector action grad | 148.7 | 130.7 | 172.1 |

## V1 (D042) vs V2 关键对比

| Metric | V1 D042 | V2 |
|---|---|---|
| Detach/Vanilla action grad ratio | **0.04** (4%) | **1.29** (129%) |
| Cosine sim (OCC vs action) | **≈ 0** | **≈ 0** ✓ |
| Conflict rate | **≈ 44%** | **≈ 50%** |

## 关键发现

1. **Cosine similarity ≈ 0 在 v2 中保持不变** — OCC 和 action 梯度在 patch_features 上几乎完全正交，无论是 Full OCC 还是 Detach 配置。

2. **Conflict rate ≈ 50% (vs v1 的 44%)** — v2 更接近纯随机（50% = 两个独立随机向量的预期冲突率）。这强化了"existence regularization"结论：OCC head 的梯度信号与 action 完全独立。

3. **Detach/Vanilla 梯度比值剧变: v1=0.04 → v2=1.29** — 这是最大的差异。v1 中 Detach 的 action 梯度只有 Vanilla 的 4%，但 v2 中 Detach 甚至比 Vanilla 更大（129%）。这说明 v2 的 Detach 模型不再表现出 v1 的"梯度抑制"现象。

4. **OCC 梯度极小** — Full OCC 的 OCC/action 梯度比只有 1.45%，Detach 更小（0.66%）。OCC head 对共享视觉表征的梯度影响微乎其微。

5. **DINOv2 vs SigLIP 均衡** — 两个 backbone 上 action 梯度几乎相等（ratio ≈ 1.03-1.04），无明显偏向。

**结论**: v2 保持"existence regularization"模式（cosine≈0, 梯度独立），但不再有 v1 的异常梯度抑制。v2 下 Full OCC BN 的梯度分配是"温和"的，不是"病理性"的。

---
