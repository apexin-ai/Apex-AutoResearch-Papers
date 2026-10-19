# setup download gemma4 e4b

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_download_gemma4_e4b_20260522T120049_result.json`
- **Structured JSON:** [`71d74f21a1e44b8a2952.json`](../../sessions/71/71d74f21a1e44b8a2952.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## Gemma-4-E4B-it 下载结果

### 1. Model ID
**`google/gemma-4-E4B-it`**（via ModelScope: `google/gemma-4-E4B-it`）

### 2. 下载状态
**成功** — 15GB，耗时 15 分钟（ModelScope CDN，不开 network_turbo 代理）

文件路径：`/root/autodl-tmp/models/gemma4_e4b_it/google/gemma-4-E4B-it/`

### 3. 模型规格
| 属性 | 值 |
|------|------|
| 架构 | `Gemma4ForConditionalGeneration`（多模态：text + vision + audio） |
| Text layers | 42（35 sliding_attention + 7 full_attention） |
| hidden_size | 2560 |
| num_attention_heads | 8 |
| num_key_value_heads | 2 |
| head_dim | 256 (sliding) / 512 (global) |
| intermediate_size | 10240 |
| MoE | 否（`enable_moe_block: false`） |
| max_position_embeddings | 131072 |
| sliding_window | 512 |
| vocab_size | 262144 |
| Vision layers | 16 (hidden_size=768, patch_size=16) |
| Audio layers | 12 (hidden_size=1024) |
| dtype | bfloat16 |
| 模型文件 | 单文件 `model.safetensors`（14.9GB） |

### 4. Thinking Token 格式
- `think_token`: `<|think|>`
- 实际 thinking 通过 channel 机制实现：`<|channel>thought\n{thinking_content}&lt;channel|>`
- 解析 regex: `(\<\|channel\>thought\n(?P&lt;thinking>.*?)\&lt;channel\|\>)?`

---
