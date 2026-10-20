# eval qwen3 baseline ppl

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen3_baseline_ppl_20260515T214738_result.json`
- **Structured JSON:** [`32a080af182dd733e28f.json`](../../sessions/32/32a080af182dd733e28f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总结果：

---

## 子任务 1: Baseline PPL

| 指标 | 值 |
|---|---|
| **eval_loss** | 3.1340 |
| **Perplexity** | 22.9654 |
| **eval_tokens** | 4,077,068 |
| eval 时间 | 249s |
| 配置 | max_length=2048, stride=1024, fp16 autocast, max_docs=5000 |

## 子任务 2: 权重真实性验证

**结论：确认为标准 HuggingFace 预训练权重，非随机初始化。**

证据：
- **文件**: model.safetensors, 1.5GB, 751,632,384 参数, 311 tensors
- **SHA256**: `f47f71177f32bcd101b7573ec9171e6a57f4f4d31148d38e382306f42996874b`
- **非符号链接**
- **Config**: Qwen3ForCausalLM, 28层, hidden_size=1024, tie_word_embeddings=true
- **权重分布**（pretrained 特征）:
  - 权重矩阵 std 小且紧凑（0.023~0.037），非 uniform random init
  - LayerNorm 随层深度变化（layer 0 mean=0.175 vs layer 14 mean=1.930），random init 时所有 layernorm 为 1.0
  - lm_head 和 embed_tokens 统计完全一致（tie_word_embeddings 生效）

## Continued Pretraining 提升

| Checkpoint | Loss | PPL |
|---|---|---|
| **Baseline (原始 Qwen3-0.6B)** | 3.1340 | **22.97** |
| ess_only_seed456 (训练后) | 2.8746 | **17.72** |
| **提升幅度** | -0.2594 | **-22.8%** |

Baseline PPL=22.97 远高于训练后的 17.72，确认 continued pretraining 带来了显著提升。已注册为 `baseline_qwen3_0.6b` 实验。

---
