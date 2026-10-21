# analysis lora param percentage

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lora-param-percentage_20260521T174458_result.json`
- **Structured JSON:** [`230ea4fecfd7cc9f30f4.json`](../../sessions/23/230ea4fecfd7cc9f30f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All architecture parameters collected. Now let me compute.

**Architecture summary from configs:**

| Model | d | d_ff | Layers | n_heads | n_kv_heads | head_dim | d_kv | vocab | tie_embed |
|---|---|---|---|---|---|---|---|---|---|
| Qwen2.5-7B | 3584 | 18944 | 28 | 28 | 4 | 128 | 512 | 152064 | false |
| Qwen2.5-14B | 5120 | 13824 | 48 | 40 | 8 | 128 | 1024 | 152064 | false |
| Gemma-2-9B | 3584 | 14336 | 42 | 16 | 8 | 256 | 2048 | 256000 | true |
| OLMo-2-7B | 4096 | 11008 | 32 | 32 | 32 | 128 | 4096 | 100352 | true |
| Phi-4 | 5120 | 17920 | 40 | 40 | 10 | 128 | 1280 | 100352 | false |
| LLaMA-3.1-8B | 4096 | 14336 | 32 | 32 | 8 | 128 | 1024 | 128256 | false |

**LoRA r=16, target_modules = [q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj]**

For each module, LoRA params = r × (in_features + out_features):

Per layer LoRA = r × Σ(in_i + out_i) across 7 modules:
- q: (d + d_q), k: (d + d_kv), v: (d + d_kv), o: (d_q + d)
- gate: (d + d_ff), up: (d + d_ff), down: (d_ff + d)

Total LoRA = num_layers × per_layer

| Model | Total Params | Per-layer sum | LoRA Params (r=16) | Trainable % |
|-------|-------------|--------------|-------------------|-------------|
| Qwen2.5-7B | 7,616,086,528 (7.62B) | 90,112 | 40,370,176 (40.4M) | 0.530% |
| Qwen2.5-14B | 14,769,689,600 (14.77B) | 89,600 | 68,812,800 (68.8M) | 0.466% |
| Gemma-2-9B | 9,241,705,984 (9.24B) | 80,384 | 54,018,048 (54.0M) | 0.585% |
| OLMo-2-7B | 6,887,575,552 (6.89B) | 78,080 | 39,976,960 (40.0M) | 0.580% |
| Phi-4 | ~14,659,814,400 (14.66B) | 102,400 | 65,536,000 (65.5M) | 0.447% |
| LLaMA-3.1-8B | 8,030,261,248 (8.03B) | 81,920 | 41,943,040 (41.9M) | 0.522% |

**计算细节（以 Qwen2.5-7B 为例）：**
- d_kv = 4 × 128 = 512 (GQA, 4 KV heads)
- Per-layer sum = (3584+3584) + (3584+512) + (3584+512) + (3584+3584) + (3584+18944) + (3584+18944) + (18944+3584) = 90,112
- Per-layer LoRA = 16 × 90,112 = 1,441,792
- Total LoRA = 28 layers × 1,441,792 = 40,370,176

**注意：**
- Gemma-2-9B 的 head_dim=256（显式设置，非 d/n_heads=224），导致 d_q=4096 ≠ d=3584
- OLMo-2-7B 使用 MHA（n_kv=n_heads=32），k/v 不压缩，trainable % 较高
- Phi-4 实际使用 fused qkv_proj + gate_up_proj，若用 fused LoRA 则参数量为 55.7M (0.380%)，上表按概念等价的 7 个独立模块计算
- 总参数数从 config 手动计算（含 embedding/LM head/LayerNorm），与 HuggingFace 报告值一致

---
