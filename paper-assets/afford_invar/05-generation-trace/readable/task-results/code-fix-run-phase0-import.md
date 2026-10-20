# code fix run phase0 import

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-run-phase0-import_20260519T184808_result.json`
- **Structured JSON:** [`802641e5a17c84faeb55.json`](../../sessions/80/802641e5a17c84faeb55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改和验证完成。

---

### 修改总结

**修改的文件：**

1. **`run_phase0.py`**（Bug 1 修复）
   - 第 22 行：`from diversity_metrics import run_diversity_metrics, _ensure_nltk_data` → `from diversity_metrics import run_diversity_metrics`
   - 第 73-75 行：`_ensure_nltk_data()` 替换为内联 `nltk.download("punkt"/"punkt_tab")`

2. **`diversity_metrics.py`**（Bug 2 修复）
   - 新增 `_detect_model_type()` — 读 config.json 判断模型类型
   - 新增 `_siglip_text_embeddings()` — SigLIP text encoder embedding
   - 新增 `_llm_embed_tokens()` — 从 OpenVLA safetensors 提取 Llama-2 embed_tokens + mean pooling（回退方案）
   - 重写 `compute_openvla_embedding_metrics()` — 自动分发：
     - SigLIP 模型 → 直接用 SiglipTextModel
     - OpenVLA 模型 → 优先用 `/root/autodl-tmp/siglip-base-local`（SigLIP text encoder），否则回退到 LLM embed_tokens
   - `--model-path` 默认值改为 `/root/autodl-tmp/openvla-7b`

3. **`tier_classifier.py`** — 无需修改，已正确使用 `openvla_embed_sim` 优先 + 阈值 0.95/0.80

**OpenVLA text encoder 实现方式：** OpenVLA 基于 Prismatic VLM，SigLIP 仅用作 vision encoder，text 部分是 Llama-2-7b。方案为加载独立的 SigLIP text encoder（`siglip-base-local`），与 OpenVLA 训练时使用的 vision-language alignment 空间一致。

**验证结果：**
- `from run_phase0 import *` → `import OK`
- `--help` 两个脚本均通过
- 端到端 dummy 测试：SigLIP embedding 正常计算，tier 分类使用 `openvla_embed_sim`，5 条 paraphrase 分布为 Tier-2 60% + Tier-3 40%（Tier-2+ = 100%）

---
