# data fig5 per conv extract

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_fig5_per_conv_extract_20260520T112923_result.json`
- **Structured JSON:** [`8fcb537f98e77a63a446.json`](../../sessions/8f/8fcb537f98e77a63a446.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据如下：

## Gen N=5 (v7, generative decoding)

| β | GAR mean | GAR std | PPL mean | PPL std |
|---|----------|---------|----------|---------|
| 0.0 | 0.0285 | 0.0140 | 1.409 | 0.118 |
| 0.5 | 0.0328 | 0.0082 | 1.387 | 0.111 |
| 1.0 | 0.0444 | 0.0074 | 1.360 | 0.101 |
| 2.0 | 0.0749 | 0.0107 | 1.411 | 0.124 |
| 5.0 | 0.6971 | 0.0198 | 1.908 | 0.357 |
| 10.0 | 0.9588 | 0.0028 | 4.220 | 0.988 |

Per-conversation breakdown (Gen):

| β | conv0 | conv1 | conv2 | conv3 | conv4 |
|---|-------|-------|-------|-------|-------|
| **GAR** | | | | | |
| 0.0 | 0.0205 | 0.0308 | 0.0150 | 0.0249 | 0.0512 |
| 0.5 | 0.0264 | 0.0367 | 0.0251 | 0.0308 | 0.0450 |
| 1.0 | 0.0328 | 0.0517 | 0.0481 | 0.0421 | 0.0472 |
| 2.0 | 0.0601 | 0.0763 | 0.0891 | 0.0700 | 0.0789 |
| 5.0 | 0.6897 | 0.7246 | 0.7012 | 0.6699 | 0.7000 |
| 10.0 | 0.9560 | 0.9565 | 0.9626 | 0.9586 | 0.9605 |
| **PPL** | | | | | |
| 0.0 | 1.459 | 1.421 | 1.529 | 1.213 | 1.424 |
| 0.5 | 1.469 | 1.367 | 1.498 | 1.214 | 1.388 |
| 1.0 | 1.358 | 1.392 | 1.473 | 1.197 | 1.380 |
| 2.0 | 1.403 | 1.446 | 1.486 | 1.202 | 1.517 |
| 5.0 | 1.741 | 2.074 | 2.009 | 1.390 | 2.328 |
| 10.0 | 3.066 | 5.795 | 4.223 | 4.038 | 3.979 |

## TF N=200 (eval200, teacher-forcing)

| β | GAR mean | GAR std | PPL mean | PPL std |
|---|----------|---------|----------|---------|
| 0.0 | 0.5215 | 0.0745 | 2.618 | 0.819 |
| 2.0 | 0.5969 | 0.0750 | 2.688 | 0.845 |
| 3.0 | 0.7769 | 0.0466 | 2.931 | 0.969 |
| 4.0 | 0.8088 | 0.0450 | 3.490 | 1.507 |
| 5.0 | 0.8275 | 0.0489 | 6.148 | 11.108 |
| 10.0 | 0.9715 | 0.0148 | 505.210 | 463.107 |

注意：Gen 和 TF 的 beta 取值范围不同（Gen 有 0.5/1.0，TF 有 3.0/4.0）。β=10 在 TF 下 PPL 爆炸（505±463），说明过度 steering 在 teacher-forcing 下灾难性退化。Gen 模式下 β=5 已经把 GAR 推到 ~0.70 而 PPL 仅 ~1.9，是一个合理的 trade-off 拐点。

---
