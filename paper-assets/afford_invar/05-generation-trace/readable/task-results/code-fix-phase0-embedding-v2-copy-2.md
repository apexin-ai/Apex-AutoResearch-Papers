# code fix phase0 embedding v2

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-phase0-embedding-v2_20260519T180010_result.json`
- **Structured JSON:** [`269011bc0556e6fdf74f.json`](../../sessions/26/269011bc0556e6fdf74f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。总结修改和测试结果：

---

## 修改内容

### 1. `diversity_metrics.py` — 核心修改
- **替换 SigLIP 方案为 LLM token embedding 方案**：OpenVLA 权重中没有独立的 SigLIP text encoder，但 `lm_head.weight` 在 shard 3 中可用。用 `safetensors` 直接加载 `lm_head.weight` → tokenize → mean pooling → L2 normalize，作为 `openvla_embed_sim`（主指标）
- **修复 nltk.download 阻塞**：新增 `_ensure_nltk_data()` 函数，先用 `nltk.data.find()` 检查数据是否存在，仅在缺失时下载
- **MiniLM / NLI 改为 optional**：加 try/except，模型不可用时 gracefully 跳过，不阻塞整个 pipeline
- **`--model-path` 默认值**恢复为 `/root/autodl-tmp/openvla-7b`

### 2. `run_phase0.py` — 同步修改
- 替换 `nltk.download()` 为 `from diversity_metrics import _ensure_nltk_data`

### 3. `tier_classifier.py` — 无需修改
- 已正确实现 `_pick_embed_key()`：优先用 `openvla_embed_sim`，fallback 到 `minilm_embed_sim`

## OpenVLA text encoder 实现方式

**LLM token embedding (lm_head.weight)**，不是 SigLIP。原因：
- OpenVLA 基于 Prismatic VLM，text 经 Llama-2 LLM 处理
- SigLIP 仅用作 vision backbone，权重中无 SigLIP text encoder
- `embed_tokens.weight` 在 shard 1（缺失），`lm_head.weight` 在 shard 3（存在）→ fallback 成功
- shape=[32064, 4096], dtype=bfloat16

## Dummy 测试结果

```
Primary embedding model: openvla_lm_head
  openvla_embed_sim:  mean=0.9624  std=0.0136  [0.9375, 0.9769]
  minilm_embed_sim:   mean=0.7104  std=0.1589  [0.5028, 0.9279]

Tier Classification (openvla_embed_sim):
  Tier-1 (trivial):   4  (80.0%)
  Tier-2 (moderate):  1  (20.0%)  — "lift the crimson mug from the desk surface" (sim=0.938)
  Tier-3 (deep):      0  (0.0%)
```

OpenVLA 和 MiniLM 距离分布差异显著：OpenVLA token embedding 的 sim 集中在 0.93-0.98（高相似），MiniLM 的 sim 分布更宽（0.50-0.93）。Tier 阈值 0.95/0.80 在 OpenVLA 空间中仍然合理——"lift the crimson mug" 这类用完全不同词汇表达的 paraphrase 被正确分到 Tier-2。

**注意**: `embed_tokens.weight` (shard 1) 缺失，当前用 `lm_head.weight` 替代。如果后续补全 shard 1，代码会自动优先使用 `embed_tokens`。

---
