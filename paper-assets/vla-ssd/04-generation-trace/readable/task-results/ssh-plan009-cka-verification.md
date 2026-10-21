# ssh plan009 cka verification

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan009-cka-verification_20260515T234351_result.json`
- **Structured JSON:** [`a06d78aad445ab27b727.json`](../../sessions/a0/a06d78aad445ab27b727.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CKA verification 完成。结果总结：

## 结果

### Linear CKA (frame-level, features vs 7-DoF actions)
| Source | CKA |
|--------|-----|
| untrained image_mean L23 | **0.0894** |
| trained image_mean L23 | 0.0834 |
| projector | 0.0809 |
| DINO | 0.0664 |
| trained last_preaction L32 | **0.1270** |

### RDM CKA (demo-level kernel CKA)
| Source | CKA |
|--------|-----|
| trained image_mean L23 | **0.2599** |
| projector | 0.2568 |
| untrained image_mean L23 | 0.2464 |
| DINO | 0.2408 |
| trained last_preaction L32 | **0.2898** |

### 与 RSA 对比
| | RSA | Linear CKA | RDM CKA |
|--|-----|------------|---------|
| #1 | projector (0.615) | untrained (0.089) | trained (0.260) |
| #2 | trained (0.501) | trained (0.083) | projector (0.257) |
| #3 | untrained (0.485) | projector (0.081) | untrained (0.246) |
| #4 | DINO (0.388) | DINO (0.066) | DINO (0.241) |

### 分析

**一致的发现：**
- DINO 在所有三种指标中都是最低 → robust
- trained last_preaction (L32) 的 CKA 远高于 image_mean → 与 RSA 一致，last token 比 image tokens 更 action-aligned
- Per-layer CKA 趋势：later layers > earlier layers → 与 RSA per-layer curve 方向一致

**不一致之处：**
- **Linear CKA** 的 ranking (untrained > trained > projector) 与 RSA 相反。原因：linear CKA 直接比较 4096-D features vs 7-D actions，维度严重不匹配导致 CKA 值极低 (0.06-0.13)，条件间差异在噪声量级内
- **RDM CKA** 中 trained (0.2599) 和 projector (0.2568) 近乎打平（差 0.003），而 RSA 中 projector 明显领先 (0.615 vs 0.501)。这说明 projector 的优势在 CKA 度量下被压缩了

**结论**: CKA 部分验证了 RSA 发现——DINO 最弱和 per-layer 趋势都 robust。但 projector vs trained 的排序在指标间不完全一致：RSA 强调 projector 优势，RDM CKA 显示二者接近。Linear CKA 因维度不匹配不适合直接比较，不作为主要证据。

---
