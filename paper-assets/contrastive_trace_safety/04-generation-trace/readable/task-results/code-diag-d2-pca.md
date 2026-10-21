# code diag d2 pca

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_diag_d2_pca_20260516T193417_result.json`
- **Structured JSON:** [`d7f0ea1a1b024b8c5d68.json`](../../sessions/d7/d7f0ea1a1b024b8c5d68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D2 完成。结果：

| Layer | Fisher(原始4096d) | Fisher(PCA-3d) | 方差解释率 |
|-------|-------------------|----------------|-----------|
| 12    | 17.46             | 0.953          | 16.6%     |
| 14    | 17.88             | 0.928          | 17.0%     |
| 20    | 18.61             | 0.920          | 16.6%     |
| 24    | 18.11             | **1.111**      | 15.9%     |

关键发现：
- 原始高维空间 Fisher ratio 很高（17-18），但这是高维空间的常见现象
- PCA 投影到 3 维后 Fisher ratio 约 0.9-1.1，**分离度真实但不强**
- Top-3 PC 仅解释 16-17% 方差——信号分散在多个维度，不集中在主成分上
- Layer 24 在 PCA 空间分离度最好（1.111），与 D1 中 layer 14 的 accuracy 最佳并不矛盾（线性探针可利用全部维度）

结论：pre/post-commitment 信号存在但分布式，符合 D1 中 78-81% 的中等准确率。4 张图已保存到服务器 `artifacts/diagnostics/`。

---
