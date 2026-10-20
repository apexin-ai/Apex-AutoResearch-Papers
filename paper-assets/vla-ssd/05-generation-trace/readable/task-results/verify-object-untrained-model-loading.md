# verify object untrained model loading

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_object_untrained_model_loading_20260521T105953_result.json`
- **Structured JSON:** [`4b1ecb30205c11602445.json`](../../sessions/4b/4b1ecb30205c11602445.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**(A) 脚本加载了正确的 untrained model，openvla-7b 本身已有 VLA 预训练 routing。**

### 证据

**1. 脚本路径正确**
- Line 28: `TRAINED_CKPT = ".../openvla-7b-finetuned-libero-object"`
- Line 29: `UNTRAINED_CKPT = ".../openvla-7b"`
- Line 529: `untrained` 条件走 `UNTRAINED_CKPT`，无误。

**2. 日志确认加载了 openvla-7b（非 finetuned）**
- 日志第一行：`Output: /root/autodl-tmp/vla-ssd/results/libero_object_untrained`
- 加载了 **3 个 shard**（`Loading checkpoint shards: 0/3 → 3/3`）
- `openvla-7b/` 目录有 **3 个** safetensors 文件（~14.9GB）
- `openvla-7b-finetuned-libero-object/` 有 **4 个** safetensors 文件（~15.1GB）
- shard 数量匹配 → 加载的确实是 base model。

**3. openvla-7b 不是 raw Llama-2-7B，是 OXE 预训练过的 VLA**
- `config.json` 关键字段：
  - `"model_type": "openvla"`
  - `"architectures": ["OpenVLAForActionPrediction"]`
  - `"hf_llm_id": "meta-llama/Llama-2-7b-hf"`（骨干，但已封装为 VLA）
  - `"n_action_bins": 256`（action tokenization）
  - `"vision_backbone_id": "dinosiglip-vit-so-224px"`（双 vision encoder）
  - `"norm_stats"` 包含几十个 OXE 数据集的统计量（austin_buds, austin_sailor, viola 等）

### 解释 L1=24/32 与 Goal untrained 0/32 的矛盾

**不矛盾。** 两个 "untrained" 的含义不同：

- **Object untrained (openvla-7b)**：在 970K+ OXE 机器人轨迹上预训练过的 VLA base model。已经学会了 instruction-conditioned action routing。L1=24/32 instruction-dominant 是 OXE 预训练建立的 routing pattern，合理。
- **Goal untrained (0/32)**：如果那个实验用的是真正的 random init 或纯语言模型，0/32 也合理——没见过 action data，不会有 instruction-action routing。

**不是 bug，是两个实验的 "untrained baseline" 定义不同。** 需要确认 Goal untrained 用的是哪个 checkpoint——如果也是 `openvla-7b`，那 0/32 反而可疑；如果是 raw Llama-2，那两边结果都合理。

---
