# analysis llama layer analysis

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama-layer-analysis_20260512T022207_result.json`
- **Structured JSON:** [`6f31a2c419c5fd030523.json`](../../sessions/6f/6f31a2c419c5fd030523.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出文件在 `/home/sonny/redundancy-compound-sparsity/results/neg_cross_model/analysis/`。

---

**关键发现：**

**1. Llama per-layer r 极其均匀**：32 层 r 范围 0.393–0.485，标准差极小。每一层的 anchor_sim 都与 surprisal 强相关。

**2. DeepSeek 有 11 个弱/负相关层**（r < 0.05）：集中在 L0-3 和 L13-20，这些层直接拖垮了全局 r（0.147）。即使最强的层（L4, r=0.287）也远低于 Llama 的最低值。

**3. 差异最大的区间**：
| Group | Llama r | DeepSeek r | Gap |
|-------|---------|------------|-----|
| Early | 0.450 | 0.128 | +0.322 |
| Mid | 0.434 | 0.072 | **+0.361** |
| Late | 0.472 | 0.130 | +0.342 |

Mid layers gap 最大，因为 DeepSeek L13-17 几乎全是 r≈0 的死区。

**4. Δpert 方向性完全不同**：
- Llama late layers（L20-31）Δpert 平均 +14.3%，信号最强
- DeepSeek mid+late layers Δpert 为 **负值**（−3.3% 到 −3.6%），即 cross-axis 反转

**5. 架构解读**：GQA 的多 KV head 让 anchor_sim 在每层都是可靠的冗余度信号；MLA 的低秩压缩 KV 在 early/mid layers 破坏了这个对应关系。

---
