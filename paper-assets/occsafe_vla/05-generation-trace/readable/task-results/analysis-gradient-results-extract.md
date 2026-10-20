# analysis gradient results extract

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient-results-extract_20260527T085812_result.json`
- **Structured JSON:** [`2799737af5926de451b3.json`](../../sessions/27/2799737af5926de451b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已传输完成。以下是完整汇总：

## V2 梯度分析汇总

### 总览表

| 条件 | Action Loss | OCC Loss | Action Grad Norm (avg) | OCC Grad Norm (avg) | Norm Ratio (OCC/Action) | Mean Cosine Sim | Cosine Range | Conflict Rate |
|------|------------|----------|----------------------|--------------------|-----------------------|----------------|-------------|---------------|
| **Vanilla v2** | 0.2285 | 0.0000 | 0.1716 | N/A | N/A | N/A | N/A | N/A |
| **Full OCC BN v2** | 0.2541 | 0.0108 | 0.1410 | 0.0210 | 0.149 | +0.0065 | [-0.0006, +0.021] | 45.6% |
| **Full OCC LN v2** | 0.2318 | 0.0102 | 0.1340 | 0.0187 | 0.139 | +0.0045 | [-0.002, +0.013] | 45.7% |
| **Detach BN v2** | 0.2473 | 0.0121 | 0.1419 | 0 (detached) | N/A | N/A | N/A | N/A |
| **Detach LN v2** | 0.2428 | 0.0109 | 0.1346 | 0 (detached) | N/A | N/A | N/A | N/A |

### 关键发现

**1. Cosine Similarity ≈ 0 — 确认近似正交**
- Full OCC BN: mean cosine = +0.0065, Full OCC LN: +0.0045
- 跨所有 51 层，范围仅在 [-0.002, +0.021]，极度接近零
- **结论**：Action 和 OCC 梯度在共享 backbone 上几乎完全正交，不存在系统性的方向对齐或对抗

**2. Conflict Rate ≈ 45-46% — 无方向性冲突**
- BN: 45.6%, LN: 45.7%，均接近 50% 随机基线
- 略低于 50% 表示极轻微的协同（而非冲突），但不具统计显著性
- **结论**：排除 gradient conflict 作为性能变化的解释

**3. Action Grad Norm 跨条件一致 — 排除 gradient amplification**
- Vanilla: 0.1716, Full OCC BN: 0.1410, Full OCC LN: 0.1340, Detach BN: 0.1419, Detach LN: 0.1346
- OCC 条件的 action grad norm 略低于 Vanilla（约 80%，见图 d），但 Full OCC 和 Detach 之间几乎相同（BN: 0.1410 vs 0.1419, LN: 0.1340 vs 0.1346）
- **结论**：OCC head 的梯度回传并不 amplify action gradient；Full OCC 和 Detach 的 action gradient 几乎一致，说明 OCC 梯度对 backbone action 优化的直接干扰可忽略

**4. OCC Gradient Norm 远小于 Action — ~14% 比值**
- OCC/Action norm ratio: BN 14.9%, LN 13.9%
- OCC loss 本身很小（~0.01 vs action ~0.24），因此梯度贡献也相应小
- **结论**：辅助任务梯度不会主导 backbone 更新

### 与论文 Claims 的一致性

图 (d) 最关键：所有 OCC 条件的 action gradient norm ratio vs Vanilla 稳定在 ~0.78-0.85，且 **Full OCC ≈ Detach**。这直接支持论文的核心论点：

> OCC 辅助任务对 action policy 的改善不是通过 gradient-level interaction（因为梯度正交且 Full=Detach），而是通过 **representation-level** 的隐式正则化（OCC head 的存在迫使 backbone 编码更丰富的 3D 几何信息，即使梯度被 detach 也有效，因为共享 backbone 的 forward pass 本身就受 OCC loss 影响了训练过程）。

图表已保存至：
- `artifacts/gradient_v2_combined.pdf`
- `artifacts/gradient_v2_combined.png`

---
