# research lerobot libero recipes

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lerobot-libero-recipes_20260513T094527_result.json`
- **Structured JSON:** [`893f14ca9098b8726750.json`](../../sessions/89/893f14ca9098b8726750.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/smolvla-libero-finetune-survey.md`。核心结论：

### 1. SmolVLA Fine-tuning 官方方式
- `lerobot-train --policy.path=lerobot/smolvla_base --dataset.repo_id=HuggingFaceVLA/libero`
- 支持 full fine-tune（仅 action expert, VLM frozen）和 LoRA
- 官方文档: https://huggingface.co/docs/lerobot/smolvla

### 2. LIBERO 数据
**不需要自己转换**。Hub 上已有 `HuggingFaceVLA/libero`（273k frames, 4 suites），直接用。LIBERO-90 用 `IPEC-COMMUNITY/libero_90_no_noops_lerobot`。

### 3. Action Dim 6→7
**自动处理**。SmolVLA 内部 pad 到 `max_action_dim=32`，fine-tune 时从数据集推断 `action.shape=[7]`、`state.shape=[8]`。加 `--policy.output_features=null --policy.input_features=null` 让 trainer 自动推断。

### 4. 现成 Checkpoint
- **`lerobot/smolvla_libero`** — SmolVLA 已 fine-tuned on LIBERO，可直接用
- `lerobot/pi05_libero_finetuned` — π0.5, 97.5% avg
- `moojink/openvla-7b-oft-finetuned-libero-*` — OpenVLA-OFT, 97.1% avg
- `nvidia/Cosmos-Policy-LIBERO-Predict2-2B` — SOTA 98.5%

### 5. 推荐方案
先验证 `lerobot/smolvla_libero` 是否满足需求。如需自己训练，在 4090 上用 batch_size=8-16、100k steps、bfloat16 即可跑通。

---
