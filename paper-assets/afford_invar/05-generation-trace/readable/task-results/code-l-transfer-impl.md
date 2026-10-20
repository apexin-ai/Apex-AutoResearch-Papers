# code l transfer impl

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_l-transfer-impl_20260519T220356_result.json`
- **Structured JSON:** [`1ab8d80384d5a43ed5a5.json`](../../sessions/1a/1ab8d80384d5a43ed5a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出总结

### 实现的文件

| 文件 | 位置 | 说明 |
|------|------|------|
| `affordance_decoder.py` | `prismatic/models/` | 添加 `forward_with_features()` 方法，返回 heatmap + 64-ch 中间特征 |
| `pair_index.py` | `prismatic/training/` | `InstructionPairIndex`: 用 SigLIP 预计算指令对相似度矩阵，支持 build/save/load |
| `transfer_loss.py` | `prismatic/training/` | `TransferPairMiner` (特征队列 + 正负样本挖掘) + `AffordanceTransferLoss` (InfoNCE) |
| `finetune_afford_transfer.py` | `vla-scripts/` | Path B 训练入口，替换 L_consist 为 L_transfer |
| `test_transfer.py` | `tests/` | 7 个单元测试，全部通过 |

### L_transfer 公式

```
z_i = L2_normalize(global_avg_pool(decoder_features_i))   # (B, 64)
z_j = L2_normalize(global_avg_pool(decoder_features_j))   # positive from queue

L_transfer = -log( exp(z_i·z_j / τ) / (exp(z_i·z_j / τ) + Σ_k exp(z_i·z_k / τ)) )
```
- τ = 0.07, 正样本: SigLIP cosine sim > 0.85 的跨物体指令对
- 负样本: 队列中所有非正样本特征 (queue_size=256, max_neg=64)
- 特征来源: AffordanceDecoder 第二层 ConvTranspose 后的 64-ch 特征 (softmax 之前)

### 与现有代码的兼容性

- **`forward()` 完全不变** — Phase 1 训练不受影响，checkpoint 兼容
- `forward_with_features()` 是纯新增方法，内部遍历同一个 `up_blocks` Sequential
- 训练脚本是独立的 `finetune_afford_transfer.py`，不修改正在运行的 `finetune_afford.py`
- 复用了 `heatmap_entropy_loss` (from consistency_loss.py)、`AffordRLDSBatchTransform`、`AffordCollator` 等

### 相比 L_consist 的效率优势

L_transfer **不需要额外的 VLA forward pass**。特征来自队列（detached），每步只做 1 次 VLA forward + 1 次 decoder forward_with_features，比 L_consist 的 K+1 次 VLA forward 快约 3-4 倍。

### 启动 Path B

```bash
cd /root/afford_invar/openvla-oft
torchrun --nproc_per_node 1 vla-scripts/finetune_afford_transfer.py \
  --beta 0.1 --transfer_temperature 0.07 --queue_size 256
```

---
