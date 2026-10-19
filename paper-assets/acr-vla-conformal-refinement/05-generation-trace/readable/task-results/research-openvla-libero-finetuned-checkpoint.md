# research openvla libero finetuned checkpoint

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_openvla-libero-finetuned-checkpoint_20260519T163003_result.json`
- **Structured JSON:** [`aa15b85ed1696431a7e7.json`](../../sessions/aa/aa15b85ed1696431a7e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/openvla_libero_weight_investigation.md`。核心结论：

**1. 之前从未跑过 OpenVLA eval。** 服务器上无 OpenVLA 权重，代码中零引用。`vla_only` 10% SR 是 SmolVLA K=1 baseline。

**2. LIBERO fine-tuned 权重已找到：**
- 官方 `openvla/openvla-7b-finetuned-libero-object` → **88.4% SR**（LoRA, 离散 256-bin actions）
- OFT `moojink/openvla-7b-oft-finetuned-libero-object` → **98.4% SR**（连续 L1 回归, action chunk=8）

**3. 代码适配：** 只跑 baseline eval 不需改我们代码，直接用 OpenVLA 官方 eval 脚本。接 CRM 需重新设计（plan_802 已否决）。

**4. 推荐：** 用 `openvla/openvla-7b-finetuned-libero-object` 作为论文 baseline 对比。RTX 4090 可跑，~16GB 显存。如果只需报告数字，直接引用官方 88.4% 即可。

---
