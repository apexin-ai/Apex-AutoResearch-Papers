# code fix phase0 embedding v2

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-phase0-embedding-v2_20260519T194639_result.json`
- **Structured JSON:** [`596cfbb8149a06842214.json`](../../sessions/59/596cfbb8149a06842214.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline fully verified. Let me summarize the results.

---

## 结果

**代码已完全实现，无需修改。** 三个脚本均已支持 OpenVLA text encoder (SigLIP)。

### 实现方式
- **SigLIP text encoder**：从 `/root/autodl-tmp/siglip-base-local` 加载独立 SigLIP 模型（`SiglipTextModel`, 110.3M params）
- `compute_openvla_embedding_metrics()` 检测 model_type → OpenVLA 路径自动路由到 siglip-base-local
- `tier_classifier.py` 的 `_pick_embed_key()` 优先使用 `openvla_embed_sim`

### Dummy 测试结果（10 paraphrases, 2 tasks）

| 指标 | 值 |
|------|-----|
| primary_embed_model | `siglip_text_encoder` |
| embed_model_used | `openvla_embed_sim` |
| Tier-1 (trivial, >0.95) | 0 (0%) |
| Tier-2 (moderate, 0.80-0.95) | 7 (70%) |
| Tier-3 (deep, <0.80) | 3 (30%) |
| Tier-2+ total | 100% |

示例 tier 分配：
- "grab the red cup off the table" → sim=0.906, **Tier-2** (近义替换)
- "lift the crimson mug from the desk surface" → sim=0.664, **Tier-3** (词汇+语义重构)
- "slide open the highest drawer in the storage unit" → sim=0.780, **Tier-3**

### 资源使用
- SigLIP text encoder 在 CPU 运行，~950MB RSS，0 GPU VRAM
- 无需加载 7B 模型

### 注意
- MiniLM/NLI 模型需要 `source /etc/network_turbo` + `HF_ENDPOINT=https://hf-mirror.com` 才能下载，已缓存到本地
- 后续运行如果网络不通，`sentence_transformers` 会卡在 HEAD 请求重试上（最终仍能 fallback 到本地缓存，但耗时较长）

---
