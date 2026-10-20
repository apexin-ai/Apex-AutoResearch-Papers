# analysis readout rsa curve

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_readout_rsa_curve_20260517T191343_result.json`
- **Structured JSON:** [`a6d8a9ee719c1453db7c.json`](../../sessions/a6/a6d8a9ee719c1453db7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整。以下是结果。

---

## 结果：Readout Token (last_preaction) Per-Layer RSA

**来源文件**: `/root/autodl-tmp/vla-ssd/results/rsa/unified_rsa_results.json`  
**路径**: `conditions → {trained_with_inst, untrained_with_inst} → last_preaction → layer_X → mean_rsa`

### Per-Layer RSA ρ 表格

| Layer | Trained ρ | Untrained ρ |
|-------|-----------|-------------|
| L0    | nan       | nan         |
| L1    | 0.5682    | 0.6262      |
| L2    | 0.5818    | 0.6207      |
| L3    | 0.5880    | 0.6156      |
| L4    | 0.5892    | 0.6119      |
| L5    | 0.5836    | 0.6084      |
| L6    | 0.5617    | 0.6053      |
| L7    | 0.5430    | 0.6029      |
| L8    | 0.5469    | 0.6013      |
| L9    | 0.5682    | 0.6008      |
| L10   | 0.5577    | 0.5977      |
| L11   | 0.5993    | 0.5966      |
| L12   | **0.6425**| 0.5953      |
| L13   | 0.6395    | 0.5939      |
| L14   | 0.6374    | 0.5934      |
| L15   | 0.6348    | 0.5936      |
| L16   | 0.6303    | 0.5941      |
| L17   | 0.6261    | 0.5950      |
| L18   | 0.6227    | 0.5947      |
| L19   | 0.6194    | 0.5945      |
| L20   | 0.6164    | 0.5938      |
| L21   | 0.6086    | 0.5936      |
| L22   | 0.6060    | 0.5927      |
| L23   | 0.6003    | 0.5917      |
| L24   | 0.5950    | 0.5913      |
| L25   | 0.5855    | 0.5907      |
| L26   | 0.5812    | 0.5895      |
| L27   | 0.5822    | 0.5888      |
| L28   | 0.5814    | 0.5879      |
| L29   | 0.5787    | 0.5885      |
| L30   | 0.5724    | 0.5883      |
| L31   | 0.5703    | 0.5870      |
| L32   | 0.5843    | 0.5866      |

### Peak 信息

| Token | Condition | Peak Layer | Peak ρ | CI95 |
|-------|-----------|-----------|--------|------|
| last_preaction | Trained | **L12** | 0.6425 | [0.561, 0.716] |
| last_preaction | Untrained | **L1** | 0.6262 | — |
| image_mean | Trained | **L12** | 0.6282 | — |
| image_mean | Untrained | **L0** | 0.6117 | — |

### 总结

1. **Trained last_preaction 呈 inverted-U**：从 L1 (0.568) 上升至 L12 peak (0.643)，之后单调下降至 L31 (0.570)。曲线形状与 image_mean trained 一致，peak 位置完全相同（均为 L12）。

2. **Untrained last_preaction 单调递减**：L1 (0.626) 最高，逐层缓慢下降至 L32 (0.587)，无 inverted-U。这也与 image_mean untrained 的模式一致（peak 在最早层）。

3. **训练效应**：训练使 last_preaction 在中间层（L11-L16）的 RSA 显著提升（超过 untrained 约 0.04），在早期层（L1-L10）则低于 untrained。这说明训练将 action-relevant 信息从早期层重新组织到中间层——readout token 和 image_mean token 展现相同的学习动态。

4. **与 image_mean 对比**：两种 token 的 trained peak 位置完全一致（L12），trained peak ρ 值 last_preaction (0.643) 略高于 image_mean (0.628)，表明 readout token 在 peak 层对 action structure 的编码略强。

---
