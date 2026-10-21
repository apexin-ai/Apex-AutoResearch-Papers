# ssh rsa analysis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rsa-analysis_20260515T194627_result.json`
- **Structured JSON:** [`9ba6c3fa84c6dc3560a4.json`](../../sessions/9b/9ba6c3fa84c6dc3560a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量运行完成。结果已保存到 `/root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json`。

## RSA 结果摘要

### Per-layer RSA (Spearman corr: representation dissimilarity vs action dissimilarity)

| 趋势 | 数值 |
|------|------|
| Trained peak RSA | 0.4876 (layer 9) |
| Untrained peak RSA | 0.4846 (layer 12) |
| DINO RSA (constant) | 0.3880 |
| Trained > Untrained | 仅 4/33 层 (layers 2, 6, 9, 32) |
| T-U Delta 范围 | -0.0722 ~ +0.0109 |

### Per-phase RSA (均值跨层)

| Phase | Trained | Untrained | DINO |
|-------|---------|-----------|------|
| early | 0.3197 | **0.4148** | 0.4909 |
| mid | 0.5231 | **0.5248** | 0.4132 |
| late | **0.4758** | 0.4592 | 0.2601 |

### CKA (Trained vs Untrained)
CKA 从 layer 1 的 0.687 持续上升到 layer 26 的 0.860，表明 trained 和 untrained 的表征在深层高度相似。

### Gates
- **G1 FAIL**: peak delta = +0.003 (阈值 0.05)
- **G2 FAIL**: trained > untrained 仅 4/33 层

### 关键发现
1. **VLA training 并未改善 action-relevant 表征结构**——在绝大多数层中 untrained RSA 反而略高于 trained。
2. **Untrained VLA 的 RSA 非常稳定**（~0.48 跨所有层），而 trained VLA 的 RSA 在深层（20-28）明显下降（~0.41-0.44），提示 training 可能引入了 action 无关的变异。
3. **Temporal phase 差异**：trained 在 late phase 优于 untrained（0.4758 vs 0.4592），但在 early phase 远逊（0.3197 vs 0.4148）。
4. **DINO 在 early phase 最强**（0.4909），在 late phase 最弱（0.2601），与 VLA 互补。

---
