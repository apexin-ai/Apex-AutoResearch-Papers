# code unified rsa recalc

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unified_rsa_recalc_20260516T025219_result.json`
- **Structured JSON:** [`928ed41c7d7cdedf7209.json`](../../sessions/92/928ed41c7d7cdedf7209.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Method B 统一重算完成（6 个 VLA 条件 × 33 层）**

核心数字（image_mean）：

| 条件 | Best Layer | Peak RSA |
|------|-----------|----------|
| trained_with_inst | L12 | **0.6282** |
| untrained_with_inst | L0 | 0.6117 |
| trained_no_inst | L13 | 0.6225 |
| untrained_no_inst | L0 | 0.6106 |

last_preaction: trained L12 = **0.6425**, untrained L1 = 0.6262

Instruction control 4 条件几乎相同（0.6225–0.6283），instruction 内容无影响。

**与 baseline 对比：**
- SigLIP+Projector = 0.615 → VLA trained = 0.6282 (Δ=+0.013，VLA 未退化)
- Trained vs Untrained Δ = +0.017（训练效果小）
- DINO cls = 0.692 仍是最高

**与旧 Method A 对比：** Method B 值一致偏高 ~0.13，但相对排序不变。

JSON 已保存到 `/root/autodl-tmp/vla-ssd/results/rsa/unified_rsa_results.json`，summary 在本地 `artifacts/unified_rsa_summary.md`。

---
