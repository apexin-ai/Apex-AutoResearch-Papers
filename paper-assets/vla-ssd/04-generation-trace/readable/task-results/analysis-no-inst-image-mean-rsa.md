# analysis no inst image mean rsa

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_no_inst_image_mean_rsa_20260515T231839_result.json`
- **Structured JSON:** [`182d95c29fbf4817b1ae.json`](../../sessions/18/182d95c29fbf4817b1ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。结果：

**image_mean RSA (no-inst)**

| 条件 | Peak RSA | Peak Layer |
|------|----------|------------|
| trained_no_inst | **0.5014** | 23 |
| untrained_no_inst | **0.4817** | 29 |

**完整 2×2 matrix (image_mean RSA)**：

|  | with_inst | no_inst |
|--|-----------|---------|
| **trained** | 0.5014 (L23) | 0.5014 (L23) |
| **untrained** | 0.4847 (L23) | 0.4817 (L29) |

注意 trained_no_inst 的 image_mean RSA 和 trained_with_inst 完全相同（0.5014, L23）——这是因为 `image_mean` 是对所有 image token 取均值，在 trained 模型中 image token 表征不受 instruction 是否存在的影响（layer 0 两者完全一致也验证了这点）。untrained_no_inst（0.4817）比 untrained_with_inst（0.4847）略低，且 peak layer 从 23 移到 29。

结果文件：`/root/autodl-tmp/vla-ssd/results/rsa/rsa_image_mean_no_inst.json`

---
